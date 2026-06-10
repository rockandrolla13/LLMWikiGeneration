# Revisiting stylised facts: information clock, persistence, long memory and dependence 

Andreas Koukorinis[∗] , Gareth W. Peters[†] Guido Germano[‡] 

## **Abstract** 

We examine the emergence of stylised empirical facts from the statistical analysis of price and volume processes in various types of financial instruments during recent market periods, including cryptocurrencies and futures. We focus on the role of persistence (long memory) or arrival rates and dependence using empirical copulas. As part of this study, various statistical properties of asset returns are considered: distributional properties; tail properties and dependence; extreme fluctuations; path-wise regularity; linear and non-linear dependence of returns in time and across instruments. We analyze the behaviors of spot prices, returns and volumes using selected stochastic clocks. Furthermore, we investigate inter-arrival times of trades and their relationship to returns and realised volatility. We present a model to predict the timing of such jumps. 

_**Index terms—**_ Duration, Gaussian process, returns, stylised facts, volatility, volumes. 

## **1 Introduction** 

This paper studies the statistical features and empirical facts in the futures markets in a high-frequency setting. First, we describe the high frequency data and define a set of variables and statistical tests of interest. 

Understanding the properties of these empirical facts plays an important role in understanding market micro-structure, the evolution and development of market making algorithms and possibly can help in setting appropriate regulation. In contrast to most of the existing literature, we review the arguments behind the choices of stylized facts about asset prices relevant for time horizons of seconds or less. 

We concentrate on the following areas: the distribution of price changes, realised variance and its extension in bi-power variation, inter-arrival rates and volumes, order imbalance and finally persistence of trade flow. At the center of this work is multi-fractal detrended fluctuation analysis (henceforth, MFDFA) and kernel two sample testing. We use MFDFA to derive various quantities to characterise the variability and uncertainty of the empirical time series. 

For each of the phenomena, we raise and try to answer a series of questions that relate to what extent can we identify the same phenomenon in each market and if the behaviour has changed given the increase of trading activity by algorithmic strategies. In addition, we review the existence of similar phenomena in the crypto-currency market. Our work is organised as follows: in the following section 1.3, we define our notation.In section **??** , we recall the stylised facts and discuss the major findings in the literature. For each phenomenon, we set a series of questions that our work seeks to address. This study is focused on a unique and specific instruments of certain markets in fairly recent periods in financial market history. We advise prudence versus generalising these results, as most findings in literature are not verified across time and instruments. The informational effect of trades is a topic of significant interest for both practitioners as well as in different areas of applied academic research. 

This paper makes a contribution by applying a well known statistical machine learning methodologies to evaluate these artefacts and to highlight if the samples are from different distributions. 

Which name shall I use, both are used in literature? 

> ∗University College London 

> †University of California, Santa Barbara 

> ‡University College London 

## **1.1 Contributions** 

The first set of contributions of this paper is an empirical study of statistical elements of the time-series and temporal aspect of certain elements of the order books. Specifically, within this setting, we will: 

1. Use MFDFA at a central element of the work, to derive quantities that will help examine any presence time-varying short-term inefficiencies. 

2. We use kernel two-sample and goodness-of-fit tests on order-book derived variables and MFDFA-derived quantities on data that have been transformed using information clocks (clocks based on trading activity and volume traded). 

   - These kernel-based methods are used to compare the nature of the distributions; by comparing across days, across information clock transformations, as well as comparing the distributions across different instruments of the same asset class. The goal is to detect whether these procedures create systematic differences in the data distributions, or in fact such transformation can aid in creating quantities that are more stable and in fact stationary. 

3. Present evidence categorising well known statistical abnormalities known as _stylised facts_ in terms of long-memory (or persistence) in order flow, as well as understand the empirical dependence structure that links arrival rates of trades and the variations of the price process. 

4. Identify and test the concepts of memory and persistence in the intraday activity flow of various financial instruments, particularly futures which are largely unexplored. 

5. Finally, we present a brief examination of the relationship between trade sizes, arrival rates, and intra-day returns(and realised variance) by utilising copulas and independence testing. 

## **1.2 Organization of the paper** 

Section 1.3 introduces the notation for the paper. Sections 3 and **??** detail respectively our examination of price return distributions, realised variance and its extensions across various stochastic/information clocks, and explain how we plan to incorporate them into our modelling approach. Section **??** , and in section **??** the kernel based two sample test methodology is presented. In section **??** , we demonstrate the proposed tests and show numerical results and comparisons across assets. 

## **1.3 Notation** 

Normal face _x_ represents a scalar, lowercase boldface **x** represents a vector, and capital boldface **X** represents a matrix. A vector component is denoted in normal face with a subscript; for example, _xi_ is element _i_ of vector **x** . A bold lowercase letter with an index, e.g. **x** _i_ , denotes row _i_ of matrix **X** . 

|tor **x**. A bol|d lowercase letter with an index, e.g. **x**_i_, denotes row _i_ of matrix **X**.|
|---|---|
|Symbol|Description|
|_x ∼p_(_x_)|_x_ is drawn from, or distributed according to, distribution _p_(_x_)|
|**h**(**x**)|A feature vector|
|_ka_+_kb_|Addition of kernels, shorthand for _ka_(**x**_,_**x**_′_) +_kb_(**x**_,_**x**_′_)|
|_ka × kb_|Multiplication of kernels, shorthand for _ka_(**x**_,_**x**_′_)_× kb_(**x**_,_**x**_′_)|
|_k_(**X**_,_**X**)|The Gram matrix, whose _i, j_th element is _k_(**x**_i,_**x**_j_)|
|**K**|Shorthand for the Gram matrix _k_(**X**_,_**X**)|
|**_f_**(**X**)|A vector of function values, whose element _i_ is _fi_(**x**)|
|mod(_i, j_)|The modulo operator that gives the remainder of dividing the integer _i_ by the<br>integer _j_|
|**Y**:_,d_|Column _d_ of matrix **Y**.|



## **2 General framework for information clocks** 

One of the important elements of our work is the study of various phenomena using sampling frequencies that are are more _natural_ to the high-frequency microstructure of modern financial markets. The notion of time with respect to market activity provides more clarity about the arrival of new information and therefore the formation of these phenomena. This concept is not new, so we follow established definitions [1, 2, 3, 4, 5]. The novelty in our work is to characterise and discuss the more prevalent stylised facts in _information time_ . 

A stochastic clock is supposed to capture the _information_ time of the market, i.e, we wish to sample the market based on the arrival of new information. We can classify time series data as _homogeneous_ or _in-homogeneous_ based on the regularity of their arrival rate in calendar time [6]. We will use the terms _information clock/time_ or _event clock/time_ interchangeably. But 

Following Clark [7], the concept of _information event_ will refer to the _arrival of new information_ as a a quantitative measure of information arrival based on increments of the information time process. 

For example, raw price data that arrives at random times is _in-homogeneous_ . A transformation into a _homogeneous_ time series occurs by sampling at a specific frequency using a different process [6, 8]. Thus, we can construct a _homogeneous_ time series by sampling at some predefined frequency and then using an interpolation technique [9]. 

In this work, the focus is on a statistical description of prices as a function of the information that is revealed in the market from the arrival of a trade or the cumulative traded volume being high enough (and above some threshold) to reveal new information. This premise reflects similar intuition as past work from Mandelbrot in [10], Easley in [11], Knuth [12],O’Hara [13] and others. 

## **2.1 Modelling in information time** 

We will need to model the _deformed_ stochastic process that defines the asset price in _information time_ . Hence, hence we define two processes, the first will be used for the price process and the second will model the market activity, which changes over calendar time. [3] 

Before we begin, we introduce the method of subordination as described in [14] and [15]. The purpose is to use a formal mathematical framework to substitute physical or calendar time by information time which is a natural way of observing statistical facts in the market. 

## **2.1.1 Subordinated process** 

We follow the definition of Bochner in [15], to define a _subordinator_ . This definition has been used extensively in literature [7, 1, 2, 3, 6, 4]. 

## **Definition 1.** _Subordinator_ 

_A subordinator Q_ ( _t_ ) _is a right continuous non-decreasing stochastic process with values in_ R+ _that has independent and homogeneous increments._ 

This will allows us to construct a Markov process with is locally time-homogeneous. Now, let us assume we have a stochastic process _W_ ( _t_ ) indexed by a continuous variable _t_ , which represents calendar or physical time. This variable will be observed a discrete points _tn, n ∈_ N. 

## **Definition 2.** _Subordinated process_ 

_We can now define a new composite process W_ ( _Q_ ( _t_ )) _, t ≥_ 0 _by taking the original process W as a function of the subordinator Q which transforms calendar time to information time._ 

_is the word compound correct here, this does not refer to Poisson processes which is usual in literature_ 

_It is usually required that the information clock Q is an unbiased representation of calendar time t, i.e. that E_ ( _Q_ ( _t_ )) = _t._ 

## **2.1.2 Information time** 

To develop the analysis using _information time_ , we must identify a good information time process [16, 6]. Among the many used in the literature, we focus on the cumulative trade volume process, the cumulative trade count process, and the cumulative trade value process, with respect to all transactions up to and including calendar time _t_ as activity descriptor. 

Thus, we will use three information clocks: the one based on the _cumulative trade volume_ , which we will be known as the _volume clock_ , the one based on the cumulative transaction value, which will be known as _volume value clock_ , and finally the _cumulative transaction_ based clock which will be known as the _tick or activity clock_ . All three are monotonic functions of physical time. 

Next, we fix out notation more rigorously. Our goal by using these transformations based of market quantities, rather than the raw time series of asset prices themselves, is that the despite these transformations can we identify characteristics patterns in the data that correspond to the well known stylised facts [11]. In terms of calendar time _t ∈_ R, _ωt_ will measure the units of information time up to calendar time _t_ . 

|Symbol|Description|
|---|---|
|_t_|calendar time|
|_T_|time interval of length _n_,containing _t_0_, t_1_, t_2_, . . . , tn_|
|_Q_(_t_)|information time process|
|_ωt_|number of units of information time that have passed up to time _t_|
|_λ_(_t_)|instantaneous arrival rate of trades up to time _t_|
|_W_(_Q_(_t_))|Brownian motion under information time|
|_pt_|price quote sampled in calendar time at time _t_|
|_N_(_T_)|cumulative number of trades in interval _T_|
|_V_(_T_)|traded volume in interval _T_|
|_QN_|information time based on cumulative number of trades|
|_QV_|information time based on cumulative volume of trades|
|_QP V_|information time based on value of the cumulative volume of trades|



Table 1: Description of all the variables used in our work. The event indicator _i_ will take values in R[+] different clocks. The information time will either be calendar or volume or tick/transaction time in our work. 

## **Definition 3.** _Tick time_ 

_Let us define the cumulative number of trades up to calendar time t as Q[N]_ ( _t_ ) _._ 

## **4.** _Volume time_ 

_Let us define the cumulative volume traded up to calendar time t as Q[V]_ ( _t_ ) _._ 

## **2.2 Sampling rate for information clocks** 

The frequency of the sampling for any of the information clock frequency is usually made with respect to the properties of the resulting distribution of returns. The weight in the tails of the return distribution is specifically sensitive to the choice of sampling rate, i.e how much volume in each of the volume clock ticks, or how many trades in the activity clock. To determine the appropriate choice, we construct volume clocks at different sampling frequencies, and measure their in-sample deviation from a normal distribution. For the 

## **2.3 Variable definitions** 

Next, we define a number of variables that will be used in our work, in order to capture the dynamics of the market at higher frequency., We will enhance our data set with some specific features which are of interest. you have used the same notation for the natural log? 

## **Definition 5.** _Trade vector in calendar time_ 

_Let,_ **x** _ti ≡_ ( _pti, ωti_ ) _represent a trade of a financial instrument (in our case, a future, a stock or a cryptocurrency ) executed at time ti, at a price p[trade] ti , and with size/volume of trade ωti. With ξti_ = ln ( _pti_ ) _being the natural logarithm._ 

For example, in an event time based on the activity clock, we will have the passage of one tick based on the occurrence of one trade i.e. ., from an initial trade _i_ to the the next trade thereafter, similar to the volume clock of [11]. 

We have defined the price(quote) process as _pt_ and the parent process in terms of the information time as _W_ ( _q_ ), as in [4]. 

## **Definition 6.** _Price subordination to the information clock_ 

_The price process is said to be subordinated to the parent process W , and the subordinator (in our case either Q_ ( _t_ ) _, is a process that measures the information flow of the market [4]. For example, the price process under transaction clock is as follows:_ 


![](markdown_output/Stylised_Facts_Paper_Only_images/Stylised_Facts_Paper_Only.pdf-0004-16.png)


There are numerous advantages in using trade clocks for example: there is an implicit adjustment for crosssectional variation in trade frequencies, and they closely correspond to processes used by electronic market makers who allocate risk capital as a function of traded dollar volume rather than calendar time elapsed [17]. All the variables, can be defined with respect to any of the information clocks. 

**Definition 7.** _Tick frequency We define the tick frequency fi at time ti as the reciprocal of the duration_ ∆ _ti [16],_ 


![](markdown_output/Stylised_Facts_Paper_Only_images/Stylised_Facts_Paper_Only.pdf-0005-01.png)


_The tick frequency is the number of ticks per time unit._ 

## **2.4 Order book derived variables** 

Thus for a given _scale_ , ∆ _ti_ , will take values either in calendar clock (e.g. , the values can be in milliseconds, hours, days) or in event clock, where events can be for example trades or thresholds of accumulated traded volume. 

## **Definition 8.** _Price returns_ 

_Returns at scale_ ∆ _ti can be defined as: ξti,_ ∆ _ti ≡ pti_ +∆ _ti − pti. Lags in calendar time, will be denoted by the letter τ , which will be a multiple of_ ∆ _ti. Hence, for the unit interval τ will take the value 1._ 

As we will show in subsequent sections, returns can depend (greatly) on the choice of ∆ _ti_ , therefore we will relax the usual implicit econometric assumptions (of simple unit intervals). 

## **Definition 9.** _Duration_ 

_Duration is broadly defined as the difference in physical or information time between two events. This linear transformation defines a thinly point process, as a subset of the original data set._ 

We will define the following measures of duration: 

## **Definition 10.** _Trade and quote duration_ 

_For ease of use, we will refer to the measurements on chronological time as unclocked, and denote that inter-event arrival time between two consecutive events (quotes or trades) as ⌈ti, and will represent the chronological time interval between two transactions occurring at times ti−_ 1 _, ti._ 

- _Trade duration: as the information time between two consecutive trades._ 

- _Quote duration: as the information time difference between two consecutive quotes_ 

- _Volume- quote duration: the time between two quotes such that the volume traded surpasses a certain threshold. The volume duration process Di[volume] ._ 

_These do not necessarily need to be defined on a specific bid-ask quote. For our purposes, these will be defined on the trade process, thus simply the activity that can be sampled such that certain amount of volume traded._ 

## **11.** _Bars_ 

_Bars refer to the method of representing information (in our case price, traded volume, or number of trades) based on some specific sampling rate or methodology which is fixed, [18]. Time bars to refer to both intraday (high frequency) and interday (low frequency) data since the sampling occurs at fixed intervals of time for both intraday and interday time bars._ 

Using the above definition, we can define as an example, _time bars_ which will refer to data sampled (both intra-day and inter-day) at fixed intervals of calendar time. Similarly, we can define _volume bars_ which refer to fixed intervals of traded volume (hence, sampling every time a pre-defined amount of the instrument’s units has traded). And finally _tick bars_ , where the information is sample at pre-defined number of transactions or _dollar-volume bars_ which refer to fixed intervals of the value of traded volume. 

For each bar type, as information time accumulates, we will sample a vector of relevant information. 

## **Definition 12.** _Open, high, low, close prices_ 

_Let us assume an interval T as in_ **??** _. We define p_ high = sup _p_ ( _T_ ) _, p_ low = inf _p_ ( _T_ ) _, popen_ = _pt_ 0 _, pclose_ = _ptn. The interval may be defined by any choice of an information clock._ 

Figure 1: We visually represent histograms of GK volatility estimated using 3 different windows, for two separate information clocks. On the right a tick-based and on the left volume based. For both implementations the shapes are similar, with an extreme skew visible as the tick frequency is reduced (to a higher frequency). 

## **2.4.1 Intraday volatility** 

Price levels sampled at specific bar frequency have been been used in various statistical models over considered sampling frequencies for estimation and forecasting of volatility. However, with the wider availability of higher frequency data, we can developing models and algorithms that utilize more of information. In our study we use an estimator of realised volatility based on intraday price ranges as defined at the various clocks. We make the following definition as follows: 

## **Definition 13.** _Volatility_ 

_We define volatility as a measure of the variability of the price of a financial instrument over a measure of time. The estimation is dependent on the particular time horizon, hence we express it in annualised terms, which is the convention [19, 20]._ 

## _add formulas here_ 

Given the nature of our data, the need for an estimator that utilises intra-day information. Hence, we use range-based volatility estimation that involves an _open, high, low and close_ values for particular segments to produce an estimate. For more details on volatility estimators, we point the interested reader to the following references [21, 20]. Volatility does not convey any information about the likely direction of price changes. In our setting, we enhance the open and closing prices for the intervals defined by each bar, by the highest and lowest trading prices over the interval defined by the choice of bars. volatility. To avoid the microstructure biases introduced by high-frequency data and based on the conclusion of Chen et al. (2006), that the rangebased and high-frequency integrated volatility provide essentially equivalent results, we employ the classic range-based estimator of Garman an 

the definition below is not complete 

In our work, we will use the _Garman-Klass_ volatility estimator, [ **?** ]: 


![](markdown_output/Stylised_Facts_Paper_Only_images/Stylised_Facts_Paper_Only.pdf-0006-09.png)


## **3 The nature of intraday return distribution** 

The choice of distribution of financial asset returns has fundamental implications for modelling purposes, regardless of the sampling frequency. Modern day market applications require data modelling methods that capture the structural properties properly. However, there are several major issues in the modelling and forecasting of financial time series returns. First and foremost, the data is non stationary and usually with an asymmetric distribution. There are no fixed models that work all the time. The view that long term 

returns tend to approximate Gaussian, that has been motivating a lot of the empirical research proved to detrimental. Emphasizing variance has allowed risk to creep in via higher moments. At high-frequency sampling rates for returns, a growing body of literature has shown the empirical distribution of assets (various time-frequencies) is leptokurtotic. Examples of such work are, [ **?** ], [22] and [ **?** ]. In [ **?** ], the authors using a sample of high-frequency returns for 20 heavily traded US stocks, provide empirical evidence that shows that effective modelling requires continuous distributions able to capture leptokurtic, skewed, and the multimodal nature of financial data. Microstructure noise can induce upward bias in the kurtosis of standardized returns because, when volatility varies across trading days, standardized returns follow a mixture of (near) normals. Various authors have been suggesting, the use of a multivariate distribution. The main contrast of a univariate with a multivariate distribution is that the covariance matrix partly describes the dependence structure perhaps just enough for a Gaussian. However, a major shortcoming of the multivariate distribution for financial data, is that all variables have equally fat tails (sharing the same degrees of freedom) as shown in [ **?** ], [23]. In short, there is an inability to model and account for the relevance of asymmetric features as shown in [23]. 

To this end, mixture of (normal) distributions have been empirically found by numerous authors in both the unconditional and conditional framework to be of particularly flexible for modelling financial data [ **?** ]. There is enough flexibility to enable various shapes of continuous distributions, and able to capture leptokurtic, skewed and multi-modal characteristics of financial time series data. 

In this experimental section 6, we investigate through empirical experiments these topics. Specifically]: 

Using the different instruments and stochastic clocks, How does the shape of the distribution change for varying sampling rates? 

Can the normality of asset returns be recovered if we consider a stochastic time change (to an activity clock or a volume clock). 

Do different assets exhibit the same shape or we can motivate different choices? 

Our work highlights the role of relative contract specifications, especially relative price increments, between two similar assets, in determining differences in benchmark statistical facts. 

the following section needs a lot of work 

## **3.1 Symmetry of movements** 

This property relates to the fact that the left and right tail of the distribution of return is not the same. Most investors, when asked will correctly affirm that the left and right tail of the return distribution is not the same, with the left tail being larger. The behaviour of returns at the tail, can is be described by the so-called tail index. This index measures the fat-tailedness of the distribution. 

the following section needs a lot of work 

## **3.1.1 Intermittent nature of trading activity** 

In [22], it is believed that returns show a high degree of variance regardless of the measurement of scale. This behaviour is evidenced by volatility bursts, regardless of the estimator [22]. To that effect, we investigate both the effect of the arrival rate of trades on price changes (therefore volatility) and volume. We argue that... 

## **3.1.2 The nature of arrival rates and volatility** 

## **3.2 Description of the data** 

This section provides detail of the irregularly spaced data that is used throughout the remainder of this research. We analyse quote and transaction data.To perform our analysis, we first collect raw data, then define and select a set of events. To exhibit some universality in our findings, a large number of data sets and instruments is required. Our data set consists of futures data and cryptocurrency data (which have behaviour similar to futures). The data is recorded at millisecond accuracy, and we analyse both quotes and trades. Trades arrive at irregular intervals, whereas we can record market data at regular intervals. 

We will sample the market at regular intervals (for the purposes of studying the effects of changing the information clock), but also at irregular intervals as trades have such arrival rates (and for the purposes of studying effects under the calendar and event times). We have a range of data recorded over 2018, 2019 and 2020. 

calculate sampling frequency 

The Table summarises the basic characteristics of the instruments, we use for this study. 


![](markdown_output/Stylised_Facts_Paper_Only_images/Stylised_Facts_Paper_Only.pdf-0008-00.png)


**----- Start of picture text -----**<br>
StylisedFactsPaper/figures/Tick bars clockarrival-rate<br>500 750 1000-1250<br>rates for VolumeBars Clock<br>(a) (b)<br>**----- End of picture text -----**<br>


Figure 2: Differences in the profiles of arrival time differences (duration) exhibit large differences which are primarily driven by the choice of information clock. On (a) the arrival rate is estimated at a fixed amount of volume traded where we look at the differences between the arrival time stamps of the _volume clock ticks_ as a measure of the arrival duration. On (b) the same variable is estimated using difference between tick times (or trade time stamps). 

|**Symbol**|**Asset Type**|**Liquid Market Hours**|**Exchange**|**no of Days**|
|---|---|---|---|---|
|BTC 1|Bitcoin|24-hrs|Coinbase2|Monday - Sunday|
|TY1|10-Year T-Note Future|18:30 - 17:30|CBOT 3|Sunday - Friday|
|TU1|2-Year T-Note Future|18:30 - 17:30|CBOT 3|Sunday - Friday|
|DU1|Euro-Schatz 2-year Future|1:10-22:00|Eurex|Monday - Friday|
|RX1|Euro Bund 10-Year Future|1:10-22:00|Eurex|Monday - Friday|
|JB1|Japanese 10-Year Bond Futures|8:45-11:02, 12:30-15:02, 15:30-5:30|Osaka Exchange|Monday-Friday|



> _a_ Bitcoin data derived from Coinbase Pro historical data 

> _b_ The Bitcoin Mercantile Exchange 

> _c_ Chicago Board of Trade 

Describe the data cleanly here particularly around Bitcoin and change the CHF bond data with other data more description above summary statistic table that contains number of observations per period st.dev skewness kurtosis average return average stock price 

## **4 Methodology** 

## **4.1 Multifractal detrended fluctuation analysis (MFDFA)** 

High-frequency time series data, exhibits more accurately accounts for long memory and structural changes due to improved continuity in the distribution function. High frequency time series can display periods of high volatility followed by periods of low volatility. This alternation of volatility will depend on the scale under consideration. Large fluctuations tend to have different scaling behaviour than small fluctuations. This _intermittent behaviour_ leads to the multi-fractal nature of time series [24].We are looking to understand if such multifractality does exist in the data we consider and if the source of such behaviour is long range correlation. 

The structural characteristics of high frequency financial time series can often be visually apparent, but will not necessarily be captured by conventional measures, nor can they be characterised by one scaling exponent. It is clear that the dynamics of multifractality are directly related to the efficiency of markets, and therefore in the existence of artefacts that can be exploited. 

cite references here like Han, Wang and Xu 

. We use a generalisation of the well known _Detrended Fluctuation Analysis (DFA)_ , call _multifractal DFA (MF-DFA)_ [25], [26]. 

**Definition 14.** _Multifractal Detrended Fluctuation Analysis is a method which allows to measure self-affinity properties of time series._ 

One of the advantages of mfDFA is the robustness in the estimation of the Hurst exponent estimation even for non-stationary signals. [27] 

The purpose of this study is to study the multi-fractal properties of the data under different information clocks, and explore if the source are indeed certain stylised facts, such as long-range correlation. 

Based on the outcome of the long-range dependence we will examine the property of a fractal distribution (a fat-tail distribution), and examine the property of multi-fractality to detect the fluctuation feature of the micro-price returns at different time scales. 

The methodology we follow is based on [28],and we outline below the following steps: 

## **4.1.1 Algorithm for the construction of MFDFA** 

In this part, we present the various steps of algorithm for constructing MFDFA [29]. 

## **Steps of the algorithm** 

- _Calculate the profile_ 

Once we have the raw time series, we obtain the cumulative sum (by removing the mean values, because this allows long term persistence trends to be measured, this technique is typical for this type of analysis [ **?** ], [ **?** ]. Essentially, we removing the noise element and integrate the original time series. 

Let us assume a sample of a time series of variable _xt_ of length _n_ . The profile is computed in this first step as follows: 


![](markdown_output/Stylised_Facts_Paper_Only_images/Stylised_Facts_Paper_Only.pdf-0009-10.png)


This steps produces the _profile Y_ = _{yi}[k] i_ =0 

- _Divide the profile y_ ( _k_ ) _into segments_ 

The profile series, is then segmented into _ns_ = _int_ ( _n/s_ ) non-overlapping segments of length _s_ . Given the variable _s_ can take values which are not always integer multiples of the length of the profile data, this can lead to a tail amount of data to be discarded. Therefore we perform the procedure twice, starting from the beginning and moving forwards and once in reverse order. Therefore, we obtain 2* _ns_ segments. 

- _Compute the local trend for each of the segments_ 

Detrending is important to quantify the scale invariant structure of variation around the local trends. Hence, we compute the local trend _yi[loc]_ for each segments is computed by least square fit of a polynomial of order _k_ . Now the detrended time series can be obtained as follows: 


![](markdown_output/Stylised_Facts_Paper_Only_images/Stylised_Facts_Paper_Only.pdf-0009-16.png)


- _For each segment, compute the local root-mean variation_ 

The analysis gives us an exponent _H_ , the ”H Value”, a variability and confidence level _R_ that the fluctuation value _F_ ( _s_ ) relates to _s_ (the source line number). These values are summarized in section **??** and the meaning & derivation of the ”H value” are given in section **??** . 

In the next section, we apply the MF-DFA technique on the information clock price returns to study the basic features of its multi fractal behavior. 

## **4.2 Two-sample testing with kernels** 

## **4.2.1 Background for two-sample testing** 

The sampling schemes under the various information clocks, highlight the potential existence of differences between samples of the data and can create a [potential] pervasive problems which one faces in choosing an alternative stochastic clocks for high frequency data or a distributional assumption for modelling the data. Even though the sampling width of the clocks is chosen a-priori for (local) stationarity, the distributions of higher moments or other order-book derived variables of interest will likely vary. Another prevalent point, is that ensuring some sort of compatibility of high frequency market structure data can allow for the merging samples to achieve larger sample sizes. 

However, such topics do have important implications as discussed in [30] and [31], and there may be many instances, where we may wish to aggregate data across multiple trading periods. Also, when a specific model or the assumption of a distribution is required to be compared against the real data,an analytical measure of discrepancy between them is required. These are just some of the problems which can require _two-sample testing_ . The two-sample problem involves the comparison of two samples from two possibly different probability distributions. 

The classical approaches to such testing are based on the Neymanˆa€“Pearson theory of null hypothesis significance testing [ **?** ], [32]. A range of approaches exists which can vary from simple parametric, location alternative tests on univariate data such as the _t-test_ to more general non-parametric, tests. Next, we make a brief foray into statistical hypothesis testing. We describe briefly statistical hypothesis testing and specifically for the two-sample problem. 

From the perspective of statistical hypothesis, we wish to address the following questions: 

- Can we detect whether for different sampling method for each information clock, if the underlying distribution that generates returns changes substantially or not? 

- What implications does the choice of the stochastic clock for the distribution of variables derived from the data under consideration? 

- Do similar implications carry to the intra-day volatility estimation? 

## **4.2.2 Quick formulation of two sample testing** 

More formally, the procedure tests the data under the so-called _null-hypothesis H_ 0, that the two samples originate from the same distribution. The complement of _H_ 0, is known as the _alternative-hypothesis HA_ . For each hypothesis, two different distributions of the test statistic are required. Therefore, to distinguish the hypotheses, a test statistic is computed on sample data. As sample data is very often finite, this will corresponds to sampling the true distribution of the test statistic. To criterion of rejection of _H_ 0, is based on a threshold (for example, as a threshold, the 95% quantile of the null-distribution), and rejected _H_ 0 when the test statistic lies below that threshold, i.e. it is unlikely that the null-distribution has generated the test statistic and the the null-hypothesis _H_ 0 can be rejected. Therefore to solve this type of problem, it is desirable to have a criterion than takes a positive unique value if _p ̸_ = _q_ , and zero if and only if _p_ = _q_ . There are two different kinds of errors in hypothesis testing: 

- A _type I error_ is made when _H_ 0 : _p_ = _q_ is wrongly rejected.[1] 

- A _type II error_ is made when _HA_ : _p ̸_ = _q_ is incorrectly accepted.[2] 

An alternative way is simply to compute the quantile of the test statistic in the null-distribution, the socalled _p-value_ , and to compare the p-value against a desired test power, say _α_ = 0 _._ 05, by hand. In this second method both a binary answer, and also an upper bound on the type I error is generated.[3] 

## **4.2.3 A simple mathematical formulation of the two-sample test problem** 

Next we describe, a simple formulation of the problem: Let us assume that, _x ∼ p_ ( _x_ ) and _q ∼ q_ ( _y_ ), where _xi, yi ∈_ R. The goal is to test _H_ 0 : _p_ ( _x_ ) = _q_ ( _y_ ) against _HA_ : _p_ ( _x_ ) _̸_ = _q_ ( _y_ ).[4] 

In the following section, 4.2.4, we provide a brief overview of the usage of kernels in two sample testing, and specifically the maximum Mean Discrepancy(MMD) based test of Gretton, [33, 34]. 

## **4.2.4 Using kernels for two-sample testing** 

In this section, we provide a brief overview kernel-based statistical tests for this problem, as developed in [35], [ **?** ]. This type of testing is based on the fact, that two distributions are different if and only if there exists at least one function having different expectation on the two distributions. Such a test statistic is shown to be based on the maximum mean discrepancy (MMD), where we use it between the sample means and take advantage of the kernel trick. The next section provides more detail.We can informally (and perhaps 

> 1In this case, the test will indicate that the samples originate from different distributions when they are not. 

> 2In this case, the test will erroneously reject _H_ 0 that both samples have been drawn from the same distribution. 

> 3This means that the chance that the samples were generated under _H_ 0 are 5%. This is known as the _test power_ , _α_ (in this case _α_ = 0 _._ 05). And represents an upper bound on the probability for a type I error. 

> 4An ideal test should have power against all alternatives. That is, as _n, m →∞_ , the test will always reject when _p_ = _q_ for any non-zero significance level _α_ . 

misleading) claim that kernels can be used to specify the similarity between two objects.In our context, this can be misleading, as the actual specification is the similarity between two values of a _function_ evaluated on each object. 

## **4.3 Two-sample testing with the maximum mean discrepancy** 

The so called _maximum mean discrepancy_ (henceforth, MMD), has this property and allows to distinguish any two probability distributions, if used in a _reproducing kernel Hilbert space_ (RKHS). It is the distance of the mean embeddings _µp, µq_ of the distributions _p, q_ in such a RKHS _F_ – this can also be represented as a function of the expectation of kernel. The MMD is an integral probability metric defined for a reproducing kernel Hilbert space (RKHS). Smoothness is enforced by restricting the witness function to a unit ball in a reproducing kernel Hilbert space, [36]. The test statistic is defined by the difference between the mean function values on two different samples, or maximum mean discrepancy MMD, [37]. In simple terms, when this statistic takes large values, the samples are likely from different distributions. Add a witness function example and an explanation. 

As this section utilises kernels, we now give a more precise definition. 

Given samples from distributions p and q, a two-sample test determines whether to reject the null hypothesis that p = q, based on the value of a test statistic measuring the distance between the samples. One choice of test statistic is the maximum mean discrepancy (MMD), which is a distance between embeddings of the probability distributions in a reproducing kernel Hilbert space A two-sample test based on the asymptotic distribution of an unbiased estimate of MMD2 was introduced in [ **?** ] 

## **4.4 Maximum mean discrepancy** 

As mentioned earlier, _maximum mean discrepancy_ (henceforth, MMD) is the statistic that will be used tp quantify the discrepancy of two data distributions in kernel space. The design of the maximum mean discrepancy statistic has been in order to determine a function such that its expectation differs when observations come from two different probability distributions. For more details, we refer to the excellent works in [38], [36], [35]. The premise is that this statistic is computed on samples of different distributions it will measure how likely these distributions are to be different. We now provide a more precise definition: 

## **4.5 Experimental methodology** 

To apply kernel two sample testing, we describe the following steps: 

- First we define a distance metric on the empirical probability distributions of the various quantities, based on the distance of their (Hilbert space) mean embeddings. This metric as described earlier is _maximum mean discrepancy_ (MMD) 

- We compute the empirical estimates of MMD across many samples. 

- Hypothesis testing is performing using as the test statistic the MMD estimates. This will determine whether the two samples originate from the same distribution. 

## **5 Case Studies** 

## **6 Empirical data experiments on micro-price returns** 

In this section, we assess numerical performance of the distance-based and RKHS-based test-statistics on a series of micro-price change returns computed on different clocks. We investigate similarity to the Gaussian distribution under different information clocks, and the independence problem across days. 

In the experiments, we investigate four kinds of information clocks: tick-based, volume-based, and dollarvolume based, alongside the regular chronological clock. 

In the first test, perform Wilkˆa€™s & Kolmogorov tests on the returns of each instrument (under the clocks), which should not be significant to meet the assumption of normality. 

We perform a comparison across sample days (in a sliding window) For each sample we compute, a Gaussian distribution with the same sample mean and variance as our sample. We then compare the synthetic data sample and the empirical one, for each asset. 

For the same asset of empirical returns, but this time we normalise the means for each day to zero, keeping the variance the same. 

Furthermore, we investigate the variability between the samples is the mean of the micro-price log returns for each day and the changes in variance (or volatility). 

Each time series is sampled regularly if under the information clocks, but irregularly if sampled under the chronological clock. 

The test is fitted on one sample set and then tested on another! 

Describe the limitations of normality under the Wilks test 

## **6.1 How do jumps change the distribution of order book variable** 

```
StylisedFactsPaper/figures/Tickbarsclock_GK-KlassHistogram.png
```

Figure 3: The plot of interarrival times. 

## **6.2 Studying the properties of realised variance and auto-correlation under different information clocks** 

## **6.2.1 Does realised variance exhibit bias?** 

## **6.2.2 Does auto-correlation have an impact on realisity volatility?** 

## **6.2.3 Does power-law still hold?** 

## **6.2.4 Statistical properties of realised volatility** 

Power laws are theoretically interesting probability distributions that are also frequently used to describe empirical data. 

In recent years effective statistical methods for fitting power laws have been developed, but appropriate use of these techniques requires significant programming and statistical insight. In this section, we will explore basic statistical analysis and fitting of distributions. 

## **6.3 High frequency cross-correlation and dependency** 

In this section, we study the relation between trading volume, arrival rates of trades and realised volatility. The question we investigate is whether any relation between these micro-structure variables exist and, if it does, which information clock highlights the significance. The availability of ultra-high frequency data and TAQ allows us to examine the lead-lag relationships and any dependencies across data derived as a function of order book micro-structure variables. In this section, we examine the cross-impacts and the relationships between realised volatility, jump measure and some of the [....] of the order book. 

## **6.3.1 Relationship between volume and volatility** 

The relationship between volume and returns is can help explain how market information is transmitted in asset prices. The empirical examination of both correlation and causality between volume and volatility, can provide insights about their interaction, particularly when both variables are at elevated levels. 

The topic has been a subject of considerably study, mostly in single-instrument or asset setups. It is also easy to see how the understanding of this relationship can contribute in designing algorithmic trading strategies. The recent work of [39], provides insight and they observe that despite weakness in the same-day correlation between the logarithmic volume and volatility is weak, the same day and time-lagged correlation between logarithmic volume and a quantity they refer to as the highest volatility observed in a given range of volume can be strong. However, their work is concentrated in older periods, and only on daily US equity stock data. 

## **6.4 Cross correlation** 

Firstly, we deploy cross-correlation to study the relationship between these variables. It has been widely used in empirical finance to study relationships, however most studies have used data at lower frequencies or sampled only in calendar time. This is the first study that fully utilises the information clock. The usage of regularly sampled data has been problematic in the measurement of cross correlation 

quote Zhang Epps Effect 

. 

talk about Hayashi Yoshida correlation here 

Furthermore, we investigate cross-correlations up to 5 lags for Garman-Klass volatility, volume per trade, realised kurtosis and skewness. 

## **6.4.1 Relationship between arrival rates and jumps** 

Questions arise: do the cross-correlations indicate spurious relationships, because of the existence of autocorrelation? We explore Mixed Data Sampling (henceforth MIDAS) regression models to address such questions, and examine the causality of the relationships. 

## **6.5 MFDFA on price returns** 

Does the long -memory component have the same distribution for different clocks and across time? 

Figure 4: In the first study, we use the high-frequency data of the Bitcoin transactions using the volume clock. The presence of a high degree of cross-correlation between the a-synchronous time evolution of a set of features of the micro-structure is a well known empirical fact. But how much of it is evident? In this example, we examine N (in this case N =3) lags for a set of variables that describe trading activity. For each tick of the clock (row) and for a given feature (column), we shift the value for that feature N ticks of the clock prior. For each value of N (in this case)we take the value of the feature representing the Nth prior tick’s measurement. 

Figure 5: In the first study, we use the high-frequency data of the Bitcoin transactions using the volume clock. The presence of a high degree of cross-correlation between the a-synchronous time evolution of a set of features of the micro-structure is a well known empirical fact. But how much of it is evident? In this example, we examine N (in this case N =3) lags for a set of variables that describe trading activity. For each tick of the clock (row) and for a given feature (column), we shift the value for that feature N ticks of the clock prior. For each value of N (in this case)we take the value of the feature representing the Nth prior tick’s measurement. 

Figure 6: The dendrogram is a visual representation of the order book correlation data, sampled under a volume clock. As can be seen above, clusters of variables are formed by joining individual features or existing clusters with the join point referred to as a node. First, we convert a full vector-form correlation matrix to a squareform distance matrix. Then, we perform agglomerate clustering on the asynchronous square-form correlation matrix, where three apparent tendencies are observed. For example, in hierarchical linkage clustering, we can define the distance between clusters as the average distance between all inter-cluster pairs. In this case, the distance between pairs is defined to be the correlation distance. Thus, the distance between clusters is a way of generalizing the distance between pairs. In our dendrogram, the y-axis is the value of this distance metric between clusters. 

Figure 7: In this second dendrogram, we visually represent about the correlation data in some of the lags a big further.3 Similar to the first dendrogram, the y-axis is the value of this distance metric between clusters. The x-axis identifies the variables that were grouped together 


![](markdown_output/Stylised_Facts_Paper_Only_images/Stylised_Facts_Paper_Only.pdf-0017-00.png)


**----- Start of picture text -----**<br>
(a) label 1<br>**----- End of picture text -----**<br>



![](markdown_output/Stylised_Facts_Paper_Only_images/Stylised_Facts_Paper_Only.pdf-0017-01.png)


**----- Start of picture text -----**<br>
(b) label 2<br>**----- End of picture text -----**<br>


Figure 8: (a) Arrival rate profile conditioned for the jump measure versus non jump measure. The later arrival of trades causes more of an informational driven jump in the returns process. Similarly, the joint distribution of arrival rates and volatility is decidedly different (with fatter tails) when conditioned on the presence of jumps. (b) ... 


![](markdown_output/Stylised_Facts_Paper_Only_images/Stylised_Facts_Paper_Only.pdf-0018-00.png)


**----- Start of picture text -----**<br>
StylisedFactsPaper/figures/Tick bars clockrelative_jump_metric.png<br>(a) label 1<br>StylisedFactsPaper/figures/TickBars_Clockarrival_rate_histogram_jump_metric.png<br>(b) label 2<br>**----- End of picture text -----**<br>


Figure 9: (a) Visual representation of jumps under different sampling rates for the tick-bar information clock. (b) We condition the distribution of arrival rates on whether a jump is occurring or not 


![](markdown_output/Stylised_Facts_Paper_Only_images/Stylised_Facts_Paper_Only.pdf-0019-00.png)


**----- Start of picture text -----**<br>
(a) label 1<br>StylisedFactsPaper/figures/figuresvolume_bar_F_n_ntau.png<br>(b) label 2<br>**----- End of picture text -----**<br>


Figure 10: We present an example of log-log plots of the MF-DFA fluctuation function _F_ ( _n_ ) versus _n_ for different values of _q_ . On the left side :(a) volume-based information clock and on the right side (b) tick-based information clock. We fit straight lines to obtain a local Hurst exponent _Ht_ as the slope of the line, which are represented on the right side. 


![](markdown_output/Stylised_Facts_Paper_Only_images/Stylised_Facts_Paper_Only.pdf-0020-00.png)


**----- Start of picture text -----**<br>
(a) Tick<br>StylisedFactsPaper/figures/figuresvolume_bartau_qstau.png<br>(b) Volume<br>**----- End of picture text -----**<br>


Figure 11: Multifractal scaling exponents _τ_ ( _qs_ ) versus _qs_ . As in the previous plot (a) volume-based information clock and on the right side (b) tick-based information clock. The difference here is we compute the median values across the entire date range. 

## **References** 

|[1]|Helyette Geman, Dilip B Madan, and Marc Yor. Asset prices are brownian motion: only in business time.|
|---|---|
||In_Quantitative Analysis In Financial Markets: Collected Papers of the New York University Mathematical_|
||_Finance Seminar (Volume II)_, pages 103–146. World Scientifc, 2001.<br>(page )|
|[2]|T Ane and H Geman. Order fow, transaction clock, and normality of asset returns. _JOURNAL OF_|
||_FINANCE_, 55(5):2259–2284, OCT 2000.<br>(page )|
|[3]|Carlo Marinelli, Svetlozar T Rachev, Richard Roll, and Hermann G¨oppl. Subordinated stock price models:|
||heavy tails and long-range dependence in the high-frequency deutsche bank price record. In _Datamining_|
||_und Computational Finance_, pages 69–94. Springer, 2000.<br>(page )|
|[4]|Ata Tuerkoglu. Normally distributed high-frequency returns: a subordination approach. _QUANTITATIVE_|
||_FINANCE_, 16(3):389–409, MAR 3 2016.<br>(page )|
|[5]|W. Bounliphone, E. Belilovsky, M. B. Blaschko, I. Antonoglou, and A. Gretton. A test of relative similarity|
||for model selection in generative models. In _ICLR_, 2016.<br>(page )|
|[6]|Rafael Velasco-Fuentes and Wing Lon Ng. Nonlinearities in stochastic clocks: trades and volume as|
||subordinators of electronic markets. _QUANTITATIVE FINANCE_, 11(6):863–881, 2011.<br>(page )|
|[7]|Peter Clark. Subordinated stochastic process model with fnite variance for speculative prices. _Econo-_|
||_metrica_, 41(1):135–155, 1973.<br>(page )|
|[8]|Roel C. A. Oomen. High-dimensional covariance forecasting for short intra-day horizons._QUANTITATIVE_|
||_FINANCE_, 10(10):1173–1185, 2010.<br>(page )|
|[9]|Ulrich A M˜A¼ller, Michel M Dacorogna, Richard B Olsen, Olivier V Pictet, Matthias Schwarz, and Claude|
||Morgenegg. Statistical study of foreign exchange rates, empirical evidence of a price change scaling law,|
||and intraday analysis. _Journal of Banking & Finance_, 14(6):1189–1208, 1990.<br>(page )|
|[10]|Benoit B Mandelbrot. The variation of certain speculative prices. In_Fractals and scaling in fnance_, pages|
||371–418. Springer, 1997.<br>(page )|
|[11]|David Easley, Marcos M. Lopez de Prado, and Maureen O’Hara.<br>The Volume Clock: Insights into|
||the High-Frequency Paradigm. _JOURNAL OF PORTFOLIO MANAGEMENT_, 39(1):19–29, FAL 2012.|
||(page )|
|[12]|D. Knuth. Structured programming with go to statements. _ACM Journal Computing Surveys_, 6(4):268,|
||1974.<br>(page )|
|[13]|Maureen O’Hara. High Frequency Trading and Its Impact on Markets”. _Financial Analysts Journal_, 2014.|
||(page )|
|[14]|Salomon Bochner. _Lectures on Fourier integrals_, volume 42. Princeton University Press, 1959.<br>(page )|
|[15]|S Bochner. Partial ordering in the theory of martingales. _Annals of Mathematics_, pages 162–169, 1955.|
||(page )|
|[16]|Ramazan Genccay, Michel Dacorogna, Ulrich A Muller, Olivier Pictet, and Richard Olsen._An introduction_|
||_to high-frequency fnance_. Elsevier, 2001.<br>(page )|
|[17]|Sun Young Kim and Kyung Yoon Kwon. Does economic uncertainty matter in international commodity|
||futures markets? _International Journal of Finance & Economics_, 26(1):849–869, 2021.<br>(page )|
|[18]|Marcos Lopez De Prado. _Advances in fnancial machine learning_. John Wiley & Sons, 2018.<br>(page )|
|[19]|S. Lapinova and A. Saichev.<br>Comparative statistics of Garman-Klass, Parkinson, Roger-Satchell and|
||bridge estimators. _COGENT PHYSICS_, 4, 2017.<br>(page )|
|[20]|Lars Seemann, Joseph L. McCauley, and Gemunu H. Gunaratne. Intraday volatility and scaling in high fre-|
||quency foreign exchange markets. _INTERNATIONAL REVIEW OF FINANCIAL ANALYSIS_, 20(3):121–|
||126, JUN 2011.<br>(page )|



|[21]|Bart Frijns and Dimitris Margaritis. Forecasting daily volatility with intraday data._EUROPEAN JOURNAL_|
|---|---|
||_OF FINANCE_, 14(6):523–540, 2008.<br>(page )|
|[22]|Rama Cont.<br>Empirical properties of asset returns: stylized facts and statistical issues. _Quantitative_|
||_Finance_, 1:223–236, 2001.<br>(page )|
|[23]|Tony S Wirjanto and Dinghai Xu. The Applications of Mixtures of Normal Distributions in Empirical|
||Finance: A Selected Survey. _https://ideas.repec.org/p/wat/wpaper/0904.html_, 2009.<br>(page )|
|[24]|David G. Mcmillan and Alan E. H. Speigh. Long-memory in high-frequency exchange rate volatility under|
||temporal aggregation. _QUANTITATIVE FINANCE_, 8(3):251–261, 2008.<br>(page )|
|[25]|Wei Hou, Guolin Feng, Pengcheng Yan, and Shuping Li. Multifractal analysis of the drought area in|
||seven large regions of China from 1961 to 2012. _METEOROLOGY AND ATMOSPHERIC PHYSICS_,|
||130(4):459–471, AUG 2018.<br>(page )|
|[26]|Darko Stosic, Dusan Stosic, Teresa B. Ludermir, and Tatijana Stosic.<br>Multifractal behavior of price|
||and volume changes in the cryptocurrency market. _PHYSICA A-STATISTICAL MECHANICS AND ITS_|
||_APPLICATIONS_, 520:54–61, APR 15 2019.<br>(page )|
|[27]|JW Kantelhardt, SA Zschiegner, E Koscielny-Bunde, S Havlin, A Bunde, and HE Stanley. Multifractal|
||detrended fuctuation analysis of nonstationary time series. _PHYSICA A-STATISTICAL MECHANICS_|
||_AND ITS APPLICATIONS_, 316(1-4):87–114, DEC 15 2002.<br>(page )|
|[28]|Jan Kantelhardt. Detecting long-range correlations with detrended fuctuation analysis. _Elsevier Physica_|
||_A_, 295:441, 2001.<br>(page )|
|[29]|Espen A. F. Ihlen. Introduction to multifractal detrended fuctuation analysis in Matlab. _FRONTIERS_|
||_IN PHYSIOLOGY_, 3, 2012.<br>(page )|
|[30]|Martin D. Gould, Mason A. Porter, and Sam D. Howison. The Long Memory of Order Flow in the Foreign|
||Exchange Spot Market. _MARKET MICROSTRUCTURE AND LIQUIDITY_, 2(1), JUN 2016.<br>(page )|
|[31]|Christos Axioglou and Spyros Skouras. Markets change every day: Evidence from the memory of trade|
||direction. _Journal of Empirical Finance_, 18(3):423 – 446, 2011.<br>(page )|
|[32]|Wittawat Jitkrittum, Heishiro Kanagawa, Patsorn Sangkloy, James Hays, Bernhard Schoelkopf, and|
||Arthur Gretton. Informative Features for Model Comparison. In Bengio, S and Wallach, H and Larochelle,|
||H and Grauman, K and CesaBianchi, N and Garnett, R, editor,_ADVANCES IN NEURAL INFORMATION_|
||_PROCESSING SYSTEMS 31 (NIPS 2018)_, volume 31 of _Advances in Neural Information Processing_|
||_Systems_, 2018. 32nd Conference on Neural Information Processing Systems (NIPS), Montreal, CANADA,|
||DEC 02-08, 2018.<br>(page )|
|[33]|Arthur Gretton, Karsten M. Borgwardt, Malte J. Rasch, Bernhard Sch˜A¶lkopf, and Alexander Smola. A|
||kernel two-sample test. 13(25):723–773.<br>(page )|
|[34]|Arthur Gretton, Kenji Fukumizu, and Choon Hui Teo. A kernel statistical test of independence. page 8.|
||(page )|
|[35]|Arthur Gretton, Bharath Sriperumbudur, Dino Sejdinovic, Heiko Strathmann, Sivaraman Balakrishnan,|
||Massimiliano Pontil, and Kenji Fukumizu. Optimal kernel choice for large-scale two-sample tests. In|
||_Advances in Neural Information Processing Systems_, 2012.<br>(page )|
|[36]|Arthur Gretton, Kenji Fukumizu, Zaid Harchaoui, and Bharath K. Sriperumbudur. A fast, consistent|
||kernel two-sample test. pages 673—-681, 2012.<br>(page )|
|[37]|Karsten M. Borgwardt, Arthur Gretton, Malte J. Rasch, Hans-Peter Kriegel, Bernhard Schoelkopf, and|
||Alex J. Smola. Integrating structured biological data by Kernel Maximum Mean Discrepancy. _BIOIN-_|
||_FORMATICS_, 22(14):E49–E57, JUL 2006. 14th Conference on Intelligent Systems for Molecular Biology,|
||Fortaleza, BRAZIL, AUG 06-10, 2006.<br>(page )|
|[38]|BK Sriperumbudur, Kenji Fukumizu, Arthur Gretton, Gert R. G. Lanckriet, and Bernhard Sch¨olkopf.|
||Kernel choice and classifability for RKHS embeddings of probability distributions. In_Advances in Neural_|
||_Information Processing Systems_, 2009.<br>(page )|



- [39] Zeyu Zheng, Jun Gui, Zhi Qiao, Yang Fu, H. Eugene Stanley, and Baowen Li. New dynamics between volume and volatility. _Physica A: Statistical Mechanics and its Applications_ , 525:1343 – 1350, 2019. (page ) 

