***Manuscript Click here to view linked References** 

# **THE HIGH FREQUENCY MULTIFRACTAL PROPERTIES OF BITCOIN**[*] 

STAVROS STAVROYIANNIS[a ] VASSILIOS BABALOS[b          ] STELIOS BEKIROS[c ] SALIM LAHMIRI[d           ] GAZI SALAH UDDIN[e ] 

> a, b _Technological Educational Institute of Peloponnese, Greece_ 

> c _European University Institute, Florence, Italy_ 

> d _ESCA School of Management, Casablanca, Morocco_ 

> e _Linköping University, Linköping, Sweden_ 

## **ABSTRACT** 

Following the new advances in encryption and network computing, Bitcoin emerged as a private sector system facilitating peer-to-peer exchange via distributed ledgers based on blockchains, driving a transformational change towards a global economy outside the core financial system.  The main purpose of this paper is to examine the multifractal properties of the Bitcoin price using high frequency data. The methods used are the wavelet transform modulus maxima and the multifractal detrended fluctuation analysis. The results indicate that Bitcoin exhibits a large degree of multifractality in all examined time intervals, and the main source of multifractality is attributed to the high kurtosis and the fat distributional tails of the series returns. 

## _JEL classification_ : G14; G15 

_Keywords_ : Bitcoin; Wavelet transform; Detrended fluctuation analysis; Chaos; Fractality 

> a Department of Accounting and Finance, School of Management and Economics, Technological Educational Institute of Peloponnese, Antikalamos 241 00; Greece; E-mail: stavroyian@teikal.gr 

> c _Corresponding author_ : Department of Economics, Villa La Fonte, Via delle Fontanelle, 18, I-50014, Florence, Italy; Tel.: +39 055 4685 925; Fax: +39 055 4685 902; E-mail address: stelios.bekiros@eui.eu 

> b Department of Accounting and Finance, School of Management and Economics, Technological Education Institute of Peloponnese, Antikalamos 241 00, Greece; E-mail address: vbabalos@gmail.com 

> d ESCA School of Management, 7, Abou Youssef El Kindy Street, BD Moulay Youssef, Casablanca, Morocco; E-mail address: slahmiri@esca.ma 

> e Linköping University, Department of Management and Engineering, SE-581 83 Linköping, Sweden; Tel.: +46769802570; Fax: +46-013281101; E-mail address: gazi.salah.uddin@liu.se 

1 

## **1. INTRODUCTION** 

The fractal and multifractal nature of physical phenomena and empirical data has been the subject of substantial interest due to the wide range of properties associated with the scale invariance, an aspect appearing in many scientific fields. In the same vein, the variety of financial instruments together with the complexity of financial markets posed greater challenges to academics, researchers and investors. This led Peters (1994) to coin the term Fractal Market Hypothesis (FMH) as an alternative to the Efficient Market Hypothesis (EMH), focusing on the scaling properties of the distribution of returns rather than informational efficiency, and as a consequence standard asset pricing and risk management models may need to be reassessed (Onali and Goddard, 2009). Multifractality has been examined in a variety of financial time series including stock markets (Pasquini and Serva, 1999; Bouchaud et al.  2000; Andreadis and Serletis, 2002; Matia, et al.,  2003; Di Matteo et al. 2003; Oświęcimka et al., 2005; Moyano et al., 2006; Cajueiro et al., 2009; Stavroyiannis et al., 2010; Lahmiri and Bekiros, 2017; Maganini et al., 2018; ; Uddin et al. 2018), foreign exchange markets (Vandewalle, and Ausloos, 1998; Bershadskii, 2003; Norouzzadeh and Rahmani, 2006; Stavroyiannis et al., 2011), commodities (Lahmiri et al., 2017), interest rates (Cajueiro and Tabak, 2007), emerging markets (Liu et al.,  2010; Benbachir and El Alaoui, 2011; El Alaoui and Benbachir, 2013; El Alaoui and Benbachir, 2013; Samadder et al., 2013; Lahmiri S. 2017), and air pollution (Manimaran and Narayana, 2018). The degree of multifractality has been recently associated to the inefficiency of a market (Zunino et al., (2008), since small or emerging markets indicate richer multifractality than the developed ones, and Stavroyiannis et al. (2011) using high frequency data for the Euro/JPY exchange rate, introduced the local multifractality sensitivity index as an attempt to a pre-crisis signal. 

Virtual currencies existed for several years in the online gaming communities including Bitcoin (Nakamoto, 2008) (BTC, or XBT according to the ISO 4217 standard) in 

2 

MtGox (Magic the gathering online exchange). The Global Financial Crisis and the appearance of the “Internet of things”, via the inter-networking of physical devices and smart devices, has led to a rapid evolution of Bitcoin which last year started to interest a broad range of investors. There are very few works regarding the fractal and multifractal properties of the BTC including detrended fluctuation analysis (DFA) (Bariviera et al., 2017) and the rescaled Hurst exponent (R/S) (Urquhart, 2016), showing strong anti-persistence in the BTC returns. Gajardo et al. (2018) examined the asymmetric cross-correlations with crude oil, gold, and the Dow Jones Industrial Average (DJIA), and Begušić et al., (2018) examined the scaling properties of extreme price fluctuations in Bitcoin markets. Recently, Lahmiri and Bekiros (2018) examined the multifractal properties of the daily returns of BTC, splitting the sample into two periods, the low and high price regimes. They found strong evidence of multifractality in prices and returns throughout both investigated periods, and the high-price level regime period has strongly revealed nonlinear dynamic patterns. 

In this work we examine the multifractal properties of high frequency 1-minute data for the BTC, aggregated up to a 180-minute time interval. The multifractal properties are examined via the wavelet transform modulus maxima (WTMM) and the multifractal detrended fluctuation analysis (MFDFA) methods, although more gravity will be given to the second method. The results indicate the presence of multifractality with the multifractal spectra saturating at larger moment values that the daily data reported in the literature, and in agreement with Urquhart (2016), Bariviera et al.  (2017) and Lahmiri and Bekiros (2018) antipersistency is identified for all time intervals under consideration. The origin of multifractality is examined via shuffled and the amplitude adjusted Fourier transform surrogate data, and in all cases the effect of the fat tails is more pronounced than that of temporal correlations. 

The remainder of this paper is organized as follows. Section 2 presents the methodological approaches used. Section 3 provides a preliminary analysis of the data, while 

3 

Section 4 reveals the multifractal properties of the series. Section 5 conducts further empirical analysis and presents the origins of the chaotic structure. Finally, section 6 concludes. 

## **2. METHODOLOGY** 

The general formulation of multifractal time series is associated with the structure function approach and the singularity spectra, used for the multifractal characterization of normalized and stationary measures (Barabási and Vicsek, 1991; Bacry et al. 2001). Multifractality is introduced via the partition function (Feder, 1988; Peitgen et al., 2004) 

where is a real parameter, and is the Rényi scaling exponent. If the Rényi scaling exponent varies linearly with then the series is monofractal, or self-affine, otherwise it is called multifractal. The generalized multifractal dimensions are related to the scaling exponents via , in such a way that the fractal dimension of the support is and the correlation dimension is . When it comes to time series analysis a discrete version has to be used, since the data might include negative values, by splitting the initial interval into intervals, and setting, 

the partition function is defined as, 

However, this kind of formalism does not give correct results for non-stationary time series that are affected by trends or that cannot be normalized. There are two approaches towards the 

4 

calculation of the fluctuations either using the wavelet transform modulus maxima, or generalizing the detrended fluctuation analysis (DFA) to MFDFA. 

## _2.1. Wavelet transform modulus maxima (WTMM)_ 

The WTMM approach is useful in investigating the scaling properties in the presence of nonstationarities. In the WTMM method (Muzy et al., 1991; Muzy et al., 1994; Arneodo et al., 1995; Arneodo et al.,1998) the partition function is defined as the sum of the q-th powers of the local maxima of the modulus of the wavelet transform coefficients at scale . That is, instead of averaging over all wavelet coefficients one investigates only the local maxima of using the modulo-maxima method. For a given scale the position of the local maxima are determined, and summing up the power of the absolute wavelet coefficients, the partition function is calculated, 

and the scaling exponents are computed as the slope of the dyadic logarithm of the Gibb's power partition function, 

After that, there is not explicit local information present in the resulting scaling estimates, because this procedure is based on Gibb's statistical averaging or partition function . The usefulness of the partition function method resides in the fact that it obtains information on global averages, which tend to be more stable than local information. Its disadvantage is that it tends to obscure the local information. It is in fact the scaling exponents that measures the asymptotic decay of the partition function , and the concavity of the scaling function gives evidence of multifractality and the existence of more than one singularity exponent. 

5 

## _2.2. Multifractal detrended fluctuation analysis method (MFDFA)_ 

The MFDFA is an extension to the detrended fluctuation analysis (DFA) (Peng et al., 1994; Bunde et al., 2000) estimating the Hurst exponent of time series for different scales, considering the -th order partition function of the time series (Silva and Moreira, 1997; Kantelhardt et al., 2002). The Hurst exponent as a function of the moment order is computed via the following algorithm (Kantelhardt et al., 2002): 

## (i) Determine the profile, 

where, without loss of generality, the subtraction of the mean is not mandatory since it can be shown that it is eliminated at the third step via detrending. Higher order polynomials can be used in the fitting procedure and a comparison of the results for different orders of DFA allows one to estimate the type of the polynomial trend in the time series (Hu et al., 2001). 

(ii) Divide the profile into non-overlapping segments of equal length Taking into account that the length of the series does not have to be necessarily a multiple of the divisor , a small part of the profile might remain out of the calculations. In order to include this part into the calculations the same procedure is repeated starting from the opposite end thereby obtaining segments. 

(iii) For each of the segments the local trend is calculated by a least square fit of the series and the variance is determined, 

for each segment and reversing the series, 

6 

for each segment . In Eqs. (7, 8) is the fitting polynomial for the segment , and linear, quadratic, cubic, or higher order polynomials can be used in the fitting procedure (Kantelhardt et al., 2002). 

(iv) Averaging all segments, the -th order fluctuation function is obtained, 

and for , 

(v) Determine the scaling behavior of the fluctuation functions by analyzing log-log plots where is the generalized Hurst exponent for the scale . 

Along with the multifractal spectrum can be described by the mass function given 

by , and the singularity spectrum via application of a Legendre transform where . 

## **3. PRELIMINARY ANALYSIS** 

## _3.1. Time series transformations_ 

High-frequency 1-minute BTC close price data in US dollars are sourced from http://www.coindesk.com/price/. and in case of any missing minutes the previous minute close price is considered. The time span is from 01-Apr-2017 0:00 to 30-Nov-2017 23:59 comprising of 351360 entries that is 1440 per day. BTC trades 24/7 therefore there is no need to exclude the first return of each day in order to avoid outliers, structural breaks, or the arrival of new information. The time intervals used are 1-min, 5-min, 10-min, 15-min, 30-min, 60- 

7 

min, 120-min, and 180-min, since for a proper specification of the multifractal properties a signal with sufficient data is needed. 

According to Mantegna and Stanley (2000) there are four most common choices to transform and analyze the time evolution of the returns of the closing price of an asset : 

(i) Price changes with the problem that this definition is seriously affected by changes in scale, (ii) Deflated or discounted price changes 

, where can be a deflation factor, or a discounting factor, with the problem that such factors are unpredictable over the long term, and there is no unique choice for , (iii) Returns defined as a direct percentage , with the problem that the returns are sensitive to scale changes for long time horizons, and (iv) Successive differences of the natural logarithm of price . The last approach incorporates average corrections of scale changes without requiring deflators or discounting factors, but now a non-linear transformation is used. In this work returns are realized as . Fig. 1 shows BTC close price (top) the logarithm of the close price (middle) and the log-returns (bottom). 

8 

**Fig. 1.** BTC close price (top), the logarithm of the close price (middle), and the returns (bottom). 

## _3.2. Unit root tests_ 

Table 1, shows the unit root tests for the series and the returns (where * denotes statistical significance at the 5% confidence level). We report the Elliott-Rothenberg-Stock (ERS), the Phillips-Perron (PP), and the Kwiatkowski–Phillips–Schmidt–Shin (KPSS) test statistics respectively. The null hypothesis for the ERS and PP is that the series possess a unit root, while for the KPSS the null hypothesis is that the series is stationary. The statistical properties of financial time series vary with time and they also depend on different time windows. Unit root tests will indicate whether we will work with the original series, in case of stationarity, or with the returns, in case the original series are not stationary (Cajueiro and Tabak, 2007, Wang et al., 2011). The results indicate the presence of a unit root for the series and stationarity for the returns. 

9 

**Table 1** Unit root test for the series (Panel A) and the returns (Panel B) 

||1 min|5 min|10 min|15min|30 min|60 min|120 min|180 min|
|---|---|---|---|---|---|---|---|---|
|**Series**|||||||||
|ERS|21.766|26.452|26.125|32.765|36.521|31.946|19.283|20.156|
|PP|-0.5955|-0.2595|-0.1373|-0.0484|-0.1750|-0.3766|-0.4601|-0.8846|
|KPSS|9.6733*|4.1707*|2.9892*|2.4137*|1.7010*|1.2318*|0.8711*|0.7281*|
|**returns**|||||||||
|ERS|0.0021*|0.0003*|0.0022*|0.0897*|0.2942*|5.6E-05*|0.6688*|0.3466*|
|PP|-543.55*|-257.84*|-192.47*|-152.27*|-108.16*|-81.193*|-58.068*|-43.808*|
|KPSS|0.0754*|0.0899|0.0962|0.1010|0.0933|0.0876|0.0874|0.0667|



## _3.3. Descriptive statistics and stylized facts_ 

Table 2 shows the descriptive statistics and stylized facts for the returns (where * denotes 

statistical significance at the 5% critical level). 

**Table 2** Descriptive statistics and stylized facts. 

||1 min|5 min|10 min|15min|30 min|60 min|120 min|180 min|
|---|---|---|---|---|---|---|---|---|
|Mean|0.0006|0.0032|0.0063|0.0095|0.0191|0.0377|0.0749|0.1110|
|Std|0.1189|0.2772|0.3982|0.4883|0.7044|0.9857|1.3668|1.6675|
|Skew.|-0.4800*|-0.3721*|-0.4011*|-0.4977*|-0.3720*|-0.3391*|-0.4024*|0.0206|
|Kurt.|266.36*|45.805*|28.751*|26.265*|19.702*|12.620*|11.262*|14.373*|
|J.B.|1.e+09*|5.e+06*|9.e+05*|5.e+05*|1.e+05*|22691.*|8404.2*|10515.*|
|ARCH(12)|5102.3*|1139.4*|530.47*|353.33*|80.559*|50.433*|42.682*|11.798*|
|L.B.(12)|2686.0*|164.07*|65.888*|67.917*|74.089*|35.498*|31.408*|35.672*|
|L.B.-2(12)|43795.*|17990.*|10930.*|6169.3*|1907.6*|1173.8*|879.91*|216.39*|



The results of the data aggregation is an increase of the mean and the standard deviation, while the kurtosis and the statistics of the Jarque-Bera test, indicating deviation from normality, are reduced. All series possess heteroskedasticity shown by the ARCH test statistics, and all series exhibit serial correlation as shown by the Lung-Box (L.B.) for the 

returns, and the Lung-Box test statistics for the squared returns (L.B.-2), for 12 lags. 

10 

**4. MULTIFRACTAL PROPERTIES OF THE TIME SERIES** 

## _4.1. Wavelet transform modulus maxima (WTMM)_ 

WTMM is very advantageous approach for local scaling exponent estimation that allows building the local scaling exponent function for both positive and negative values. Fig. 

- 2 shows typical structural spectra for the 180-min sampling where a Morlet wavelet with 16 voices per octave, for determination of the scales has been used. 

**Fig. 2.** BTC image of the wavelet transform (top left), the skeleton structure (top right), the thermodynamic partition function (bottom left), and the moment generating function (bottom right). 

Fig. 2 (top, left) show the visualization of the wavelet transform and Fig. 2 (top, right) shows the wavelet skeleton. The wavelet skeleton aggregates all local maxima lines on each scale of the wavelet coefficient matrix. The idea behind the skeleton matrix construction is to remove all absolute wavelet coefficients that are not maximal, keeping this way all the coefficients that belong to local maxima lines. In general the skeleton function is a logical function obtaining only two values, one if the skeleton matrix elements is a maximum and zero otherwise. The scope of all these local maxima lines builds the skeleton function which shows 

11 

the periodicity of the BTC signal on decent scales, and the scalability of the signal. The whole idea of the skeleton matrix is to simplify the multifractal analysis of the whole wavelet coefficients matrix to only those coefficients that belong on the skeleton. Summing up, the WTMM formulation is used to obtain the skeleton function which provides a partition, in order to merge the WTMM method with the thermodynamic formalism in such a way so that the singularity spectrum for the BTC can be determined. 

Fig. 2 (bottom, left) shows the thermodynamics partition function for the BTC as a function of the logarithm of the scale. The thermodynamics partition function is finite only if the WTMM coefficients are not equal to zero, since all zero coefficients in the WTMM matrix have been disregarded. It is shown that BTC exhibits wavelet modulus maxima coefficients of different values and signs; the presence of relative small wavelet modulus maxima coefficients is detectable with the large values of for negative values, and the presence of larger wavelet modulus maxima coefficients for positive values. 

Finally, Fig. 2 (bottom, right) shows the moment generating function for the BTC. The multifractal behavior of financial time series assumes that an index does not have a unique fractal measure but scale with different scaling rules. In case of monofractal behavior the generating function is a line, and the concavity in the case of BTC confirms the multifractality of the BTC series. Under the same arguments Fig. 3 shows that the generating function is concave for all aggregated series under examination, an indication that multifractality is present for all BTC series. 

12 

**Fig. 3.** Moment generating function as a function of for 1-min (solid circle), 5-min (solid square), 10-min (up-triangle), 15-min (down-triangle), 30-min (rhombus), 60-min (left-triangle), 120min (right triangle), and 180-min (open circle) BTC series. 

## _4.2. Multifractal detrended fluctuation analysis (MFDFA)_ 

The accuracy of scaling exponents determined by DFA as a function of the length of the data has been studied for a fitting range from 10 to (Bashan et al., 2008), and following Kantelhardt (2009) an interval segmentation via subdivision from to 16 is used for all series under consideration. Typical log 2 _Fq_ ( _s_ ) - log2 _s_ plots (open circles) and linear fits (solid 

lines) for are shown in Fig. 4 for the 30-min returns. The top data and solid line fit represents the moment value and the lowest data and solid line fit represents the moment value. If the series are long-range power-law correlated, then increases 

as a power-law for large values of , where is the generalized Hurst exponent. 

13 

**Fig. 4.** Typical log-log plots (open circles) and linear fits of versus for the 30-min returns. 

Fig. 5 shows the generalized Hurst exponents for all BTC series. If the series are monofractal with compact support, is independent of since the scaling behavior of the variance is identical for all segments , and the averaging procedure will give an identical scaling behavior for all values of . On the other hand, if small and large fluctuations scale in a different way then there will be a significant dependence of on . 

14 

**Fig. 5.** Generalized Hurst exponents as a function of for 1-min (solid circle), 5-min (solid square), 10-min (up-triangle), 15-min (down-triangle), 30-min (rhombus), 60-min (left-triangle), 120min (right triangle), and 180-min (open circle) returns. 

Considering positive values of the segments with large variance will dominate the average and describes the scaling behavior of the segments with large fluctuations. On the contrary, for negative values of the segments with small variance will dominate the average and describes the scaling behavior of the segments with small fluctuations. The estimated parameters from the generalized Hurst exponent spectra are shown in Table 3 that is, the Hurst exponent , the inefficiency degree quantified by the multifractality range , the range of the large fluctuations, and the range of the small fluctuations. Higher variability of corresponds to richer multifractality and since large fluctuations are characterized by smaller scaling exponents than small fluctuations, the values are larger than the 

15 

values, therefore is positively defined. The values of the Hurst exponents indicate antipersistency, and in all cases are larger than , an evidence that the spectra are rightly-skewed. 

**Table 3** Estimated parameters from the generalized Hurst exponent spectra . 

|1 min|5 min|10 min|15min|30 min|60 min|120 min|180 min|
|---|---|---|---|---|---|---|---|
|<br>0.4882|0.489|0.4943|0.4919|0.4925|0.4885|0.471|0.4999|
|<br>0.6019|0.6584|0.7004|0.6791|0.6746|0.6488|0.6757|0.7358|
|<br>0.2932|0.3189|0.3496|0.3202|0.3154|0.3045|0.3283|0.3643|
|<br>0.3087|0.3395|0.3508|0.3589|0.3592|0.3443|0.3474|0.3715|



Fig. 6 shows the singularity spectra as a function of for the series under consideration calculated via application of the Legendre transform where . Singularity spectra are bell-shaped functions and can be approximated by a fourth-degree polynomial (Theiler et al., 1992; Puckovs and Matvejevs, 2012), 

and the coefficients of the fits are shown in Table 4 for all series returns. 

16 

**Fig. 6.** Singularity spectra as a function of for 1-min (solid circle), 5-min (solid square), 10-min (up-triangle), 15-min (down-triangle), 30-min (rhombus), 60-min (left-triangle), 120-min (right triangle), and 180-min (open circle) returns. 

**Table 4** Coefficients of the singularity spectra fits via a fourth-degree polynomial. 

|1 min|-58.4264|123.442|-100.640|37.8661|-4.6050|
|---|---|---|---|---|---|
|5 min|-31.4307|67.0133|-57.8561|23.9291|-2.9564|
|10 min|-13.9696|31.5739|-32.3721|16.3570|-2.1916|
|15 min|-21.4897|43.9583|-38.6036|17.1541|-2.1217|
|30 min|-24.0736|50.4528|-44.3196|19.2480|-2.3890|
|60 min|-32.5640|67.9800|-57.5241|23.5240|-2.8875|
|120 min|-33.6818|72.6608|-61.7908|24.6243|-2.8794|
|180 min|-32.3287|59.0680|-45.4237|18.2696|-2.1815|



## **5. ORIGINS OF MULTIFRACTALITY** 

Two different types of multifractality can be distinguished in time series: (i) multifractality attributed to the fat-tails of the pdf where multifractality cannot be removed via shuffling, and (ii) multifractality due to different correlations in small and large-scale fluctuations, where the shuffled time series will exhibit monofractal scaling, since all long-range correlations are 

17 

destroyed by the shuffling procedure. If both kinds of multifractality appear, the shuffled 

series will show weaker multifractality than the original series. On the other hand, to 

determine multifractality due to the broadness of the pdf the use of the amplitude adjusted 

Fourier transform (AAFT) surrogate approach, retains the temporal correlations but the 

probability function changes to a Gaussian distribution via phase randomization (Theiler et al., 1992). 

**Fig. 7.** Generalized Hurst exponents as a function of for the original returns (solid circle, black), the shuffled surrogate (solid square, red), and the AAFT surrogate (solid up-triangle, blue). 

Fig. 7 shows the generalized Hurst exponents for the original series returns, the shuffled surrogates, and the AAFT surrogates, and Table 5 compares the estimated parameters from the generalized Hurst exponent spectra for the shuffled and the AAFT surrogate return series. The shuffled surrogates have higher values of multifractality range than the AAFT, indicating that 

18 

multifractality is mostly attributed to the fat-tails of the distribution of the series returns. The values of the Hurst exponents indicate anti-persistency up to 15-min time interval, and are larger than indicating that small fluctuations dominate the shuffled surrogates. 

**Table 5** Estimated parameters from the generalized Hurst exponent spectra for the shuffled surrogate and the AAFT surrogate. 

|1 min|5 min|10 min|15min|30 min|60 min|120 min|180 min|
|---|---|---|---|---|---|---|---|
|**Shuffle surrogates**||||||||
|<br>0.4875|0.4976|0.4774|0.4639|0.5100|0.5016|0.4848|0.4825|
|<br>0.4692|0.4464|0.3607|0.3943|0.3837|0.3386|0.2871|0.3177|
|<br>0.1423|0.1624|0.1190|0.1681|0.1330|0.1413|0.1243|0.1737|
|<br>0.3269|0.2840|0.2417|0.2262|0.2507|0.1973|0.1628|0.1440|
|**AAFT surrogates**||||||||
|<br>0.4938|0.493|0.4866|0.4813|0.4901|0.5114|0.5116|0.5109|
|<br>0.1544|0.1626|0.2073|0.1746|0.1636|0.1798|0.2174|0.2572|
|<br>0.0634|0.1014|0.0919|0.0645|0.0861|0.0782|0.0994|0.1213|
|<br>0.0910|0.0612|0.1154|0.1101|0.0775|0.1016|0.1180|0.1359|



## **6. CONCLUSIONS** 

We have examined the high-frequency multifractal properties of the Bitcoin for a variety of time intervals. Both methods used, the wavelet transform modulus maxima and the multifractal detrended fluctuation analysis reveal significant multifractality for all series returns under consideration. Anti-persistency is the main characteristic of the Hurst exponent value, which might be attributed to the fact that Bitcoin is not yet an efficient market, and the absence of regulation results in large price changes and high volatility. In both original and shuffled series returns the generalized Hurst exponent spectra are characterized by antipersistency and small fluctuation domination. 

19 

## **REFERENCES** 

Andreadis I, Serletis A.2002. Evidence of a random multifractal turbulent structure in the Dow Jones industrial average. _Chaos Solitons and Fractals_ , 13, 1309–1315. 

Arneodo A, Bacry E, Graves PV, Muzy JF. 1995. Characterizing long-range correlations in DNA sequences from wavelet analysis. _Physical Review Letters_ , 74, 3293-3296. 

Arneodo A, Manneville S, Muzy JF. 1998.Towards log-normal statistics in high Reynolds number turbulence. _European Physics Journal B_ , 1, 129-140. 

Bacry E, Delour J, Muzy JF. 2001. Multifractal random walk. _Physical Review E_ , 64, 026103. Barabási AL, Vicsek T. 1991. Multifractality of self-affine fractals. _Physical Review A_ , 44, 2730-2733. 

Bariviera AF, Basgall MJ, Hasperué W, Naiouf M. 2017. Some stylized facts of the Bitcoin market. _Physica A_ , 484, 82–90. 

Bashan A, Bartsch R, Kantelhardt JW, Havlin S. 2008. Comparison of detrending methods for fluctuation analysis. _Physica A_ , 387, 5080-5090. 

Begušić S, Kostanjčar Z, Stanley HE, Podobnik B. 2018. Scaling properties of extreme price fluctuations in Bitcoin markets. _Physica A_ , 510, 400-406. 

Benbachir S, El Alaoui M. A. 2011. Multifractal Detrended Fluctuation Analysis of the Moroccan Stock Exchange. _International Research Journal of Finance and Economics_ , 78, 6- 17. 

Bershadskii A. 2003. Self-averaging phenomenon and multiscaling in Hong Kong stock market. _Physica A_ , 317, 591–596. 

Bouchaud J-P, Potters M, Meyer M. 2000. Apparent multifractality in financial time series. _European Physics Journal B_ , 13, 595–599. 

20 

Bunde A, Havlin S, Kantelhardt JW, Penzel T, Peter JH, Voigt K. 2000. Correlated and uncorrelated regions in heart-rate fluctuations during sleep. _Physical Review Letters_ , 85, 37363739. 

Cajueiro DO, Tabak BM. 2007. Long-range dependence and multifractality in the term structure of LIBOR interest rates. _Physica A_ , 373, 603–614. 

Cajueiro DO, Gogas P, Tabak BM. 2009. Does financial market liberalization increase the degree of market efficiency? The case of the Athens stock exchange. _International Review of Financial Analysis_ , 18, 50–57. 

Castro e Silva A, Moreira JG. 1997. Roughness exponents to calculate multi-affine fractal exponents. _Physica A,_ 235, 327–33. 

Di Matteo T, Aste T, Dacorogna MM. 2003. Scaling behaviors in differently developed markets. _Physica A_ , 324, 183–188. 

El Alaoui M, Benbachir S. 2013. Comparing multifractality among Czech, Hungarian and Russian stock exchanges. _International Journal of Applied Decision Sciences_ , 6, 313–323 

El Alaoui M, Benbachir S. 2013. Multifractal detrended cross-correlation analysis in the MENA area, _Physica A_ , 392, 5985-5993. 

Gajardo G, Kristjanpoller WD, Minutolo M. (2018). Does Bitcoin exhibit the same asymmetric multifractal cross-correlations with crude oil, gold and DJIA as the Euro, Great British Pound and Yen?. _Chaos, Solitons & Fractals_ , 109, 195-205. 

Hu K, Ivanov PC, Chen Z, Carpena P, Stanley HE. 2001. Effect of trends on detrended fluctuation analysis. _Physical Review E_ , 64, 011114. 

Kantelhardt JW, Zschiegner SA, Bunde A, Havlin S, Koscielny-Bunde E, Stanley HE. 2002. Multifractal detrended fluctuation analysis of non-stationary time series. _Physica A_ , 316, 87114. 

21 

Kantelhardt JW. 2009. _Fractal and Multifractal Time Series_ . In: Meyers RA, editor. Mathematics of Complexity and Dynamical Systems, Springer, New York, p.463-487. 

Lahmiri S. 2017. On fractality and chaos in Moroccan family business stock returns and volatility. _Physica A_ , 473, 29–39. 

Lahmiri S, Uddin GS, Bekiros S. 2017. Nonlinear dynamics of equity, currency and commodity markets in the aftermath of the global financial crisis. _Chaos, Solitons and Fractals_ , 103, 342–346. 

Lahmiri S, Bekiros S. 2017. Disturbances and complexity in volatility time series. _Chaos Solitons and Fractals_ , 105, 38–42. 

Lahmiri S, Bekiros 2018. S. Chaos, randomness and multi-fractality in Bitcoin market. _Chaos Solitons and Fractals_ , 106, 28–34. 

Liu L, Wang Y, Wan J. 2010. Analysis of efficiency for Shenzhen stock market: Evidence from the source of multifractality. _International Review of Financial Analysis_ , 19, 237-241. 

Mantegna RN, Stanley HE. 2000. An _Introduction to Econophysics: Correlations and Complexity in Finance_ . Cambridge University Press. 

Maganini, ND, Da Silva Filho, AC, Lima, FG. 2018. Investigation of multifractality in the Brazilian stock market. _Physica A_ , 497, 258-271. 

Manimaran, P, Narayana, AC. (2018). Multifractal detrended cross-correlation analysis on air pollutants of University of Hyderabad Campus, India. _Physica A_ , 502, Pages 228-235. 

Matia, K, Ashkenazy Y, Stanley HE. 2003. Mulifractal properties of price fluctuations of stocks and commodities. _Europhysics Letters_ , 61, 422–428. 

Moyano LG, de Souza J, Duarte Queirós SM. 2006. Multi-fractal structure of traded volume in financial markets. _Physica A_ , 371, 118–121. 

Muzy JF, Bacry E, Arneodo A. 1991. Wavelets and multifractal formalism for singular signals: Application to turbulence data. _Physical Review Letters_ , 67, 3515-3518. 

22 

Muzy JF, Bacry E, Arneodo A. 1994. The multifractal formalism revisited with wavelets. _International Journal of Bifurcation and Chaos_ , 4, 245-302. 

Nakamoto S. 2008. Bitcoin: a peer-to-peer electronic cash system. https://bitcoin.org/bitcoin.pdf 2008. 

Norouzzadeh P, Rahmani B. 2006. A multifractal detrended fluctuation description of Iranian rial–US dollar exchange rate. _Physica A_ , 367, 328–336. 

Onali E, Goddard J. 2009. Unifractality and multifractality in the Italian stock market. _International Review of Financial Analysis_ , 18, 154–163 

Oświęcimka P, Kwapień J, Drożdż S.2005.  Multifractality in the stock market: price increments versus waiting times. _Physica A_ , 347, 626–638. 

Pasquini M, Serva M. 1999. Multiscale behaviour of volatility autocorrelations in a financial market. _Economics Letters_ , 65, 275–279. 

Peng CK, Buldyrev SV, Havlin S, Simons M, Stanley HE, Goldberger AL. 1994. Mosaic organization of DNA nucleotides. _Physical Review E_ , 49, 1685-1689. 

Peters EE. 1994. Fractal Markets analysis: Applying chaos theory to investments and economics. New York: John Wiley and Sons. 

Puckovs A, Matvejevs A. 2012. Wavelet Transform Modulus Maxima Approach for World Stock Index Multifractal Analysis, _Information Technology and Management Science_ , 15, 7686 

Samadder S, Ghosh K, Basu T. 2013.Fractal analysis of prime Indian stock market indices, _Fractals_ , 21, 1350003. 

Shimizu Y, Thunder S, Ehrenberger K. 2002.Multifractal spectra as a measure of complexity in human posture. _Fractals_ , 10, 103-116. 

23 

Stavroyiannis S, Makris I, Nikolaidis V. 2010. Non-extensive properties, multifractality, and inefficiency degree of the Athens Stock Exchange General Index. _International Review of Financial Analysis_ , 19, 19-24. 

Stavroyiannis S, Nikolaidis V, Makris IA. 2011. On the multifractal properties and the local multifractality sensitivity index of euro to Japanese yen foreign currency exchange rates. _Global Business and Economics Review_ , 13, 93-103 

Theiler J, Eubank S, Longtin A, Galdrikian B, Doyne Farmer J. 1992. Testing for nonlinearity in time series: the method of surrogate data. _Physica D_ , 58, 77–94. 

Uddin, GS, Hernandez, JA, Shahzad, SJH, Yoon, SM. 2018. Time-varying evidence of efficiency, decoupling, and diversification of conventional and Islamic stocks. _International Review of Financial Analysis_ , 56, 167-180. 

Urquhart A. 2016. The inefficiency of Bitcoin. _Economics Letters_ , 148, 80–82. 

Vandewalle N, Ausloos M. 1998. Multi-affine analysis of typical currency exchange rates. _European Physics Journal B_ , 4, 257–261. 

Wang Y, Wei Y, Wu C. 2011. Analysis of the efficiency and multifractality of gold markets based on multifractal detrended fluctuation analysis. _Physica A_ , 390, 817–827. 

Zunino L, Figliola A, Tabak BM, Pérez DG, Garavaglia M, Rosso OA. 2008. Multifractal structure in Latin-American market indices. _Chaos, Solitons & Fractals_ , 41, 2331-2340. 

24 

