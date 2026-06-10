_Journal of Financial Econometrics_ , 2025, **23(2)** , nbae018 https://doi.org/10.1093/jjfinec/nbae018 **Article** 

**==> picture [64 x 52] intentionally omitted <==**

## **Large-Dimensional Portfolio Selection with a High-Frequency-Based Dynamic Factor Model** 

## **Simon T. Bodilsen 1,2** 

1Department of Economics and Business Economics, Aarhus University, Aarhus, 8210, Denmark 2Danish Finance Institute, Frederiksberg, 2000, Denmark 

Address correspondence to Simon T. Bodilsen, Department of Economics and Business Economics, Aarhus University, Fuglesangs All�e 4, Aarhus V, 8210, Denmark, or e-mail: sibo@econ.au.dk. 

## **Abstract** 

This article proposes a new predictive model for large-dimensional realized covariance matrices. Using high-frequency data, we estimate daily realized covariance matrices for the constituents of the S&P 500 Index and a set of observable factors. Using a standard decomposition of the joint covariance matrix, we express the covariance matrix of the individual assets similar to a dynamic factor model. To forecast the covariance matrix, we model the components of the covariance structure using a series of autoregressive processes. A novel feature of the model is the use of the data-driven hierarchical clustering algorithm to determine the structure of the idiosyncratic covariance matrix. A simulation study shows that this method can accurately estimate the block structure as long as the number of blocks is small relative to the number of stocks. In an out-of-sample portfolio selection exercise, we find that the proposed model outperforms other commonly used multivariate volatility models in extant literature. 

**Keywords:** big data, hierarchical clustering, high-frequency data, minimum variance portfolio, multivariate volatility 

**JEL classifications:** C55, C58, G11 

This article introduces a new approach for modeling and forecasting the covariance matrix of a high-dimensional vector of stock returns. A precise characterization of the covariance matrix is highly important in many financial applications. In particular, this is the case in risk management and portfolio allocation settings where a reliable forecast of the covariance matrix of the assets is essential. In this study, we put forward a very flexible and easily implementable modeling framework for covariance matrices, by specifying a highfrequency-based dynamic factor model for a potentially large number of stocks. 

Estimating, modeling, and forecasting covariance matrices in a high-dimensional setting are challenged by the fact that the number of unique elements in the matrices is a quadratic function of the number of assets under consideration. Moreover, the requirement of a 

I am grateful to two anonymous referees, Christian Brownlees, Niels Strange Grønborg, Jorge Wolfgang Hansen, Peter Reinhardt Hansen, Anders Bredahl Kock, and Asger Lunde for helpful comments and suggestions. The author acknowledges support from the Danish Finance Institute (DFI). An earlier version of this article has been circulated under the title “Multivariate High-Frequency-Based Factor Model”. 

**Received:** June 20, 2022. **Revised:** February 19, 2024. **Editorial decision:** July 4, 2024. **Accepted:** August 7, 2024 © The Author(s) 2024. Published by Oxford University Press. All rights reserved. For permissions, please email: journals.permissions@oup.com 

**2** _Journal of Financial Econometrics_ 

covariance matrix to be positive definite poses an additional layer of complexity to this process. A typical solution to the former curse of dimensionality problem is the use of factor models (see, e.g., De Nard, Ledoit, and Wolf 2021). Factor models are widely used in finance, and assume in this context that the dynamics of _N_ stock prices are well captured by a _K_ -dimensional vector of factors, with _K_ � _N_ , such that the modeling procedure takes place in much lower-dimensional space relative to the original problem. In this article, we specify a high-frequency-based dynamic factor model for a large number of stocks, where the factors are represented by a low number of observable traded assets. The model is high frequency based in the sense that high-frequency data are utilized to construct realized measures of the components that theoretically determine the covariance structure in the factor model. 

In contrast to existing studies that use a similar framework, we do not assume a specific structure of the idiosyncratic part of the model-implied covariance structure. Strict factor models assume independence between the stocks conditional on the factors leading to a diagonal idiosyncratic covariance matrix. In approximate factor models (Chamberlain and Rothschild 1983), the independence assumption is relaxed and allows for a more general structure of the idiosyncratic part. In this latter setting, a series of papers initialized by Fan, Furger, and Xiu (2016) have suggested that a block structure based on sector or industry groups of the underlying stocks delivers a satisfactory description of the idiosyncratic covariance matrix. We do not pursue this idea in this article per se. Instead, we use the hierarchical clustering (HC) algorithm dating back to Ward (1963) to infer a block structure in the idiosyncratic covariance matrix. Specifically, we exploit the information contained in the idiosyncratic correlation matrices to identify clusters of stocks that are similar as measured by idiosyncratic correlation. Unsupervised learning methods have been widely used in finance (see, e.g., Bollerslev, Patton, and Zhang (2021) and Oh and Patton (2023) for recent applications). But to our best knowledge, this article is the first to infer a block structure of the idiosyncratic covariance matrix in a factor model setting using this technique. 

The use of realized measures in covariance modeling has generally been employed in two ways. One way to benefit from realized measures is to use them as a driving factor for the latent conditional covariance instead of outer products of daily returns in multivariate GARCH models. Examples of such approaches include the multivariate HEAVY model of Noureldin, Shephard, and Sheppard (2012) and its extensions with heavy tails and a factor structure proposed, respectively, by Opschoor, Janus, Lucas, and Van Dijk (2018) and Sheppard and Xu (2018). 

The second approach relies solely on the time series of the realized measures to predict future realizations of the daily covariance matrix. For example, Chiriac and Voev (2011) propose a fractional integrated model for the time series of Cholesky factors of a realized covariance matrix, Golosnoy, Gribisch, and Liesenfeld (2012) propose the conditional autoregressive Wishart model, while Oh and Patton (2016) combined the ideas of the DCC model (Engle 2002) and the heterogeneous autoregressive (HAR) model (Corsi 2009) in the HAR-DRD model. 

We continue along these lines and propose a new predictive high-frequency-based factor model, that is particularly well-suited for settings in which the number of assets is large. Using high-frequency prices of the individual assets and of observable factors represented by exchange-traded funds (ETFs) tracking the S&P 500 Index and its sectors, we construct daily estimates of the components determining the covariance structure using the multivariate realized kernel (MRK) estimator of Barndorff-Nielsen, Hansen, Lunde, and Shephard (2011). To break the curse of dimensionality, we suggest modeling these three components separately using autoregressive time series models, to combine these into a forecast of the covariance matrix of the individual assets. 

Bodilsen j Large-Dimensional Portfolio Selection **3** 

The proposed model is attractive from a practical point of view. First, the model is highly scalable in the sense that it can easily handle situations with hundreds of assets. Second, although the number of parameters can be quite large, the number of parameters only grows linearly with the number of assets and can be estimated in closed form using ordinary least squares. No numerical optimization is required, which implies that model estimation is incredibly fast even in the case where the asset universe consists of the constituents of the S&P 500 Index. Third, the model framework allows for a data-driven approach to determine the structure of the idiosyncratic covariance matrix, which is a novel feature of the proposed model. The model is related to, but distinct from, the model independently proposed by Alves, de Brito, Medeiros, and Ribeiro (2024). For example, we use a different strategy to model the factor and idiosyncratic covariance matrix and further estimate the block structure in the idiosyncratic covariance matrix. 

In the empirical analysis, we use our newly developed model in a portfolio allocation setting, using the constituents of the S&P 500 Index as the asset universe. In an out-of-sample analysis, we provide evidence showing that variants of our model can outperform existing popular dynamic covariance models in the sense of lower ex-post portfolio standard deviation both at the daily and weekly horizons. Moreover, we show that models based on our methodology result in portfolios with a much lower measure of turnover. Another key finding of the present study is that the use of a data-driven approach to determine the structure of the idiosyncratic covariance matrix outperforms the sector-based approach considered in extant literature in the portfolio selection application. 

The remainder of the article is organized as follows. In Section 1, we introduce the model framework. Section 2 presents the econometric framework underlying the predictive model. Section 4 presents the results of a simulation study. In Section 5, we present alternative covariance models, and Section 7 introduces the portfolio allocation problems studied in the empirical part. In Section 7, we discuss the data sources, provide in-sample insights from the model, and present the results of the out-of-sample portfolio allocation analyses. Section 8 concludes. 

## **1 Model Framework** 

The underlying model is a slightly modified version of the framework put forward by Fan et al. (2016). We consider a financial market with _N_ risky assets for which the logarithmic prices are described by a stochastic process _p_ . The price process is assumed to follow the continuous-time factor model 

**==> picture [210 x 10] intentionally omitted <==**

where _ft_ is a _K_ -dimensional vector of observed factor prices, _zt_ is the idiosyncratic component, and _βt_ is an _N_ × _K_ matrix of factor loadings. Vast empirical evidence exists proving time-variation in the systematic risk factors (see, e.g., Andersen, Bollerslev, Diebold, and Wu 2006; Barndorff-Nielsen and Shephard, 2004). To take this fact into account and still allow for easy identification of the factor loadings, we will assume that _βt_ is constant within the trading day.[1 ] By using the convention that a trading day has unit length, we can state this assumption as _βt_ ¼ _β_ d _t_ e for _t_ 2 R þ , where d�e is the ceiling function. 

> 1 We note, that the hypothesis of constant market beta within the trading day has been investigated and rejected in a recent paper by Andersen, Thyrsgaard, and Todorov (2021). They find evidence that crosssectional dispersion of market betas on the U.S. stock market declines throughout the trading day, leading to a compression of market betas towards one. 

**4** _Journal of Financial Econometrics_ 

We will assume that the factor prices and the idiosyncratic component evolve according to continuous Ito semimartingales of the form ^ 

**==> picture [247 x 52] intentionally omitted <==**

where _W_[ð] _[f]_[Þ] and _W_ ð _[z]_ Þ are independent standard Brownian motions. The drift processes ~ _at_ and _b_[~] _t_ are assumed to be progressively measurable, and the instantaneous covolatility processes _θt_ and _γt_ are c�adl�ag. Following Fan et al. (2016), we impose the exogeneity condition of zero quadratic covariation between _f_ and _z_ , that is, ½ _f ; z_ � _t_ ¼ 0 for all _t_ . The main objects of interest are the increments of the quadratic variation process of _p_ . Define the instantaneous covariance matrix of _f_ and _z_ to be Q _t_ ¼ _θtθ_[0] _t_[and ][G] _[t]_[ ¼] _[ γ] t[γ]_[0] _t_[, respec-] tively. Further, we define ½ _x_ � _[t] s_[¼ ½] _[x]_[�] _t[−]_[½] _[x]_[�] _s_[to be the increment in the quadratic variation pro-] cess for a generic semimartingale _x_ over the interval from _s_ to _t_ . Under the model structure – as described by Equations (1) (3), the quadratic variation process of _p_ reads in this setup 

**==> picture [363 x 82] intentionally omitted <==**

1.1 Specification of the Idiosyncratic Covariance Structure 

In the factor modeling literature, it is standard to impose a sparsity condition on the idiosyncratic covariance matrix. In a strict factor model, it is assumed that ½ _z_ � _t_ is a diagonal matrix, whereas approximate factor models also impose sparsity but allow the idiosyncratic covariance matrix to be non-diagonal (Chamberlain and Rothschild 1983). We will assume that ½ _z_ � _t_ is a block diagonal matrix with 1 _< M_ ≤ _N_ blocks. Hence, we have the following representation 

**==> picture [238 x 12] intentionally omitted <==**

where each ½ _z_ � _i;t_ is of dimension _Ni_ × _Ni_ with[P] _[M] i_ ¼1 _[N][i]_[ ¼] _[ N]_[.] 

Let S _t_ denote the set of non-zero entries in ½ _z_ � _t_ , and hence contain all information about the block structure. In contrast to many studies employing a similar modeling framework as presented here (e.g., Aït-Sahalia and Xiu 2017; Alves et al. 2024; Fan et al. 2016), we will assume that S _t_ is unknown and must be inferred from data. A typical approach in the literature is to assume that S _t_ is deterministic and time-invariant and that its structure is determined either by imposing a diagonal structure or by grouping firms within the same sector or industry to the same block. The latter choice is empirically appealing, and it leads to an intuitive and economically motivated estimator of the idiosyncratic covariance matrix (Fan et al. 2016). However, this choice does not necessarily provide the optimal description of the idiosyncratic risk. In particular, the structure of ½ _z_ � _t_ depends crucially on the number of common factors that are employed and their ability to explain the cross-sectional variations in stock prices. 

Bodilsen j Large-Dimensional Portfolio Selection **5** 

To consider these concerns, we suggest using a data-driven approach to determine the structure of the idiosyncratic covariance matrix, for a given choice of observable factors. We use the HC method to find clusters of stocks that are similar as measured by idiosyncratic correlation and thereby provide us with an estimate of the unknown S _t_ . Hence, in this setting, we do not assume a specific type of factor model, but instead, we let data inform us to select the most appropriate model structure. 

## **2 Econometric Identification of the Factor Model Covariance Structure** 

This section describes how we construct estimates of the components determining the covariance structure as given by Equations (4) and (5) using observed data. 

From (4), it follows that we can write the increment of the quadratic variation of _p_ between integer time instants _s_ and _t_ as 

**==> picture [324 x 26] intentionally omitted <==**

implying that the quadratic variation over multiple days is obtained by adding up the daily increments of the quadratic variation process. As a consequence, we only need to study the estimation and prediction of the daily quadratic variation, which we will denote by S _t_ � S _t −_ 1: _t_ . 

## 2.1 High-Frequency-Based Covariance Estimation 

To estimate S _t_ , we consider an approach in which we estimate the daily quadratic variation process of the joint process _yt_ ¼ � _p_[0] _t[;][f] t_[ 0] �0 2 R _N_ þ _K_ using observed intra-day prices. Due to the imposed model structure and the assumptions of zero quadratic covariation between _f_ and _z_ and piecewise constant betas, it follows that the daily increments of the quadratic variation process of _y_ can be expressed as 

**==> picture [120 x 29] intentionally omitted <==**

High-frequency-based estimation of large-dimensional covariance matrices is notoriously difficult due to the problems arising from market microstructure noise, asynchronicity, and the requirement of positive semidefiniteness. In this article, we use the MRK estimator of Barndorff-Nielsen et al. (2011) as the estimator of ½ _y_ � _[t] t −_ 1[. We implement it us-] ing the non-stochastic Parzen kernel function with a bandwidth chosen according to the recommendation of Barndorff-Nielsen et al. (2011). The MRK estimator is a consistent estimator for the quadratic variation ½ _y_ � _[t] t −_ 1[and is further guaranteed to be positive semidefin-] ite and robust to certain types of market microstructure noise in the observed prices.[2] Denote by _Yt_ the MRK estimate of ½ _y_ � _[t] t −_ 1[, which, without loss of generality, can be fur-] ther decomposed as 

**==> picture [96 x 29] intentionally omitted <==**

> 2 A potential drawback of this method is the requirement of using a homogeneous series of high-frequency prices across all assets. Typically, this is solved by refresh-time sampling (Barndorff-Nielsen et al. 2011; Harris, McInish, Shoesmith, and Wood 1995). However, this would typically imply a massive data loss in largedimensional settings. For this reason, we opt to use prices that are sampled every 30 seconds using the previous tick method in this study. 

**6** _Journal of Financial Econometrics_ 

where _Y_ ð1 _;_ 1Þ _;t_[is an ] _[N]_[ ×] _[ N ]_[matrix, ] _[Y]_ ð2 _;_ 2Þ _;t_[is a ] _[K]_[ ×] _[ K ]_[matrix, and ] _[Y]_ ð1 _;_ 2Þ _;t_[is an ] _[N]_[ ×] _[ K ]_[matrix. ] Now, since _Yt_ is a consistent estimate of ½ _y_ � _[t] t −_ 1[, it readily follows from the model assump-] tions that 

**==> picture [248 x 52] intentionally omitted <==**

such that, given the availability of _Yt_ , consistent estimates of the components determining the covariance structure of _p_ are given as simple byproducts hereof. In particular, an initial estimate of S _t_ can be formed as 

**==> picture [236 x 14] intentionally omitted <==**

## 2.2 Estimation of the Block Structure via Hierarchical Clustering 

The estimate S[^] _t_ in Equation (7) does not incorporate any information about the assumed structure of the idiosyncratic covariance matrix, that is, S _t_ . As mentioned in the previous section, we use the HC method to infer S _t_ . 

The HC method is an agglomerative clustering algorithm. In this setting, it means that each of the _N_ assets initially represents a singleton cluster. At each of the remaining _N−_ 1 steps of the algorithm, the two most similar clusters—as defined by a measure of distance between clusters—are merged. After the final step of the algorithm, all assets will belong to the same cluster, and the block structure can be determined by “cutting the tree” at a certain threshold value. Hence, the HC algorithm does not pre-select the number of clusters in the data. To implement the HC method, it requires the user to supply a distance measure between each pair of assets, and a so-called linkage criterion to determine the distance between clusters based on the pairwise distances. 

To measure the similarity between the _N_ stocks, we use the information contained in the daily idiosyncratic correlation matrices, which are obtained by transforming each _Zt_ into a correlation matrix. We suggest to measure the pairwise dissimilarity between asset _i_ and _j_ up to time _t_ as 

**==> picture [235 x 11] intentionally omitted <==**

where _ρ_ ð _i;j_ Þ _;t_[is the average daily idiosyncratic correlation between assets ] _[i ]_[and ] _[j ]_[over some ] pre-specified horizon of time. Using the absolute value of _ρ_ ð _i;j_ Þ _;t_[, we capture the fact that ] assets that, on average, have a large negative idiosyncratic correlation also can be regarded as being similar in some sense too. 

We employ the complete linkage criterion to define the distance between two clusters.[3 ] Under complete linkage the distance between two clusters A and B is defined as 

**==> picture [150 x 15] intentionally omitted <==**

> 3 Several other linkage criteria have also been used in applied work. This includes the single-linkage criterion (minimum distance clustering), the unweighted average linkage criterion, and Ward’s minimum variance linkage criterion. See also the survey of Murtagh and Contreras (2012) for an overview of the different linkage criteria in HC. Based on our analysis, we find the complete linkage criterion to deliver the most satisfactory clustering assignments in practice. 

Bodilsen j Large-Dimensional Portfolio Selection **7** 

Let C[ð] 1 _[τ] ;_[Þ] _t[;]_[...] _[;]_[C][ð] _M[τ]_[Þ] _;t_[�] f[1] _[;]_[...] _[;][N]_ g denote the clusters of stocks detected by the HC algorithm using a threshold value _τ_ 2 ð0 _;_ 1Þ to cut the tree, where 

**==> picture [202 x 27] intentionally omitted <==**

Our estimate of S _t_ is then formed by setting 

**==> picture [310 x 17] intentionally omitted <==**

The estimate of the idiosyncratic covariance matrix that takes the inferred block structure into account, is then given by the following hard-thresholded version of _Zt_ 

**==> picture [124 x 16] intentionally omitted <==**

where **1** �ð Þ denotes the indicator function, such that for all pairs ð _k; l_ Þ 62 _St_ we have ð Þ _Z[S]_ ð _k;l_ Þ _;t_[¼][ 0. Using ][Equation (6)][, it follows that we can estimate the quadratic variation of ] _[p ]_ between _t−_ 1 and _t_ by 

**==> picture [224 x 16] intentionally omitted <==**

ð Þ By repeating this procedure on each day, we obtain the time series of _Bt_ , _Ft_ , and _Zt[S]_[, which ] can be dynamically modeled to construct a conditional model for S _t_ . It should be noted that since _Yt_ is symmetric positive definite, it is easy to verify that _Ft_ and _Zt_ (and hence also ð Þ ð _S_ Þ _Zt[S]_[) are symmetric positive definite, which, in turn, implies that both ][S][^] _t_[and ][S][^] _t_[are sym-] metric positive definite. 

## **3 Forecasting Methodology** 

In this section, we describe the modeling approach utilized to construct forecasts of the covariance matrix of the _N_ assets. We will work under the general framework that the predictive horizon of interest is _h_ days. Initially, we consider the problem of producing one-day-ahead covariance forecasts. A more general _h_ -days-ahead forecasting procedure is outlined in the Supplementary Appendix. 

Based on representation (10), we propose to produce one-period forecasts of S _t_ þ 1 conditional on time _t_ information by 

**==> picture [255 x 13] intentionally omitted <==**

That is, the forecast of the covariance matrix of _p_ is obtained by combining forecasts of the factor loadings, the factor covariance matrix, and the idiosyncratic covariance matrix. Due to the model assumptions of independence between the factors and the idiosyncratic part, we can forecast these components completely separately. 

## 3.1 Forecasting the Factor Covariance Matrix 

The key building block for forecasting the covariance matrix of the common observable factors is the HAR-DRD model developed in Oh and Patton (2016), which combines the 

**8** _Journal of Financial Econometrics_ 

ideas of the dynamic conditional correlation (DCC) model by Engle (2002) with the heterogeneous autoregressive (HAR) model of Corsi (2009).[4 ] The DCC approach relies on the decomposition 

**==> picture [265 x 71] intentionally omitted <==**

where _Dt_ is a diagonal matrix of factor volatilities and _Rt_ is the correlation matrix of the factors. In the original DCC model of Engle (2002), a two-step procedure is employed to construct a conditional model for the covariance matrix of a vector of stock returns. In the first step, the conditional variances are modeled using univariate GARCH models. In the second step, the conditional covariance matrix of the devolatilized vector of returns is modeled and is subsequently transformed into a correlation matrix. In the present, we follow the approach suggested in Oh and Patton (2016). They propose to use the HAR model directly on the realized variances and correlations to capture the empirical evidence of longrange dependence in these series. 

We model each component of _Dt_ separately and follow the common practice in the literature (e.g., Corsi and Reno 2012� ) of specifying the HAR model for the logarithmic variances 

**==> picture [309 x 14] intentionally omitted <==**

where _xi;t_ ¼ log _F_ ð _i;i_ Þ _;t[;][ x]_ ð _i;[h] t_ Þ[¼] 1 _h_ P _hs_ ¼1 _[x][i][;][t][−][s]_[þ][1 ][for ] _[h]_[ 2][ N][, and ] _[ε][i][;][t ]_[is a zero mean error term ] which can take on values on the entire real line. Due to the log specification, the forecast of _F_ ð _i;i_ Þ _;t_[will always be strictly positive. The log-specification induces a Jensen’s inequality bias ] in the forecast of _F_ ð _i;i_ Þ _;t_[, if the reverse transformation is used. To avoid this bias, we use a ] bootstrap approach. After having estimated the model, we obtain the residuals and draw a bootstrap sample from the residuals of length _L_ with replacements. The demeaned bootstrap _L_ sample will be denoted as � _ε_[�] _i;l_ � _l_ ¼1[. Our prediction of ] _[F]_ ð _[i][;][i]_ Þ _;t_ þ 1[is then given as the average ] 

**==> picture [253 x 27] intentionally omitted <==**

^ where _xi;t_ þ 1 is the fitted value from the regression in Equation (15). 

For the correlation part, represented by _Rt_ , we follow the suggestion in Oh and Patton (2016) and model all unique elements of _Rt_ jointly as a restricted HAR model. Let _ρt_ denote the vectorized strictly lower triangular of _Rt_ , and let _ρ_ � ¼ _T_ 1 P _Tt_ ¼1 _[ρ] t_[denote the sample aver-] age of _ρt_ . The _K_ ð _K −_ 1Þ _=_ 2-dimensional vector _ρt_ is then modeled using the following parsimonious specification 

**==> picture [295 x 14] intentionally omitted <==**

> 4 The HAR-DRD model is also used in several recent related studies such as Bollerslev, Patton, and Quaedvlieg (2018), Buccheri, Livieri, Pirino, and Pollastri (2020), and Vassallo, Buccheri, and Corsi (2021). 

Bodilsen j Large-Dimensional Portfolio Selection **9** 

where _c_ 1 _; c_ 2 _; c_ 3 are scalar parameters with the side restriction[P][3] _i_ ¼1 _[c][i][ <]_[1. The error term ] _[η][t ]_ is assumed to have zero mean and follow a distribution with support on the space of differences of correlation matrices. To reduce the number of parameters, “correlation targeting” is used to remove the intercept parameters. 

The models in Equations (15) and (17) are estimated using ordinary least squares (OLS). The forecast _Ft_ þ 1j _t_ is obtained from Equations (12)–(14) using the predicted values from Equations (16) and (17). It readily follows from Theorem 2 in Oh and Patton (2016) that the forecast _Ft_ þ 1j _t_ is positive definite since the original time series of _Ft_ are all positive definite by construction. 

## 3.2 Forecasting of Factor Loadings 

As previously explained, the _N_ × _K_ matrix of factor loadings is assumed to be constant within the day but can vary freely between different days. To model the daily dynamics of the factor loadings, we specify a HAR-type model similar to the one exploited for the correlations in the factor covariance matrix. In Alves et al. (2024), they find evidence that the factor loadings have long memory and model each of the _NK_ unique components using an unrestricted HAR model. This approach requires the estimation of 4 _NK_ unknown parameters. To enforce parsimony, we suggest the following “beta targeting” representation 

**==> picture [234 x 13] intentionally omitted <==**

where _bt_ ¼ vecð _Bt_ Þ 2 R _[NK ]_ and _b_[�] ¼ _T_ 1 P _Tt_ ¼1 _[b][t]_[. The error term ] _[ξ][t ]_[is assumed to have mean ] zero and having a support over the entire R _[NK]_ . Thus, we can once again resort to OLS as the estimation method. 

## 3.3 Forecasting of the Idiosyncratic Covariance Matrix 

The final ingredient for constructing a forecast of the covariance matrix of the asset returns is a forecast of the covariance of the idiosyncratic part of the price process. Ideally, the _K_ common factors _f_ should explain all co-movements among the assets leading to a strict factor model, such that _Zt_ is a diagonal matrix. Empirically, we find the diagonal assumption on _Zt_ to be violated even for a large number of factors. Hence, using the methodology described in Section 3, we use HC to determine the set of non-zero entries in the idiosyncratic covariance matrix. Given an estimate of the block structure, _St_ , we can write 

**==> picture [237 x 13] intentionally omitted <==**

and construct a forecast of the idiosyncratic covariance matrix _Zt_ þ 1j _t_ by modeling and forecasting each of the _M_ components separately using the HAR-DRD model as also used for the factor covariance matrix. That is, we model the diagonal elements using Equation (15), and the lower off-diagonal elements of the corresponding correlation matrices using Equation (17). Since a block-diagonal matrix is positive definite if all of its blocks are positive definite, it follows that the forecast _Zt_ þ 1j _t_ is a positive definite matrix. 

## 3.4 Combining the Parts 

The forecast of the daily covariance matrix of the _N_ assets is constructed using Equation ð Þ (11), using the forecast of _Bt_ , _Ft_ , and _Zt[S]_[as just described. Since ] _[F] t_ þ 1j _t_[and ] _[Z] t_ þ 1j _t_[are sym-] metric and positive definite, it follows immediately that S _t_ þ 1j _t_ is a symmetric positive definite matrix, and hence it constitutes a well-defined covariance matrix. 

The model is appealing from a practical point of view. Given the time series of the highfrequency-based covariance matrices, the model only requires the user to run the HC 

**10** _Journal of Financial Econometrics_ 

algorithm and a sequence of OLS regressions. This means that no time-consuming numerical optimization techniques are required. This makes the estimation procedure very fast even in a very high-dimensional setting. For the model to be empirically successful, it is of utmost importance that we can obtain a reliable estimate of the latent daily covariance matrix. Everything in S _t_ þ 1j _t_ depends on the realized covariance matrices, and hence a poor estimate of S _t_ can completely deteriorate the model’s performance. 

The dynamic multivariate volatility model put forward in this article nests the HARDRD model of Oh and Patton (2016) as a special case. When we discard the factor structure ( _K_ ¼ 0) and use a single block ( _M_ ¼ 1) in Equation (18), we effectively reduce the model to the HAR-DRD model. In the following, we will refer to our predictive multivariate volatility model as the CLUstered High-Frequency-based Factor (CLUHFF) model. 

## **4 Simulation Study** 

## 4.1 Simulation Setup 

In this section, we conduct a simulation study to investigate to which extent our proposed HC methodology can detect the correct block structure in the idiosyncratic covariance matrix using synthetic data. 

We simulate _N_ -dimensional log price processes as special cases of the model described – by Equations (1) (5). We specify the following model 

**==> picture [70 x 10] intentionally omitted <==**

with d _ft_ ¼ _θt_ d _Wt_[ð] _[f]_[Þ] and d _zt_ ¼ _γt_ d _Wt_ ð _[z]_ Þ[. Following ][Aït-Sahalia and Xiu (2017)][, we model ] the factor volatilities as Cox-Ingersoll-Ross (CIR) processes: 

**==> picture [216 x 18] intentionally omitted <==**

where _W_[~] _j_ is a standard Brownian motion. We set _κ_[ð] _[f]_[Þ] ¼ 1 _; ξ_[ð] _[f]_[Þ] ¼ 0 _:_ 0001, and _ϕ_[ð] _[f]_[Þ] ¼ 0 _:_ 01. To model dependence between the factors, we generate a _K_ -dimensional correlated Brownian motion, where the correlation structure is simulated using the method proposed in Archakov, Hansen, and Luo (2023), by drawing a uniform distributed vector of dimension _K_ ð _K −_ 1Þ _=_ 2 on the interval from ½ _−_ 0 _:_ 8 _;_ 0 _:_ 8�, and then using the transformation given in Archakov and Hansen (2021) to construct the corresponding correlation matrix. The factor loadings _β_ are held constant in time. We draw the first column of _β_ from the uniform distribution _U_ ð0 _:_ 25 _;_ 1 _:_ 75Þ to mimic a market factor, and for _K >_ 1, simulate the remaining _K−_ 1 columns of _β_ independently from _U_ ð _−_ 0 _:_ 25 _;_ 0 _:_ 25Þ. 

The idiosyncratic volatilities are also assumed to be CIR processes but with parameters � _κ_ ð _[z]_ Þ _; ξ_ ð _[z]_ Þ _; ϕ_ ð _z_ Þ� ¼ ð1 _;_ 0 _:_ 00015 _;_ 0 _:_ 01Þ. The number of blocks in the idiosyncratic covariance matrix is fixed to _M_ in each simulation, and we randomly assign the number of assets ð _Ni_ Þ in each block. To model dependence within each block, we generate a block-correlated Brownian motion, where the correlation structure within each block is simulated using the method of Archakov et al. (2023). In this case, we draw for each _i_ ¼ 1 _;_ ... _; M_ a vector of dimension _Ni_ ð _Ni −_ 1Þ _=_ 2, where the marginal distribution of each element is equal to the law of the random variable 

**==> picture [295 x 13] intentionally omitted <==**

where IGð _a; b_ Þ **1** ð _c;d_ Þ[denotes the inverse Gaussian distribution with mean ] _[a ]_[and shape ] _[b ]_ truncated to the interval ( _c_ , _d_ ). The chosen calibration of the parameters ensures, for all 

Bodilsen j Large-Dimensional Portfolio Selection **11** 

values of _Ni_ , that the off-diagonal elements of the corresponding _Ni_ × _Ni_ correlation matrix are strictly positive and that they most likely fall in the region between 0.03 and 0.30 with an average of approximately 0.10. Thus, we only allow for a relatively weak idiosyncratic correlation among the stocks making this a hard test for the clustering method. 

We simulate 23,400 prices for each day using a Euler scheme. This corresponds to an observation frequency of one second assuming a trading day of 6.5 hours. To account for market microstructure noise, we add independent Gaussian noise with mean zero and variance _ω_[2 ] to the simulated log prices. To model the asynchronicity of the data, we sample the prices according to a Poisson process sampling scheme with common parameter _λi_ , so that, on average, we observe 23,400/ _λi_ observations per asset each day. The asynchronous and noise-contaminated prices are rounded to two decimal points in line with the observed prices during our sample period. We select the _λi_ parameters, such that we, on average, have 15,000 daily price observations available across the stocks. 

Using the asynchronous and noisy prices, we estimate the components of the quadratic variation of _p_ using the methodology described in Section 3.1 and estimate the number of blocks in the idiosyncratic covariance matrix as outlined in Section 3.2. Throughout this simulation study, we fix _N_ ¼ 400 to investigate the properties of our method in a large-dimensional case corresponding to our empirical analysis. We simulate _T_ ¼ 200 days of data and repeat this 100 times. This is done under different parameter settings. The model parameters that we vary are _K_ 2 f1 _;_ 5g _; ω_[2] 2 �0 _;_ 7 × 10 _[−]_[8] _;_ 28 × 10 _[−]_[8] �, and _M_ 2 f5 _;_ 11 _;_ 25 _;_ 74 _;_ 400g. The values considered for the noise variance correspond to (i) no noise, (ii) the level of noise estimated from our empirical data using the estimator of Barndorff-Nielsen, Hansen, Lunde, and Shephard (2009), and (iii) a high-noise scenario. The number of blocks corresponds to a homogeneous case with few blocks ( _M_ ¼ 5), Global Industrial Classification Standard (GICS) sector segmentation ( _M_ ¼ 11), GICS industry groups ( _M_ ¼ 25), GICS industries ( _M_ ¼ 74), and a strict factor model ( _M_ ¼ 400). The HC algorithm uses complete linkage and the dissimilarity measure defined in Equation (8). To select the number of clusters, we consider eight cut-off values of _τ_ ranging from 0.95 to 0.9999. 

To measure the performance of the method, we report four different performance metrics: 

- i) The average number of estimated blocks ( _M_[^] Þ, 

- ii) The average Rand Index (RI) of Rand (1971) to measure the similarity between the estimated ( _S_ ) and true cluster assignments (SÞ, where a value of one represents perfect agreement between _S_ and S, 

- iii) The proportion of simulations with _S_ ¼ S, 

- iv) The average root-mean-squared error (RMSE) of the estimated idiosyncratic correlations. 

## 4.2 Simulation Results 

The results of the simulation study are summarized in Tables 1–2.[5] 

In Table 1, we consider the case of a one-factor model 8. In Panel (a), the no-noise case is considered, and we find that irrespective of the value of _M_ , the HC method can always estimate the correct block structure. This is also reflected in an average RMSE of the estimated idiosyncratic correlations of around 0.006. However, the cut-off value needed to ensure a perfect block detection differs according to the size of _M_ . For a small number of blocks, a 

> 5 In Supplementary Appendix Table IA.2, we further present simulation results for a correctly specified fivefactor model. The results and conclusions are very similar to those presented in Table 1, and therefore not included in the main text. 

**12** _Journal of Financial Econometrics_ 

|**_M_**¼**5**<br>**_M_**¼**11**<br>**_M_**¼**25**<br>**_M_**¼**74**<br>**_M_**¼**400**|_τ_<br>^**_M_**<br>**RI**<br>**_S_**¼ S<br>^**_M_**<br>**RI**<br>**_S_**¼ S<br>^**_M_**<br>**RI**<br>**_S_**¼ S<br>^**_M_**<br>**RI**<br>**_S_**¼ S<br>^**_M_**<br>**RI**<br>**_S_**¼ S|Panel (a):_ω_2¼0|Corr. RMSE:<br>0.006<br>0.006<br>0.006<br>0.006<br>0.006|0.9500<br>41.150<br>0.835<br>0.000<br>74.530<br>0.921<br>0.000<br>107.210<br>0.968<br>0.000<br>166.460<br>0.991<br>0.000<br>400.000<br>1.000<br>1.000|0.9600<br>20.620<br>0.883<br>0.000<br>45.480<br>0.934<br>0.000<br>75.830<br>0.973<br>0.000<br>133.890<br>0.993<br>0.000<br>400.000<br>1.000<br>1.000|0.9700<br>8.980<br>0.958<br>0.010<br>22.400<br>0.964<br>0.000<br>43.920<br>0.985<br>0.000<br>93.740<br>0.997<br>0.000<br>399.990<br>1.000<br>0.990|0.9800<br>5.180<br>0.998<br>0.820<br>11.520<br>0.998<br>0.550<br>25.920<br>0.999<br>0.420<br>74.840<br>1.000<br>0.420<br>373.380<br>1.000<br>0.000|0.9900<br>5.000<br>1.000<br>1.000<br>11.000<br>1.000<br>1.000<br>25.000<br>1.000<br>1.000<br>73.870<br>1.000<br>0.880<br>194.490<br>0.997<br>0.000|0.9950<br>5.000<br>1.000<br>1.000<br>11.000<br>1.000<br>1.000<br>25.000<br>1.000<br>1.000<br>72.250<br>1.000<br>0.140<br>123.230<br>0.994<br>0.000|0.9990<br>5.000<br>1.000<br>1.000<br>11.000<br>1.000<br>1.000<br>24.980<br>1.000<br>0.980<br>52.410<br>0.995<br>0.000<br>53.470<br>0.982<br>0.000|0.9999<br>5.000<br>1.000<br>1.000<br>10.990<br>1.000<br>0.990<br>19.110<br>0.987<br>0.000<br>19.300<br>0.959<br>0.000<br>19.550<br>0.946<br>0.000|Panel (b):_ω_2¼7×10_−_8|Corr. RMSE:<br>0.037<br>0.038<br>0.038<br>0.039<br>0.038|0.9500<br>17.840<br>0.904<br>0.000<br>36.450<br>0.948<br>0.000<br>58.070<br>0.981<br>0.000<br>104.230<br>0.995<br>0.000<br>248.560<br>0.977<br>0.000|0.9600<br>8.980<br>0.965<br>0.000<br>20.870<br>0.974<br>0.000<br>38.020<br>0.991<br>0.000<br>82.330<br>0.996<br>0.000<br>208.300<br>0.954<br>0.000|0.9700<br>5.330<br>0.998<br>0.690<br>12.410<br>0.996<br>0.240<br>26.870<br>0.999<br>0.140<br>70.560<br>0.995<br>0.000<br>161.480<br>0.922<br>0.000|0.9800<br>5.010<br>1.000<br>0.990<br>11.010<br>1.000<br>0.990<br>25.040<br>1.000<br>0.880<br>63.060<br>0.990<br>0.000<br>102.840<br>0.871<br>0.000|0.9900<br>5.000<br>1.000<br>1.000<br>11.000<br>1.000<br>1.000<br>24.590<br>1.000<br>0.620<br>47.240<br>0.976<br>0.000<br>51.560<br>0.789<br>0.000|0.9950<br>5.000<br>1.000<br>1.000<br>11.000<br>1.000<br>1.000<br>23.060<br>0.996<br>0.050<br>32.590<br>0.957<br>0.000<br>32.170<br>0.729<br>0.000|0.9990<br>5.000<br>1.000<br>1.000<br>10.780<br>0.998<br>0.780<br>15.440<br>0.967<br>0.000<br>15.630<br>0.913<br>0.000<br>15.070<br>0.665<br>0.000|0.9999<br>4.820<br>0.990<br>0.820<br>6.010<br>0.903<br>0.000<br>6.380<br>0.860<br>0.000<br>6.260<br>0.806<br>0.000<br>6.280<br>0.582<br>0.000|Panel (c):_ω_2¼28×10_−_8|Corr. RMSE:<br>0.064<br>0.066<br>0.066<br>0.067<br>0.067|0.9500<br>13.800<br>0.936<br>0.000<br>27.980<br>0.964<br>0.000<br>45.690<br>0.985<br>0.000<br>84.120<br>0.972<br>0.000<br>163.790<br>0.861<br>0.000|0.9600<br>7.740<br>0.979<br>0.050<br>17.240<br>0.985<br>0.000<br>32.680<br>0.991<br>0.000<br>70.270<br>0.962<br>0.000<br>133.670<br>0.818<br>0.000|0.9700<br>5.340<br>0.998<br>0.700<br>11.840<br>0.998<br>0.390<br>26.200<br>0.994<br>0.070<br>60.120<br>0.949<br>0.000<br>98.760<br>0.762<br>0.000|0.9800<br>5.020<br>1.000<br>0.980<br>11.050<br>1.000<br>0.940<br>24.780<br>0.993<br>0.120<br>49.470<br>0.930<br>0.000<br>59.430<br>0.697<br>0.000|0.9900<br>5.000<br>1.000<br>1.000<br>10.980<br>1.000<br>0.970<br>22.410<br>0.985<br>0.010<br>30.600<br>0.894<br>0.000<br>31.180<br>0.613<br>0.000|0.9950<br>5.000<br>1.000<br>1.000<br>10.830<br>0.999<br>0.850<br>18.160<br>0.968<br>0.000<br>20.230<br>0.865<br>0.000<br>19.850<br>0.547<br>0.000|0.9990<br>4.990<br>0.999<br>0.990<br>8.760<br>0.968<br>0.030<br>9.790<br>0.910<br>0.000<br>10.110<br>0.807<br>0.000<br>9.580<br>0.496<br>0.000|0.9999<br>3.680<br>0.897<br>0.050<br>3.980<br>0.802<br>0.000<br>4.130<br>0.746<br>0.000<br>4.110<br>0.658<br>0.000<br>4.080<br>0.404<br>0.000|Notes: The table summarizes the simulation results, where the true data-generating process is a one-factor market model (_K_¼1) with_N_¼400 stocks.^_M_denotes the average|number of estimated blocks, RI is the average of the Rand Index, the column_S_¼ Sdenotes the fraction of simulations where the estimated block structure is equal to the true|block structure, and Corr. RMSE denotes the average RMSE of the estimated idiosyncratic correlations. The numbers are based on 200days and 100 simulations.|Downloaded from https://academic.oup.com/jfec/article/23/2/nbae018/7738288 by DO NOT USE Institute of Education merged with 9000272 user on 20 May 2026|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|



Bodilsen j Large-Dimensional Portfolio Selection 

|**_M_**¼**5**<br>**_M_**¼**11**<br>**_M_**¼**25**<br>**_M_**¼**74**<br>**_M_**¼**400**|_τ_<br>^**_M_**<br>**RI**<br>**_S_**¼ S<br>^**_M_**<br>**RI**<br>**_S_**¼ S<br>^**_M_**<br>**RI**<br>**_S_**¼ S<br>^**_M_**<br>**RI**<br>**_S_**¼ S<br>^**_M_**<br>**RI**<br>**_S_**¼ S|Panel (a):_ω_2¼0|Corr. RMSE:<br>0.083<br>0.088<br>0.086<br>0.086<br>0.088|0.9500<br>39.580<br>0.826<br>0.000<br>57.120<br>0.909<br>0.000<br>71.690<br>0.944<br>0.000<br>80.730<br>0.956<br>0.000<br>75.460<br>0.943<br>0.000|0.9600<br>33.940<br>0.830<br>0.000<br>49.430<br>0.909<br>0.000<br>62.330<br>0.940<br>0.000<br>67.920<br>0.952<br>0.000<br>57.550<br>0.935<br>0.000|0.9700<br>29.220<br>0.833<br>0.000<br>43.030<br>0.907<br>0.000<br>53.200<br>0.937<br>0.000<br>55.660<br>0.946<br>0.000<br>41.840<br>0.925<br>0.000|0.9800<br>25.250<br>0.837<br>0.000<br>36.790<br>0.905<br>0.000<br>44.730<br>0.933<br>0.000<br>44.070<br>0.939<br>0.000<br>27.990<br>0.914<br>0.000|0.9900<br>21.390<br>0.841<br>0.000<br>30.330<br>0.902<br>0.000<br>35.360<br>0.926<br>0.000<br>32.110<br>0.929<br>0.000<br>18.170<br>0.898<br>0.000|0.9950<br>18.830<br>0.844<br>0.000<br>25.370<br>0.899<br>0.000<br>28.030<br>0.920<br>0.000<br>24.940<br>0.920<br>0.000<br>14.890<br>0.887<br>0.000|0.9990<br>12.980<br>0.848<br>0.000<br>15.390<br>0.878<br>0.000<br>15.890<br>0.894<br>0.000<br>14.640<br>0.892<br>0.000<br>10.860<br>0.863<br>0.000|0.9999<br>6.510<br>0.810<br>0.000<br>6.470<br>0.796<br>0.000<br>6.750<br>0.807<br>0.000<br>6.770<br>0.813<br>0.000<br>6.070<br>0.785<br>0.000|Panel (b):_ω_2¼7×10_−_8|Corr. RMSE:<br>0.099<br>0.098<br>0.097<br>0.104<br>0.098|0.9500<br>29.050<br>0.834<br>0.000<br>43.480<br>0.906<br>0.000<br>54.480<br>0.936<br>0.000<br>55.820<br>0.938<br>0.000<br>43.580<br>0.934<br>0.000|0.9600<br>25.260<br>0.838<br>0.000<br>37.580<br>0.903<br>0.000<br>46.630<br>0.931<br>0.000<br>45.900<br>0.930<br>0.000<br>32.650<br>0.924<br>0.000|0.9700<br>22.280<br>0.840<br>0.000<br>32.520<br>0.901<br>0.000<br>39.780<br>0.925<br>0.000<br>37.190<br>0.922<br>0.000<br>23.920<br>0.911<br>0.000|0.9800<br>19.590<br>0.843<br>0.000<br>28.170<br>0.897<br>0.000<br>33.470<br>0.918<br>0.000<br>29.230<br>0.910<br>0.000<br>17.980<br>0.899<br>0.000|0.9900<br>17.070<br>0.845<br>0.000<br>23.450<br>0.890<br>0.000<br>26.720<br>0.908<br>0.000<br>22.070<br>0.895<br>0.000<br>13.620<br>0.880<br>0.000|0.9950<br>14.780<br>0.845<br>0.000<br>19.730<br>0.883<br>0.000<br>21.260<br>0.896<br>0.000<br>17.800<br>0.884<br>0.000<br>11.910<br>0.870<br>0.000|0.9990<br>10.420<br>0.839<br>0.000<br>12.550<br>0.855<br>0.000<br>12.530<br>0.867<br>0.000<br>10.950<br>0.847<br>0.000<br>9.110<br>0.843<br>0.000|0.9999<br>5.480<br>0.781<br>0.000<br>5.660<br>0.766<br>0.000<br>5.850<br>0.774<br>0.000<br>5.570<br>0.755<br>0.000<br>5.380<br>0.768<br>0.000|Panel (c):_ω_2¼28×10_−_8|Corr. RMSE:<br>0.111<br>0.113<br>0.116<br>0.117<br>0.117|0.9500<br>26.090<br>0.835<br>0.000<br>37.040<br>0.900<br>0.000<br>43.230<br>0.923<br>0.000<br>42.660<br>0.930<br>0.000<br>33.390<br>0.919<br>0.000|0.9600<br>22.760<br>0.836<br>0.000<br>32.440<br>0.896<br>0.000<br>36.820<br>0.915<br>0.000<br>35.000<br>0.922<br>0.000<br>25.510<br>0.907<br>0.000|0.9700<br>20.040<br>0.836<br>0.000<br>27.820<br>0.891<br>0.000<br>31.310<br>0.908<br>0.000<br>28.440<br>0.912<br>0.000<br>19.340<br>0.893<br>0.000|0.9800<br>17.410<br>0.838<br>0.000<br>23.780<br>0.883<br>0.000<br>25.700<br>0.898<br>0.000<br>22.320<br>0.901<br>0.000<br>14.630<br>0.875<br>0.000|0.9900<br>15.020<br>0.839<br>0.000<br>19.520<br>0.874<br>0.000<br>20.100<br>0.885<br>0.000<br>17.280<br>0.886<br>0.000<br>11.380<br>0.855<br>0.000|0.9950<br>13.270<br>0.835<br>0.000<br>16.800<br>0.866<br>0.000<br>16.190<br>0.871<br>0.000<br>14.370<br>0.873<br>0.000<br>10.150<br>0.847<br>0.000|0.9990<br>9.440<br>0.821<br>0.000<br>10.410<br>0.833<br>0.000<br>10.140<br>0.836<br>0.000<br>9.270<br>0.834<br>0.000<br>7.760<br>0.812<br>0.000|0.9999<br>4.770<br>0.745<br>0.000<br>5.000<br>0.737<br>0.000<br>4.930<br>0.737<br>0.000<br>4.830<br>0.738<br>0.000<br>4.520<br>0.712<br>0.000|Notes: The table summarizes the simulation results, where the true data-generating process is a fve-factor market model (_K_¼5) with_N_¼400 stocks, but where the estimation<br>process only uses the frst factor (_K_�¼1).^_M_denotes the average number of estimated blocks, RI is the average of the Rand Index, the column_S_¼ Sdenotes the fraction of|simulations where the estimated block structure is equal to the true block structure, and Corr. RMSE denotes the average RMSE of the estimated idiosyncratic correlations.|The numbers are based on 200days and 100 simulations.|Downloaded from https://academic.oup.com/jfec/article/23/2/nbae018/7738288 by DO NOT USE Institute of Education merged with 9000272 user on 20 May 2026|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|



**14** _Journal of Financial Econometrics_ 

cut-off value very close to one must be chosen, whereas, in the case of a strict factor model, the optimal value of _τ_ is 0.96 (and lower). 

Panel (b) contains the results in a realistic market microstructure noise case. In this case, the method performs well for a moderate amount of blocks ( _M_ ≤ 25) but struggles to find the correct block structure in the cases of high _M_ . This finding is expected given an RMSE of around 0.038 in this case. For 5 and 11 blocks, we have no estimation errors when using a cut-off value around 0.995, while a slightly lower value of _τ_ is needed for 25 blocks. 

Finally, in panel (c) the noise variance is increased by a factor of four and corresponds roughly to the highest level of noise estimated for our empirical data. The RMSE of the idiosyncratic correlations has increased to around 0.066. Even in this case, we can with a high likelihood recover the true block structure for _M_ ≤ 11 by using the MRK estimator in combination with HC. When the number of blocks exceeds 25, the method is very unlikely to infer the true structure of the model. 

In Table 2, we present similar simulation results where we consider a misspecified model. The true data-generating process is a five-factor model ( _K_ ¼ 5), but the estimation process assumes a one-factor model ( _K_[�] ¼ 1) using only the first component mimicking the market factor. In this scenario, our method always fails to infer the true structure of the model for the model specifications considered here. The RMSEs of the idiosyncratic correlations are substantially higher due to misspecification (0.083–0.117). This directly implies that the dissimilarity measures used by the HC method are imprecise, and hence the likelihood of identifying the true model becomes very low. 

The simulation study shows that, under correct model specification, our methodology performs well in identifying an unknown block structure in the idiosyncratic covariance matrix in a large-dimensional setting as long as the number of blocks _M_ is relatively small compared to _N_ . This is reassuring since the number of blocks reported in similar studies is typically reported to be lower than 25. The reasoning behind this finding is that when _M_ is small compared to _N_ , it is sufficient that we estimate the average idiosyncratic correlation to be close to zero for some pairs of stocks from different blocks to separate them under complete linkage. On the other extreme, when the true model is a strict factor model, it is required that we have an estimate of the idiosyncratic correlation for every pair of stocks very close to zero. Since we have a substantial amount of estimation error, it is unlikely that we detect a strict factor model unless we are willing to use a very low cut-off value. More generally, the results suggest that the optimal choice of cut-off value varies according to _M_ . A large cut-off value can be used for a small number of blocks, whereas lower values of the cut-off parameter must be selected to be able to detect block structures with a high number of blocks. 

## **5 Alternative Dynamic Conditional Covariance Models** 

We will use the CLUHFF model in a portfolio allocation application. The performance of the model will be compared to other well-known alternatives from the multivariate volatility literature. We consider the following set of alternative models: 

- The random walk (RW) model, in which S _t_ : _t_ þ _h_ j _t_ ¼ _h_ S[^] _t_ . 

- The block random walk (Block-RW) model similar to Fan et al. (2016), in which ð _S_ Þ 

- S _t_ : _t_ þ _h_ j _t_ ¼ _h_ S[^] _t_[, where ] _[S ]_[is determined by HC. ] 

- The DCC-NL and BEKK-NL models proposed in Engle, Ledoit, and Wolf (2019). 

- The multivariate HEAVY model of Noureldin et al. (2012). 

- The HAR-DRD model of Oh and Patton (2016). 

- The Factor-LASSO model proposed by Alves et al. (2024). 

Bodilsen j Large-Dimensional Portfolio Selection **15** 

The DCC-NL and BEKK-NL models proposed in Engle et al. (2019) are slight modifications of the DCC model of Engle (2002) and the covariance targeting scalar BEKK model of Engle and Kroner (1995), respectively. The main difference between the original models and their NL variants is that the latter uses the non-linear shrinkage method of Ledoit and Wolf (2012) to estimate the unconditional covariance matrix rather than using the sample covariance matrix. The second difference is the use of the composite likelihood technique of Pakel, Shephard, Sheppard, and Engle (2021) for parameter estimation. Both modifications ensure that the models are applicable in large-dimensional settings. In the DCC-NL the conditional variances are modeled using univariate GARCH(1, 1) processes. 

The multivariate HEAVY model constructs the conditional covariance matrix of returns in a similar spirit as the BEKK model. However, in the HEAVY model, the conditional covariance matrix is driven by a realized covariance matrix rather than by the outer product of returns. We implement the model using the model specification given by Equations (12) and (13) in Noureldin et al. (2012). For computational convenience, we adopt the scalar specification of the model, such that the number of unknown parameters to be estimated is only four. The model is estimated using a composite Wishart likelihood technique to avoid the time-consuming matrix inversion needed to evaluate the standard Wishart likelihood function. 

The Factor-LASSO model of Alves et al. (2024) employs a similar approach to model large-dimensional covariance matrices as ours, in which the factor covariance matrix, factor loadings, and idiosyncratic covariance matrix are separately modeled using autoregressive processes. However, there are several aspects where this model is different. First, the model is heavily parameterized. This is solved by a LASSO estimation approach, which increases the computational burden substantially relative to the OLS estimation approach that is feasible for the CLUHFF model. Second and related, the authors restrict the dynamics of the idiosyncratic covariance matrix to be solely driven by the idiosyncratic variances from the previous day to ensure that the number of parameters to be estimated does not increase too rapidly. Third, in contrast to ours, the model framework does not automatically ensure that the forecasted covariance matrix is positive definite. To ensure this, the authors use the nonlinear log-matrix transformation, such that, when reverted via the matrix exponential, the forecast is a valid covariance matrix. Fourth, the block structure of the idiosyncratic covariance matrix is assumed to be known and determined by sector classification irrespective of the number of factors in the model. To be comparable with the CLUHFF model, we implement a one-factor and a 10-factor version of this model in the empirical application using the same set of factors. 

To summarize, the set of competitor models contains models only relying on daily returns (DCC-NL and BEKK-NL), as well as models only relying on realized measures (RW, Block-RW, HAR-DRD, and Factor-LASSO), and combinations thereof (HEAVY). 

In addition to using model-based approaches to portfolio selection, we also include the equal weighting 1 _=N_ strategy as advocated by DeMiguel, Garlappi, and Uppal (2009) in our empirical application. 

## **6 Portfolio Allocation** 

We will evaluate the merits of our predictive multivariate volatility model in a portfolio allocation setting. The classical portfolio selection problem of Markowitz (1952) requires both an estimate of the covariance matrix and of expected returns. Since the focus of this article is on forecasting large covariance matrices but ignores the difficult task of predicting the first moment of returns, we consider variants of the global minimum variance portfolio (GMVP) selection problem in line with a vast body of extant literature. 

**16** _Journal of Financial Econometrics_ 

We consider an investor that can invest in a portfolio consisting of _N_ different assets. The investor rebalances the portfolio every _h_ th trading day and chooses the portfolio weights at times _t_ ¼ _t_ 0 _; t_ 0 þ _h;_ ... _; T − h_ based on a forecast of S _t_ : _t_ þ _h_ . The GMVP problem can then be stated as 

**==> picture [292 x 16] intentionally omitted <==**

0 where _wt_ þ _h_ j _t_ ¼ ð _w_ 1 _;t_ þ _h_ j _t;_ ... _; wN;t_ þ _h_ j _t_ Þ is an _N_ × 1 vector of relative portfolio weights chosen at time _t_ to be held until _t_ þ _h_ , S _t_ : _t_ þ _h_ j _t_ is the forecast of the _N_ × _N_ covariance matrix of returns over the next _h_ days, and _ι_ is an _N_ × 1 vector of ones. When S _t_ : _t_ þ _h_ j _t_ is positive definite, the unique solution to the GMVP problem is given by 

**==> picture [80 x 30] intentionally omitted <==**

We will consider two extensions of the problem in Equation (19) as suggested by Lunde, Shephard, and Sheppard (2016). First, we extend the problem by imposing a leverage constraint on the investor. This can be achieved by imposing an _L_ 1 constraint on the portfolio weights. Adding a short-sale restriction makes the portfolio selection more realistic, as many investors such as pension funds and mutual funds face leverage constraints. Second, we extend the GMVP problem by imposing a lower and upper bound of _u_ on each portfolio weight. A constraint of this type ensures that the portfolio is well diversified since the number of non-zero weights is at least b1 _=u_ c in this scenario. The optimization problem under these additional constraints can be stated as 

**==> picture [245 x 56] intentionally omitted <==**

where k �k1 and k �k1 denote the _L_ 1 and _L_ 1 norm, respectively, and _s_ denotes the percentage that is allowed to be held short 

The optimization problem in Equation (20) does have a solution when S _t_ : _t_ þ _h_ j _t_ is positive definite. The solution can, however, not be expressed in closed form as in the classical GMVP problem. To find the optimal portfolio weights in this case, we use the CVX package for MATLAB of Grant and Boyd (2014). 

## **7 Empirical Application** 

## 7.1 Data Description 

We analyze high-frequency stock price data for the constituents of the S&P 500 Index over the period from January 2007 to December 2015. The data are obtained from the New York Stock Exchange Trade and Quote (TAQ) database. We use the stocks in the S&P 500 Index as of the end of 2015, for which we can collect data for every trading day in the sample period. Following Lunde et al. (2016), we exclude illiquid stocks in the sense that we require the stocks to be traded at least 195 times a day to remain in the sample. In total, this results in 396 different stocks, which we follow over the 2 _;_ 266 official trading days during the 2007–2015 period. 

Bodilsen j Large-Dimensional Portfolio Selection **17** 

The information from the TAQ database is merged with the Center for Research in Security Prices (CRSP) daily stock files to obtain the daily return series. 

As observed factors, we use the 10 Standard & Poor’s Depositary Receipts (SPDR) ETFs, with the ticker symbols SPY, XLE, XLB, XLI, XLY, XLP, XLV, XLF, XLK, and XLU. The SPY ETF tracks the S&P 500 Index and is a common choice to proxy the market portfolio in the literature. The remaining nine factors are sector ETFs, which track the S&P 500 Index constituents based on their sector membership as classified by GICS.[6 ] The chosen set of factors follows the recent literature on high-dimensional factor models for stock data (see, e.g., Aït-Sahalia and Xiu 2017; Fan et al. 2016; Gribisch, Hartkopf, and Liesenfeld 2020; Hartkopf 2023), where it has been found that the inclusion of the sector ETFs improves the idiosyncratic correlation sparsity relative to the one-factor market model and further yields an idiosyncratic correlation structure that is stable across time.[7] 

We estimate the daily quadratic variation of the stocks and factors with the MRK estimator using a homogeneous price series sampled every 30 seconds using the previous tick method, such that we generally have 780 observations available to estimate S _t_ . 

The sample period 2007–2015 contains both the financial crisis and the flash crashes in 2010, 2011, and 2015. These periods were characterized by large intra-day price swings, and consequently, the entries of the realized covariance matrix on these days are extreme compared to the rest of the sample. To reduce the impact of these events on the parameter estimation and forecasting ability, we clean the covariance matrices using the approach of Callot, Kock, and Medeiros (2017). That is, we flag each day on which one-fourth of the unique entries of _Yt_ are more than four standard errors away from its sample average up to then. On such days, the entries of _Yt_ are replaced with the average of the covariance matrices from the five immediately preceding and following non-flagged days. 

We split the full sample of 2 _;_ 266 daily observations covering the period from January 2007 to December 2015 into an in-sample and an out-of-sample. The in-sample consists of the first five years of data corresponding to 1 _;_ 260 daily observations. The out-of-sample consists of the remaining 1 _;_ 006 observations representing the period 2012–2015. 

## 7.2 In-Sample Analysis of the Idiosyncratic Covariance Matrices 

Following Fan et al. (2016) and Aït-Sahalia and Xiu (2017), we investigate the effect of varying the number of common observable factors on the sparsity pattern of the idiosyncratic covariance matrix. We use the full sample of the 396 stocks and consider a onefactor model and a 10-factor model. For the one-factor model, we use the S&P 500 Index tracking ETF SPY as the only observable factor, in which case we consider a CAPM-type model. For the 10-factor model, we additionally augment the model with the nine SPDR sector ETFs as observable factors. 

To carry out this analysis, we transform each of the _Zt_ matrices into correlation matrices and denote an off-diagonal entry to be significant if it is larger than 0.15 in absolute value for more than half of the days in the in-sample period. 

It is of great interest to study how a block structure determined by the HC approach compares to a block structure determined by GICS sector membership. To this end, we implement the HC algorithm to the idiosyncratic correlation matrices over the in-sample period as described in Section 3.2. Based on the simulation results in Section 5, we select a conservative cut-off value of _τ_ ¼ 0 _:_ 9999 so that we might model irrelevant correlations 

> 6 The relation between the ticker symbols and GICS sectors is given as follows: Energy (XLE), Materials (XLB), Industrials (XLI), Consumer Discretionary (XLY), Consumer Staples (XLP), Health Care (XLV), Financial (XLF), Information Technology (XLK), and Utilities (XLU). 

> 7 The aforementioned studies further incorporate the three Fama-French factors in their examination of high-dimensional factor models. However, the high-frequency prices of these factors are only publicly available at the 5-minute frequency. This limitation prevents us from directly utilizing these factors in our empirical study, as the daily estimate of S _t_ relies on prices sampled every 30 seconds. 

**18** _Journal of Financial Econometrics_ 

**==> picture [337 x 317] intentionally omitted <==**

**----- Start of picture text -----**<br>
( a ) One-factor model – HC ( b ) One-factor model – Sectors<br>400 400<br>350 350<br>300 300<br>250 250<br>200 200<br>150 150<br>100 100<br>50 50<br>0 0<br>0 50 100 150 200 250 300 350 400 0 50 100 150 200 250 300 350 400<br>( c ) Ten-factor model – HC ( d ) Ten-factor model – Sectors<br>400 400<br>350 350<br>300 300<br>250 250<br>200 200<br>150 150<br>100 100<br>50 50<br>0 0<br>0 50 100 150 200 250 300 350 400 0 50 100 150 200 250 300 350 400<br>**----- End of picture text -----**<br>


**Figure 1.** The subfigures display the significant entries of the average idiosyncratic correlation matrices. In (a) and (c), the blocks are determined by hierarchical clustering using complete linkage with a cut-off value of 0.9999. In (b) and (d), the blocks are determined using sector membership based on the first two digits of the company’s GICS code. Panels (a) and (b) consider the one-factor market model with the ETF SPY as a factor, while panels (c) and (d) consider the 10-factor model with the additional nine SPDR sector ETFs. 

inside the blocks, but on the other hand, there is a low likelihood of overestimating the number of blocks which would cause some true non-zero correlations to be set equal to zero. 

The in-sample results from employing the HC algorithm to the idiosyncratic correlation matrices are depicted in Figure 1. Panels (a) and (b) show the sparsity pattern for the onefactor market model, using HC and sector membership to determine the block structure, respectively. These figures show that the market factor alone is not capable of removing the cross-asset dependence. The HC algorithm detects four relatively large blocks, while by construction the sector-based method results in a 10-dimensional block structure. In Panel (c) and (d), the block structure is illustrated for the 10-factor model. In this case, almost all residual correlations outside the blocks are eliminated. The HC method detects six blocks, where each of them contains a large proportion of significantly correlated pairs of stocks. 

Although the block structure of the idiosyncratic covariance matrix is much clearer in the case of the 10-factor model, it is important to emphasize that this finding does not necessarily imply that this model will perform better than the one-factor model for portfolio 

Bodilsen j Large-Dimensional Portfolio Selection **19** 

selection. It merely indicates that the market factor in itself is incapable of removing the majority of the residual correlations. One advantage of using a one-factor model in our forecasting model is that we only need to estimate a dynamic model for _N_ different factor loadings, compared to _NK_ in the general case. For a large _K_ there will presumably be some factor loadings which will be unpredictable. For the one-factor market model, it is known from previous studies that the daily market betas are fairly persistent and can be predicted quite well (see, e.g., Andersen et al. 2006 and Hansen, Lunde, and Voev 2014). 

To help us understand how the HC algorithm detects clusters of stocks with similar idiosyncratic correlation, we present the corresponding dendrograms in Figure 2. In these dendrograms, we consider the constituents of the S&P 100 Index for illustrative purposes. For the one-factor model depicted in Panel (a), we estimate four blocks using the cut-off value of 0.9999. Here it is found that stocks within the same sector are closely related, but we also find a substantial amount of dependence among stocks from different sectors which results in a model structure where the estimated blocks generally include stocks from different sectors. The exception is the last block in Panel (a), which solely contains the stocks from the industrial sector. We also observe that stocks from the energy sector, financial sector, healthcare sector, telecommunication sector, and utilities sector are well separated from the other stocks in the sample. With a slightly lower cut-off value, some of these sectors would have formed distinct blocks. In the full model with both the market and the sector ETFs as factors in Panel (b), the correlation distances given by Equation (8) are reduced, and we obtain five blocks of companies using the threshold of 0.9999. After controlling for both the market component and the sector ETFs, we find that the strong intrasectorial dependence is still present although it has been reduced significantly. This has the effect that the composition of blocks we estimate in this case is somewhat different compared to the one-factor model. Nevertheless, we observe that stocks from the aforementioned sectors are generally found within the same blocks. This suggests a high degree of dependence among the stocks within these specific sectors. 

In Supplementary Appendix Tables A.3 and A.4, we provide a complete overview of the estimated block assignment for the S&P 500 Index sample in the one-factor model and 10factor model, respectively. We observe a similar pattern as previously described for the S&P 100 Index. In the one-factor model stocks within the same sector are closely linked, however, the amount of between-sector dependence is too large to justify a block structure based on sector segmentation. In the 10-factor model, we find that the strong dependence within sectors generally is reduced. This does however not hold for the stocks from the energy sector and utilities sector, where all stocks within these sectors are allocated to the same block. In fact, the energy sector is the only sector represented in block number 5 in Supplementary Appendix Table A.4. 

In summary, our initial in-sample analyses suggest that implementation of the CLUHFF model using HC will result in a significantly different idiosyncratic covariance structure depending on the number of common factors used in the model specification. In particular, we find evidence that this data-driven approach provides a model structure that is very different from a strict factor model or the commonly used sector-based approach to determine a block structure. Note, that our findings does not rule out the possibility that the true structure of the idiosyncratic covariance matrix can be described by sector segmentation if the correct factors can be identified. In some sense, our approach can be regarded as a data-driven way to specify the “optimal” model structure for a given choice of factors. 

## 7.3 Out-of-Sample Portfolio Allocation 

In this section, we describe the forecasting setup and present the main results of the empirical analysis. In the forecasting study, we employ a rolling window forecasting scheme, where we estimate the model using the first _t_ 0 ¼ 1 _;_ 260 observations for the first forecast 

_Journal of Financial Econometrics_ 

**20** 

**==> picture [194 x 517] intentionally omitted <==**

**----- Start of picture text -----**<br>
model model<br>One-factor Ten-factor<br>)( a )( b<br>1.00 0.90 0.80 0.70 0.60 0.50 0.40 1.00 0.95 0.90 0.85 0.80 0.75 0.70 0.65 0.60 0.55 0.50<br> LMT  DOW<br> RTN  DD<br> GD  MON<br> BA  EXC<br> UTX  SO<br> HON  ABT<br> UPS  PEP<br> FDX  KO<br> UNP  NKE<br> NSC  PCLN<br> CAT  AMZN<br> EMR GOOG<br> MMM  INTC<br> GE  TXN<br>QCOM  ORCL<br> TXN  MSFT<br> INTC  AAPL<br> MSFTCSCO  VZ T<br> ORCL CSCO<br> IBM  IBM<br> AAPL EMC  CQCOM<br> AMZNGOOG  BAC BK<br> PCLN  JPM<br> MA  MET<br> ACN  ALL<br> TWX  WFC<br> DIS  USB<br> SBUX  GS<br> MCD  MS<br> NKE  BLK<br> CVS  MA<br> WMT  AXP<br> COST  COF<br> TGT  HON<br> LOW  UTX<br> HD  BA<br> XOM  GD<br> CVX  RTN<br> COP  LMT<br> OXY  AIG<br> APC  F<br> DVN  MMM<br> SLB  MDT<br> HAL  PFE<br> MON  UNH<br> DD  JNJ<br> DOW  BIIB<br> BIIB  GILD<br> GILD  CELG<br> CELG AMGN<br>AMGN  MRK<br> UNH  LLY<br> MDT  BMY<br> JNJ  SBUX<br> ABT  MCD<br> LLY  TWX<br> BMY  DIS<br> MRK  HD<br> PFE  LOW<br> MO  TGT<br> KO PEP  WMT COST<br> PG  MO<br> CL  CVS<br> SO  PG<br> EXC  CL<br> VZ T  UPS EMR<br> BLK  FDX<br> GS  NSC<br> MS  UNP<br> BK  GE<br> USB  CAT<br> WFC  APC<br> JPM  DVN<br> C BAC  XOM OXY<br> AXP  CVX<br> COF  HAL<br> ALL  SLB<br> MET  COP<br> AIG F  EMC ACN<br>**----- End of picture text -----**<br>


Bodilsen j Large-Dimensional Portfolio Selection **21** 

and subsequently forecast the cumulative covariance matrix over the next _h_ days. For the next _h_ -days ahead forecast, we use the sample consisting of observations _h_ through 1 _;_ 260 þ _h_ to estimate the models.[8 ] We continue in this fashion until we reach the end of the sample. 

Let _T_ ( _h_ ) denote the number of _h_ -days portfolio allocations performed over the out-ofsample period, and denote by _rt_ : _t_ þ _h_ the vector of the _h_ -days close-to-close returns. Moreover, to simplify notation, we define _rt_ ð _h_ Þ � _rt_ 0 þ ð _t −_ 1Þ _h_ : _t_ 0 þ _th_ and _wt_ ð _h_ Þ � _wt_ 0 þ _th_ j _t_ 0 þ ð _t −_ 1Þ _h_[. For each portfolio allocation problem, predictive horizon, and ] forecasting model, we then consider the following summary statistics calculated over the out-of-sample period: 

**==> picture [259 x 41] intentionally omitted <==**

- Sharpe ratio: _μσpp_ ðð _hh_ ÞÞ ~~[.]~~ 

- Turnover: _N_ ð _T_ ð1 _h_ Þ _−_ 1Þ P _Tt_ ¼ð _h_ 2Þ P _Ni_ ¼1[j] _[w][i][;][t]_ ð _[h]_ Þ _− wi;t −_ 1ð _h_ Þj. 

- � Proportion of leverage: _NT_ 1ð _h_ Þ P _Tt_ ¼ð _h_ 1Þ P _Ni_ ¼1 **[1]** � _[w][i][;][t]_ ð _[h]_ Þ _<_ 0�. � Maximum weight: max1 ≤ _i_ ≤ _N;_ 1 ≤ _t_ ≤ _T_ ð _h_ Þ _[w] i;t_ ð _[h]_ Þ. � Minimum weight: min1 ≤ _i_ ≤ _N;_ 1 ≤ _t_ ≤ _T_ ð _h_ Þ _[w] i;t_ ð _[h]_ Þ. 

The GMVP has been shown not only to possess good properties in terms of producing lowvariance portfolios but also to exhibit good properties with respect to a high out-of-sample Sharpe ratio (Jagannathan and Ma 2003). However, since the optimization problem solely focuses on minimizing the variance of the portfolio without taking expected returns into account, the statistic of main interest is the portfolio standard deviation rather than the Sharpe ratio when evaluating the performance of the different covariance estimators (Engle et al. 2019; Ledoit and Wolf 2017). However, from a practical point of view, average returns, Sharpe ratio, proportion of leverage, and turnover measure are naturally also of great interest and thus also presented for completeness. The maximum and minimum weight statistics indicate the degree of diversification of the constructed portfolios. 

We present the results for four different variants of our model and compare their performance with the models introduced in Section 6. For the CLUHFF models, we consider a one-factor market model using SPY as the factor and a 10-factor model with all SPDR ETFs as factors. For each choice of factor structure, we select the block structure using either HC or the sector-based (S) approach. We denote these four different implementations of our model as 1F-HC, 1F-S, 10F-HC, and 10F-S. For the block RW models, we also consider a one- and 10-factor model with the block structure estimated by HC, denoted by RW-1F-HC and RW-10F-HC, respectively. 

For the CLUHFF models employing HC, we re-estimate the set of non-zero entries in the idiosyncratic covariance matrix (S _t_ ) every 25days over the out-of-sample period using data from the most recent 1 _;_ 260 days. In this way, we can account for potential time-variation in the idiosyncratic correlations, thereby allowing the model structure to adapt to structural changes/events that might influence the dependence structure over the out-of-sample period in a data-driven way. 

> 8 For the DCC-NL, BEKK-NL, and HEAVY models, we only re-estimate the models in every b100 _=h_ c iteration of the forecasting procedure. This is done to considerably reduce the running time of the forecasting exercise. In an unreported analysis, we have investigated the sensitivity of the results to this choice. We find that the results are fairly insensitive to the frequency at which the models are re-estimated. 

**22** _Journal of Financial Econometrics_ 

Based on the in-sample evidence presented in Supplementary Appendix Table A.5, we leave out the daily component from the predictive regressions for the factor loadings and the idiosyncratic correlations and only use the weekly and monthly averages as _h_ -step ahead predictors. We find that this choice leads to a similar fit to the data when a full parametrization of the model is employed. To make variance predictions we set _L_ ¼ 10 _;_ 000 in Equation (16). 

Finally, to judge the statistical significance of the CLUHFF methodology, we employ the model confidence set (MCS) procedure of Hansen, Lunde, and Nason (2011). We use the MCS to avoid the multiple comparison problem that arises when comparing 14 different models. We implement the MCS procedure using a confidence level of 90% with the squared portfolio returns as the time series of losses. The MCS procedure gives us a set of _p_ -values from which the set consisting of the best models can be determined. 

## **7.3.1 Portfolio allocation results** 

Table 3 presents the results of the out-of-sample portfolio selection problems. In Panel (a), we consider the results using the GMVP objective function in Equation (19) with daily rebalancing ( _h_ ¼ 1). For this problem, the model that constructs portfolios with the lowest standard deviation is 1F-HC followed by the three other CLUHFF models. The 1F-HC model has an annualized portfolio standard deviation of 7.38% and reduces the portfolio risk by almost 50% compared to an equal-weighted portfolio. The MCS _p_ -values are reported in the last rows of the summary statistics and show that the 1F-HC is the only model included in the 90% MCS at the daily horizon. 

For the one-factor model, the results suggest that the implementation with an estimated block structure performs better than using sector segmentation. However, in the 10-factor model, the results are slightly in favor of the sector-based approach. We expected these results based on the illustrations in Figure 1, where the sector-based approach results in a block structure that sets too many significant correlations equal to zero in the one-factor case, where the HC method is better at capturing the dependence structure. In the 10-factor model, the sector-based approach appears to be a more reasonable choice, which is also reflected in the empirical results. 

The HAR-DRD model, which is a special case of the CLUHFF model, produces portfolios with a level of variation close to the CLUHFF models and has the highest Sharpe ratio among all models in Panel (a). However, in this high-dimensional setting with nearly 400 assets under consideration, the HAR-DRD model becomes computationally demanding, since we have to estimate a linear regression model for the _N_ ð _N −_ 1Þ _=_ 2 distinct correlations. To estimate a model of the type in Equation (17), we need to stack the time series of _T_ ¼ 1 _;_ 260 in-sample observations, which for _N_ ¼ 396 results in a regression model with more than 98 million observations. In an out-of-sample forecasting setting with daily reestimation, such a large number of observations makes this model very time-consuming to implement relative to the modification of the model that we propose. This is one of the main advantages of using the factor structure combined with a block structure in the idiosyncratic covariance matrix. For _M >_ 1 blocks we can reduce the dimension of the predictive correlation regression in Equation (17) substantially. 

An interesting observation is that the measures of turnover are much lower for the CLUHFF models compared to the corresponding numbers for the second-best-performing models (HAR-DRD and 1F-LASSO). In particular, the turnover numbers produced by the 10-factor models are low. The fact that the CLUHFF model produces portfolios with the lowest standard deviation and measures of turnover highlights its great potential in largedimensional portfolio allocation settings. The models that do not rely on intra-day information (DCC-NL, BEKK-NL, and 1 _=N_ ) are inferior to the high-frequency-based models in this exercise, with the 1 _=N_ strategy as the worst-performing model. Among the RW-based 

Bodilsen j 

**23** 

|**RW**<br>**RW-**<br>**RW-**<br>**1F-HC**<br>**1F-S**<br>**10F-HC**<br>**10F-S**<br>**DCC**<br>**BEKK**<br>**HEAVY**<br>**HAR-**<br>**1F-**<br>**10F-**<br>**1**_=_**N**|**1F-HC**<br>**10F-HC**<br>**DRD**<br>**LASSO**<br>**LASSO**|Panel (a): GMVPs for_h_¼1|Std. dev<br>10.984<br>10.626<br>10.426<br>7.380<br>7.709<br>7.864<br>7.843<br>9.176<br>8.857<br>8.222<br>7.939<br>8.159<br>8.840<br>13.752|Average<br>14.201<br>16.163<br>17.192<br>12.345<br>12.188<br>11.570<br>12.100<br>14.594<br>13.745<br>11.621<br>14.864<br>14.869<br>14.679<br>14.498|Sharpe ratio<br>1.293<br>1.521<br>1.649<br>1.673<br>1.581<br>1.471<br>1.543<br>1.590<br>1.552<br>1.413<br>1.872<br>1.822<br>1.661<br>1.054|Turnover<br>12.159<br>9.636<br>7.980<br>1.206<br>1.088<br>0.985<br>0.988<br>1.591<br>0.614<br>2.416<br>3.523<br>1.591<br>2.595<br>0.000|Leverage<br>0.476<br>0.465<br>0.458<br>0.468<br>0.477<br>0.486<br>0.480<br>0.507<br>0.463<br>0.474<br>0.493<br>0.484<br>0.456<br>0.000|Max weight<br>0.432<br>0.627<br>0.536<br>0.175<br>0.152<br>0.208<br>0.205<br>0.478<br>0.141<br>0.191<br>0.238<br>0.248<br>0.300<br>0.003|Min weight<br>–0.442<br>–0.318<br>–0.263<br>–0.077<br>–0.076<br>–0.089<br>–0.088<br>–0.062<br>–0.071<br>–0.041<br>–0.099<br>–0.096<br>–0.144<br>0.003|MCS_p_-value<br>0.000<br>0.000<br>0.000<br>1.000<br>0.000<br>0.000<br>0.000<br>0.000<br>0.000<br>0.000<br>0.000<br>0.000<br>0.000<br>0.000|Panel (b): Restricted Minimum Variance Portfolios for_h_¼1|Std. dev<br>9.859<br>9.449<br>9.471<br>8.631<br>8.735<br>8.758<br>8.768<br>9.454<br>9.475<br>9.187<br>8.898<br>8.985<br>9.503<br>13.752|Average<br>19.869<br>18.653<br>18.438<br>13.380<br>12.946<br>11.358<br>11.372<br>12.153<br>12.697<br>10.060<br>15.329<br>12.765<br>14.014<br>14.498|Sharpe ratio<br>2.015<br>1.974<br>1.947<br>1.550<br>1.482<br>1.297<br>1.297<br>1.286<br>1.340<br>1.095<br>1.723<br>1.421<br>1.475<br>1.054|Turnover<br>2.255<br>2.125<br>2.155<br>0.572<br>0.538<br>0.470<br>0.468<br>0.737<br>0.521<br>1.170<br>1.227<br>0.706<br>1.136<br>0.000|Leverage<br>0.323<br>0.335<br>0.335<br>0.348<br>0.348<br>0.356<br>0.350<br>0.328<br>0.314<br>0.344<br>0.348<br>0.324<br>0.270<br>0.000|Max weight<br>0.084<br>0.084<br>0.084<br>0.084<br>0.084<br>0.084<br>0.084<br>0.084<br>0.084<br>0.084<br>0.084<br>0.084<br>0.084<br>0.003|Min weight<br>–0.084<br>–0.084<br>–0.084<br>–0.069<br>–0.071<br>–0.084<br>–0.084<br>–0.084<br>–0.084<br>–0.084<br>–0.070<br>–0.084<br>–0.084<br>0.003|MCS_p_-value<br>0.000<br>0.000<br>0.000<br>1.000<br>0.196<br>0.320<br>0.196<br>0.001<br>0.000<br>0.001<br>0.095<br>0.001<br>0.000<br>0.000|Panel (c): GMVPs for_h_¼5|Std. dev<br>12.791<br>11.497<br>11.804<br>7.526<br>7.923<br>8.012<br>8.028<br>8.386<br>8.387<br>8.102<br>8.081<br>8.117<br>8.426<br>12.848|Average<br>17.523<br>12.850<br>12.727<br>11.268<br>10.959<br>10.061<br>10.393<br>13.264<br>12.279<br>12.363<br>11.265<br>11.842<br>16.675<br>14.530|Sharpe ratio<br>1.370<br>1.118<br>1.078<br>1.497<br>1.383<br>1.256<br>1.295<br>1.582<br>1.464<br>1.526<br>1.394<br>1.459<br>1.979<br>1.131|Turnover<br>12.233<br>9.634<br>7.980<br>2.036<br>1.807<br>1.213<br>1.218<br>2.447<br>1.217<br>3.061<br>4.219<br>2.023<br>2.945<br>0.000|Leverage<br>0.476<br>0.465<br>0.458<br>0.469<br>0.479<br>0.490<br>0.483<br>0.502<br>0.466<br>0.474<br>0.491<br>0.482<br>0.460<br>0.000|Max weight<br>0.288<br>0.627<br>0.536<br>0.135<br>0.122<br>0.170<br>0.169<br>0.384<br>0.151<br>0.131<br>0.182<br>0.170<br>0.188<br>0.003|Min weight<br>–0.343<br>–0.318<br>–0.263<br>–0.064<br>–0.065<br>–0.072<br>–0.068<br>–0.073<br>–0.079<br>–0.041<br>–0.086<br>–0.091<br>–0.091<br>0.003|MCS_p_-value<br>0.000<br>0.000<br>0.000<br>1.000<br>0.028<br>0.138<br>0.028<br>0.028<br>0.028<br>0.028<br>0.028<br>0.028<br>0.028<br>0.000|Notes: The table shows the summary statistics of the constructed portfolios over the out-of-sample period from January 2012 to December 2015 using stocks from S&P 500|Index. The optimization problem inEquation (20)is implemented with_s_¼20%and_u_¼1_=_ð2log_N_Þ. The confdence level for the MCS procedure is 90% and is implemented|using the stationary bootstrap with 30_;_000 bootstrap replications and an average block length of 5. The standard deviations and averages are annualized.|Downloaded from https://academic.oup.com/jfec/article/23/2/nbae018/7738288 by DO NOT USE Institute of Education merged with 9000272 user on 20 May 2026|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|



**24** _Journal of Financial Econometrics_ 

**==> picture [337 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
15<br>RW<br>1F-HC<br>10F-S<br>10 BEKK-NL<br>1F-LASSO<br>5<br>0<br>2013 2014 2015<br>**----- End of picture text -----**<br>


**Figure 3.** This figure compares the annualized accumulated volatility of the daily GMVPs for five different models for each year in the out-of-sample period from 2012 to 2015. The cumulative portfolio volatility is fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi **f** _t_ defined as qP _s_ ¼1[ð] _[w][s]_[ð] _[h]_[Þ][0] _[r][s]_[ð] _[h]_[ÞÞ][2] . 

models, we observe a slight reduction in the portfolio standard deviation by imposing a factor structure with a block structure in the idiosyncratic covariance, relative to using the unconstrained covariance estimator in Equation (7). 

Given that the results of the daily GMVP analysis are in favor of the CLUHFF models, it is of interest to study whether the models are performing well over the entire out-of-sample period, or whether the good performance can be attributed to a specific period. To this fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi f end, we plot the cumulative portfolio volatility defined as rP _ts_ ¼1 � _[w][s]_ � _[h]_[Þ][0] _[r][s]_ ð _[h]_ Þ�2 yearly in Figure 3. In this figure, we consider the portfolios constructed based on the RW model, the 1F-HC model, the 10F-S model, the BEKK-NL model, and the 1F-LASSO model. The figure shows that the ranking among the models is stable across the years, with the 1F-HC model consistently being the best model followed by the 10F-S model. In Panel (b), we show the results using the objective function in Equation (20) with _h_ ¼ 1. In this scenario, we control the amount of leverage by imposing _s_ ¼ 20% and set the lower and upper bounds on the weights as _u_ ¼ 1 _=_ ð2log _N_ Þ. This choice of _u_ corresponds to a bound of 0.084 for the S&P 500 Index sample. 

The results suggest that the CLUHFF models perform best also in the presence of restrictions on the portfolio weights. All four implementations of the CLUHFF model are included in the 90% MCS, whereas none of the competitor models are included. The portfolio standard deviations across the CLUHFF models are very similar but again with the 1F-HC as the best-performing model overall based on the portfolio standard deviation metric. Except for the RW models, the portfolio standard deviations in Panel (b) have increased relative to the GMVP results in Panel (a). However, the measures of turnover are greatly reduced in the presence of constraints. 

Finally, in Panel (c) of Table 3 we consider an investor with a weekly investment horizon ( _h_ ¼ 5). That is, the investor chooses at days _t_ ¼ _t_ 0 _; t_ 0 þ 5 _;_ ... _; T −_ 5 the portfolio weights for a portfolio to be held for the following week based on a forecast of the 5-day cumulative covariance matrix. To construct weekly forecasts of the covariance matrix, we use the direct forecasting approach outlined in the Supplementary Appendix. 

Also in this scenario, the 1F-HC CLUHFF model produces the portfolios with the smallest standard deviation (7.526%) followed by the other three CLUHFF variants. The HCbased CLUHFF models, 1F-HC and 10F-HC, are the only two models in the 90% MCS. However, in this case, we generally find the CLUHFF model to produce the portfolios with 

Bodilsen j Large-Dimensional Portfolio Selection **25** 

the lowest returns, which results in several of the other models achieving a higher out-ofsample Sharpe ratio. 

In Supplementary Appendix Tables A.6–A.8, we provide additional out-of-sample portfolio allocation results for the S&P 100 Index and the Dow Jones Industrial Average as a robustness check. Also for these asset universes, the CLUHFF models are found to be dominant in terms of portfolio standard deviation. 

## **8 Conclusion** 

In this article, we introduce the CLUHFF model, a novel approach for modeling and forecasting large-dimensional covariance matrices of stock returns. The model belongs to the class of dynamic factor models, where the common factors are observable traded assets. The components determining the covariance structure are modeled using autoregressive time series models. This leads to a highly flexible multivariate volatility model, which produces a well-conditioned and positive definite forecast of the latent covariance matrix. Furthermore, the model is extremely easy and computationally fast to estimate even in very high dimensions. As a novel feature, we use a data-driven hierarchical clustering approach to determine the structure of the idiosyncratic covariance matrix. In the empirical application, we study the economic value of our new modeling approach through portfolio allocation problems. At the daily level, the best-performing model reduces the portfolio standard deviation by approximately 50% compared to an equal-weighted portfolio consisting of the stocks in the S&P 500 Index in a global minimum variance setting. We find the superiority of the newly developed models to be robust to the presence of restrictions on the portfolio weights and the choice of investment horizon. 

A refinement of the CLUHFF model introduced in this article is to develop a more theoretical grounded way of selecting the number of clusters in the idiosyncratic covariance matrix when using the HC algorithm. In the present article, we use a fixed threshold to assign stocks to different clusters based on insights from a realistic large-scale simulation study conducted in this article. A more rigorous way of determining the block structure is desirable and could potentially lead to a refinement of the model. We leave this interesting issue for further research. 

## **Supplemental Data** 

Supplemental data are available at https://www.datahostingsite.com 

## **References** 

Aït-Sahalia, Y., and D. Xiu. 2017. Using Principal Component Analysis to Estimate a High Dimensional Factor Model with High-Frequency Data. _Journal of Econometrics_ 201: 384–399. 

Alves, R. P., D. S. de Brito, M. C. Medeiros, and R. M. Ribeiro. 2024. Forecasting Large Realized Covariance Matrices: The Benefits of Factor Models and Shrinkage. _Journal of Financial Econometrics_ 22: 696–742. 

Andersen, T. G., T. Bollerslev, F. X. Diebold, and G. Wu. 2006. Realized Beta: Persistence and Predictability. _Econometric Analysis of Financial and Economic Time Series_ 20: 1–39. Andersen, T. G., M. Thyrsgaard, and V. Todorov. 2021. Recalcitrant Betas: Intraday Variation in the Cross-Sectional Dispersion of Systematic Risk. _Quantitative Economics_ 12: 647–682. 

- Archakov, I., and P. R. Hansen. 2021. A New Parametrization of Correlation Matrices. _Econometrica_ 89: 1699–1715. 

Archakov, I., P. R. Hansen, and Y. Luo. 2023. A New Method for Generating Random Correlation Matrices. _The Econometrics Journal_ 27: 188–212. 

**26** _Journal of Financial Econometrics_ 

Barndorff-Nielsen, O. E., P. R. Hansen, A. Lunde, and N. Shephard. 2009. Realized Kernels in Practice: Trades and Quotes. _The Econometrics Journal_ 12: C1–C32. 

Barndorff-Nielsen, O. E., P. R. Hansen, A. Lunde, and N. Shephard. 2011. Multivariate Realised Kernels: Consistent Positive Semi-Definite Estimators of the Covariation of Equity Prices with Noise and Non-Synchronous Trading. _Journal of Econometrics_ 162: 149–169. 

Barndorff-Nielsen, O. E., and N. Shephard. 2004. Econometric Analysis of Realized Covariation: High Frequency Based Covariance, Regression, and Correlation in Financial Economics. _Econometrica_ 72: 885–925. 

Bollerslev, T., A. J. Patton, and R. Quaedvlieg. 2018. Modeling and Forecasting (un) Reliable Realized Covariances for More Reliable Financial Decisions. _Journal of Econometrics_ 207: 71–91. 

Bollerslev, T., A. J. Patton, and H. Zhang. 2021. Equity Clusters through the Lens of Realized Semicorrelations. _Economics Letters_ 211: 110245. 

Buccheri, G., G. Livieri, D. Pirino, and A. Pollastri. 2020. A Closed-Form Formula Characterization of the Epps Effect. _Quantitative Finance_ 20: 243–254. 

Callot, L. A., A. B. Kock, and M. C. Medeiros. 2017. Modeling and Forecasting Large Realized Covariance Matrices and Portfolio Choice. _Journal of Applied Econometrics_ 32: 140–158. 

Chamberlain, G., and M. Rothschild. 1983. Arbitrage, Factor Structure, and Mean-Variance Analysis on Large Asset Markets. _Econometrica_ 51: 1281–1304. 

Chiriac, R., and V. Voev. 2011. Modelling and Forecasting Multivariate Realized Volatility. _Journal of Applied Econometrics_ 26: 922–947. 

Corsi, F. 2009. A Simple Approximate Long-Memory Model of Realized Volatility. _Journal of Financial Econometrics_ 7: 174–196. 

Corsi, F., and R. Reno. 2012. Discrete-Time Volatility Forecasting with Persistent Leverage Effect and the � Link with Continuous-Time Volatility Modeling. _Journal of Business & Economic Statistics_ 30: 368–380. 

De Nard, G., O. Ledoit, and M. Wolf. 2021. Factor Models for Portfolio Selection in Large Dimensions: The Good, the Better and the Ugly. _Journal of Financial Econometrics_ 19: 236–257. 

- DeMiguel, V., L. Garlappi, and R. Uppal. 2009. Optimal versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy? _Review of Financial Studies_ 22: 1915–1953. 

Engle, R. 2002. Dynamic Conditional Correlation: A Simple Class of Multivariate Generalized Autoregressive Conditional Heteroskedasticity Models. _Journal of Business & Economic Statistics_ 20: 339–350. 

Engle, R. F., and K. F. Kroner. 1995. Multivariate Simultaneous Generalized ARCH. _Econometric Theory_ 11: 122–150. 

Engle, R. F., O. Ledoit, and M. Wolf. 2019. Large Dynamic Covariance Matrices. _Journal of Business & Economic Statistics_ 37: 363–375. 

- Fan, J., A. Furger, and D. Xiu. 2016. Incorporating Global Industrial Classification Standard into Portfolio Allocation: A Simple Factor-Based Large Covariance Matrix Estimator with High-Frequency Data. _Journal of Business & Economic Statistics_ 34: 489–503. 

- Golosnoy, V., B. Gribisch, and R. Liesenfeld. 2012. The Conditional Autoregressive Wishart Model for Multivariate Stock Market Volatility. _Journal of Econometrics_ 167: 211–223. 

- Grant, M., and S. Boyd. 2014. March). CVX: Matlab software for disciplined convex programming, version 2.1. http://cvxr.com/cvx. 

- Gribisch, B., J. P. Hartkopf, and R. Liesenfeld. 2020. Factor State–Space Models for High-Dimensional Realized Covariance Matrices of Asset Returns. _Journal of Empirical Finance_ 55: 1–20. 

Hansen, P. R., A. Lunde, and J. M. Nason. 2011. The Model Confidence Set. _Econometrica_ 79: 453–497. Hansen, P. R., A. Lunde, and V. Voev. 2014. Realized Beta GARCH: A Multivariate GARCH Model with Realized Measures of Volatility. _Journal of Applied Econometrics_ 29: 774–799. 

Harris, F. H., T. H. McInish, G. L. Shoesmith, and R. A. Wood. 1995. Cointegration, Error Correction, and Price Discovery on Informationally Linked Security Markets. _The Journal of Financial and Quantitative Analysis_ 30: 563–579. 

- Hartkopf, J. P. 2023. Composite Forecasting of Vast-Dimensional Realized Covariance Matrices Using Factor State-Space Models. _Empirical Economics_ 64: 393–436. 

Jagannathan, R., and T. Ma. 2003. Risk Reduction in Large Portfolios: Why Imposing the Wrong Constraints Helps. _The Journal of Finance_ 58: 1651–1683. 

Bodilsen j Large-Dimensional Portfolio Selection **27** 

Ledoit, O., and M. Wolf. 2012. Nonlinear Shrinkage Estimation of Large-Dimensional Covariance Matrices. _The Annals of Statistics_ 40: 1024–1060. 

Ledoit, O., and M. Wolf. 2017. Nonlinear Shrinkage of the Covariance Matrix for Portfolio Selection: Markowitz Meets Goldilocks. _The Review of Financial Studies_ 30: 4349–4388. 

Lunde, A., N. Shephard, and K. Sheppard. 2016. Econometric Analysis of Vast Covariance Matrices Using Composite Realized Kernels and Their Application to Portfolio Choice. _Journal of Business & Economic Statistics_ 34: 504–518. 

Markowitz, H. 1952. Portfolio Selection. _The Journal of Finance_ 7: 77–91. 

Murtagh, F., and P. Contreras. 2012. Algorithms for Hierarchical Clustering: An Overview. _WIREs Data Mining and Knowledge Discovery_ 2: 86–97. 

Noureldin, D., N. Shephard, and K. Sheppard. 2012. Multivariate High-Frequency-Based Volatility (HEAVY) Models. _Journal of Applied Econometrics_ 27: 907–933. 

Oh, D. H., and A. J. Patton. 2016. High-Dimensional Copula-Based Distributions with Mixed Frequency Data. _Journal of Econometrics_ 193: 349–366. 

Oh, D. H., and A. J. Patton. 2023. Dynamic Factor Copula Models with Estimated Cluster Assignments. _Journal of Econometrics_ 237: 105374. 

Opschoor, A., P. Janus, A. Lucas, and D. Van Dijk. 2018. New HEAVY Models for Fat-Tailed Realized Covariances and Returns. _Journal of Business & Economic Statistics_ 36: 643–657. 

Pakel, C., N. Shephard, K. Sheppard, and R. F. Engle. 2021. Fitting Vast Dimensional Time-Varying Covariance Models. _Journal of Business & Economic Statistics_ 39: 652–668. 

Rand, W. M. 1971. Objective Criteria for the Evaluation of Clustering Methods. _Journal of the American Statistical Association_ 66: 846–850. 

Sheppard, K., and W. Xu. 2018. Factor High-Frequency-Based Volatility (HEAVY) Models. _Journal of Financial Econometrics_ 17: 33–65. 

Vassallo, D., G. Buccheri, and F. Corsi. 2021. A DCC-Type Approach for Realized Covariance Modeling with Score-Driven Dynamics. _International Journal of Forecasting_ 37: 569–586. 

Ward, J. H. 1963. Hierarchical Grouping to Optimize an Objective Function. _Journal of the American Statistical Association_ 58: 236–244. 

© The Author(s) 2024. Published by Oxford University Press. All rights reserved. For permissions, please email: journals.permissions@oup.com Journal of Financial Econometrics, 2024, 23, 1–27 https://doi.org/10.1093/jjfinec/nbae018 Article 

