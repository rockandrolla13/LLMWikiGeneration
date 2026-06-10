Journal of Financial Econometrics, 2020, Vol. 18, No. 3, 585–628 doi: 10.1093/jjfinec/nbaa015 Article 

**==> picture [55 x 55] intentionally omitted <==**

# Mixed-Frequency Macro–Finance Factor Models: Theory and Applications* 

## Elena Andreou[1,2] , Patrick Gagliardini[3,4] , Eric Ghysels[2,5] and Mirco Rubin[6] 

> 1University of Cyprus, 2CEPR, 3Universita`della Svizzera italiana, 4Swiss Finance Institute, 5University of North Carolina - Chapel Hill and 6EDHEC Business School 

Address correspondence to Elena Andreou, University of Cyprus, University Avenue 1, P. O. Box 20537, 1678 Nicosia, Cyprus, or e-mail: elena.andreou@ucy.ac.cy. 

Received April 20, 2020; revised April 20, 2020; accepted April 30, 2020 

## Abstract 

This article presents tests for the existence of common factors spanning two large panels/groups of macroeconomic and financial variables, and the estimation of common and group-specific factors. New analytical results are derived regarding (i) the difference in the asymptotic distribution of the test statistics when aggregating the data first and then extracting the principal components (PCs), or vice versa, as well as (ii) the estimation of the common factor and its asymptotic distribution, extending the work of Andreou et al. (2019). We find that although there is no empirical evidence for one common factor, with constant loadings, in the United States during the period 1963– 2017, there is evidence of one common macro–finance factor during the pre- and postGreat Moderation regimes. The aforementioned approaches of estimating PCs yield almost identical common and group-specific (financial and macro) factors which turn out to be significant in predicting key economic indicators, such as real Gross Domestic Product (GDP) growth and the CBOE Volatility Index, among others. 

Key words: large panel, unobservable pervasive factors, mixed frequency, canonical correlations, forecasting models 

JEL classification: C22, C38, C53, C55 

This article contributes to our understanding of factor models, one of many areas which was of keen interest to Peter Christoffersen, in particular when it touched on research in 

- We would like to thank the Editor, Frank Diebold, and two referees for insightful comments which helped improve our article. The first author would like to acknowledge that this work was funded by the Republic of Cyprus through the Research and Innovation Foundation (Project: INTERNATIONAL/USA/0118/0043). The authors would like to thank Mathias Drehmann for sharing his business and financial cycle indicators series. 

> VC The Author(s) 2020. Published by Oxford University Press. All rights reserved. For permissions, please email: journals.permissions@oup.com 

Journal of Financial Econometrics 

586 

both finance and econometrics.[1] Christoffersen was a real scholar and we would like to illustrate this by reporting on an exchange we had with him. At some point, we asked Christoffersen whether we could use his realized skewness series for our own research—obviously citing the original work (Amaya et al., 2015). Christoffersen graciously sent us his data series, and we are happy to put that series—among others—to good use in this article. 

In this article, new analytical results are derived for the asymptotic distribution of the principal components (PCs) as well as the test for common factors between groups/panels of variables of mixed data frequencies, when either aggregating the data first and then extracting the PCs or when applying PC analysis (PCA) first and then aggregating the estimates. In addition, the asymptotic theory results are derived for the common factor estimation methods. New empirical results are also presented to test for the existence of common factors spanning two large panels/groups of macroeconomic and financial variables, as well as to estimate common and group-specific factors related to each of the aforementioned panels. 

Hence this article contributes to the macro–finance literature in extracting the common factor (CF) also refered to as macro–finance factor between the financial sector and the U.S. real/nominal economy indicators. A macro–finance factor is the common part among the spaces of pervasive factors in the macro and finance panels. In other words, it is a common factor among the PCs extracted independently from the panels of macro and finance series. The role of the common as well as financial- and macro-specific factors for forecasting key macroeconomic and financial indicators is evaluated both in-sample (IS) and outof-sample (OOS), uncovering some interesting results. 

Macro panel data are often sampled at a low frequency (LF) (e.g., annual/quarterly), whereas higher frequency (HF) (e.g., daily/weekly) data are typically collected pertaining to financial indicators. Prime examples are, for example, for the macro panels, the Stock and Watson (2008) quarterly data as well as the McCracken and Ng (2016) FRED quarterly/ monthly data dominated by macroeconomic indicators, versus higher frequency financial indicators such as the (intra)daily stock market or exchange rate indices, the Gilchrist and Zakrajsek (2012) monthly credit spreads panel and the Fama and French portfolios of sorted equity returns. Extracting the common factor (the evidence suggests there is only a single common factor—more on this later) between the two large panels/groups of macroeconomic and financial markets series provides a way to study how the U.S. common macro–finance component has evolved over time, its cyclical behavior, which variables drive this common factor, how the factor and/or its loadings might have changed over the last 55 years, as well as the role of the common factor in Granger causing and forecasting key economic indicators. 

In extracting factors from mixed-frequency group panels, two approaches are pursued: the first approach is to aggregate the HF data and then perform PCA while the second approach refers to extracting the PCA first. Andreou et al. (2019) established the large sample distributional properties of the statistic for testing the number of common and groupspecific factors in the first approach. While the two alternative approaches were also compared in Andreou et al. (2019) with accompanying simulation evidence, this article provides analytical results deriving the asymptotic expansion of PCs estimates following these two approaches and how these affect the distribution of the test for common factors 

- 1 A partial list of his contributions in the area includes Christoffersen, Ghysels, and Swanson (2002), Christoffersen, Fournier, and Jacobs (2017), Christoffersen et al. (2014), Christoffersen and Langlois (2013), among others. 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

587 

between the groups/panels. Moreover, conditions are presented under which the asymptotic distributions of the common factor test following the two approaches coincide. 

Our empirical analysis presents evidence that the two approaches of aggregation first/ PCA last or PCA first/aggregation last, yield almost identical PCs estimates as well as inferences regarding the number of factors and the common factor test. For our given groups of the monthly financial panel and the quarterly U.S. macro panel, we find that although there is no evidence for one common factor in the United States during the full sample period starting from the 1960s, there is, however, evidence of one CF during the pre- and postGreat Moderation (GM) regimes. We show that this is due to structural changes in the loadings of the common factor during the period 1963–2017, which is driven by almost all the categories of macro and financial variables considered in this study. In addition, groupspecific factors, namely HF financial factors and LF macro factors are extracted. The forecasting role of the aforementioned factors (common and group specific) is further investigated in predicting key macroeconomic as well as financial indicators such as real GDP and consumption of services and nondurable goods growth, the Moody’s corporate bond default spread, the CBOE Volatility Index (VIX) and Variance Risk Premium (VRP) as well as the Exchange Traded Fund (ETF) iShares Core S&P500 returns. Our mixed-frequency group factors are also compared with other well-known factors in the literature extracted from different but related panels such as the mixed-frequency small panel factor measuring real business conditions of Aruoba, Diebold, and Scotti (2009), the large panel of corporate spreads factor of Gilchrist and Zakrajsek (2012), the large panel extracting an activity index/factor by Brave and Butters (2012), among others. Last but not least, the role of groups/panels of mixed sampling frequencies of data in estimating common and group-specific factors via PCs is also compared with the traditional approach that extracts factors from a single panel that stacks all variables (both macro and financial) together in common (low) frequency. 

The article is organized as follows: Section 1 presents the mixed-frequency group factor model and the test for common factors. Section 2 provides the asymptotic results of the factors and the common factor test for the two approaches: PCA first or PCA last as well as the asymptotic distribution of estimators of the common factor. Section 3 presents a comprehensive empirical analysis, and Section 4 concludes the article. Online Appendix, henceforth referred to as OA, provides proofs, supplementary theoretical results, an extensive description of the dataset used in the empirical application, and additional empirical results. 

## 1 Group Factor Models 

In this section, we revisit the class of group factor models studied by Andreou et al. (2019), henceforth AGGR.[2] We use the following notation for the group factor model setting, assuming two groups: 

**==> picture [245 x 42] intentionally omitted <==**

- 2 See also Kose, Otrok, and Whiteman (2008), Goyal, Pe´rignon, and Villa (2008), Chen (2012), Wang (2012), Ando and Bai (2015), and Breitung and Eickmeier (2016) for recent contributions to the group factor model literature. 

Journal of Financial Econometrics 

588 

where yj;t ¼ ½yj;1t; . . . ; yj;Njt�[0] collects observations for Nj individuals in group j, K[c] j[¼] ½k[c] j;1[;][ . . .][ ;][ k][c] j;Nj[�][0][and][K][s] j[¼ ½][k][s] j;1[;][ . . .][ ;][ k][s] j;Nj[�][0][are][the][matrices][of][factor][loadings,][and][e][j][;][t][¼] ½ej;1t; . . . ; ej;Njt�[0] is the vector of error terms, with j ¼ 1, 2, and t ¼ 1; . . . ; T, related to our empirical analysis of the macro and financial groups/panels. The dimensions of the common factor ft[c][and][the][group-specific][factors][f][ s] 1;t[;][f][ s] 2;t[are,][respectively,][k][c][,][k][s] 1[,][and][k][s] 2[.][The] errors and factor processes are stationary, serially mixing, and satisfy the assumptions on weak cross-sectional dependence and existence of higher-order moments in AGGR, Appendix A. The group-specific factors f1[s] ;t[and][ f][ s] 2;t[are orthogonal to the common factor][ f][ c] t[.] Since the unobservable factors can be standardized, we assume (see Assumption A.2 in AGGR): 

**==> picture [334 x 121] intentionally omitted <==**

We consider the generic setting of Equation (1.1) and let kj ¼ k[c] þ k[s] j[, for][ j][ ¼][ 1, 2, be the] dimensions of the pervasive factor spaces for the two groups, and define k ¼ minðk1; k2Þ. We collect the factors of each group in the kj-dimensional vectors hj;t ¼ ðft[c][0][;][ f][ s] j;t[0][Þ][0][and define] their variance and covariance matrices: Vj‘ :¼ Eðhj;th[0] ‘;t[Þ][;][ j][; ‘][ ¼][ 1][;][ 2][:][ From][ Equation (1.2)][ we] have Vjj ¼ Ikj for j ¼ 1, 2. AGGR show that the factor space dimensions k[c] , k[s] 1[;][k][s] 2[are iden-] tifiable using canonical correlation analysis applied to h1;t and h2;t. In particular, according to their Proposition 1, it is shown that the number of common factors k[c] , the common factor space spanned by ft[c][, and the spaces spanned by group-specific factors can be identified] from the canonical correlations and canonical variables of h1;t and h2;t: Therefore, the factor space dimensions k[c] and k[s] j[and factors][ f][ c] t[and][ f][ s] j;t[,][ j][ ¼][ 1, 2, are identifiable (up to a rota-] tion) from information that can be inferred by disjoint PCA on the two subgroups. Indeed, disjoint PCA on the two subgroups allows us to identify the dimensions k1 and k2, and vectors h1;t and h2;t up to linear one-to-one transformations. Therefore, our group factor model provides some key insights in estimating and testing for the existence of the CF between these two groups/panels, while at the same time estimating the group-specific financial and macro factors which are orthogonal to the common factor. 

Assuming for a moment that the true number of factors kj > 0 in each subgroup j ¼ 1, 2, is known, and also that the true number of common factors k[c] > 0, is known, then the following estimation procedure for the common factors can be implemented. Let h1;t and h2;t be estimated (up to a rotation) by extracting the first kj PCs from each subpanel j, and denote by h[^] j;t these PC estimates of the factors, j ¼ 1, 2. Let H[^] j ¼ ½h[^] j;1; . . . ; h[^] j;T �[0] be the ðT; kjÞ matrix of estimated PCs extracted from panel Yj ¼ ½yj;1; . . . ; yj;T �[0] associated with the largest kj eigenvalues of matrix N1jT[Y][j][Y] j[0][,][ j][ ¼][ 1, 2. Let][V][^][ j][‘][denote the empirical covariance matrix of] 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

589 

the estimated vectors h[^] j;t and h[^] ‘;t, that is, V[^] j‘ ¼ T1[H][^] 0j[H][^][‘][¼] T1 PTt¼1[h][^][j][;][t][ ^][h] 0‘;t[;][ j][; ‘][ ¼][ 1][;][ 2][;][and][let] matrices R[^] and R[^] � be defined as: 

**==> picture [267 x 14] intentionally omitted <==**

where R[^] and R[^] � have the same nonzero eigenvalues. The kc largest eigenvalues of R^ (resp. R^�), denoted by q^ 2‘[;][‘][ ¼][ 1][;][ . . .][ ;][ k][c][,][are][the][first][k][c][squared][sample][canonical][correlation][be-] Wtween^ 1 (resp.h[^] 1;t ðandk2; kh[^][c] 2Þ;tmatrix: The associatedW[^] 2), are thek[c] canonicaleigenvectorsdirections,associated withcollectedthein kthe[c] largest eigenval-ðk1; k[c] Þ matrix ues of matrix R[^] (resp. R[^] �), normalized to have length 1 with respect to V^ 11 (resp. V^ 22). It 0 0 also holds that W[^] 1[V][^][ 11] W[^] 1 ¼ Ikc ; and W[^] 2[V][^][ 22] W[^] 2 ¼ Ikc : 

f^ct � AGGR consider two estimators of the common factors vector, that are[¼] W[^] 02[h][^][2][;][t][.][Note][that,] T1 PTt¼1[f][^] ct[f][^] ct 0[¼][ I][k][c][,][and][similarly][for][f][^] ct �[,][that][is,] f[^] ct[¼][the] W[^][estimated] 01[h][^][1][;][t][and] common factor values match IS the normalization condition of identity variance–covariance matrix in Equation (1.2). In this article, we explore the idea that linear combinations of these two “basis” estimators also yield valid estimators. More specifically, let us consider the estimator 

**==> picture [210 x 17] intentionally omitted <==**

where scalar parameter x is the weight. Transformation by matrix SðxÞ ¼ ½ð1 þ x[2] ÞIkc þ 2xD[^] �[�][1][=][2] , where D[^] ¼ diag ðq^ 1; . . . ; ^qk[c] Þ ensures property T1 PTt¼1[f][^] ct ?[ð][f][^] ct ?[Þ][0][¼] Ikc in sample.[3] 

Note that the idea we explore is reminiscent of forecast combinations, originated by Bates and Granger (1969) who studied optimal mean square error (MSE) forecast combinations. The natural question which emerges is how to choose the weight. One possibility is suggested by revisiting the work in Goyal, Pe´rignon, and Villa (2008) and references therein. They consider the estimator of the common factors that is obtained by the rows of the ðT; k[c] Þ matrix of standardized eigenvectors of matrix T1[ð][ ^][H][1][H][^] 01[þ][H][^][2][H][^] 02[Þ][associated][with] the k[c] largest eigenvalues. The computations in Section D.2 of Online Appendix of AGGR show that the rows of the eigenvectors matrix are ðf[^] ct[þ][f][^] ct �[Þ][0][;][t][¼][ 1][;][ . . .][ ;][ T][, up to normaliza-] tion. Hence, the Goyal, Pe´rignon, and Villa (2008) estimator corresponds to the linear combination in Equation (1.4) with weight x ¼ 1, that is, the equally weighted linear combination of the two basis estimators f[^] ct[and][f][^] ct �[.] 

An alternative choice for x is provided by the optimal weight which minimizes the asymptotic MSE (AMSE) of the factor estimator which would be more in line with the approach put forward by Bates and Granger (1969) (see also Timmermann, 2006 for a survey). We consider the asymptotics with N1; N2; T ! 1 such that 

**==> picture [260 x 17] intentionally omitted <==**

Further, to simplify the exposition, we focus here on the setting with k[c] ¼ 1, that is, a single common factor as we find in our empirical analysis, and conditionally homoskedastic errors that are uncorrelated across series and panels (see Online Appendix for a more 

**==> picture [331 x 21] intentionally omitted <==**

Journal of Financial Econometrics 

590 

general analysis). From AGGR Online Appendix Section D.5, we have the joint asymptotic distribution 

**==> picture [248 x 46] intentionally omitted <==**

where the asymptotic variance is the (2,2) diagonal matrix Ru ¼ diag ðR[ð] u[cc] ;11[Þ][;][ R][ð] u[cc] ;22[Þ][Þ][,][with] Ru;jj ¼ R[�] K;[1] j[X][K][;][j][R] K[�] ;[1] j[;][R][K][;][j][¼][ lim][N] j[!1] N1j PNi¼j1[k][j][;][i][k][0] j;i[and][X][K][;][j][¼][ lim][N] j[!1] N1j PNi¼j1[c][j][;][i][k][j][;][i][k][0] j;i[,][for] kj;i ¼ ðk[c] j;i[;][ k][s] j;i[0][Þ][0][and][c] j;i[¼][ E][½][e][2] j;i;t[�][,][j][ ¼][ 1,][2,][and][(][cc][)][denotes][the][upper-left][element][of][a] matrix. Random variables H[^] c and H[^] �c[converge][to][1][in][probability][for][the][suitable][sign] fix of the latent factor. The bias terms are b[c] j;t[¼][ �][c] j[ð][R] K[�] ;[1] j[h][j][;][t][Þ][ð][c][Þ][,] j ¼ 1,2, where �cj ¼ limNj!1 N1j PNi¼j1[c] j;i[.][From][Equation][(1.6)][,][we][obtain][the][AMSE][of][the][linear][combin-] ation f[^] ct ? in Equation (1.4), which depends on the factor realization ft via the asymptotic bias. In Online Appendix, we show that the average (across factor realizations) AMSE is minimized for 

**==> picture [222 x 29] intentionally omitted <==**

where Bjj ¼ �c[2] j h[R][�] K;[2] jiðccÞ, j ¼ 1, 2, and B12 ¼ �c1�c2hR[�] K;[1] 1[V][12][R][�] K;[1] 2iðccÞ. When N1=T[2] ¼ oð1Þ, the bias terms do not matter, and the optimal weight x depends positively on the ratio of the error variances Rðu[cc] ;11Þ[=][R] ðu[cc] ;22Þ[and][the][ratio][of][the][cross-sectional][dimensions][N][2][=][N][1][.][4][If] N1=T[2] does not shrink to zero, there is an effect from the bias terms. Of course, the parametric family Equation (1.4) encompasses the AGGR estimators f[^] ct[and][f][^] ct �[,][which][corres-] pond to choicesFor a given xchoice¼ 0 andof the x ¼ þ1weight, respectively.x, let F[^] c? ¼ ½f^c1? 0; . . . ; f[^] Tc? 0�[0] be the ðT; k[c] Þ matrix of estimated common factors, and K[^] cj[¼ ½][^][k] cj;1[;][ . . .][ ;][ ^][k] cj;Nj[�][0][the][ð][N][j][;][ k][c][Þ][matrix][collecting][the][esti-] mated loadings: 

**==> picture [250 x 19] intentionally omitted <==**

c c? commonMoreover, letfactor f[^] nct ?j[;] ;t[for] ¼ y[j] j[ ¼] ;t �[ 1,] K[^][2] j[f][^][and] t[be the residuals of the regression of][N][j][¼ ½][n][j][;][1][;][ . . .][ ;][ n][j][;][T][�][0][be][the][ð][T][;][ N][j][Þ][matrix][ y][j][;][t][on the estimated][of][the][regres-] sion residuals, for j ¼ 1, 2. Estimators of the specific factors f[^] s1;t[(resp.][f][^] s2;t[)][are][defined][as] the firsts k[s] 1[(resp.] s[ k][s] 2[) PCs of subpanel] s[ N][1][(resp.][ N][2][), namely, the columns of the][ ð][T][;][ k][s] j[Þ][ ma-] trixmatrixmatedF[^] j common[¼ ½] N1jT[f][^][N] j;1[j][N][;][ . . .][0] j[,] factors[normalized][ ;][ ^][f] j;T[�][0][are] in the[the][to] columns[have][eigenvectors][F][^] sj 0[F] of[^] sj[=] F[T][^] c[associated] ?[¼] are[ I][k][s] j orthogonal[for][j][with][ ¼][ 1,][the][2.] in[By][k] sample[s] j[construction,][largest] to[eigenvalues] the estimated[the][esti-][of] 

> 4 AGGR assumes that N2 ¼ minfN1; N2g without loss of generality. Note that depending on the application, N2 may pertain to either the LF or HF data panel. 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

591 

group-specific factors F[^] sj[,][for][j][ ¼][ 1,][2.][Finally,][the][loadings of][the][group-specific][factors are] estimated by 

**==> picture [244 x 19] intentionally omitted <==**

where K[^] sj[¼ ½][^][k] sj;1[;][ . . .][ ;][ ^][k] sj;Nj[�][0][is the][ ð][N][j][;][ k][s] j[Þ][ matrix collecting the estimated loadings.] How does one determine the dimension k[c] of the common factor space? To answer this question, we first consider the case where the number of pervasive factors k1 and k2 in each subpanel is known, hence k ¼ minðk1; k2Þ is also known, and we relax this assumption below. The dimension k[c] is the number of unit canonical correlations between h1;t and h2;t; see Proposition 1 in AGGR. We consider the hypotheses: H(0) ¼ f1 > q1 � . . . � qk[g][;][ H][(1)] ¼ fq1 ¼ 1 > q2 � . . . � qk[g][;][. . .][ ;][H][ð][k][c][Þ][¼][f][q] 1[¼ ���¼][ q] k[c][¼][ 1][ >][ q] k[c] þ1[�][. . .][ �][q] k[g][;][. . .][ ;] and finally, HðkÞ ¼ fq1 ¼ ���¼ qk[¼][ 1][g][;][ where][ q] 1[;][ . . .][ ;][ q] k[are the ordered canonical corre-] lations of h1;t and h2;t. Hypothesis H(0) corresponds to the absence of common factors. Generically, Hðk[c] Þ corresponds to the case of k[c] common factors and k1 � k[c] and k2 � k[c] group-specific factors in each group. The largest possible number of common factors is k ¼ minðk1; k2Þ: In order to select the number of common factors, let us consider the following sequence of tests: H0 ¼ Hðk[c] Þ against H1 ¼ [0 � r < kc HðrÞ; for each k[c] ¼ k; k � 1; . . . ; 1. To test H0 against H1, for any given k[c] ¼ k; k � 1; . . . ; 1 we consider: 

**==> picture [194 x 24] intentionally omitted <==**

The statistic[^] nðk[c] Þ corresponds to the sum of the k[c] largest sample canonical correlations of h[^] 1;t and h[^] 2;t. We reject the null H0 ¼ Hðk[c] Þ when[^] nðk[c] Þ � k[c] is negative and large. 

The critical value is obtained from the large sample distribution of the statistic under the joint asymptotics N1; N2; T ! 1; and the assumptions in Equation (1.5), as provided in AGGR. Then, let R^ U ¼ ðN2=N1ÞR^ ðucc;11Þ[þ][R][^] ðucc;22Þ[,] with R^ u;jj ¼ ðN1j[K][^] 0j[K][^][j][Þ][�][1][ð] N1j[K][^] 0j[C][^][j][ ^][K][j][Þ] ðN1j[K][^] 0j[K][^][j][Þ][�][1] where K^ j ¼ ½K^ cj .[..] K^ sj[�][;][K][^] cj and K^ sj are the loadings estimators, C^ j ¼ diag ð^cj;i; i ¼ 1; . . . ; NjÞ with ^cj;i ¼ T1 PTt¼1[^][e][2] j;i;t[,][and][ ^][e][j][;][i][;][t][¼][ y][j][;][i][;][t][ �][^][k] cj;i 0[f][^] ct ?[�][^][k] sj;i 0[f][^] sj;t[,][for][j][ ¼][ 1,] 2. Define the test statistic: 

**==> picture [292 x 24] intentionally omitted <==**

with N ¼ minfN1; N2g: Then Theorem 2 of AGGR, which holds under the assumptions that the errors are conditionally homoskedastic martingale difference sequences and are not cross-sectionally correlated, shows that: (i) under the null hypothesis H0 ¼ Hðk[c] Þ of k[c] common factors, we have:[e] nðk[c] Þ!d Nð0; 1Þ and (ii) under the alternative hypothesis p H1 ¼ [0 � r < kc HðrÞ, we have:[e] nðk[c] Þ! �1. Importantly, the asymptotic distribution and rate of convergence of the test statistic[e] nðk[c] Þ in Theorem 2 of AGGR are unchanged when the true numbers of pervasive factors k1 and k2 are unknown, and is estimated by consistent selection methods as those provided, among others, by Bai and Ng (2002), Onatski (2010), and Ahn and Horenstein (2013). The above test statistics can be used to determine the number of common factors (and therefore by difference the number of group-specific factors) by means of a sequential testing procedure, see Proposition 2 in AGGR. 

Journal of Financial Econometrics 

592 

## 2 Mixed-Frequency Group Factor Model: PCA First or Last? 

When we apply the theory of group factor models to mixed-frequency data, some additional issues emerge, not studied by AGGR. It is the purpose of this section to expand on such issues. First, we pose the case of mixed frequency as a group factor model in the first subsection. Then, we address specific issues hitherto unresolved—namely the interchange of aggregation and PCA. We are able to solve explicitly the comparison under some restrictive conditions and provide practical guidance to empirical work. The derivations in this section are complementary to the Monte Carlo simulations reported in AGGR. They provide analytic support instead of simulation-based evidence. 

## 2.1 Model Structure 

Let t ¼ 1, 2, . . . ; T be the LF time units. Each time period ðt � 1; t� is divided into M subperiods with HF dates t � 1 þ m=M, with m ¼ 1, . . . ; M and the cross-section is of size NH for the HF data and NL for the LF data. We let x[H] m;[;] t[i][;][ for][ i][ ¼][ 1,][ . . .][ ;][ N] H[;][ be the HF data observa-] tion i during subperiod m of LF period t. Similarly, x[L] t[;][i][, with][ i][ ¼][ 1,][ . . .][ ;][ N] L[, is the observa-] tion of the i[th] LF series at t. These observations are gathered into the NH-dimensional vectors x[H] m;t[, for all][ m][, and the][ N][L][-dimensional vector][ x][L] t[, respectively.] 

There are three types of latent pervasive factors, g[C] m;t[;][g][H] m;t[,][and][g][L] m;t[;][respectively,][of][di-] mension k[C] , k[H] , and k[L] : The former represents a vector of factors which affect both HF and LF data, and the other two types of factors affect exclusively high (superscript H) and low (marked by L) frequency data. The latent factor model with HF data sampling is: 

**==> picture [231 x 25] intentionally omitted <==**

where m ¼ 1; . . . ; M and t ¼ 1; . . . ; T, and KHC, KH, KLC, and KL are matrices of factor loadings. The vector x[L] m[�] ;t[is][unobserved][for][each][HF][subperiod][and][the][measurements,] denoted by x[L] t[,][depend][on][the][observation][scheme,][which][can][be][either][flow][sampling][or] stock sampling (or some general linear scheme). 

In the case of flow sampling, the LF observations are the sum (or average) of all x[L] m[�] ;t across all m, that is, x�[L] t[¼][ P][M] m¼1[x] m[L][�] ;t[.][5][ Then, model (2.1) implies:] 

**==> picture [262 x 38] intentionally omitted <==**

PMmLet¼1[e] m[U] us;t[;][U] define[ ¼][ H][,] the[L][,][and] aggregated[the][aggregated] variables[factors:] and[g][�] innovations[U] t[:][¼][P][M] m¼1[g] x�m[U][H] t;t[;][U] :¼[ ¼][P][ C][,][M] m[H] ¼1[,][x][L] m[H][.] ;t[Then][,][e][�][U] t[we] :¼ can stack the observations x�[H] t[and][x][�][L] t[and write:] 

**==> picture [249 x 42] intentionally omitted <==**

> 5 In the case of stock sampling, the LF observations are the end-of-period values xM[L][�] ;t[(or the values] at some other given date m within a subperiod). The analysis proceeds analogously, replacing summation over subperiods with evaluation at the end-of-period. We cover the flow sampling here because it corresponds to the empirical analysis reported in later sections. 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

593 

that is, the group factor model, with common factor g�[C] t[and][group-specific][factors][g][�][H] t[and] g�[L] t[.][The][normalized][latent][common][and][group-specific][factors][g][�][U] t[;][U][ ¼][ C][;][ H][;][ L][,][satisfy][the] counterpart of Equation (1.2). 

Finally, the results in AGGR can be applied for identification and inference in the mixed-frequency factor model—see their section 5 for details. In particular, AGGR show under mild assumptions on the factor loadings, that the HF values g[C] m;t[and][ g][H] m;t[of the com-] mon and high-frequency factors (HFFs) are identifiable. Not surprisingly, only the flowsampled values g�[L] t[of][the][low-frequency][factor][(LFF)][are][identifiable][from][the][LF][observa-] tions of the corresponding group (or panel). 

## 2.2 Aggregation and PCA 

Inference on the factor spaces and their dimensions can be conducted in two ways which are described below. We focus first on the inference on the number of common factors and leave the estimation of factor values for the next subsection. 

(1) First flow sample the data and obtain a group factor model for observables x�[H] t[;][i] and x�[L] t[;][i][, with pervasive factors, loadings matrices, and idiosyncratic errors given by] 

**==> picture [267 x 54] intentionally omitted <==**

inh^1;thet andHFh^2and;t, computeLF panels,therespectively.canonical correlationsNext, applyq^ ‘PCAand canonicalin each groupdirectionsto get WPC^ 1 estimatesand W[^] 2, and the test statistic[^] nðk[C] Þ ¼[P][k] ‘¼[C] 1[q][^] ‘[for][ k][C][ common factors. Theorem 1 of AGGR implies] that under the null Hðk[C] Þ the test statistic (after recentering and standardization) is asymptotically standard Gaussian. 

hg[C] m(2);t[0][;][ g][H] mFirst;t[0] i0 atperformHF andPCAh2;t ¼on,�g�[C] trespectively,[0] ; �g[L] t[0] �0 at LF,theandHFthenandflowLF panelssample totheextractHF factorh1;mesti-;t ¼ matesand h[^] 2to;t, the canonical directionsget h[�] 1;t ¼[P][M] m¼1[h][�][1][;][m][;][t][,][compute] W[�] 1 and W[the][�] 2, and the test statistic[canonical][correlations][�] nð[q][�] k‘[C][among] Þ ¼[P][k] ‘¼[LF][C] 1[q][�][PCs] ‘[for][h][ k][�][1][C][;][t] common factors. The “check” symbol notation highlights the difference with approach (1). If the HF panel data, PC estimates obey an asymptotic expansion of the same type as the one in Proposition 3 of AGGR, then upon aggregation: 

**==> picture [305 x 104] intentionally omitted <==**

where h1;t is as in Equation (2.4) and 

Journal of Financial Econometrics 

594 

g[2] 1;m;t[¼][ plim] NH !1 N1H PNi¼H1[E][½ð][e] m[H] ;[;] t[i][Þ][2][jF] t[�][;][d][�] 1;t[¼][ P][M] m¼1[d][1][;][m][;][t][;][#][�][1][;][t][¼][ P][M] m¼1[#][1][;][m][;][t] is a remainder term and F t ¼ rðFs; s � tÞ is the sigma field generated by current and past factor values Ft ¼ ðft[c][0][;][ f][ s] 1;[0] t[;][ f][ s] 2;[0] t[Þ][0][.][6][The][asymptotic][distribution][of][the][test][statistic][follows][from] Theorem 1 in AGGR by substituting the quantities in Equation (2.6) for j ¼ 1 and those in Equation (2.5) for j ¼ 2. Specifically, under the null hypothesis H0 ¼ Hðk[C] Þ and the assumptions in Equation (1.5) that correspond to the regularity conditions in Theorem 1 of AGGR, the asymptotic distribution of the test statistics[�] nðk[c] Þ ¼[P][k] ‘¼[c] 1[q][�] ‘;t[in approach (2) is] such that: 

**==> picture [333 x 42] intentionally omitted <==**

**==> picture [327 x 176] intentionally omitted <==**

and similarly for R[e] u;22 and R[e] u;12 using the LF quantities. The term b2;t is defined in AGGR as b2;t ¼ ~~ð~~ N1L PNi¼L1[k][2][;][i][k] 2[0] ;i[Þ][�][1] ~~[ð]~~ T1 PTt¼1[h][2][;][t][h] 2[0] ;t[Þ][�][1][g] 2[2] ;t[h][2][;][t] with g[2] 2;t[¼][ plim] NL!1 N1L PNi¼L1[E][½][e][2] 2;i;t[jF][ t][�][and][b][�][2][;][t][¼][ R][�] K;[1] 2[g][2] 2;t[h][2][;][t][is][its][large][cross-sectional] limit, b[��] 1;t ¼ R[�] K;[1] 1[E][½][h][1][;][m][;][t][h][0] 1;m;t[�][�][1] M1 PMm¼1[g] 1[2] ;m;t[h][1][;][m][;][t][is][the][large][cross-sectional][limit][of][b][�][1][;][t] defined in Equation (2.6), and RK;1 ¼ limNH !1 N1H PNi¼H1[k][1][;][i][k][0] 1;i[and][similarly][for][R][K][;][2][.][The] upper index (c) denotes the upper ðk[c] ; 1Þ block of a vector, and the upper index (c, c) denotes the upper-left ðk[c] ; k[c] Þ block of a matrix. 

The zero-mean terms uj;t, for j ¼ 1, 2, which drive asymptotic normality in the expansions of the PCs estimates are the same in both approaches (1) and (2). Hence, matrix XU;1 in the variance of the asymptotic distribution of the test statistic is also the same. Instead, the bias components b1;t and b[�] 1;t differ, which explain the different recentering term R[�] B and variance contribution X[�] U;2 when PCA is performed first compared to the result in 

> 6 The remainder term #[�] 1;t is the flow-sampled value of higher-order terms #1;m;t in the asymptotic expansion of the PCs in Group 1. A probability bound on its magnitude follows from Proposition 3 in AGGR. 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

595 

AGGR Theorem 1.[7] Therefore, the test statistics generally differ depending on whether aggregation or PCA is performed first. 

There is an important special case in which the asymptotic distributions of the test statistics in the two approaches coincide. Namely, let us assume that the HF error processes are uncorrelated across individual series and panels, at all leads and lags, and are conditionally homoskedastic martingale difference sequences given the unobservable factors: 

**==> picture [266 x 59] intentionally omitted <==**

where e[U] t�[;][i] 1þm=M[�][e] m[U][;] ;[i] t[,][for][U][ ¼][ H][;][ L][,][where] ne[U] n;[;] s[i] on < m_s < t[consists][of][all][error][terms] previous to subperiod m of date t. Then, XU;2 ¼ X[�] U;2 ¼ 0 and R[e] B ¼ R[�] B ¼ 0 in both approaches, and the test statistic under the null hypothesis Hðk[C] Þ is such that: 

**==> picture [303 x 24] intentionally omitted <==**

where R[e] u;11 ¼ MðN1H PNi¼H1[k][1][;][i][k] 1[0] ;i[Þ][�][1] ~~[ð]~~ N1H PNi¼H1[k][1][;][i][k] 1[0] ;i[c] H;i[Þ] ~~[ð]~~ N1H PNi¼H1[k][1][;][i][k] 1[0] ;i[Þ][�][1][and][similarly] for R[e] u;22 using the corresponding LF quantities, R[e] U ¼ ðNL=NHÞR[e] u;11 þ R[e] u;22; R[e] cc ¼ T1 PTt¼1[g][�][C] t[g][�][C] t[0] ; and RU being the large sample limit of R[e] U as NH; NL ! 1. The same distributional result as Equation (2.9) holds for[�] nðk[C] Þ. Even if the recentering and rescaling terms in the asymptotic distribution are the same whenever aggregation or PCA is performed first, the test statistic values[^] nðk[C] Þ and[�] nðk[C] Þ in the two approaches differ, because the canonical correlations estimates differ. 

## 2.3 Mixed-Frequency Factor Estimation 

In this subsection, we consider the estimation of the factor values and focus in particular on the asymptotic distribution of the estimator of the common factor. Building on the previous subsection, there are two approaches depending on whether aggregation (flow sampling) is performed before or after PCA. To simplify the exposition, we focus on the case k[C] ¼ 1. 

(i) When data are flow-sampled first, the estimator of the LF values of the common factor is 

**==> picture [213 x 16] intentionally omitted <==**

^ �1=2 ^�C 0 where SðxÞ ¼ �1 þ x[2] þ 2xq1� and x is the weight, with gt[¼] W[^] 1[h][^][1][;][t] and ^�C� 0 C? �H gt ¼ ^�W[^] L 2[h][^][2][;][t][.][Then,][we][use][the][residuals][from][g][^�] t to estimate the specific factors^ g[^] t and^ gt[,] ^ and the common^ and group-specific factor loadings to get K1 ¼ �KHC : KH�; K[^] 2 ¼ �K[^] LC : KL� in analogy with the procedure introduced in Section 1 

- 7 Vectors d1;t and d[�] 1;t differ, but are both a (stochastic, asymptotically nonsingular) linear transformation of vector h1;t, and therefore their contribution to the test statistic is asymptotically negligible. Further, matrices H1 and H[�] 1 that correspond to rotations of the factor estimates, also differ in approaches (1) and (2), but they are immaterial for the values of estimators and test statistics. 

Journal of Financial Econometrics 

596 

for the general group-factor framework. Finally, we estimate the HFF values g^[C] m;t[and][g][^][H] m;t from the cross-sectional regression of x[H] m;t[onto the estimated loadings:] 

**==> picture [219 x 31] intentionally omitted <==**

and LF estimates(ii) When PCA is g�[�] performed[C] t[�] ¼ W[�] 02[h][^] first, we have HF estimates[2][;][t][, of the common factor values. We follow the principle of lin-] g�[C] m;t[¼] W[�] 01[h][�][1][;][m][;][t][,][for][m][ ¼][ 1][;][ . . .][ ;][ M][,] ear combination to obtain another and possibly more efficient (in a sense to be defined below) HF estimator of the common factor. Consider the estimation of the common factor value for subperiod m. The linear combination of g�[C] n;t[;][n][ ¼][ 1][;][ . . .][ ;][ M][, and][g][��][C] t[�][, which yields an asymp-] totically unbiased estimator of g[C] m;t[, has the form] 

**==> picture [219 x 17] intentionally omitted <==**

for a coefficient am, up to a standardization to impose unit sample variance, where g��[C] t[¼][ P][M] n¼1[g][�] n[C] ;t[¼] W[�] 01[h][�][1][;][t][.] When we aggregate across subperiods, we get �� g[C] t[?] :¼[P][M] m¼1[g][�] m[C][?] ;t[¼][ a][g][��][C] t[þ ð][1][ �][a][Þ][g][��][C] t[�][,][where][a][ :][¼][ 1][ �][P][M] m¼1[a][m][.][Therefore,][for][the][flow-] sampled estimators, we get a linear combination analogous to Equation (2.10) with relative weight: 

**==> picture [194 x 10] intentionally omitted <==**

Finally, we use the residuals from g�[C] m[?] ;t[on the][HF panel,][and][the residuals][of][g][��][C] t[?] on the LF panel, to extract the group-specific factor estimates g�[H] m;t[and][g][��][L] t[.] 

How to choose the weights? If we mimic the Goyal, Pe´rignon, and Villa (2008) estimator in our mixed-frequency setting, we chose x ¼ 1 in (2.10) for the aggregation-first estimator. To have an analogous choice for the PCA-first estimator, Equation (2.12) suggests to have a ¼ 1=2. Imposing equal weights across subperiods as the simplest option, this yields am ¼ ð2MÞ[�][1] in Equation (2.11). 

Another approach to the determination of the weights consists of minimizing the asymptotic MSE of the estimators. For this purpose, we might consider either the flow-sampled estimates g�[^] Ct ? and g�[�][C] t[?] or the HF estimates g^[C] m[?] ;t[and][g][�][C] m[?] ;t[. In this article, we consider the for-] mer option and assume that the HF weights am ¼ M1 ð[1][ �][a] Þ ¼ M1 1þxx[for][the][PCA-first][esti-] mator are homogenous across subperiods. The latter option in a general framework is more challenging and is left for future research. Note that we impose Equation (2.8) to derive the results below. In Online Appendix, we derive the asymptotic Gaussian distributions of the flow-sampled estimators: 

**==> picture [181 x 22] intentionally omitted <==**

and 

**==> picture [181 x 23] intentionally omitted <==**

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

597 

whereþR[ð] u[cc] ;22[Þ][Þ][,] b� Ct ?with[ð][x][Þ ¼] 1þ1b�xC1[ð] ;[b][�] t C1[¼] ;t[ M][þ][ x][�][c][b][�] HC2[ð] ;t[R][Þ][;][�] K[e][b] ;[1] 1Ct[h] ?[1][ð][;][x][t][Þ][Þ ¼][ð][c][Þ][;] 1[b][�] þ1C2x;t[ð][e][b][¼] C1;[ M] t[þ][�][c][ x] L[b][�][ð][R] C2;t[�] K[Þ] ;[1] 2[h][2] and[;][t][Þ][ð][c][Þ][;] V[?] ebðxC1;Þ ¼t[¼] ð1M1þ1[�] x[c] Þ[H][2][ð][x][2][l] ð[R] R[ð] u[�] K[cc] ;11;[1][Þ] 1 E½h1;m;th[0] 1;m;t[�][�][1][h][1][;][t][Þ][ð][c][Þ][,] and R[ð] u[cc] ;jj[Þ][¼][ M][ð][R] K[�] ;[1] j[X][K][;][j][R] K[�] ;[1] j[Þ][ð][cc][Þ][,] j ¼ 1,2, RK;1 ¼ limNH !1 N1H PNi¼H1[k][1][;][i][k] 1[0] ;i[and][X][K][;][1][¼][ lim][N] H[!1] N1H PNi¼H1[c] H;i[k][1][;][i][k][0] 1;i[,][and][similarly][for][j][ ¼][ 2][on] the LF panel. The flow-sampled estimators with aggregation first or PCA first have the same asymptotic variance (for given x) and different asymptotic bias at order 1=T. The asymptotic bias is negligible if N=T[2] ¼ oð1Þ; and the two approaches PCA first or last are asymptotically equivalent.[8] The average AMSE of the aggregation-first estimator is 

**==> picture [334 x 63] intentionally omitted <==**

**==> picture [222 x 29] intentionally omitted <==**

For the PCA-first estimator, we get similar formulas with B11 and B12 replaced by Be11 ¼ M1[2][�][c][2] H[½][R] K[�] ;[1] 1[E][ð][h][1][;][m][;][t][h][0] 1;m;t[Þ][�][2][R] K[�] ;[1] 1[�][ð][cc][Þ] and Be12 ¼ �cH�cL½R[�] K;[1] 1[E][ð][h][1][;][m][;][t][h][0] 1;m;t[Þ][�][1][V][12][R] K[�] ;[1] 2[�][ð][cc][Þ][,] respectively. We can compare the AMSE of the aggregation-first and PCA-first estimators for specific DGPs. As in the Monte Carlo experiments in AGGR, let us assume that the HF dynamics f of the latent factors is given by the VAR(1) process gm;t ¼ aFgm�1;t þ pfgm;t with common AR coefficient aF, where gm;t ¼ ðg[C] m[0] ;t[;][ g] m[H] ;[0] t[;][ g] m[L][0] ;t[Þ][0] is the stacked factor vector, gm;t ¼ ðg[C] m[0] ;t[;][ g] m[H] ;[0] t[;][ g] m[L][0] ;t[Þ][0][�][IID][ð][0][;][ R][g][Þ][,][matrix][R][g][has][identity][matrices][as][diagonal][blocks,] Covf ¼ 1ðM�g[2][H] maj[2] F;t[;][with][ g] m[L] ;t[Þ ¼][j][ ¼][ U][ 1][,][ �][and] M2[2][zero] PMm¼[elements] 1[m][ð][1][ �][a][elsewhere.] F[M][�][m] Þ to ensure[The][scale] the[of] standardization[the][innovation] V[variance] ðhj;tÞ ¼ Ik[is] j . Then, we have E½h1;m;th[0] 1;m;t[�¼] M1[2] j[I][k][1][,][which][yields][B][e][11][¼][ j][B][11][and][B][e][12][¼][ j][B][12][with] j < 1. Therefore, from Equation (2.13), we can see that for this DGP the PCA-first estimator has smaller asymptotic bias and average AMSE for any given choice of weight x > 0 (the same in both approaches), such as x ¼ 1 for the analogue of the Goyal, Pe´rignon, and Villa (2008) estimator, as well as for the optimal choices of the weights (as long as these are positive, and B12 > 0). 

## 3 Empirical Analysis 

## 3.1 Data Description 

We employ two large panels/groups of variables available at two different sampling frequencies. The first panel comprises NL ¼ 188 LF, quarterly U.S. macroeconomic variables while the second panel comprises NH ¼ 116 HF, monthly financial variables.[9] The choice 

- 8 This corroborates the findings in our empirical analysis, where we have T ¼ 218 and N ¼ 116 and we find that the two approaches yield very similar estimates. 

- 9 Note that therefore in the empirical analysis NH < NL, but this does not matter since the large sample results can be derived in this case by interchanging the roles of NH and NL. 

Journal of Financial Econometrics 

598 

of quarterly frequency for the macro data is based on maximizing NL in this group to incorporate important indicators from the National Income and Product Accounts related to GDP, government expenditure, investment, among others. Similarly, the choice of the monthly frequency is constrained by the trade-off between increasing NH aiming to enlarge the cross section of financial variables to include, for example, interest rates and credit spreads, and at the same time covering a long-span of time series, T. While we acknowledge that many financial series are available at a much higher frequency (e.g., daily and/or intradaily), this choice would compromise both N and T as many of these higher frequencies series are not available since the early 1960s and this would challenge our inferential framework which is based on large N and T. 

The time series period is 1963m7–2017m12, with T ¼ 218 quarterly and TM ¼ 654 monthly observations. The macro panel is based on the quarterly macro indicators of FRED-QD (McCracken and Ng, 2016).[10] The financial panel includes the following financial indicator categories: (i) Interest Rates, (ii) Stock Markets, (iii) Exchange Rates, (iv) Soft (a) and Hard (b) Commodities.[11] All variables are transformed to represent stationary variables and each series is demeaned and standardized in the panel following either FRED-QD or the corresponding transformations for stationarity in Stock and Watson (2002) and Brave and Butters (2014). 

We also consider the following well-known factors in the literature extracted from different but related panels, such as the ADS factor of Aruoba, Diebold, and Scotti (2009) measuring real business conditions and based on a mixed-frequency small panel, the Chicago Federal National Activity Index (CFNAI) and the National Financial Conditions Indicator (NFCI; Brave and Butters, 2014) extracted from larger panels, as well as the credit spreads index of Gilchrist and Zakrajsek (2012) available from authors. 

The role of the aforementioned factors from the literature, as well as our mixedfrequency group factors, namely the common and group-specific factors, are further investigated in predicting key macroeconomic as well as financial indicators such as real GDP and consumption of services and nondurable goods growth, the Moody’s corporate bond default spread, the CBOE’s VIX also referred to as the “fear index”, the VRP (available from Zhou, 2018), as well as the ETF iShares Core S&P500 Index. 

## 3.2 Extracting the Common and Group-Specific Factors 

Within the mixed-frequency group factor model comprising U.S. quarterly (Low) frequency (LF) macroeconomic indicators and monthly (High) frequency (HF) financial variables, we investigate whether there is a CF spanning these two panels, as well as group-specific 

- 10 The panel includes the following eleven categories of variables: (i) National Income and Product (NIPA), (ii) Industrial Production, (iii) Employment and Unemployment, (iv) Housing, (v) Inventories, Orders and Sales, (vi) Prices, (vii) Earnings and Productivity, (viii) Money and Credit, (ix) Household Balance Sheet, (x) Consumer Expectations, and (xi) Nonhousehold balance sheet. The macro variables in each category are listed in Online Appendix Table OA.1. Our macro panel excludes the following FRED-QD categories: Exchange Rates, Interest Rates, and Stock Markets, since most of these variables are available at monthly frequency and belong to the financial panel. 

- 11 The financial variables in each category and the corresponding data sources are listed in Online Appendix Table OA.2. 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

599 

Financial/HF and Macro/LFFs, HFF, and LFF, respectively. Employing the methods developed in AGGR and further expanded in Sections 1 and 2, we find that although there is no common factor in the United States during the full sample period from 1963 to 2017, there is however, evidence of a single CF during the pre- and post-GM periods. These results are presented in Tables 1 and 2 which report the estimated number of pervasive factors in the HF and LF panels, as well as the canonical correlations and test statistics for the common factors, respectively. Following the analysis in the previous section, we apply the CF test using the PCA approach first as well as PCA last (i.e., aggregation first) to examine how inferences related to the number of factors and the CF test is affected. It is worth mentioning at the outset that we find that these two approaches of estimating factors yield very similar results for this empirical application. 

## 3.2.1 Group specific factors 

We start by selecting the number of factors in each subpanel and each subperiod. In Table 1, we report the results for the ICp2 information criterion of Bai and Ng (2002; similar results apply for the ICp1) and we choose the maximum number of factors (kmax) equal to ten in order to avoid excluding potentially important factors from the panels.[12] The ICp1 and ICp2 dominate the other criteria in Bai and Ng (2002). We focus the discussion on the number of factors in each subperiod (pre- and post-GM), given that we find one common factor in each of these regimes. For the panel/group of financial variables at monthly frequency (x[H] ) and quarterly frequency (x�[H] ), the ICp2 criterion, during the pre-GM period, selects six factors for x[H] and eight factors for x�[H] . In contrast, during the post-GM period, ICp2 selects nine factors for the x[H] and ten factors for x�[H] . On the contrary, for the quarterly macro variables panel/group, ICp2 selects five and six factors in the pre- and post-GM periods, respectively. The inference on the number of factors is robust to the PCA first or last approach, as shown in Table 1. Last but not least, we compare our inference on the number of group/frequency specific factors with the traditional approach of applying the ICp2 to a single panel with a common low (quarterly) frequency which stacks all the variables together, denoted by [x�[H] ; x�[L] ] in Table 1. In the latter case, the ICp2 chooses seven factors in the pre-GM vis-a`-vis nine factors in the post-GM. In our subsequent empirical applications, we proceed with the aggregation first approach (also followed in the empirical analysis of AGGR). 

Most criteria for factor selection, including the ICp2, choose factors in an unconditional setup, that is, without conditioning on the variable(s) of interest that the factors aim to explain or forecast. Moreover, from the total number of factors chosen from the panels and subperiods, it is expected that different factors will have varying explanatory power for different dependent variables of interest (e.g., macro or financial) and for alternative subperiods. Hence given that we are interested in the role of these factors in a conditional setup, our empirical analysis considers the above number of factors for each subpanel and regime in order to avoid any omitted factors/variables (hence the choice of kmax ¼ 10) in explaining key macro and financial variables. Subsequently, we reassess the conditional 

- 12 Similar results apply to kmax ¼ 8 found in Online Appendix Tables OA.3 and OA.4. Note that for smaller values of kmax < 6, we ignore some of the estimated factors in each subpanel and regime vis-a`-vis kmax ¼ 8 or 10 which also turn out to be significant in the conditional setup for explaining key macro and financial variables, as discussed in the next subsection. 

Journal of Financial Econometrics 

600 

Table 1 Estimated number of pervasive factors in HF and LF panels 

||Full Sample<br>xH<br>�xH<br>�xL<br>½�xH �xL�|Pre-GM<br>xH<br>�xH<br>�xL<br>½�xH �xL�|Post-GM|
|---|---|---|---|
||||xH<br>�xH<br>�xL<br>½�xH �xL�|
|ICp2<br>Aggregation frst<br>PCA frst|–<br>10<br>8<br>10<br>8<br>–|–<br>8<br>5<br>7<br>6<br>–|–<br>10<br>6<br>9<br>9<br>–|



Table 2 Canonical correlations and test statistics for common factors 

|Aggregation first/PCA last|||
|---|---|---|
|Full sample<br>(cv¼ �2.0003)kc ¼0)<br>i<br>^qi<br>enðiÞ|Pre-GM<br>(cv¼ �1.9048)kc ¼1)<br>i<br>^qi<br>enðiÞ|Post-GM|
|||(cv¼ �1.9477)kc ¼1)<br>i<br>^qi<br>enðiÞ|
|1<br>0.839<br>�5.139<br>2<br>0.782<br>�4.027<br>3<br>0.715<br>�7.211<br>4<br>0.590<br>�9.171<br>5<br>0.378<br>�12.51<br>6<br>0.170<br>�14.04<br>7<br>0.034<br>�8.384<br>8<br>0.025<br>�8.300|1<br>0.913<br>0.376<br>2<br>0.800<br>�4.015<br>3<br>0.696<br>�8.325<br>4<br>0.25<br>�8.987<br>5<br>0.150<br>�9.436|1<br>0.911<br>�0.187<br>2<br>0.812<br>�4.842<br>3<br>0.701<br>�8.721<br>4<br>0.545<br>�8.303<br>5<br>0.376<br>�7.872<br>6<br>0.144<br>�3.731|



PCA first/aggregation last 

|FULL SAMPLE<br>(cv¼ �2.0003)kc ¼0)<br>i<br>^qi<br>enðiÞ|Pre-GM<br>(cv¼ �1.9048)kc ¼1)<br>i<br>^qi<br>enðiÞ|Post-GM|
|---|---|---|
|||(cv¼ �1.9477)kc ¼1)<br>i<br>^qi<br>enðiÞ|
|1<br>0.834<br>�4.567<br>2<br>0.701<br>�10.640<br>3<br>0.603<br>�11.000<br>4<br>0.550<br>�12.850<br>5<br>0.258<br>�13.710<br>6<br>0.182<br>�14.180<br>7<br>0.080<br>�9.204<br>8<br>0.038<br>�6.405|1<br>0.894<br>�1.098<br>2<br>0.722<br>�6.721<br>3<br>0.626<br>�11.000<br>4<br>0.241<br>�8.714<br>5<br>0.228<br>�7.521|1<br>0.906<br>�0.195<br>2<br>0.786<br>�5.852<br>3<br>0.670<br>�9.609<br>4<br>0.434<br>�13.370<br>5<br>0.356<br>�8.260<br>6<br>0.200<br>�4.103|



Notes: x�[H] is the (T, NH) panel of the quarterly data computed as the sum of the HF monthly (TM, NH) panel data, x[H] , and x�[L] is the (T, NL) panel of the LF quarterly data and kmax ¼ 10. The number of observations is given by NH ¼ 116 for monthly financial variables, NL¼188 for quarterly macroeconomic variables, Tpost ¼ 128 during the post-GM period (1986q1–2017q4), Tpre ¼ 82 during the pre-GM period (1963q3– 1983q4), Tfull ¼ 218 during the full sample period (1963q3–2017q4). q^ i and[e] nðiÞ refer to the canonical correlation and test static of the i common factor, respectively. k[c] is the estimated number of common factors defined as k[c] ¼ maxfi : 1 � f i � kmax;[e] nðiÞ � cvg, where cv refers to the critical value reported above which is defined in AGGR as �cðNpTi ffiffiÞ[c] with c ¼ 0.95 and c ¼ 0:1. 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

601 

significance of factors using both IS and OOS criteria such as the goodness-of-fit, significance/thresholding for targeted predictors (Bai and Ng, 2008) and testing based on mean squared forecasting error criteria, discussed in Subsection 3.3. 

## 3.2.2 Common factor 

The estimated canonical correlations in each of the two subpanels of LF and HF data and the test statistics, reported in Table 2, provide evidence that there is one common factor in the two subperiods, before and after the mid-1980s. The inference on a single common factor in these two regimes is also robust whether we apply the PCA first or last approach, as shown by the two panels in Table 2. Note also that while results reported in Tables 1 and 2 refer to 1984q1 being the change point, as reported in Stock and Watson (2008), the results on the existence of one common factor are robust to other break dates in the mid-1980s during the period 1984q1–1985q4, which is also consistent with other studies in the literature.[13] Given that the inference on a single CF for these two regimes is robust following the two approaches, PCA first or last, we proceed to compare the actual PC estimates from these two approaches shown in Figure 1a and b, for the pre- and post-GM periods, respectively. The CFs estimated following the two approaches are very closely correlated as shown by the two PCs which are almost superimposed in Figure 1a and b, with the correlation of the factors from PCA first and last being 0.95 and 0.98, during the pre- and post-GM regimes, respectively. Moreover, the persistence of the CFs as measured by the simple AR(1) coefficient is estimated to be 0.79 (and 0.91) for PCA first and 0.88 (and 0.93) for the PCA last for the monthly CF in the first regime (and in the second regime). Further evidence on the factor estimates obtained from the two approaches is provided in Online Appendix Table OA.6 which reports the correlation matrices of all the factors showing that the corresponding PCs (from aggregation or PCA first) yield correlations of 0.94–1.00. 

In Table 3, we provide additional evidence which shows the alternative CF estimation methods discussed in Sections 1 and 2, focusing on the post-GM period. The common factor estimators CF1, CF2, CF3, and CF4 are based on Equation (2.10) with x ¼ 0, x ¼ þ1, x ¼ 1, and x as specified in Equation (2.14), respectively. These results show that not only the correlations of the alternative CFs are very high across the different estimation types (reported in Table 3), but also the time series behavior of these CF estimates is almost identical as shown in Figure 2. Hence, in the subsequent analysis, we use the third estimation type, CF3, that is, Equation (2.10) with x ¼ 1. Moreover, given the empirical evidence that the two approaches (PCA last or first) yield almost identical factor estimates we proceed with one of them namely aggregation first/PCA last, not only for conciseness in reporting results, but also because the aggregation first approach is more comparable to the common frequency single panel PCA approach (according to which all data are aggregated to a 

- 13 Enlarging the panel to include other financial indicators such as the Fama–French portfolios related to the forty-nine industries and 100 portfolios sorted on size and book to market, we find no common factor during the full sample and the two subperiods. This evidence suggests that a financial panel dominated by these U.S. portfolio-type stock market variables may mask the existence of a common factor between the macro and financial panels and other financial indicators (including the stock market indices). Further evidence related to the role of specific stock market variables (e.g., the VXO) in driving the common factor is provided below, related to the changing structure of the CF during the pre- and post-GM periods. 

Journal of Financial Econometrics 

602 

Figure 1 Common factor (CF) estimates using PCA first and last approaches during the (a) pre-GM and (b) post-GM. 

common LF and all variables are collapsed to a common panel in order to estimate the PCA at the end). This latter approach would be denoted as the common frequency factors (CFFs). 

The evidence of a CF during the pre- and post-GM is further investigated by testing for a structural change in the loadings of the CF (as well as the HFFs and the LFFs) in the mid1980s, which seems to affect the inference on the existence of a common factor during the full sample period, 1963–2017. If factor loadings have a break which is not only small, but also the change point is sufficiently independent across the cross section of time series used to estimate the factors, then its effect is averaged out across the many series in the panel and the PCs estimates are not affected (e.g., Stock and Watson, 2002). Applying theLM (resp. supLM) test for a break in the loadings of factor models proposed by Breitung and 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

603 

Table 3 Correlation coefficients between common factor (CF) estimation types during the postGM 

||CF1|CF2|CF3|CF4|
|---|---|---|---|---|
|Panel A: Correlations of HF CFs|Panel A: Correlations of HF CFs||||
|CF1|1|0.888|0.997|1|
|CF2|0.888|1|0.915|0.894|
|CF3|0.997|0.915|1|0.998|
|CF4|1|0.894|0.998|1|
|Panel B: Correlations of LF CFs:|Panel B: Correlations of LF CFs:||||
|CF1|1|0.927|0.998|1|
|CF2|0.927|1|0.942|0.931|
|CF3|0.998|0.942|1|0.999|
|CF4|1|0.931|0.999|1|



Notes: The common factor estimators CF1, CF2, CF3, and CF4 based on Equation (2.10) with x ¼ 0, x ¼ þ1, x ¼ 1, and x as specified in Equation (2.14), respectively. 

Figure 2 Common factor (CF) estimation types CF1, CF2, CF3, and CF4 during the post-GM. 

Eickmeier (2011), we report empirical evidence in Table 4 that in the mid-1980s, 50% (resp. 73%) of the CF loadings associated with the LF/macro series change, whereas 55% (resp. 67%) of the HF/financial loadings in the CF change, as shown by the total percentage of rejections of the null (no break) hypothesis. Note that applying the Chow test for breaks in factor loadings proposed in Stock and Watson (2008), we also find evidence of breaks.[14] Yet, given that the LM test for known break and supLM for unknown breaks are valid under more general assumptions and exhibit better finite sample properties (Breitung and Eickmeier, 2011), we focus our discussion on the LM-type tests. Within the cross section, 

- 14 We present only the results for the Breitung and Eickmeier (2011) supLM test. The results of the Chow test proposed by Stock and Watson (2008) are found in Online Appendix Table OA.5. 

Journal of Financial Econometrics 

604 

Table 4 LM-type tests for the GM structural break in the loadings of dynamic factor models 

||CF|CF|CFF1|CFF2|CFF1,|CFFs|CF, HFFs,|
|---|---|---|---|---|---|---|---|
||(Quarterly|(Monthly|(%)|(%)|CFF2 (%)|(ICp2) (%)|LFFs (%)|
||loadings)|loadings)||||||
||(%)|(%)||||||
|LM test (Breitung and Eickmeier, 2011)||||||||
|Total|50.0|55.2|46.1|60.5|68.4|89.5|99.0|
|Interest rates||67|93|74|96|100|100|
|U.S. stock market indices||69|62|69|77|100|100|
|Exchange rates||64|4|28|20|96|100|
|Commodities||41|22|14|22|49|94|
|NIPA|59||82|100|95|100|100|
|IP|60||93|80|93|100|100|
|Employment|70||66|89|98|100|100|
|Housing|100||0|100|100|100|100|
|Inventories, orders, and sales|50||83|100|100|100|100|
|Prices|9||24|33|46|91|100|
|Earnings and Productivity|40||50|60|90|100|100|
|Money and Credit|62||38|77|77|92|100|
|Household Balance Sheets|78||33|100|100|100|100|
|Consumer Expectations|100||0|100|100|100|100|
|Non-Household Balance Sheets|27||45|91|100|100|100|
|supLM test (Breitung and Eickmeier, 2011)||||||||
|Total|73.4|67.2|50.7|71.7|74.7|96.7|98.7|
|Interest rates||96|96|85|100|100|100|
|U.S. stock market indices||92|69|85|85|100|100|
|Exchange rates||60|8|36|36|100|100|
|Commodities||49|22|33|29|84|92|
|NIPA|91||82|100|100|100|100|
|IP|100||93|87|100|100|100|
|Employment|89||70|93|100|100|100|
|Housing|100||9|100|100|100|100|
|Inventories, orders, and sales|100||83|100|100|100|100|
|Prices|35||24|52|57|98|100|
|Earnings and Productivity|70||90|100|100|100|100|
|Money and Credit|69||46|77|77|92|100|
|Household Balance Sheets|89||44|100|100|100|100|
|Consumer Expectations|100||0|100|100|100|100|
|Non-Household Balance Sheets|55||64|100|100|100|100|



Notes: The reported values refer to the percentage of rejections of the null hypothesis of no breaks in the loadings. The above results refer to the case of estimating mixed-frequency group factors (CF, HFFs, and LFFs) with aggregation first (i.e., PCA last) which is more comparable to the CFFs. Same results apply to the case of estimating the factors with the PCA first approach. The reported results for the LM test refer to the subsample 1986q1–2017q4. Results are robust to other known break dates, namely 1984q4 as well as 1985q4. CF refers to the common factor from the MFF model. CFF extracted from the stacked panel of all low/quarterly frequency variables. The details of the variable categories and the variable definitions are found in Online Appendix. Bold values indicate the percentage of rejections for the total number of variables for the null hypothesis of no structural break of the LM test (for 5% significance level). 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

605 

there is strong evidence that the GM is associated with changes in the CF loadings of all variable categories in the two groups, macro and financial. Moreover, there is evidence that a large percentage of CF loadings change within many variables categories. In contrast, the changes in the loadings appear to be relatively smaller (than the total change in the loadings) for the consumer/producer prices and non-household balance sheet indicators (in the macro panel), as well as for exchange rates and commodity prices (in the financial panel). The supLM test results show strong evidence that approximately more than 90% of the loadings of the CF related to the individual series in the following categories change due to the GM: interest rates and stock market return indices in monthly financial panel, as well as National Income and Product Accounts (NIPA), IP, Employment, Housing, Inventories, Orders and Sales, Household Balance Sheet, and Consumer Expectations in the quarterly macro panel. Similarly, the correlation of the loadings of the CF in these two regimes, marked by the GM, is quite small, for both the HF (0.09) and LF (0.12) series loadings. Last but not least, the results on the structural break analysis and the percentage changes in the loadings of different series categories are the same whether we apply the PCA first or last approach. 

The time series behavior of the estimated CF during the pre- and post-GM as well as the corresponding full sample CF is presented in Figure 3. The dashed and dotted lines refer to the CF in the aforementioned regimes vis-a`-vis the solid line which refers to the full sample CF. The CFs in Figure 3 present at least three interesting features of the macro–finance factor. First, there is a shift in the mean of the estimated PCs in the two regimes and ignoring the break seems to overestimate the mean of the full sample CF in the early 1960s and underestimate it in the mid-1980s, as shown by comparing the solid, dashed, and dotted lines representing the CFs in the three periods. Interpreting the PCs in Figure 3 as the CFs we find that the GM has caused an increase in the mean of this factor, conditional on the two regimes, as shown by the relatively higher mean during the mid-1980s until the early 2000 (compared to the mean of the CF shown by the dashed line). Second, the CF in the post-GM period has a strong cyclical behavior (vis-a`-vis that in the first regime), suggesting that during the recent period the CF is dominated by the behavior of business cycle macro series as well as financial cycle-related series, as opposed to that of financial asset returns series (such as FX and stock market returns). Hence, our analysis provides additional and complementary evidence in the literature related to the GM structural break in the loadings of factor models, demonstrating how this has affected the loadings of the U.S. CF as well as the inference and behavior of this common component, while allowing us to study the behavior of group-specific (financial or macro) factors jointly. Third, we observe that during the U.S. NBER recession dates marked by the grey areas in Figure 3, the CF in most cases exhibits relative peaks associated, for example, with the recent global financial crisis in 2007–2008, the dotcom bubble in 2001, the banking strains in early 1990s, and the two oil crises in the mid-1970s and early 1980s, followed by downturns after each crisis/recession. In Figure 4, we relate our CF during the post-GM period with the U.S. business cycle and financial cycle of Drehmann, Borio, and Tsatsaronis (2012) and observe that our CF is dominated by long cycles similar to those of the financial cycle in the 1980s and during 2000– 2017.[15] The financial cycle has 0.45 correlation with the CF in the post-GM regime as 

15 The Drehmann, Borio, and Tsatsaronis (2012) financial cycle is a frequency-based (band-pass) filter capturing medium-term cycles using five financial variables: credit to private and non-financial 

Journal of Financial Econometrics 

606 

Figure 3 Common factor (CF) and NBER recessions during the full period (1963m07–2017m12) and during the pre- and post-GM (1963m07–1983m12 and 1986m01–2017m12, respectively) using the PCA last approach. 

Figure 4 The Business Cycle (BusC), the Financial Cycle (FinC), and the CF during the post-GM period. 

opposed to the business cycle with which correlation is very low, that is, 0.04 (reported later in the last two rows of Table 5). 

The changing structure of the estimated macro–finance common factor in the two regimes is further investigated by examining the different categories that drive the CFs, as well as the HFFs, LFFs, and CFFs, during the two regimes. The categories of financial and macro variables and their R[2] are reported in Table 6. Further details of the specific 

sector, the ratio of credit to GDP, equity prices, residential property prices, and an index of aggregate asset prices including residential and commercial property and equity prices. Similarly, the business cycle is a band-pass filter capturing fluctuations in real GDP over a period of one to eight years. 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

607 

|Panel A: Correlation matrix of quarterly CF, HFFs, LFFs from mixed-frequencies group factor model and the CFF with other factors and variables in the pre-GM period|Mixed-frequency group factors<br>CFFs<br>CF1<br>HF1<br>HF2<br>HF3<br>HF4<br>HF5<br>LF1<br>LF2<br>LF3<br>LF4<br>CFF1<br>CFF2<br>CFF3<br>CFF4<br>CFF5<br>CFF6<br>CFF7|GDP<br>0.52<br>0.20<br>�0.26<br>0.06<br>0.01<br>�0.11<br>0.55<br>�0.34<br>�0.18<br>0.35<br>�0.53<br>�0.27<br>0.46<br>�0.07<br>�0.15<br>0.15<br>�0.03<br>RealCons<br>0.66<br>0.09<br>�0.09<br>0.05<br>0.11<br>0.03<br>0.13<br>�0.18<br>�0.17<br>�0.08<br>�0.65<br>0.01<br>0.32<br>0.06<br>�0.05<br>�0.03<br>�0.03<br>Baa-Aaa<br>�0.35<br>�0.26<br>0.45<br>�0.08<br>�0.19<br>0.24<br>�0.30<br>0.43<br>�0.03<br>0.28<br>0.28<br>0.32<br>�0.51<br>�0.12<br>�0.07<br>�0.11<br>0.01<br>ADS<br>0.61<br>0.17<br>�0.27<br>0.08<br>0.00<br>�0.23<br>0.39<br>�0.20<br>�0.07<br>�0.14<br>�0.56<br>�0.20<br>0.44<br>�0.09<br>�0.11<br>0.14<br>0.02<br>CFNAI<br>0.56<br>0.18<br>�0.32<br>0.22<br>�0.01<br>�0.20<br>0.52<br>�0.26<br>0.06<br>�0.27<br>�0.54<br>�0.27<br>0.49<br>�0.22<br>�0.03<br>0.12<br>0.05<br>NFCI<br>�0.90<br>0.19<br>0.25<br>�0.33<br>�0.04<br>0.21<br>�0.15<br>0.20<br>0.00<br>0.12<br>0.76<br>�0.15<br>�0.58<br>0.28<br>�0.05<br>�0.07<br>0.20<br>GZ_SPRD<br>�0.49<br>�0.14<br>0.48<br>�0.10<br>0.44<br>0.20<br>�0.47<br>�0.03<br>0.04<br>0.17<br>0.37<br>0.30<br>�0.43<br>0.40<br>0.45<br>0.02<br>�0.14<br>RM_RF<br>0.35<br>0.02<br>�0.36<br>�0.03<br>0.16<br>0.04<br>�0.03<br>�0.40<br>0.05<br>�0.03<br>�0.21<br>�0.01<br>0.45<br>0.20<br>0.00<br>�0.09<br>�0.01<br>SMB<br>0.11<br>0.17<br>�0.33<br>0.11<br>0.19<br>�0.03<br>0.15<br>�0.25<br>0.11<br>0.04<br>�0.06<br>�0.22<br>0.32<br>0.10<br>0.15<br>�0.02<br>�0.03<br>HML<br>�0.04<br>�0.07<br>0.09<br>0.11<br>�0.04<br>�0.28<br>�0.01<br>0.08<br>�0.15<br>�0.21<br>0.03<br>0.04<br>�0.06<br>�0.19<br>0.06<br>0.18<br>0.07<br>UMD<br>�0.08<br>0.02<br>�0.05<br>�0.02<br>�0.22<br>0.05<br>0.07<br>0.12<br>0.19<br>0.01<br>0.10<br>�0.08<br>�0.05<br>�0.12<br>�0.15<br>�0.09<br>0.00<br>FinC<br>0.13<br>0.34<br>0.23<br>0.33<br>�0.41<br>0.18<br>0.21<br>0.50<br>0.02<br>�0.12<br>�0.30<br>�0.23<br>�0.32<br>�0.40<br>�0.04<br>�0.37<br>�0.13<br>BusC<br>�0.52<br>0.46<br>0.11<br>0.09<br>�0.56<br>�0.11<br>0.34<br>0.63<br>0.02<br>�0.13<br>0.37<br>�0.51<br>�0.48<br>�0.38<br>�0.25<br>�0.12<br>0.03|
|---|---|---|



Journal of Financial Econometrics 

608 

|Panel B: Correlation matrix of quarterly CF, HFs, LFs from mixed-frequencies factor model and the CFFs with other factors and variables in the post-GM period|Mixed-frequency group factors<br>CFFs<br>CF1<br>HF1<br>HF2<br>HF3<br>HF4<br>HF5<br>HF6<br>HF7<br>HF8<br>LF1<br>LF2<br>LF3<br>LF4<br>LF5<br>CFF1<br>CFF2<br>CFF3<br>CFF4<br>CFF5<br>CFF6<br>CFF7<br>CFF8<br>CFF9|GDP<br>0.30<br>0.16<br>�0.51<br>0.02<br>�0.10 �0.13<br>0.00<br>0.18<br>0.06<br>�0.70 �0.12 �0.38 �0.18<br>0.21<br>�0.74<br>0.02<br>0.01<br>0.05<br>0.10<br>�0.05 �0.12<br>0.20<br>0.03<br>RealCons<br>0.46<br>0.12<br>�0.39 �0.08<br>0.06<br>�0.12 �0.07<br>0.11<br>0.08<br>�0.51<br>0.00<br>�0.08 �0.25 �0.07 �0.66 �0.25<br>0.03<br>�0.03 �0.02 �0.09 �0.07<br>0.07<br>0.13<br>Baa-Aaa<br>0.05<br>0.11<br>0.45<br>0.07<br>0.24<br>0.06<br>�0.18 �0.23<br>0.12<br>0.24<br>0.41<br>0.34<br>�0.06<br>0.03<br>0.29<br>�0.20<br>0.25<br>�0.35 �0.15 �0.04 �0.12 �0.26<br>0.09<br>logVIX<br>0.02<br>�0.13<br>0.65<br>�0.06<br>0.19<br>0.10<br>0.27<br>0.13<br>0.22<br>0.49<br>0.00<br>�0.08 �0.03 �0.08<br>0.57<br>�0.26<br>0.08<br>�0.07 �0.08 �0.09<br>0.04<br>0.38<br>0.14<br>VRP<br>0.08<br>�0.20 �0.10 �0.11 �0.09<br>0.38<br>0.04<br>0.15<br>0.09<br>�0.05<br>0.00<br>�0.29 �0.03 �0.08 �0.05 �0.10 �0.22<br>0.20<br>�0.01<br>0.25<br>�0.27<br>0.19<br>0.04<br>ETF_iSHARES �0.18 �0.16 �0.75<br>0.16<br>�0.33<br>0.05<br>0.18<br>0.14<br>�0.05 �0.46 �0.39 �0.22 �0.06<br>0.00<br>�0.54<br>0.45<br>�0.45<br>0.27<br>0.16<br>0.31<br>0.17<br>0.14<br>�0.02<br>ADS<br>0.18<br>0.10<br>�0.65<br>0.05<br>�0.17 �0.16 �0.04<br>0.24<br>�0.03 �0.80 �0.18 �0.20 �0.03 �0.04 �0.79<br>0.18<br>�0.11<br>0.07<br>0.15<br>�0.05 �0.12<br>0.18<br>0.03<br>CFNAI<br>0.20<br>0.08<br>�0.61<br>0.08<br>�0.20 �0.27 �0.06<br>0.20<br>�0.03 �0.81 �0.15 �0.12 �0.01 �0.06 �0.79<br>0.17<br>�0.11<br>0.00<br>0.21<br>�0.12 �0.09<br>0.12<br>�0.01<br>NFCI<br>�0.02<br>0.08<br>0.72<br>0.15<br>�0.03<br>0.42<br>0.21<br>�0.06<br>0.14<br>0.76<br>0.00<br>0.01<br>0.18<br>�0.03<br>0.75<br>�0.18<br>0.30<br>�0.09<br>0.06<br>0.35<br>0.02<br>0.20<br>0.06<br>GZ_SPRD<br>�0.35<br>0.01<br>0.68<br>�0.12<br>0.10<br>0.17<br>0.14<br>�0.21<br>0.15<br>0.70<br>0.09<br>0.08<br>�0.11<br>0.03<br>0.82<br>�0.02<br>0.19<br>0.06<br>�0.12 �0.01<br>0.13<br>�0.10<br>0.11<br>SKEW<br>�0.45<br>0.07<br>�0.17<br>0.18<br>0.07<br>�0.18 �0.07 �0.01<br>0.46<br>�0.16<br>0.07<br>0.21<br>�0.12<br>0.03<br>�0.02<br>0.45<br>�0.04 �0.10 �0.14 �0.10<br>0.09<br>�0.25<br>0.45<br>logSKEW<br>�0.45<br>0.07<br>�0.17<br>0.18<br>0.07<br>�0.18 �0.07 �0.01<br>0.46<br>�0.16<br>0.07<br>0.21<br>�0.12<br>0.02<br>�0.01<br>0.45<br>�0.04 �0.10 �0.13 �0.09<br>0.09<br>�0.24<br>0.45<br>RM_RF<br>0.01<br>0.03<br>�0.25<br>0.09<br>0.03<br>�0.20<br>0.03<br>0.19<br>�0.04 �0.37 �0.07 �0.14<br>0.11<br>�0.10 �0.30<br>0.16<br>�0.06 �0.04<br>0.02<br>�0.15 �0.03<br>0.19<br>�0.05<br>SMB<br>�0.10<br>0.21<br>0.03<br>�0.27 �0.05 �0.13<br>0.14<br>0.07<br>�0.06 �0.01 �0.16 �0.28<br>0.04<br>0.10<br>0.01<br>0.05<br>0.20<br>0.29<br>0.03<br>�0.23<br>0.05<br>0.12<br>�0.12<br>HML<br>�0.05 �0.10 �0.04 �0.19 �0.02 �0.02 �0.07<br>0.10<br>�0.01 �0.05 �0.02 �0.20<br>0.03<br>0.01<br>�0.02 �0.01 �0.11<br>0.18<br>0.00<br>�0.13 �0.13<br>0.04<br>�0.13<br>UMD<br>0.12<br>�0.14<br>0.10<br>0.03<br>0.12<br>0.03<br>0.02<br>�0.09 �0.11<br>0.09<br>0.11<br>0.21<br>�0.11 �0.07<br>0.06<br>�0.17 �0.10 �0.16 �0.08<br>0.02<br>0.04<br>�0.04 �0.01<br>FinC<br>0.45<br>�0.03<br>0.14<br>0.05<br>�0.17<br>0.06<br>0.17<br>�0.12 �0.04<br>0.34<br>�0.04 �0.03<br>0.27<br>0.01<br>0.06<br>�0.42<br>0.07<br>�0.05<br>0.24<br>0.23<br>0.16<br>0.04<br>�0.25<br>BusC<br>�0.04 �0.08<br>0.19<br>0.26<br>0.13<br>�0.20 �0.06 �0.26 �0.09<br>0.10<br>0.19<br>0.51<br>�0.13<br>0.08<br>0.17<br>0.01<br>�0.03 �0.42 �0.02 �0.08<br>0.19<br>�0.24 �0.02|Notes: The quarterly variables used in the correlation matrices are Real GDP growth (GDP), Real Consumption growth (RealCons), Moody’s default spread (Baa-Aaa), VIX<br>(logVIX), VRP, ETF iShares Core S&P500 (ETF_iSHARES), the Aruoba, Diebold, and Scotti (2009) index (ADS), the Chicago Fed National Activity Index (CFNAI), the NFCI, the<br>Gilchrist and Zakrajsek (2012) spread (GZ_SPRD), the Amaya et al. (2015) realized skewness (SKEW and logSKEW), the Fama–French factors (Excess market returns [RM_RF],<br>SMB, HML, and UMD) and theDrehmann, Borio, and Tsatsaronis (2012)U.S. Financial Cycle (FinC) and Business Cycle (BusC) indicators. Pairwise correlations are reported for all<br>variables for the pre- and post-GM, except the following variables for the subperiods in the parenthesis: CFNAI(1967q1), NFCI (pre: 1971q1), and GZ_SPDR (pre: 1973q1–1983q4).<br>Bold values indicate the maximum correlation of each factor with the corresponding variable in the frst column.<br>Downloaded from https://academic.oup.com/jfec/article/18/3/585/5909329 by Eastman Dental Institute user on 20 May 2026|
|---|---|---|---|



Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

609 

Table 6 MFF (CF, HFF, and LFF) and CFF and their R[2] with alternative variable categories 

|Panel A: Pre-GM Factors<br>Factors<br>R2<br>Category of variables|Panel B: Post-GM Factors|
|---|---|
||Factors<br>R2<br>Category of variables|
|CF<br>0.42–0.85<br>Interest rates<br>0.59<br>Stock markets: VXO<br>0.28–0.49<br>Commodities spreads<br>0.61<br>Consumer Expectations<br>0.40–0.56<br>Non-Household Balance Sheets<br>0.29–0.50<br>Money and Credit<br>0.27–0.38<br>NIPA<br>0.32–0.37<br>Earnings and Productivity<br>0.29–0.32<br>Household Balance Sheets<br>0.29<br>Employment<br>HFF1<br>0.35–0.52<br>Interest rates<br>0.36–0.45<br>Stock Markets<br>0.42<br>IP<br>0.34<br>Employment<br>0.26<br>Prices<br>HFF2<br>0.25–0.44<br>Commodities spreads,<br>Exchange rates<br>0.26–0.29<br>Interest rates<br>0.28<br>Employment<br>HFF3<br>0.37–0.45<br>Interest rates<br>0.30<br>Exchange rates<br>0.28<br>Household Balance Sheets<br>HFF4<br>0.26–0.31<br>Interest rates, Exchange rates<br>HFF5<br>0.44–0.46<br>Stock Markets<br>0.30<br>Interest rates<br>LFF1<br>0.25–0.36<br>Interest rates<br>0.26<br>Stock markets<br>0.53–0.76<br>Employment, IP<br>0.56<br>NIPA<br>LFF2<br>0.29<br>Interest rates<br>0.31–0.46<br>IP<br>0.27–0.42<br>Employment<br>0.31–0.37<br>NIPA<br>0.26–0.36<br>Inventories, orders, and sales<br>0.31<br>Non-Household Balance Sheets<br>0.26–0.31<br>Housing<br>LFF3<br>0.25–0.66<br>Prices<br>LFF4<br>0.26–0.50<br>Prices, earnings, and productivity|CF<br>0.52–0.64<br>Commodities spreads<br>0.30–0.46<br>Interest rates<br>0.28–0.56<br>Employment<br>0.55<br>IP<br>0.37<br>Household Balance Sheets<br>0.28–0.37<br>NIPA<br>0.26–0.36<br>Money and Credit<br>0.36<br>Consumer Expectations<br>HFF1<br>0.28–0.81<br>Interest rates<br>HFF2<br>0.34–0.55<br>Stock Markets<br>0.32–0.42<br>Exchange rates<br>0.26–0.34<br>Interest rates<br>0.27–0.58<br>Household Balance Sheets<br>0.36<br>Inventories, orders, and sales<br>0.26–0.30<br>NIPA<br>0.26<br>Employment<br>0.25<br>Housing<br>HFF3<br>0.27–0.46<br>Commodities spreads<br>0.26–0.37<br>Interest rates<br>0.38<br>Money and Credit<br>0.32<br>Inventories, orders, and sales<br>HFF4<br>0.26–0.62<br>Exchange rates<br>HFF5<br>0.26–0.42<br>Stock Markets<br>0.29–0.34<br>Exchange rates<br>HFF6<br>0.37–0.52<br>Interest rates<br>HFF8<br>0.26–0.28<br>Commodities spreads<br>LFF1<br>0.34<br>Interest rates<br>0.34<br>Stock Markets<br>0.66–0.83<br>Employment<br>0.72<br>NIPA<br>0.62–0.71<br>IP<br>0.67<br>Inventories, orders, and sales<br>LFF2<br>0.28–0.81<br>Prices<br>LFF3<br>0.48<br>Money and Credit<br>0.45<br>Earnings and Productivity<br>0.31<br>Inventories, orders, and sales<br>LFF4<br>0.26<br>Money and Credit<br>0.25–0.26<br>NIPA<br>LFF5<br>0.61–0.71<br>Earnings and Productivity|



Journal of Financial Econometrics 

610 

variables in each category can be found in Table OA.7 in Online Appendix (with the corresponding acronyms for each variable used to extract the factors). Focusing on the CFs results reported in the top of Panels A and B in Table 6, the evidence suggests that the CF loads on three main financial categories during the pre-GM regime, namely interest rates spreads (both government and corporate default spreads) with R[2] ¼ 0.42–0.85, commodities spreads (the difference between future and spot prices) with R[2] ¼ 0.28–0.49 and theVXO with R[2] ¼ 0.59.[16] In contrast, in the post-GM, the CF is no longer driven by the VXO (and any other stock market indicators). In fact, the R[2] of the regression of the CF and VXO in the second regime drops to 0.01. Our group factor model reveals that in the post-GM, the VXO instead drives the second HF (monthly) financial factor, HFF2, with R[2] ¼ 0.55, as shown in Table OA.7, Panel B. Moreover, interest rates spreads while being one of the main drivers of the CF in both regimes, their R[2] becomes weaker in the post-GM period with R[2] ¼ 0.30–0.46, while commodities spreads are still highly correlated with the CF in the post-GM with R[2] ¼ 0.52–0.64. These results further explain the changing role of the drivers of the CF, which in the last four decades, was mainly driven by commodities spreads and interest rates and not by the VXO or any other stock market indices. We find that the main drivers of the macro–finance CF are interest rates and credit spread factors (also found by Gilchrist and Zakrajsek, 2012 for the U.S. economic activity), as well as commodities spreads and returns (also found by Gospodinov and Ng, 2013 for explaining the U.S. inflation and by Chaise, Ferrara, and Giannone, 2017 for global economic activity). These relationships of the CF with specific variables are further analyzed in the next subsection using dynamic partial correlations in a predictive context. Hence, we will investigate the role of our CF in Granger causing as well forecasting out of sample key financial and macro variables (including the VIX). 

Turning to the LF quarterly macro variables, we find that many different categories drive the CF. In the pre-GM regime, the CF is driven by variables in the following categories ranked in terms of the higher R[2] first: Consumer Expectations (R[2] ¼ 0.61), nonHousehold Balance Sheets (R[2] ¼ 0.40–0.56), Money and Credit (R[2] ¼ 0.29–0.50), National Income and Product Accounts (R[2] ¼ 0.27–0.38), Earnings and Productivity (R[2] ¼ 0.32–0.37), Household Balance Sheets (R[2] ¼ 0.29–0.32), and Employment (R[2] ¼ 0.29). While in the post-GM, the aforementioned variable categories are still important with similar R[2] , the non-Household Balance Sheets as well as Earnings and Productivity, are no longer correlated with the CF. Instead the Industrial Production (namely Capacity Utilization: Manufacturing with R[2] ¼ 0.55) becomes an important driver of the CF in the post-GM and the role of the Employment category increases with R[2] ¼ 0.28–0.56. 

Last but not least, we obtain the correlation of the CF with some key economic and financial variables which we will evaluate in terms of forecasting, as well as with other wellknown factors in the literature in the two regimes. Table 5 shows that the correlation of the CF with real GDP and consumption growth is higher in the pre-GM period rather than in the post-GM period (in Panels A and B, respectively). The same applies for the correlation 

- 16 For the full sample factor estimation, we consider the CBOE S&P100 Volatility Index (VXO) due to the longer historical sample since the 1960s. In the post-GM period, we examine the role of the factors in predicting the VIX which is not only a broader index (referring to the S&P500) but also a benchmark indicator in the VRP. Note that in the post-GM the correlation of the VXO and VIX is 0.97. 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

611 

between the CF with the ADS index or CFNAI, for which their correlation drops below one-third compared to that in the first regime. More importantly, while in the first regime the CF is highly correlated with the financial factors and indicators, for example, the NFCI (0.90), Baa-Aaa (0.35), excess stock market returns (0.35), their correlation with the CF in the second regime drops to 0.02, 0.05, and 0.01, respectively. 

Naturally, we wish to investigate how our Mixed-Frequency Group Factors (MFFs), that is, the CF, the HFFs, and the LFFs, compare to the traditional approach which employs aggregated (quarterly) data and pools the macro and financial panels to extract the CFFs from a single panel. First, we find evidence consistent with the literature above, that the loadings of the CFFs also exhibit a break associated with the GM. Evidence from the LM (resp. supLM) test in Table 4 reveals that using all the CFFs chosen by the ICp2 criterion, there is overwhelming evidence of a break in 90% (resp. 97%) of the loadings of all the series in the panel (both the macro and financial) in the mid-1980s. However, in order to compare the results derived from our CF, we focus on the first and second CFFs (CFF1 and CFF2 or both together), which have the highest correlation with the CF in pre- and postbreak regimes. This result is reported in Table 7 (in the first column of Panels A and B), where the CF is highly correlated with the CFF1 (0.90) in the pre-GM regime and with the CFF2 (0.82) in the post-GM regime. The supLM, based on Table 4, yields very similar results whether using the CF or CFF2 or both CFF1 and CFF2 with regard to the total percentage of loadings changing, whereas the CFF2 also provides closer results to those of the CF when it comes to the various variable category loadings changes (as shown, for instance, by the consumer expectations category) as opposed to CFF1. Last, applying the LM-type tests to all CFFs or all the MFFs (CF, HFFs, and LFFs) selected by the ICp2, we find that all loadings change in almost all categories. Our results suggest that focusing on the CF loading change point tests we are able to identify more heterogeneity in the change point of the loadings of different variable categories that drive the macro–finance factor. 

The relationship of the CFFs and mixed-frequency group factors as well as key macro and financial variables is further analyzed in Tables 5 and 7. Table 7 shows that the ICp2 criterion selects a larger number of factors (HFF, LFF, and CFF) in the post-GM period rather than in the pre-GM period. As expected, the CF, LFFs, and HFFs are highly correlated with different CFFs in the two subperiods. For instance, in the pre-GM, the first CFF (CFF1) is highly correlated with the CF and the second CFF (CFF2) with both HFF1 and LFF1. In contrast, in the post-GM, CFF1 is correlated with HFF2 and LFF1 whereas CFF2 with just CF. These results suggest that while extracting factors from the mixed-frequency group factor model it is possible to identify and label common versus group-specific factors even in different regimes, whereas, this is less obvious in the CFF model. Hence, in many cases, it is difficult to isolate what is the driving group of the CFFs. Turning to Table 5, we find that in both subperiods while CFF1 is highly correlated with real GDP, Consumption growth, the CFNAI, and the ADS index, in the post-GM period CFF1 becomes highly correlated with NFCI and GZ_spread as opposed to the pre-GM period. 

## 3.3 Predictive Evidence 

In this subsection, we investigate the role of our estimated mixed-frequency group factors using IS and OOS predictive regression models in explaining and forecasting key macro and financial variables, namely the real GDP and Consumption growth, the Moody’s Baa- 

Journal of Financial Econometrics 

612 

|Panel A: Correlation matrix of quarterly CF, HFFs, LFFs from mixed-frequencies group factor model and the CFFs in the pre-GM, 1963q3–1983q4.|Mixed-frequency group factors<br>CF<br>HFF1<br>HFF2<br>HFF3<br>HFF4<br>HFF5<br>LFF1<br>LFF2<br>LFF3<br>LFF4|Common frequency<br>factors<br>CFF1<br>0.90<br>0.26<br>0.28<br>0.09<br>0.08<br>0.00<br>0.17<br>0.15<br>0.03<br>0.03<br>CFF2<br>0.19<br>0.88<br>0.30<br>0.09<br>0.09<br>0.17<br>0.79<br>0.06<br>0.05<br>0.05<br>CFF3<br>0.29<br>0.26<br>0.86<br>0.14<br>0.21<br>0.01<br>0.18<br>0.72<br>0.06<br>0.14<br>CFF4<br>0.00<br>0.22<br>0.06<br>0.67<br>0.60<br>0.29<br>0.32<br>0.35<br>0.03<br>0.19<br>CFF5<br>0.19<br>0.06<br>0.18<br>0.67<br>0.68<br>0.04<br>0.04<br>0.24<br>0.23<br>0.13<br>CFF6<br>0.04<br>0.14<br>0.13<br>0.24<br>0.30<br>0.84<br>0.31<br>0.02<br>0.03<br>0.14<br>CFF7<br>0.05<br>0.01<br>0.05<br>0.00<br>0.03<br>0.07<br>0.01<br>0.09<br>0.14<br>0.22|Panel B: Correlation matrix of quarterly CF, HFFs, LFFs from mixed-frequencies factor model and the CFFs in the post-GM, 1986q1–2017q4|Mixed-frequency factors<br>CF<br>HFF1<br>HFF2<br>HFF3<br>HFF4<br>HFF5<br>HFF6<br>HFF7<br>HFF8<br>LFF1<br>LFF2<br>LFF3 LFF4 LFF5|Common frequency<br>factors<br>CFF1<br>0.41<br>0.23<br>0.81<br>0.04<br>0.02<br>0.20<br>0.11<br>0.09<br>0.01<br>0.80<br>0.10<br>0.08<br>0.12<br>0.05<br>CFF2<br>0.82<br>0.20<br>0.28<br>0.37<br>0.14<br>0.11<br>0.04<br>0.12<br>0.01<br>0.39<br>0.09<br>0.10<br>0.10<br>0.06<br>CFF3<br>0.09<br>0.95<br>0.29<br>0.05<br>0.01<br>0.02<br>0.00<br>0.03<br>0.00<br>0.10<br>0.02<br>0.08<br>0.20<br>0.15<br>CFF4<br>0.23<br>0.06<br>0.25<br>0.80<br>0.31<br>0.25<br>0.18<br>0.04<br>0.00<br>0.15<br>0.36<br>0.61<br>0.15<br>0.06<br>CFF5<br>0.19<br>0.05<br>0.20<br>0.16<br>0.90<br>0.24<br>0.02<br>0.01<br>0.02<br>0.10<br>0.34<br>0.05<br>0.41<br>0.02<br>CFF6<br>0.13<br>0.04<br>0.19<br>0.39<br>0.18<br>0.82<br>0.08<br>0.20<br>0.01<br>0.24<br>0.10<br>0.03<br>0.04<br>0.00<br>CFF7<br>0.03<br>0.01<br>0.12<br>0.08<br>0.09<br>0.32<br>0.58<br>0.54<br>0.05<br>0.19<br>0.54<br>0.35<br>0.22<br>0.13<br>CFF8<br>0.16<br>0.01<br>0.08<br>0.13<br>0.09<br>0.08<br>0.61<br>0.67<br>0.08<br>0.06<br>0.28<br>0.26<br>0.14<br>0.11<br>CFF9<br>0.00<br>0.00<br>0.04<br>0.01<br>0.03<br>0.05<br>0.06<br>0.22<br>0.72<br>0.03<br>0.14<br>0.25<br>0.49<br>0.12|(continued)|
|---|---|---|---|---|---|---|



Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

613 

|Panel C: Correlation matrix of quarterly CF, HFFs, LFFs from mixed-frequencies factor model and the CFFs during the entire period 1963q3–2017q4|Mixed-frequency factors<br>CF1<br>HFF1<br>HFF2<br>HFF3<br>HFF4<br>HFF5<br>HFF6<br>HFF7<br>LFF1<br>LFF2<br>LFF3<br>LFF4<br>LFF5<br>LFF6<br>LFF7|Common frequency<br>factors<br>CFF1<br>0.76<br>0.22<br>0.52<br>0.15<br>0.05<br>0.10<br>0.14<br>0.01<br>0.50<br>0.03<br>0.10<br>0.03<br>0.00<br>0.01<br>0.07<br>CFF2<br>0.58<br>0.16<br>0.63<br>0.13<br>0.08<br>0.21<br>0.17<br>0.19<br>0.73<br>0.02<br>0.10<br>0.05<br>0.06<br>0.06<br>0.01<br>CFF3<br>0.05<br>0.92<br>0.35<br>0.01<br>0.11<br>0.02<br>0.03<br>0.08<br>0.08<br>0.26<br>0.56<br>0.26<br>0.02<br>0.08<br>0.01<br>CFF4<br>0.04<br>0.14<br>0.30<br>0.90<br>0.08<br>0.14<br>0.14<br>0.12<br>0.17<br>0.12<br>0.23<br>0.18<br>0.16<br>0.25<br>0.30<br>CFF5<br>0.02<br>0.17<br>0.08<br>0.14<br>0.94<br>0.11<br>0.09<br>0.04<br>0.10<br>0.40<br>0.17<br>0.02<br>0.04<br>0.12<br>0.04<br>CFF6<br>0.22<br>0.06<br>0.10<br>0.22<br>0.04<br>0.92<br>0.17<br>0.07<br>0.02<br>0.04<br>0.03<br>0.05<br>0.24<br>0.15<br>0.30<br>CFF7<br>0.04<br>0.14<br>0.25<br>0.26<br>0.22<br>0.20<br>0.70<br>0.37<br>0.30<br>0.22<br>0.22<br>0.01<br>0.12<br>0.06<br>0.09<br>CFF8<br>0.14<br>0.04<br>0.01<br>0.09<br>0.04<br>0.10<br>0.46<br>0.77<br>0.00<br>0.39<br>0.48<br>0.11<br>0.02<br>0.04<br>0.05<br>CFF9<br>0.07<br>0.08<br>0.10<br>0.04<br>0.17<br>0.03<br>0.31<br>0.09<br>0.16<br>0.53<br>0.02<br>0.04<br>0.09<br>0.02<br>0.07<br>CFF10<br>0.02<br>0.00<br>0.10<br>0.02<br>0.07<br>0.03<br>0.20<br>0.21<br>0.14<br>0.42<br>0.20<br>0.55<br>0.09<br>0.23<br>0.10|Bold values indicate the maximum correlation of each mixed-frequency factor with the corresponding common frequency factor (CFF).|
|---|---|---|---|



Journal of Financial Econometrics 

614 

Aaa default spread, the VIX, the VRP, and the ETF iShares Core S&P500 returns. We focus at forecasting these variables at quarterly frequency given that in many cases the quarterly frequency is the frequency of interest of policy makers as well as for comparison purposes across all variables. We consider traditional linear factor augmented distributed lag (FADL) models when all variables and factors are at the same, low (quarterly) frequency estimated by least squares (referred to as Linear-LS). Among these specifications, we include the models with the traditional CFFs considered in the literature. Additionally, we estimate the corresponding FADL-MIDAS models by nonlinear least squares (referred to as MIDAS-NLS), given that predictors/factors are available at higher frequency (monthly) than the dependent variable and some MIDAS weighting schemes can be estimated by NLS. Alternative HF weighting polynomials (the Almon and the Step) are used for estimating the FADL-MIDAS models. The predictive role and information content of our factors is also assessed relative to other related and established U.S. factors in the literature, such as the CFNAI, the NFCI, the ADS index, the GZ_spread, and the four Fama–French factors, excess market returns (RM-RF), small-minus-big (SMB), high-minus-low (HML), and momentum (UMD). 

## 3.3.1 IS predictive evidence 

The IS linear and MIDAS predictive models are presented in Tables 8 and 9 and include our MFFs extracted from the mixed-frequency group factor model and/or the aforementioned well-known factors in the literature as well as the traditional CFFs. More precisely in Table 8 we report the results for real GDP and Consumption growth as well as the corporate bonds default spread for the two subperiods marked by the GM, while in Table 9 we report the results for the VIX, VRP, and ETF returns for the more recent period, due to the shorter data sample available. Given the large model space involved in estimating the above models for all predictors, lag lengths, and HF weighting polynomials, we focus on reporting the results for those models where predictors turn out to be significant following the Bai and Ng (2008) targeted predictors approach with hard thresholding (based on the 10% significance level and the heteroskedastic and autocorrelation Newey–West standard errors). For the lag length p in these FADL type models, we consider p ¼ 1 up to four quarters and select the number of lags using theBIC (which is a consistent information criterion and selects parsimonious models—a desirable property for forecasting models). For most models reported in Tables 8 and 9, the BIC selects one lag. For each dependent variable, the FADL and FADL-MIDAS models are compared in terms of the BIC. We highlight in bold the three models with the lowest BIC values and mark with a[þ] the model that yields the lowest BIC among these. Of special interest is the predictive or Granger causal role of the CF evaluated via the significance and estimated regression coefficient of the CF (b[^] CF) which are also reported in Tables 8 and 9.[17] 

In the top panel of Table 8, we present the results of real GDP growth in the two regimes. The first column reports the alternative model specifications in each row while the 

- 17 Alternative approaches of dealing with the large model space such as alternative criteria for model selection, model averaging, shrinkage, among others, can also be pursued in this context. Although these are complementary approaches, our analysis aims at uncovering the predictive role of the common macro–finance as well as the group-specific factors in comparison to other factors and hence we consider the model selection approach. 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

615 

|Predictive model specifications<br>GDP 1963q3–1983q4<br>GDP 1986q1–2017q4<br>Targeted predictors<br>^bCF<br>BIC<br>Targeted predictors<br>^bCF<br>BIC|LD<br>–<br>�6.189<br>–<br>�7.557<br>LD, all CFFs [ICp2] in Linear-LS<br>–<br>�6.378<br>–<br>�7.558<br>LD, CFFs in Linear-LS<br>CFF:1,3,4,5<br>–<br>�6.518<br>CFF:1,2,3,5,7,8<br>–<br>�7.652<br>LD, MFFs in linear-LS<br>CF<br>0.238***<br>�6.505<br>CF, HFF4, LFF1<br>0.050***<br>�7.666<br>LD, MFFs in Almon MIDAS<br>CF, HFF6, LFF1<br>0.164***<br>�6.434<br>CF, LFF:1,5, HFF:1,5<br>0.027**<br>�7.792<br>LD, MFFs in step MIDAS<br>CF, LFF1<br>0.176**<br>�6.433<br>CF, LFF:1,5, HFF:1,5<br>0.012**<br>�7.773<br>LD, ADS, MFFs in Linear-LS<br>ADS<br>–<br>�7.216þ<br>ADS, HFF4<br>–<br>�8.067<br>LD, ADS, MFFs in Almon MIDAS<br>ADS, LFF5, HFF1<br>–<br>�7.142<br>ADS<br>–<br>�8.195<br>LD, ADS, MFFs in step MIDAS<br>ADS, CF, LFF5, HFF:1,2,3<br>0.062***<br>�7.119<br>ADS<br>–<br>�8.223þ<br>LD, CFNAI, MFFs in Linear-LS<br>CFNAI<br>–<br>�6.626<br>CF, CFNAI, HFF4, LFF1<br>–<br>�7.717<br>LD, CFNAI, MFFs in Almon MIDAS<br>CFNAI<br>–<br>�6.671<br>CFNAI, HFF5, LFF1<br>–<br>�8.101<br>LD, CFNAI, MFFs in step MIDAS<br>CFNAI, CF, LFF5, HFF:1,2,3<br>0.021***<br>�6.801<br>CFNAI, HFF5<br>–<br>�8.070<br>LD, NFCI, MFFs in Linear-LS<br>CF, HFF3<br>0.242***<br>�6.476<br>CF, LFF1<br>0.045**<br>�7.619<br>LD, NFCI, MFFs in Almon MIDAS<br>NFCI, CF, LFF:1,2, HFF:3,5,6<br>0.288***<br>�6.230<br>CF, LFF:1,5, HFF5<br>0.027**<br>�7.695<br>LD, NFCI, MFFs in step MIDAS<br>CF, LFF:1,5, HFF:1,5<br>0.232***<br>�6.322<br>CF, LFF:3,5, HFF5<br>0.035***<br>�7.547<br>LD, GZ_SPRD, MFFs in Linear-LS<br>HFF:3,6<br>–<br>�6.091<br>CF, HFF4, LFF1<br>0.050***<br>�7.666<br>LD, GZ_SPRD, MFFs in Almon MIDAS<br>CF, HFF3<br>0.154***<br>�6.496<br>CF, HFF:2,5, LFF1<br>0.033***<br>�7.766<br>LD, GZ_SPRD, MFFs in step MIDAS<br>HFF:1,6<br>–<br>�6.019<br>GZ_SPRD, LFF5, HFF6<br>–<br>�7.662<br>LD, FFs, MFFs in Linear-LS<br>CF, LFF5, HFF3<br>0.243***<br>�6.442<br>HML, UMD, RM_RF, CF,<br>LFF1, HFF:2,3,4,5<br>0.058***<br>�7.578<br>LD, FFs, MFFs in Almon MIDAS<br>CF, LFF1<br>0.166***<br>�6.483<br>RM_RF, UMD, HML, CF,<br>LFF1, HFF:2,3,5<br>0.030***<br>�7.739<br>LD, FFs, MFFs in step MIDAS<br>–<br>–<br>�6.189<br>RM_RF, HML, LFF1, HFF:1,2,5<br>–<br>�7.569|(continued)|
|---|---|---|



Journal of Financial Econometrics 

616 

|Predictive model specifications<br>RealCons 1963q3–1983q4<br>RealCons 1986q1–2017q4<br>Targeted predictors<br>^bCF<br>BIC<br>Targeted predictors<br>^bCF<br>BIC|LD<br>–<br>�7.840<br>–<br>�8.578<br>LD, all CFFs [ICp2] in Linear-LS<br>–<br>�7.922<br>–<br>�8.634<br>LD, CFFs in Linear-LS<br>CFF:1,2,3<br>–<br>�8.125<br>CFF:1,2,7,9<br>–<br>�8.775<br>LD, MFFs in Linear-LS<br>CF, HFF2<br>0.093***<br>�8.104<br>CF, HFF:4,5,7, LFF:1,3,4<br>0.057***<br>�8.768<br>LD, MFFs in Almon MIDAS<br>CF<br>0.073***<br>�8.138þ<br>CF, HFF:4,5, LFF:1,3<br>0.030***<br>�8.796<br>LD, MFFs in step MIDAS<br>–<br>–<br>–<br>LFF1, HFF3<br>–<br>8.573<br>LD, ADS, MFFs in Linear-LS<br>ADS, CF, LFF4, HFF:2,4<br>0.078***<br>�8.015<br>ADS, CF, LFF:1,3,4, HFF:4,5,7<br>0.053***<br>�8.751<br>LD, ADS, MFFs in Almon MIDAS<br>ADS<br>–<br>�7.849<br>ADS, CF, LFF:2,3, HFF:4,5<br>0.019***<br>�8.879þ<br>LD, ADS, MFFs in step MIDAS<br>ADS<br>–<br>�7.988<br>ADS, LFF1, HFF4<br>–<br>�8.725<br>LD, CFNAI, MFFs in Linear-LS<br>CFNAI, CF, LFF4, HFF:2,4,7<br>0.081***<br>�7.951<br>CF, LFF:1,3,4, HFF:4,5,7<br>0.057***<br>�8.768<br>LD, CFNAI, MFFs in Almon MIDAS<br>CFNAI, HFF4<br>–<br>�7.829<br>CFNAI, CF, LFF:2,3, HFF:4,5<br>0.017***<br>�8.875<br>LD, CFNAI, MFFs in step MIDAS<br>–<br>–<br>–<br>CFNAI, LFF:2,3, HFF4<br>–<br>�8.722<br>LD, NFCI, MFFs in Linear-LS<br>HFF2<br>–<br>�7.918<br>CF, LFF:1,3,4, HFF:4,5,7<br>0.057***<br>�8.768<br>LD, NFCI, MFFs in Almon MIDAS<br>NFCI, CF, HFF:5,7<br>0.098***<br>�7.817<br>CF, LFF1, HFF:4,5<br>0.031***<br>�8.795<br>LD, NFCI, MFFs in step MIDAS<br>CF, HFF:5,6<br>–<br>�7.972<br>LFF1<br>–<br>–<br>LD, GZ_SPRD, MFFs in Linear-LS<br>HFF7<br>–<br>�7.798<br>CF, LFF:1,3,4, HFF:4,5,7<br>0.057***<br>�8.768<br>LD, GZ_SPRD, MFFs in Almon MIDAS<br>–<br>–<br>–<br>CF, LFF:1,3, HFF:4,5<br>0.030***<br>�8.796<br>LD, GZ_SPRD, MFFs in step MIDAS<br>GZ_SPRD, LFF:4,5, HFF:3,5,6<br>–<br>�7.282<br>LFF1, HFF:3,4<br>–<br>�8.579<br>LD, FFs, MFFs in Linear-LS<br>UMD, CF, HFF7<br>0.093***<br>�7.946<br>CF, LFF:1,3,4, HFF:4,7<br>0.056***<br>�8.733<br>LD, FFs, MFFs in Almon MIDAS<br>HFF4<br>–<br>�7.810<br>CF, LFF:1,3, HFF4<br>0.031***<br>�8.752<br>LD, FFs, MFFs in step MIDAS<br>UMD<br>–<br>�7.876<br>LF1<br>–<br>–|(continued)|
|---|---|---|



Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

617 

|Predictive model specifications<br>Baa-Aaa 1963q3–1983q4<br>Baa-Aaa 1986q1–2017q4<br>Targeted predictors<br>^bCF<br>BIC<br>Targeted predictors<br>^bCF<br>BIC|LD<br>–<br>�0.201<br>–<br>�0.328<br>LD, all CFFs [ICp2] in Linear-LS<br>–<br>�0.773<br>–<br>�0.419<br>LD, CFFs in Linear-LS<br>CFF:1,4,5,6<br>–<br>�0.896<br>CFF:1,2,4,5,6<br>–<br>�0.434<br>LD, MFFs in Linear-LS<br>CF, LFF:1,3, HFF:2,4,6<br>0.054***<br>�0.917<br>LFF1, HFF:2,5<br>–<br>�0.534<br>LD, MFFs in Almon MIDAS<br>CF, HFF:1,3,4,6<br>0.042***<br>�0.636<br>LFF1, HFF:1,2,5<br>–<br>�0.854<br>LD, MFFs in step MIDAS<br>CF, LFF:2,5, HFF:1,2,3,5,6,7<br>0.024**<br>�0.816<br>HFF:1,2,3,5<br>–<br>�0.962<br>LD, ADS, MFFs in Linear-LS<br>ADS, CF, LFF:1,3, HFF:2,4,6,7<br>0.040***<br>�0.930<br>HFF:2,5<br>–<br>�0.601<br>LD, ADS, MFFs in Almon MIDAS<br>ADS, CF, HFF:1,4,6<br>0.030***<br>�0.619<br>ADS, HFF:1,2,5<br>–<br>�0.928<br>LD, ADS, MFFs in step MIDAS<br>ADS, CF, LFF:2,5, HFF:1,3,5,6,7<br>0.000***<br>�0.977þ<br>ADS, HFF:1,2,3,5,7<br>–<br>�1.062<br>LD, CFNAI, MFFs in Linear-LS<br>CFNAI, CF, LFF3, HFF:2,4,6,7<br>0.037***<br>�0.776<br>HFF:2,5<br>–<br>�0.601<br>LD, CFNAI, MFFs in Almon MIDAS<br>CFNAI, CF, LFF2, HFF:1,4,6<br>0.028***<br>�0.589<br>HFF:1,2,5<br>–<br>�0.909<br>LD, CFNAI, MFFs in step MIDAS<br>CFNAI, CF, HFF:3,4,5,6,7<br>0.006***<br>�0.794<br>CFNAI, HFF:1,2,3,5,7<br>–<br>�1.028<br>LD, NFCI, MFFs in Linear-LS<br>NFCI, LFF:2,3, HFF:2,3,4,5,7<br>–<br>�0.791<br>LFF1, HFF:2,5<br>–<br>�0.572<br>LD, NFCI, MFFs in Almon MIDAS<br>HFF4<br>–<br>�0.172<br>HFF:1,2,5<br>–<br>�0.909<br>LD, NFCI, MFFs in step MIDAS<br>NFCI, CF, HFF:1,2,3,5,6,7<br>0.048***<br>�0.377<br>NFCI, CF, HFF:1,5<br>0.004**<br>�1.227þ<br>LD, GZ_SPRD, MFFs in Linear-LS<br>CF, LFF3, HFF:2,4,6<br>0.048***<br>�0.865<br>GZ_SPRD, LFF1, HFF:2,4,5,7<br>–<br>�0.532<br>LD, GZ_SPRD, MFFs in Almon MIDAS<br>HFF:3,6,8<br>–<br>�0.078<br>GZ_SPRD, LFF1, HFF:1,2,5<br>–<br>�0.845<br>LD, GZ_SPRD, MFFs in step MIDAS<br>CF, HFF:3,4,5,6,7<br>0.025***<br>�0.689<br>GZ_SPRD, HFF:1,5<br>–<br>�1.188<br>LD, FFs, MFFs in Linear-LS<br>CF, LFF:1,3, HFF:2,4,6<br>0.054***<br>�0.917<br>LFF1, HFF7<br>–<br>�0.350<br>LD, FFs, MFFs in Almon MIDAS<br>RM_RF, SMB, CF, LFF3, HFF:2,4,7,8<br>0.040***<br>�0.535<br>LFF1, HFF:1,2,5<br>–<br>�0.891<br>LD, FFs, MFFs in step MIDAS<br>RM_RF, UMD, CF, LFF:3,5, HFF:2,3,4,5,6,7,8<br>0.037***<br>�0.755<br>UMD, HFF:1,2<br>–<br>�0.777|Notes:Bold BIC values refer to the models with the three lowest BIC for each dependent variable and the BIC values with a þ denotes the model with minimum BIC for each variable.<br>Targeted predictors are based on the Bai and Ng (2008) hard thresholding approach using 10% signifcance level, Newey–West standard errors with the Bartlett kernel and data-<br>driven bandwidth selection. The corresponding signifcance of the regression coeffcient of the CF refers to the following signifcance levels: ***1%, **5%, and *10%. The common<br>factor (CF), the HFFs, and the LFFs are estimated using the quarterly (LF) and monthly (HF) frequency macro and fnancial series panels, respectively, using the MFF model. The<br>MIDAS model step (s¼3) and Almon (d¼1) are reported given that yield parsimonious representations with low BIC. The CFFs are estimated from all the series at the quarterly LF<br>stacked in a common panel. The predictive model involves the following predictors: the lagged dependent (LD) term, the MFFs, namely the Common Factor (CF), the HFFs and<br>LFFs, the CFFs, the Aruoba, Diebold, and Scotti (2009) (ADS) index, the Chicago National Activity and Financial Conditions Indices (CFNAI and NFCI, respectively), the four<br>Fama–French (FF) factors (RM-RF, SMB, HML, UMD) andGilchrist and Zakrajsek (2012)spread (GZ_SPRD).|
|---|---|---|



Journal of Financial Econometrics 

618 

Table 9 VIX (logVIX), VRP, and ETF iShares Core S&P500 (ETF_iSHARES) predictive models BIC results: FADL Linear-LS and FADL MIDAS NLS models with alternative Factors (CFFs and MFFs) 

|Predictive model specifications|logVIX targeted predictors|^bCF|BIC|
|---|---|---|---|
||1990q1–2017q4|||
|LD||–|�1.542|
|LD, all CFFs [ICp2] in Linear-LS||–|�1.261|
|LD, CFFs in Linear-LS|CFF:2,5,6|–|�1.466|
|LD, MFFs in Linear-LS|CF, LFF5, HFF:2,3,4,5,6,7,8|0.015***|�1.386|
|LD, MFFs in Almon MIDAS|CF, LFF3, HFF:2,3,4,6,7,8|0.013***|�1.671|
|LD, MFFs in step MIDAS|LFF:3,5, HFF:2,3,5,6,7,8|–|�1.536|
|LD, ADS, MFFs in Linear-LS|CF, LFF5, HFF:2,3,4,5,6,7,8|0.015***|�1.386|
|LD, ADS, MFFs in Almon MIDAS|CF, LFF3, HFF:2,3,4,6,7,8|0.013***|�1.671|
|LD, ADS, MFFs in step MIDAS|ADS, LFF:3,5, HFF:2,5,6,7,8|–|�1.504|
|LD, CFNAI, MFFs in Linear-LS|CF, LFF5, HFF:2,3,4,5,6,7,8|0.015***|�1.386|
|LD, CFNAI, MFFs in Almon|CF, LFF3, HFF:2,3,4,6,7,8|0.013***|�1.671|
|LD, CFNAI, MFFs in step MIDAS|CFNAI, LFF:3,5, HFF:2,3,5,6,7,8|–|�1.536|
|LD, NFCI, MFFs in Linear-LS|CF, LFF5, HFF:2,3,4,5,6,7,8|0.015***|�1.386|
|LD, NFCI, MFFs in Almon MIDAS|CF, LFF:3,4, HFF:2,3,4,5,6,7,8|0.012***|�1.628|
|LD, NFCI, MFFs in step MIDAS|LFF:3,5, HFF:2,5,6,8|–|�1.606|
|LD, GZ_SPRD, MFFs in Linear-LS|CF, LFF:3,5, HFF:2,3,4,5,6,7,8|0.014**|�1.358|
|LD, GZ_SPRD, MFFs in Almon MIDAS|GZ_SPRD, CF, LFF3, HFF:2,4,6,7,8|0.019***|�1.649|
|LD, GZ_SPRD, MFFs in step MIDAS|LFF3, LFF5, HFF:2,5,6,7,8|–|�1.567|
|LD, FFs, MFFs in Linear-LS|CF, HFF:1,5,7,8|–|�1.370|
|LD, FFs, MFFs in Almon MIDAS|RM_RF, CF, LFF:3,5, HFF:1,2,4,7,8|0.005**|�1.630|
|LD, FFs, MFFs in step MIDAS|RM_RF, LFF:3,5, HFF:2,7,8|–|�1.688þ|
|LD, logSKEW, MFFs in Linear-LS|CF, HFF:2,3,4,6,7,8|0.011**|�1.373|
|LD, logSKEW, MFFs in Almon MIDAS|CF, LFF3, HFF:2,3,4,5,6,7,8|0.012***|�1.644|
|LD, logSKEW, MFFs in step MIDAS|LFF:3,5, HFF:2,5,6,7,8|–|�1.567|
|Predictive model specifcations|VRP targeted predictors|^bCF|BIC|
||1990q1–2017q4|||
|LD||–|8.288|
|LD, all CFFs [ICp2] in Linear-LS||–|8.423|
|LD, CFFs in Linear-LS|CFF:2,3,7,8,9|–|8.297|
|LD, MFFs in Linear-LS|CF, HFF:1,2,7,8|1.649**|8.343|
|LD, MFFs in Almon MIDAS|CF, HFF:1,7,8|1.103***|8.282|
|LD, MFFs in step MIDAS|HFF:1,2,3,5,7|–|8.438|
|LD, ADS, MFFs in Linear-LS|CF, HFF:1,2,3,6,7,8|2.121**|8.360|
|LD, ADS, MFFs in Almon MIDAS|ADS, CF, LFF1, HFF:1,2,3,5,7,8|0.679*|8.188|
|LD, ADS, MFFs in step MIDAS|ADS, LFF1, HFF:1,2,3,5,6|–|8.369|
|LD, CFNAI, MFFs in Linear-LS|CF, HFF:1,2,7,8|1.649**|8.343|
|LD, CFNAI, MFFs in Almon|CFNAI, CF, LFF1, HFF:1,2,5,7,8|–|8.249|
|LD, CFNAI, MFFs in step MIDAS|CFNAI, HFF:1,2,3,5,8|–|8.460|
|LD, NFCI, MFFs in Linear-LS|NFCI, CF, HFF:1,7,8|2.356***|8.260|
|LD, NFCI, MFFs in Almon MIDAS|NFCI, CF, HFF:1,5,7|1.372***|8.169þ|
|LD, NFCI, MFFs in step MIDAS|HFF:1,3,5,7|–|8.436|
|LD, GZ_SPRD, MFFs in Linear-LS|CF, HFF:1,7,8|1.370*|8.343|
|LD, GZ_SPRD, MFFs in Almon MIDAS|CF, HFF:1,7,8|1.103***|8.282|
|LD, GZ_SPRD, MFFs in step MIDAS|CF, HFF:1,2,3,5,6,7|0.239**|8.439|
|LD, FFs, MFFs in Linear-LS|CF, LFF5, HFF:3,4,5,7,8|–|8.463|
|LD, FFs, MFFs in Almon MIDAS|RM_RF, HML, CF, HFF:1,7,8|1.069***|8.177|
|LD, FFs, MFFs in step MIDAS|RM_RF, HML, HFF:1,3,7|–|8.403|
|LD, SKEW, MFFs in Linear-LS|CF, HFF:1,2,3,7,8|1.795***|8.345|
|LD, SKEW, MFFs in Almon MIDAS|CF, HFF:1,7,8|1.103***|8.282|
|LD, SKEW, MFFs in step MIDAS|CF, HFF:1,2,3,5,7|–|8.427|



(continued) 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

619 

Table 9 VIX (logVIX), VRP, and ETF iShares Core S&P500 (ETF_iSHARES) predictive models BIC results: FADL Linear-LS and FADL MIDAS NLS models with alternative Factors (CFFs and MFFs) 

|Predictive model specifications|ETF_iSHARES targeted|^bCF|BIC|
|---|---|---|---|
||predictors 2000q3–2017q4|||
|LD||–|�1.993|
|LD, all CFFs [ICp2] in Linear-LS||–|�2.035|
|LD, CFFs in Linear-LS|CFF:2,5,8|–|�1.899|
|LD, MFFs in Linear-LS|CF, HFF7|0.010***|�1.944|
|LD, MFFs in Almon MIDAS|CF, HFF:1,2,3,5|0.006***|�2.712|
|LD, MFFs in step MIDAS|CF, LFF1, HFF:2,3,5,7,8|0.000**|�3.466|
|LD, ADS, MFFs in Linear-LS|ADS, CF, HFF7|0.014***|�2.100|
|LD, ADS, MFFs in Almon MIDAS|CF, HFF:2,3,5|0.006***|�2.724|
|LD, ADS, MFFs in step MIDAS|CF, HFF:2,3,5,7,8|0.002**|�3.372|
|LD, CFNAI, MFFs in Linear-LS|CF, HFF7|0.010***|�1.944|
|LD, CFNAI, MFFs in Almon|CF, HFF:1,2,3,5|0.006***|�2.712|
|LD, CFNAI, MFFs in step MIDAS|HFF:2,3,4,5,7|–|�3.523þ|
|LD, NFCI, MFFs in Linear-LS|NFCI, HFF:1,2,3|–|�1.962|
|LD, NFCI, MFFs in Almon MIDAS|CF, HFF:1,2,3,5|0.006***|�2.712|
|LD, NFCI, MFFs in step MIDAS|CF, HFF:2,3,5,7,8|0.002**|�3.372|
|LD, GZ_SPRD, MFFs in Linear-LS|GZ_SPRD, CF, HFF7|0.014***|�1.888|
|LD, GZ_SPRD, MFFs in Almon MIDAS|CF, HFF:1,2,3,5|0.006***|�2.712|
|LD, GZ_SPRD, MFFs in step MIDAS|HFF:2,3,5,7,8|–|�3.290|
|LD, FFs, MFFs in Linear-LS|CF, HFF7|0.010***|�1.944|
|LD, FFs, MFFs in Almon MIDAS|HFF:2,3,5|–|�2.644|
|LD, FFs, MFFs in step MIDAS|RM_RF, SMB, HFF:2,4,7|–|�3.443|
|LD, logSKEW, MFFs in Linear-LS|CF, LFF2, HFF7|0.010***|�1.885|
|LD, logSKEW, MFFs in Almon MIDAS|logSKEW, HFF:1,2,3,5,7|–|�2.686|
|LD, logSKEW, MFFs in step MIDAS|HFF:2,3,5,7|–|�3.369|



Notes: Bold BIC values refer to the models with the three lowest BIC for each dependent variable and the BIC values with a[þ] denotes the model with minimum BIC for each variable. Targeted predictors are based on the Bai and Ng (2008) hard thresholding approach using 10% significance level, Newey–West standard errors with the Bartlett kernel and data-driven bandwidth selection. The corresponding significance of the regression coefficient of the CF refers to the following significance levels: ***1%, **5%, and *10%. The common factor (CF), the HFFs, and the LFFs are estimated using the quarterly (LF) and monthly (HF) frequency macro and financial series panels, respectively, using the MFF model. The MIDAS model step (s ¼ 3) and Almon (d ¼ 1) are reported given that yield parsimonious representations with low BIC. The CFFs are estimated from all the series at the quarterly LF stacked in a common panel. The predictive model involves the following predictors: the lagged dependent (LD) term, the MFFs, namely the Common Factor (CF), the HFFs and LFFs, the CFFs, the Aruoba, Diebold, and Scotti (2009) (ADS) index, the Chicago National Activity and Financial Conditions Indices (CFNAI and NFCI, respectively), the four Fama–French (FF) factors (RM-RF, SMB, HML, UMD), Gilchrist and Zakrajsek (2012) spread (GZ_SPRD) and the Amaya, Christoffersen, Jacobs, and Vasquez (2015) Realized Skewness (SKEW). 

second and fifth columns list the significant predictors/factors in each model that correspond to each of the two regimes. The corresponding BIC values for each model in the first and second regime are reported in fourth and last columns, respectively. Last but by no means least, the estimated regression coefficient of the CF and its statistical significance in the pre- and post-GM periods are also reported. There are two interesting results to note 

Journal of Financial Econometrics 

620 

about the GDP growth predictive models: first, following the targeted predictors approach, the model with the lowest BIC is a simple linear model and a MIDAS model in the first and second regimes, respectively, with just the lagged ADS index, followed by the MIDAS models which also include some of the significant LFFs and HFFs and the CF, especially in the first regime. Second, comparing the estimated predictive coefficients of the common factor in all the reported models in the pre- and post-GM regimes, we find that while it is significant in both regimes, its estimated value has dropped by at least a third in the second regime. Hence, although still statistically significant, the actual value of the predictive coefficient of the CF in explaining GDP growth has decreased in the last three decades. 

This finding also extends to the real Consumption growth models reported in the second panel, for which the estimated CF coefficient drops by a half in the recent regime. More interestingly, the results for the default spread, found in the last panel, show that the CF turns out to be significant in many models in the first regime, whereas in the second regime it turns out to lose its Granger causality role in almost all models, except in a single model with the lowest BIC. For real Consumption growth, the model with the minimum BIC is a MIDAS specification with just the lagged CF in the first regime and the CF along with the ADS, LFFs, and HFFs in the second regime. Similarly, for the default spread in the first regime the MIDAS model with the CF, HFFs as well as the ADS index and the LFFs is the model with the best fit. In the second regime, the MIDAS model with the CF, HFFs, and NFCI yields the lowest BIC for the U.S. corporate bond default rate. Summarizing Table 8 shows that while the CF Granger causes the real GDP and consumption of services and nondurable goods growth in the two regimes, its predictive estimated effect is much lower in the post-GM regime. These findings not only extend to the case of the default spread but the results from the alternative models show that the Granger causality role of the CF is much weaker in the post-GM regime relative to the pre-GM period for this spread. 

Turning to Table 9, we report the results for predictive models for the log(VIX), VRP, and the ETF iShares Core S&P500 returns during the second regime and based on data availability. Within these predictive models, we also consider the Realized Skewness (SKEW) proposed in Amaya et al. (2015) which turns out to be a significant predictor in the log specification of a model for ETF returns along with other HFFs. The reported results in Table 9 provide two broad conclusions: first, for these three key financial indicators, the models that yield the lowest BIC are MIDAS specifications, which include a subset of our MFFs along with the excess market returns for the VIX and the NFCI for the VRP. Second, even if the CF is not driven by any stock market indices (as discussed in the previous subsection) and even though in the post-GM the VXO is no longer closely related with the CF, the evidence in Table 9 shows that in the recent regime in many models the CF is a strongly significant predictor Granger causing the VIX, VRP, and ETF returns in the last three decades. Given the recent financial crisis, we add a simple dummy variable in the constant of all the AR, FADL, and FADL-MIDAS models (which takes the value one during 2008q4 and zero otherwise) and find that while this is significant for almost all models for all dependent variables (except for real consumption), it does not affect the significance of the predictive regression coefficient of the CF and the models selected by BIC. Hence, the results reported in Tables 8 and 9 are robust to excluding the recent global financial crisis. 

In comparing the CFFs in linear-LS models with our MFFs in either linear-LS or MIDAS-NLS models, we find that the MFFs perform relatively better in terms of BIC for all variables (except for real GDP growth in the pre-GM period). Comparing the model 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

621 

results in rows 2–6 in Tables 8 and 9 for each variable and regime, we find that the models with MFFs provide the best fit (in terms of BIC) when combined with MIDAS instead of linear-LS specifications especially in the second regime. Hence our empirical evidence suggests that it is the combination of the information content of the MFFs as well as their role in MIDAS predictive regressions vis-a`-vis that of the CFFs (in linear-LS models) that provides goodness of fit improvements. Yet, what is not obvious to isolate and infer in predictive models with CFFs, as opposed to those with MFFs, is the role of the CF as shown in either linear or MIDAS models with the CF. 

Summarizing, the large dimensional empirical analysis reduces the dimensionality of the data via mixed-frequency group factor models, yet we still face the large model space of alternative factors, predictors, and predictive model specifications. We find that model selection approaches favor MIDAS predictive regression models and mixed-frequency group factors as predictors of key macro and financial variables. The overall results in Tables 8 and 9 show that the lowest BIC favors MIDAS specifications with some of our mixedfrequency group factors (i.e., CF, HFFs, and LFFs) mainly for the second regime, as opposed to the traditional CFFs. Additionally, the ADS, the NFCI, and excess market returns turn out to be additional significant predictors, among the aforementioned factors for models with the lowest BIC. For instance, the ADS factor turns out to be significant in the models with the best fit (based on BIC) for the real GDP growth and the default spread in the pre-GM period and for the real Consumption growth for the post-GM period. This is an interesting finding given that both the MFFs and ADS are based on the idea of deriving factors from mixed-frequency grouped data, albeit of different sizes and types of crosssectional information. For the VIX, VRP, and ETF returns, we find that our HFFs (along with other factors such as the CF, LFF, NFCI, excess market returns) yield predictive models with the lowest BIC. 

## 3.3.2 OOS predictive evidence 

We analyze the OOS predictive ability of our factors (MFFs and CFFs) reporting in Table 10 the root mean squared errors (RMSE) ratios of linear and MIDAS models vis-a`vis the random walk (RW) model, often considered as a simple benchmark model for both macro and financial indicators. Given the evidence of structural change, we focus on evaluating the forecasting performance of the models in the more recent post-GM and longer period. Panel A refers to the results for the three variables that have the longer sample period (Real GDP, Consumption, and Baa-Aaa), whereas Panel B refers to the financial variables with the shorter sample (VIX, VRP, and ETF returns). The IS period for the models in Panel A refer to 1986q1–2001q4, while for the variables in Panel B, namely for the VIX and VRP, the IS period is 1990q1–2003q4 and for the ETF returns it is 2000q3–2007q1, due to the shorter data availability. For the factor augmented predictive models (reported in each row of Table 10), we focus on evaluating the forecasting ability of the corresponding model (in each row) with the significant predictors during the IS period, given these are more parsimonious representations than the model with all factors. For the OOS forecasting evaluation, we pursue two approaches, the fixed and the recursive sample schemes. We report the results one-quarter ahead given the sample sizes. While the fixed OOS approach is pursued in many studies for evaluating macro forecasting models, the recursive OOS approach is more realistic especially for financial data as it is not subject to the look ahead bias criticism. The MSE-F test (Gonc¸alves, McCracken, and Perron, 2017) is performed to 

Journal of Financial Econometrics 

622 

|GDP<br>RealCons<br>Baa-Aaa<br>Predictive model specifcations<br>Fixed sample<br>Recursive sample<br>Fixed sample<br>Recursive sample<br>Fixed sample<br>Recursive sample|LD<br>1.00<br>1.00<br>1.03<br>LD, all CFFs [ICp2]<br>0.88*<br>0.81*<br>0.79*<br>0.61*<br>1.15<br>0.57*<br>LD, CFFs in Linear-LS<br>0.77*<br>0.83*<br>0.55*<br>0.65*<br>1.00<br>0.59*<br>LD, MFFs in Linear-LS<br>0.82*<br>0.81*<br>0.59*<br>0.79*<br>0.89*<br>0.52*<br>LD, ADS, MFFs in Linear-LS<br>0.64*<br>0.69*<br>0.59*<br>0.72*<br>0.96*<br>0.54*<br>LD, CFNAI, MFFs in Linear-LS<br>0.81*<br>0.78*<br>0.59*<br>0.79*<br>0.96*<br>0.54*<br>LD, NFCI, MFFs in Linear-LS<br>0.86*<br>0.79*<br>0.59*<br>0.79*<br>0.89*<br>0.52*<br>LD, GZ_SPRD, MFFs in Linear-LS<br>0.82*<br>0.81*<br>0.59*<br>0.79*<br>0.77*<br>0.60*<br>LD, FFs, MFFs in Linear-LS<br>0.78*<br>0.77*<br>0.53*<br>0.82*<br>0.91*<br>0.57*|Panel A2: RMSE ratios for Almon MIDAS models vis-a`-vis the RW model for Real GDP growth (GDP), Real Consumption growth (RealCons), and Moody’s default<br>spread (Baa-Aaa)|Predictive model specifcations<br>Fixed sample<br>Recursive sample<br>Fixed sample<br>Recursive sample<br>Fixed Sample<br>Recursive Sample|LD, MFFs in Almon<br>0.74*<br>0.79*<br>0.47*<br>0.93*<br>0.91*<br>0.62*<br>LD, ADS, MFFs in Almon<br>0.58*<br>0.63*<br>0.49*<br>0.67*<br>0.94*<br>0.51*<br>LD, CFNAI, MFFs in Almon<br>0.59*<br>0.64*<br>0.44*<br>0.73*<br>0.96*<br>0.58*<br>LD, NFCI, MFFs in Almon<br>0.77*<br>0.79*<br>0.49*<br>0.88*<br>0.96*<br>0.58*<br>LD, GZ_SPRD, MFFs in Almon<br>0.77*<br>0.80*<br>0.47*<br>0.93*<br>0.91*<br>0.41*<br>LD, FFs, MFFs in Almon MIDAS<br>0.90*<br>0.80*<br>0.52*<br>0.93*<br>0.91*<br>0.58*|
|---|---|---|---|---|



Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

623 

|Panel B1: RMSE ratios for Linear-LS models vis-a`-vis the RW model for VIX (logVIX), VRP, and ETF iShares Core S&P500 (ETF_iSHARES)|logVIX<br>VRP<br>ETF_iSHARES<br>Predictive model specifcations<br>Fixed sample<br>Recursive sample<br>Fixed sample<br>Recursive sample<br>Fixed sample<br>Recursive sample|LD<br>0.99<br>1.00<br>1.00<br>LD, all CFFs [ICp2]<br>1.76<br>0.70*<br>0.94*<br>0.97*<br>1.36<br>1.53<br>LD, CFFs in Linear-LS<br>0.87*<br>0.70*<br>0.93*<br>0.98<br>0.98<br>1.07<br>LD, MFFs in Linear-LS<br>1.20<br>0.76*<br>0.96*<br>0.93*<br>0.98<br>1.26<br>LD, ADS, MFFs in Linear-LS<br>1.20<br>0.76*<br>0.99<br>0.98<br>0.85*<br>1.19<br>LD, CFNAI, MFFs in Linear-LS<br>1.20<br>0.76*<br>0.96*<br>0.93*<br>0.98<br>1.26<br>LD, NFCI, MFFs in Linear-LS<br>1.20<br>0.76*<br>0.94*<br>1.04<br>2.07<br>1.46<br>LD, GZ_SPRD, MFFs in Linear-LS<br>1.20<br>0.77*<br>0.97<br>1.03<br>1.01<br>1.27<br>LD, FFs, MFFs in Linear-LS<br>1.16<br>0.72*<br>1.25<br>1.04<br>0.98<br>1.26<br>LD, SKEW, MFFs in Linear-LS<br>1.06<br>0.74*<br>0.94*<br>0.92*<br>1.00<br>1.27|Panel B2: RMSE ratios for Almon MIDAS models vis-a`-vis the RW model for VIX (logVIX), VRP, and ETF iShares Core S&P500 (ETF_iSHARES)|Predictive Model Specifcations<br>Fixed sample<br>Recursive sample<br>Fixed sample<br>Recursive sample<br>Fixed sample<br>Recursive sample|LD, MFFs in Almon<br>0.98<br>0.78*<br>0.91*<br>0.96*<br>1.26<br>1.84<br>LD, ADS, MFFs in Almon<br>0.98<br>0.78*<br>0.92*<br>0.98<br>0.86*<br>1.84<br>LD, CFNAI, MFFs in Almon<br>0.98<br>0.78*<br>0.93*<br>0.99<br>1.26<br>1.84<br>LD, NFCI, MFFs in Almon<br>1.08<br>0.80*<br>0.91*<br>1.08<br>1.26<br>1.84<br>LD, GZ_SPRD, MFFs in Almon<br>0.77*<br>0.75*<br>0.91*<br>0.96*<br>1.26<br>1.84<br>LD, FFs, MFFs in Almon MIDAS<br>0.78*<br>0.54*<br>0.99<br>0.97*<br>0.78*<br>1.08<br>LD, SKEW, MFFs in Almon<br>1.11<br>0.78*<br>0.91*<br>0.96*<br>1.31<br>2.00|Notes:The IS period refers to 1986q1–2001q4 for the Real GDP growth (GDP), Real Consumption growth (RealCons), and the Moody’s default spread (Baa-Aaa), 1990q1–2003q4<br>for the VIX (logVIX) and VRP, and 2000q3–2007q1 for the ETF iShares Core S&P500 (ETF_iSHARES). The OOS period refers to 2002q1–2017q4 for the GDP, RealCons and Baa-<br>Aaa, 2004q1–2017q4 for the logVIX and VRP, and 2007q2–2017q4 for the ETF_iSHARES. For the GZ_SPRD, the end date is 2016M08 hence IS period is 1986q1–2001q2 and<br>OOS period 2001q3–2016q3. The OOS analysis is performed based on a fxed sample as well as the recursive estimation of the factors in pseudo real-time at each forecast origin using<br>the recent vintage of data. * denotes the cases where the MSE-F statistic is greater than the critical values at 5% signifcance level which implies that the competing model as specifed<br>in the frst column performs signifcantly better than the RW benchmark model. Bold RMSE ratios refer to the min RMSE across all models for a given dependent variable. The pre-<br>dictive model involves the following predictors: The lagged dependent (LD) term, the MFFs, namely the Common Factor (CF), the HFFs and LFFs, the CFFs, the Aruoba, Diebold,<br>and Scotti (2009) (ADS) index, the Chicago National Activity and Financial Conditions Indices (CFNAI and NFCI, respectively), the four Fama–French (FF) factors (RM-RF, SMB,<br>HML, UMD),Gilchrist and Zakrajsek (2012)spread (GZ_SPRD) and theAmaya, Christoffersen, Jacobs, and Vasquez (2015)Realized Skewness (SKEW).<br>Downloaded from https://academic.oup.com/jfec/article/18/3/585/5909329 by Eastman Dental Institute user on 20 May 2026|
|---|---|---|---|---|---|---|



Journal of Financial Econometrics 

624 

evaluate if the factor augmented predictive regression models yield statistically significant predictive gains vis-a`-vis other benchmark models like the RW (or the AR reported in the first row of Panels A1 and B1), as marked in Table 10. Similarly, the model with the lowest and significant RMSE ratio for each dependent variable and each family of models and forecasting scheme is marked in bold in Table 10. 

Four broad results can be highlighted from Table 10: first, the RMSE ratios of almost all factor augmented predictive models (linear or MIDAS) vis-a`-vis the RW or the AR model (given it has the same RMSE as the RW), for forecasting the real GDP growth, the real Consumption growth and the default spread, are statistically significant and less than one (shown in Panels A1 and A2). This is also the case for most (but not all) the models for the VIX, VRP, and ETF returns, which seem harder to forecast OOS. This could be due to the nature of these financial series and/or the shorter sample available. Second, for the best performing model with the lowest RMSE ratio, the recursive OOS approach yields similar and in some cases improved forecasting gains vis-a`-vis the fixed sample OOS scheme for all variables, except the ETF returns. Interestingly, although the recursive method is a more demanding OOS forecasting scheme, it not only improves over the fixed sample OOS but for at least two cases—namely the default spread and the VIX—it also substantially improves the forecasting gains, as shown by the corresponding lowest RMSE ratios. Third, the models with the lowest RMSE ratios refer to models with our MFFs rather than the traditional CFFs as predictors, in almost all cases. Additional factors turn out to improve the recursive OOS forecasts, namely the ADS index for the GDP, the CFNAI for the Consumption, the NFCI and GZ spread for the corporate default spread, the excess market returns for the VIX, along with some of our MFFs. Finally, in most cases, the best performing FADL-MIDAS models (with the lowest RMSE) provide forecasting gains over the corresponding best performing FADL linear-LS model (comparing the corresponding best RMSE models in Panels A1 and A2 or Panels B1 and B2). 

To further investigate the OOS forecasting performance of the models in the recent post-GM period, we employ the Model Confidence Set (MCS) procedure developed by Hansen, Lunde, and Nason (2011). In line with Table 10, we use the significant predictors for each model and focus on the recursive scheme. In Table 11, we report the RMSE, the p- value and the ranking of each model. Following Hansen, Lunde, and Nason (2011), we use 75% and 90% confidence levels. The MCS results are consistent with those in Table 10 and show that for all variables at least one of the Linear-LS and PDL/Almon MIDAS models perform better than RW, which in most cases ranks among the worst predictive models. 

Concluding, we provide evidence that for quarterly real GDP and Consumption growth, the Moody’s corporate bond spread as well as the VIX, VRP, and ETF returns, during the pre- and post-GM periods, our CF, as well as the group-specific macro and financial factors have significant IS and OOS forecasting abilities. This evidence is especially strong in the context of MIDAS predictive regressions, vis-a`-vis the traditional linear predictive regressions, for example, FADL type models, as well as the RW and AR benchmark models. Moreover, comparing the role of the CF, during the pre- and post-GM, in Granger causing GDP or Consumption growth as well as the default spread, we find that while the CF is significant in both subperiods, it has a relatively smaller estimated coefficient in the post-GM period. Hence, during the recent period, the role of the CF, while still significant, turns out to be relatively much weaker in Granger causing the aforementioned key economic variables. These predictive regression models results extend the evidence of a break in the 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

625 

Table 11 MCS by Hansen, Lunde, and Nason (2011) for OOS forecasting ability of mixed-frequency factors, CFFs, as well as other types of factors 

Panel A1: RMSE for Linear-LS models and the RW model for Real GDP growth (GDP), Real Consumption growth (RealCons), and Moody’s default spread (Baa-Aaa) 

|Specifcation|GDP<br>RealCons<br>Baa-Aaa<br>Recursive sample<br>Recursive sample<br>Recursive sample|
|---|---|
||RMSE<br>p-value<br>Rank<br>RMSE<br>p-value<br>Rank<br>RMSE<br>p-value<br>Rank|
|LD, all CFFs [ICP2]<br>LD, CFFs in Linear-LS<br>LD, MFFs in Linear-LS<br>LD, ADS, MFFs in Linear-LS<br>LD, CFNAI, MFFs in Linear-LS<br>LD, NFCI, MFFs in Linear-LS<br>LD, GZ_SPRD, MFFs in Linear-LS<br>LD, FFs, MFFs in Linear-LS<br>RW|0.51<br>0.73**<br>4<br>0.24<br>1.00**<br>1<br>0.27<br>0.82**<br>2<br>0.52<br>0.62**<br>5<br>0.25<br>0.94**<br>2<br>0.28<br>0.57*<br>3<br>0.51<br>0.49**<br>7<br>0.31<br>0.32*<br>3<br>0.25<br>1.00**<br>1<br>0.44<br>1.00**<br>1<br>0.28<br>0.22*<br>6<br>0.26<br>0.27*<br>6<br>0.49<br>0.54**<br>6<br>0.32<br>0.29*<br>4<br>0.26<br>0.27*<br>6<br>0.50<br>0.36**<br>8<br>0.28<br>0.22*<br>6<br>0.25<br>1.00**<br>1<br>0.48<br>0.78**<br>3<br>0.28<br>0.22*<br>6<br>0.38<br>0.45*<br>4<br>0.51<br>0.49**<br>7<br>0.28<br>0.22*<br>6<br>0.27<br>0.18*<br>7<br>0.63<br>0.86**<br>2<br>0.39<br>0.29*<br>5<br>0.48<br>0.36*<br>5|



Panel A2: RMSE for PDL/Almon MIDAS models and the RW for Real GDP growth (GDP), Real Consumption growth (RealCons), and Moody’s default spread (Baa-Aaa) 

|Specifcation|Recursive sample<br>Recursive sample<br>Recursive sample|
|---|---|
||RMSE<br>p-value<br>Rank<br>RMSE<br>p-value<br>Rank<br>RMSE<br>p-value<br>Rank|
|LD, MFFs in PDL/Almon<br>LD, ADS, MFFs in PDL/Almon<br>LD, CFNAI, MFFs in PDL/Almon<br>LD, NFCI, MFFs in PDL/Almon<br>LD, GZ_SPRD, MFFs in PDL/Almon<br>LD, FFs, MFFs in PDL/Almon MIDAS<br>RW|0.50<br>0.29*<br>5<br>0.37<br>0.43*<br>3<br>0.31<br>0.15*<br>3<br>0.40<br>1.00**<br>1<br>0.26<br>1.00**<br>1<br>0.25<br>0.12*<br>5<br>0.41<br>0.86**<br>2<br>0.29<br>0.06<br>5<br>0.29<br>0.13*<br>4<br>0.50<br>0.29*<br>5<br>0.35<br>0.77**<br>2<br>0.29<br>0.13*<br>4<br>0.51<br>0.31*<br>4<br>0.37<br>0.43*<br>3<br>0.20<br>1.00**<br>1<br>0.51<br>0.15*<br>6<br>0.37<br>0.43*<br>3<br>0.29<br>0.13*<br>4<br>0.63<br>0.51*<br>3<br>0.39<br>0.21*<br>4<br>0.49<br>0.17*<br>2|



Panel B1: RMSE for Linear-LS models and the RW for VIX (logVIX), Variance Risk Premium (VRP), and ETF iShares (ETF_iShares) 

|Specifcation|logVIX<br>VRP<br>ETF_iShares<br>Recursive sample<br>Recursive sample<br>Recursive sample|
|---|---|
||RMSE<br>p-value<br>Rank<br>RMSE<br>p-value<br>Rank<br>RMSE<br>p-value<br>Rank|
|LD, all CFFs [ICP2]<br>LD, CFFs in Linear-LS<br>LD, MFFs in Linear-LS<br>LD, ADS, MFFs in Linear-LS<br>LD, CFNAI, MFFs in Linear-LS<br>LD, NFCI, MFFs in Linear-LS<br>LD, GZ_SPRD, MFFs in Linear-LS<br>LD, FFs, MFFs in Linear-LS<br>LD, SKEW, MFFs in Linear-LS<br>RW|0.11<br>1.00**<br>2<br>15.57<br>0.85**<br>5<br>0.102<br>0.64**<br>5<br>0.11<br>1.00**<br>1<br>15.67<br>0.94**<br>4<br>0.072<br>0.15*<br>8<br>0.12<br>0.65**<br>5<br>14.88<br>1.00**<br>2<br>0.083<br>0.94**<br>3<br>0.12<br>0.65**<br>5<br>15.74<br>0.24*<br>9<br>0.077<br>0.99**<br>2<br>0.12<br>0.65**<br>5<br>14.88<br>1.00**<br>2<br>0.083<br>0.94**<br>3<br>0.12<br>0.65**<br>5<br>16.74<br>0.79**<br>7<br>0.096<br>0.59**<br>6<br>0.12<br>0.64**<br>6<br>16.50<br>0.72**<br>8<br>0.083<br>0.51**<br>7<br>0.12<br>1.00**<br>3<br>16.67<br>0.86**<br>6<br>0.083<br>0.94**<br>3<br>0.12<br>0.95**<br>4<br>14.87<br>1.00**<br>1<br>0.084<br>0.91**<br>4<br>0.16<br>0.08<br>7<br>16.02<br>0.98**<br>3<br>0.066<br>1.00**<br>1|



Journal of Financial Econometrics 

626 

Table 11 Continued 

Panel B2: RMSE for PDL/Almon MIDAS models and the RW for VIX (logVIX), VRP, and ETF iShares (ETF_iShares) 

|Specifcation|Recursive sample|Recursive sample|Recursive sample|
|---|---|---|---|
||RMSE<br>p-value<br>Rank|RMSE<br>p-value<br>Rank|RMSE<br>p-value<br>Rank|
|LD, MFFs in PDL/Almon<br>LD, ADS, MFFs in<br>PDL/Almon<br>LD, CFNAI, MFFs in<br>PDL/Almon<br>LD, NFCI, MFFs in<br>PDL/Almon<br>LD, GZ_SPRD, MFFs in<br>PDL/Almon<br>LD, FFs, MFFs in PDL/<br>Almon MIDAS<br>LD, SKEW, MFFs in<br>PDL/Almon<br>RW|0.13<br>0.00<br>3<br>0.13<br>0.00<br>3<br>0.13<br>0.00<br>3<br>0.13<br>0.00<br>4<br>0.12<br>0.03<br>2<br>0.09<br>1.00**<br>1<br>0.13<br>0.00<br>3<br>0.16<br>0.00<br>5|15.34<br>1.00**<br>1<br>15.62<br>0.90**<br>3<br>15.83<br>0.90**<br>4<br>17.31<br>0.40**<br>6<br>15.34<br>1.00**<br>1<br>15.49<br>1.00**<br>2<br>15.34<br>1.00**<br>1<br>15.98<br>0.84**<br>5|0.14<br>0.00<br>4<br>0.14<br>0.00<br>4<br>0.14<br>0.00<br>4<br>0.14<br>0.00<br>4<br>0.14<br>0.00<br>4<br>0.08<br>0.56<br>2<br>0.15<br>0.17<br>3<br>0.07<br>1.00**<br>1|



Notes: The IS period refers to 1986q1–2001q4 for the Real GDP growth (GDP), Real Consumption growth (RealCons) and the Moody’s default spread (Baa-Aaa), 1990q1–2003q4 for the VIX (logVIX) and VRP, and 2000q3–2007q1 for the ETF iShares Core S&P500 (ETF_iSHARES). The OOS period refers to 2002q1– 2017q4 for the GDP, RealCons, and Baa-Aaa, 2004q1–2017q4 for the logVIX and VRP, and 2007q2–2017q4 for the ETF_iSHARES. For the GZ_SPRD, the end date is 2016M08 hence IS period is 1986q1–2001q2 and OOS period is 2001q3–2016q3. The OOS analysis is performed based on the recursive estimation of the factors in pseudo real-time at each forecast origin using the recent vintage of data. Bold values refer to the models ranking first according to MCS. The results based on significance level 10% and 25% are identified by (*) and (**), respectively. RMSEs of GDP and RealCons are multiplied by 100. 

loadings of the factor models (reported in the previous subsection), to the conditional setup related to the estimated impact of the CF as a predictor of key macro and financial variables. 

## 4 Conclusions 

This article contributes further to our understanding of group factor models for extracting PCs from large panels of mixed data frequencies, allowing us to estimate and test for the existence of the common factor among the groups as well as the group-specific factors. New analytical results are derived for the asymptotic distribution of the PCs and test statistics for the existence of the common factor especially regarding the alternative approaches of aggregating the data first and then extracting PCs, or applying PCA first and then aggregating the factor estimates. Our framework provides an interesting setup to study the common factors among two large groups/panels of quarterly macro and monthly financial indicators, in order to test for the existence of a CF as well as estimate the group-specific financial and macro factors. Interestingly, we find one CF in the United States during the pre- and post-GM, since the early 1960s. Structural break analysis reveals that the loadings of the CF have changed during the pre- and post-GM and that the loadings of certain financial 

Andreou et al. j Mixed-Frequency Macro–Finance Factor Models 

627 

assets have become relatively weaker during the recent regime. Our empirical analysis shows that the estimated PCs are almost identical whether we pursue the PCA approach first and then aggregate the factors or whether we aggregate the data and then apply PCA. The forecasting role of our factors, as well as other established factors in the literature, is further investigated in predicting key macro and financial indicators, such as real GDP and Consumption, the VIX, the VRP, corporate bond default spreads, and ETF iShares Core S&P500 returns, via FADL and FADL-MIDAS type models. Our empirical results provide evidence of significant forecasting gains of our factors for these key economic indicators and show that the CF, while being significant in both regimes, has a weaker predictive effect in the recent period covering the last three decades. 

## Supplemental Data 

Supplemental data is available at Journal of Financial Econometrics online. 

## References 

- Ahn, S. C., and A. R. Horenstein. 2013. Eigenvalue Ratio Test for the Number of Factors. Econometrica 81: 1203–1227. 

- Amaya, D., P. Christoffersen, K. Jacobs, and A. Vasquez. 2015. Does Realized Skewness Predict the Cross-Section of Equity Returns?. Journal of Financial Economics 118: 135–167. 

- Ando, T., and J. Bai. 2015. Multifactor Asset Pricing with a Large Number of Observable Risk Factors and Unobservable Common and Group-Specific Factors. Journal of Financial Econometrics 13: 556–604. 

- Andreou, E., P. Gagliardini, E. Ghysels, and M. Rubin. 2019. Inference in Group Factor Models with an Application to Mixed-Frequency Data. Econometrica 87: 1267–1305. 

- Aruoba, S., F. Diebold, and C. Scotti. 2009. Real-Time Measurement of Business Conditions. Journal of Business & Economic Statistics 27: 417–427. 

- Bai, J., and S. Ng. 2002. Determining the Number of Factors in Approximate Factor Models. Econometrica 70: 191–221. 

- Bai, J., and S. Ng. 2008. Forecasting Economic Time Series Using Targeted Predictors. Journal of Econometrics 146: 304–317. 

- Bates, J. M., and C. W. Granger. 1969. The Combination of Forecasts. Journal of the Operational Research Society 20: 451–468. 

- Brave, S., and R. A. Butters. 2012. Diagnosing the Financial System: Financial Conditions and Financial Stress. International Journal of Central Banking 8: 191–239. 

- Brave, S., and R. A. Butters. 2014. Nowcasting Using the Chicago Fed National Activity Index. Economic Perspectives 38: 19–37. 

- Breitung, J., and S. Eickmeier. 2011. Testing for Structural Breaks in Dynamic Factor Models. Journal of Econometrics 163: 71–84. 

- Breitung, J., and S. Eickmeier. 2016. Analyzing International Business and Financial Cycles Using Multi-Level Factor Models: A Comparison of Alternative Approaches. Advances in Econometrics 15: 177–214. 

- Chaise, S. D., L. Ferrara, and D. Giannone. 2017. “Common Factors of Commodity Prices.” Working paper 645, Banque de France. 

- Chen, P. 2012. “Common Factors and Specific Factors.” Working Paper. 

- Christoffersen, P., C. Dorion, K. Jacobs, and L. Karoui. 2014. Nonlinear Filtering in Affine Term Structure Models. Management Science 60: 2248–2268. 

Journal of Financial Econometrics 

628 

- Christoffersen, P., M. Fournier, and K. Jacobs. 2017. The Factor Structure in Equity Options. The Review of Financial Studies 31: 595–637. 

- Christoffersen, P., E. Ghysels, and N. R. Swanson. 2002. Let’s Get “Real” about Using Economic Data. Journal of Empirical Finance 9: 343–360. 

- Christoffersen, P., and H. Langlois. 2013. The Joint Dynamics of Equity Market Factors. Journal of Financial and Quantitative Analysis 48: 1371–1404. 

- Drehmann, M., C. Borio, and K. Tsatsaronis. 2012. “Characterising the Financial Cycle: Don’t Lose Sight of the Medium Term!.” BIS Working Papers 380, Bank for International Settlements. 

- Gilchrist, S., and E. Zakrajsek. 2012. Credit Spreads and Business Cycle Fluctuations. American Economic Review 102: 1692–1720. 

- Gonc¸alves, S., M. W. McCracken, and B. Perron. 2017. Tests of Equal Accuracy for Nested Models with Estimated Factors. Journal of Econometrics 198: 231–252. 

- Gospodinov, N., and S. Ng. 2013. Commodity Prices, Convenience Yields, and Inflation. Review of Economics and Statistics 95: 206–219. 

- Goyal, A., C. Pe´rignon, and C. Villa. 2008. How Common Are Common Return Factors across the NYSE and Nasdaq?. Journal of Financial Economics 90: 252–271. 

- Hansen, P., A. Lunde, and J. Nason. 2011. The Model Confidence Set. Econometrica 79: 453–497. 

- Kose, A. M., C. Otrok, and C. H. Whiteman. 2008. Understanding the Evolution of World Business Cycles. Journal of International Economics 75: 110–130. 

- McCracken, M., and S. Ng. 2016. FRED-MD: A Monthly Database for Macroeconomic Research. Journal of Business & Economic Statistics 36: 574–589. 

- Onatski, A. 2010. Determining the Number of Factors from Empirical Distribution of Eigenvalues. Review of Economics and Statistics 92: 1004–1016. 

- Stock, J., and M. Watson. 2002. Forecasting Using Principal Components from a Large Number of Predictors. Journal of the American Statistical Association 97: 1167–1179. 

- Stock, J., and M. Watson. 2008. “Forecasting in Dynamic Factor Models Subject to Structural Instability.” In N. Shephard and J. Castle (eds.), The Methodology and Practice of Econometrics: Festschrift in Honor of D.F. Hendry, pp. 1–57. Oxford University Press. 

- Timmermann, A. 2006. “Forecast Combinations.” In G. Elliott, C. Granger, and A. Timmermann (eds.), Handbook of Economic Forecasting, Volume 1, pp. 136–96. Elsevier. 

- Wang, P. 2012. “Large Dimensional Factor Models with a Multi-Level Factor Structure: Identification, Estimation, and Inference.” Working Paper, Hong Kong University of Science and Technology. 

- Zhou, H. 2018. Variance Risk Premia, Asset Predictability Puzzles, and Macroeconomic Uncertainty. Annual Review of Financial Economics 10: 481–497. 

