Order ‡ow, transaction clock and normality of asset returns: a comment on Ané and Geman (2000) 

## Anthony Murphy 

Hertford College, Oxford OX1 3BW, UK (anthony.murphy@nu¤.ox.ac.uk) 

## Marwan Izzeldin 

Department of Economics, Lancaster University, Lancaster LA1 4YX, UK. (m.izzeldin@lancaster.ac.uk) 

This version December 2006 

## Abstract 

We investigate the procedure used by Ané and Geman (2000) to recover the moments of information ‡ow from high frequency data in a model which generalizes the subordinated or mixture of distributions process in Clark (1973). Using Monte Carlo experiments we show that the third and higher moments of the latent information ‡ow cannot be accurately recovered using this procedure. We explain why this happens. We also show that, contrary to the claims in AG, returns conditioned on the recentered number of trades are not approximately Gaussian. KEY WORDS: Information ‡ow; returns; normality; subordinated process. 

1 

## 1. INTRODUCTION 

Since the highly in‡uential work of Clark (1973), researchers have devoted a great deal of time and e¤ort to examining the relationship between the volatility of returns and measures of market activity such as volume and the number of transactions. For example, see Besembinder and Seguin (1993), Chan and Fong (2000), Easley and O’Hara (1992), Easley et. al. (1997), Epps and Epps (1976), Gallant et. al. (1992), Harris (1986, 1987), Hasbrouk (1999), Jones et. al. (1994), Karpo¤ (1987, 1988), Lamaourex and Lastrapes (1990, 1994), Li (2004), Liesenfeld (1998, 2001), Richardson and Smith (1994) and Tauchen and Pitts (1983). 

Clark (1973) was the …rst to propose using a stochastic clock as a time changer in order to recover the normality of returns. Clark wrote the price process for cotton futures as a subordinated process, where the economic interpretation of the subordinator was the cumulative volume of traded contracts. 

In the empirical section of Ané and Geman (AG, 2000), a widely cited and important paper, the authors revisit Clark’s method of dealing with the nonnormality of observed returns. AG considered a general time change process. Using a novel non-parametric procedure, AG claim to have recovered the moments of the time change process which, apart from its …rst moment, matched the moments of the observed number of transactions but not those of volume in their data. Geman (2005, p.2712) summarized this result as showing, "that in order to recover a quasi perfect normality of returns, the transactions clock is better represented by the number of trades than the volume". 

These empirical results are not uncontroversial. On the one hand it is consistent with the …ndings of Hasbrouk (1999), Easley and O’Hara (1992), Jones, Kaul and Lipton (1994) and Lillo, Farmer and Mantegna (2003). On the other hand, Li (2004) and Izzeldin (2005), for example, are unable to reproduce this …nding. The other important theoretical contribution of the AG paper - the result that any arbitrage-free return process can be expressed as a stochastic time-changed Brownian motion process - is, of course, not an issue. 

In this paper, we examine the empirical procedure AG used to recover the moments of the time changer or information ‡ow. We identify some problems with the procedure and show, using Monte Carlo experiments, that their procedure produces extremely inaccurate estimates of the higher moments of the time changer. We explain why this happens and suggest that, contrary to the claim in AG, it is very di¢ cult to model the stochastic time change non-parametrically. We also show that, contrary to the claims in AG, actual returns conditioned on the recentered number of trades are not approximately Gaussian. 

The outline of this paper is as follows. In Section 2, we sketch the AG model of returns and critically examine their procedure for recovering the moments of the stochastic time change generating the non-normality of returns. Our Monte Carlo experiments are described in Section 3. The results of these experiments are discussed in Section 4. In Section 5, we use actual 1997 Nastraq data for Cisco and Intel - the same two stocks and the year used by AG - to show that the transactions and volume clocks do not produce near normal returns. In Section 

2 

6, we show that this result also applies to other stock returns. We conclude with a brief summary in Section 7. 

## 2. RECOVERING THE MOMENTS OF THE STOCHASTIC TIME CHANGER 

Ané and Geman (AG, 2000) consider a general return process r(t) = x(i(t)) where x(:) is a Brownian motion and i(t) is some stochastic time change or information ‡ow process, which may include a jump component. The stochastic time change process generalizes the subordinated processes considered by Clark (1973). The Brownian motion assumption is innocuous since, as AG note, any arbitrage-free return process can be expressed as a time-changed Brownian motion process (Monroe, 1978). At a point in time, a time changed Brownian motion process is just a normal mixture. 

We consider a discrete time version of the AG process since the notation is somewhat simpler and our arguments remain valid in continuous time. In discrete time, AG assume that, conditional on the exogenous time changer / information ‡ow it, returns rt are normally distributed with mean �rit and variance �[2] r[i][t][.][Thus][r][t][is][distributed][as][a][normal][mixture:] 


![](markdown_output/AG_images/AG.pdf-0003-04.png)


Let m[i] 1[; :::][,][m][i] 6[denote the …rst six (central) moments of][ i][t][.][Then, it is straight] forward to show that the …rst six unconditional (central) moments m[r] 1[; :::; m][r] 6[of] the normal mixture rt are as follows: 


![](markdown_output/AG_images/AG.pdf-0003-06.png)


These moment conditions are the discrete time analogues of those in Appendix A of AG. 

There are a number of identi…cation problems. Firstly, the parameters �r and �[2] r[are][only][identi…ed][up][to][scale][since][i][t][is][not][observed.][Suppose][i][t][is] replaced by �it with �> 0 so that m[i] 1[; : : : ; m][i] 6[become][�m][i] 1[; : : : ; �][6][m][i] 6[in][the] moment conditions. Then �r=� and �[2] r[=�][satisfy][the][new][moment][conditions.] Li (2004) also noted this problem. Thus �r, �[2] r[and][m][i] 1[are][not][separately] identi…ed. One solution to this scaling problem is to normalize the mean of the unobserved information ‡ow process m[i] 1[to][one.][It][is][not][clear][how][AG][deal] with this issue. 

3 

Secondly, with high frequency data, returns are zero on average so, a priori, it is plausible to set �r to zero. However, when �r = 0, the three uneven moment conditions are identically zero so identi…cation becomes even more problematic. Finally, even when �r is non zero and m[i] 1[is][set][to][one,][the][seven][remaining] parameters (�r; �[2] r[; m] 2[i][; : : : ; m][i] 6[)][are][not][identi…ed][from][six][moment][conditions.] They can only be recovered if additional restrictions are imposed or additional moment conditions are added. 

AG augment the six moment conditions with a number of approximate moment generating function (MGF) conditions: 


![](markdown_output/AG_images/AG.pdf-0004-02.png)


where �i = �i�r + 2[1][�] i[2][�][2] r[and][di¤erent][values][of][�] i[are][used.][This][approach][is] similar to the exact MGF approach set out in Quandt and Ramsey (1978) and Schmidt (1982). AG do not explicitly discuss the likely approximation errors involved in these restrictions or the choice of the �i’s. Here, we follow Geman and Ané (1996), a closely related paper, and use the values -0.7,-0.5, 0.3 and 0.6 for the �i’s. 

AG suggest that the results are not sensitive to the particular choice of the �i’s as long as very large and small values are not used. Our results con…rm this. However, our Monte Carlo simulations suggest that the approximate MGF conditions are not very informative about the higher moments of it. One reason for this is that the higher order m[i] 3[and][m][i] 4[terms][in][AG’s][approximate][MGF] conditions are extremely small. As a result, m[i] 3[and][m][i] 4[are][poorly][identi…ed,][if] at all. Another reason is that very large sample sizes are required to estimate accurately E[exp(�irt)] using its sample analog T1 Pt[exp(][�] i[r][t][)][.][In][addition,] T1 Pt[exp(][�] i[r][t][)][ and] T[1] Pt[exp(][�] j[r][t][)][ are highly collinear when][ �] i[and][ �] j[have the] same sign. For these reasons, the use of additional approximate MGF conditions is of little help in identifying the higher moments of it, especially with high frequency data when �r is basically zero. This is not a small sample problem. 

We also consider a bivariate data generation process or DGP similar to those considered by Clark (1973), Tauchen and Pitts (1983), Harris (1987) and Richardson and Smith (1994), inter alia. Conditional on the information ‡ow it, we assume that returns rt and observed "market activity" at (volume, log volume, the number of trades etc.) are independently and normally distributed as: 


![](markdown_output/AG_images/AG.pdf-0004-06.png)


with the means and variances of both rt and at linear in it. Of course, there is no compelling theoretical reason to assume that market activity, however de…ned or transformed, is normally distributed and linear in it. 

As before, the unconditional bivariate moments m[ra] jk[=][E][(][r][t][�][Er][t][)][j][(][a][t][�] Eat)[k] of rt and at are easily calculated. The univariate and bivariate moments can be used to identify and estimate �r; �a; �[2] r[and][ �][2] a[as well as the moments of] 

4 

the information ‡ow process m[i] 2[; ::; m][i] 6[.][The][bivariate][approach][should,][assum-] ing a correctly speci…ed data generation process (DGP), produce more precise estimates since it exploits more information and uses exact moments. It also provides more potential over-identifying restrictions. 

## 3. THE MONTE CARLO EXPERIMENTS 

In our Monte Carlo experiments, we simulate returns from three DGPs and see how well the AG procedure works. Our three DGPs are the normal lognormal, the normal inverse Gaussian and the normal gamma. All three normal mixture distributions have been widely used in the empirical …nance literature. The three DGPs simply assume di¤erent (exogenous) distributions for it, with rt j it s N (�rit; �[2] r[i][t][)][ in every case.][They are all easy to calibrate and simulate.] 

The normal lognormal mixture was initially used by Clark (1973) to model the returns on cotton futures. In this model, the unobserved information ‡ow it is assumed to be lognormally distributed. In the normal inverse Gaussian DGP, introduced by Barndor¤-Nielsen (1995), the information ‡ow is distributed as an inverse Gaussian random variable. In the normal gamma (or variance gamma) DGP, associated with Madan and Seneta (1990), the information ‡ow has a gamma distribution. In all three cases, the distributions of it depend on two parameters. However since the …rst moment of it is normalized to unity, the two parameters are not independent. 

We used the following settings in the Monte Carlos. We set �r equal to 0 or 0.1 and �[2] r[equal][to][0.1.][The][zero][mean][setting][is][probably][the][appropriate][one] to use when considering high frequency data. The parameters of the information ‡ow distributions were chosen so that m[i] 2[= 0][:][5][ given the normalization][ m][i] 1[= 1][.] The other moments of it vary by distribution. In our bivariate simulations, we use �a = 3 and �[2] a[= 1][:][3][ for our "market activity" variable.][These settings were] suggested by the results from using the bivariate moment conditions to recover the moments of it using 10 years of Nastraq return and volume data for the Dell stock at the 5 minute frequency. 

In our experiments, we restrict our attention to recovering the …rst four central moments of it, as the higher moments of it are more di¢ cult to estimate. The simulations and moment estimation / recovery were carried out in the econometrics package TSP (Hall and Cummins 1997). AG used a method of moments like procedure to try and recover the moments of it. We used the generalized method of moments or GMM procedure (Hansen, 1982) which should be more e¢ cient, a point also noted by Li (2004). In practice, the method of moments and GMM procedures produce very similar results, so we only present the latter here. 

We use sample sizes of 500, 1000, 2500, 5000 and 10000 observations in our experiments. Sample sizes of 5000 and 10000 observations are not uncommon in studies using, respectively, daily and high frequency data. Finally, our Monte Carlo results are all based on 1000 replications. 

5 

## 4. THE MONTE CARLO RESULTS 

In Tables 1, 2 and 3 we look at the performance of the AG univariate procedure for recovering the moments of the time changer it. We use the 2nd, 4th and 6th moment of the return process rt and two approximate moments based on the MGF. The results for the Normal Lognormal DGP are set out in Table 1. The results show the third and fourth order moments of the time changer / information ‡ow it cannot be accurately recovered using the AG procedure. This is true even in very large samples of 10,000 observations, so the poor performance of the AG procedure is not just a small sample problem. For example, with 10,000 observations, the average value of mb[i] 3[is][close][to][the][true][value][of] 0.875 in the DGP, but the associated average standard error of 0.495 remains large. As expected, the results for m[i] 4[are considerably worse than those for][ m][i] 3[.] Note that the GMM test statistic gives no indication of this poor performance. 

We carried out further Monte Carlo experiments to see if our poor performance …nding is robust. The results for the normal gamma and normal inverse Gaussian DGPs in Tables 2 and 3 are similar to those for the normal log normal DGP in Table 1. We also ran some Monte Carlo experiments using DGPs (i) with non-zero means for returns, (ii) rescaling returns by multiplying them by 100, (iii) with di¤erent and/or additional moment conditions and (iv), as noted above, using least squares rather than GMM to estimate the moments of the time changer. In all cases, the AG procedure cannot recover the higher moments of the unobserved time changer / information ‡ow. The approximate MGF moment conditions are just not informative about the moments of it. 

In Table 4 we set out some representative GMM results for the case where we use the moments of both returns rt and some activity variable at (such as the number of trades or volume) to recover the moments of the time changer / information ‡ow. The results in Table 4 show that the third and fourth order moments of it can be recovered in this bivariate setup. Of course, the bivariate setup involves additional assumptions and large samples are required to estimate the higher moments of it precisely. This …nding also holds true for the two other bivariate DGPs - normal gamma and normal inverse Gaussian - which we examined. 

## 5. EVIDENCE USING CISCO AND INTEL RETURN DATA 

In the empirical section of their paper, AG used Reuters data for 1997 to examine 1 and 10 minute returns for Cisco Systems and 5 and 15 minute returns for Intel. We did not have access to the actual data used by AG so we used the NYSE TAQ trade data for the same two stocks. We downloaded the data from the Wharton Research Data Services website and calculated the intra day (9.30 am to 4 pm) returns, volume and the number of trades for the two stocks. We omitted a small number of prer holiday afternoon periods, when the volume of trade was very low or zero. When calculating the Cisco and Intel returns, we used 10 and 15 minute time intervals respectively.. 

Table 5 reports the estimated moments of the time changer / information ‡ow it using AG’s univariate moments and two di¤erent sets of bivariate mo- 

6 

ments using the number of trades or volume as our activity measure. The AG procedure produces large and implausible estimates of m[i] 3[and][m][i] 4[,][in][line][with] our Monte Carlo results, whereas the bivariate results appear more plausible and signi…cant. The volume and trade results are reasonably similar to each other, which should come as no surprise since the number of trades and volume are highly correlated. The estimated moments of it do not match those of either volume or the number of trades, contrary to AG’s claim that the transactions clock should be based on the number of trades. 

Even though the AG procedure does not produce accurate estimates of the higher moments of it, it is still possible that returns conditioned by the recentered number of transactions may be approximately Gaussian. However, Figure 1 and the more formal results in Table 6 con…rm that returns conditioned by re-centered volume or the number of transactions are not normally distributed. The recentred variables are scaled to have a mean of unity. 

The conditioned returns are more Gaussian than the raw returns but the normal distribution still provides a poor approximation. The Jarque-Bera test statistics bear this out: the null of normality is always decisively rejected. The evidence does not support AG’s claim regarding the transactions clock. It would be extremely useful if all the important features of the latent information ‡ow were captured by a combination of returns and the number of trades or volume. Unfortunately, this does not appear to be the case. 

## 6. SOME FURTHER EVIDENCE 

We also tried to recover the moments of it using data for Dell and WorldCom stocks. We used 5 minute binned Nastraq data for 68 trading days from 8th March to the 8th June 2000, which yielded 5,304 observations per stock. Table 7 reports the estimated moments of the time changer / information ‡ow it The AG procedure again produces large and implausible estimates of m[i] 3[and][m][i] 4[.] The bivariate procedures generate more plausible and signi…cant estimates. In fact, the estimated moments of it for both Dell and WorldCom using trades and volume are similar. Moreover, in the case of Dell, the moments of re-centered transactions are surprisingly close to the estimated moments recovered using the bivariate model with transactions. However, it is clear from Figure 2 and the results in Table 8 that both the Dell and WorldCom returns conditioned by re-centered volume or the number of transactions are not normally distributed. 

## 7. CONCLUSIONS 

We show that the univariate procedure used by Ané and Geman (2000) to recover the moments of the latent time changer / information ‡ow from high frequency data is not reliable. Our Monte Carlo results show that the third and higher moments of the time changer cannot be accurately recovered using AG’s procedure because the approximate MGF conditions used are not informative. Our Monte Carlo results show that bivariate procedures work fairly well assuming the mean and variance of market "activity" is linear in the time changer. We also present some empirical evidence that returns conditioned on the re-centered number of trades or volume are not Gaussian. 

7 

## ACKNOWLEDGMENTS 

We thank, Professor Mark Salmon, Professor Hélyette Geman, Professor David Peel, and Clive Bowsher for their helpful comments. 

## REFERENCES 

Ané, T., and Geman, H. (2000), "Order ‡ow, transaction clock, and normality of asset returns", The Journal of Finance, 55(5), 2259–2284. 

Barndor¤-Nielsen, O. E. (1995), "Normal inverse Gaussian processes and the modelling of stock returns", research report 300, Dept. of Theoretical Statistics, Aarhus University. 

Bessembinder, H., and Seguin, P. J. (1993), "Price volatility, trading volume, and market depth: Evidence from futures markets", Journal of Financial and Quantitative Analysis, 28, 21–39. 

Chan, K. , and Fong, W. (2000), "Trade size, order imbalance, and the volatilityvolume relation", Journal of Financial Economics, 57(2), 247–273. 

Clark, P. K. (1973), ‘A subordinated stochastic process model with …nite variance for speculative prices’, Econometrica, 41(1), 135–155. 

Easley, D., and O’Hara, M. (1992), "Time and the process of security price adjustment", The Journal of Finance, 47(2), 577–605. 

Easley, D., Kiefer, N., and O’Hara, M. (1997), "One day in the life of a very common stock", Review of Financial Studies, 10, 805–835. 

Epps, W., and Epps, M. (1976), "The stochastic dependence of security price changes and transaction volumes: Implications for the mixture of distribution hypothesis", Econometrica, 44(2), 305–321. 

Gallant, A. R., Rossi, J„and Tauchen, G. (1992), "Stock prices and volumes", Review of Financial Studies, 5, 199–242. 

Geman, H. (2005), "From measure change to time changes in asset pricing", Journal of Banking and Finance, 29, 2701–2722. 

Geman, H., and Ané, T. (1996), "Stochastic subordination", Risk, 9(9), 145– 150. 

Hall, B. H., and Cummins, C. (1997), TSP 4.5 User’s Guide, TSP International, Palo Alto, California. 

Hansen, L. P. (1982), "Large sample properties of generalized methods of moments estimators", Econometrica, 50, 1029–1054. 

Harris, L. (1986), "Cross-security tests of the mixture of distributions hypothesis", Journal of Financial and Quantitative Analysis, 21, 39–46. 

8 

Harris, L. (1987), "Transaction data test of the mixture of distributions hypothesis", Journal of Financial and Quantitative Analysis, 22, 127–41. 

Hasbrouk, J. (1999), "Trading fast and slow: Security market events in real time", working paper, New York Stock Exchange. 

Izzeldin, M. (2005), "Essays on the mixture of distribution hypothesis model: Investigating model validity in high frequency data", unpublished Ph.D. dissertation, Cass Business School, City University, London. 

Jones, M., Kaul, G., and Lipson, M. (1994), "Transactions, volume and volatility", Review of Financial Studies, 7(4), 631-651. 

Karpo¤, J. M. (1987), "The relation between price changes and trading volume: A survey", Journal of Financial and Quantitative Analysis, 22(1), 109-126. 

Karpo¤, J. M. (1988), "Costly short sales and the correlation of returns with volume", Journal of Financial Research, 11, 173–188. 

Lamaourex, C. G., and Lastrapes, D. (1990), "Heteroskedasticity in stock return data: Volume versus GARCH e¤ects", Journal of Finance, 45, 221–229. 

Lamaourex, C. G., and Lastrapes, D. (1994), "Endogenous trading volume and momentum in stock-return volatility", Journal of Business and Economic Statistics, 2, 253–260. 

Li, Y. (2004), "Estimation of information time in stock returns", working paper, Department of Economics, Yale University. 

Liesenfeld, R. (1998), "Dynamic bivariate mixture models: Modelling the behavior of prices and trading volume", Journal of Business and Economic Statistics, 16, 101–109. 

Liesenfeld, R. (2001), "A generalized bivariate mixture model for stock price volatility and trading volume", Journal of Econometrics, 104, 141–178. 

Lillo, F., Farmer, J. D., and Mantegna, R. (2003), "Master curve for priceimpact function", Nature, 421(6919), 129–130. 

Madan, D. B., and Seneta, E. (1990), "The VG model for share market returns", Journal of Business, 63, 511–524. 

Monroe, I. (1978), "Processes that can be embedded in Brownian motion", Annals of Probability, 6(1), 42–56. 

Quandt, R. E., and Ramsey, J. B. (1978), "Estimating mixtures of normal distributions and switching regressions", Journal of the American Statistical Association, 73, 730–738. 

Richardson, M., and Smith,T. (1994), "A direct test of the mixture of distribution hypothesis: measuring the daily ‡ow of information", The Journal of Financial and Quantative Analysis, 29(1), 101–116. 

9 

Schmidt, P. (1982), "An improved version of the Quandt-Ramsey MGF estimator for mixtures of normal distributions and switching regressions’, Econometrica, 50(2), 501–516. 

Tauchen, G., and Pitts, M. (1983), "The price varability-volume relationship on speculative markets", Econometrica, 51(2), 485–505. 

10 

|Table 1. Estimated Moments of the Time Changer - Normal Lognormal DGP for Returns<br>Zero mean for returns (�r = 0) and one over-identifying restriction|Size of GMM Test Statistic|10% Level<br>5% Level<br>1% Level|11%<br>5%<br>1%<br>9%<br>6%<br>1%<br>9%<br>5%<br>1%<br>9%<br>6%<br>1%<br>11%<br>5%<br>1%|-<br>-<br>-|NOTE: The moments of the time changer are estimated using GMM and AG’s univariate procedure. The<br>following …ve moment conditions are used - the 2nd, 4th and 6th moment of r and two approximate MGF<br>moments with �= -0.7 and 0.6. The results are based on 1000 converged replications. The table entries are<br>the average parameter estimates and standard errors (in parentheses) in the 1000 Monte Carlo experiments.<br>Details of the DGP are set out in Section 3 of the paper.|
|---|---|---|---|---|---|
||Ave. GMM Parameter Estimates and Std. Errors<br><br><br><br><br>|�r<br>�2<br>r<br>mi<br>1<br>mi<br>2<br>mi<br>3<br>mi<br>4|0.000<br>0.099<br>1.000<br>0.457<br>0.584<br>-248.9<br>-<br>(0.008)<br>-<br>(0.218)<br>(0.847)<br>(5330.2)<br>0.000<br>0.099<br>1.000<br>0.471<br>0.671<br>-135.2<br>-<br>(0.005)<br>-<br>(0.160)<br>(0.560)<br>(3741.8)<br>0.000<br>0.099<br>1.000<br>0.488<br>0.805<br>-86.8<br>-<br>(0.003)<br>-<br>(0.122)<br>(0.602)<br>(2565.0)<br>0.000<br>0.099<br>1.000<br>0.497<br>0.839<br>15.7<br>-<br>(0.002)<br>-<br>(0.094)<br>(0.534)<br>(1890.6)<br>0.000<br>0.099<br>1.000<br>0.500<br>0.898<br>-52.1<br>-<br>(0.001)<br>-<br>(0.073)<br>(0.495)<br>(1387.8)|0.000<br>0.100<br>1.000<br>0.500<br>0.875<br>3.890||
||Sample<br>Size||T = 500<br>T = 1000<br>T = 2500<br>T = 5000<br>T = 10000|True Parameters||



11 

|Table 2. Estimated Moments of the Time Changer - Normal Gamma DGP for Returns<br>Zero mean for returns (�r = 0) and one over-identifying restriction|Size of GMM Test Statistic|10% Level<br>5% Level<br>1% Level|9%<br>5%<br>1%<br>11%<br>5%<br>1%<br>9%<br>5%<br>1%<br>12%<br>6%<br>1%<br>11%<br>6%<br>1%|-<br>-<br>-|NOTE: See notes to Table 1.|
|---|---|---|---|---|---|
||Ave. GMM Parameter Estimates and Std. Errors<br><br><br><br><br>|�r<br>�2<br>r<br>mi<br>1<br>mi<br>2<br>mi<br>3<br>mi<br>4|0.000<br>0.098<br>1.000<br>0.470<br>0.366<br>28.459<br>-<br>(0.008)<br>-<br>(0.181)<br>(0.422)<br>(4978.098)<br>0.000<br>0.099<br>1.000<br>0.493<br>0.459<br>-115.658<br>-<br>(0.005)<br>-<br>(0.146)<br>(0.447)<br>(3622.802)<br>0.000<br>0.099<br>1.000<br>0.500<br>0.527<br>16.134<br>-<br>(0.003)<br>-<br>(0.104)<br>(0.421)<br>(2407.032)<br>0.000<br>0.100<br>1.000<br>0.489<br>0.445<br>80.300<br>-<br>(0.002)<br>-<br>(0.073)<br>(0.285)<br>(1674.744)<br>0.000<br>0.100<br>1.000<br>0.496<br>0.476<br>-16.435<br>-<br>(0.001)<br>-<br>(0.054)<br>(0.241)<br>(1214.866)|0.000<br>0.100<br>1.000<br>0.500<br>0.500<br>1.500||
||Sample<br>Size||T = 500<br>T = 1000<br>T = 2500<br>T = 5000<br>T = 10000|True Parameters||



12 

|Table 3. Estimated Moments of the Time Changer - Normal Inverse Gaussian DGP for Returns<br>Zero mean for returns (�r = 0) and one over-identifying restriction|Size of GMM Test Statistic|10% Level<br>5% Level<br>1% Level|11%<br>6%<br>1%<br>9%<br>5%<br>1%<br>9%<br>5%<br>1%<br>10%<br>5%<br>1%<br>11%<br>6%<br>1%|-<br>-<br>-|NOTE: See notes to Table 1.|
|---|---|---|---|---|---|
||Ave. GMM Parameter Estimates and Std. Errors<br><br><br><br><br>|�r<br>�2<br>r<br>mi<br>1<br>mi<br>2<br>mi<br>3<br>mi<br>4|0.000<br>0.099<br>1.000<br>0.453<br>0.495<br>86.875<br>-<br>(0.008)<br>-<br>(0.195)<br>(0.529)<br>(5020.108)<br>0.000<br>0.099<br>1.000<br>0.467<br>0.548<br>-101.931<br>-<br>(0.005)<br>-<br>(0.152)<br>(0.475)<br>(3688.182)<br>0.000<br>0.099<br>1.000<br>0.495<br>0.718<br>-118.704<br>-<br>(0.003)<br>-<br>(0.117)<br>(0.510)<br>(2543.679)<br>0.000<br>0.099<br>1.000<br>0.497<br>0.737<br>69.395<br>-<br>(0.002)<br>-<br>(0.089)<br>(0.452)<br>(1884.414)<br>0.000<br>0.100<br>1.000<br>0.500<br>0.747<br>-42.212<br>-<br>(0.001)<br>-<br>(0.066)<br>(0.367)<br>(1327.396)|0.000<br>0.100<br>1.000<br>0.500<br>1.500<br>2.625||
||Sample<br>Size||T = 500<br>T = 1000<br>T = 2500<br>T = 5000<br>T = 10000|True Parameters||



13 

|Table 4. Estimated Moments of the Time Changer<br>Bivariate Normal Lognormal DGP for Returns and "Activity"<br>Zero mean for returns and one over-identifying restriction|Size of GMM Test Statistic|10% Level<br>5% Level<br>1% Level|22%<br>15%<br>7%<br>20%<br>14%<br>7%<br>17%<br>11%<br>6%<br>16%<br>11%<br>5%<br>15%<br>10%<br>5%|-<br>-<br>-|NOTE: GMM results based on 1000 replications using the following seven moment conditions - the second and fourth<br>moments of returns r, the …rst four moments of "activity" a and the covariance between r2 and a.|
|---|---|---|---|---|---|
||Ave. GMM Parameter Estimates and Std. Errors<br><br><br><br><br><br>|�r<br>�2<br>r<br>�a<br>�2<br>a<br>mi<br>1<br>mi<br>2<br>mi<br>3<br>mi<br>4|0.000<br>0.096<br>2.980<br>1.818<br>1.000<br>0.439<br>0.745<br>2.508<br>-<br>(0.007)<br>(0.107)<br>(0.955)<br>-<br>(0.106)<br>(0.326)<br>(1.806)<br>0.000<br>0.098<br>2.988<br>1.697<br>1.000<br>0.462<br>0.758<br>2.963<br>-<br>(0.005)<br>(0.076)<br>(0.714)<br>-<br>(0.082)<br>(0.268)<br>(1.741)<br>0.000<br>0.099<br>2.995<br>1.593<br>1.000<br>0.482<br>0.844<br>3.565<br>-<br>(0.003)<br>(0.048)<br>(0.487)<br>-<br>(0.058)<br>(0.207)<br>(1.565)<br>0.000<br>0.099<br>2.998<br>1.524<br>1.000<br>0.491<br>0.858<br>3.755<br>-<br>(0.002)<br>(0.034)<br>(0.357)<br>-<br>(0.043)<br>(0.161)<br>(1.377)<br>0.000<br>0.099<br>2.998<br>1.525<br>1.000<br>0.495<br>0.863<br>3.773<br>-<br>(0.001)<br>(0.024)<br>(0.256)<br>-<br>(0.031)<br>(0.120)<br>(1.088)|0.000<br>0.100<br>3.000<br>1.500<br>1.000<br>0.500<br>0.875<br>3.890||
||Sample<br>Size||T = 500<br>T = 1000<br>T = 2500<br>T = 5000<br>T = 10000|True Parameters||



14 

Table 5. Estimated Moments of the Time Changer it for Cisco and Intel Using the Univariate AG Procedure and Two Bivariate Procedures 

|Moments|Cisco (10 Minute) Returns<br><br><br>|Intel (15 Minute) Returns<br><br><br>|
|---|---|---|
||mi<br>2<br>mi<br>3<br>mi<br>4<br>mi<br>2<br>mi<br>3<br>mi<br>4||
|Univariate moments<br>Bivariate moments with volume<br>Bivariate moments with transactions|63.279<br>9992.91<br>1.15e+09<br>9.897<br>424.198<br>5.7e+08<br>(21.837)<br>(3190.57)<br>(8.8e+08)<br>(1.994)<br>(88.523)<br>(1.8e+08)<br>0.667<br>1.636<br>8.311<br>0.858<br>2.607<br>20.379<br>(0.094)<br>(0.232)<br>(2.038)<br>(0.085)<br>(0.554)<br>(7.082)<br>0.814<br>2.231<br>14.397<br>0.914<br>3.254<br>28.705<br>(0.073)<br>(0.304)<br>(3.012)<br>(0.094)<br>(0.773)<br>(12.906)||
|Moments of re-centered volume<br>Moments of re-centered transactions|0.707<br>1.439<br>6.461<br>0.603<br>1.659<br>11.777<br>0.540<br>0.851<br>3.114<br>0.520<br>1.208<br>6.194||



NOTE: GMM results with standard errors in parentheses. The moment conditions used are the same as those in Tables 1 to 3. The bivariate moments are the same as in Table 4. The Cisco and Intel results are based on on 10 and 15 minute return data respectively. The Data are described in Section 5 of the the text. The re-centered volume and transactions data are scaled so that they have unit means. 

Table 6. The Moments of Cisco and Intel Raw Returns and Returns Conditioned by the Re-centered Number of Trades and Volume 

||Cisco Systems (10 Minutes)<br>r<br>r<br>~~p~~<br>v<br>r<br>~~p~~<br>t|Intel (15 Minutes)<br>r<br>r<br>~~p~~<br>v<br>r<br>~~p~~<br>t|
|---|---|---|
|Mean<br>Variance<br>Skewness<br>Excess Kurtosis<br>Jera-Barque Test|0.0009<br>-0.0003<br>-0.0008<br>0.243<br>0.239<br>0.277<br>0.004<br>0.471<br>-6.456<br>194.930<br>117.144<br>522.913<br>1.15e+07<br>5.60e+07<br>1.11e+08|-0.003<br>-0.008<br>-0.007<br>0.169<br>0.156<br>0.154<br>-0.101<br>-0.219<br>-0.210<br>20.087<br>7.525<br>55.412<br>109721.2<br>15449.1<br>839714.4|



NOTE: r = returns, v = re-centered volume, t = re-centered no of transactions. The data are the same as in Table 5. 

15 

Table 7. Estimated Moments of the Time Changer it for Dell and WorldCom Using the Univariate AG Procedure and Two Bivariate Procedures 

|Moments|Dell<br><br><br>|WorldCom<br><br><br>|
|---|---|---|
||mi<br>2<br>mi<br>3<br>mi<br>4<br>mi<br>2<br>mi<br>3<br>mi<br>4||
|Univariate moments<br>Bivariate moments with volume<br>Bivariate moments with transactions|1.200<br>3.275<br>0.144e+11<br>3.953<br>65.409<br>0.478e+12<br>(0.169)<br>(0.976)<br>(0.341e+10)<br>(0.095)<br>(25.115)<br>(0.124e+11)<br>0.498<br>1.940<br>10.304<br>0.618<br>1.317<br>7.366<br>(0.044)<br>(0.312)<br>(2.423)<br>(0.133)<br>(0.398)<br>(0.027)<br>0.603<br>1.686<br>10.650<br>0.622<br>1.197<br>5.706<br>(0.043)<br>(0.306)<br>(3.427)<br>(0.092)<br>(0.279)<br>(1.618)||
|Moments of re-centered volume<br>Moments of re-centered transactions|0.806<br>2.361<br>14.905<br>0.534<br>1.191<br>6.657<br>0.611<br>1.707<br>10.851<br>0.390<br>0.773<br>3.488||



NOTE: GMM results with standard errors in parentheses. The moment conditions used are the same as those in Tables 1 to 3. The bivariate moments are the same as in Table 4. The binned 5 minute data used are described in Section 6 of the paper. Volume and transactions are scaled so that they have a mean of one. The sample size is 5,236. 

Table 8. The Moments of Dell and WorldCom Raw Returns and Returns Conditioned by the Re-centered Number of Trades and Volume 

||Dell<br>r<br>r<br>~~p~~<br>v<br>r<br>~~p~~<br>t|WorldCom<br>r<br>r<br>~~p~~<br>v<br>r<br>~~p~~<br>t|
|---|---|---|
|Mean<br>Variance<br>Skewness<br>Excess Kurtosis<br>Jera-Barque Test|0.0008<br>-0.0072<br>-0.0073<br>0.105<br>0.108<br>0.088<br>0.054<br>-0.147<br>-0.114<br>3.774<br>3.138<br>0.579<br>3111.0<br>301.6<br>84.8|-0.005<br>-0.0076<br>-0.0064<br>0.064<br>0.058<br>0.051<br>-0.038<br>0.047<br>0.040<br>11.864<br>2.762<br>2.637<br>30714.2<br>1666.6<br>1519.3|



NOTE: r = returns, v = re-centered volume, t = re-centered no of transactions. The data are the same as in Table 7. 

16 


![](markdown_output/AG_images/AG.pdf-0017-00.png)


**----- Start of picture text -----**<br>
0.025<br>Ln Empirical MGF<br>Ln AG Approx MGF<br>0.020<br>0.015<br>0.010<br>0.005<br>0.000<br>-0.6 -0.5 -0.4 -0.3 -0.2 -0.1 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7<br>**----- End of picture text -----**<br>


Figure 1. The AG approximate and empirical MGFs for a NIG return process with 10,000 observations. The natural logs of the empirical and approximate MGFs are plotted against �, which ranges from -0.7 to +0.7. In the DGP, rt j it s N (0; 10[1][i][t][)][and][i][t][is][Inverse][Gaussian][with][parameters][�][=][1] and � = 2 AG’s approximate MGF is exp(�m[i] 1[)] h1 +[�] 2[2][m] 2[i][+][�] 6[3][m] 3[i][+][�] 24[4][m] 4[i] i,[1] where m[i] 1[:::; m][i] 4[are][the][moments][of][i][t][and][�][.=][1] 2[�][2] 10[(since][�][r][=][0][and][�][2] r[=] 101[in][this][case).][The][empirical][MGF][is][just] T[1] Pt[exp(][�r][t][)][.] 

17 


![](markdown_output/AG_images/AG.pdf-0018-00.png)


**----- Start of picture text -----**<br>
150 150<br>CISCO Returns INTEL Returns<br>Normal Normal<br>100 100<br>50 50<br>-0.03 -0.02 -0.01 0.00 0.01 0.02 0.03 -0.03 -0.02 -0.01 0.00 0.01 0.02 0.03<br>CISCO r / sqrt(t) INTEL r / sqrt (t)<br>Normal 100 Normal<br>100<br>50 50<br>-0.02 -0.01 0.00 0.01 0.02 0.03 -0.03 -0.02 -0.01 0.00 0.01 0.02 0.03<br>CISCO r / sqrt(v) INTEL r / sqrt(v)<br>100 Normal 100 Normal<br>50 50<br>-0.02 -0.01 0.00 0.01 0.02 0.03 -0.02 -0.01 0.00 0.01 0.02 0.03<br>**----- End of picture text -----**<br>


Figure 2. Estimated densities of Cisco Systems and Intel raw returns and returns conditioned by the re-centered numbers of trades and volume. The Cisco 10 minute returns are shown on the right and Intel 15 minute returns on the left. The densities of the raw returns, returns conditioned by trades and returns conditioned by volume are displayed in top, middle and bottom panels respectively. Normal distributions with the same mean and variances are also shown. The data are described in Section 5 of the paper. 

18 


![](markdown_output/AG_images/AG.pdf-0019-00.png)


**----- Start of picture text -----**<br>
DELL Returns WCOM Returns<br>1.5 Normal 2 Normal<br>1.0<br>1<br>0.5<br>-2 -1 0 1 2 -2 -1 0 1 2 3<br>1.5<br>DELL: r / sqrt(t) 2 WCOM: r / sqrt(t)<br>Normal Normal<br>1.0<br>1<br>0.5<br>-1.0 -0.5 0.0 0.5 1.0 1.5 -1 0 1 2<br>1.5<br>DELL: r / sqrt(v) 2 WCOM: r / sqrt(v)<br>Normal Normal<br>1.0<br>1<br>0.5<br>-1.5 -1.0 -0.5 0.0 0.5 1.0 1.5 2.0 -1 0 1 2<br>**----- End of picture text -----**<br>


Figure 3. Estimated densities of Dell and WorldCom returns and returns conditioned by the re-centered numbers of trades and volume. The Dell returns are shown on the right and WorldCom returns on the left. The densities of the raw returns, returns conditioned by trades and returns conditioned by volume are displayed in top, middle and bottom panels respectively. Normal distributions with the same mean and variances are also shown.The data are described in Section 6 of the paper. 

19 

