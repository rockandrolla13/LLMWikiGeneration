_Journal of Financial Econometrics_ , 2026, **24(3)** , nbag006 https://doi.org/10.1093/jjfinec/nbag006 **Article** 

## **Multifactor Timing with Deep Learning Paul Cotturo[1] , Fred Liu[2,3,] and Robert Proner[3,4]** 

1Department of Statistics and Actuarial Science, University of Waterloo, Waterloo, ON N2L3G1, Canada 

2Department of Economics and Finance, University of Guelph, Guelph, ON N1G2W1, Canada 

3Department of Economics, University of Western Ontario, London, ON N6A3K7, Canada 

4Department of Economics, University of Toronto, Toronto, ON M5S1A1, Canada Address correspondence to Fred Liu, Department of Economics and Finance, University of Guelph, 50 Stone Rd E, Guelph, ON N1G2W1, Canada, or e-mail: fred.liu@uoguelph.ca. 

## **Abstract** 

**We develop deep neural networks with economically motivated restrictions that are designed to overcome the main challenges of factor timing. Our critical innovations include integrating multitask (MT) learning to capture the common structure across factors, with long short-term memory neural networks to extract financial and macroeconomic states. This dynamic MT neural network outperforms all benchmarks in terms of predictive accuracy and economic gains. We pinpoint unemployment, along with variations on leverage, profitability, and money as key predictors, and highlight the importance of capturing their nonlinear interactions. Improved factor timing through neural networks with economic restrictions facilitates more reliable investigation into the economic mechanisms driving factor risk premia, and underscores the value of deep learning for factor investing.** 

**Key words** factor timing, deep learning, economic structure, machine learning, dynamic multitask neural networks, big data 

**JEL classifications** G10, G11, G12, G17, C14, C22, C45, C58 

Factors in the cross-section of stock returns are persistent sources of risk premia (Fama and French 1993), forming the basis for factor investing. Factors such as value and momentum deliver high returns over the long run, but can underperform in the short run, creating the opportunity for investors to engage in factor timing. Many investors use multifactor portfolio strategies that buy factor portfolios expected to outperform and sell factor portfolios expected to underperform, which raises several interesting questions. First, can we predict the probability of a factor outperforming or underperforming? Second, what is the economic significance of these predictions? Third, which variables are more influential for factor timing, and do their nonlinear interactions matter? This paper is dedicated to answering these questions, consequently enabling a more reliable investigation into the economic mechanisms that drive factor risk premia. 

There are four major challenges of factor timing that the literature so far has struggled to overcome in a unified framework. First, factor risk premia are a function of many financial and macroeconomic variables (Bender et al. 2018; Dong et al. 2022). Second, the functional form linking predictors to factor risk premia is unknown and likely complex, depending on nonlinear interactions among the 

We are grateful to the Editor (Fabio Trojani) and two anonymous referees for their insightful and detailed comments that substantially improved the paper. 

**Received:** March 22, 2024. **Revised:** December 31, 2025. **Accepted:** February 16, 2026 © The Author(s) 2026. Published by Oxford University Press. 

This is an Open Access article distributed under the terms of the Creative Commons Attribution-NonCommercial License (https://creativecommons.org/ licenses/by-nc/4.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited. For commercial re-use, please contact reprints@oup.com for reprints and translation rights for reprints. All other permissions can be obtained through our RightsLink service via the Permissions link on the article page on our site—for further information please contact journals.permissions@oup.com. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**2** 

variables (Gu, Kelly, and Xiu 2020; Didisheim et al. 2024; Kelly, Malamud, and Zhou 2024). Third, factor risk premia are time-varying and depend on macroeconomic and financial conditions (Hodges et al. 2017; Polk, Haghbin, and de Longis 2020; Ilmanen et al. 2021). Fourth, factor returns exhibit a lowdimensional common structure, which can be exploited to improve factor timing (Haddad, Kozak, and Santosh 2020; Kagkadis et al. 2024). While the literature has largely used linear models that can address some of these challenges, none of these models, to our knowledge, can overcome all of them. As a result, the fundamental question concerning the feasibility of factor timing remains contentious (Asness 2016; Asness et al. 2017; Dichtl et al. 2019). 

In this paper, we introduce a deep learning approach for factor timing that addresses the aforementioned challenges by incorporating economically motivated restrictions. Since factor timing is fundamentally a prediction problem, employing neural networks is a natural choice, as they excel at handling a large number of variables and complex functional forms. However, most off-the-shelf neural networks are designed for prediction tasks in static environments with high signal-to-noise ratios and a large number of observations. In contrast, factor risk premia are time-varying, exhibit low signal-to-noise ratios, and are observed over relatively short historical samples, leading off-the-shelf neural networks to overfit. Hence, economic restrictions play a crucial role in regularization and are essential for improving the out-of-sample predictive accuracy of neural networks. 

This paper demonstrates how to improve deep learning models for factor timing by incorporating economic structure. Our crucial innovation is to develop a multitask (MT) neural network architecture that jointly predicts risk premia across multiple factors within a single functional form. MT learns common latent variables across factors and also uses factor-specific layers to capture each factor’s nonlinear exposures to these latent variables. This economic restriction offers two main benefits that improve the model’s out-of-sample generalizability. First, MT incorporates the economic restriction that risk premia across factors stem from a low-dimensional set of common latent variables, which allows the model to capture commonalities among factors and improves performance. This shared representation has been shown to enhance data efficiency (Caruana 1997), which is critical for applying deep learning to the limited historical observations available for estimating factor risk premia. In contrast, single-factor models are unable to leverage the low-dimensional common structure across factors, which renders them susceptible to overfitting on factor-specific noise. Second, multitask learning (MTL) acts as a regularization technique that compels MT to generalize across multiple outputs (Ruder 2017), thereby preventing overfitting to the noise of a single factor. This regularization is particularly important given the low signal-to-noise ratios of factor risk premia, exacerbated by relatively short historical samples. 

Furthermore, we incorporate a high-dimensional set of variables and capture the time variation in factor risk premia as a function of macroeconomic and financial conditions using two separate recurrent long short-term memory neural networks (LSTMs), which perform dimension reduction and extract time-series dynamics. The first LSTM takes in a large number of macroeconomic time series as inputs, and summarizes their dynamics into a small number of macroeconomic state processes; while the second LSTM takes in a large number of financial time series as inputs, and summarizes their dynamics into a small number of financial state processes. Chen, Pelger, and Zhu (2024) demonstrate that LSTMs can detect cycles, hence our LSTMs are designed to capture business and financial cycles. The economic restriction of separately modeling the macroeconomic and financial cycle dynamics generally reduces the number of parameters, and thus further enhances the neural network’s out-of-sample performance. Augmenting the MT architecture with LSTMs gives rise to the dynamic multitask (DMT) neural network model to address all four major challenges of factor timing. 

In our baseline analysis, we study five well-known factor portfolios over 57 years from January 1965 to December 2021: size factor, Small Minus Big (SMB); value factor, High Minus Low (HML); profitability factor, Robust Minus Weak (RMW); and investment factor, Conservative Minus Aggressive (CMA) from Fama and French (2015), and momentum (MOM). Our predictors consist of 259 variables, including 122 macroeconomic variables from McCracken and Ng (2016), and 137 financial variables from Chen and Zimmermann (2022). In each month, we condition on these predictors to forecast the probability that each factor portfolio return is positive. We compare MT and DMT, which predict the probabilities of all factor portfolios in a single functional form, against off-the-shelf models that 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**3** 

estimate a separate functional form for each factor. These off-the-shelf classification models include logistic regression (LR), logistic regression with the elastic net penalty (EN), random forest (RF), gradient boosted trees (GBT), support vector machine (SVM), feed-forward neural network (NN), and LSTM. 

Our results advance the knowledge on factor timing in three main dimensions. First, we assess the predictive power of the different models for factor timing using the out-of-sample classification accuracy metric, defined as the proportion of correctly classified return signs in the out-of-sample period from January 1990 to December 2021. We show that economic restrictions matter for the average accuracy across factor portfolios. Linear models, LR and EN, achieve accuracies of 53.1% and 53.3%, respectively, underperforming the 53.5% accuracy of the buy-and-hold (BUY) benchmark, which always predicts a positive return. Nonlinear tree-based models, RF and GBT, improve accuracy to 55.6% and 54.8%, respectively. In contrast, SVM, NN, and LSTM exhibit lower accuracies of 53.1%, 53.8%, and 53.8%, respectively, suggestive of overfitting to factor-specific noise. Imposing an economically motivated common structure across factors through MT raises accuracy to 55.4%, reflecting the regularization and data-efficiency benefits of MTL. Moreover, by incorporating time-series dynamics alongside this common structure, DMT delivers the highest average accuracy of 56.4%. 

Second, we study whether factor timing using machine learning models can be exploited in an economically significant trading strategy. We employ a strategy that takes a long position in a factor portfolio when the model predicts a positive return and exits the position otherwise. Our multifactor strategy is then an equal-weighted (EW) portfolio of these strategy returns across all factor portfolios. We find that economic performance mostly aligns with average predictive accuracy. Linear models, LR and EN, deliver low Sharpe ratios of 0.61 and 0.52, respectively. Static nonlinear models, RF, GBT, SVM, and NN, generally achieve higher Sharpe ratios ranging from 0.61 to 0.67. Imposing a common structure across factors through MT further raises the Sharpe ratio to 0.69. Incorporating time-series dynamics with LSTM increases the Sharpe ratio to 0.76, while combining economic structure and dynamics in DMT yields the highest Sharpe ratio of 0.82 and the highest alpha of 1.4% ( _t_ -statistic of 3.05), substantially outperforming the multifactor BUY benchmark, which attains a Sharpe ratio of 0.60. Even after accounting for transaction costs of 14 basis points, DMT maintains strong performance, with a Sharpe ratio of 0.74 and an alpha of 1.01% ( _t_ -statistic of 2.21). Moreover, we find substantial heterogeneity in predictability across factor portfolios, consistent with Neuhierl et al. (2023). 

Third, we quantify the importance of different predictors for multifactor timing using Shapley values, which measure changes in model predictions when individual predictors are excluded from estimation. Models largely agree on the most influential predictors for multifactor timing, which differ substantially from the predictors of individual stock risk premia documented in Gu et al. (2020). Among macroeconomic variables, unemployment emerges as the single most influential predictor, while money variables, such as reserves of depository institutions, constitute the most important macroeconomic category. Among financial variables, predictors in the leverage category, such as industry concentration, are particularly influential. We also document substantial heterogeneity in predictor importance across factors, consistent with Neuhierl et al. (2023). Despite this heterogeneity, leverage, profitability, and money consistently rank among the most influential categories, suggesting that they help drive the common structure across factors. In addition, predictor importance varies meaningfully over time. Finally, we show that DMT captures rich pairwise nonlinear interactions for each factor, highlighting that its superior performance stems from its ability to model complex nonlinear functional forms. 

We further extend the response variables to a broader set of 149 factor portfolios from Jensen, Kelly, and Pedersen (2023) (henceforth JKP) to assess the generalizability of our findings. We adapt DMT to jointly estimate the conditional probabilities of all JKP factor portfolios within a single functional form, thereby imposing a common structure across all 149 factors. The results closely mirror the baseline findings. DMT achieves the highest average accuracy of 53.8%, outperforming the BUY benchmark accuracy of 52.8%. It also delivers the highest multifactor Sharpe ratio of 0.88, well above the multifactor BUY Sharpe ratio of 0.63. Long–short quintile portfolios formed on DMT forecasts likewise exhibit the strongest economic performance. Together, these results demonstrate the scalability and robustness of DMT. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**4** 

The rest of the paper is organized as follows. Section 1 reviews the related literature. Section 2 details the data, methodology, and estimation procedure. Section 3 presents the baseline results. Section 4 reports additional analysis using the JKP factors. Finally, Section 5 offers concluding remarks. 

## **1 Related literature** 

In this paper, we develop economically motivated deep learning models for factor timing, contributing to at least two existing strands of literature. First, we build upon the extensive literature that investigates factor predictability through linear models. Market predictability is a central topic in financial economics. The comprehensive reviews by Koijen and Van Nieuwerburgh (2011) and Rapach and Zhou (2013) underscore the depth and breadth of research in this domain. Various papers extend the ideas of market predictability to specific factors. For example, the predictability of the value factor is explored by Baba Yara, Boons, and Tamoni (2021) and Cohen, Polk, and Vuolteenaho (2003). Similarly, the predictability of the momentum factor is studied in Cooper, Gutierrez Jr, and Hameed (2004) and Daniel and Moskowitz (2016). Furthermore, Asness, Moskowitz, and Pedersen (2013) and Polk, Vayanos, and Woolley (2022) focus on both the value and momentum factors, whereas Kelly, Moskowitz, and Pruitt (2021) study momentum and reversal. 

A growing literature examines multifactor predictability. Greenwood and Hanson (2012) employ corporate share issuance to predict multiple factor returns. Kelly and Pruitt (2013) predict the value, size, and momentum factors using valuation ratios. Moreira and Muir (2017) adopt volatility approaches for multifactor timing. Haddad, Kozak, and Santosh (2020), Kagkadis et al. (2024), Kelly, Malamud, and Pedersen (2023), and Neuhierl et al. (2023) harness dimension reduction techniques for their factor predictions. Furthermore, Gupta and Kelly (2019) and Moskowitz, Ooi, and Pedersen (2012) document factor momentum. A common theme among these studies is their reliance on linear models and a lack of time-series dynamics. In contrast, we introduce the DMT model that captures time-series dynamics, a wide range of predictors, nonlinear interactions, and commonalities across factor risk premia. 

Second, we contribute to the rapidly expanding literature that uses off-the-shelf machine learning techniques to forecast stock returns. In their seminal work, Gu, Kelly, and Xiu (2020) employ an extensive array of off-the-shelf machine learning techniques to forecast individual stock and factor returns.[1] We benchmark our analysis against their top-performing model based on a deep neural network with three hidden layers. Our findings demonstrate that incorporating a common structure across factors together with time-series dynamics yields superior predictions compared to off-theshelf models. 

A few papers study factor predictability using nonlinear machine learning models. Kelly, Malamud, and Zhou (2024) develop a theoretical framework highlighting the “Virtues of Complexity,” showing that strategy Sharpe ratios can increase with model complexity, and provide empirical evidence that nonlinear machine-learning models can effectively forecast the market factor. Kelly, Malamud, and Zhou (2022) extend this framework to a broader set of factor portfolios and other complex asset classes, documenting empirical results that are consistent with the theoretical predictions in Kelly, Malamud, and Zhou (2024). 

Several recent papers introduce machine learning models with economic restrictions to improve forecasts. Aleti and Bollerslev (2025), Bryzgalova, Pelger, and Zhu (2025), Chen, Pelger, and Zhu (2024), Feng et al. (2024), Gu, Kelly, and Xiu (2021), and Kozak, Nagel, and Santosh (2020) impose no-arbitrage restrictions when predicting individual stock returns. Guijarro-Ordonez, Pelger, and Zanotti (2025) 

> 1 Other papers that employ off-the-shelf machine learning techniques to forecast stock returns include Aleti, Bollerslev, and Siggaard (2025), Chinco, Clark-Joseph, and Ye (2019), Choi, Jiang, and Zhang (2025), Freyberger, Neuhierl, and Weber (2020), Huddleston, Liu, and Stentoft (2023), Leippold, Wang, and Zhou (2022), and Liu and Stentoft (2023). 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**5** 

develop a deep learning approach for statistical arbitrage. Liu (2025) develops multitask neural networks that incorporate an economic restriction based on a common structure across return quantiles, which enhances the accuracy of quantile forecasts, resulting in significant statistical and economic gains. Proner (2023) introduces DMT neural networks that jointly forecast inflation and unemployment, incorporating an economic restriction that is motivated by the Phillips Curve. Our paper complements this literature by developing a deep learning framework with economically motivated restrictions that directly addresses the four main challenges of factor timing. 

## **2 Data, methodology, and estimation procedure** 

## **2.1 Data** 

In our baseline analysis presented in Section 3, our factor sample spans January 1965 to December 2021, totaling 57 years. We use five monthly factor portfolios from Kenneth French’s data library as response variables: SMB, HML, RMW, CMA, and MOM. The first four correspond to the size, value, profitability, and investment factors from Fama and French (2015), while the fifth factor, momentum, goes long past winners and short past losers. We focus on these factors because they are used extensively in the academic literature and by practitioners (e.g., for measuring risk-adjusted investment performance). As further analysis documented in Section 4, we also forecast the much broader set of factor portfolios from Jensen, Kelly, and Pedersen (2023) spanning from March 1969 to December 2021.[2] We deliberately exclude the market factor portfolio to ensure our results are not driven by market timing, as prior research demonstrates that nonlinear machine learning models can effectively time the market (e.g., Kelly, Malamud, and Zhou 2024).[3] 

As macroeconomic predictors, we include variables from the FRED-MD database, as detailed in McCracken and Ng (2016), covering categories such as labor, money, output, and inflation. We apply their transformations to generate stationary time series. Following Bianchi, Buchner, and Tamoni € (2021) and Chen, Pelger, and Zhu (2024), we lag the macroeconomic variables by one additional month (i.e., we use the observation at _t −_ 1) to account for announcement delays. 

As financial predictors, we include long–short anomaly portfolio returns. This choice is motivated by Dong et al. (2022), who theoretically and empirically show that long–short anomaly portfolio returns predict the market factor. We employ the anomalies detailed in Chen and Zimmermann (2022) and categorize them loosely following Gu, Kelly, and Xiu (2020) and Jensen, Kelly, and Pedersen (2023), spanning investment, leverage, liquidity, price trend, profitability, quality, risk, and value.[4] 

The macroeconomic and financial datasets contain predictors with substantial missing values.[5] Imputing these missing values can introduce considerable noise, particularly when gaps are large. To address this issue, we exclude predictors with any missing values before 1990, corresponding to the beginning of our out-of-sample period, and impute the remaining missing values with the expanding training set mean. This procedure yields 122 macroeconomic predictors and 137 financial predictors.[6] Supplementary Tables IA2 and IA3 provide a descriptive list of these macroeconomic and financial predictors. 

> 2 Our sample begins in March 1969. We exclude four factors (eqnetis_at, eqnpo_me, eqpo_me, netis_at) that are not available at this start date, leaving 149 factors as response variables. The monthly data are available at www.jkpfactors.com. We adopt the capped value-weighted factors used in their main specification. We thank the authors for making the data available. 

> 3 In an earlier draft of the paper, we included the market factor and obtained similar conclusions. We thank an anony4 mous reviewer for suggesting this exclusion.The monthly data are available at www.openassetpricing.com. We use the August 2023 release. We thank the authors 

> 5 For example, the activism1 and activism2 variables from for making the data available. Chen and Zimmermann (2022) are missing until October 1990. 

> 6 The FRED-MD database contains 126 variables; therefore, our filtering criteria exclude 126 _−_ 122 ¼ 4 macroeconomic variables, such as the Trade Weighted U.S. Dollar Index. Similarly, the August 2023 release of Chen and Zimmermann (2022) includes 212 variables; therefore, our filtering criteria exclude 212 _−_ 137 ¼ 75 financial variables, such as announcementreturn, activism1, and activism2. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**6** 

## **2.2 Methodology** 

We study factor timing by forecasting the sign of factor portfolio returns. We adopt a classification approach for factor timing for two main reasons. First, the probability prediction naturally translates into an intuitive trading strategy. Second, factor portfolio returns exhibit heavy tails (Daniel and Moskowitz 2016; Arnott et al. 2019), which can be detrimental for regression approaches but do not affect classification approaches. 

In its most general form, we describe the conditional probability that a factor portfolio earns a positive return as 

**==> picture [252 x 10] intentionally omitted <==**

where factor portfolios are indexed by _i_ ¼ 1 _;_ ... _; N_ , months by _t_ ¼ 1 _;_ ... _; T_ , and the return of factor portfolio _i_ in month _t_ þ 1 is denoted as _ri;t_ þ 1.[7] Our objective is to estimate a functional form _gi_ ð�Þ, which links the _p_ -dimensional vector of predictors _xt_ to the probability of a positive return _πi;t_ þ 1. To achieve this objective, we introduce MT neural network architectures, each of which jointly models the _πi;t_ þ 1 across all _N_ factor portfolios within a single functional form and incorporates several other economically motivated restrictions on _gi_ , which are detailed in the next sections. 

## **2.2.1 MT neural network** 

Factor returns exhibit a low-dimensional common structure. Haddad, Kozak, and Santosh (2020) and Kagkadis et al. (2024) document this by applying principal component analysis (PCA) and showing that a small number of latent variables explain the majority of the variation across a broad set of factor returns. They further show that these shared latent variables are highly predictable and that exploiting this common structure substantially improves factor timing. However, PCA is a linear technique for estimating latent variables, whereas Gu, Kelly, and Xiu (2021) show that allowing for nonlinear interactions in the latent variable estimation can significantly enhance predictive power. 

Motivated by this evidence, we develop an MT architecture that incorporates a common structure capable of capturing nonlinear interactions. Figure 1 illustrates an example of the MT architecture. The “hard sharing” hidden layers interact and nonlinearly transform the input predictors into shared latent variables, imposing an economically motivated restriction of a low-dimensional common structure across factor portfolios. The “factor-specific” layers capture nonlinear exposures to the shared latent variables, which we refer to as factor-specific loadings, and aggregate these exposures to produce the final prediction of _πi;t_ þ 1 for each factor portfolio. These factor-specific loadings can be viewed as a nonlinear analogue of PCA loadings, as they allow each factor portfolio to load flexibly on the shared latent variables. 

The MT framework employs MTL, which acts as a form of regularization that reduces overfitting to factor-specific noise, especially in low signal-to-noise environments. Joint prediction across multiple factor portfolios forces the neural network’s hard-sharing parameters to be sufficiently general to produce useful signals for most factors.[8] This simultaneous learning of related tasks, known as inductive transfer, improves generalizability, as what is learned for each factor can help other factors be learned better (Ruder 2017). Consequently, MTL increases the effective sample size by leveraging the additional information contained in the training signals of related tasks (Caruana 1997). This data efficiency property is especially valuable in monthly time-series settings, where the number of observations is small relative to the number of model parameters. 

> 7 This framework is inspired by Gu, Kelly, and Xiu (2020), who apply it to model individual stock returns in excess of the risk-free rate. In contrast, we apply the framework to factor portfolio returns, defined as the returns of a long portfolio in excess of the returns of a short portfolio. 

> 8 Incorporating a common structure does not guarantee improved predictability for every individual factor; rather, it is designed to improve the predictability of the multifactor portfolio. For example, Haddad, Kozak, and Santosh (2020) show that imposing a common structure substantially improves predictions for the size factor but performs poorly for the gross profitability factor. This evidence is consistent with the heterogeneity in factor predictability emphasized by Neuhierl et al. (2023). 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**7** 

**Figure 1** Multitask neural network architecture example. Macroeconomic and financial predictors are input into a fully connected (dense) layer, where they are nonlinearly interacted. Next, the network splits into branches to learn factor-specific loadings and predict probabilities _πi;t_ þ 1 for each factor. 

## **2.2.2 DMT neural network** 

Factor risk premia are time-varying and depend on macroeconomic and financial conditions (Hodges et al. 2017; Polk, Haghbin, and de Longis 2020; Ilmanen et al. 2021). For example, Kozak, Nagel, and Santosh (2020) show that their optimal factor timing portfolio is closely related to several proxies for business and financial conditions such as inflation and market volatility. Static models such as MT and most off-the-shelf models only incorporate predictor values in the preceding period, which is insufficient for the model to learn business and financial cycle dynamics. To address this, following Chen, Pelger, and Zhu (2024), we incorporate dynamic nonlinear dependencies using LSTMs (Hochreiter and Schmidhuber 1997). LSTMs capture complex nonlinear time-series dynamics rather than relying solely on values at time _t_ . 

The DMT architecture, illustrated in Figure 2, integrates dynamics by employing LSTMs. Given the high-dimensionality and strong cross-sectional dependence among macroeconomic and financial raw input variables, there’s overlapping information that can be captured by a low-dimensional model. Functionally, our LSTMs serve to reduce dimensionality, akin to PCA, while also extracting dynamics similar to those in state space models, within a broader nonlinear framework. By consolidating the high-dimensional raw inputs into a small number of hidden state processes, we prevent the model from overfitting on the noise specific to each macroeconomic or financial time series. Supplementary Appendix IA1.2.5 provides a detailed description of the LSTM architecture. 

While LSTMs capture time-series dynamics, they are substantially more complex than dense layers and therefore benefit from stronger regularization. Chen, Pelger, and Zhu (2024) show that directly modeling interactions among high-dimensional macroeconomic and financial raw inputs causes the model to massively overfit and perform poorly out-of-sample. They further demonstrate that regularizing the architecture by first reducing the macroeconomic variables into a small set of latent state 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**8** 

**Figure 2** Dynamic multitask neural network architecture example. Macroeconomic and financial predictors are input into the network separately and propagate through LSTM layers, where nonlinear dynamic features are constructed. These nonlinear dynamic macroeconomic and financial features are then nonlinearly interacted in a fully connected (dense) layer. Finally, the network splits into branches to learn factor-specific loadings and predict probabilities _πi;t_ þ 1 for each factor. 

variables using an LSTM, and only then interacting them with financial predictors, substantially improves predictive performance. 

Motivated by their approach, we assign separate LSTMs to the macroeconomic and financial inputs, reducing the dimensionality handled by each LSTM, which in turn provides regularization benefits. The DMT architecture therefore employs two LSTMs positioned before the first dense layer: the upper LSTM nonlinearly transforms the macroeconomic time series into a reduced set of latent macroeconomic state variables, and the lower LSTM analogously extracts latent financial state variables. This design generally reduces the number of model parameters relative to using a single LSTM on the combined predictor set, helping to mitigate overfitting. A subsequent hard-sharing layer then nonlinearly interacts the two sets of high-level hidden states, producing a low-dimensional set of shared latent variables for the DMT model. 

In addition to the regularization benefits, the separate LSTMs have meaningful economic interpretations. Chen, Pelger, and Zhu (2024) demonstrate that LSTMs have the ability to identify cyclical patterns and capture business cycle dynamics when applied to macroeconomic variables. Likewise, Dong et al. (2022) show that the predictive power of long–short anomaly portfolio returns is closely related to financial condition proxies such as aggregate liquidity, volatility, arbitrage capital costs, uncertainty, and sentiment. The LSTM applied to long–short anomaly portfolio returns can thus be viewed as capturing financial cycle dynamics. 

Separating the LSTMs to capture business and financial cycles mitigates overfitting and improves model stability, but at the cost of reduced flexibility due to restricted interactions between macroeconomic and financial raw inputs. Whether this economically motivated restriction improves performance is therefore an empirical question. To address this, we also study an alternative architecture, 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**9** 

DMTc, which mirrors DMT but _combines_ the macroeconomic and financial raw inputs into a single LSTM. 

## **2.2.3 Off-the-shelf models** 

We consider a variety of off-the-shelf machine learning models from Hastie et al. (2009) as comparative benchmarks. These models estimate a separate functional form _gi_ for each factor _i_ and can be highly susceptible to overfitting to factor-specific noise. In addition, they do not exploit the common structure across factors, and are largely static in the sense that they do not incorporate time-series dynamics. The static off-the-shelf models include linear models (LR and EN) and nonlinear models (RF, GBT, SVM, and NN). We also consider a dynamic off-the-shelf model in the form of an LSTM, which is trained separately for each factor. These models are described in detail in Supplementary Appendix IA1. 

## **2.2.4 Estimation procedure** 

To estimate the models, we use the validation set approach and divide our full sample into three disjoint time periods. For the baseline analysis presented in Section 3, we start by estimating the model parameters on a training sample of 23 years (1965–1987). We then perform an extensive hyperparameter optimization, validating the model’s fit in the next two years (1988–1989). Lastly, we assess the predictive power in the one-year testing sample (1990). We keep the models fixed for one year and replicate this procedure extending the training sample by one year in each iteration, for a total of 32 out-of-sample years (1990–2021). In the training, validation, and test sets, each predictor is standardized using the mean and variance computed from the corresponding training sample. In Section 4, we apply an analogous approach to estimate the models for the JKP factors, with the only difference being that each training sample begins in March 1969 rather than January 1965. Supplementary Appendix IA3 details the hyperparameter optimization setup, which is used for both the baseline and JKP analyses. 

## **3 Baseline results** 

## **3.1 Time-varying factor risk premia** 

Figure 3 reports cumulative returns for the five baseline factors and an EW portfolio constructed across the five factors. SMB exhibits the weakest performance, while HML performs well prior to the global financial crisis (GFC) but suffers a large postcrisis drawdown. RMW and CMA deliver similar trajectories with intermittent drawdowns, and MOM achieves the highest cumulative return despite a sharp GFC crash. In general, factors respond differently to adverse financial and macroeconomic conditions, as indicated by NBER recessions, highlighting the diversification benefits of holding multiple factors. Consistent with this, the EW portfolio attains the second-highest cumulative return while exhibiting lower volatility than the individual factors. 

Over the out-of-sample period from 1990 to 2021, the SMB, HML, RMW, CMA, and MOM factors earn annualized Sharpe ratios of 0.16, 0.11, 0.49, 0.32, and 0.34, respectively. However, the EW portfolio attains a Sharpe ratio of 0.60. This sizable improvement in the Sharpe ratio from multifactor relative to single-factor investing highlights the well-known diversification benefits across factors and motivates a multifactor framework. The subsequent sections show that multifactor timing using models with economic restrictions can further enhance both statistical and economic performance. 

## **3.2 Out-of-sample predictive power** 

We evaluate the predictive power of the machine learning models using the out-of-sample accuracy metric, defined as the proportion of correctly classified return signs in the test set.[9] Table 1 reports 

> 9 We report the accuracy metric given that the dependent variable is generally balanced. Other metrics, such as the F1score, produce similar results. However, our findings indicate a stronger correlation between accuracy and the Sharpe ratio compared to other metrics such as the F1-score. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**10** 

**Figure 3** Cumulative returns of each factor. The figure illustrates the cumulative log returns for each factor across the entire sample period from January 1965 to December 2021, with NBER recessions shaded in gray. 

**Table 1** Out-of-sample prediction performance. 

||**BUY**|**LR**|**EN**|**RF**|**GBT**|**SVM**|**NN**|**LSTM**|**MT**|**DMTc**|**DMT**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Mean|53.5|53.1|53.3|55.6|54.8|53.1|53.8|53.8|55.4|54.8|56.4|
|SMB|51.6|52.9|53.1|58.6|55.2|52.6|51.8|57.0|53.6|53.9|57.3|
|HML|47.9|54.7|51.8|52.6|53.6|50.3|51.8|49.0|55.5|54.4|57.0|
|RMW|58.3|50.5|53.4|55.5|51.8|55.2|54.7|57.6|57.6|56.5|53.4|
|CMA|49.2|51.6|49.2|51.3|53.9|49.2|51.3|46.1|51.0|49.7|52.9|
|MOM|60.4|56.0|58.9|59.9|59.4|58.1|59.4|59.4|59.4|59.6|61.2|



This table reports classification accuracy (in percent), defined as the fraction of return signs correctly classified, for the out-of-sample period from January 1990 to December 2021. Results are shown for all models and for a buy-and-hold (BUY) benchmark, which always predicts a positive return. The first row consolidates the findings by calculating the average accuracy across all factors, while the following rows individually detail the accuracy for each respective factor. 

the accuracy (in percent) of the models for the out-of-sample period from January 1990 to December 2021. We compare 10 models and a naive buy-and-hold (BUY) benchmark that always predicts a positive return. 

The first row of Table 1 reports the average accuracy across all five factors for each model. Linear models, LR and EN, yield low accuracies of 53.1% and 53.3%, respectively, falling short of the BUY benchmark accuracy of 53.5%, reflecting their limited flexibility. Accuracy improves to 55.6% and 54.8%, respectively, when nonlinear interactions are introduced through the tree-based models RF and GBT. In contrast, the kernel-based model SVM attains one of the lowest accuracies at 53.1%, indicative of excessive flexibility leading to overfitting to factor-specific noise. 

Turning to the deep learning models, NN and LSTM, which do not impose economic structure, both exhibit a relatively low accuracy of 53.8%, suggestive of overfitting to factor-specific noise. Imposing an economically motivated common structure across factors through MT yields a larger improvement, raising the accuracy to 55.4%, which indicates that the regularization and data-efficiency benefits of MTL enhance forecasting performance. By separately incorporating business and financial cycle dynamics with MTL, DMT achieves the highest accuracy of 56.4%. In contrast, when 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**11** 

macroeconomic and financial inputs are combined rather than separated in DMTc, the model exhibits mild overfitting, resulting in a lower accuracy of 54.8%, although it still outperforms the singletask LSTM. 

The subsequent rows of Table 1 report model accuracy for each factor. DMT outperforms the BUY benchmark for every factor except RMW. It is the top performer for HML and MOM, achieving accuracies of 57.0% and 61.2%, respectively, compared with BUY accuracies of 47.9% and 60.4%. DMT also delivers the second highest accuracy for SMB and CMA at 57.3% and 52.9%, respectively, compared with BUY accuracies of 51.6% and 49.2%. In contrast, for RMW all models underperform the BUY benchmark accuracy of 58.3%, with DMT attaining an accuracy of 53.4%. Overall, while different models perform best for different factors, DMT provides the most consistent performance across factors. 

To make pairwise comparisons of models, we use a modified Diebold and Mariano (1995) (DM) test that accounts for the potential cross-sectional dependence of factors. Given our focus on classification, we use the cross-sectional average log loss to compare the probability forecasts of our models.[10] The DM test statistic for a comparison of models 1 and 2 is defined as DM12 ¼ _d_ 12 _=σd_ 12[, ] where _d_ 12 and _σd_ 12[are, respectively, the mean and ][Newey and West (1987)][ standard error of ] _[d]_[12] _[;][t]_[þ][1 ] over the test sample. _d_ 12 _;t_ þ 1 is the forecasting error between the two models, calculated as the cross-sectional average of log loss differentials from each model over each period _t_ þ 1, 

**==> picture [252 x 25] intentionally omitted <==**

b where _e_[ð] _i;[j] t_[Þ] þ 1[¼] _[−][y][i][;][t]_[þ][1][ log][ð][b] _[π]_[ð] _i;[j] t_[Þ] þ 1[Þ] _[−]_[ð][1] _[−][y][i][;][t]_[ þ][1][Þ][log][ð][1] _[−]_[b] _[π]_[ð] _i;[j] t_[Þ] þ 1[Þ][ denotes the log loss of model ] _[j ]_[for factor ] _i_ at time _t_ þ 1, and _yi;t_ þ 1 � _I_ ð _ri;t_ þ 1 _>_ 0Þ is an indicator function that takes a value of one if factor _i_ ’s return is positive and zero otherwise. 

Table 2 reports the DM test statistics that provide pairwise comparisons of model probability forecasts based on the log loss criterion. A positive statistic indicates that the column model outperforms the row model and a bold entry denotes statistical significance at the 5% level. The first row shows that all models deliver positive and statistically significant improvements relative to the BUY benchmark. The next two rows indicate that all nonlinear models significantly outperform LR and EN. The fourth row shows that RF significantly outperforms all other models in terms of log loss. Notably, the last column shows that RF, GBT, LSTM, and MT outperform DMT according to the DM tests, despite DMT achieving a higher accuracy. This discrepancy highlights a disconnect between probability forecast performance under the log-loss criterion and classification accuracy, raising the question of which metric is more relevant for factor-timing strategies. We address this question in the next section. 

## **3.3 Multifactor timing** 

Next, we evaluate the economic significance of factor timing strategies derived from each model’s forecasts, using a multifactor portfolio. Motivated by Campbell and Thompson (2008), we apply realistic constraints that restrict short selling and leverage. For every factor, we take a long position if the model forecasts a positive return; otherwise, we exit the position, yielding zero returns. The strategy return for factor _i_ at time _t_ þ 1 is expressed as 

**==> picture [250 x 13] intentionally omitted <==**

where _I_ ð�Þ is an indicator function that takes a value of one if the predicted probability exceeds 50% and zero otherwise. Our multifactor strategy is then an EW portfolio of the strategy returns across all 

> 10 SVMs are excluded from this analysis since they do not provide probabilities. Although Platt scaling can estimate probabilities from SVM predictions, it may yield estimates contradicting the SVM classifications. Hence, we omit SVM from the DM tests. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**12** 

**Table 2** Comparison of probability predictions using Diebold–Mariano tests. 

||**LR**|**EN**|**RF**|**GBT**|**NN**|**LSTM**|**MT**|**DMTc**|**DMT**|
|---|---|---|---|---|---|---|---|---|---|
|BUY|**34.73**|**37.00**|**38.83**|**38.75**|**38.70**|**38.74**|**38.80**|**38.75**|**38.74**|
|LR||**6.20**|**5.85**|**5.60**|**5.55**|**5.76**|**5.79**|**5.41**|**5.59**|
|EN|||**3.67**|**3.26**|**3.04**|**3.45**|**3.54**|**2.92**|**3.18**|
|RF||||**−3.92**|**−5.41**|**−2.44**|**−2.38**|**−4.33**|**−3.50**|
|GBT|||||**−2.22**|1.00|1.09|**−**1.66|**−**0.37|
|NN||||||**3.50**|**4.29**|0.41|1.81|
|LSTM|||||||0.16|**−2.81**|**−**1.42|
|MT||||||||**−3.01**|**−**1.71|
|DMTc|||||||||1.56|



This table presents test statistics from pooled Diebold–Mariano tests. We perform pairwise comparisons of model probability forecasts, using the average log loss across factors. A positive statistic indicates the column model outperforms the row model, and a bold number denotes significance at the 5% level for each test. We omit SVM, since it does not output probabilities. 

**Table 3** Multifactor timing strategy performance. 

||**BUY**|**LR**|**EN**|**RF**|**GBT**|**SVM**|**NN**|**LSTM**|**MT**|**DMTc**|**DMT**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|SR|0.60|0.61|0.52|0.66|0.61|0.62|0.67|0.76|0.69|0.75|0.82|
|_α_||0.73|0.09|0.61|0.41|0.42|0.78|0.95|0.70|0.96|1.40|
|_t_ð_α_Þ||1.53|0.22|1.69|1.02|1.07|1.53|2.66|1.91|2.62|3.05|
|_β_||0.50|0.71|0.87|0.78|0.78|0.69|0.78|0.83|0.76|0.81|
|_R_2||47.83|70.50|80.76|75.13|78.10|67.05|83.17|82.20|77.40|76.78|



This table reports the performance of multifactor timing strategies by model, where strategy returns are defined as _rt_ -statistic ( _i_[Strategy] _;t_ þ 1 ¼ _I_ ð _tπ_ b( _αi;_ )), beta ( _t_ þ 1 _>_ 0 _:_ 5 _β_ Þ), and percentage _ri;t_ þ 1. Reported are the annualized Sharpe ratio (SR), along with the alpha ( _R_[2 ] with respect to the multifactor buy-and-hold (BUY) benchmark. _α_ ), Newey–West 

factors. Motivated by Moreira and Muir (2017), for each model we conduct a time-series regression of the strategy returns on the multifactor BUY, defined as an EW portfolio of factor returns. This spanning regression provides the strategy’s alpha, beta, and _R_[2 ] relative to the multifactor BUY. 

The first row of Table 3 presents the annualized Sharpe ratio for each model. Linear models, LR and EN, deliver relatively low Sharpe ratios of 0.61 and 0.52, respectively. The static nonlinear models, RF, GBT, SVM, and NN, generally deliver improvements, with Sharpe ratios of 0.66, 0.61, 0.62, and 0.67, respectively, reflecting economic gains from incorporating nonlinear interactions. Incorporating a common structure, MT outperforms all other static models with a Sharpe ratio of 0.69. 

Turning to dynamic models, LSTM outperforms all static models with a Sharpe ratio of 0.76. DMT is the best-performing model, achieving a Sharpe ratio of 0.82 and substantially outperforming the multifactor BUY benchmark, which attains a Sharpe ratio of 0.60. DMT also outperforms DMTc, which achieves a Sharpe ratio of 0.75, indicating that separating macroeconomic and financial inputs to capture distinct business and financial cycle dynamics yields superior gains. Notably, the LSTM, MT, DMTc, and DMT models all outperform RF in Sharpe ratio terms despite being significantly outperformed by RF in the DM tests reported in Table 2. This contrast demonstrates that superior probability forecasts do not necessarily translate into superior economic performance. The accuracy results in Table 1 track economic performance more closely, although discrepancies remain. These findings are consistent with the argument in Kelly, Malamud, and Zhou (2024) that statistical accuracy and economic significance do not necessarily coincide. 

The second row of Table 3 reports the annualized alpha earned by each model. Only the dynamic models, LSTM, DMTc, and DMT, generate alphas that are statistically significant at the 5% level, 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**13** 

**Figure 4** Cumulative returns of multifactor timing. This figure plots the cumulative log returns of multifactor timing strategies by model over the out-of-sample period from January 1990 to December 2021. Each model’s returns are adjusted to have the same volatility as the multifactor buy-and-hold (BUY) benchmark. NBER recessions are shown in gray. 

indicating that incorporating time-series dynamics is important for significantly outperforming the multifactor BUY benchmark. DMT achieves the highest alpha of 1.40% ( _t_ -stat of 3.05), substantially exceeding the alphas of DMTc at 0.96% ( _t_ -stat of 2.62) and LSTM at 0.95% ( _t_ -stat of 2.66), which highlights the additional gains from imposing economic restrictions. While no static model produces an alpha that is statistically significant at the 5% level, RF and MT attain alphas that are significant at the 10% level, equal to 0.61% ( _t_ -statistic of 1.69) and 0.70% ( _t_ -statistic of 1.91), respectively. 

Figure 4 illustrates the cumulative returns of each model alongside the multifactor BUY benchmark, with all model returns scaled to match the volatility of the multifactor BUY. The rankings across models closely align with the Sharpe ratio rankings reported in Table 3. DMT achieves the highest cumulative return, followed by LSTM, DMTc, and MT. Among the static off-the-shelf models, NN and RF deliver the strongest performance, while LR, GBT, and SVM generate similar cumulative returns and modestly outperform the multifactor BUY. In contrast, EN underperforms the benchmark. 

Interestingly, DMT experiences less severe drawdowns than the multifactor BUY benchmark and other models during the GFC and the COVID crisis. To better understand when DMT’s outperformance is achieved, we regress the residuals from the factor-spanning test on indicator variables for the GFC and COVID periods. Because the residuals are orthogonal to the multifactor BUY benchmark by construction, a positive coefficient indicates relative outperformance during crisis periods. Panel A of Supplementary Table IA4 reports the results. Only the DMT and NN models exhibit positive coefficients for both the GFC and COVID episodes, indicating that these models deliver particularly strong factor-adjusted performance during crisis states.[11] Panel B reports an analogous regression in which the spanning residuals are regressed on an indicator for negative market excess returns. All models load positively on this indicator, implying that they tend to outperform the benchmark during downmarket states. Taken together, these results suggest that superior performance in adverse states partially explains DMT’s strong economic gains. 

> 11 Statistical power is limited due to the small number of crisis observations, and most coefficients are therefore not statistically significant. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**14** 

While the strategy in Equation (3) is appealing because it imposes realistic constraints on shortselling and leverage, it is informative to assess robustness to alternative trading strategies. We therefore report two additional strategies in the Supplementary Appendix as robustness checks. Supplementary Table IA5 presents results for a strategy that modifies Equation (3) by short selling the factor, rather than exiting the position, when the predicted probability falls below 50%. This stratb egy is given by _ri_[ShortStrategy] _;t_ þ 1 ¼ ð2 × _I_ ð _π i;t_ þ 1 _>_ 0 _:_ 5Þ _−_ 1Þ _ri;t_ þ 1. Supplementary Table IA6 reports results for a long-only strategy that modifies Equation (3) by allowing the position in factor _i_ to scale with the b predicted probability. This strategy is given by _ri_[ProbabilityStrategy] _;t_ þ 1 ¼ b _π i;t_ þ 1 _I_ ð _π i;t_ þ 1 _>_ 0 _:_ 5Þ _ri;t_ þ 1. Both strategies yield Sharpe ratios similar to those reported in Table 3, with DMT outperforming all other models. DMT also consistently achieves the highest alpha across models under both alternative strategies. Given that the results are similar and that Equation (3) represents a realistic trading strategy, we do not pursue these alternative strategies further. 

## **3.4 Single-factor timing** 

Next, we break down the multifactor timing performance of each model by evaluating the performance of strategy (3) for each individual factor. Table 4 reports each model’s annualized Sharpe ratio, along with the alpha, Newey–West _t_ -statistic, beta, and _R_[2 ] from a time-series regression of the strategy on the respective single-factor BUY benchmark. 

Table 4 shows substantial heterogeneity in performance across factors for each off-the-shelf model. In contrast, DMT is the only model to deliver positive alphas that are statistically significant at the 10% level for all factors except RMW, highlighting the importance of jointly incorporating economic structure and time-series dynamics for reliable factor timing. Moreover, although DMT is designed to optimize multifactor performance, it also achieves the highest Sharpe ratios when timing HML and CMA at 0.36 and 0.49, respectively, substantially exceeding the corresponding BUY Sharpe ratios of 0.11 and 0.32. DMT further attains the third-highest Sharpe ratio for SMB at 0.40 and the second-highest Sharpe ratio for MOM at 0.49, both outperforming the corresponding BUY Sharpe ratios of 0.16 and 0.34. 

The first and third panels of Table 4 show that LSTM achieves the highest Sharpe ratios for SMB and RMW at 0.55 and 0.61, respectively, while the fifth panel indicates that NN achieves the highest Sharpe ratio for MOM at 0.52. These results suggest that imposing a common economic structure may be slightly less beneficial for SMB and MOM, while single-task models, such as NN and LSTM, may be more effective for RMW. Overall, these findings are consistent with the heterogeneity in factor predictability documented by Neuhierl et al. (2023). 

_−_ Quantitatively, DMT improves the Sharpe ratio relative to the single-factor Buy by 0.24, 0.25, 0.17, 0.17, and 0.15 for the SMB, HML, RMW, CMA, and MOM factors, respectively. In comparison, the topperforming model from Gu, Kelly, and Xiu (2020), a three-layer neural network, enhances the Sharpe _−_ ratio over the single-factor Buy by 0.15, 0.04, 0.01, 0.05, and 0.04 for these factors. This comparison underscores DMT’s superior factor timing capabilities relative to the best model in Gu, Kelly, and Xiu (2020), except in the case of RMW. DMT’s superior performance can be largely attributed to its incorporation of economic structure and time-series dynamics, aspects not captured by the three-layer neural network. 

## **3.5 Transaction costs** 

Table 5 presents the profitability of multifactor timing strategies after accounting for transaction costs incurred when deviating from the BUY benchmark. Motivated by Moreira and Muir (2017), we consider transaction costs of 1, 5, 10, and 14 basis points, which are subtracted from returns in months in which the strategy exits a factor position, that is, when Equation (3) equals zero. Even with transaction costs of 14 basis points in Panel (d), DMT still achieves a Sharpe ratio of 0.74, surpassing the multifactor BUY Sharpe ratio of 0.60. Moreover, DMT is the only model to deliver a statistically significant alpha of 1.01% ( _t_ -statistic of 2.21). Supplementary Table IA7 presents the after-cost profitability of DMT for each factor. Even with transaction costs of 14 basis points in Panel (d), DMT achieves a 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**15** 

**Table 4** Single-factor timing strategy performance. 

|**Factor**||**BUY**|**LR**|**EN**|**RF**|**GBT**|**SVM**|**NN**|**LSTM**|**MT**|**DMTc**|**DMT**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|SMB|SR|0.16|0.33|0.23|0.49|0.37|0.34|0.17|0.55|0.28|0.35|0.40|
||_α_||1.66|0.87|3.07|1.90|1.79|0.39|3.30|1.35|1.83|2.14|
||_t_ð_α_Þ||1.84|0.91|3.69|2.23|2.00|0.43|3.71|1.68|2.01|2.28|
||_β_||0.52|0.52|0.67|0.46|0.66|0.52|0.52|0.72|0.58|0.52|
||_R_2||52.11|52.25|67.98|45.77|66.12|52.16|52.96|71.81|58.13|51.99|
|HML|SR|0.11|0.13|0.05|0.09|0.22|0.03|0.00|0.04|0.27|0.26|0.36|
||_α_||0.43|_−_0.21|0.02|1.10|_−_0.56|_−_0.77|_−_0.47|1.55|1.48|2.40|
||_t_ð_α_Þ||0.46|_−_0.22|0.02|1.22|_−_0.63|_−_0.83|_−_0.55|1.70|1.58|2.56|
||_β_||0.45|0.47|0.65|0.63|0.69|0.66|0.71|0.69|0.64|0.68|
||_R_2||45.14|47.25|64.58|63.27|68.73|65.91|70.75|69.38|64.67|68.26|
|RMW|SR|0.49|0.43|0.38|0.46|0.35|0.50|0.55|0.61|0.42|0.43|0.32|
||_α_||0.60|_−_0.07|0.39|_−_0.08|0.76|1.17|1.47|_−_0.16|_−_0.22|_−_1.22|
||_t_ð_α_Þ||0.63|_−_0.07|0.38|_−_0.08|0.75|1.11|1.42|_−_0.29|_−_0.44|_−_2.91|
||_β_||0.50|0.63|0.71|0.56|0.65|0.63|0.77|0.81|0.89|0.91|
||_R_2||49.18|62.83|70.70|55.75|65.04|63.31|76.89|80.91|88.29|90.61|
|CMA|SR|0.32|0.20|0.12|0.35|0.43|0.27|0.33|0.12|0.38|0.29|0.49|
||_α_||0.00|_−_0.76|0.27|0.88|_−_0.25|0.41|_−_0.87|0.67|0.25|1.29|
||_t_ð_α_Þ||0.00|_−_1.35|0.76|1.79|_−_0.65|0.71|_−_1.60|1.18|0.43|2.43|
||_β_||0.40|0.63|0.91|0.79|0.89|0.64|0.68|0.68|0.60|0.71|
||_R_2||40.16|62.66|90.76|79.40|89.05|63.72|68.19|68.43|59.93|71.49|
|MOM|SR|0.34|0.33|0.38|0.33|0.28|0.35|0.52|0.42|0.34|0.37|0.49|
||_α_||0.88|1.04|_−_0.15|_−_0.59|0.62|3.21|1.48|_−_0.00|0.56|2.71|
||_t_ð_α_Þ||0.61|0.99|_−_1.14|_−_0.69|0.48|1.60|1.20|_−_0.01|0.85|1.72|
||_β_||0.55|0.82|1.00|0.87|0.84|0.73|0.90|0.98|0.96|0.83|
||_R_2||55.22|82.43|99.77|87.25|84.11|73.40|90.45|98.45|95.81|83.35|



This table presents the performance of the single-factor timing strategies by model. Reported are the annualized Sharpe ratio (SR), along with the alpha ( _α_ ), Newey–West _t_ -statistic ( _t_ ( _α_ )), beta ( _β_ ), and percentage _R_[2 ] with respect to the singlefactor buy-and-hold (BUY) benchmark. 

positive alpha for all factors except RMW. DMT also earns a Sharpe ratio that beats the single-factor BUY, displayed in Panel (e), for every factor except RMW. 

## **3.6 Which predictors matter?** 

We next study the importance of each predictor for factor timing. The ideal approach would be to reestimate the model while sequentially excluding each predictor. However, this method is not feasible due to the computational demands posed by the large number of predictors (a total of 259) in our estimation. To circumvent this challenge, we employ Shapley values, a methodology rooted in cooperative game theory, to assess the impact of individual predictors on the model’s prediction. Shapley values provide an approximation of how the model’s predictions would have varied if certain predictors had been excluded in its estimation. For a detailed description of Shapley values, see Supplementary Appendix IA2. 

## **3.6.1 Multifactor variable importance** 

We compute Shapley values for each model and factor over the out-of-sample period from January 1990 to December 2021. For each model and factor, we calculate the absolute Shapley value for each month and average these into a single importance measure for each predictor. Subsequently, we obtain a multifactor importance measure for each model by averaging across the factors. Figures 5 and 6 present the rankings of macroeconomic and financial variables, respectively. For these heatmaps, 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**16** 

**Table 5** Factor-timing profitability with transaction costs. 

||**BUY**|**LR**|**EN**|**RF**|**GBT**|**SVM**|**NN**|**LSTM**|**MT**|**DMTc**|**DMT**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**(a) 1 basis point**||||||||||||
|SR|0.60|0.60|0.51|0.66|0.60|0.62|0.66|0.76|0.69|0.74|0.82|
|_α_||0.68|0.05|0.60|0.38|0.40|0.75|0.93|0.67|0.93|1.37|
|_t_ð_α_Þ||1.42|0.13|1.63|0.94|1.01|1.47|2.60|1.84|2.54|3.00|
|**(b) 5 basis points**||||||||||||
|SR|0.60|0.54|0.48|0.64|0.57|0.60|0.64|0.74|0.66|0.71|0.79|
|_α_||0.47|_−_0.09|0.52|0.25|0.30|0.63|0.84|0.56|0.81|1.26|
|_t_ð_α_Þ||0.99|_−_0.22|1.42|0.63|0.76|1.23|2.38|1.54|2.22|2.76|
|**(c) 10 basis points**||||||||||||
|SR|0.60|0.47|0.44|0.62|0.54|0.57|0.60|0.71|0.63|0.68|0.76|
|_α_||0.21|_−_0.27|0.42|0.10|0.18|0.47|0.74|0.42|0.67|1.12|
|_t_ð_α_Þ||0.45|_−_0.66|1.16|0.24|0.45|0.93|2.09|1.17|1.82|2.46|
|**(d) 14 basis**||**points**||||||||||
|SR|0.60|0.42|0.41|0.61|0.51|0.55|0.57|0.70|0.61|0.65|0.74|
|_α_||0.01|_−_0.41|0.34|_−_0.03|0.08|0.35|0.66|0.31|0.55|1.01|
|_t_ð_α_Þ||0.02|_−_1.01|0.94|_−_0.07|0.20|0.69|1.86|0.86|1.50|2.21|



This table presents the Sharpe ratio (SR), alpha ( _α_ ), and Newey–West _t_ -statistic ( _t_ ( _α_ )) of the factor timing strategy for each model after accounting for transaction costs. We consider transaction costs of 1, 5, 10, and 14 basis points, which are subtracted from strategy returns in months when factors are exited. 

we rank the multifactor importance of each variable for each model, then sum their ranks across models. The color gradient within each column shows the model-specific ranking of predictors from the most to least important (darkest to lightest). 

Figure 5 reveals substantial agreement across models regarding the ranking of key macroeconomic predictors. The most influential predictor is civilians unemployed for 15–26 weeks, which belongs to the labor category. Two additional labor variables also rank among the top 10, namely all employees: financial activities and average weekly hours in manufacturing. Money variables also rank prominently, with 3 variables appearing among the top 10: reserves and total reserves of depository institutions, and real estate loans at all commercial banks. The remaining top 10 variables span a heterogeneous set of categories, including inflation (personal cons. exp: durable goods, ppi: finished consumer goods), stocks (vix), and output (ip: nondurable consumer goods). In contrast, most of the least influential macroeconomic variables are associated with interest rates. 

Figure 6 reveals a strong consensus across models regarding the ranking of key financial predictors. Variables in the leverage category account for 4 of the top 10 predictors, including industry concentration (sales), tangibility, organizational capital, and firm age. The remaining top 10 variables span several distinct categories, including value (net payout yield), profitability (dividend omission), investment (inventory change), price trends (return seasonality years 11–15), risk (tail risk beta), and liquidity (inst own and idio vol). 

Interestingly, variables identified by Gu, Kelly, and Xiu (2020) as important predictors of individual stock returns rank among the least influential for factor timing. These include the bid–ask spread, past trading volume, size, idiosyncratic risk from the three-factor model, capm beta, and six-month momentum. This pattern likely reflects the fact that machine learning predictions for individual stocks are often driven by short-lived characteristics that are particularly effective for small and illiquid stocks (Jensen et al. 2026; Avramov, Cheng, and Metzker 2023). In contrast, our results indicate that accounting variables, particularly those in the leverage category, play a dominant role in factor timing, consistent with the fact that factor portfolios are primarily constructed from larger and more liquid stocks. This contrast highlights fundamental differences in the economic mechanisms and functional forms that drive predictability at the stock versus factor level. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**17** 

**Figure 5** Variable importance rankings of macroeconomic variables. (a) Top 61 macroeconomic variables and (b) bottom 61 macroeconomic variables. This figure displays the rankings of macroeconomic variables. We rank the multifactor importance of each macroeconomic variable for each model, then sum their ranks. The color gradient within each column shows the model-specific ranking of predictors from the most to least important (darkest to lightest). 

Supplementary Figure IA2 displays the 20 most influential variables by model and shows that a rich set of macroeconomic and financial variables contributes to multifactor timing. This breadth of influential predictors underscores the need for a high-dimensional modeling framework capable of capturing diverse signals. To further synthesize these findings, we construct an importance measure for each predictor category by averaging the multifactor importance measures within each respective category. Supplementary Figure IA3 shows that the category importance by model largely aligns with the individual predictor importance results. Among macroeconomic categories, money, prices, stocks, and housing are particularly influential, while rates are the least. While labor contributes several highly influential variables, it also contains many lower-ranked predictors, which reduces its overall importance as a category. Among financial categories, leverage and profitability stand out in terms of influence, while the risk and liquidity categories play a comparatively smaller role in explaining factor timing performance. These figures show that many financial predictors and categories are highly influential, indicating that a broad set of asset pricing anomalies contributes meaningfully to factor timing, consistent with Dong et al. (2022) but in contrast to the findings of Cakici et al. (2024) and Engelberg et al. (2023). 

## **3.6.2 Single-factor variable importance** 

We next examine the influential predictors for each factor. Figure 7 reports the 20 most influential variables for each factor based on the DMT model. Both the composition and ranking of influential variables vary substantially across factors, consistent with the heterogeneity in predictor importance documented by Neuhierl et al. (2023). 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**18** 

**Figure 6** Variable importance rankings of financial variables. (a) Top 68 financial variables and (b) bottom 69 financial variables. This figure displays the rankings of financial variables. We rank the multifactor importance of each financial variable for each model, then sum their ranks. The color gradient within each column shows the model-specific ranking of predictors from the most to least important (darkest to lightest). 

Panel (a) shows that financial variables dominate the predictability of SMB, with tail risk beta emerging as the most influential predictor. The prominence of tail risk beta is consistent with Kelly and Jiang (2014) and Liu (2020), who show that tail risk, measured using power law distributions, is informative for predicting portfolio and individual stock returns. Price trend variables are also highly influential, including return seasonality years 11–15, momentum based on ff3 residuals, and return seasonality years 16–20. Leverage plays an important role as well, with five influential predictors drawn from this category, including convertible debt indicator, tangibility, organizational capital, industry concentration (sales), and composite debt issuance. 

Panel (b) highlights the importance of accounting variables for HML. Variables from the leverage and profitability categories account for 10 of the most influential predictors. These include four leverage variables (industry concentration [sales and equity], tangibility, investment to revenue), and six profitability variables (dividend omission, change in net noncurrent op assets, accruals, sales growth over overhead growth, operating profits/book equity, inventory growth). The important role of accounting variables for stock predictability is consistent with evidence in Chen and Zhang (2007). 

Panels (c) and (d) show that macroeconomic variables are particularly influential for RMW and CMA. Key macroeconomic predictors overlap across the two factors in categories such as labor (civilians unemployed for 15–26 weeks), inflation (ppi: finished goods), and money (reserves and total reserves of depository institutions), although there are notable differences, such as the importance of stocks (vix) for RMW and output (ip: nondurable consumer goods) for CMA. Among financial variables, there is also overlap in influential predictors from the price trends (price delay coeff) and 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**19** 

**Figure 7** Variable importance by factor for the DMT model. (a) SMB, (b) HML, (c) RMW, (d) CMA, and (e) MOM. This figure presents the 20 most influential variables by factor for the DMT model. For each factor, we calculate the absolute Shapley value for each month and average these into a single importance measure for each predictor. 

profitability (accruals, operating profits/book equity) categories. Notably, influential predictors overlap across HML, RMW, and CMA, suggesting that these accounting-based factors are driven by common underlying economic fundamentals. 

Finally, Panel (e) shows that MOM is highly sensitive to the vix, consistent with the vulnerability of momentum strategies to adverse financial and business cycle conditions such as the GFC. Price trend variables are especially influential, including return seasonality years 11–15, price delay coeff, off season reversal years 11–15, and momentum in high volume stocks. Tail risk beta is also a key predictor, consistent with the crash risk of momentum strategies documented by Daniel and Moskowitz (2016). In addition, accounting variables play a nontrivial role, particularly profitability (accruals, sales growth over inventory growth) and leverage (firm age, industry concentration [sales], tangibility). Macroeconomic predictors related to inflation (ppi: metals and metal products, personal cons. exp: durable goods, cpi: apparel) and labor (all employees: financial activities, civilians unemployed—less than 5 weeks) are also influential. These findings complement the view of momentum as driven by sentiment (Antoniou, Doukas, and Subrahmanyam 2013) by highlighting the additional role of fundamental macroeconomic and financial variables. 

We next summarize category importance using the DMT model in Figure 8. Among financial categories, leverage, profitability, and price trends consistently rank highest, underscoring their central role in factor timing. Among macroeconomic categories, money is frequently influential, whereas rates 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**20** 

**Figure 8** Category importance by factor for the DMT model. (a) SMB, (b) HML, (c) RMW, (d) CMA, and (e) MOM. This figure presents the importance of variable categories by factor for the DMT model. For each factor, we calculate the absolute Shapley value for each month and average these into a single importance measure for each predictor. These importance measures are then averaged by category. 

are consistently the least influential. Thus, although individual predictors are heterogeneous across factors, there is substantial commonality in the most important categories, suggesting that the common structure across factors is largely driven by these categories. 

## **3.6.3 Time variation in multifactor variable importance** 

Furthermore, we examine time variation in predictor importance. Figure 9 plots the yearly average multifactor importance of each predictor category for the DMT model. Category importance measures are normalized to sum to one in each year, yielding a measure of relative importance over time, where darker colors indicate greater influence in a given year. The figure reveals substantial time variation in importance across all categories. Among macroeconomic categories, money is most influential from 1999 to 2011, while housing becomes particularly important in the post-GFC period from 2009 to 2014. Among financial categories, leverage and profitability are highly influential in most years, except during the post-dot-com bust from 2002 to 2004 and in 2014, periods in which investment and risk are relatively more influential. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**21** 

**Figure 9** Category importance by year for the DMT model. This figure presents the most influential categories by year for the DMT model. For each factor, we calculate the absolute Shapley value for each month and average these each year into a yearly importance measure for each predictor. Subsequently, we obtain a multifactor importance measure for each predictor for the DMT model by averaging across the factors. Next, we derive an importance measure for each category by averaging the multifactor importance measures within each category. Finally, category importance measures are ranked within each year, yielding a measure of relative category importance over time, where darker colors indicate greater influence in a given year. 

## **3.6.4 Nonlinear interactions** 

Finally, we examine the role of nonlinear interactions in driving DMT’s superior performance. While the model admits a large number of potential interactions, we highlight a small set to elucidate DMT’s inner workings. Figure 10 presents three-dimensional interaction surfaces, with predictor values on the horizontal axes and Shapley values on the vertical axis. Panel (d) shows that the contribution of civilians unemployed for 15–26 weeks varies nonmonotonically with changes in reserves of depository institutions, exhibiting a pronounced trough when reserve changes are close to their historical mean (i.e., near zero after standardization). In this region, increases in unemployment generate strongly negative Shapley values, lowering the _πi;t_ þ 1 forecast. In contrast, when reserves experience large positive or negative shocks, Shapley values are close to zero, indicating that shifts in monetary conditions dominate CMA predictability and attenuate the incremental role of labor signals. 

The remaining panels reveal similar patterns for the other factors, in which pairs of influential predictors generate complex nonlinear interactions. Although visualization is necessarily restricted to three dimensions, these surfaces suggest that factor risk premia are governed by highly complex relationships in much higher dimensional predictor spaces. More importantly, the results illustrate the advantage of DMT in capturing such nonlinear interactions, which translate into superior out-ofsample performance, underscoring the effectiveness of DMT in exploiting multidimensional dependencies among predictors to improve factor timing. 

## **3.7 Understanding the economic drivers of multifactor timing** 

Section 3.1 shows that multifactor investing offers substantial diversification benefits, motivating a multifactor timing framework. This naturally raises the question of which models are suitable for multifactor timing. The results in Section 3 advance our understanding of model choice in addressing the key challenges of factor timing and, in doing so, shed light on the economic mechanisms driving factor risk premia. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**22** 

**Figure 10** Interaction plots by factor. (a) SMB, (b) HML, (c) RMW, (d) CMA, and (e) MOM. Plot of three-dimensional surfaces. Each plot shows a variable plotted along the right horizontal axis, its Shapley values for the DMT model along the vertical, and a variable it interacts with on the left horizontal axis. 

Section 3.3 shows that linear models (LR and EN) are too inflexible to capture the complex functional form of factor risk premia. Static off-the-shelf nonlinear models (RF, GBT, SVM, and NN) generally improve performance, suggesting that they better extract signal from noisy predictors and therefore achieve higher Sharpe ratios, as predicted by the virtues of complexity (Kelly, Malamud, and Zhou 2024). Imposing an economically motivated common structure across factors through MT further improves performance, consistent with Haddad, Kozak, and Santosh (2020). Incorporating time-series dynamics through LSTM leads to additional gains. Moreover, by jointly imposing a 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**23** 

common structure and separately incorporating business and financial cycle dynamics, DMT achieves the highest Sharpe ratio. 

Furthermore, Section 3.6 shows that factor risk premia depend on a rich set of financial and macroeconomic variables. While machine learning models largely agree on the most influential predictors for multifactor timing, there is substantial heterogeneity in predictor importance across factors. Despite this heterogeneity, several categories, such as leverage, profitability, and money, are consistently influential, suggesting that these variables help drive the common structure across factors. We further show that variable importance varies over time, and that DMT extracts predictive information through rich nonlinear interactions among these variables. Overall, DMT achieves superior performance by effectively addressing the four major challenges of factor timing. 

## **4 JKP results** 

The baseline analysis presented in Section 3 shows that deep learning models incorporating economic structure and time-series dynamics substantially improve multifactor timing for five factors widely used in the academic literature and by practitioners. This section examines whether these gains generalize to a much broader set of factors over the out-of-sample period from January 1990 to December 2021. 

Jensen, Kelly, and Pedersen (2023) provide a comprehensive analysis showing that many factors exhibit strong in-sample and out-of-sample performance, offering compelling evidence of their robustness and replicability. The JKP factors therefore provide a natural proving ground for assessing the generalizability of factor-timing strategies based on deep learning models with economically motivated restrictions. To this end, we extend the DMT model described in Section 2.2.2 to jointly estimate the conditional probability _πi;t_ þ 1, as defined in Equation (1), for all JKP factors within a single functional form. This approach imposes a common structure across all 149 factors. The expanded factor set substantially increases the number of parameters relative to the baseline specification, providing a stringent test of the scalability and robustness of DMT. Without effective economic restrictions, such as a common structure, this increase in model parameters would typically lead to severe overfitting. As off-the-shelf benchmark models, we include LR, EN, RF, GBT, and SVM, each of which estimates a separate functional form for the conditional probability _πi;t_ þ 1 of each factor. We exclude the remaining deep learning models due to computational constraints. 

## **4.1 Out-of-sample predictive power of JKP factors** 

We begin by evaluating the predictive power of machine learning models for the JKP factors. Table 6 reports the mean out-of-sample classification accuracy across the 149 factors, along with pairwise model comparisons based on the modified DM test described in Section 3.2. Panel (a) shows that the ranking of models by mean accuracy largely mirrors the baseline results in Table 1. Linear models, LR and EN, achieve lower accuracies of 51.0% and 52.4%, respectively, and underperform the BUY benchmark accuracy of 52.8%, reflecting their limited flexibility. The accuracy improves with the inclusion of nonlinear interactions, with RF achieving 53.3%. In contrast, GBT and SVM attain lower accuracies of 52.4% and 52.3%, respectively, suggestive of overfitting to factor-specific noise. DMT delivers the highest accuracy at 53.8%, reflecting the benefits of incorporating economic structure and time-series dynamics. 

Panel (b) reports DM test statistics that provide pairwise comparisons of probability forecasts across models based on the log loss criterion. The first row shows that all models significantly outperform the BUY benchmark. The next two rows indicate that all nonlinear models significantly outperform LR and EN. The fourth row shows that RF outperforms both GBT and DMT, despite DMT achieving a higher accuracy. As in the baseline analysis, this discrepancy highlights a disconnect between probability forecast performance based on the log loss criterion and classification accuracy. The subsequent sections show that classification accuracy is more closely aligned with the economic significance of factor-timing strategies than probability-based DM test statistics. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**24** 

**Table 6** JKP out-of-sample predictive performance. 

## **(a) Mean accuracy by model** 

||**BUY**|**LR**|**EN**|**RF**|**GBT**|**SVM**|**DMT**|
|---|---|---|---|---|---|---|---|
|Accuracy|52.8|51.0|52.4|53.3|52.4|52.3|53.8|
|**(b) Comparison**|**of probability**|**predictions using DM tests**||||||
||**LR**|**EN**||**RF**|**GBT**||**DMT**|
|BUY|**69.06**|**75.28**||**77.01**|**76.40**||**77.21**|
|LR|||**9.30**|**8.48**|**7.65**||**8.39**|
|EN||||**6.75**|**4.65**||**6.51**|
|RF|||||_−_**16.89**||_−_1.46|
|GBT|||||||**9.49**|



Panel (a) of this table reports average classification accuracy (in percent) across JKP factors. Panel (b) presents test statistics from pooled Diebold–Mariano tests. A positive statistic indicates the column model outperforms the row model, and a bold number denotes significance at the 5% level for each test. We omit SVM, since it does not output probabilities. 

**Table 7** JKP multifactor timing strategy performance. 

||**BUY**|**LR**|**EN**|**RF**|**GBT**|**SVM**|**DMT**|
|---|---|---|---|---|---|---|---|
|SR|0.63|0.66|0.78|0.80|0.82|0.66|0.88|
|_α_||0.53|0.68|0.73|0.73|0.43|1.03|
|_t_ð_α_Þ||1.83|2.42|2.94|2.98|1.32|3.62|
|_β_||0.39|0.52|0.67|0.51|0.62|0.70|
|_R_2||43.40|61.91|74.87|64.50|64.95|72.95|



This table reports the performance of multifactor timing strategies by model for the JKP factors, where strategy returns are defined as alpha ( _α_ ), Newey–West _ri_[Strategy] _;t_ þ 1 ¼ _t I_ -statistic (ðb _π i;t_ þ 1 _> t_ 0( _:α_ 5)), beta (Þ _ri;t_ þ 1. Reported are the annualized Sharpe ratio (SR), along with the annualized _β_ ), and percentage _R_[2 ] with respect to the JKP multifactor buy-and-hold (BUY) benchmark. 

## **4.2 Multifactor timing of JKP factors** 

Next, we evaluate the economic significance of multifactor timing for the JKP factors using an EW multifactor portfolio for each model, with strategy returns defined in Equation (3). Table 7 reports the annualized Sharpe ratio of each model, along with the spanning test alpha, beta, and _R_[2 ] relative to the JKP multifactor BUY benchmark, which is constructed as the EW mean of strategy returns across all 149 factors. 

Overall, the results in Table 7 closely mirror those from the baseline analysis in Table 3. All models outperform the multifactor BUY benchmark, which records a Sharpe ratio of 0.63. Linear models, LR and EN, deliver lower Sharpe ratios of 0.66 and 0.78, respectively. Sharpe ratios slightly increase to 0.80 and 0.82, respectively, when nonlinear interactions are incorporated through the tree-based models RF and GBT. However, SVM ties for the lowest Sharpe ratio of 0.66, suggestive of overfitting to factor-specific noise due to excessive model flexibility. 

DMT achieves the highest Sharpe ratio of 0.88, demonstrating that the economic gains from incorporating economic structure and time-series dynamics extend to a broad set of factors. It also exceeds the Sharpe ratios of 0.71 and 0.73 from multifactor timing on a broad set of factors using PCA models in Haddad, Kozak, and Santosh (2020) and Kagkadis et al. (2024), respectively. DMT also delivers the highest alpha of 1.03% ( _t_ -stat of 3.62), followed by RF and GBT with alphas of 0.73% 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**25** 

**Figure 11** Cumulative returns of JKP multifactor timing. This figure plots the cumulative log returns of JKP multifactor timing strategies by model over the out-of-sample period from January 1990 to December 2021. Each model’s returns are adjusted to have the same volatility as the JKP multifactor buy-and-hold (BUY) benchmark. NBER recessions are shown in gray. 

( _t_ -stats of 2.94 and 2.98), respectively. As in the baseline analysis, DMT delivers stronger economic performance than RF despite being outperformed in the DM tests, reinforcing that probability forecast performance is not tightly linked to economic performance. In contrast, DMT’s superior classification accuracy aligns more closely with its higher Sharpe ratio and alpha, underscoring the relevance of accuracy for factor-timing strategies. 

Figure 11 plots the cumulative returns of each model alongside the JKP multifactor BUY benchmark, with all model returns scaled to match the volatility of the JKP multifactor BUY. The rankings across models closely align with the Sharpe ratio rankings reported in Table 7. DMT delivers the highest cumulative return, followed by GBT, RF, and EN. LR and SVM exhibit similar cumulative returns and modestly outperform the JKP multifactor BUY benchmark. 

Can the multifactor timing results for the JKP factors withstand transaction costs? Supplementary Table IA8 reports the performance of multifactor timing strategies after accounting for transaction costs of 1, 5, 10, and 14 basis points, which are subtracted from strategy returns in months when factor positions are exited. Panel (d) shows that, under the highest transaction cost of 14 basis points, DMT achieves the highest Sharpe ratio of 0.75, which comfortably exceeds the JKP multifactor BUY Sharpe ratio of 0.63. Moreover, DMT is the only model to deliver a statistically significant alpha of 0.63% ( _t_ -stat of 2.23). These findings closely mirror the baseline results with transaction costs reported in Table 5, providing further evidence that DMT’s economic gains are robust to realistic trading frictions and scale to a broad set of factors. 

## **4.3 JKP factor portfolios using conditional probability forecasts** 

Finally, we further evaluate the economic significance of the conditional probability forecasts using a portfolio sorting strategy applied to the 149 factors. At the end of each month, we forecast the onemonth-ahead conditional probability _πi;t_ þ 1, and sort factors into quintiles based on these forecasts. We reconstitute portfolios each month using equal weights. Table 8 reports the performance results, where “Low” denotes the portfolio with the lowest _πi;t_ þ 1 forecasts (quintile 1), “High” denotes the portfolio with the highest _πi;t_ þ 1 forecasts (quintile 5), and “H–L” denotes the long–short portfolio that buys the highest _πi;t_ þ 1 portfolio (quintile 5) and sells the lowest (quintile 1). 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**26** 

**Table 8** Performance of EW quintile portfolios sorted on conditional probability forecasts. 

||**LR**|**EN**|**RF**|**GBT**|**DMT**|
|---|---|---|---|---|---|
|Low|0.76|1.47|_−_0.67|1.09|_−_1.26|
|2|2.67|1.08|1.73|1.31|0.80|
|3|2.14|1.98|2.70|2.10|2.40|
|4|2.71|3.59|3.10|3.22|4.24|
|High|3.10|3.27|4.56|3.67|5.26|
|H–L|2.33|1.80|5.24|2.58|6.52|
|_t_(H–L)|1.53|1.24|4.21|2.26|3.73|
|SR|0.24|0.19|0.70|0.35|0.67|
|Sortino|0.27|0.22|0.87|0.41|1.00|
|Max DD|73.00|89.17|87.28|71.01|63.82|
|_α_|4.61|3.65|5.98|4.06|7.00|
|_t_(_α_)|2.76|2.02|4.44|3.24|3.87|
|_R_2|13.60|10.01|2.55|10.48|0.62|



This table reports the performance of EW quintile portfolios formed by sorting the JKP factors on one-month-ahead conditional probability _πi;t_ þ 1 forecasts. At the end of each month, factors are sorted into quintiles based on _πi;t_ þ 1 forecasts and portfolios are reconstituted monthly using equal weights. “Low” and “High” denote the lowest and highest quintiles, respectively, and “H–L” denotes the long–short portfolio that buys the high quintile and sells the low quintile. The average realized returns are in annualized percentage. For the long–short portfolios, we additionally report the Newey–West _t_ -statistics ( _t_ (H–L)), annualized Sharpe and Sortino ratios (SR, Sortino), percent maximum drawdowns (Max DD), as well as annualized alphas ( _α_ ), Newey–West _t_ -statistics ( _t_ ( _α_ )), and percentage _R_[2 ] values from spanning regressions on the JKP multifactor buy-and-hold (BUY) benchmark. We omit SVM, since it does not output probabilities. 

Table 8 shows that annualized average returns increase monotonically across quintile portfolios for all nonlinear models, indicating that these models accurately rank factors by their _πi;t_ þ 1 forecasts. In contrast, long–short portfolios based on LR and EN earn low average returns of 2.33% ( _t_ -stat of 1.53) and 1.80% ( _t_ -stat of 1.24), respectively, confirming that the weak probability forecasts of linear models translate into limited economic significance. Among the off-the-shelf models, RF delivers the highest long–short return of 5.24% ( _t_ -stat of 4.21), consistent with its strong probability forecasts. GBT attains a moderate long–short return of 2.58% ( _t_ -stat of 2.26), reflecting weaker probability forecasts. By jointly incorporating economic structure and time-series dynamics, DMT achieves the highest long–short return of 6.52% ( _t_ -stat of 3.73). 

The Sharpe ratios of long-short portfolios reported in Table 8 largely mirror the patterns observed for average returns. Long–short portfolios based on LR and EN exhibit the lowest Sharpe ratios of 0.24 and 0.19, respectively, reflecting the weak performance of linear models. GBT attains a moderate Sharpe ratio of 0.35. Notably, despite delivering a lower average return, RF achieves the highest Sharpe ratio of 0.70, slightly exceeding the Sharpe ratio of 0.67 attained by DMT. However, because the Sharpe ratio is based on total volatility and treats upside and downside volatility symmetrically, a lower Sharpe ratio may reflect desirable upside volatility rather than inferior performance. To address this limitation, we also report the Sortino ratio, which depends only on downside volatility. Table 8 shows that DMT attains a Sortino ratio of 1.00, substantially higher than RF’s Sortino ratio of 0.87, confirming that DMT’s lower Sharpe ratio is driven by elevated upside volatility rather than increased downside risk. 

In addition, DMT exhibits the lowest maximum drawdown among all models at 63.82%, followed by GBT and LR with maximum drawdowns of 71.01% and 73.00%, respectively. RF and EN experience the largest maximum drawdowns of 87.28% and 89.17%, indicating substantially higher tail risk for these long–short portfolios. Table 8 also reports the spanning test alpha relative to the JKP multifactor BUY benchmark. DMT delivers the highest alpha of 7.00% ( _t_ -stat of 3.87), followed by RF with an alpha of 5.98% ( _t_ -stat of 4.44). Taken together, these results show that DMT’s superior accuracy 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**27** 

translates into more effective cross-sectional ranking of conditional factor risk premia, as reflected in long–short portfolios formed on probability forecasts. 

## **5 Conclusion** 

Understanding factor risk premia is a central topic in financial economics and the burgeoning factor investing industry. An extensive literature studies factor predictability using predominantly static and linear single-factor models with limited numbers of predictors. While such literature reveals important insights, the empirical evidence on factor timing remains mixed, and its feasibility continues to be actively debated. Building on the recent success of a rapidly growing literature that applies machine learning techniques to model stock returns, we introduce deep neural networks that incorporate economically motivated restrictions, tailored to address the main challenges of factor timing. 

In this paper, we develop a DMT deep learning model to forecast five well-known factors using 122 macroeconomic and 137 financial predictors over the 57 year period from January 1965 to December 2021. Empirically, we demonstrate several results that advance our knowledge of factor timing. First, we show that incorporating economic structure and time-series dynamics improves the predictive accuracy of factor timing models. Second, we demonstrate that deep learning models with economic structure deliver substantial economic gains in a multifactor portfolio, which is further enhanced by incorporating time-series dynamics. Third, we document that key predictors for factor timing include unemployment and variables in the leverage, profitability, and money categories, and show that both their time variation and nonlinear interactions play an important role in effective factor timing. Finally, we establish that these results generalize to a much broader set of factors. Our dynamic multifactor deep learning approach yields substantially improved factor timing performance, highlighting the value of incorporating economically motivated restrictions into deep learning models for factor investing, and facilitating a more reliable investigation of the economic mechanisms driving factor risk premia. 

## **Supplemental Material** 

Supplemental material is available at _Journal of Financial Econometrics_ online. 

## **Conflict of Interest** 

None declared. 

## **Funding** 

This paper was supported by Social Sciences and Humanities Research Council Insight Development Grant (430-2022-00399) and the Digital Research Alliance of Canada Resources for Research Groups 2022 competition (ID 4286). 

## **References** 

Aleti, S., and T. Bollerslev. 2025. News and Asset Pricing: A High-Frequency Anatomy of the SDF. _The Review of Financial Studies_ 38: 712–759. 

Aleti, S., T. Bollerslev, and M. Siggaard. 2025. Intraday Market Return Predictability Culled from the Factor Zoo. _Management Science_ 71: 7731–7751. 

Antoniou, C., J. A. Doukas, and A. Subrahmanyam. 2013. Cognitive Dissonance, Sentiment, and 

Momentum. _Journal of Financial and Quantitative Analysis_ 48: 245–275. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**28** 

Arnott, R., C. R. Harvey, V. Kalesnik, and J. Linnainmaa. 2019. Alice’s Adventures in Factorland: Three Blunders That Plague Factor Investing. _The Journal of Portfolio Management_ 45: 18–36. Asness, C., S. Chandra, A. Ilmanen, and R. Israel. 2017. Contrarian Factor Timing Is Deceptively Difficult. _The Journal of Portfolio Management_ 43: 72–87. 

Asness, C. S. 2016. Invited Editorial Comment: The Siren Song of Factor Timing Aka “Smart Beta Timing” Aka “Style Timing”. _The Journal of Portfolio Management_ 42: 1–6. Asness, C. S., T. J. Moskowitz, and L. H. Pedersen. 2013. Value and Momentum Everywhere. _The Journal of Finance_ 68: 929–985. Avramov, D., S. Cheng, and L. Metzker. 2023. Machine Learning vs. Economic Restrictions: Evidence from Stock Return Predictability. _Management Science_ 69: 2587–2619. Baba Yara, F., M. Boons, and A. Tamoni. 2021. Value Return Predictability across Asset Classes and Commonalities in Risk Premia. _Review of Finance_ 25: 449–484. 

Bender, J., X. Sun, R. Thomas, and V. Zdorovtsov. 2018. The Promises and Pitfalls of Factor Timing. _The Journal of Portfolio Management_ 44: 79–92. 

Bianchi, D., M. Buchner, and A. Tamoni. 2021. Bond Risk Premiums with Machine Learning. € _The Review of Financial Studies_ 34: 1046–1089. 

Bryzgalova, S., M. Pelger, and J. Zhu. 2025. Forest Through the Trees: Building Cross-Sections of Stock Returns. _The Journal of Finance_ 80: 2447–2506. 

Cakici, N., C. Fieberg, D. Metko, and A. Zaremba. 2024. Do Anomalies Really Predict Market Returns? New Data and New Evidence. _Review of Finance_ 28: 1–44. 

Campbell, J. Y., and S. B. Thompson. 2008. Predicting Excess Stock Returns out of Sample: Can Anything Beat the Historical Average? _Review of Financial Studies_ 21: 1509–1531. 

Caruana, R. 1997. Multitask Learning. _Machine Learning_ 28: 41–75. Chen, A. Y., and T. Zimmermann. 2022. Open Source Cross-Sectional Asset Pricing. _Critical Finance Review_ 11: 207–264. Chen, L., M. Pelger, and J. Zhu. 2024. Deep Learning in Asset Pricing. _Management Science_ 70: 714–750. 

Chen, P., and G. Zhang. 2007. How Do Accounting Variables Explain Stock Price Movements? Theory and Evidence. _Journal of Accounting and Economics_ 43: 219–244. 

Chinco, A., A. D. Clark-Joseph, and M. Ye. 2019. Sparse Signals in the Cross-Section of Returns. _The Journal of Finance_ 74: 449–492. 

Choi, D., W. Jiang, and C. Zhang. 2025. Alpha Go Everywhere: Machine Learning and International Stock Returns. _The Review of Asset Pricing Studies_ 15: 288–331. 

Cohen, R. B., C. Polk, and T. Vuolteenaho. 2003. The Value Spread. _The Journal of Finance_ 58: 609–641. Cooper, M. J., R. C. Gutierrez Jr, and A. Hameed. 2004. Market States and Momentum. _The Journal of Finance_ 59: 1345–1365. Daniel, K., and T. J. Moskowitz. 2016. Momentum Crashes. _Journal of Financial Economics_ 122: 221–247. 

Dichtl, H., W. Drobetz, H. Lohre, C. Rother, and P. Vosskamp. 2019. Optimal Timing and Tilting of Equity Factors. _Financial Analysts Journal_ 75: 84–102. Didisheim, A., S. B. Ke, B. T. Kelly, and S. Malamud. 2024. APT or “AIPT”? The Surprising Dominance of Large Factor Models. NBER Working Paper 33012 (2024). https://doi.org/10.3386/w33012 Diebold, F. X., and R. S. Mariano. 1995. Comparing Predictive Accuracy. _Journal of Business & Economic Statistics_ 13: 253–263. 

Dong, X., Y. Li, D. E. Rapach, and G. Zhou. 2022. Anomalies and the Expected Market Return. _The Journal of Finance_ 77: 639–681. 

Engelberg, J., R. D. McLean, J. Pontiff, and M. C. Ringgenberg. 2023. Do Cross-Sectional Predictors Contain Systematic Information? _Journal of Financial and Quantitative Analysis_ 58: 1172–1201. Fama, E. F., and K. R. French. 1993. Common Risk Factors in the Returns on Stocks and Bonds. _Journal of Financial Economics_ 33: 3–56. Fama, E. F., and K. R. French. 2015. A Five-Factor Asset Pricing Model. _Journal of Financial Economics_ 116: 1–22. 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**29** 

Feng, G., J. He, N. G. Polson, and J. Xu. 2024. Deep Learning in Characteristics-Sorted Factor Models. _Journal of Financial and Quantitative Analysis_ 59: 3001–3036. Freyberger, J., A. Neuhierl, and M. Weber. 2020. Dissecting Characteristics Nonparametrically. _The Review of Financial Studies_ 33: 2326–2377. Greenwood, R., and S. G. Hanson. 2012. Share Issuance and Factor Timing. _The Journal of Finance_ 67: 761–798. Gu, S., B. Kelly, and D. Xiu. 2020. Empirical Asset Pricing via Machine Learning. _The Review of Financial Studies_ 33: 2223–2273. Gu, S., B. Kelly, and D. Xiu. 2021. Autoencoder Asset Pricing Models. _Journal of Econometrics_ 222: 429–450. Guijarro-Ordonez, J., M. Pelger, and G. Zanotti. 2025. Deep Learning Statistical Arbitrage. _Management Science_ . Forthcoming. Gupta, T., and B. Kelly. 2019. Factor Momentum Everywhere. _The Journal of Portfolio Management_ 45: 13–36. Haddad, V., S. Kozak, and S. Santosh. 2020. Factor Timing. _The Review of Financial Studies_ 33: 1980–2018. Hastie, T., R. Tibshirani, and J. H. Friedman. 2009. _The Elements of Statistical Learning: Data Mining, Inference, and Prediction_ , Vol. 2. New York: Springer. Hochreiter, S., and J. Schmidhuber. 1997. Long Short-Term Memory. _Neural Computation_ 9: 1735–1780. Hodges, P., K. Hogan, J. R. Peterson, and A. Ang. 2017. Factor Timing with Cross-Sectional and Time-Series Predictors. _The Journal of Portfolio Management_ 44: 30–43. Huddleston, D., F. Liu, and L. Stentoft. 2023. Intraday Market Predictability: A Machine Learning Approach. _Journal of Financial Econometrics_ 21: 485–527. Ilmanen, A., R. Israel, R. Lee, T. J. Moskowitz, and A. Thapar. 2021. How Do Factor Premia Vary over Time? A Century of Evidence. _Journal of Investment Management_ 19: 15–57. Jensen, T. I., B. Kelly, and L. H. Pedersen. 2023. Is There a Replication Crisis in Finance? _The Journal of Finance_ 78: 2465–2518. Jensen, T. I., B. T. Kelly, S. Malamud, and L. H. Pedersen. 2026. Machine Learning and the Implementable Efficient Frontier. _The Review of Financial Studies_ 2026: hhag022. https://doi.org/ 10.1093/rfs/hhag022 Kagkadis, A., I. Nolte, S. Nolte, and N. Vasilas. 2024. Factor Timing with Portfolio Characteristics. _The Review of Asset Pricing Studies_ 14: 84–118. Kelly, B., and H. Jiang. 2014. Tail Risk and Asset Prices. _Review of Financial Studies_ 27: 2841–2871. Kelly, B., S. Malamud, and L. H. Pedersen. 2023. Principal Portfolios. _The Journal of Finance_ 78: 347–387. Kelly, B., S. Malamud, and K. Zhou. 2024. The Virtue of Complexity in Return Prediction. _The Journal of Finance_ 79: 459–503. Kelly, B., and S. Pruitt. 2013. Market Expectations in the Cross-Section of Present Values. _The Journal of Finance_ 68: 1721–1756. Kelly, B. T., S. Malamud, and K. Zhou. 2022. The Virtue of Complexity Everywhere. Available at SSRN: https://ssrn.com/abstract=4171581 Kelly, B. T., T. J. Moskowitz, and S. Pruitt. 2021. Understanding Momentum and Reversal. _Journal of Financial Economics_ 140: 726–743. Koijen, R. S., and S. Van Nieuwerburgh. 2011. Predictability of Returns and Cash Flows. _Annual Review of Financial Economics_ 3: 467–491. Kozak, S., S. Nagel, and S. Santosh. 2020. Shrinking the Cross-Section. _Journal of Financial Economics_ 135: 271–292. Leippold, M., Q. Wang, and W. Zhou. 2022. Machine Learning in the Chinese Stock Market. _Journal of Financial Economics_ 145: 64–82. Liu, F. 2020. Can the Premium for Idiosyncratic Tail Risk be Explained by Exposures to its Common Factor? Available at SSRN: https://ssrn.com/abstract=3711215 

_Journal of Financial Econometrics_ , 2026, Vol, 24, Issue 3 

**30** 

Liu, F. 2025. Stock Distribution and Risk Premia Predictability with Quantile Machine Learning. Available at SSRN: https://ssrn.com/abstract=4491887 

Liu, F., and L. Stentoft. 2023. Intraday Stock Predictability Everywhere. Available at SSRN: https:// ssrn.com/abstract=4496917 

McCracken, M. W., and S. Ng. 2016. Fred-md: A Monthly Database for Macroeconomic Research. _Journal of Business & Economic Statistics_ 34: 574–589. 

Moreira, A., and T. Muir. 2017. Volatility-Managed Portfolios. _The Journal of Finance_ 72: 1611–1644. Moskowitz, T. J., Y. H. Ooi, and L. H. Pedersen. 2012. Time Series Momentum. _Journal of Financial Economics_ 104: 228–250. 

Neuhierl, A., O. Randl, C. Reschenhofer, and J. Zechner. 2023. Timing the Factor Zoo. Available at SSRN: https://ssrn.com/abstract=4376898 

Newey, W. K., and K. D. West. 1987. A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix. _Econometrica_ 55: 703–708. 

Polk, C., M. Haghbin, and A. de Longis. 2020. Time-Series Variation in Factor Premia: The Influence of the Business Cycle. _Journal of Investment Management_ 18: 69–89. 

Polk, C., D. Vayanos, and P. Woolley. 2022. Long-horizon Investing in a Non-capm World. Available at SSRN: https://ssrn.com/abstract=4096829 

Proner, R. 2023. A Multi-task Deep Learning Model for Inflation Forecasting: Dynamic Phillips Curve Neural Network. Available at SSRN: https://ssrn.com/abstract=4454118 

Rapach, D., and G. Zhou. 2013. Forecasting Stock Returns. _Handbook of Economic Forecasting_ 2: 328–383. 

Ruder, S. 2017. An Overview of Multi-task Learning in Deep Neural Networks. arXiv, arXiv:1706.05098, preprint: not peer reviewed. https://arxiv.org/abs/1706.05098 

© The Author(s) 2026. Published by Oxford University Press. This is an Open Access article distributed under the terms of the Creative Commons Attribution-NonCommercial License (https:// creativecommons.org/licenses/by-nc/4.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited. For commercial re-use, please contact reprints@oup.com for reprints and translation rights for reprints. All other permissions can be obtained through our RightsLink service via the Permissions link on the article page on our site—for further information please contact journals.permissions@oup.com. Journal of Financial Econometrics, 2026, 24, 1–30 https://doi.org/10.1093/jjfinec/nbag006 Article 

