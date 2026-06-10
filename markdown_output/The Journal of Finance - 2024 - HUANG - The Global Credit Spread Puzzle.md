THE JOURNAL OF FINANCE[•] VOL. LXXX, NO. 1[•] FEBRUARY 2025 

## **The Global Credit Spread Puzzle** 

JING-ZHI HUANG, YOSHIO NOZAWA, and ZHAN SHI[*] 

## **ABSTRACT** 

We examine the ability of structural models to predict credit spreads using global default data and security-level credit spread data in eight developed economies. We find that two representative, pure default-risk models tend to underpredict the average credit spreads on investment-grade (IG) bonds, especially their spreads over government bonds, thereby providing evidence for a “global credit spread puzzle.” However, a model incorporating endogenous liquidity in the secondary debt market helps mitigate the puzzle. Furthermore, the model captures certain determinants of corporate bond market frictions across the eight economies and substantially improves the cross-sectional fit of individual IG credit spreads. 

HOW ARE CORPORATE BONDS OUTSIDE the United States priced based on fundamentals? Despite the rapid growth in many corporate bond markets around the world, research on this important question is limited. In this paper, we 

*Jing-Zhi Huang is with the Smeal College of Business, Penn State University. Yoshio Nozawa is with the Rotman School of Management and UTSC at the University of Toronto. Zhan Shi is with the PBC School of Finance, Tsinghua University. We are very grateful to Wei Xiong (Editor), an Associate Editor, and two anonymous referees for their extensive and detailed comments that helped improve the paper substantially. We would also like to thank Gurdip Bakshi, Snehal Banerjee, Mehmet Canayaz, Hui Chen, Wenxin Du, Nicolae Gârleanu, Bob Goldstein, Zhiguo He, Yurong Hong, Grace Hu, Ralph Koijen, Anh Le, David Li, Juhani Linnainmaa, Christian Lundblad, Konstantin Milbradt, Jun Pan, Carolin Pflueger, Scott Richardson, Lukas Schmid, Michael Schwert, Matt Spiegel, Adi Sunderam, Yiyao Wang, Toni Whited, and Haoxiang Zhu; seminar participants at CUHK-Shenzhen, The Hong Kong Monetary Authority, HKUST, Lugano, Penn State, SAIF, SWUFE, Temple, Toronto, Tsinghua University, and UMass Amherst; and conference participants (and especially discussants) at the 2019 Dolomite Winter Finance Conference (Alberto Plazzi), the 2019 University of Connecticut Finance Conference (Fan Yang), the 2019 CICF (Jayoung Nam), the 9[th] FIRN Annual Conference (Antje Berndt), and the 2020 AFA (Peter Feldhütter) for helpful comments and suggestions. We also thank Terrence O’Brien, Shasta Shakya, Xiaowei Wang, Yao Xiao, and Hongyu Yao for their able research assistance. Shi thanks the funding support from Tsinghua University (#100030060). The initial draft of the paper was prepared when Yoshio Nozawa was at the Federal Reserve Board. We have read _The Journal of Finance_ ’s disclosure policy and 

Correspondence: Jing-Zhi Huang, Smeal College of Business, Penn State University, University Park, PA 16802; e-mail: jxh56@psu.edu 

This is an open access article under the terms of the Creative Commons AttributionNonCommercial-NoDerivs License, which permits use and distribution in any medium, provided the original work is properly cited, the use is non-commercial and no modifications or adaptations are made. 

DOI: 10.1111/jofi.13409 

© 2024 The Author(s). _The Journal of Finance_ published by Wiley Periodicals LLC on behalf of American Finance Association. 

101 

_The Journal of Finance[®]_ 

102 

aim to narrow this gap by studying the determinants of corporate bond prices in eight developed economies using the structural approach in the spirit of Merton (1974). In particular, we address two important questions: (Q1) Can standard structural models of risky debt explain corporate bond yield spreads in different credit markets, and (Q2) if the answer is no, how can we improve such models? 

One stylized fact documented in the U.S. credit market is that, once calibrated to historical default data and equity risk premia, standard structural models generate similar credit spreads and tend to substantially underpredict investment-grade (IG) corporate-Treasury spreads (Huang and Huang (2012))—a finding often referred to as the credit spread puzzle (CSP). Given the consensus that the corporate-Treasury spread includes a nondefault component, subsequent studies mainly focus on a weaker version of this puzzle, namely, the puzzle based on corporate spreads over alternative “default-free” benchmarks. For instance, Chen, Collin-Dufresne, and Goldstein (2009) and Chen (2010) examine BBB-AAA spreads, and Bao (2009) considers single-name credit default swap (CDS) spreads. A recent debate focuses on whether the CSP exists when the interest rate swap (IRS) yield curve is used as the defaultfree benchmark (Feldhütter and Schaefer (2018), Du, Elkamhi, and Ericsson (2019), Bai, Goldstein, and Yang (2020)). Accordingly, in the first part of our analysis, we examine the question raised in (Q1) in general and the CSP in particular. We document robust evidence for both versions of the puzzle—the one based on government bond yields and the other based on LIBOR swap rates—in developed credit markets outside the United States. 

One main factor behind this “global credit spread puzzle” (GCSP) is likely the fact that standard structural models do not include a corporate bond liquidity component. Therefore, in the second part of our analysis, we consider a variant of the He and Milbradt (2014) model with endogenous corporate bond illiquidity, an important corporate bond pricing model that has not been empirically tested in prior literature. We show that incorporating debt market frictions can help mitigate the GCSP, thereby shedding light on the question raised in (Q2). 

We now describe our analysis in more detail. We choose a variant of the Black and Cox (1976) model as our baseline model, a one-factor model with a flat default boundary for coupon-bearing bonds.[1] This choice is driven mainly by the flexibility offered by this model, termed the BC model for convenience, as it can accommodate several other important features—such as stationary leverage ratios and endogenous corporate bond illiquidity—while maintaining tractability. We empirically test the BC model using security-level pricing data on domestic corporate bonds in eight developed countries—Australia, Canada, France, Germany, Italy, Japan, the United Kingdom, and the United States— from 1997 to 2017, as well as global default data from 1970 to 2017. We focus on the ability of the model to predict corporate bond spreads over swap rates instead of government bond yields in our main analysis, because the recent 

1 This is also the baseline model examined in Huang and Huang (2012). 

_The Global Credit Spread Puzzle_ 

103 

debate on the CSP in the U.S. market revolves around its swap rate–based version, not the Treasury-based version of the puzzle. 

We first examine the model’s performance based on 24 IG/country groups (portfolios) of corporate bonds, a combination of three IG credit rating categories—AAA&AA (referred to as AA+ for convenience), A, and BBB—and eight countries. Given that estimation of default boundary (denoted _d_ ) in the model lies at the heart of the recent debate on the swap rate–based CSP, we implement the model with three alternative estimates of _d_ for each country.[2] We obtain the mean pricing error (MPE) of the model—the average of differences between the model and observed spreads—for each of 72 (24×3) IG/country/ _d_ bins. We find that 53 of these bins have a significantly negative MPE, implying an underprediction of credit spreads. The 19 bins not displaying such an underprediction include all nine bins in Japan, five in France, three in Germany, and two in Canada. However, these 19 MPEs may be driven by negative credit spreads over swap rates in the data, which the model fails to reproduce by nature. For instance, more than 50% of credit spreads in the AA+/Japan group are negative. When we exclude observations with negative credit spreads from the sample, the number of bins with the underprediction problem increases to 58. 

Note also that our sample consists of all qualified nonfinancial bonds. For comparison, we repeat the analysis for industrial firms only. We find that the number of bins displaying the underprediction problem is 62 and 57 with and without controls for negative credit spreads over swap rates. In the former case, nine out of the 10 (= 72 − 62) bins without the underprediction problem belong to Japan. That is, if we focus on industrial firms with positive observed credit spreads (a sample more comparable to those used in the empirical literature on structural models), the model underpredicts the average IG spread except for the nine IG bins in Japan (and one BBB/Italy/ _d_ bin). 

Next, we examine the ability of the model to predict the average IG spread at the country level. Note that doing so also helps mitigate the concern that some of these 24 IG/country groups are small. We find that out of 24 IG[ctry] / _d_ bins (a combination of eight IG groups at the country level and three estimates of _d_ ), the model underpredicts the mean spread for 20 and 17 (21 and 20) bins for the full sample (industrial firms) with and without controls for negative credit spreads in the data. In the case of industrial firms without negative observed spreads over swap rates, the only three IG[ctry] / _d_ bins not displaying a spread-underprediction problem all belong to Japan, that is, the BC model underpredicts the average IG spread at the country level for every country except Japan. We also repeat the analysis using a pooled sample of all seven nonU.S. countries. The model underpredicts the average credit spread for A-rated bonds, BBB bonds, and all IG bonds in the pooled sample. This is also true for 

> 2 The three estimates are obtained using the methods of Feldhütter and Schaefer (2018), Bai, Goldstein, and Yang (2020), and this study (see Section III.B.3) and, for convenience, are denoted by _d[FS]_ , _d[BGY]_ , and _d[HNS]_ , respectively. 

_The Journal of Finance[®]_ 

104 

the AA+ group once observations with negative observed credit spreads over swap rates are removed from the sample. 

Taken together, our results show that once calibrated to default data, the BC model tends to underpredict IG credit spreads, especially after controlling for negative spreads in the data. The evidence is robust to the use of 72 IG/country/ _d_ bins, 24 IG[ctry] / _d_ bins, or the pooled sample of non-U.S. countries. At the country level, Japan is the only market where we find little evidence of a CSP. Overall, we provide evidence that there is a swap rate–based CSP in credit markets outside the United States. 

To explore what may be missing in the BC model, we examine a variety of factors that may drive its pricing errors. We do not find evidence that heterogeneity in loss given default (LGD), default probabilities, investors’ risk aversion, or proxies for macroeconomic conditions can explain the underprediction of credit spreads in our sample. However, there is evidence indicating that time-varying leverage is one potential missing factor. We therefore implement the Collin-Dufresne and Goldstein (2001, CDG) model, which incorporates stationary leverage ratios into the BC model. We find that although the CDG model improves pricing performance overall, it still underpredicts the average spread for 16 out of 24 IG/country groups and six out of eight IG[ctry] groups, compared with 17 and six under the BC( _d[FS]_ ) model, where _d[FS]_ indicates the estimate of _d_ used in the implementation of the BC model.[3] In particular, the CSP is also applicable to the CDG model. This finding echoes the original version of the CSP in the U.S. market, given that both the BC and CDG models are already calibrated to the same default data in our analysis. It follows from Huang and Huang (2012) and Chen, Collin-Dufresne, and Goldstein (2009) that this “similarity” between the BC and CDG models is expected to extend to the other standard structural models implemented in the former study. 

In the second part of our analysis, we address the question raised in (Q2). Guided by our finding that liquidity measures such as bid-ask spreads explain a significant fraction of the BC model’s pricing errors, we focus on the illiquidity channel as the main source of the model misspecification. Specifically, we seek to augment the BC model with endogenous illiquidity in the secondary debt market induced by search and bargaining frictions in connection with corporate bonds traded over the counter (OTC). The debt structure of the BC model allows it to seamlessly incorporate the approach to modeling an OTC debt market as considered in Duffie, Gârleanu, and Pedersen (2005) and He and Milbradt (2014). The resulting extended model, termed the HM model, is a reduced-form variant of the He and Milbradt (2014) model. In this reducedform model, there is no rollover risk in the primary debt market in the sense of He and Xiong (2012), and a yield spread can be decomposed into the BC model–implied spread and a liquidity component. 

Importantly, the HM and BC models share the same model-implied default probability under the physical measure. This feature allows us to estimate 

> 3 We use BC( _dFS_ ) rather than BC( _dBGY_ ) or BC( _dHNS_ ) as the benchmark because _dFS_ is usually higher than _d[BGY]_ or _d[HNS]_ , and thus using _d[FS]_ biases against finding a CSP (see Section III.B.3). 

_The Global Credit Spread Puzzle_ 

105 

liquidity-related parameters at the country level by fitting to proportional bidask spreads (specified endogenously under the HM model), not credit spreads, while keeping firm fundamental parameters the same as in the BC model.[4] It follows that the HM model–implied liquidity component measures the incremental contribution of search and bargaining frictions over the BC model, thereby making the HM model suitable for studying the CSP. Moreover, unlike rollover risk (i.e., liquidity-driven default risk), the impact of such frictions on yield spreads is not constrained by calibration of the model to default data. The HM model can therefore provide a significant default-driven liquidity component in the yield spread, especially in the left tail of credit spread distribution. 

We find that the HM model raises the predicted spread and therefore reduces the negative MPEs for IG bonds substantially. For instance, the MPEs in basis points (bps) for AA+, A, and BBB bonds in the United Kingdom narrow from (−27, −39, −92) under BC( _d[FS]_ ) to (1, 13, −26) under the HM( _d[FS]_ ) model. For Australia, they are (−98, −125, −151) compared to (6, −15, −10). Of the 24 IG/country bins, the number of bins with a significantly negative MPE drops from 17 under BC( _d[FS]_ ) to six under HM( _d[FS]_ ) for the full sample, and from 19 to seven for industrial bonds. Among the seven nations that exhibit CSP at the country level in the case of industrial issuers excluding negative credit spreads, the puzzle disappears in France, Germany, Italy, and the United States under the HM model, and the MPEs for Australia, Canada, and the United Kingdom all shrink significantly, from (−134, −106, −86) bps under BC( _d[FS]_ ) to (−11, −25, −25) bps under HM( _d[FS]_ ). Taken together, our results show that incorporating search and bargaining frictions helps mitigate the CSP substantially. 

Incorporating such frictions also helps substantially increase the explanatory power of the model for individual IG bond spreads in every country. For instance, the HM model has a much higher _R_[2] in panel regressions of observed spreads on their model-implied counterparts at the bond level: Whereas the _R_[2] ranges from 19% for Australia to 35% for Canada under the BC model and is less than 22% under the CDG model, the _R_[2] under the HM model ranges from 34% for France to 79% for Australia and is greater than 50% for five countries. 

We find that the sharply improved performance under the HM model is due to, in part, two factors. One is that its default-driven liquidity component helps raise yield spreads in the left tail of the distribution, whereas such spreads are usually zero under the BC model and close to zero under the CDG model for half of the 24 IG/country bins. The other factor is that the HM model captures 

> 4 Note that there is no one-to-one mapping between a bond’s (proportional) bid-ask spread and credit spread. In our sample, on average, time-series correlations between bid-ask spreads and yield spreads are low. In addition, although mean bid-ask spreads and mean yield spreads at the country level are positively correlated, they do not have the same ordering. For example, consider the mean bid-ask spread and mean yield spread (over swap rates) on BBB bonds. They are 29 and 164 basis points (bps) for Australia, respectively, ranking as #7 and #1 among the eight countries; 47 and 131 bps for the United States, respectively, ranking as #2 and #4; and 60 and 157 bps for the United Kingdom, respectively, ranking as #1 and #2 (see Section IV.B). As a result, bonds with high observed credit spreads do not necessarily have high HM model–implied credit spreads in our analysis. 

_The Journal of Finance[®]_ 

106 

the heterogeneity in various measures of corporate bond market frictions, such as the price impact of fire sales, across the eight countries. 

Lastly, for completeness and comparison, we repeat the main analysis using government bond yields as the default-free rates. We find robust evidence for a government bond yield–based CSP, and, as expected, it is stronger than its swap rate–based counterpart. For instance, the BC model underpredicts the mean credit spread over government bonds for 21 out of 24 IG/country/ _d[FS]_ bins and 67 out of 72 IG/country/ _d_ bins, compared with 17 and 53 bins in the case of the swap rate–based CSP. The government bond yield–based puzzle is also more challenging for the HM model to explain, although incorporating debt illiquidity still helps improve the model performance substantially. For example, the HM model underpredicts the spread over government bond yields (swap rates) for 12 (six) out of the 24 IG/country/ _d[FS]_ bins. 

This paper contributes to the literature in at least three respects. First, it is among the first to conduct an empirical analysis of structural credit risk models using a sample of individual corporate bonds from eight developed countries. Second, we provide strong evidence for both the swap rate–based and government bond yield–based versions of the CSP in international credit markets. Third, we propose and test the HM model with endogenous illiquidity—a model that has not been tested before—that makes it possible to isolate corporate bond illiquidity as a potential source of the CSP. We show that incorporating such illiquidity helps improve model performance and mitigate the CSP, as well as deepens our understanding of the puzzle. 

The rest of the paper is organized as follows. In Section I, we review the related literature. In Section II, we describe the data used in our empirical analysis. In Section III, we examine the performance of the purely credit risk–based BC and CDG models. We consider the HM model that incorporates corporate bond illiquidity in Section IV. Section V concludes. 

## **I. Related Literature** 

This paper relates to the literature that explains U.S. corporate credit spreads through the lens of structural models, with a particular focus on the extant literature that explores model implications for both real default probabilities and credit spreads. To resolve the CSP based on the U.S. Treasury yields à la Huang and Huang (2012, hereafter HH), many studies propose various economic channels to account for the credit component of yield spreads by incorporating additional sources of the default premium. Examples include Cremers, Driessen, and Maenhout (2008), Bao (2009), Chen, Collin-Dufresne, and Goldstein (2009), Bhamra, Kuehn, and Strebulaev (2010), Chen (2010), Gourio (2013), Kuehn and Schmid (2014), Christoffersen, Du, and Elkamhi (2017), McQuade (2018), Du, Elkamhi, and Ericsson (2019), and Shi (2019).[5] In contrast, He and Milbradt (2014) and Chen et al. (2018) incorporate OTC 

> 5 Albagli, Hellwig, and Tsyvinski (2014, 2024) show that noisy aggregation of dispersed information in financial markets can explain the CSP in the U.S. market. 

_The Global Credit Spread Puzzle_ 

107 

market search frictions into structural models to capture the noncredit component of yield spreads. More recently, researchers have debated the swap rate– based CSP in the U.S. market. Feldhütter and Schaefer (2018, FS) report that the BC model for zero-coupon bonds performs well in matching the average IG bond spreads over swap rates. Bai, Goldstein, and Yang (2020, BGY) argue that the FS calibration method underestimates the ratio of book debt to the market value of assets for CCC- to C-rated firms and, as a result, overestimates the default boundary and consequently the model-implied credit spread. Feldhütter and Schaefer (2023) address this issue by excluding the major rating category C from their estimation sample. 

We contribute to the above literature along several dimensions. First, we investigate the CSP using data on individual corporate bonds from seven nonU.S. countries. Additionally, we examine single-name CDS markets in these countries. We provide evidence that both the original and weak versions of the puzzle exist in credit markets outside the United States. Second, we consider not only standard structural models but also the type of models developed by He and Milbradt (2014) and Chen et al. (2018), which have not been empirically tested in the literature. Among other things, using the latter type of models allows us to obtain a model-based estimate of the liquidity premium across different credit markets.[6] Third, we propose and implement an alternative method for determining the default boundary and compare it with the methods of FS and BGY. We show that the main conclusions of this study hold regardless of which of these three methods is used. Lastly, we extend a related literature going back to Jones, Mason, and Rosenfeld (1984) that focuses on the implications of structural models under the risk-neutral (Q) measure using alternative empirical methodologies. See, for example, Eom, Helwege, and Huang (2004), Schaefer and Strebulaev (2008), Bao and Pan (2013), Bao and Hou (2017), Culp, Nozawa, and Veronesi (2018), Huang, Shi, and Zhou (2020), and a recent survey by Bakshi, Gao, and Zhong (2022). 

Several studies empirically decompose observed corporate yield spreads into default and liquidity components using a reduced-form approach (Longstaff, Mithal, and Neis (2005)), linear regressions (Dick-Nielsen, Feldhütter, and Lando (2012)), or natural experiments (Kriebel, Pfingsten, and Platte (2023)). These studies take observed yield spreads as inputs to the model and their estimated liquidity components directly incorporate yield spreads. In contrast, our decomposition is based on a structural model calibrated to default data and estimates liquidity components based on bid-ask spreads. Thus, our approach is not in favor of either a credit risk- or liquidity-based explanation of the CSP a priori and, in addition, can accommodate liquidity and default risk interdependences (Friewald, Jankowitsch, and Subrahmanyam (2012)) in 

6 He and Xiong (2012) quantify the illiquidity component in corporate bond spreads by modeling secondary market frictions in the spirit of Amihud and Mendelson (1986). Their model is not implemented here as we do not have access to transaction data for non-U.S. corporate bonds (e.g., data on trading frequency). See Huang, Liu, and Shi (2023) for an empirical study of the model using data on commercial paper prices in China and the United States. 

_The Journal of Finance[®]_ 

108 

Even fewer papers examine corporate bond markets outside the United States. Valenzuela (2016) investigates the role of rollover risk in international bonds using regression models, while Kang and Pflueger (2015) provide evidence for the link between inflation risk and corporate bond prices using data on international bond indexes. Liao (2020) studies differences in corporate bond yield spreads from the same issuer in different currency denominations and develops a regression-based measure of the aggregated credit spread differential for such bonds. None of these studies, however, tests structural models for domestic issuers outside the United States, which is the focus of this paper. Our finding that a structural model with domestic bond market search frictions has strong explanatory power for credit spreads in the domestic currency may help explain the notion that “the credit market is segmented by the denomination currencies” in Liao (2020). 

## **II. Data** 

We use month-end prices for corporate bonds in the ICE Bank of America Merrill Lynch Global Corporate Index and High Yield Index (“ML data”) from _Mercury_ , the client portal of Bank of America Merrill Lynch (ML).[7] The sample period runs from January 1997 to December 2017 except for Italy and Australia, whose samples start in 2003 and 2007, respectively. ML data cover corporate bonds denominated in six international currencies: Australian dollars, British pounds, Canadian dollars, euro (and former euro-area currencies such as the Deutsche Mark), Japanese yen, and U.S. dollars. Focusing on domestic issues in domestic currencies, we consider seven advanced, non-U.S. economies in our analysis: Australia (AUS), Canada (CAN), France (FRA), Germany (DEU), Italy (ITA), Japan (JPN), and the United Kingdom (GBR). As of December 2017, these seven countries account for 30% and 19% of the market values of corporate bonds in the ML Global Corporate Index and ML High Yield Index, respectively; the United States accounts for about 50% and 51%, respectively. Note that we focus on domestic issues in each country to provide out-of-sample evidence for the CSP; if we include foreign currency– denominated bonds issued by U.S. firms, then our empirical results will likely mechanically resemble those in the United States. Also, the ML database imposes a minimum maturity of one year and minimum face values, which vary across currencies.[8] For bond characteristics, ML data provide the credit rating, maturity date, and coupon of each issue. 

We merge the ML bond data with firm and stock data from Compustat Global or Compustat NA for Canada, which provides balance sheet information as 

> 7 ML corporate bond data have been used in several studies. For example, Liu (2016) uses ML data on global corporate bond returns. FS find that ML data for U.S. bonds are close to Bloomberg bid prices. Goldberg and Nozawa (2021) document that ML quotes and transaction prices in TRACE are similar. 

8 For the IG index, the minimum face values are AUD 100M, CAD 100M, EUR 250M, JPY 20B, GBP 100M, and USD 250M. For the HY index (which does not include Australia and Japan given the lack of market activity), they are USD 250M, EUR 250M, GBP 100M, and CAD 100M. 

_The Global Credit Spread Puzzle_ 

109 

well as stock return volatility. We link the bond- and firm-level observations based on each issuer’s name. We use Compustat name history data to track the history of names for each identifier (GVKEY), and then use the Levenshtein algorithm to find a candidate match and manually verify each match. For firms with multiple stock issues, we remove duplicate observations for shares listed in multiple stock exchanges. If a firm has multiple share classes, we add them up to compute the market value of firm equity, but we take the value-weighted average across shares in computing stock returns (which we use in computing volatility). To reduce the effect of outliers, we drop an observation if its equity book-to-market ratio is greater than 8 (the 99[th] percentile of the distribution) or less than 0.05 (the 1[th] percentile). 

Next, we use Bloomberg to identify the callability, seniority, and security of each bond. We choose senior, unsecured, noncallable bonds issued by nonfinancial issuers. Bloomberg also provides information on large shareholders of bond issuers, which allows us to screen out state-owned firms. Specifically, we drop firms for which government equity ownership is more than 50%. We also decrease a firm’s credit rating by one notch (e.g., change from AA to AA-) if the ownership ratio is between 20% and 50%, following Moody’s (2014).[9] A more detailed description of our sample selection process is provided in Section I.B of the Internet Appendix.[10] 

To facilitate comparison with recent studies using U.S. data, we merge the Lehman Brothers Fixed Income Database and ML U.S. Corporate Bond Database to obtain month-end prices of U.S. corporate bonds from 1987 to 2015. The beginning of the sample period follows FS. We use CRSP for stock prices and Compustat NA for accounting data for U.S. bonds. 

As mentioned before, we consider both corporate-government yield spreads and corporate spreads over IRS rates in this study. We obtain government bond yields with maturities of 0.25, 1, 5, 10, and 20 years for each country from Mercury; we use German government bond yields for government bond yields in all euro-area countries. We obtain swap rates from Barclays Live. A corporate bond’s yield spread is over the (continuously compounded) yield of a (hypothetical) default-free bond with exactly the same coupon rate and time to maturity. 

We use data on Bloomberg Generic (BGN) bid and ask prices of corporate bonds in our estimation of parameters on search frictions. We also use daily data on the number of distinct quotes and the number of contributing dealers from the IHS Markit Bond Pricing Database in this analysis. We use monthend single-name CDS spreads from 2002 to 2017 obtained from Markit. In addition, we obtain historical default rates and recovery rates (including U.S. and non-U.S. issuers) from Moody’s Default and Recovery Database (DRD). 

Lastly, we use stock market index data for each country from Global Financial Data. The indexes used include TOPIX for JPN, FTSE100 for GBR, DAX 

> 9 This adjustment leads to our removing one firm (Areva S.A.) and downgrading five firms (Engie S.A., ENBW Energie Baden, Deutsche Telekom, Thales, and Deutsche Post A.G.). 

> 10 The Internet Appendix is available in the online version of the paper on _The Journal of Finance_ website. 

_The Journal of Finance[®]_ 

110 

for DEU, Paris CAC40 for FRA, FTSE MIB Index for ITA, TSX Composite Index for CAN, and S&P/ASX200 index for AUS. We obtain macroeconomic data from the Organisation for Economic Co-operation and Development (OECD) website and Federal Reserve Economic Data (FRED). 

Table I presents summary statistics for our sample of corporate bonds. After eliminating extreme values of credit spreads (those below the 0.5 percentile and above the 99.5 percentile), we take the simple average across bonds for each portfolio formed on credit ratings and maturity. We form four portfolios by credit ratings: AA+ (including AAA and AA), A, BBB, and high-yield (HY) bonds rated BB or below. Note that AUS and JPN have no HY bonds in our sample. For a given credit rating, corporate-government credit spreads are much higher than their counterparts over swap rates, and both spreads vary substantially across countries. For example, the mean BBB spread over government bonds (swap rates) ranges from 41 (26) bps in JPN to 231 (183) bps in AUS. We also compare our corporate-government credit spreads and optionadjusted spreads of ML indexes in Section I.C of the Internet Appendix and find that these two spreads for IG bonds are similar to each other. 

Years to maturity vary across countries as well. CAN and GBR have longmaturity bonds, ranging from 8.9 years (Canadian BBB bonds) to 16.6 years (Canadian A bonds) for IG bonds. In contrast, AUS and DEU have bonds of shorter maturity on average, with 3.8 years for Australian BBB bonds and German AA+ bonds and 6.3 years for Australian AA+ bonds. 

Regarding issue size (face value of bonds), CAN has the smallest average issue size, whereas the European countries have a large average issue size. In terms of the average number of bond issues per month (“Average NObs”), JPN is the second largest (even though there are no Japanese HY bonds in our sample), behind the United States. The average number of IG bonds per issuer—which measures the concentration of issuers—also varies across countries: It ranges from 5.4 for BBB to 13.5 for AA+ in JPN and from 4.6 for BBB to 12.6 for A in CAN, indicating that bonds in JPN and CAN are dominated by large issuers; the average is lower in the other countries, with AUS being the lowest (1.0, 3.2, and 2.2 bonds per issuer for AA+, A, and BBB firms, respectively). 

## **III. Structural Models without Search Frictions** 

In this section, we examine the empirical performance of two standard structural models in the global corporate bond markets. We begin with the baseline model, the main focus of the analysis. We then consider the extension of the model that allows for stationary leverage ratios. 

## _A. The Baseline Model_ 

Consider a corporate bond of fixed maturity _T_ and face value _K_ , which pays a continuous coupon at a constant rate _c_ . Default occurs when the firm value 

_The Global Credit Spread Puzzle_ 

111 

## **Table I** 

## **Summary Statistics for Corporate Bond Data** 

This table reports summary statistics for corporate bond data in the full sample. We sort bonds into portfolios based on credit rating and time to maturity every month and compute simple averages of characteristics across bonds every month. We then take averages over time for each portfolio and report the results. We consider four credit rating categories: AA+ (including AAA and AA), A, BBB, and high-yield (HY). Corporate bond credit spreads (in basis points [bps]) are computed over government bond yields or swap rates. Issue size is the face value of bonds (in USD millions). Average NObs refers to how many bonds (per month) we have in each portfolio. NBonds/Issuer represents the average number of bonds per issuer in the sample. The sample is monthly from 1997 to 2017 for the non-U.S. sample except for Australia (starting in 2007) and Italy (starting in 2003), and from 1987 to 2015 for U.S. bonds. 

||Bond Characteristics by Credit Ratings|Bond Characteristics by Credit Ratings|
|---|---|---|
||AA+<br>A<br>BBB<br>HY|AA+<br>A<br>BBB<br>HY|
|Credit spreads (in bps)<br>Over govt. bond yields<br>Over swap rates<br>Years to maturity<br>Issue size (USDmil)<br>Average NObs<br>NBonds/Issuer|Japan<br>17<br>27<br>41<br>−<br>3<br>12<br>26<br>−<br>6.5<br>5.1<br>4.2<br>−<br>344<br>311<br>278<br>−<br>94.6<br>56.8<br>61.8<br>−<br>13.5<br>7.6<br>5.4<br>−|Italy|
|||86<br>114<br>161<br>246<br>51<br>80<br>122<br>202<br>10<br>7.7<br>6.9<br>6.4<br>1340<br>1216<br>1075<br>751<br>2.0<br>11.4<br>24.2<br>4.4<br>3.6<br>5.3<br>5.6<br>5.9|
|Credit Spreads (in bps)<br>Over govt. bond yields<br>Over swap rates<br>Years to maturity<br>Issue size (USDmil)<br>Average NObs<br>NBonds/Issuer|United Kingdom<br>77<br>129<br>176<br>418<br>32<br>97<br>140<br>388<br>10.6<br>12.1<br>9.3<br>8.3<br>609<br>439<br>408<br>401<br>4.0<br>28.7<br>20.8<br>4.2<br>2.5<br>5.3<br>2.7<br>2.3|Canada|
|||82<br>99<br>160<br>344<br>56<br>76<br>139<br>324<br>16.4<br>16.6<br>8.9<br>4.7<br>100<br>153<br>220<br>181<br>1.5<br>26.0<br>47.9<br>1.6<br>5.7<br>12.6<br>4.6<br>1.5|
|Credit spreads (in bps)<br>Over govt. bond yields<br>Over swap rates<br>Years to maturity<br>Issue size (USDmil)<br>Average NObs<br>NBonds/Issuer|Germany<br>52<br>89<br>121<br>278<br>25<br>52<br>87<br>237<br>3.8<br>5.6<br>6.2<br>4.3<br>726<br>1077<br>870<br>745<br>2.1<br>17.6<br>24.0<br>6.8<br>1.8<br>4.5<br>4.7<br>3.7|Australia|
|||146<br>185<br>231<br>−<br>103<br>137<br>183<br>−<br>6.3<br>4.3<br>3.8<br>−<br>222<br>250<br>176<br>−<br>0.7<br>16.0<br>9.2<br>−<br>1.0<br>3.2<br>2.2<br>−|
|Credit spreads (in bps)<br>Over govt. bond yields<br>Over swap rates<br>Years to maturity<br>Issue size (USDmil)<br>Average NObs<br>NBonds/Issuer|France<br>59<br>87<br>136<br>295<br>24<br>53<br>100<br>256<br>5.1<br>6<br>5.6<br>4<br>896<br>853<br>715<br>689<br>7.8<br>35.9<br>39.6<br>10.5<br>4.0<br>5.5<br>3.8<br>3.8|United States|
|||71<br>99<br>166<br>415<br>33<br>59<br>127<br>381<br>6.6<br>6.9<br>6.9<br>6.8<br>565<br>409<br>358<br>300<br>56.5<br>212.2<br>276.0<br>200.3<br>4.6<br>4.8<br>4.1<br>2.9|



_The Journal of Finance[®]_ 

112 

falls to a threshold (the default boundary) the first time before or at _T_ . The risk-free interest rate _r_ is assumed to be constant. 

Under this baseline model, the price of such a defaultable bond is 

**==> picture [343 x 22] intentionally omitted <==**

where _π[Q]_ ( _t, T_ ) is the risk-neutral default probability over ( _t, T_ ], _G_ ( _t, T_ ) is the state-dependent time- _t_ price of the Arrow-Debreu default claim, and _R_ is the recovery rate (equation (1) also coincides with equation (3) of Leland and Toft (1996)). The yield to maturity, _y_ ( _t, T_ ), solves the following equation: 

**==> picture [276 x 24] intentionally omitted <==**

The model-implied credit spread is given by _s[BC]_ ( _t, T_ ) = _y_ ( _t, T_ ) − _r_ . 

Note that the baseline, BC, and Longstaff and Schwartz (1995) models all assume an exogenous, flat default boundary, although they adopt different recovery rules. It follows that the baseline model can be viewed as a variant of the BC model. We focus on this variant because it is nested within the HM model considered in Section IV (see equation (5)). Other variants used in the literature include two for discrete-coupon bonds as implemented in Bao (2009) and HH, one for zero-coupon bonds considered in FS, and two for CDS used in BGY and Huang, Shi, and Zhou (2020). We find that the four specifications used for corporate bond pricing lead to fairly similar predicted credit spreads for IG bonds with the same set of parameter values (see Section II of the Internet Appendix). Below we use the baseline model and the BC model interchangeably. 

## _B. Estimation of Input Parameters_ 

This subsection describes how to estimate the parameters of the BC model. Let _K/At_ be the leverage of firm at _t_ , _σ[A]_ be asset volatility, _δ_ be asset payout rate, _μ_ be the drift of the firm’s asset value under the physical measure P, and _θ[Q]_[(] _[K][/][A][t][, σ][ A][, δ,][ R][,][ d]_[)][be][the][vectors][of][parameters][under][Q][.][We][estimate] _BC_[:][=] _K/At_ , _σ[A]_ , and _δ_ at the firm level; _R_ , _d_ , and the Sharpe ratio (SR) at the country level; and the probability of default (PD) under P at the horizon×credit rating category level. 

## _B.1. Firm-Level Parameters_ 

We consider three different estimates of leverage: (i) quasi-market leverage, computed as book debt/(book debt+market equity); (ii) market leverage, where an approximate market value of debt is used; and (iii) leverage and asset volatility obtained jointly in the spirit of Jones, Mason, and Rosenfeld (1984, hereafter JMR); see Section III.B.3 for details. 

Besides the JMR method, we can estimate asset volatility by using either the quasi-market or market leverage. HH do so by calibrating to default rates 

_The Global Credit Spread Puzzle_ 

113 

by credit ratings. For comparison, we focus on the following estimate suggested by Schaefer and Strebulaev (2008): 

**==> picture [317 x 19] intentionally omitted <==**

where _Li,t_ is firm _i_ ’s leverage, _σi[E] ,t_[is its equity volatility,] _[ σ] i[ D] ,t_[is its debt volatility,] isanding daily stock returns with a one-year rolling window. Estimatingmore _ρi[ED] ,t_ challenging.[is the correlation between debt and stock returns. We estimate] To strike a balance between accuracy and transparency, _σi[D] ,t_[and] _[ σ] i[ E] ,t[ ρ]_[us-] _i[ED] ,t_ we estimate them in three steps. First, we compute the constant volatility for each bond using monthly returns. Second, we take the simple average across bonds within each rating category for each country to compute the average debt volatility. Third, we assign the same debt volatility for bonds in each credit-rating/country bin. For correlation, we repeat similar steps by computing correlation using monthly stock and bond returns for each bond, and then take the average for each rating and in each country. After computing asset volatility for all firms and months, we take the firm-level average over time to obtain the constant asset volatility. 

The payout ratio is the ratio of payments to outside stakeholders (dividends, share repurchases, and net interest payments) over the past year divided by the asset value. If a firm’s payout ratio is more than three times the median payout ratio in the country, we set the firm’s payout ratio to be the latter. 

Table II reports summary statistics for _K/A, σ[E] , σ[A]_ , and _δ_ based on the quasimarket leverage. To facilitate comparison across countries, we focus on BBB firms, for which we have the largest number of observations. The average _K/A_ is 0.24 (AUS), 0.31 (USA), 0.33 (CAN and GBR), 0.37 (DEU), and 0.39 (FRA), but is much higher for JPN (0.52) and ITA (0.53). The median _K/A_ is similar to the mean _K/A_ . JPN has the lowest average _δ_ , whereas CAN, ITA, and USA have the highest values. The mean _σ[A]_ is 0.13 in ITA; 0.15 in CAN; 0.18 in JPN, DEU, and FRA; 0.19 in GBR; 0.20 in AUS; and 0.26 in USA. Overall, conditional on credit ratings, there is no clear pattern in the fundamental riskiness of firms across countries. In Sections III.C and III.D, we evaluate whether the variation in fundamentals aligns with the variation in credit spreads across countries using the BC model. 

We estimate firm _i_ ’s drift parameter according to _μi,t_ = _rt_ + _SR_ · _σi[A]_[,][where] _SR_ is the country-level SR. Given _μi,t_ , we can then compute firm _i_ ’s modelimplied PD under P. 

## _B.2. Country-Level Inputs_ 

The SR of assets is needed to match the model-implied P-measure default probability to the historical default frequency. As we evaluate a structural model using bond-level data, ideally we need the SRs of individual firms. However, given that Chen, Collin-Dufresne, and Goldstein (2009) and FS use a single SR (0.22) for U.S. firms because of data limitations, we estimate one 

_The Journal of Finance[®]_ 

114 

## **Table II** 

## **Firm-Level Inputs to the Black-Cox Model** 

This table presents summary statistics for firm-level inputs to the Black and Cox (1976) model for each country and each credit rating. The inputs include the following: _K/A_ is leverage, defined as the ratio of the book value of debt to the sum of the book value of debt and the market value of equity, _σ[E]_ is annualized equity volatility, _σ[A]_ is annualized asset volatility, and _δ_ is the payout ratio. The statistics are computed using the panel data of bond issuers, and NObs is the number of firms included in each category. The sample is from 1997 to 2017 for non-U.S. firms and from 

|Rating|NObs<br>Mean<br>10%<br>50%<br>90%|NObs<br>Mean<br>10%<br>50%<br>90%|
|---|---|---|
|_K/A_<br>AA+<br>A<br>BBB<br>HY<br>_σ E_<br>AA+<br>A<br>BBB<br>HY<br>_σ A_<br>AA+<br>A<br>BBB<br>HY<br>_δ_<br>AA+<br>A<br>BBB<br>HY|Japan<br>31<br>0.44<br>0.21<br>0.42<br>0.73<br>64<br>0.46<br>0.22<br>0.46<br>0.72<br>63<br>0.52<br>0.33<br>0.52<br>0.71<br>0<br>−<br>−<br>−<br>−<br>31<br>0.26<br>0.16<br>0.24<br>0.38<br>64<br>0.31<br>0.19<br>0.29<br>0.46<br>63<br>0.37<br>0.23<br>0.36<br>0.51<br>0<br>−<br>−<br>−<br>−<br>31<br>0.15<br>0.05<br>0.15<br>0.22<br>64<br>0.17<br>0.08<br>0.17<br>0.24<br>63<br>0.18<br>0.10<br>0.17<br>0.23<br>0<br>−<br>−<br>−<br>−<br>31<br>0.009<br>0.004<br>0.008<br>0.016<br>64<br>0.008<br>0.000<br>0.007<br>0.016<br>63<br>0.005<br>0.000<br>0.004<br>0.012<br>0<br>−<br>−<br>−<br>−|Germany|
|||9<br>0.35<br>0.11<br>0.21<br>0.75<br>28<br>0.41<br>0.16<br>0.43<br>0.64<br>39<br>0.37<br>0.12<br>0.36<br>0.60<br>12<br>0.38<br>0.23<br>0.36<br>0.57<br>9<br>0.27<br>0.17<br>0.24<br>0.42<br>28<br>0.31<br>0.18<br>0.28<br>0.48<br>39<br>0.28<br>0.18<br>0.26<br>0.43<br>12<br>0.32<br>0.20<br>0.28<br>0.45<br>9<br>0.19<br>0.05<br>0.20<br>0.29<br>28<br>0.18<br>0.11<br>0.17<br>0.28<br>39<br>0.18<br>0.11<br>0.16<br>0.25<br>12<br>0.20<br>0.16<br>0.20<br>0.24<br>9<br>0.015<br>0.000<br>0.007<br>0.040<br>28<br>0.024<br>0.006<br>0.018<br>0.053<br>39<br>0.036<br>0.011<br>0.035<br>0.063<br>12<br>0.030<br>0.020<br>0.027<br>0.045|
|_K/A_<br>AA+<br>A<br>BBB<br>HY<br>_σ E_<br>AA+<br>A<br>BBB<br>HY<br>_σ A_<br>AA+<br>A<br>BBB<br>HY<br>_δ_<br>AA+<br>A<br>BBB<br>HY|United Kingdom<br>15<br>0.19<br>0.07<br>0.16<br>0.34<br>42<br>0.36<br>0.15<br>0.34<br>0.57<br>40<br>0.33<br>0.16<br>0.32<br>0.57<br>13<br>0.39<br>0.18<br>0.40<br>0.61<br>15<br>0.26<br>0.17<br>0.26<br>0.37<br>42<br>0.24<br>0.14<br>0.22<br>0.40<br>40<br>0.27<br>0.17<br>0.24<br>0.44<br>13<br>0.37<br>0.22<br>0.33<br>0.63<br>15<br>0.21<br>0.16<br>0.20<br>0.28<br>42<br>0.16<br>0.12<br>0.15<br>0.22<br>40<br>0.19<br>0.14<br>0.18<br>0.25<br>13<br>0.22<br>0.17<br>0.20<br>0.31<br>15<br>0.011<br>0.000<br>0.003<br>0.037<br>42<br>0.021<br>0.000<br>0.004<br>0.050<br>40<br>0.025<br>0.000<br>0.030<br>0.051<br>13<br>0.034<br>0.000<br>0.036<br>0.060|France|
|||9<br>0.24<br>0.07<br>0.21<br>0.48<br>24<br>0.36<br>0.08<br>0.35<br>0.65<br>39<br>0.39<br>0.16<br>0.39<br>0.59<br>18<br>0.54<br>0.27<br>0.54<br>0.78<br>9<br>0.30<br>0.19<br>0.27<br>0.48<br>24<br>0.27<br>0.17<br>0.25<br>0.43<br>39<br>0.29<br>0.18<br>0.26<br>0.45<br>18<br>0.38<br>0.23<br>0.36<br>0.57<br>9<br>0.21<br>0.15<br>0.22<br>0.29<br>24<br>0.18<br>0.11<br>0.16<br>0.26<br>39<br>0.18<br>0.11<br>0.18<br>0.25<br>18<br>0.19<br>0.11<br>0.17<br>0.26<br>9<br>0.024<br>0.008<br>0.022<br>0.045<br>24<br>0.026<br>0.000<br>0.022<br>0.055<br>39<br>0.025<br>0.003<br>0.021<br>0.049<br>18<br>0.020<br>0.005<br>0.016<br>0.044|
|||(_Continued_)|



_The Global Credit Spread Puzzle_ 

115 

**Table II** _—Continued_ 

|Rating|NObs<br>Mean<br>10%<br>50%<br>90%|NObs<br>Mean<br>10%<br>50%<br>90%|
|---|---|---|
|_K/A_<br>AA+<br>A<br>BBB<br>HY<br>_σ E_<br>AA+<br>A<br>BBB<br>HY<br>_σ A_<br>AA+<br>A<br>BBB<br>HY<br>_δ_<br>AA+<br>A<br>BBB<br>HY|Italy<br>3<br>0.26<br>0.17<br>0.27<br>0.33<br>11<br>0.40<br>0.22<br>0.41<br>0.58<br>18<br>0.53<br>0.40<br>0.53<br>0.70<br>6<br>0.61<br>0.41<br>0.66<br>0.70<br>3<br>0.24<br>0.12<br>0.21<br>0.48<br>11<br>0.24<br>0.16<br>0.22<br>0.34<br>18<br>0.26<br>0.18<br>0.25<br>0.33<br>6<br>0.34<br>0.28<br>0.33<br>0.44<br>3<br>0.17<br>0.11<br>0.19<br>0.22<br>11<br>0.15<br>0.12<br>0.14<br>0.19<br>18<br>0.13<br>0.11<br>0.13<br>0.15<br>6<br>0.15<br>0.12<br>0.13<br>0.20<br>3<br>0.052<br>0.042<br>0.054<br>0.064<br>11<br>0.045<br>0.020<br>0.050<br>0.060<br>18<br>0.048<br>0.024<br>0.046<br>0.073<br>6<br>0.065<br>0.016<br>0.089<br>0.101|Australia|
|||1<br>0.78<br>0.68<br>0.78<br>0.88<br>10<br>0.26<br>0.12<br>0.22<br>0.55<br>17<br>0.24<br>0.11<br>0.24<br>0.36<br>0<br>−<br>−<br>−<br>−<br>1<br>0.25<br>0.18<br>0.25<br>0.34<br>10<br>0.21<br>0.14<br>0.19<br>0.28<br>17<br>0.27<br>0.19<br>0.24<br>0.37<br>0<br>−<br>−<br>−<br>−<br>1<br>0.06<br>0.06<br>0.06<br>0.06<br>10<br>0.15<br>0.09<br>0.15<br>0.22<br>17<br>0.20<br>0.15<br>0.20<br>0.26<br>0<br>−<br>−<br>−<br>−<br>1<br>0.000<br>0.000<br>0.000<br>0.000<br>10<br>0.033<br>0.000<br>0.040<br>0.071<br>17<br>0.034<br>0.000<br>0.037<br>0.057<br>0<br>−<br>−<br>−<br>−|
|_K/A_<br>AA+<br>A<br>BBB<br>HY<br>_σ E_<br>AA+<br>A<br>BBB<br>HY<br>_σ A_<br>AA+<br>A<br>BBB<br>HY<br>_δ_<br>AA+<br>A<br>BBB<br>HY|Canada<br>3<br>0.37<br>0.19<br>0.41<br>0.48<br>18<br>0.36<br>0.19<br>0.36<br>0.46<br>51<br>0.33<br>0.14<br>0.32<br>0.50<br>5<br>0.39<br>0.22<br>0.36<br>0.60<br>3<br>0.24<br>0.11<br>0.27<br>0.34<br>18<br>0.19<br>0.13<br>0.17<br>0.29<br>51<br>0.22<br>0.13<br>0.19<br>0.33<br>5<br>0.33<br>0.19<br>0.30<br>0.49<br>3<br>0.14<br>0.12<br>0.13<br>0.18<br>18<br>0.13<br>0.10<br>0.12<br>0.15<br>51<br>0.15<br>0.08<br>0.14<br>0.23<br>5<br>0.20<br>0.15<br>0.20<br>0.25<br>3<br>0.048<br>0.025<br>0.046<br>0.079<br>18<br>0.038<br>0.017<br>0.039<br>0.055<br>51<br>0.034<br>0.000<br>0.035<br>0.061<br>5<br>0.045<br>0.022<br>0.044<br>0.066|United States|
|||79<br>0.16<br>0.06<br>0.15<br>0.25<br>312<br>0.23<br>0.09<br>0.19<br>0.42<br>544<br>0.31<br>0.13<br>0.29<br>0.50<br>661<br>0.48<br>0.22<br>0.46<br>0.77<br>79<br>0.24<br>0.15<br>0.23<br>0.34<br>312<br>0.29<br>0.18<br>0.27<br>0.41<br>544<br>0.33<br>0.21<br>0.31<br>0.49<br>661<br>0.49<br>0.28<br>0.44<br>0.78<br>79<br>0.23<br>0.19<br>0.22<br>0.26<br>312<br>0.25<br>0.19<br>0.23<br>0.35<br>544<br>0.26<br>0.19<br>0.25<br>0.35<br>661<br>0.30<br>0.21<br>0.28<br>0.41<br>79<br>0.040<br>0.010<br>0.041<br>0.074<br>312<br>0.046<br>0.015<br>0.041<br>0.082<br>544<br>0.047<br>0.014<br>0.041<br>0.091<br>661<br>0.043<br>0.012<br>0.037<br>0.079|



SR separately for each country. Specifically, for each stock over all Compustat firms from 1987 to 2017, we compute its SR using the stock’s average annual return and average volatility, and then take the median value in each country for its country-level SR. Panel A of Table III reports the estimated median SR based on either the one-year swap rate (labeled “median SR (swap)”) or government yield (“median SR (Govt)”) as the “risk-free” rate. The swap rate– based SR is 0.17 (ITA and JPN), 0.21 (DEU), 0.22 (AUS), 0.23 (CAN), 0.27 (GBR), 0.28 (FRA), and 0.22 (USA) following FS. The government bond yield– based SR is 0.18 (ITA), 0.20 (JPN), 0.23 (AUS, CAN, and DEU), 0.29 (FRA and GBR), and 0.22 (USA) following Chen, Collin-Dufresne, and Goldstein (2009). 

_The Journal of Finance[®]_ 

116 

## **Table III** 

## **Estimates for the Sharpe Ratio (SR) and Default Boundary** 

Panel A presents the estimate for the SR on individual stocks in each country with either the one-year swap rate or government bond yield as the risk-free rate. For each non-U.S. country, we first compute average annual returns and average volatility for each stock using the full sample of stock returns until 2017, and then the SR for each stock. We next obtain the trimmed 0.5% mean (by excluding the top and bottom 0.5%) and median SRs across firms in each non-U.S. country. For these estimates, we use all Compustat firms. The estimates of the SR for the United States are taken from Chen, Collin-Dufresne, and Goldstein (2009) and Feldhütter and Schaefer (2018). Panel B reports the estimate of default boundary ( _d_ ) obtained for each country by calibrating the Black and Cox (1976) model to either regional default rates (Panel B1) or aggregate default rates in the seven non-U.S. countries (Panel B2), based on the sample of firms that have at least one bond in the Merrill Lynch data (including callable bonds). Here, _drf[M]_[denotes][the][estimate][of] _[d]_ obtained by using method _M_ (for estimating a firm’s market asset value) and the default-free rate _rf_ , where _M_ = { _FS, BGY, HNS_ } and _rf_ = { _Govt, swap_ }. 

|Mean SR (swap)<br>Median SR (swap)<br>Mean SR (Govt)<br>Median SR (Govt)<br>Number of frms<br>Sample begins<br>_dFS_<br>_swap_<br>_dBGY_<br>_swap_<br>_dHNS_<br>_swap_<br>_dFS_<br>_govt_<br>_dBGY_<br>_govt_<br>_dHNS_<br>_govt_<br>B2.<br>_dFS_<br>_swap_<br>_dBGY_<br>_swap_<br>_dHNS_<br>_swap_<br>_dFS_<br>_govt_<br>_dBGY_<br>_govt_<br>_dHNS_<br>_govt_|Japan<br>0.22<br>0.17<br>0.23<br>0.20<br>4829<br>1987<br>0.85<br>0.84<br>0.85<br>0.82<br>0.81<br>0.77<br>Based on<br>0.86<br>0.83<br>0.79<br>0.82<br>0.81<br>0.76|U.K.<br>Germany<br>France<br>Italy<br>Canada<br>Australia<br>Panel A: Sharpe Ratios<br>0.31<br>0.25<br>0.28<br>0.19<br>0.27<br>0.28<br>0.27<br>0.21<br>0.28<br>0.17<br>0.23<br>0.22<br>0.33<br>0.26<br>0.28<br>0.19<br>0.27<br>0.28<br>0.29<br>0.23<br>0.29<br>0.18<br>0.23<br>0.23<br>3037<br>1108<br>1077<br>565<br>3664<br>1388<br>1987<br>1987<br>1987<br>1987<br>1984<br>1987<br>Panel B: Default Boundary Estimates<br>B1. Based on Regional Default Rates<br>**1.01**<br>0.91<br>**1.01**<br>0.81<br>**1.04**<br>0.94<br>**1.00**<br>0.91<br>**1.00**<br>0.80<br>**1.04**<br>0.91<br>**1.04**<br>0.90<br>**1.01**<br>0.81<br>**1.04**<br>0.93<br>1.00<br>0.85<br>0.94<br>0.78<br>**1.01**<br>0.92<br>0.95<br>0.84<br>0.94<br>0.76<br>0.98<br>0.89<br>0.97<br>0.83<br>0.93<br>0.79<br>1.00<br>0.90<br>Aggregate Default Rates in Seven Non-U.S. Countries<br>**1.01**<br>0.91<br>0.98<br>0.81<br>**1.05**<br>0.96<br>0.97<br>0.87<br>0.96<br>0.80<br>**1.04**<br>0.95<br>0.98<br>0.91<br>0.97<br>0.80<br>**1.01**<br>0.91<br>**1.01**<br>0.87<br>0.96<br>0.80<br>**1.02**<br>0.93<br>0.96<br>0.86<br>0.94<br>0.79<br>0.99<br>0.91<br>0.98<br>0.83<br>0.95<br>0.80<br>0.96<br>0.91|U.S.<br>0.22<br>0.22<br>0.86<br>0.75<br>0.81<br>0.82<br>0.73<br>0.78<br>0.86<br>0.75<br>0.81<br>0.82<br>0.73<br>0.78|
|---|---|---|---|



The SRs across countries are reasonably similar to each other. If high credit spreads in AUS reflect high risk aversion for Australian investors, then the SR in AUS must be much higher than in other countries, which we do not see in the data.[11] 

11 In an earlier version of the paper, we also estimate the median SRs using a smaller subsample of firms matched to our bond data sets. In many cases, these estimates are similar to their counterparts obtained using all firms. 

_The Global Credit Spread Puzzle_ 

117 

**==> picture [361 x 306] intentionally omitted <==**

**----- Start of picture text -----**<br>
Panel (A): U.S. Recovery Rates<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3 Annual Data<br>Moving Average<br>0.2<br>1990 1995 2000 2005 2010 2015 2020<br>Panel (B): Moving Average Recovery Rates by Region<br>0.6<br>0.4<br>U.S.<br>Other 7<br>0.2 Europe<br>Other Developed<br>Global<br>0<br>1990 1995 2000 2005 2010 2015 2020<br>**----- End of picture text -----**<br>


**Figure 1. Average recovery rates of senior unsecured debts** . This figure plots issuerweighted average recovery rates for senior unsecured debts over time. The underlying recovery data are based on trading prices at or post-default. For a given issuer, the firm-wide recovery rate is the weighted-average recovery rate across all of the issuer’s debts, where the weights are the size of the debts. Panel A presents the one-year (dashed line) and the five-year moving average (solid line) recovery rates for corporate defaults in the United States (and associated tax havens). Panel B compares the five-year moving average recovery rates across five different groups of economies: three based on geographic regions—the United States (solid blue line), Europe (green dotted line), and other developed countries (black dash-dotted line)—where regional definitions follow S&P Global Ratings; the seven non-U.S. countries in our sample (red dashed line), namely, Australia, Canada, France, Germany, Italy, Japan, and the United Kingdom; and global (magenta dash-dotted line), encompassing all countries in the Moody’s DRD database. (Color figure can be viewed at wileyonlinelibrary.com) 

The recovery rate is often assumed to be constant and equal to Moody’s estimate for senior unsecured bonds at the global level (including non-U.S. bonds) in analyzing U.S. corporate bond prices in the literature. Panel A of Figure 1 shows that there is substantial cyclical variation in corporate recovery rates in the United States over time (dashed blue line), consistent with Chen (2010). The five-year moving average (solid blue line) reflects a less noisy 

_The Journal of Finance[®]_ 

118 

representation of the time-series variation and a stronger cyclical pattern. However, a challenge we face in estimating such moving average recovery rates (MARRs) for every non-U.S. country in our sample relates to data limitations. We find that, although Moody’s DRD covers default events across countries, there are many missing values for the trading price–based recovery rates in JPN, DEU, FRA, ITA, and AUS, possibly reflecting the lack of active distressed debt markets in these countries. We therefore follow the procedures of S&P RatingsDirect by aggregating countries into four broad regions: United States (and tax havens), Europe, other developed countries (ODCs), and emerging markets.[12] 

Panel B of Figure 1 plots the MARRs for the United States (blue), Europe (green dot), and ODCs (black)—the three regions relevant to our study. The MARRs show marked divergence across regions when at least one major economy is experiencing a recession. For instance, the MARR in Europe reached its trough in the second half of our sample period (31.9%) in 2012, the turning point of the European debt crisis. Likewise, the debt crisis followed the subprime crisis in the United States and caused its recovery rate to continue to decrease from 53.0% in 2007 to 39.1% in 2012. In contrast, ODCs were less affected by the sovereign debt crisis and instead experienced an increase in the recovery rate (from 41.4% to 48.5%). Given the nontrivial time-series and cross-sectional variations in the recovery rate, we use the regional five-year MARR in our baseline analysis. Our main findings are robust to alternative measures of heterogeneous recovery rates across different markets (see Section III.C.4). 

Another important input comprises P-measure default probabilities, usually proxied by Moody’s estimates of historical default frequencies at the global level. Figure 2 plots average cumulative default rates from one to 20 years for four geographic regions by credit ratings. As in the case of recovery rates, cumulative default rates vary widely across regions. For instance, AA+ firms in the United States and Europe share similar default rates over different horizons, and this is also the case for A firms with horizons up to 12 years; however, AA+ and A firms in ODCs have substantially lower default rates. BBB firms in the United States and ODCs have similar default rates. In contrast, the HY default rates in the United States are much higher than their counterparts in the other regions, consistent with a recent finding by the S&P that the average five-year HY default rate is 16.23% for the United States and 10.23% for Europe (S&PGlobal (2020)). This finding reflects the highly developed U.S. market for high-yield debt financing, as the United States has a considerably higher share of HY companies relative to other regions. To take this heterogeneity into account, we use estimates of regional default rates for different rating categories in the determination of the default boundary ( _d_ ). 

> 12 Under the country classification of the Department of Economic and Social Affairs of the United Nations Secretariat (UN/DESA) adopted by S&P RatingsDirect, the category of Other Developed Economies includes only four countries: Australia, Canada, Japan, and New Zealand (S&PGlobal (2020)). 

_The Global Credit Spread Puzzle_ 

119 

**==> picture [359 x 280] intentionally omitted <==**

**----- Start of picture text -----**<br>
 AA+    A<br>3 6<br>U.S.<br>Europe<br>2 Other developed 4<br>Emerging<br>1 2<br>0 0<br>0 5 10 15 20 0 5 10 15 20<br> BBB   HY<br>10<br>40<br>30<br>5 20<br>10<br>0 0<br>0 5 10 15 20 0 5 10 15 20<br>Default Rate (%)<br>Default Rate (%)<br>**----- End of picture text -----**<br>


**Figure 2. Regional corporate default rates** . This figure plots issuer-weighted average cumulative default rates over various investment horizons in years by credit rating category. The four credit rating groups considered are AA+ (including both AAA and AA bonds), A, BBB, and high yield (HY). In each rating category, default rates are presented using four specific geographic regions—the United States (and tax havens), Europe, other developed countries, and emerging markets. Regional definitions follow S&P Global Ratings. Cumulative default rates are generated by averaging the multiyear default rates of regional cohorts formed at monthly intervals. (Color figure can be viewed at wileyonlinelibrary.com) 

## _B.3. Default Boundary_ 

A variety of methods have been used to estimate _d_ , such as model-free calibration (Bao (2009) and HH), estimation with bankruptcy data (Davydenko (2013)), and estimation with CDS data (BGY and Huang, Shi, and Zhou (2020)). For comparison, we follow FS and BGY and estimate _d_ by matching the model-implied P-measure default probability—which is given by, say, equation (7) with _rt_ replaced by _μt_ under the BC model—to the historical data. Given no consensus to date on how to best implement this method, we consider three alternative implementations in our analysis. Below we briefly describe the three methods (see Section III of the Internet Appendix for more details). 

The first method, proposed by FS, is to back out _d_ by minimizing the distance between historical default frequencies and the Black-Cox default probabilities 

_The Journal of Finance[®]_ 

120 

at the rating and maturity bin level. The second method comes from BGY, who show that the FS estimates of _d_ for U.S. firms are sensitive to the proxies used for firms’ asset market values. BGY propose using an estimated market value of debt rather than its book value to obtain the asset market value. The third method, referred to as HNS, is a model-based approach in which the asset market value is not explicitly approximated with some observable proxies, but rather the asset value together with asset volatility are determined via the BC model based on equity value and equity volatility in the spirit of JMR and Bao (2009). Note that under all three methods, _d_ is assumed to be the same for all firms over time in each country. If the calibration is done separately for different credit ratings in a given country, then estimates of _d_ for IG (HY) firms will be lower (higher) than the single estimate for all firms in the country. 

We implement each of the three methods using two alternative proxies for the default-free rates: government bond yields and LIBOR IRS yields. For convenience, let _drf[M]_[denote][the][estimate][of] _[d]_[obtained][by][using][method] _[M]_[and] the default-free rate _rf_ , where _M_ = { _FS, BGY, HNS_ } and _rf_ = { _Govt, swap_ }. We omit the notation _M_ and _rf_ from _drf[M]_[depending][on][the][context,][however,][if][no] confusion arises. 

Panel B of Table III reports two sets of estimates of _d_ for each country. The first is based on regional default rates (Panel B1) and is used in the baseline analysis. The other is based on aggregate default rates in the seven non-U.S. countries (Panel B2) and is used in a robustness check (see Section III.C.4). Here, we focus on Panel B1 and make four observations. First, _dswap[M][>][ d] Govt[M]_[∀] _[M]_ for all countries. This finding helps explain why the swap rate–based CSP is weaker than the government bond–based CSP. 

Second, _drf[FS]_ ≥ _drf[BGY]_ ∀ _rf_ , _drf[FS]_ ≥ _drf[HNS]_ ∀ _rf_ except for GBR when _rf_ = _swap_ or ITA when _rf_ = _Govt_ , and _drf[HNS]_ ≥ _drf[BGY]_ ∀ _rf_ except for DEU when _rf_ = _swap_ or JPN, DEU, and FRA when _rf_ = _Govt_ . That is, for a given _rf_ , _drf[FS]_ ( _drf[BGY]_ ) tends to be the highest (lowest) estimate of _d_ . We therefore focus more on _drf[FS]_ than on _drf[BGY]_ or _drf[HNS]_ in our empirical analysis, as using a higher _d_ biases against finding a CSP (see Section IV.B of the Internet Appendix). Third, CAN, ITA, and GBR all have estimates of _d_ greater than one. For instance, _dswap[M]_[=][ 1] _[.]_[04][ ∀] _[M]_[and] _[d] Govt[FS]_[=][ 1] _[.]_[01][for][CAN.][These][results][imply][that] our measure of market leverage is merely a proxy for the true leverage. If the true measure of leverage is available in the data, then _d <_ 1 _._ 0 as there is no reason for a firm to default when its equity value is positive. However, there may be debt-like obligations that are missing in the book value of debt in balance sheets. For example, firms with higher operating leverage are more likely to default than firms with low operating leverage, even if the financial leverage is the same.[13] 

Lastly, several estimates of _d_ for the U.S. market have been reported in the literature. For instance, HH obtain _dGovt_ = 0 _._ 60 by calibration (but also use 

13 We thank Bob Goldstein for pointing this out. 

_The Global Credit Spread Puzzle_ 

121 

_dGovt_ = 1 _._ 0 as a robustness check). Using a sample of defaulted firms, Davydenko (2013) estimates that _dGovt_ = 0 _._ 66. The reported estimates of _dswap_ are indeed generally higher. Huang, Shi, and Zhou (2020) obtain a median of 0.75 using a jump-diffusion structural model and single-name CDS data. FS report that _dswap[FS]_[=][ 0] _[.]_[89,][and][BGY][find][that] _[d] swap[FS]_[=][ 0] _[.]_[82.][14][These][findings][indicate] that at least in the case of the United States, _drf[FS]_[∀] _[rf]_[tends][to][be][higher][than] the estimates of _d_ obtained using the other methods. 

## _C. Is There a GCSP?_ 

Given all the inputs, we implement the BC model to calculate its modelimplied spreads over swap rates at the individual bond level. We then compare these spreads with their counterparts in the data and focus on the ability of the model to predict average IG spreads. 

## _C.1. The Baseline Results_ 

We first divide our sample of corporate bonds into 24 (3 × 8) IG/country bins and six HY/country bins and examine the ability of the model to predict the mean credit spread of each bin. Figure 3 compares the mean of predicted spreads ( _x_ -axis) from the BC( _dswap[FS]_[)][model][(pink][dot)][and][the][data][(] _[y]_[-axis)] for each of these 30 bins. If the model explains the average spread of a bin well, then its corresponding pink dot plots along the 45[◦] “fair-pricing” dashed line; if the model underpredicts (overpredicts) the mean spread, then the pink dot plots in the upper left (lower right) triangular region. Among the 24 IG/country/ _dswap[FS]_[bins,][the][pink][dot][lies][below][the][45][◦][line][for][six][of][them,] including (AA+, A, BBB)/JPN, (A, BBB)/FRA, and A/DEU, and above the line for the remaining 18 bins. For HY bonds, CAN, DEU, GBR, and USA lie above the line, while FRA and ITA below the line. Thus, visually, the model underpredicts the average spread for 18 out of 24 IG/country/ _dswap[FS]_[bins][and] for four out of six HY/country/ _dswap[FS]_[bins.] 

We next examine the statistical significance of each pink dot’s distance to the 45[◦] line. To this end, we focus on each dot’s pricing error (= model spread − actual spread) under the model. We report the MPE of the BC model for each of the 30 credit rating (CR)/country groups in rows labeled “BC( _dswap[FS]_[)”] in Panel A of Table IV. Among the 24 IG/country/ _dswap[FS]_[bins,][the][MPE][is][sig-] nificantly negative for 17 bins, including all three IG groups in AUS, ITA, GBR, and USA, (A, BBB)/CAN, and (AA+, BBB)/DEU, and AA+/FRA, ranging from −150.5 bps for BBB/AUS to −10.5 bps for BBB/DEU. As for the remaining seven IG/country/ _dswap[FS]_[bins,][the][MPE][is][significantly][positive][for][A/DEU,] 

> 14 Recall that we use only four rating categories (AA+, A, BBB, and HY) for non-U.S. bonds because of the limited sample size but seven categories (CCC through AAA) for the U.S. sample. Therefore, the weight of HY bonds is smaller for non-U.S. countries than for the United States, which helps explain why _d[BGY]_ and _d[FS]_ are rather similar for the non-U.S. countries except for GBR. 

_The Journal of Finance[®]_ 

122 

## **Table IV** 

## **Bond-Level Pricing Errors of Structural Models: Swap Rates as Default-Free Rates** 

The table summarizes the mean pricing errors (MPEs) (in bps) of three structural models in predicting corporate bond spreads over swap rates, for each of 30 different credit rating/country groups. Pricing errors are reported as the differences between the model-implied and observed spreads. The three models are those of Black and Cox (1976, BC) and Collin-Dufresne and Goldstein (2001, CDG), and He and Milbradt (2014, HM). Parameters _dswap[FS]_[,] _[d] swap[BGY]_[,] _[d] swap[HNS]_[,][and] _[d][CDG] swap_ indicate the default boundary used in the implementation of the models. The first three parameters are as defined in Table III and _d[CDG] swap_[is][obtained][by][calibrating][the][CDG][model][to][default] data. Panel A reports the MPEs of all spread observations while Panel B focuses on observations with nonnegative observed spreads. Statistics in parentheses are _t_ -statistics, with standard errors clustered by bond issue. ***, **, and * denote significance at the 1%, 5%, and 10% two-tailed level against the null hypothesis that the MPE is zero. The sample period spans from 1997 to 2017 for the non-U.S. countries and from 1987 to 2015 for the United States. 

||Panel A: Including Observations with Negative Credit Spreads|Panel A: Including Observations with Negative Credit Spreads|
|---|---|---|
|Models|AA+<br>A<br>BBB<br>HY|AA+<br>A<br>BBB<br>HY|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|Japan|Italy|
||12_._6∗∗∗<br>21_._7∗∗∗<br>33_._8∗∗∗<br>−<br>(12.7)<br>(8.1)<br>(5.0)<br>−<br>10_._0∗∗∗<br>19_._4∗∗∗<br>28_._2∗∗∗<br>−<br>(12.7)<br>(7.5)<br>(3.7)<br>−<br>7_._2∗∗∗<br>9_._2∗∗∗<br>16.4<br>−<br>(14.1)<br>(3.9)<br>(1.5)<br>−<br>19_._9∗∗∗<br>21_._0∗∗∗<br>18.9<br>−<br>(4.4)<br>(3.3)<br>(1.4)<br>−<br>33_._2∗∗∗<br>38_._6∗∗∗<br>54_._0∗∗∗<br>−<br>(24.6)<br>(18.1)<br>(13.9)<br>−|−47_._7∗∗∗<br>−78_._0∗∗∗<br>−14_._7∗<br>82.2<br>(−10.5)<br>(−17.0)<br>(−1.7)<br>(1.4)<br>−48_._2∗∗∗<br>−80_._4∗∗∗<br>−32_._4∗∗∗<br>8.5<br>(−10.3)<br>(−17.7)<br>(−4.6)<br>(0.2)<br>−33_._5∗∗∗<br>−66_._8∗∗∗<br>−20_._1∗∗∗<br>26.8<br>(−9.0)<br>(−15.9)<br>(−3.5)<br>(0.7)<br>−20_._3∗∗∗<br>−6_._3∗∗∗<br>−51_._8∗∗∗<br>−15.7<br>(−3.8)<br>(−2.6)<br>(−4.7)<br>(−1.1)<br>−15_._1∗∗<br>−26_._5∗∗∗<br>30_._2∗∗∗<br>176_._0∗∗∗<br>(−2.3)<br>(−7.1)<br>(3.4)<br>(3.2)|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_) <br>HM(_dFS_<br>_swap_)|United Kingdom|Canada|
||−27_._0∗∗∗−38_._5∗∗∗<br>−92_._3∗∗∗<br>−172_._0∗∗∗<br>(−5.0)<br>(−8.4)<br>(−10.6)<br>(−7.1)<br>−28_._3∗∗∗−59_._6∗∗∗−100_._3∗∗∗−170_._0∗∗∗<br>(−5.9)<br>(−11.5)<br>(−13.7)<br>(−6.6)<br>−11_._9∗∗∗−40_._5∗∗∗<br>−74_._8∗∗∗<br>−166_._1∗∗∗<br>(−2.7)<br>(−8.6)<br>(−10.9)<br>(−8.0)<br> −21_._8∗∗∗−34_._8∗∗∗<br>−55_._2∗∗∗<br>−127_._0∗∗<br>(−6.0)<br>(−3.9)<br>(−5.6)<br>(−2.3)<br>0.9<br>13.4<br>−26_._1∗∗∗<br>−39_._8∗∗∗<br>(0.9)<br>(1.3)<br>(−4.2)<br>(−2.7)|−5.8<br>−49_._7∗∗∗<br>−105_._4∗∗∗<br>−112.7<br>(−0.4)<br>(−13.0)<br>(−27.8)<br>(−1.4)<br>−30_._2∗<br>−58_._2∗∗∗<br>−110_._1∗∗∗<br>−136_._0∗∗<br>(−1.9)<br>(−15.9)<br>(−29.9)<br>(−2.3)<br>−10.3<br>−50_._0∗∗∗<br>−108_._4∗∗∗−146_._9∗∗∗<br>(−0.6)<br>(−12.9)<br>(−29.8)<br>(−3.3)<br>7_._9∗∗∗<br>−39_._4∗∗∗<br>−85_._8∗∗∗<br>−137_._8∗∗∗<br>(3.4)<br>(−8.4)<br>(−12.5)<br>(−3.1)<br>36_._3∗∗<br>−2.7<br>−21_._7∗∗∗<br>33.7<br>(2.1)<br>(−1.4)<br>(−12.2)<br>(0.5)|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)|Germany|Australia|
||(_Continued_)||



_The Global Credit Spread Puzzle_ 

123 

**Table IV** _—Continued_ 

||Panel A: Including Observations with Negative Credit Spreads|Panel A: Including Observations with Negative Credit Spreads|
|---|---|---|
|Models|AA+<br>A<br>BBB<br>HY|AA+<br>A<br>BBB<br>HY|
|CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|−18_._8∗∗∗<br>−11_._7∗∗∗<br>−6.1<br>113_._7∗∗<br>(−5.3)<br>(−4.0)<br>(−0.7)<br>(2.3)<br>5.1<br>60_._0∗∗∗<br>42_._2∗∗∗<br>−25_._9∗∗∗<br>(0.6)<br>(6.5)<br>(2.9)<br>(−3.9)|−61_._5∗∗∗<br>−70_._9∗∗∗<br>−43_._1∗∗∗<br>−<br>(−11.2)<br>(−4.7)<br>(−2.6)<br>−<br>5.7<br>−15_._2∗∗∗<br>−9_._8∗∗<br>−<br>(1.3)<br>(−3.6)<br>(−2.0)<br>−|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|France<br>−20_._5∗∗∗<br>58.2<br>17_._8∗∗∗<br>157_._0∗∗∗<br>(−9.3)<br>(1.5)<br>(3.3)<br>(4.0)<br>−22_._6∗∗∗<br>28.0<br>−7_._0∗∗∗<br>108_._3∗∗∗<br>(−9.8)<br>(0.3)<br>(−5.6)<br>(3.1)<br>−11_._7∗∗∗<br>32.9<br>3_._2∗∗∗<br>102_._9∗∗∗<br>(−5.8)<br>(1.1)<br>(3.9)<br>(3.7)<br>2.8<br>47_._5∗∗∗<br>−17_._4∗∗∗<br>153_._5∗<br>(0.0)<br>(3.7)<br>(−4.6)<br>(1.9)<br>13_._2∗∗∗<br>104_._7∗∗∗<br>76_._1∗∗∗<br>218_._4∗∗∗<br>(4.8)<br>(7.7)<br>(5.5)<br>(6.3)|United States<br>−18_._1∗∗∗<br>−16_._9∗∗∗<br>−32_._6∗∗∗<br>−5.5<br>(−6.2)<br>(−14.0)<br>(−14.8)<br>(−1.0)<br>−21_._5∗∗∗<br>−32_._8∗∗∗<br>−67_._3∗∗∗<br>−90_._3∗∗∗<br>(−10.3)<br>(−28.9)<br>(−34.1)<br>(−15.9)<br>−15_._5∗∗∗<br>−18_._5∗∗∗<br>−40_._9∗∗∗<br>−63_._0∗∗∗<br>(−7.7)<br>(−19.3)<br>(−23.2)<br>(−13.7)<br>−17_._6∗∗∗<br>24_._8∗∗∗<br>−56_._7∗∗∗<br>99_._2∗∗∗<br>(−13.0)<br>(4.0)<br>(−13.3)<br>(5.9)<br>10_._1∗∗∗<br>16_._3∗∗∗<br>25_._3∗∗∗<br>73_._1∗∗∗<br>(2.6)<br>(6.2)<br>(8.5)<br>(12.5)|



Panel B: Excluding Observations with Negative Credit Spreads 

|Models|AA+<br>A<br>BBB<br>HY|AA+<br>A<br>BBB<br>HY|
|---|---|---|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|Japan<br>4_._9∗∗∗<br>9_._9∗∗∗<br>9_._9∗∗∗<br>−<br>(4.7)<br>(5.8)<br>(4.5)<br>−<br>2_._1∗∗∗<br>8_._1∗∗∗<br>6_._6∗∗∗<br>−<br>(2.7)<br>(5.1)<br>(3.2)<br>−<br>1_._0∗<br>1.3<br>1.7<br>−<br>(1.8)<br>(1.2)<br>(1.0)<br>−<br>17_._9∗∗∗<br>8.8<br>13.2<br>−<br>(2.6)<br>(1.4)<br>(1.3)<br>−<br>19_._3∗∗∗<br>27_._0∗∗∗<br>31_._0∗∗∗<br>−<br>(14.1)<br>(14.2)<br>(13.6)<br>−|Italy|
|||−49_._2∗∗∗−78_._8∗∗∗<br>−15_._3∗<br>82.3<br>(−11.1)<br>(−17.0)<br>(−1.7)<br>(1.4)<br>−49_._7∗∗∗−81_._1∗∗∗<br>−32_._8∗∗∗<br>8.5<br>(−10.8)<br>(−17.8)<br>(−4.6)<br>(0.2)<br>−34_._8∗∗∗−67_._5∗∗∗<br>−20_._5∗∗∗<br>26.8<br>(−9.6)<br>(−15.9)<br>(−3.5)<br>(0.7)<br>−21_._2∗∗∗<br>−6_._7∗∗∗<br>−52_._1∗∗∗<br>−15.9<br>(−3.9)<br>(−2.6)<br>(−4.8)<br>(−1.1)<br>−17_._4∗∗<br>−27_._1∗∗∗<br>29_._6∗∗∗<br>176_._1∗∗∗<br>(−2.6)<br>(−7.2)<br>(3.4)<br>(3.2)|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_) <br>HM(_dFS_<br>_swap_)|United Kingdom<br>−34_._1∗∗∗−58_._7∗∗∗<br>−92_._3∗∗∗<br>−172_._0∗∗∗<br>(−5.7)<br>(−8.5)<br>(−10.6)<br>(−7.1)<br>−35_._7∗∗∗−68_._4∗∗∗−100_._4∗∗∗−170_._0∗∗∗<br>(−6.9)<br>(−11.7)<br>(−13.6)<br>(−6.6)<br>−17_._7∗∗∗−49_._1∗∗∗<br>−74_._9∗∗∗<br>−166_._1∗∗∗<br>(−3.2)<br>(−8.6)<br>(−10.9)<br>(−8.0)<br> −28_._1∗∗∗−34_._8∗∗∗<br>−55_._3∗∗∗<br>−127_._0∗∗<br>(−7.3)<br>(−3.9)<br>(−5.6)<br>(−2.3)<br>−6.3<br>−6.7<br>−26_._1∗∗∗<br>−39_._8∗∗∗<br>(−1.2)<br>(−1.4)<br>(−4.2)<br>(−2.7)|Canada|
|||−7.4<br>−51_._4∗∗∗−113_._0∗∗∗<br>−112.7<br>(−0.4)<br>(−13.0)<br>(−27.8)<br>(−1.4)<br>−31_._6∗<br>−59_._4∗∗∗−116_._8∗∗∗<br>−136_._0∗∗<br>(−1.9)<br>(−16.0)<br>(−29.9)<br>(−2.3)<br>−11.5<br>−51_._2∗∗∗−114_._0∗∗∗−146_._9∗∗∗<br>(−0.6)<br>(−13.0)<br>(−29.8)<br>(−3.3)<br>7_._3∗∗∗<br>−39_._9∗∗∗<br>−86_._0∗∗∗<br>−137_._8∗∗∗<br>(3.4)<br>(−8.4)<br>(−12.5)<br>(−3.1)<br>34_._8∗∗<br>−4.2<br>−29_._1∗∗∗<br>33.7<br>(2.1)<br>(−1.5)<br>(−12.2)<br>(0.5)|



( _Continued_ ) 

_The Journal of Finance[®]_ 

124 

**Table IV** _—Continued_ 

||Panel B: Excluding Observations with Negative Credit Spreads|Panel B: Excluding Observations with Negative Credit Spreads|
|---|---|---|
|Models|AA+<br>A<br>BBB<br>HY|AA+<br>A<br>BBB<br>HY|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_) <br>HM(_dFS_<br>_swap_)|Germany<br>−28_._2∗∗∗<br>−7_._8∗<br>−36_._8∗∗∗<br>−137_._2∗∗∗<br>(−7.9)<br>(−1.8)<br>(−6.0)<br>(−9.9)<br>−28_._2∗∗∗<br>−11_._2∗∗∗<br>−41_._4∗∗∗<br>−138_._3∗∗∗<br>(−8.0)<br>(−2.9)<br>(−7.1)<br>(−11.0)<br>−17_._1∗∗∗<br>−9_._1∗∗∗<br>−35_._2∗∗∗<br>−129_._2∗∗∗<br>(−5.2)<br>(−2.7)<br>(−7.1)<br>(−11.2)<br> −24_._2∗∗∗<br>−21_._5∗∗∗<br>−6.1<br>113_._7∗∗<br>(−8.8)<br>(−4.2)<br>(−0.7)<br>(2.3)<br>−0.4<br>31_._8∗∗∗<br>16_._2∗∗∗<br>−25_._9∗∗∗<br>(−0.1)<br>(6.4)<br>(2.9)<br>(−3.9)|Australia|
|||−98_._2∗∗∗<br>−124_._9∗∗∗<br>−150_._5∗∗∗<br>−<br>(−21.0)<br>(−18.1)<br>(−13.3)<br>−<br>−99_._5∗∗∗<br>−126_._4∗∗∗<br>−151_._3∗∗∗<br>−<br>(−21.1)<br>(−18.3)<br>(−13.4)<br>−<br>−94_._4∗∗∗<br>−117_._3∗∗∗<br>−129_._9∗∗∗<br>−<br>(−20.4)<br>(−20.4)<br>(−11.6)<br>−<br>−61_._5∗∗∗<br>−70_._9∗∗∗<br>−43_._1∗∗∗<br>−<br>(−11.2)<br>(−4.7)<br>(−2.6)<br>−<br>5.7<br>−15_._2∗∗∗<br>−9_._8∗∗<br>−<br>(1.3)<br>(−3.6)<br>(−2.0)<br>−|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|France<br>−24_._5∗∗∗<br>10.4<br>−23_._7∗∗∗<br>127_._6∗∗∗<br>(−9.9)<br>(1.4)<br>(−3.4)<br>(4.0)<br>−26_._7∗∗∗<br>−2.4<br>−33_._6∗∗∗<br>84_._9∗∗∗<br>(−10.5)<br>(−0.4)<br>(−5.7)<br>(3.1)<br>−14_._9∗∗∗<br>5.1<br>−20_._9∗∗∗<br>81_._7∗∗∗<br>(−6.5)<br>(1.0)<br>(−4.0)<br>(3.7)<br>−2.3<br>45_._0∗∗∗<br>−21_._1∗∗∗<br>146_._6∗<br>(−0.4)<br>(3.6)<br>(−4.7)<br>(1.9)<br>9_._9∗∗∗<br>55_._2∗∗∗<br>34_._6∗∗∗<br>188_._9∗∗∗<br>(4.2)<br>(7.6)<br>(5.5)<br>(6.3)|United States|
|||−23_._0∗∗∗<br>−24_._9∗∗∗<br>−40_._7∗∗∗<br>−7.1<br>(−6.5)<br>(−14.2)<br>(−14.8)<br>(−1.0)<br>−26_._6∗∗∗<br>−37_._6∗∗∗<br>−71_._3∗∗∗<br>−91_._2∗∗∗<br>(−11.1)<br>(−29.4)<br>(−34.2)<br>(−15.9)<br>−19_._8∗∗∗<br>−23_._3∗∗∗<br>−45_._4∗∗∗<br>−64_._0∗∗∗<br>(−8.3)<br>(−19.6)<br>(−23.2)<br>(−13.7)<br>−21_._6∗∗∗<br>22_._4∗∗∗<br>−57_._1∗∗∗<br>98_._8∗∗∗<br>(−14.8)<br>(3.8)<br>(−13.3)<br>(5.9)<br>5_._3∗<br>8_._8∗∗∗<br>17_._7∗∗∗<br>71_._7∗∗∗<br>(1.7)<br>(5.8)<br>(8.4)<br>(12.5)|



BBB/FRA, and all three in JPN. Note that although AA+/CAN lies slightly above the 45[◦] line and A/FRA below the line in Figure 3, their distances to the line are not statistically different from zero at the 10% level. While the MPEs for IG bonds are overwhelmingly negative, the results on HY bonds are more mixed. Among the six HY/country/ _dswap[FS]_[bins,][the][MPE][is][significantly][nega-] tive for DEU and GBR, insignificant for CAN, ITA, and USA, and significantly positive for FRA. 

The MPEs of models BC( _dswap[BGY]_[)][and][BC(] _[d] swap[HNS]_[),][reported][in][rows,][respec-] tively, labeled “BC( _dswap[BGY]_[)” and “BC(] _[d] swap[HNS]_[),” show patterns similar to those un-] der BC( _dswap[FS]_[),][with][the][exception][of][four][combinations:][For][AA][+][/CAN][and] BBB/FRA, the results for BC( _dswap[HNS]_[)][are][consistent][with][those][for][BC(] _[d] swap[FS]_[)] but differ from those for BC( _dswap[BGY]_[),][whose][MPEs][are][significantly][negative,] and for HY/CAN and HY/USA, the MPEs are insignificant under BC( _dswap[FS]_[)] but become significantly negative under either BC( _dswap[BGY]_[)][or][BC(] _[d] swap[HNS]_[).][These] four exceptions are consistent with the fact that _dswap[BGY]_[tends][to][be][the][lowest] of the three estimates of _d_ (Panel B of Table III). Overall, model BC( _dswap[BGY]_[)] (BC( _dswap[HNS]_[)) underpredicts the average spread for 19 (17) IG/country bins.] 

_The Global Credit Spread Puzzle_ 

125 

Taking all three estimates of _d_ into account, we find that the BC model significantly underpredicts the average level of corporate yield spreads over swap rates for 53 (17 + 19 + 17) and overpredicts for 13 (including eight bins in JPN) out of 72 IG/country/ _d_ bins. For comparison, the corresponding quantities for HY bonds are 10 and three out of 18 HY/country/ _d_ bins. 

We also examine the ability of the model to match the average IG spread at the country level. This test also helps mitigate the concern that some of our CR/country groups are small. The results for 24 IG[ctry] / _d_ bins, reported in Panel A of Table V, indicate that the MPEs of BC( _dswap[FS]_[)][are][significantly][pos-] itive for FRA and JPN, insignificantly positive for DEU, and significantly negative for the remaining five countries. The MPEs of BC( _dswap[BGY]_[)][and][BC(] _[d] swap[HNS]_[)] show similar patterns, except for DEU and FRA: The MPEs are now insignificant for FRA and significantly negative for DEU. Thus, the BC model underpredicts the mean IG spread for AUS, CAN, ITA, GBR, and USA and overpredicts for JPN. For DEU and FRA, the conclusion depends on the estimate of _d_ used: Whereas BC( _dswap[BGY]_[)][and][BC(] _[d] swap[HNS]_[)][underpredict][for][DEU][and][perform][well][for] FRA, BC( _dswap[FS]_[)][overpredicts][for][FRA][and][fits][the][observed][spread][level][well] for DEU. Overall, the BC model underpredicts the average IG spread for 17 (5 + 6 + 6) out of 24 IG[ctry] / _d_ bins. 

## _C.2. Adjusting for Negative Yield Spreads over Swap Rates in the Data_ 

One concern about the positive MPEs discussed in Section III.C.1 is that they may be driven by bonds with negative yield spreads over swap rates while the model-based spreads are nonnegative by construction. Our sample includes a nontrivial number of such negative spreads especially among AAA and AA bonds, with AUS being the only country with no negative spreads in the data (see Table VI). For instance, in the AA+ group, more than 50% of the spreads in JPN and at least 10% of the spreads in DEU, GBR, and USA are negative. For A-rated bonds, at least 25% of the spreads in JPN are negative. In the data, negative spreads account for about 8.30% of the observations in the full IG sample, and their prevalence in the international sample (14.90%) is much larger than that in the U.S. sample (2.04%). Negative spreads over swap rates are not surprising, however, as swap rates include a credit risk component and a (swap market) liquidity component (e.g., Liu, Longstaff, and Mandell (2006), Feldhütter and Lando (2008)). One way to mitigate this negative spread problem is to use overnight index swap (OIS) rates as the default-free benchmark; however, OIS rates with maturities more than two years are available only for EUR, GBP, JPY, and USD and only after 2008. Another way to do so is to use government bond yields, which we do in Section IV.D. Still, both positive Treasury-OIS spreads and negative swap-Treasury spreads are observed in the U.S. market (Klingler and Sundaresan (2019), He, Nagel, and Song (2022)). Based on these considerations, we address the issue of negative spreads over swap rates by simply excluding the corresponding observations from the sample. Doing so affects the sample size materially for JPN, which nevertheless has the largest AA+ group among the eight countries. 

_The Journal of Finance[®]_ 

126 

## **Table V** 

## **Pricing Errors for Investment-Grade Corporate Bonds at the Country Level with Swap Rates as Default-Free Rates** 

The table reports the MPEs (in bps) of three structural models—BC( _d_ ), CDG( _d_ ), and HM( _d_ )—in predicting IG corporate bond spreads over swap rates in each country. Here the default boundary _d_ used in the implementation of the models is as specified in Table IV. Pricing errors are calculated as the differences between the model-implied and observed spreads. Panel A is based on the full sample, Panel B on the sample of observations with nonnegative observed spreads, Panel C on the sample of industrial bond issuers, and Panel D on the sample of observations with nonnegative observed spreads for industrial bond issuers. Statistics in parentheses are _t_ -statistics, with standard errors clustered by bond issue. ***, **, and * denote significance at the 1%, 5%, and 10% two-tailed level against the null hypothesis that the MPE is zero. The sample period spans from 1997 to 2017 for the non-U.S. countries and from 1987 to 2015 for the United States. 

|Model<br>BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|Japan<br>U.K.<br>Panel A: Full<br>20_._5∗∗∗<br>−62_._1∗∗∗<br>(12.4)<br>(−12.9)<br>17_._2∗∗∗<br>−76_._1∗∗∗<br>(11.0)<br>(−16.7)<br>10_._2∗∗∗<br>−54_._2∗∗∗<br>(8.2)<br>(−13.0)<br>19_._9∗∗∗<br>−43_._2∗∗∗<br>(4.7)<br>(−6.9)<br>40_._0∗∗∗<br>−5_._3∗∗∗<br>(26.1)<br>(−3.8)|Germany<br>France<br>Italy<br>Canada<br>Australia<br>Sample Including Negative Credit Spreads<br>1.4<br>32_._2∗<br>−35_._9∗∗∗<br>−88_._8∗∗∗<br>−133_._3∗∗∗<br>(0.1)<br>(1.8)<br>(−5.7)<br>(−22.7)<br>(−21.4)<br>−6_._6∗∗∗<br>6.9<br>−48_._0∗∗∗<br>−94_._7∗∗∗<br>−134_._6∗∗∗<br>(−4.1)<br>(1.1)<br>(−9.6)<br>(−25.6)<br>(−21.6)<br>−7_._1∗∗∗<br>14.8<br>−35_._1∗∗∗<br>−91_._0∗∗∗<br>−121_._2∗∗∗<br>(−4.3)<br>(0.2)<br>(−8.4)<br>(−23.5)<br>(−21.8)<br>−9_._0∗∗<br>12.3<br>−36_._2∗∗∗<br>−71_._8∗∗∗<br>−60_._8∗∗∗<br>(−2.3)<br>(1.6)<br>(−4.6)<br>(−13.0)<br>(−5.4)<br>47_._6∗∗∗<br>83_._4∗∗∗<br>10_._4∗<br>−15_._8∗∗∗<br>−12_._7∗∗∗<br>(5.2)<br>(9.5)<br>(1.7)<br>(−9.8)<br>(−3.8)|U.S.<br>−25_._9∗∗∗<br>(−15.6)<br>−51_._5∗∗∗<br>(−38.2)<br>−30_._9∗∗∗<br>(−25.5)<br>−24_._3∗∗∗<br>(−7.3)<br>20_._9∗∗∗<br>(11.1)|
|---|---|---|---|



|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)<br>BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|Panel B: Full<br>9_._3∗∗∗<br>−72_._8∗∗∗<br>(7.6)<br>(−13.1)<br>6_._5∗∗∗<br>−81_._3∗∗∗<br>(5.6)<br>(−17.0)<br>2_._0∗∗<br>−59_._3∗∗∗<br>(2.3)<br>(−13.2)<br>13_._5∗∗∗<br>−43_._9∗∗∗<br>(2.7)<br>(−6.9)<br>27_._3∗∗∗<br>−15_._5∗∗∗<br>(20.4)<br>(−3.9)<br>Panel C: Industrial<br>23_._6∗∗∗<br>−84_._6∗∗∗<br>(13.4)<br>(−14.0)<br>19_._7∗∗∗<br>−89_._5∗∗∗<br>(12.2)<br>(−16.0)<br>12_._3∗∗∗<br>−65_._0∗∗∗<br>(10.2)<br>(−12.3)<br>23_._9∗∗∗<br>−47_._5∗∗∗<br>(5.0)<br>(−5.8)<br>42_._6∗∗∗<br>−24_._3∗∗∗<br>(24.5)<br>(−6.3)|Sample Excluding Negative Credit Spreads<br>−23_._9∗∗∗<br>−7.3<br>−36_._3∗∗∗<br>−94_._7∗∗∗<br>−133_._3∗∗∗<br>−33_._4∗∗∗<br>(−5.7)<br>(−1.4)<br>(−5.8)<br>(−23.1)<br>(−21.4)<br>(−18.6)<br>−27_._9∗∗∗<br>−18_._4∗∗∗<br>−48_._4∗∗∗<br>−99_._9∗∗∗<br>−134_._6∗∗∗<br>−56_._2∗∗∗<br>(−7.1)<br>(−4.4)<br>(−9.7)<br>(−26.0)<br>(−21.6)<br>(−40.7)<br>−23_._4∗∗∗<br>−8_._2∗∗<br>−35_._5∗∗∗<br>−95_._4∗∗∗<br>−121_._2∗∗∗<br>−35_._6∗∗∗<br>(−7.0)<br>(−2.2)<br>(−8.4)<br>(−23.8)<br>(−21.8)<br>(−28.1)<br>−13_._0∗∗<br>8.0<br>−36_._6∗∗∗<br>−72_._2∗∗∗<br>−60_._8∗∗∗<br>−26_._5∗∗∗<br>(−2.4)<br>(1.4)<br>(−4.6)<br>(−13.0)<br>(−5.4)<br>(−7.7)<br>22_._6∗∗∗<br>43_._6∗∗∗<br>10_._0∗<br>−21_._4∗∗∗<br>−12_._7∗∗∗<br>14_._2∗∗∗<br>(5.6)<br>(9.0)<br>(1.7)<br>(−10.3)<br>(−3.8)<br>(10.1)<br>Bond Issuers Including Negative Credit Spreads<br>−1.6<br>−24_._2∗∗∗<br>−37_._0∗∗∗<br>−99_._5∗∗∗<br>−133_._7∗∗∗<br>−30_._0∗∗∗<br>(−1.5)<br>(−4.7)<br>(−3.8)<br>(−25.0)<br>(−19.4)<br>(−16.3)<br>−8_._0∗∗<br>−32_._0∗∗∗<br>−43_._0∗∗∗<br>−104_._6∗∗∗<br>−134_._2∗∗∗<br>−49_._9∗∗∗<br>(−2.3)<br>(−7.0)<br>(−5.0)<br>(−28.1)<br>(−19.4)<br>(−34.1)<br>−9_._8∗∗∗<br>−20_._3∗∗∗<br>−35_._9∗∗∗<br>−99_._7∗∗∗<br>−120_._0∗∗∗<br>−31_._6∗∗∗<br>(−2.8)<br>(−5.1)<br>(−5.5)<br>(−26.3)<br>(−19.6)<br>(−24.1)<br>−8_._9∗<br>13_._6∗<br>−40_._6∗∗<br>−71_._4∗∗∗<br>−57_._6∗∗∗<br>−13_._6∗∗∗<br>(−1.9)<br>(1.7)<br>(−2.3)<br>(−12.7)<br>(−5.3)<br>(−3.5)<br>43_._8∗∗∗<br>27_._1∗∗∗<br>9.1<br>−19_._1∗∗∗<br>−11_._0∗∗∗<br>13_._9∗∗∗<br>(3.9)<br>(4.9)<br>(1.0)<br>(−9.8)<br>(−3.2)<br>(9.2)<br>(_Continued_)|
|---|---|---|



_The Global Credit Spread Puzzle_ 

127 

**Table V** _—Continued_ 

|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|Panel D: Industrial Bond Issuers Excluding Negative Credit<br>15_._6∗∗∗<br>−86_._1∗∗∗<br>−24_._1∗∗∗<br>−30_._9∗∗∗<br>−37_._1∗∗∗<br>−106_._1∗∗∗<br>(9.2)<br>(−14.2)<br>(−4.2)<br>(−6.3)<br>(−3.8)<br>(−26.2)<br>11_._9∗∗∗<br>−91_._1∗∗∗<br>−27_._4∗∗∗<br>−37_._1∗∗∗<br>−43_._1∗∗∗<br>−110_._5∗∗∗<br>(7.6)<br>(−16.3)<br>(−4.9)<br>(−8.7)<br>(−5.0)<br>(−29.2)<br>6_._2∗∗∗<br>−66_._3∗∗∗<br>−24_._5∗∗∗<br>−24_._6∗∗∗<br>−36_._0∗∗∗<br>−104_._6∗∗∗<br>(5.3)<br>(−12.5)<br>(−5.5)<br>(−6.5)<br>(−5.5)<br>(−27.1)<br>17_._8∗∗∗<br>−48_._4∗∗∗<br>−13_._2∗∗<br>12.0<br>−40_._7∗∗<br>−71_._6∗∗∗<br>(3.1)<br>(−5.9)<br>(−2.1)<br>(1.6)<br>(−2.3)<br>(−12.7)<br>33_._9∗∗∗<br>−25_._3∗∗∗<br>21_._8∗∗∗<br>20_._5∗∗∗<br>9.0<br>−25_._4∗∗∗<br>(18.8)<br>(−6.4)<br>(4.0)<br>(4.6)<br>(1.0)<br>(−11.1)|Spreads<br>−133_._7∗∗∗<br>(−19.4)<br>−134_._2∗∗∗<br>(−19.4)<br>−120_._0∗∗∗<br>(−19.6)<br>−57_._6∗∗∗<br>(−5.3)<br>−11_._0∗∗∗<br>(−3.2)|−32_._7∗∗∗<br>(−17.4)<br>−52_._4∗∗∗<br>(−35.1)<br>−33_._7∗∗∗<br>(−25.1)<br>−15_._7∗∗∗<br>(−3.9)<br>12_._1∗∗∗<br>(8.5)|
|---|---|---|---|



Panel B of Table IV reports the MPEs for the sample of positive spreads only, providing a fairer assessment of the pricing performance of the BC model than Panel A of the table. As expected, removing negative spreads lowers the MPE and has the largest impact on the AA+ group. For instance, under model BC( _dswap[FS]_[),][the][MPE][for][AA][+][bonds][decreases][by][more][than][4][bps][for] all countries except ITA, CAN, and AUS (the three countries with very few observations of negative spreads, as suggested by Panel A of Table VI), and the number of IG/country bins with a significantly negative (positive) MPE increases (decreases) from 17 to 19 (from five to three). If we consider all three estimates of _d_ , the model significantly underpredicts the mean of nonnegative credit spreads over swap rates for 58 and overpredicts for seven (all in JPN) out of 72 IG/country/ _d_ bins. In contrast, excluding negative spreads has little impact on the results for HY bonds qualitatively. 

Panel B of Table V reports the MPEs for IG bonds at the country level based on positive spreads only. Compared with the case not adjusted for negative spreads (Panel A of the table), the BC model underpredicts the average IG spread for 20 (versus 17 before) and overpredicts for three (versus four before) out of the 24 IG[ctry] / _d_ bins. 

In summary, in this subsection we control for negative yield spreads over swap rates by excluding those observations with such spreads from the analysis. Doing so, we obtain considerably stronger evidence of a CSP at both the CR/country and country levels. 

## _C.3. Evidence Based on Industrial Firms Only_ 

The sample of bond issuers used so far includes utility firms. Given that the empirical literature on structural models typically focuses on U.S. industrial firms, we rerun the baseline analysis using industrial firms only (see Section IV.C of the Internet Appendix). Below we summarize the main findings. 

We begin with the results for the 72 IG/country/ _d_ bins allowing for negative spreads. Compared with Panel A of Table IV for the full sample, the number of IG/country/ _d_ bins with a significantly negative (positive) MPE increases 

_The Journal of Finance[®]_ 

128 

|**Table VI**<br>**Percentiles of Predicted and Observed Credit Spreads over Swap Rates**<br>This table reports summary statistics for the distributions of observed credit spreads (in bps) and predicted spreads (in bps) for each of eight countries<br>by four credit rating groups, AA+(Panel A), A (Panel B), BBB (Panel C), and HY (Panel D). Predicted spreads are generated using the BC(_d_), CDG(_d_),<br>and HM(_d_) models, where the default boundary_d_is as specifed in TableIV. Statistics are computed using panel data from 1997 to 2017 for the non-<br>U.S. countries and from 1987 to 2015 for the United States.|Data/Model<br>Mean<br>10%<br>25%<br>50%<br>75%<br>90%<br>99%<br>Mean<br>10%<br>25%<br>50%<br>75%<br>90%<br>99%|Panel A: Yield Spreads for AA+Bonds<br>Panel B: Yield Spreads for A Bonds<br>Japan<br>Observed<br>1<br>−9<br>−5<br>−0<br>5<br>13<br>38<br>8<br>−6<br>−1<br>5<br>14<br>25<br>67<br>BC(_dFS_<br>_swap_)<br>14<br>0<br>0<br>1<br>16<br>47<br>112<br>30<br>0<br>0<br>7<br>36<br>87<br>257<br>BC(_dBGY_<br>_swap_)<br>11<br>0<br>0<br>1<br>15<br>42<br>75<br>28<br>0<br>0<br>7<br>33<br>81<br>235<br>BC(_dHNS_<br>_swap_)<br>9<br>0<br>0<br>0<br>8<br>30<br>81<br>17<br>0<br>0<br>2<br>20<br>53<br>160<br>CDG(_dCDG_<br>_swap_)<br>21<br>0<br>1<br>1<br>2<br>28<br>523<br>29<br>1<br>1<br>3<br>26<br>61<br>422<br>HM(_dFS_<br>_swap_)<br>35<br>4<br>6<br>23<br>53<br>88<br>132<br>47<br>8<br>16<br>31<br>54<br>104<br>269<br>U.K.<br>Observed<br>33<br>−1<br>11<br>34<br>50<br>65<br>93<br>106<br>33<br>54<br>85<br>128<br>196<br>499<br>BC(_dFS_<br>_swap_)<br>6<br>0<br>0<br>0<br>1<br>7<br>140<br>67<br>0<br>0<br>9<br>49<br>148<br>1648<br>BC(_dBGY_<br>_swap_)<br>5<br>0<br>0<br>0<br>1<br>7<br>102<br>46<br>0<br>0<br>6<br>35<br>102<br>728<br>BC(_dHNS_<br>_swap_)<br>21<br>7<br>12<br>17<br>25<br>31<br>115<br>65<br>5<br>14<br>27<br>67<br>144<br>692<br>CDG(_dCDG_<br>_swap_)<br>11<br>3<br>4<br>11<br>15<br>20<br>29<br>71<br>17<br>32<br>58<br>81<br>100<br>426<br>HM(_dFS_<br>_swap_)<br>34<br>4<br>11<br>26<br>38<br>81<br>155<br>119<br>24<br>40<br>71<br>113<br>210<br>1696<br>Germany<br>Observed<br>27<br>−1<br>10<br>28<br>39<br>48<br>104<br>54<br>13<br>22<br>39<br>63<br>102<br>353<br>BC(_dFS_<br>_swap_)<br>4<br>0<br>0<br>0<br>1<br>7<br>98<br>74<br>0<br>0<br>11<br>80<br>199<br>937<br>BC(_dBGY_<br>_swap_)<br>4<br>0<br>0<br>0<br>1<br>7<br>101<br>68<br>0<br>0<br>9<br>67<br>176<br>918<br>BC(_dHNS_<br>_swap_)<br>15<br>6<br>9<br>12<br>15<br>18<br>134<br>63<br>1<br>4<br>16<br>72<br>161<br>644<br>CDG(_dCDG_<br>_swap_)<br>8<br>2<br>5<br>7<br>10<br>13<br>31<br>42<br>2<br>8<br>24<br>43<br>62<br>457<br>HM(_dFS_<br>_swap_)<br>32<br>7<br>10<br>20<br>40<br>80<br>147<br>114<br>22<br>34<br>62<br>118<br>240<br>981<br>France<br>Observed<br>36<br>1<br>10<br>26<br>50<br>82<br>168<br>58<br>14<br>25<br>47<br>74<br>112<br>236<br>BC(_dFS_<br>_swap_)<br>15<br>0<br>0<br>1<br>13<br>45<br>196<br>116<br>0<br>0<br>7<br>160<br>382<br>917<br>BC(_dBGY_<br>_swap_)<br>13<br>0<br>0<br>1<br>12<br>37<br>172<br>86<br>0<br>0<br>6<br>120<br>276<br>735<br>BC(_dHNS_<br>_swap_)<br>24<br>1<br>5<br>13<br>29<br>61<br>153<br>90<br>1<br>3<br>24<br>133<br>268<br>599|(_Continued_)|
|---|---|---|---|



_The Global Credit Spread Puzzle_ 

129 

|Data/Model<br>Mean<br>10%<br>25%<br>50%<br>75%<br>90%<br>99%<br>Mean<br>10%<br>25%<br>50%<br>75%<br>90%<br>99%|CDG(_dCDG_<br>_swap_)<br>39<br>8<br>15<br>38<br>52<br>75<br>144<br>105<br>2<br>29<br>58<br>109<br>226<br>858<br>HM(_dFS_<br>_swap_)<br>49<br>7<br>19<br>37<br>66<br>96<br>244<br>162<br>29<br>42<br>68<br>209<br>430<br>959<br>Italy<br>Observed<br>53<br>12<br>29<br>49<br>74<br>95<br>139<br>111<br>32<br>51<br>91<br>143<br>235<br>381<br>BC(_dFS_<br>_swap_)<br>5<br>0<br>0<br>2<br>6<br>14<br>26<br>33<br>0<br>0<br>7<br>42<br>100<br>270<br>BC(_dBGY_<br>_swap_)<br>4<br>0<br>0<br>2<br>6<br>12<br>25<br>31<br>0<br>0<br>5<br>36<br>90<br>269<br>BC(_dHNS_<br>_swap_)<br>19<br>5<br>8<br>12<br>19<br>49<br>99<br>44<br>1<br>6<br>20<br>64<br>117<br>258<br>CDG(_dCDG_<br>_swap_)<br>33<br>8<br>10<br>30<br>46<br>75<br>100<br>105<br>38<br>60<br>88<br>131<br>207<br>304<br>HM(_dFS_<br>_swap_)<br>37<br>9<br>16<br>25<br>47<br>79<br>161<br>85<br>17<br>30<br>59<br>119<br>189<br>325<br>Canada<br>Observed<br>55<br>19<br>29<br>39<br>50<br>104<br>237<br>74<br>21<br>36<br>60<br>92<br>135<br>314<br>BC(_dFS_<br>_swap_)<br>49<br>2<br>5<br>16<br>92<br>131<br>271<br>24<br>0<br>1<br>8<br>25<br>54<br>292<br>BC(_dBGY_<br>_swap_)<br>24<br>1<br>3<br>6<br>40<br>68<br>185<br>16<br>0<br>0<br>4<br>15<br>36<br>187<br>BC(_dHNS_<br>_swap_)<br>44<br>11<br>15<br>28<br>72<br>95<br>173<br>24<br>1<br>4<br>10<br>27<br>58<br>201<br>CDG(_dCDG_<br>_swap_)<br>62<br>28<br>35<br>47<br>67<br>111<br>227<br>34<br>8<br>16<br>25<br>38<br>55<br>278<br>HM(_dFS_<br>_swap_)<br>91<br>45<br>52<br>64<br>121<br>178<br>295<br>71<br>13<br>25<br>51<br>91<br>153<br>366<br>Australia<br>Observed<br>102<br>47<br>59<br>93<br>157<br>164<br>181<br>129<br>58<br>78<br>115<br>157<br>200<br>498<br>BC(_dFS_<br>_swap_)<br>4<br>0<br>0<br>1<br>4<br>12<br>23<br>4<br>0<br>0<br>0<br>0<br>11<br>67<br>BC(_dBGY_<br>_swap_)<br>2<br>0<br>0<br>0<br>5<br>7<br>11<br>3<br>0<br>0<br>0<br>0<br>7<br>52<br>BC(_dHNS_<br>_swap_)<br>7<br>2<br>4<br>7<br>12<br>13<br>15<br>12<br>1<br>2<br>4<br>11<br>21<br>152<br>CDG(_dCDG_<br>_swap_)<br>40<br>30<br>38<br>42<br>45<br>46<br>48<br>58<br>12<br>18<br>26<br>39<br>63<br>716<br>HM(_dFS_<br>_swap_)<br>107<br>22<br>69<br>98<br>160<br>169<br>181<br>114<br>31<br>52<br>89<br>164<br>203<br>493<br>U.S.<br>Observed<br>26<br>−1<br>7<br>16<br>31<br>60<br>176<br>54<br>9<br>20<br>37<br>67<br>113<br>305<br>BC(_dFS_<br>_swap_)<br>8<br>0<br>0<br>0<br>1<br>9<br>140<br>37<br>0<br>0<br>2<br>24<br>104<br>541<br>BC(_dBGY_<br>_swap_)<br>4<br>0<br>0<br>0<br>1<br>5<br>74<br>21<br>0<br>0<br>1<br>12<br>57<br>331<br>BC(_dHNS_<br>_swap_)<br>10<br>0<br>1<br>6<br>11<br>17<br>96<br>36<br>2<br>6<br>13<br>36<br>91<br>346<br>CDG(_dCDG_<br>_swap_)<br>8<br>0<br>0<br>2<br>6<br>18<br>117<br>79<br>0<br>2<br>15<br>57<br>169<br>1333<br>HM(_dFS_<br>_swap_)<br>36<br>3<br>5<br>12<br>36<br>110<br>262<br>70<br>7<br>15<br>36<br>77<br>173<br>562|(_Continued_)|
|---|---|---|



_The Journal of Finance[®]_ 

130 

|Data/Model<br>Mean<br>10%<br>25%<br>50%<br>75%<br>90%<br>99%<br>Mean<br>10%<br>25%<br>50%<br>75%<br>90%<br>99%|Panel C: Yield Spreads for BBB Bonds<br>Panel D: Yield Spreads for High-Yield Bonds<br>Japan<br>Observed<br>25<br>3<br>8<br>16<br>30<br>55<br>155<br>BC(_dFS_<br>_swap_)<br>59<br>0<br>1<br>17<br>68<br>156<br>615<br>BC(_dBGY_<br>_swap_)<br>53<br>0<br>1<br>15<br>62<br>141<br>542<br>BC(_dHNS_<br>_swap_)<br>42<br>0<br>1<br>12<br>51<br>110<br>394<br>CDG(_dCDG_<br>_swap_)<br>44<br>2<br>3<br>6<br>21<br>47<br>1058<br>HM(_dFS_<br>_swap_)<br>79<br>11<br>23<br>43<br>89<br>174<br>634<br>U.K.<br>Observed<br>157<br>67<br>91<br>125<br>180<br>264<br>781<br>425<br>201<br>267<br>352<br>470<br>795<br>1220<br>BC(_dFS_<br>_swap_)<br>65<br>0<br>3<br>20<br>61<br>182<br>608<br>253<br>1<br>39<br>136<br>314<br>654<br>1696<br>BC(_dBGY_<br>_swap_)<br>57<br>0<br>2<br>14<br>46<br>143<br>670<br>255<br>1<br>26<br>111<br>300<br>706<br>1633<br>BC(_dHNS_<br>_swap_)<br>83<br>4<br>15<br>36<br>97<br>203<br>585<br>259<br>6<br>47<br>138<br>319<br>715<br>1318<br>CDG(_dCDG_<br>_swap_)<br>102<br>18<br>35<br>79<br>122<br>188<br>594<br>298<br>41<br>90<br>160<br>368<br>755<br>1629<br>HM(_dFS_<br>_swap_)<br>131<br>30<br>57<br>91<br>142<br>271<br>696<br>385<br>136<br>195<br>284<br>420<br>798<br>1753<br>Germany<br>Observed<br>82<br>21<br>38<br>64<br>103<br>160<br>354<br>232<br>83<br>117<br>171<br>265<br>443<br>1220<br>BC(_dFS_<br>_swap_)<br>71<br>0<br>0<br>7<br>54<br>187<br>1091<br>95<br>0<br>1<br>24<br>101<br>229<br>1107<br>BC(_dBGY_<br>_swap_)<br>61<br>0<br>0<br>6<br>45<br>149<br>862<br>94<br>0<br>1<br>18<br>87<br>211<br>1368<br>BC(_dHNS_<br>_swap_)<br>63<br>1<br>4<br>14<br>62<br>171<br>723<br>103<br>0<br>2<br>20<br>107<br>228<br>1318<br>CDG(_dCDG_<br>_swap_)<br>76<br>2<br>15<br>46<br>95<br>192<br>456<br>347<br>15<br>130<br>295<br>500<br>816<br>1168<br>HM(_dFS_<br>_swap_)<br>124<br>31<br>46<br>71<br>119<br>247<br>1153<br>206<br>62<br>90<br>134<br>230<br>392<br>1536<br>France<br>Observed<br>105<br>24<br>45<br>79<br>129<br>211<br>534<br>264<br>80<br>134<br>219<br>338<br>513<br>1179<br>BC(_dFS_<br>_swap_)<br>123<br>0<br>1<br>18<br>123<br>351<br>1440<br>421<br>2<br>42<br>230<br>640<br>1153<br>1696<br>BC(_dBGY_<br>_swap_)<br>98<br>0<br>1<br>15<br>97<br>287<br>982<br>373<br>1<br>26<br>174<br>536<br>1084<br>1633<br>BC(_dHNS_<br>_swap_)<br>109<br>1<br>7<br>36<br>126<br>304<br>897<br>367<br>14<br>65<br>222<br>560<br>1001<br>1318<br>CDG(_dCDG_<br>_swap_)<br>88<br>20<br>54<br>92<br>118<br>141<br>232<br>418<br>18<br>54<br>146<br>505<br>1090<br>3575<br>HM(_dFS_<br>_swap_)<br>181<br>42<br>60<br>90<br>187<br>416<br>1500<br>483<br>88<br>131<br>300<br>670<br>1179<br>1753|(_Continued_)|
|---|---|---|



131 

|Data/Model<br>Mean<br>10%<br>25%<br>50%<br>75%<br>90%<br>99%<br>Mean<br>10%<br>25%<br>50%<br>75%<br>90%<br>99%|Italy<br>Observed<br>114<br>24<br>42<br>75<br>150<br>266<br>478<br>186<br>54<br>102<br>172<br>238<br>333<br>576|BC(_dFS_<br>_swap_)<br>99<br>0<br>2<br>23<br>104<br>344<br>759<br>268<br>1<br>12<br>132<br>496<br>782<br>1084|BC(_dBGY_<br>_swap_)<br>81<br>0<br>1<br>14<br>74<br>275<br>715<br>194<br>0<br>7<br>77<br>344<br>596<br>827|_The Global Credit Spread_<br>BC(_dHNS_<br>_swap_)<br>94<br>2<br>13<br>42<br>108<br>278<br>574<br>212<br>24<br>55<br>125<br>355<br>536<br>694<br>CDG(_dCDG_<br>_swap_)<br>62<br>0<br>25<br>51<br>80<br>122<br>462<br>170<br>9<br>68<br>144<br>233<br>358<br>703<br>HM(_dFS_<br>_swap_)<br>144<br>12<br>35<br>80<br>170<br>399<br>818<br>362<br>91<br>129<br>257<br>559<br>838<br>1124<br>Canada<br>Observed<br>146<br>57<br>83<br>123<br>176<br>241<br>613<br>336<br>145<br>197<br>271<br>427<br>584<br>1051<br>BC(_dFS_<br>_swap_)<br>41<br>0<br>0<br>3<br>26<br>81<br>746<br>223<br>0<br>2<br>33<br>294<br>843<br>1502<br>BC(_dBGY_<br>_swap_)<br>36<br>0<br>0<br>2<br>19<br>66<br>874<br>200<br>0<br>2<br>27<br>243<br>744<br>1312<br>BC(_dHNS_<br>_swap_)<br>37<br>1<br>1<br>5<br>27<br>83<br>597<br>189<br>5<br>10<br>37<br>319<br>629<br>989<br>CDG(_dCDG_<br>_swap_)<br>60<br>26<br>40<br>50<br>64<br>87<br>211<br>198<br>5<br>36<br>126<br>256<br>605<br>783<br>HM(_dFS_<br>_swap_)<br>124<br>45<br>61<br>85<br>132<br>218<br>782<br>369<br>78<br>133<br>230<br>480<br>914<br>1569<br>Australia<br>Observed<br>164<br>72<br>98<br>142<br>191<br>260<br>608<br>BC(_dFS_<br>_swap_)<br>14<br>0<br>0<br>0<br>2<br>14<br>319<br>BC(_dBGY_<br>_swap_)<br>13<br>0<br>0<br>0<br>2<br>11<br>265|_Puzzle_<br>BC(_dHNS_<br>_swap_)<br>35<br>2<br>4<br>8<br>26<br>61<br>383<br>CDG(_dCDG_<br>_swap_)<br>121<br>39<br>56<br>75<br>140<br>250<br>619<br>HM(_dFS_<br>_swap_)<br>155<br>53<br>75<br>120<br>205<br>273<br>604|U.S.<br>Observed<br>131<br>32<br>49<br>91<br>161<br>272<br>679<br>398<br>99<br>193<br>352<br>534<br>743<br>1220|BC(_dFS_<br>_swap_)<br>98<br>0<br>3<br>29<br>116<br>280<br>841<br>393<br>12<br>70<br>241<br>567<br>1048<br>1696|BC(_dBGY_<br>_swap_)<br>63<br>0<br>1<br>14<br>68<br>180<br>620<br>308<br>5<br>39<br>159<br>417<br>859<br>1633|BC(_dHNS_<br>_swap_)<br>90<br>7<br>15<br>47<br>114<br>229<br>592<br>335<br>27<br>87<br>232<br>481<br>823<br>1318|CDG(_dCDG_<br>_swap_)<br>74<br>0<br>1<br>6<br>53<br>198<br>1087<br>492<br>4<br>25<br>166<br>628<br>1593<br>3053|HM(_dFS_<br>_swap_)<br>156<br>26<br>47<br>97<br>194<br>352<br>901<br>471<br>89<br>177<br>345<br>621<br>1090<br>1753|
|---|---|---|---|---|---|---|---|---|---|---|---|



_The Journal of Finance[®]_ 

132 

(decreases) from 53 to 57 (from 13 to 10). The most notable changes occur in the six (A, BBB)/FRA/ _d_ bins—where the number of bins with a significantly negative MPE increases from one to six—and the three A/DEU/ _d_ bins, where the number of bins with a significantly positive MPE decreases from three to one. Such changes are due to state-owned bond issuers (see Section II), most of which are classified as utility firms.[15] Controlling for negative spreads, the number of IG/country/ _d_ bins with a significantly negative MPE increases further to 62 and the nine IG/JPN/ _d_ bins are the only ones with a significantly positive MPE. The results for the 18 HY/country/ _d_ bins are qualitatively the same as their counterparts in the base case, except that the MPE for HY/USA/ _d[FS]_ is now significantly negative whereas it is insignificant before. 

Panels C and D of Table V report the MPEs for IG bonds issued by industrial firms at the country level with and without observations with negative spreads included, respectively. Compared with the results in Panels A and B for the full sample, FRA is affected the most: All three of its IG[FRA] _/d_ bins now have an MPE that is significantly negative at the 1% level. In contrast, the three IG[JPN] / _d_ bins all continue to have a significantly positive MPE. Overall, 20 (21) out of 24 IG[ctry] / _d_ bins in Panel C (Panel D) show a significantly negative MPE. 

To summarize, we find stronger evidence of a CSP in industrial firms relative to the full sample. In particular, the BC model significantly underpredicts the mean IG spread at the country level for all eight countries except Japan once negative yield spreads are excluded from the sample. 

## _C.4. Additional Robustness Checks_ 

In this subsection, we conduct two additional robustness tests: one based on the sample that consists of all bonds from the seven non-U.S. countries and the other based on a sample of single-name CDS spreads. We relegate the details of these two exercises to Sections IV.C and IV.D of the Internet Appendix, respectively. We summarize the main results from the analyses below. 

First, we repeat the analysis in Section III.C.1 using the pooled sample of non-U.S. corporate bonds. Doing so not only helps address the concern that some non-U.S. data samples are small, especially compared with the U.S. sample (Table I), but also provides an overall picture of structural model performance in the seven corporate bond markets outside the United States. However, here we do not simply pool the predicted spreads of the non-U.S. bonds obtained in the baseline case, as the default boundary and recovery rate used to calculate these spreads are estimated using the regional default rates and recovery rates. Instead, we first reestimate the default boundary and recovery rate using the aggregate default rates and recovery rates derived from the 

> 15 A typical example is Engie S.A., a French state-owned utility company. In most months after 2011 (until the end of our sample period), its leverage ratio is greater than 50%, but the observed − spreads of its bonds are lower than 70 bps; its credit rating is tabulated as A after our adjustment for government equity ownership. This example suggests that adjusting the credit rating by one notch lower is inadequate for these large state-owned utility companies. 

_The Global Credit Spread Puzzle_ 

133 

seven non-U.S. countries. We then re-compute the model-implied spreads on the non-U.S. bonds. 

Panel B2 of Table III reports the new estimates of _d_ for the seven countries, which generally differ from their counterparts in the base case (Panel B1 of Table III). Panel B of Figure 1 plots the five-year moving average of issuerweighted recovery rates for senior unsecured debts for the seven non-U.S. countries (red dashed line). The non-U.S. recovery rates generally move together with and are mostly higher than the U.S. rates in our study sample. 

Using the recalculated BC model–implied spreads, we find that the model significantly underpredicts the average credit spread for AA+ (if observations with negative spreads are excluded), A, BBB, and all IG bonds in the pooled sample, that is, for nine and six out of nine IG[non-US] / _d_ bins with and without controls for negative spreads in the data (see Internet Appendix Table IA.IX). If we limit the sample to pooled non-U.S. industrial issuers, then these two numbers become eight and six out of nine IG[non-US] / _d_ bins (see Internet Appendix Table IA.VIII). Overall, there is strong evidence of a CSP in the pooled non-U.S. sample, especially after controlling for negative credit spreads. 

We next examine the model performance using a sample of single-name CDS spreads for the same eight countries, which is much smaller than our corporate bond sample. Focusing on the most liquid, five-year contracts, we find that the BC model tends to underpredict average CDS spreads on IG names in AUS, CAN, GBR, and USA. We further find that this is the case for nine out of nine IG[non-US] / _d_ bins in the pooled non-U.S. sample (see Internet Appendix Table IA.XI). 

## _D. Percentiles of Predicted Credit Spreads_ 

One question that arises from the analysis in Section III.C is whether the negative MPEs of certain bond portfolios are driven by outliers. A related question is to what extent are some portfolios fairly priced simply because certain component bonds are substantially overpriced while other component bonds are significantly underpriced. After all, a successful model should price credit spreads on each bond. In this subsection, we examine the percentiles of bondlevel credit spreads to shed light on these questions. 

We tabulate the percentiles of both actual and predicted spreads for each of 90 (30 × 3) CR/country/ _d_ bins in rows labeled “BC( _dswap[FS]_[)”,][“BC(] _[d] swap[BGY]_[)”,][and] “BC( _dswap[HNS]_[)”][in][Table][VI][.][16][Notably,][except][in][the][cases][of][negative][percentiles] of observed spreads, the BC model substantially underpredicts the spreads in the left tail across all countries and credit ratings. The model also markedly underpredicts the median spread in every bin except for six bins in JPN and 

> 16 The average observed credit spreads over swap rates shown in Table VI are different from those reported in Table I. The reason is that we take the average of portfolio credit spreads in Table I and of bond credit spreads in Table VI. In addition, Table VI does not include those observations for which the predicted spreads are not computable, for example, due to missing model inputs. 

_The Journal of Finance[®]_ 

134 

the HY/FRA/ _dswap[FS]_[bin. As a result, the mean predicted spread is heavily influ-] enced by the observation in the right tail and is significantly higher than the median predicted spread. For instance, consider the A/DEU group, the only IG group with a significantly positive MPE under BC( _dswap[M]_[)][ ∀] _[M]_[ besides (AA][+][,] A)/JPN. In this case, (data, BC( _dswap[FS]_[)) in bps is (102] _[,]_[ 199) at the 90][th][ percentile,] (353 _,_ 937) at the 99[th] percentile, (54 _,_ 74) at the mean, and (39 _,_ 11) at the median. Additionally, out of the six (A, BBB)/FRA/ _d_ bins, similar patterns occur in those five without the spread underprediction problem. Taken together, these results indicate that the BC model generates severe right skewness relative to the data and that its fair or overprediction of the mean credit spread is due to those highly overpredicted spreads in the right tail. 

We obtain qualitatively similar results for the subsamples of positive credit spreads, industrial firms, and pooled non-U.S. bonds (see Section IV.E of the Internet Appendix). We also examine the percentiles of predicted and observed IG spreads at the country level, as well as their Q-Q plots, which indicate that the two sets of percentiles are distinct from each other (see Section IV.H of the Internet Appendix). 

In summary, our results from Section III.D show that the ability of the BC model to predict the mean spread depends crucially on the predicted spreads in the right tail, but that the distributions of the predicted and observed spreads are quite different. We next examine the fitting errors of the model directly and explore their potential drivers in Section III.E. 

## _E. Dissecting Pricing Errors of the BC Model_ 

We begin with three groups of variables that may account for the pricing errors at the country level: recovery rates, financial market conditions, and liquidity factors. We then consider variables that may co-vary with the bond-level pricing errors, such as the inputs of the BC model, equity market factors, macro conditions, and liquidity. Except for recovery rates, we examine potential links between the above variables and the pricing errors using panel regressions (detailed in Section IV.F of the Internet Appendix). Below we summarize the main results of our analysis. 

We use the regional five-year MARR in the baseline analysis. Recovery rates may vary at the country level, however, because of different legal environments across countries. We thus consider two alternative estimates for LGD. The first is the HY CDS spread–implied (forward-looking) LGD from Markit (their counterparts for IG names have very low cross-sectional variation and thus are not used here). We use the average implied LGD value across all HY single-name CDS contracts in each country as its country-specific LGD, except for AUS (as there are no HY Australian CDS contracts denominated in Australian dollars in our sample). The second alternative measure is based on the country-specific bankruptcy efficiency scores (equivalent to the recovery rates times 100) estimated by Djankov et al. (2008) using survey data. 

We rerun the baseline analysis under BC( _dswap[FS]_[)][using][the][two][alternative] measures of LGD above. Figure 4 plots the MPE versus the CDS-implied LGD 

_The Global Credit Spread Puzzle_ 135 

**==> picture [342 x 185] intentionally omitted <==**

**----- Start of picture text -----**<br>
FRA FRA<br>20 20<br>JPN JPN<br>0 0<br>USA USA<br>-20 -20<br>DEU DEU<br>-40 -40<br>ITA ITA<br>GBR GBR<br>CAN CAN<br>-60 -60<br>-80 -80<br>-100 -100<br>-120 -120<br>AUS<br>-140 -140<br>60 62 64 66 0 10 20 30 40 50<br>CDS-LGD 1 - Bankruptcy Efficiency<br>Pricing Errors (bps) Pricing Errors (bps)<br>**----- End of picture text -----**<br>


**Figure 4. Loss given default (LGD) and pricing errors** . This figure plots the mean pricing errors (MPEs)—the difference in credit spreads between the BC( _dswap[FS]_[)][model][and][the][data][for] IG bonds—against two alternative proxies for the LGD across eight countries in the sample. The first proxy, “ _CDS-LGD_ ,” is the average LGD implied from high-yield CDS contracts (left panel). The second proxy, “ _1-Bankruptcy Efficiency_ ,” is the survey-based measure of LGD constructed in Djankov et al. (2008) (right panel). The eight countries are Australia (AUS), Canada (CAN), France (FRA), Germany (DEU), the United Kingdom (GBR), Italy (ITA), Japan (JPN), and the United States (USA). AUS is not shown in the left panel, as there are no HY Australian CDS contracts denominated in Australian dollars in the study sample. (Color figure can be viewed at wileyonlinelibrary.com) 

(left panel) and the survey-based LGD (right panel) at the country level by credit rating. If LGD is the driver of the cross-country difference in credit spreads, we should see a negative relationship between the MPE and LGD. The left panel instead displays a positive relationship. In particular, even though Japan’s LGD is slightly higher than that in the other countries (which are very similar to each other), credit spreads in JPN are lower than in the other countries. The right panel shows a slightly positive relationship between the MPE and LGD. While DEU, FRA, and ITA have relatively low bankruptcy efficiency scores (and thus high LGD estimates), the remaining five countries have relatively high efficiency scores. These results indicate that neither measure of the heterogeneous LGD estimates explains the BC model’s large pricing errors in corporate bond spreads. 

We consider five indicators of market conditions and three proxies for corporate bond illiquidity in our panel regressions of the country-level pricing errors. The five indicators include the one-year risk-free rate, the slope of the yield curve, the stock market index option-implied volatility and volatility skew, and the equity variance risk premium (VRP) estimator of Bollerslev, Tauchen, and Zhou (2009). The use of the latter two indicators is motivated by the finding of Du, Elkamhi, and Ericsson (2019) that incorporating jumps, stochastic asset volatility, and the asset VRP helps reconcile the CSP in the 

_The Journal of Finance[®]_ 

136 

U.S. single-name CDS market. The three illiquidity proxies used are the average bid-ask spread for each country, computed using bid and ask prices from the BGN pricing source, the bond-CDS basis, and TED spreads for each country given that they capture information about funding market conditions for dealers.[17] Our regression results indicate that the illiquidity proxies have much greater explanatory power for variation in the country-level pricing errors than do the market condition indicators. 

We explore the source of the bond-level pricing errors using 10 different panel regression specifications. The explanatory variables that we use can be divided into three groups. The first group has three inputs for the BC model: the risk-free rate, leverage, and equity volatility (asset volatility is not used here because it is assumed to be constant and thus does not reflect timevariation in volatility). The second group consists of variables that may help explain the CSP in the U.S. market as proposed in the literature. They include two proxies for macro conditions, namely, the real GDP growth rate (seasonally adjusted) and the slope of the yield curve (Chen, Collin-Dufresne, and Goldstein (2009), Bhamra, Kuehn, and Strebulaev (2010), Chen (2010)), three variables related to stock market index option-implied volatility (Du, Elkamhi, and Ericsson (2019)), and proxies for corporate bond illiquidity. The third group has four standard equity market factors, { _MKTt, SMBt, HMLt, UMDt_ }, which hold some explanatory ability for credit spreads in the United States (e.g., Collin-Dufresne, Goldstein, and Martin (2001), Avramov, Jostova, and Philipov (2007)). 

Our main finding is that firm leverage, implied volatility, and market liquidity display the most robust statistical significance in explaining bond-level pricing errors. In particular, the regression coefficient on leverage has a positive sign regardless of the specification considered and the coefficients on three illiquidity measures tend to have a negative sign. These findings imply that the leverage dynamics in the BC model may be misspecified and that the model may need to incorporate corporate bond illiquidity. 

## _F. Structural Models with Stationary Leverage Ratios_ 

Given that the BC model has a negative MPE for IG bonds and that its bond-level pricing errors have a positive regression coefficient on leverage, incorporating mean-reverting leverage ratios into the model may improve its performance. Accordingly, we implement the one-factor CDG model with nonstochastic interest rates in this subsection.[18] 

> 17 Transaction-based illiquidity measures developed for the U.S. market are not implemented here as we have no access to transaction data for non-U.S. corporate bonds in our sample. Bai and Collin-Dufresne (2019) find that the CDS-bond basis is negatively correlated with corporate bond illiquidity. Chen et al. (2018) target their model-implied liquidity component in corporate yield spreads at the bond-CDS spread. 

> 18 Several studies have empirically examined the CDG model using U.S. data. For example, Eom, Helwege, and Huang (2004) and Feldhütter and Schaefer (2023) do so using data on individual corporate bond prices, HH using aggregate data for different rating categories, and Huang, 

_The Global Credit Spread Puzzle_ 

137 

## **Table VII** 

## **Parameter Estimates for the Stationary Leverage Model** 

This table summarizes the GMM estimation results of parameters in the Collin-Dufresne and Goldstein (2001, CDG) model. In the test, seven moment conditions are used, and they are constructed based on the pricing relationship for 1-, 2-, 3-, 5-, 7-, and 10-year single-name CDS spreads as well as equity volatility estimated with daily stock returns. Parameters _κ_ and _ν_ define the dynamics of the corporate debt level, and _L_[¯] _[Q]_ represents the model-implied long-run mean of the risk-neutral leverage. The average parameter estimates are computed for every credit rating category in each country. Parameter _d[CDG] swap_[(] _[d][CDG] Govt_[) denotes the default boundary estimated by calibrat-] ing the CDG model to default data, with the LIBOR swap rates (government bond yields) as the default-free rates for a given country. 

|Parameters<br>Credit<br>Rating|Country|
|---|---|
||Japan<br>U.K.<br>Germany<br>France<br>Italy<br>Canada<br>U.S.<br>Australia|
|_κ_<br>AA+<br>A<br>BBB<br>HY<br>_ν_<br>AA+<br>A<br>BBB<br>HY<br>¯_LQ_<br>AA+<br>A<br>BBB<br>HY<br>_dCDG_<br>_swap_<br>All<br>_dCDG_<br>_Govt_<br>All|16.82<br>16.29<br>16.90<br>17.04<br>19.49<br>13.67<br>17.54<br>13.42<br>15.02<br>15.18<br>15.56<br>15.40<br>19.42<br>14.85<br>14.40<br>15.71<br>13.20<br>15.48<br>14.33<br>13.01<br>12.90<br>15.41<br>13.09<br>15.58<br>−<br>7.70<br>6.33<br>5.80<br>6.03<br>7.71<br>5.88<br>−<br>0.31<br>0.32<br>0.48<br>0.63<br>0.30<br>0.56<br>0.45<br>0.14<br>0.31<br>0.28<br>0.48<br>0.33<br>0.33<br>0.32<br>0.40<br>0.24<br>0.28<br>0.28<br>0.38<br>0.75<br>0.29<br>0.35<br>0.41<br>0.22<br>−<br>0.25<br>0.54<br>0.23<br>0.29<br>0.22<br>0.39<br>−<br>0.74<br>0.73<br>0.62<br>0.53<br>0.74<br>0.57<br>0.64<br>0.87<br>0.74<br>0.76<br>0.62<br>0.72<br>0.72<br>0.73<br>0.67<br>0.79<br>0.76<br>0.76<br>0.68<br>0.47<br>0.75<br>0.71<br>0.67<br>0.80<br>−<br>0.79<br>0.58<br>0.80<br>0.75<br>0.81<br>0.69<br>−<br>0.71<br>0.96<br>0.93<br>0.95<br>0.76<br>0.99<br>0.91<br>0.92<br>0.67<br>0.93<br>0.91<br>0.93<br>0.72<br>0.98<br>0.90<br>0.90|



In this model, the following dynamics of a firm’s total debt level ( _Kt_ ) are assumed: 

**==> picture [248 x 10] intentionally omitted <==**

where _κ_ captures the speed at which log-leverage, ln( _Kt/At_ ), reverts to the target ratio under Q: ln( _L_[¯] _[Q]_ ) ≡[−] _[r]_[+] _[δ]_[+] _κ_[(] _[σ][ A]_[)][2] _[/]_[2] − _ν_ . If _κ_ = 0, then the default boundary is flat and the model degenerates to the Black-Cox type. Default probabilities under Q or P and risky debt valuation in this model can be all calculated by following CDG. Below we summarize the main results on the estimation and performance of the CDG model (see Section IV.G of the Internet Appendix for details of the analysis). 

Table VII shows the average estimates of _κ_ and _ν_ (or equivalently _L_[¯] _[Q]_ ) by credit rating category, as well as _d[CDG] swap_[(the][estimate][of] _[d]_[obtained][by] calibrating the CDG model to default data), in each country. The average _κ_ lies between 12 and 20 for IG bond issuers but ranges from 5.80 to 7.71 for HY ones. These estimates are consistent with the values reported by Huang, Shi, and Zhou (2020), who draw generalized method of moments (GMM)-based 

Shi, and Zhou (2020) using data on single-name CDS spreads. However, few studies have tested the CDG model using security-level credit spread data outside the United States. 

_The Journal of Finance[®]_ 

138 

statistical inference of the CDG model using U.S. data. Compared with its counterparts under the BC model, _d[CDG] swap_[is][lower][except][for][DEU][and][USA.] This result is not surprising, given that for countries with high target leverage, a lower _d_ is needed for the CDG model to fit the historical default rates (e.g., for JPN _dswap[FS]_[=][ 0] _[.]_[85 and] _[ d][CDG] swap_[=][ 0] _[.]_[71).] Panel A of Table IV reports the MPEs of the CDG model for each of 24 IG/country bins in rows labeled “CDG( _d[CDG] swap_[).”][Whereas][the][model][solves][the] underprediction problem for the AA+/FRA, A/USA, and BBB/DEU groups, it leads to such a problem for A/DEU and BBB/FRA. Overall, the model still underpredicts the mean IG spread for 16 out of 24 IG/country bins (compared with 17 bins under BC( _dswap[FS]_[)),][and][it][continues][to][do][so][after][adjusting][for] negative spreads (Panel B of Table IV). 

Rows labeled “CDG( _d[CDG] swap_[)”][in][Table][V][report][the][results][for][IG][bonds][at] the country level. Panels A and B show that the CDG model underpredicts the mean spread for six countries without and with adjustment for negative spreads, even one more country (DEU) than under BC( _dswap[FS]_[)][in][the][former] case. In the case of industrial issuers, the number of countries with the underprediction problem under CDG( _d[CDG] swap_[) is still six, compared with six and seven] under BC( _dswap[FS]_[) without and with adjustment for negative spreads (as shown] in Panels C and D, respectively). 

The predicted percentiles reported in rows labeled “CDG( _d[CDG] swap_[)” in Table][ VI] illustrate the sources of the improved MPEs under the CDG model. Among the aforementioned three groups whose underprediction problem under BC( _dswap[FS]_[)] is overcome by the CDG model, the higher and more accurate predicted spreads at the 75[th] and lower percentiles are key for AA+/FRA and BBB/DEU, whereas the extremely overpredicted spread at the 99[th] percentile (1,333 bps compared with 305 bps in the data) is the main driver for A/USA. These two patterns also hold for BBB/GBR and A/AUS, respectively, whose MPEs under CDG( _d[CDG] swap_[)] become much less negative albeit are still significant at the 1% level. In cases such as AA+/CAN, A/ITA, BBB/AUS, and BBB/FRA, the CDG model predicts the spread more accurately across all percentiles. 

In sum, Section III.F shows that the GCSP is robust to the CDG model. We therefore focus on corporate bond liquidity next and examine whether it can help mitigate the puzzle. 

## **IV. Structural Models with Search Frictions** 

In this section, we incorporate corporate bond illiquidity into the BC model and obtain a structural model with endogenous corporate bond illiquidity. The model follows directly from the insights of He and Milbradt (2014) and is suitable for studying the GCSP. 

## _A. Outline of the Model_ 

The debt structure, default boundary, and default trigger in the model are as described in Section III.A. The new ingredient is endogenous liquidity in 

_The Global Credit Spread Puzzle_ 

139 

the secondary debt market with search frictions and bargaining. As shown by Duffie, Gârleanu, and Pedersen (2005), endogenous bond illiquidity can be derived from the valuation wedge between _L_ -type investors, who have been hit by liquidity shocks and thus face costs for holding bonds, and _H_ -type investors, who have not. Such investors’ corporate bond valuation functions, _DL_ ( _t, T_ ) and _DH_ ( _t, T_ ), follow Proposition 1 in He and Milbradt (2014), 

**==> picture [351 x 56] intentionally omitted <==**

where _χ_ is the holding cost, { _RH, RL_ } are state-dependent recovery rates, _Z_ is a 2-by-2 matrix of liquidity-adjusted discount factors, _U_ is the matrix that diagonalizes _Z_ , _π[Q]_ ( _t, T_ ) is the time- _t_ risk-neutral default probability over ( _t, T_ ], and _G_ ( _t, T_ ) = diag[ _G_ 1( _t, T_ ) _, G_ 2( _t, T_ )] is the state-dependent time- _t_ price of the Arrow-Debreu default claim. The bond valuation formula in equation (5) essentially maps its counterpart under the BC model in equation (1) with the discount rate adjusted by transition intensity and the bond cash flows adjusted by holding costs. 

Specifically, _Z_ , _π[Q]_ ( _t, T_ ), and _G_ are 

**==> picture [333 x 121] intentionally omitted <==**

where _r_ is the default-free rate, _ξ_ is the intensity of transforming an _H_ -type investor to an _L_ -type one, _λ_ is the intensity of investors trading with dealers, _β_ is investors’ bargaining power vis-`a-vis dealers, _λβ_ is the intensity of a “backward” transition from the _L_ state to the _H_ state, and � _r_ 1 = _r_ + _ξ_ + _λβ >_ � _r_ 2 = _r_ . Additionally, _d_ is the default boundary, _K/At_ is time- _t_ leverage, _σ[A]_ is asset � volatility, _δ_ is the payout ratio, _ν_ = _r_ − _δ_ − 0 _._ 5( _σ[A]_ )[2] , _ζ j_ = � _ν_[2] + 2 _r j_ ( _σ[A]_ )[2] , and _N_ [·] is the cumulative standard normal distribution function. 

Given that the ML data consist of bid quotes instead of mid prices, we focus on the bid price in our empirical analysis of the model specified in equation (5). Under this model, the bid price is 

**==> picture [274 x 13] intentionally omitted <==**

_The Journal of Finance[®]_ 

140 

The yield to maturity, _y[HM]_ ( _t, T_ ), solves equation (2) with _D[BC]_ ( _t, T_ ) replaced by _D[HM] B_ ( _t, T_ ). 

Given its debt structure with an exogenous default boundary, the model considered here has no rollover risk in the primary debt market associated with stationary debt structure. The model is thus a reduced-form variant of the He and Milbradt (2014) model and termed the HM or search model for convenience. Unlike the He and Milbradt (2014) decomposition of yield spreads, _y[HM]_ ( _t, T_ ) here does not have a liquidity-driven default component. However, _y[HM]_ ( _t, T_ ) does include a default-driven liquidity component as in the He and Milbradt (2014) model. This component captures the interaction between default risk and illiquidity and, as shown later, plays an important role in helping mitigate the CSP. 

Two other noteworthy features of this reduced-form model make it suitable for the purpose of this study. First, since the HM model is developed in the risk-neutral setting, _π[Q]_ ( _t, T_ ) in equation (5) can be determined based on its counterpart under P. Second, the liquidity component of _y[HM]_ can be empirically pinned down by using proportional bid-ask spreads rather than corporate bond prices—as noted earlier, there is no one-to-one mapping between a bond’s bidask spread and price. Taken together, these two features make it possible for us to quantify the incremental impact of search frictions on corporate bond spreads while controlling for P-measure default probabilities and credit risk factors, that is, to isolate the contribution of market illiquidity to the CSP. 

## _B. Estimation of Input Parameters_ 

The HM model parameters include type-dependent recovery rates, { _RH, RL_ }, and the parameters characterizing search frictions, { _ξ, λ, β, χ_ }. We estimate these six parameters using data on BGN bid and ask prices that are matched with our final sample of corporate bonds (see Section V.A of the Internet Appendix for evidence justifying the use of BGN data here). 

## _B.1. Type-Dependent Recovery Rates_ 

To determine { _RH, RL_ }, we adopt the assumption in He and Milbradt (2014) that the historical recovery rate corresponds to the bid in the post-default market. It follows that we can obtain { _RH, RL_ } by solving the following system of equations for each country: 

**==> picture [232 x 11] intentionally omitted <==**

**==> picture [248 x 24] intentionally omitted <==**

where we set the historical average recovery rate _R_ to be the same as that specified in Section III.B.2 and set the proportional bid-ask spread of defaulted bonds, _φd_ , to 2.8% as reported by Jankowitsch, Nagler, and Subrahmanyam (2014) using U.S. data. As a result, the time- _t_ { _RH, RL_ } for a given non-U.S. 

_The Global Credit Spread Puzzle_ 

141 

country depends on the calibrated recovery rate ( _R_ ) at _t_ (as described in Section III.B.2) as well as its _β_ estimate, but not on the post-default market liquidity of the country. This estimation scheme therefore enables us to get around the problem that there is not much data available on transaction costs of defaulted bonds in the seven non-U.S. countries. Nonetheless, in an analysis detailed in Section V.B of the Internet Appendix, we present evidence indicating that allowing for heterogeneity in bid-ask spreads of defaulted bonds in these countries will likely improve the performance of the HM model. 

## _B.2. Parameters on Search Frictions_ 

To model type- _L_ agent’s holding costs, we follow He and Milbradt (2014) and assume _χ_ = _χc_ · _c_ + _χk_ · 1. Let _θ[S]_ = { _ξ, λ, β, χc, χk_ }. We determine _θ[S]_ based on the following expression for the time- _t_ HM model-implied proportional bid-ask spread for a bond with maturity _T_ : 

**==> picture [298 x 59] intentionally omitted <==**

where _D[HM] A_ is the ask price and equal to _DH_ , and _D[HM] B_ is given by equation (10). Specifically, for each country, _θ[S]_ is estimated by minimizing the summed square of fitting errors over the entire sample, 

**==> picture [274 x 27] intentionally omitted <==**

where _φ_ ( _t, Ti_ ; _θ[S]_ ) and _φt[obs] ,Ti_[denote the time-] _[t]_[model-implied and observed BGN] proportional bid-ask spreads for bond _i_ with maturity _Ti_ , respectively. Given that the bond-level measures of bid-ask spreads are inevitably rather noisy, we obtain _φt[obs] ,Ti_[in][two][steps.][First,][in][each][month,][we][assign][the][bid-ask][spreads] of individual bonds to one of 12 rating-maturity bins constructed from four credit ratings (AA+, A, BBB, HY) and three maturity groups ( _<_ 5 years, 5–10 years, 10+ years). Next, we obtain the median bid-ask spread of bonds in the same category and use this smoothed bid-ask spread as our measure of _φt[obs] ,Ti_[in] equation (14).[19] 

We illustrate the model fit to proportional bid-ask spreads in Figure 5, relegating the details of the fitting errors to Section V.C of the Internet Appendix. 

> 19 This cross-sectional smoothing within each rating-maturity group is motivated by the key implication of He and Milbradt (2014): The endogenous bid-ask spread depends not only on the issuer’s default risk but also on the bond’s time to maturity. Compared to unsmoothed bid-ask spreads, smoothed ones have stronger explanatory power for individual bonds’ pricing errors in panel regressions (untabulated). In Section V.C of the Internet Appendix, we provide further analysis of unsmoothed and smoothed bid-ask spreads. Additionally, we reestimate _θ[S]_ by targeting 

_The Journal of Finance[®]_ 

142 

**==> picture [359 x 388] intentionally omitted <==**

**----- Start of picture text -----**<br>
AA+ A<br>60 70<br>Mean<br>50 Median AUS 60<br>AUS GBR<br>40 50 ITAGBR<br>USA USA FRA<br>30 GBR CAN CA USANFRAFRA 40 ITAUSAUS A FRA<br>20 ITITAAJPNJPNGBRDEU 30 JP CNAN CAN DEUDEUAUS<br>DEU JPN<br>20<br>10<br>10<br>20 40 60 20 40 60<br>Model (bps) Model (bps)<br>BBB HY<br>70 120<br>60 100 USA<br>GBR GBR<br>GBR GBR<br>USA<br>50 USA<br>ITA 80<br>I TAUSA FRA<br>40 CAN FRA<br>D EUFRA 60<br>FRA ITA<br>30 JPNAUSCAN DEU CCAANN DEU DEITAU<br>AUS<br>JPN 40<br>20<br>20<br>20 40 60 20 40 60 80 100 120<br>Model (bps) Model (bps)<br>Data (bps) Data (bps)<br>Data (bps) Data (bps)<br>**----- End of picture text -----**<br>


**Figure 5. Predicted versus observed proportional bid-ask spreads** . This figure plots the observed (proportional) bid-ask spreads against their modeled counterparts for each country by credit rating. Model-implied bid-ask spreads are calculated using a variant of the He and Milbradt (2014) model with the default boundary _d_ = _dswap[FS]_[.][The][average][(median)][bid-ask][spreads] are marked with a pink dot (blue asterisk). The eight countries included in the final sample are Australia (AUS), Canada (CAN), France (FRA), Germany (DEU), the United Kingdom (GBR), Italy (ITA), Japan (JPN), and the United States (USA). AUS and JPN have no high-yield (HY) bonds in the sample. (Color figure can be viewed at wileyonlinelibrary.com) 

## By inspection, the model fits both the median and mean bid-ask spreads reasonably well, although the model appears to overestimate the mean slightly 

secondary-market transaction volume as well in equation (14) and show that credit spreads based on this new estimate of _θ[S]_ are similar to the main results. 

_The Global Credit Spread Puzzle_ 

143 

more than the median. Note that the mean bid-ask spreads and mean credit spreads are correlated across countries but do not have the same ordering (see Tables VI and IA.XIX). For instance, GBR ranks fourth for AA+ bonds, first for A, and first for BBB under the average bid-ask spread, but ranks fifth, third, and second, respectively, under the mean credit spread. 

We report[�] _θ[S]_ at the country level in Panel A of Table VIII. All five parameters show substantial heterogeneity, and the pattern of cross-country variation is generally consistent with the results on pricing errors discussed in Section III.C. For instance, the estimated intensity to meet dealers ( _λ_[ˆ] ) is 1.75 in ITA and ranges from 3.31 in GBR to 6.34 in FRA among the remaining seven countries. GBR has the second-lowest _λ_[ˆ] but the highest estimated liquidity shock intensity ( _ξ_[ˆ] ) at 0.24. AUS has much higher estimates of the holding cost parameters ( _χ_ � _k_ and _χ_ � _c_ ) relative to the rest. CAN has the second-highest _χ_ � _c_ (0.14) and the third-lowest _λ_[ˆ] (4.44). For JPN, � _χk_ , � _χc_ , _ξ_[ˆ] , and _λ_[ˆ] are all on the high liquidity side. Recall from Table V that under the BC model, AUS, CAN, and GBR have the most negative MPEs for IG bonds at the country level, while MPEs for JPN are overwhelmingly positive. Thus, incorporating search frictions in the secondary bond market into the BC model can potentially improve the model performance, except perhaps for JPN. 

## _B.3. Are the Country-Level Estimates of Search Parameters Reasonable?_ 

Before proceeding to the pricing implications of the HM model, we look further into the interpretations of our search parameter estimates by going beyond the MPEs at the country level. In particular, we examine whether these estimates can capture certain aspects of the cross-sectional heterogeneity across the eight corporate bond markets. 

First, the liquidity shock intensity ( _ξ_ ) captures bond supply in the secondary market and is proxied by dealer inventory in He and Milbradt (2014). As the order flow information used to infer dealer inventory in the seven non-U.S. corporate bond markets is unavailable, we try to link our _ξ_[�] to investor composition in each country (see Section I.A of the Internet Appendix). For example, mutual funds typically suffer a greater intensity of liquidity shocks and have much higher trading frequencies than the more traditional participants in the corporate bond market (Li and Yu (2023)). Given this insight, we calculate the market share of corporate debt securities held by mutual funds and compare it with _ξ_[�] . Panel A of Figure 6 shows that _ξ_[�] is positively correlated with the share and, in particular, is fairly low for countries where mutual funds’ share is minimal such as JPN. In contrast, given their endogenous choice to invest in corporate bonds, households, nonfinancial corporations, and governments are unlikely to be forced to sell their corporate bond holdings by liquidity shocks. Panel B reveals that _ξ_[�] and the share of these investors are indeed negatively correlated. For instance, the share is negligible for GBR with the highest _ξ_[�] , and the opposite is true for CAN. 

Next, consider _χ_ = ( _χk, χc_ ), the proportional costs incurred to bond investors once they are hit by liquidity shocks. He and Milbradt (2014) calibrate _χ_ to 

_The Journal of Finance[®]_ 

144 

## **Table VIII** 

## **Estimates of Bond Illiquidity in Secondary Markets** 

The table presents the estimated parameters on secondary market search frictions as modeled by He and Milbradt (2014) for each country. The five parameters characterizing search frictions are holding cost per unit of principal ( _χk_ ), holding cost per unit of coupon ( _χc_ ), liquidity shock intensity ( _ξ_ ), the intensity to meet dealers ( _λ_ ), and the bargaining power of investors ( _β_ ). The parameter estimates are obtained for two alternative default-free rates in each country: swap rates (Panel A) and government bond yields (Panel B). The model parameters are estimated by minimizing the mean squared fitting errors to the observed proportional bid-ask spreads in each country. Standard errors, reported in brackets, are computed with a quasi-Newton approximation of the Hessian matrix. 

|Japan<br>U.K.<br>Germany<br>France<br>Italy<br>Canada<br>U.S.<br>Australia|_χk_×102<br>_χc_<br>_ξ_<br>Panel A: Swap Rates as the Default-Free Rates<br>0.099<br>0.070<br>0.120<br>[0.021]<br>[0.015]<br>[0.006]<br>0.090<br>0.041<br>0.239<br>[0.024]<br>[0.016]<br>[0.026]<br>0.710<br>0.142<br>0.142<br>[0.064]<br>[0.030]<br>[0.013]<br>0.527<br>0.048<br>0.182<br>[0.267]<br>[0.093]<br>[0.025]<br>0.180<br>0.005<br>0.209<br>[0.021]<br>[0.020]<br>[0.007]<br>0.279<br>0.139<br>0.108<br>[0.074]<br>[0.053]<br>[0.005]<br>0.088<br>0.067<br>0.184<br>[0.044]<br>[0.082]<br>[0.025]<br>1.153<br>0.293<br>0.184<br>[0.162]<br>[0.085]<br>[0.021]|_λ_<br>5.250<br>[0.125]<br>3.309<br>[0.470]<br>5.955<br>[0.132]<br>6.339<br>[0.200]<br>1.747<br>[0.125]<br>4.445<br>[0.340]<br>4.838<br>[1.063]<br>5.445<br>[0.297]|_β_<br>0.016<br>[0.002]<br>0.070<br>[0.011]<br>0.018<br>[0.005]<br>0.033<br>[0.020]<br>0.118<br>[0.002]<br>0.020<br>[0.003]<br>0.043<br>[0.010]<br>0.024<br>[0.002]|
|---|---|---|---|



|Japan<br>U.K.<br>Germany<br>France<br>Italy<br>Canada<br>U.S.<br>Australia|Panel B:<br>0.090<br>[0.019]<br>0.085<br>[0.024]<br>0.605<br>[0.048]<br>0.615<br>[0.341]<br>0.184<br>[0.020]<br>0.279<br>[0.089]<br>0.083<br>[0.043]<br>1.146<br>[0.200]|Government Bond Yields as the Default-Free<br>0.052<br>0.108<br>[0.011]<br>[0.004]<br>0.037<br>0.270<br>[0.017]<br>[0.031]<br>0.110<br>0.138<br>[0.033]<br>[0.015]<br>0.050<br>0.150<br>[0.117]<br>[0.032]<br>0.005<br>0.209<br>[0.023]<br>[0.007]<br>0.139<br>0.108<br>[0.067]<br>[0.006]<br>0.060<br>0.215<br>[0.105]<br>[0.032]<br>0.290<br>0.189<br>[0.099]<br>[0.027]|Rates<br>5.323<br>[0.108]<br>4.087<br>[0.354]<br>5.939<br>[0.135]<br>6.422<br>[0.210]<br>1.755<br>[0.128]<br>4.446<br>[0.417]<br>5.750<br>[1.362]<br>5.454<br>[0.324]|0.020<br>[0.002]<br>0.065<br>[0.013]<br>0.021<br>[0.006]<br>0.028<br>[0.025]<br>0.118<br>[0.002]<br>0.020<br>[0.003]<br>0.044<br>[0.013]<br>0.024<br>[0.002]|
|---|---|---|---|---|



_The Global Credit Spread Puzzle_ 

145 

**==> picture [349 x 379] intentionally omitted <==**

**----- Start of picture text -----**<br>
Panel (A) Panel (B)<br>0.3 0.3<br>0.25 0.25<br>GBR GBR<br>ITA ITA<br>0.2 0.2<br>USAFRA AUS FRAAUS USA<br>0.15 0.15<br>DEU DEU<br>JPN JPN<br>CAN CAN<br>0.1 0.1<br>0 0.2 0.4 0.6 0 0.1 0.2 0.3 0.4<br>Share of Mutual Funds Share of HHs, Corps., Gov<br>Panel (C) Panel (D)<br>0.03 0.03<br>AUS AUS<br>0.02 0.02<br>DEU DEU<br>0.01 CAN 0.01 CAN<br>FRA FRA<br>USA USA<br>GBR<br>JPN ITA JPN [GBR] ITA<br>0 0<br>0.5 1 1.5 2 0.5 1 1.5<br>Cost of Downgrade Events (%) Cost of Index Exclusions (%)<br>Panel (E) Panel (F)<br>7<br>FRA<br>6 DEU ITA<br>AUSJPN 0.1<br>5 USA<br>CAN<br>4 GBR<br>3 GBR 0.05 USA<br>FRA<br>2 ITA DEU CANAUS JPN<br>1 0<br>0.15 0.2 0.25 0.3 0.1 0.2 0.3 0.4<br>Scaled Number of Dealers Frequency of Downgrades (%)<br>**----- End of picture text -----**<br>


**Figure 6. Model estimates for secondary market frictions** . This figure compares the model estimates for corporate bond market frictions with their empirical proxies at the country level. The first two panels plot the estimated liquidity shock intensity ( _ξ_ ) against the share of corporate debt securities held by mutual funds (Panel A) or by households (HHs), nonfinancial corporations, and governments (Panel B) over the period from 2013 to 2017. The next two panels compare the modelimplied average holding cost ( _χk_ + _c_ ¯ _χc_ ) with the estimated cost for forced selling of downgraded bonds (Panel C) and of bonds exiting the ICE BofAML corporate index (Panel D), respectively. Panel E plots the estimated meeting rate between customers and dealers ( _λ_ ) against the scaled number of quoting dealers for a representative bond. Empirical proxies in Panels C to E are reported as the average over the 2003 to 2017 period. Panel F plots the estimated bargaining power of customers ( _β_ ) against the annual frequency of rating downgrades from investment grade to junk status over the 1970 to 2017 period. (Color figure can be viewed at wileyonlinelibrary.com) 

_The Journal of Finance[®]_ 

146 

fit the average bid-ask spreads of AA and BBB bonds in the United States, whereas we use bid-ask spreads on individual bonds in our estimation. To see whether the cross-country pattern of our � _χ_ is reasonable, we focus on two types of events that may force investors to sell their corporate bond holdings for nonfundamental reasons and that lead customers to demand liquidity in the corporate bond market: An IG bond downgraded to “junk” or a bond exiting from certain bond indexes. The former event triggers regulation-induced fire sales (Ellul, Jotikasthira, and Lundblad (2011), Ambrose, Cai, and Helwege (2012)), and the latter makes index trackers sell the exiting bonds to minimize their tracking errors (Dick-Nielsen and Rossi (2018)). Holding the amount of arbitrage capital constant, the heterogeneity in _χ_ is expected to show up as a difference in the cost of forced selling across countries. We estimate the cost for a given bond using its abnormal return, which is obtained by regressing its log price returns on theoretical determinants of changes in the fundamental bond value (e.g., Ellul, Jotikasthira, and Lundblad (2011)). Specifically, we estimate the regression using data for the period [−180, −1] days from the event day and measure the abnormal return as the regression fitting errors over days 0 to +30. As the ML database stops covering a bond once it exits from ML’s IG index (except for a few downgraded bonds that are subsequently included in ML’s HY index), we use Markit data on daily prices of corporate bonds around the events in this exercise. 

Panel C of Figure 6 compares the (average) estimated cost of downgrades with the average holding cost as implied by the search model, � _χk_ + _c_ ¯ � _χc_ , where _c_ ¯ denotes the average coupon rate of all issues in the country. The plot indicates a clear positive relation between the two costs. For instance, AUS has the highest _χ_ � _k_ + _c_ ¯ � _χc_ and the second-highest average fire-sale loss from fallen angels over a 30-day horizon at 1.81%. We also estimate the cost of forced selling due to all exclusion events based on the ICE BofA ML corporate index, which include (i) downgrades to junk, (ii) time to maturity becoming less than one year, and (iii) other scenarios for a bond to exit the index. As indicated in Panel D, this estimated cost is also strongly correlated with _χ_ � _k_ + _c_ ¯ � _χc_ . 

Lastly, consider the empirical relevance of our estimates for _λ_ and _β_ . In the Duffie, Gârleanu, and Pedersen (2005) model with only one bond, _λ_ captures the intensity of investors’ search for dealers as well as dealers’ search for investors. In practice, there are thousands of bonds to be potentially traded in a given market, and the ease of finding counterparties to trade a bond is directly related to the number of dealers quoting the bond. On the other hand, since investors find dealers through random search and must bargain with dealers sequentially, _λ_ also depends on the size of the dealer base, on which investors also rely. In an extreme scenario, if there is only one bond dealer in a country who provides quotations for all bonds in the country, then _λ_ equals one and the secondary market is essentially centralized. Accordingly, we proxy for the dealer-customer meeting rate of bond _i_ in country _j_ using the average number of dealers quoting bond _i_ scaled by the total number of contributing dealers 

_The Global Credit Spread Puzzle_ 

147 

in country _j_ .[20] We construct this ratio using data on daily trader quotes for individual bonds from the Markit Bond Pricing Database and then aggregate this ratio country by country. We find that while a typical corporate bond in ITA has 17.6% of all dealers quoting it on average, it is over 26% in DEU and FRA. Panel E of Figure 6 indicates that[�] _λ_ is positively related to this proxy for the dealer-customer meeting rate. In particular, the higher[�] _λ_ is, the easier it is for an investor to find dealers to trade a particular bond. 

Parameter _β_ represents dealers’ bargaining power relative to that of customers and is difficult to measure because the bargaining process is unobservable. We follow Friewald and Nagler (2019) and measure _β_ using the likelihood of a bond becoming a “fallen angel.” The intuition is that a rating downgrade puts pressure on several types of bond investors to sell the bond[21] and thus puts them in an unfavorable position when negotiating with dealers (Lagos, Rocheteau, and Weill (2011)). In our implementation, we collect downgrades from IG to HY status as recorded in the Moody’s DRD from 1970 to 2017 and calculate the annual downgrading frequency at the country level, where 1970 is chosen as the start year due to the limited coverage of non-U.S. issuers in _Moody’s DRD_ prior to that point. We then aggregate this ratio for each country and plot it against our _β_[�] . Panel F of Figure 6 shows that our _β_[�] is empirically relevant: The higher the frequency of rating downgrades, the lower _β_[�] . 

## _C. Performance of the Model with Endogenous Liquidity_ 

In this subsection, we implement the HM model and investigate whether incorporating search frictions into the BC model helps improve model performance. We first examine the ability of the HM model to predict credit spread levels as well as their distributions. We then focus on the explanatory power of the model for the variations of credit spreads. For comparison, we implement the HM model with _d_ = _dswap[FS]_[only][and][refer][to][this][model][specification] as HM( _dswap[FS]_[).] 

## _C.1. Impact on the CSP_ 

To ensure that the HM and BC model–implied default probabilities under P are the same, we implement equation (5) with the same set of nonsearchrelated inputs as summarized in Section III.B. We calculate the predicted yield, _y[HM]_ , using the bid price in equation (10). As the BC and HM models have the same P-measure default probabilities, the yield differential, _y[HM] L_ = 

20 This measure is also related to Friewald and Nagler’s (2019) proxy for search frictions, which reflects the overall connectivity between dealers. When dealers are not closely connected, they tend to quote distinct sets of bonds, and thus the scaled number of dealers for an average bond is expected to be low. 

> 21 Ellul, Jotikasthira, and Lundblad (2011) show that regulatory constraints imposed on insurance companies lead to forced selling of fallen angels. Chen et al. (2014) find evidence for changes in the investment practices of bond market participants as induced by rating-sensitive investor clientele. 

_The Journal of Finance[®]_ 

148 

_y[HM]_ − _y[BC]_ , represents the HM model–implied liquidity component of _y[HM]_ . The question is: how much can this liquidity component explain the gap between observed yields and _y[BC]_ ? 

To answer this question, we first examine the explanatory power of _y[HM] L_ for the BC pricing errors at the bond level using panel regressions (in an analysis detailed in Section IV.F of the Internet Appendix). We find that _y[HM] L_ has a significantly negative coefficient and captures 25% of the variation in BC pricing errors. Importantly, _y[HM] L_ remains highly significant in the presence of all the potential drivers of the pricing errors that are considered in Section III.E, and indeed absorbs the role of observed proportional bid-ask spreads. These regression results suggest that the HM model reasonably characterizes the liquidity component in bond yield spreads. 

Next, we compare the HM model–implied spreads with their counterparts in the data. Figure 3 plots 30 pairs of (data, HM( _dswap[FS]_[)) (blue asterisks), along] with their counterparts under BC( _dswap[FS]_[)][(pink][dots).][Among][the][24][IG][pairs,] the number of blue asterisks (pink dots) located above the 45[◦] fair-pricing line is seven (18), with one (seven), three (five), and three (six) for AA+, A, and BBB, respectively, that is, visually the HM model underpredicts the average spread for only seven out of 24 IG/country/ _dswap[FS]_[bins,][as][opposed][to][18][in][the] case of BC( _dswap[FS]_[).] 

Table IV reports the MPEs of the HM model for the 24 IG/country/ _dswap[FS]_[bins] in rows labeled “HM( _dswap[FS]_[)” with (Panel A) and without (Panel B) observations] with negative spreads included. Panel A shows that the number of bins with a significantly negative MPE is now six under HM( _dswap[FS]_[),][down][from][17][un-] der BC( _dswap[FS]_[)][and][16][under][CDG(] _[d][CDG] swap_[).][There][are][also][five][IG/country/] _[d] swap[FS]_ bins with an insignificant MPE under HM( _dswap[FS]_[)—(AA][+][,A)/GBR,][A/CAN,] AA+/DEU, and AA+/AUS—but a significantly negative MPE under BC( _dswap[FS]_[).] The most striking improvement occurs in Australian bonds, whose rounded MPEs in bps for AA+, A, and BBB go from (−98, −125, −151) under BC( _dswap[FS]_[)] to (6, −15, −10) under HM( _dswap[FS]_[).][The][HM][model][also][significantly][improves] the rounded MPE of the HY/GBR group from −172 bps under BC( _dswap[FS]_[)][to] −40 bps, and that of HY/DEU from −137 bps to −26 bps. However, for those bins for which the BC model already overestimates spreads (e.g., (AA+, A, BBB)/JPN and BBB/FRA) or fairly predicts spreads (e.g., AA+/CAN, HY/ITA, and HY/USA), incorporating search frictions does not help. As expected, the MPEs reported in Panel B are either more negative or less positive than their counterparts in Panel A. For instance, in the case of FRA, the rounded MPE in bps under HM( _dswap[FS]_[)][for][(AA][+][,][A,][BBB,][HY)][drops][from][(13,][105,][76,][218)] in Panel A to (10, 55, 35, 189) in Panel B. The number of IG/country/ _dswap[FS]_[bins] with a significantly negative MPE under HM( _dswap[FS]_[) continues to be six.] 

The results shown in Table IV are based on the full sample of nonfinancial firms. If we focus on industrial issuers (see Section IV.C.2 of the Internet Appendix), the number of IG/country/ _dswap[FS]_[bins][with][a][significantly][negative] MPE under HM( _dswap[FS]_[)][is][seven][with][or][without][controls][for][negative][spreads.] 

_The Global Credit Spread Puzzle_ 

149 

**==> picture [359 x 384] intentionally omitted <==**

**----- Start of picture text -----**<br>
AA+ A<br>120<br>Black-Cox<br>100 AUS He-Milbradt A US 150<br>AUS A US<br>80<br>ITA I TA<br>GBR G BR<br>100<br>60<br>ITA I TACAN C AN<br>CAN C AN<br>40 FR A F RA USA U DEUSA DF RAEU F RA<br>GBR G BR 50<br>DEUUSA DU EUSA<br>20<br>J PNJ PN<br>0 JPN J PN 0<br>0 50 100 0 50 100 150<br>Model (bps) Model (bps)<br>BBB HY<br>200<br>500<br>AUS A US<br>GBR G BR GBR G BR<br>150 CAN C AN 400 US A U S A<br>USA U SA CAN C AN<br>ITA I TA 300<br>FRA F RA<br>100 F RAF RA<br>DEU D EU DEU D EU<br>200<br>ITA I TA<br>50<br>100<br>J PNJ PN<br>0 0<br>0 50 100 150 200 0 200 400<br>Model (bps) Model (bps)<br>Data (bps) Data (bps)<br>Data (bps) Data (bps)<br>**----- End of picture text -----**<br>


**Figure 3. Predicted versus observed corporate bond spreads over swap rates** . This figure plots the average observed corporate bond yield spreads over swap rates against their predicted counterparts for each of 30 credit rating/country groups in the sample. Predicted spreads are calculated using either the Black and Cox (1976) model (pink dots) or (a variant of) the He and Milbradt (2014) model (blue asterisks) with the default boundary _dswap[FS]_[. For investment-grade] groups (AA+, A, or BBB groups), all eight countries are plotted, including Australia (AUS), Canada (CAN), France (FRA), Germany (DEU), Italy (ITA), Japan (JPN), the United Kingdom (GBR), and the United States (USA). For high-yield (HY) bonds, AUS and JPN have no such bonds in the sample. (Color figure can be viewed at wileyonlinelibrary.com) 

This result is consistent with the earlier evidence that the CSP is stronger in industrial issuers. 

Table V presents the MPEs of the HM model for the eight IG[ctry] / _dswap[FS]_[bins in] rows labeled “HM( _dswap[FS]_[).” For the full sample (Panel A), HM(] _[d] swap[FS]_[) overcomes] 

_The Journal of Finance[®]_ 

150 

the underprediction problem of BC( _dswap[FS]_[) for ITA and USA, reducing the num-] ber of bins with a significantly negative MPE to three (AUS, CAN, and GBR) from five under BC( _dswap[FS]_[).][Furthermore,][although][HM(] _[d] swap[FS]_[)][still][underpre-] dicts the mean IG spread in AUS, CAN, and GBR, the model fit improves substantially: The rounded MPEs in bps for these three countries go from (−133, −89, −62) under BC( _dswap[FS]_[) to (][−][13,][ −][16,][ −][5) under HM(] _[d] swap[FS]_[). The MPEs for] JPN, DEU, and FRA, however, become more positive under HM( _dswap[FS]_[) than un-] der BC( _dswap[FS]_[).][Panel][B][shows][that][although][excluding][negative][spreads][does] not affect the MPEs of HM( _dswap[FS]_[)][qualitatively,][the][positive][MPEs][for][JPN,] DEU, FRA, and USA decline significantly relative to the full sample. Moreover, HM( _dswap[FS]_[)][now][overcomes][the][underprediction][problem][of][BC(] _[d] swap[FS]_[)][for] three countries (DEU, ITA, and USA). The MPEs of HM( _dswap[FS]_[)][for][industrial] issuers without and with controls for negative spreads, reported in Panels C and D, are qualitatively the same as their counterparts for nonfinancial issuers in Panels A and B, except that the MPE for ITA is now insignificantly different from zero. 

The incremental impact of incorporating search frictions is most notable in Panel D, in which the sample used is most comparable to those used in the literature and the MPE of BC( _dswap[FS]_[)][is][significantly][negative][for][every][coun-] try except JPN. First, HM( _dswap[FS]_[)][overcomes][the][CSP][in][DEU,][FRA,][ITA,][and] USA. Second, the CSP becomes much weaker in AUS, CAN, and GBR: The rounded MPEs in bps for the three countries improve from (−134, −106, −86) under BC( _dswap[FS]_[)][to][(][−][11,][−][25,][−][25)][under][HM(] _[d] swap[FS]_[).][Taken][together,][these] results show that the HM model helps significantly mitigate the CSP at the country level. 

For ease of comparison, Panel A1 of Table IX summarizes the main results on the ability of the BC, CDG, and HM models to match the average spread on individual IG/country/ _dswap[FS]_[bins][(columns][(1)][to][(3)),][IG][bonds][at][the][country] level (columns (4) to (6)), or three IG groups in either the U.S. or non-U.S. subsample (columns (7) to (12)). Note that in the case of the non-U.S. sample, we implement the BC model only because the purpose of using this pooled sample is to check the robustness of the CSP. In sum, we find that incorporating search frictions significantly reduces both the number of IG/country/ _dswap[FS]_[groups and] the number of countries with the underprediction problem, thereby providing evidence that doing so helps mitigate the GCSP. 

## _C.2. Distribution of the HM Model–Implied Spreads over Swap Rates_ 

To see more clearly where the predictive power of the HM model for the average IG spreads comes from, we examine the distribution of the HM( _dswap[FS]_[)-] implied credit spreads in this subsection. For convenience, let _sCR[Data]_ and _sCR[M]_ denote the observed credit spread and the model _M_ -implied spread for bonds rated _CR_ , respectively, where _M_ = {BC, CDG, HM} and _CR_ = {AA+, A, BBB, HY}. Similarly, let _s_ ¯ _CR[Data]_ and _s_ ¯ _CR[M]_[denote][the][mean][observed][and][predicted] spreads, respectively. 

_The Global Credit Spread Puzzle_ 

151 

## **Table IX** 

## **Summary of Results for Investment-Grade (IG) Credit Spreads** 

This table summarizes results on the ability of three alternative credit risk models to predict IG corporate bond yield spreads over swap rates (Panel A) and government bond yields (Panel B). The three models are the BC( _d_ ), CDG( _d_ ), and HM( _d_ ) models, where _d_ denotes the default boundary used in the implementation of the models. Parameter _drf[M]_[is][as][defined][in][Table][III][,] where _M_ = { _FS, BGY, HNS_ } and _rf_ = { _Govt, swap_ }; _d[CDG] rf_ is the counterpart of _drf[M]_[under the CDG] model. There are three IG categories (AAA&AA, A, BBB) in each of eight countries in our sample. For a given default boundary _d_ , there are 24 IG/country bins (a combination of three IG categories and eight countries), eight IG[ctry] bins (eight IG groups at the country level), three IG/USA bins in the U.S. subsample, and three IG[non-US] bins in the non-U.S. subsample. Panel A1 tabulates the number of IG/country bins (columns (1) to (3)), the number of IG[ctry] bins or countries (columns (4) to (6)), and the number of IG groups in either the U.S. (columns (7) to (9)) or non-U.S. subsamples (columns (10) to (12)) for which a given credit risk model underpredicts (“under”), fairly predicts (“fair”), or overpredicts (“over”) the average IG yield spreads over swap rates. The results are reported for the full sample with and without controls for negative observed yield spreads, as well as for the subsample of industrial issuers with and without controls for negative observed yield spreads. Panel B1 is the government bond yield–based counterpart of Panel A1 for the full sample. Panel A2 (B2) reports the slope coefficient and _R_[2] from a panel regression of observed yield spreads over swap rates (government bond yields) for individual IG bonds in each country on their predicted spreads by a given structural model. Panel A3 (B3) shows the time-series correlation between the average observed and predicted IG credit spreads over swap rates (government bond yields) for each country. 

||(1)<br>(2)<br>(3)<br>(4)<br>(5)<br>(6)<br>(7)<br>(8)<br>(9)<br>(10)<br>(11)<br>(12)|
|---|---|
||Panel A: Swap Rates as the Default-Free Rates|
||Panel A1: Prediction of Average Corporate Yield Spreads|
||# of IG/country bins<br># of IGctry bins<br># of IG/USA bins<br># of IGnon-US bins|
|Model|under<br>fair<br>over<br>under<br>fair<br>over<br>under<br>fair<br>over<br>under<br>fair<br>over|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|Full Sample<br>Full Sample|
||17<br>2<br>5<br>5<br>1<br>2<br>3<br>0<br>0<br>2<br>0<br>1<br>19<br>1<br>4<br>6<br>1<br>1<br>3<br>0<br>0<br>2<br>0<br>1<br>17<br>3<br>4<br>6<br>1<br>1<br>3<br>0<br>0<br>2<br>1<br>0<br>16<br>3<br>5<br>6<br>1<br>1<br>6<br>5<br>13<br>3<br>0<br>5|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|Negative Credit Spreads Excluded<br>Negative Credit Spreads Excluded|
||19<br>2<br>3<br>6<br>1<br>1<br>3<br>0<br>0<br>3<br>0<br>0<br>20<br>1<br>3<br>7<br>0<br>1<br>3<br>0<br>0<br>3<br>0<br>0<br>19<br>4<br>1<br>7<br>0<br>1<br>3<br>0<br>0<br>3<br>0<br>0<br>16<br>4<br>4<br>6<br>1<br>1<br>6<br>5<br>13<br>4<br>0<br>4|
||(_Continued_)|



_The Journal of Finance[®]_ 

152 

**Table IX** _—Continued_ 

||(1)<br>(2)<br>(3)<br>(4)<br>(5)<br>(6)<br>(7)<br>(8)<br>(9)<br>(10)<br>(11)<br>(12)|
|---|---|
||Panel A: Swap Rates as the Default-Free Rates|
||Panel A1: Prediction of Average Corporate Yield Spreads|
||# of IG/country bins<br># of IGctry bins<br># of IG/USA bins<br># of IGnon-US bins|
|Model|under<br>fair<br>over<br>under<br>fair<br>over<br>under<br>fair<br>over<br>under<br>fair<br>over|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|Industrial Issuers<br>Industrial Issuers|
||19<br>2<br>3<br>6<br>1<br>1<br>3<br>0<br>0<br>2<br>0<br>1<br>20<br>1<br>3<br>7<br>0<br>1<br>3<br>0<br>0<br>2<br>0<br>1<br>18<br>2<br>4<br>7<br>0<br>1<br>3<br>0<br>0<br>2<br>0<br>1<br>14<br>5<br>5<br>6<br>0<br>2<br>7<br>4<br>13<br>3<br>1<br>4|
|BC(_dFS_<br>_swap_)<br>BC(_dBGY_<br>_swap_)<br>BC(_dHNS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|Industrial Issuers w/o Neg. Sprds.<br>Industrial Issuers w/o Neg. Sprds.|
||20<br>1<br>3<br>7<br>0<br>1<br>3<br>0<br>0<br>2<br>1<br>0<br>21<br>0<br>3<br>7<br>0<br>1<br>3<br>0<br>0<br>3<br>0<br>0<br>21<br>0<br>3<br>7<br>0<br>1<br>3<br>0<br>0<br>3<br>0<br>0<br>15<br>4<br>5<br>6<br>1<br>1<br>7<br>4<br>13<br>4<br>1<br>3|



Panel A2: Security-Level Regression of Actual Spreads on Predicted Spreads 

|BC(_dFS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|Slope<br>_R_2<br>Slope<br>_R_2<br>Slope<br>_R_2|JPN<br>0.36<br>0.34<br>0.01<br>0.00<br>0.36<br>0.40|GBR<br>0.53<br>0.29<br>0.16<br>0.03<br>0.67<br>0.58|DEU<br>0.34<br>0.25<br>0.00<br>0.00<br>0.40<br>0.36|FRA<br>0.28<br>0.24<br>0.07<br>0.01<br>0.33<br>0.34|ITA<br>0.40<br>0.34<br>0.01<br>0.00<br>0.48<br>0.51|CAN<br>0.66<br>0.35<br>0.30<br>0.05<br>0.81<br>0.73|AUS<br>0.87<br>0.19<br>0.32<br>0.21<br>0.81<br>0.79|USA<br>0.43<br>0.24<br>0.07<br>0.01<br>0.59<br>0.54|
|---|---|---|---|---|---|---|---|---|---|



Panel A3: Time-Series Correlation of Average Observed and Predicted IG Spreads 

|BC(_dFS_<br>_swap_)<br>CDG(_dCDG_<br>_swap_)<br>HM(_dFS_<br>_swap_)|JPN<br>0.70<br>0.57<br>0.72|GBR<br>0.90<br>0.44<br>0.94|DEU<br>0.57<br>−0.14<br>0.68|FRA<br>0.55<br>0.17<br>0.65|ITA<br>0.76<br>0.53<br>0.87|CAN<br>0.60<br>0.86<br>0.86|AUS<br>USA<br>0.64<br>0.73<br>0.73<br>0.51<br>0.92<br>0.91<br>(_Continued_)|
|---|---|---|---|---|---|---|---|



_The Global Credit Spread Puzzle_ 

153 

**Table IX** _—Continued_ 

Panel B: Government Bond Yields as the Default-Free Rates 

Panel B1: Prediction of Average Corporate Yield Spreads 

|Model|# of IG/country bins|# of IGctry bins|# of IG/USA bins|# of IGnon-US bins|
|---|---|---|---|---|
||under<br>fair<br>over|under<br>fair<br>over|under<br>fair<br>over|under<br>fair<br>over|
|BC(_dFS_<br>_Govt_)<br>BC(_dBGY_<br>_Govt_ )<br>BC(_dHNS_<br>_Govt_ )<br>CDG(_dCDG_<br>_Govt_ )<br>HM(_dFS_<br>_Govt_)|21<br>2<br>1<br>24<br>0<br>0<br>22<br>2<br>0<br>20<br>2<br>2<br>12<br>7<br>5|7<br>0<br>1<br>8<br>0<br>0<br>8<br>0<br>0<br>6<br>1<br>1<br>5<br>2<br>1|3<br>0<br>0<br>3<br>0<br>0<br>3<br>0<br>0|3<br>0<br>0<br>3<br>0<br>0<br>3<br>0<br>0|



Panel B2: Security-Level Regression of Actual Spreads on Predicted Spreads 

|BC(_dFS_<br>_Govt_)<br>CDG(_dCDG_<br>_Govt_ )<br>HM(_dFS_<br>_Govt_)|Slope<br>_R_2<br>Slope<br>_R_2<br>Slope<br>_R_2|JPN<br>0.13<br>0.16<br>0.00<br>0.00<br>0.13<br>0.17|GBR<br>0.14<br>0.06<br>0.19<br>0.06<br>0.21<br>0.15|DEU<br>0.16<br>0.09<br>0.02<br>0.00<br>0.24<br>0.21|FRA<br>0.15<br>0.10<br>0.04<br>0.00<br>0.22<br>0.22|ITA<br>0.42<br>0.30<br>−0.02<br>0.00<br>0.57<br>0.58|CAN<br>0.05<br>0.02<br>0.25<br>0.05<br>0.09<br>0.08|AUS<br>0.73<br>0.06<br>0.25<br>0.18<br>0.80<br>0.75|USA<br>0.37<br>0.16<br>0.08<br>0.02<br>0.46<br>0.41|
|---|---|---|---|---|---|---|---|---|---|



Panel B3: Time-Series Correlation of Average Observed and Predicted IG Spreads 

|BC(_dFS_<br>_Govt_)<br>CDG(_dCDG_<br>_Govt_ )<br>HM(_dFS_<br>_Govt_)|JPN<br>0.62<br>0.27<br>0.66|GBR<br>0.71<br>0.55<br>0.88|DEU<br>0.60<br>0.00<br>0.81|FRA<br>0.50<br>0.25<br>0.71|ITA<br>0.75<br>0.38<br>0.91|CAN<br>0.35<br>0.87<br>0.89|AUS<br>0.66<br>0.69<br>0.97|USA<br>0.67<br>0.47<br>0.95|
|---|---|---|---|---|---|---|---|---|



Table VI tabulates the percentiles of the HM model–implied spreads for each of 30 CR/country groups in rows labeled “HM( _dswap[FS]_[).”][As][expected,][the][HM] model lowers the model performance for the three IG/JPN groups, which all exhibit an overprediction problem even under BC( _dswap[FS]_[). We therefore focus on] the remaining 27 groups in the discussion that follows. Note first that the HM model generates sizable spreads in the left tail across all CR/country groups. As a result, the model improves the fit in the left tail except for AA+/UK, AA+/DEU, and AA+/USA, whose 10[th] percentiles for spreads are all negative. For example, the 10[th] percentiles in bps by credit ratings in the United States are ( _s[Data] A , s[BC] A[,][ s][CDG] A , s[HM] A_ ) = (9 _,_ 0 _,_ 0 _,_ 7), ( _s[Data] BBB[,][ s][BC] BBB[,][ s][CDG] BBB[,][ s] BBB[HM]_[)][ =][(32] _[,]_[ 0] _[,]_[ 0] _[,]_[ 26),] and ( _s[Data] HY[,][ s][BC] HY[,][ s][CDG] HY[,][ s] HY[HM]_[)][ =][(99] _[,]_[ 12] _[,]_[ 4] _[,]_[ 89).][Similarly,][the][HM][model][also][no-] tably improves the fit to the spreads at the 25[th] percentile for each of the 27 non-Japan groups. Furthermore, the model matches the median spread much 

_The Journal of Finance[®]_ 

154 

better than the BC model does, except for AA+/CAN, HY/FRA, and HY/ITA. For example, in the case of the BBB/USA group, the 25[th] and 50[th] percentiles are: _s[Data]_[(49] _[,]_[ 91),] _[ s][BC]_[(3] _[,]_[ 29), and] _[ s][HM]_[(47] _[,]_[ 97).] _BBB_[=] _BBB_[=] _BBB_[=] The impact of higher left-tail spreads on the mean predicted spread can be seen clearly in the BBB/AUS and BBB/USA groups. In the former case, ( _s[Data] BBB[,][ s][BC] BBB[,][ s][CDG] BBB[,][ s] BBB[HM]_[)][ =][(72] _[,]_[ 0] _[,]_[ 39] _[,]_[ 53)][at][the][10][th][percentile][and] (608 _,_ 319 _,_ 619 _,_ 604) at the 99[th] percentile, and ( ¯ _s[Data] BBB[,][s]_[¯] _[BC] BBB[,][s]_[¯] _[CDG] BBB[,][s]_[¯] _[HM] BBB_[)][ =] (164 _,_ 14 _,_ 121 _,_ 155). That is, even though _s[HM] BBB_[is][slightly][lower][than] _[s][CDG] BBB_ at the 99[th] percentile, _s_ ¯ _[HM] BBB_[is][much][higher][and][closer][to] _[s]_[¯] _[Data] BBB_[than] _[s]_[¯] _[CDG] BBB_[.] The results for the BBB/USA group illustrate this point further, noticing that ( _s[Data] BBB[,][ s][BC] BBB[,][ s][CDG] BBB[,][ s] BBB[HM]_[)][ =][(679] _[,]_[ 841] _[,]_[ 1087] _[,]_[ 901)][at][the][99][th][percentile][and] ( ¯ _s[Data] BBB[,][s]_[¯] _[BC] BBB[,][s]_[¯] _[CDG] BBB[,][s]_[¯] _[HM] BBB_[)][ =][(131] _[,]_[ 98] _[,]_[ 74] _[,]_[ 156). Taken together, these findings pro-] vide clear evidence that the default-driven liquidity component of _y[HM]_ , a key insight of He and Milbradt (2014), plays an essential role in raising the model spreads in the left tail and thus helping overcome the underprediction problem in many of the 21 non-JPN IG/country groups. The performance of the HM model in fitting the spreads in the right tail, however, is mixed. When the BC model significantly underpredicts the spread in the right tail, the HM model can improve the fit substantially. For example, in the case of spreads at the 99[th] percentile, ( _s[Data] A , s[BC] A[,][ s] A[HM]_ ) = (498 _,_ 67 _,_ 493) bps for A/AUS and ( _s[Data] BBB[,][ s][BC] BBB[,][ s] BBB[HM]_[)][ =][(781] _[,]_[ 608] _[,]_[ 696) bps for BBB/GBR. When] the BC model overpredicts or slightly underpredicts the spread in the right tail, however, incorporating search frictions will lead to overprediction of the spread, and the magnitude of overprediction could be fairly large. For example, ( _s[Data] A , s[BC] A[,][ s] A[HM]_ ) at the 90[th] percentile = (113 _,_ 104 _,_ 173) for A/USA and (272 _,_ 280 _,_ 352) for BBB/USA. 

To summarize, incorporating search frictions into the BC model raises the model spread, but the impact of doing so on model performance varies across different quantiles of credit spreads. The liquidity component ( _y[HM] L_ ) generally improves the model fit for spreads at the 50[th] or lower percentiles, and consequently the fit for the average IG spread. This is also the case for spreads in the right tail for certain IG/country groups of bonds, but the liquidity component can be overly high in some other IG/country groups. In Section IV.H of the Internet Appendix, we repeat the analysis of this subsection using the subsamples of positive spreads and industrial issuers and obtain similar results. We also examine Q-Q plots of IG credit spreads at the country level and find that the HM model significantly improves the shape of the distribution of the predicted spreads in all countries. 

## _C.3. Comovement between Predicted and Observed Spreads_ 

Our analysis so far focuses on the ability of structural models to fit the level and distribution of credit spreads. However, a model with superb performance along these dimensions does not necessarily lead to a close one-to-one correspondence between the modeled and observed spreads. In this subsection, we focus on this aspect of model performance, in particular, the explanatory power 

_The Global Credit Spread Puzzle_ 

155 

of the BC, CDG, and HM models for the variation in IG credit spreads. We relegate details of this analysis to Sections IV.H.5 and IV.H.6 of the Internet Appendix and summarize its main results below. 

We first run a panel regression of monthly observed spreads on individual IG bonds on their predicted counterparts under each of the three structural models for each country. Panel A2 of Table IX reports the slope coefficient and regression _R_[2] under each model for each country. Under model BC( _dswap[FS]_[),][the] slope coefficient ranges from 0.28 for FRA to 0.87 for AUS, and the _R_[2] from 0.19 for AUS to 0.35 for CAN. The slope coefficient under model CDG( _d[CDG] swap_[),] however, is much lower than its counterpart under BC( _dswap[FS]_[) for every country;] this is also the case for the _R_[2] except AUS, for which the _R_[2] is 0.21 under CDG( _d[CDG] swap_[).][22][In][contrast,][the] _[R]_[2][under][HM(] _[d] swap[FS]_[)][is][notably][higher][than][its] counterpart under either the BC or CDG model, ranging from 0.34 for FRA to 0.79 for AUS. This is also the case for the slope coefficient, which is closer to one under the HM model for all countries except AUS (for JPN, the slope coefficient = 0 _._ 361 [BC] and 0 _._ 364 [HM]). Overall, the HM model substantially improves the cross-sectional fit of individual IG credit spreads in every country. This conclusion is reinforced by the results on the three models’ absolute pricing errors as shown in Section IV.H.2 of the Internet Appendix. 

Given that the panel regression results are derived mainly from the crosssectional variation in credit spreads, we next examine model performance in capturing their time-series variation. To this end, we estimate the correlation (denoted _ρ[IG]_ ) between the monthly means of observed and predicted IG spreads in each country and report the results in Panel A3 of Table IX. Under BC( _dswap[FS]_[),] _[ ρ][IG]_[ranges from 0.55 in FRA to 0.90 for GBR. The] _[ ρ][IG]_[under] CDG( _d[CDG] swap_[)][is][lower][than][that][under][BC(] _[d] swap[FS]_[)][except][for][AUS][and][CAN.][In] contrast, _ρ[IG]_ under HM( _dswap[FS]_[) is higher][than its counterpart][under][either][the] BC or CDG model, ranging from 0.65 in FRA to 0.94 for GBR. Taken together, these results show that incorporating search frictions also helps better capture the time-variation of IG spreads for every country. 

## _D. Evidence Based on Yield Spreads over Government Bonds_ 

We use the swap rates as the “default-free” rates in the analysis so far. For completeness and comparison, and because corporate bond spreads are usually quoted over government bond yields in practice,[23] we repeat the main analysis 

22 The main objective in our GMM-based estimation of the CDG model is to minimize the mean fitting error. As shown in Section III.F, incorporating mean-reverting leverage ratios into the BC model clearly improves the MPE. How to improve the explanatory power of the CDG model for bond-level spreads represents an interesting question for future research. 

> 23 This is the case at least for IG bonds—the focus of this study—whereas HY bonds are often marked as a percent of face value; see, for example, _The Wall Street Journal_ , The Bloomberg Barclays U.S. Corporate Bond Index Factsheet (May 3, 2019), and The Bloomberg Barclays U.S. Corporate High Yield Bond Index Factsheet (May 20, 2020). Note that we do not take a stand here on what the “true” risk-free asset is in the eight economies. See Du, Im, and Schreger (2018), 

_The Journal of Finance[®]_ 

156 

using government bond yields as the default-free rates in Section VI of the Internet Appendix. This subsection summarizes the main results of the analysis. 

Note that some of the model inputs need to be reestimated when a different default-free rate is used. For the BC model as well as the HM model, the new estimates of _d_ — _d[FS]_[given][in][Panel][B][of][Table][III][.] _Govt[,][ d] Govt[BGY][,]_[ and] _[ d] Govt[HNS]_[—are] Table VII reports the parameter inputs to the CDG model, including _d[CDG] Govt_[(the] new estimate of _d_ ). Panel B of Table VIII tabulates the new estimate of _θ[S]_ . Panel B of Table IX summarizes our main results on model performance when government bond yields are used as the default-free rates. We highlight three main takeaways here. First, there is evidence on a government bond yield–based GCSP. For example, as indicated in Panel B1 of Table IX, the BC model underpredicts the average credit spread for 67 (21 + 24 + 22) out of 72 IG/country/ _d_ bins (column (1)) and for 23 (7 + 8 + 8) out of 24 IG[ctry] / _d_ bins (column (4)). Recall from Panel A1 of Table IX that these quantities are 53 and 17 (58 and 20 controlling for negative credit spreads) in the case of the swap rate–based CSP. In particular, there is an underprediction problem for seven out of nine IG/JPN/ _dGovt_ bins but for none of nine IG/JPN/ _dswap_ bins. These results indicate that the government-based version of the CSP is stronger than its swap rate–based version. 

Second, the HM model delivers better performance than the two other models in capturing cross-sectional variation in individual IG credit spreads. Panel B2 of Table IX reports results from panel regressions of monthly observed spreads on individual IG bonds on their predicted counterparts under each of the three models for every country. Whereas the _R_[2] under BC( _dGovt[FS]_[)][ranges] from 0.02 for CAN to 0.30 for ITA, and the _R_[2] under CDG( _d[CDG] Govt_[)][ranges][from] zero for four countries to 0.18 for AUS, the _R_[2] under HM( _dGovt[FS]_[)][is][the][highest] among the three models for every country, ranging from 0.08 for CAN to 0.75 for AUS. Moreover, the increase in the _R_[2] under HM( _dGovt[FS]_[)][is][substantial][ex-] cept for JPN. This is also the case for the slope coefficient with one exception: The CDG model has a larger slope coefficient than the HM model for CAN. Similarly, as indicated in Panel B3 of Table IX, the HM model captures the time-series correlation between the monthly means of observed and predicted IG spreads notably better than either the BC or CDG model in every country. Compared with _ρ[IG]_ under the BC (CDG) model ranging from 0.35 to 0.75 (0.00 to 0.87), _ρ[IG]_ under the HM model ranges from 0.66 for JPN to 0.97 for AUS. 

Third, the government bond yield–based CSP poses a tougher challenge to the HM model than its swap rate–based version. For instance, the model overcomes the underprediction problem for only nine out of 21 IG/country/ _dGovt[FS]_[bins] in the former version of the puzzle, but does so for 11 out of 17 IG/country/ _dswap[FS]_ bins (or for 13 out of 19 bins after controlling for negative credit spreads) in the latter version. The HM model also has lower explanatory power for individual IG credit spreads over government bonds than for spreads over swap rates. 

Diamond and Van Tassel (2023), and Augustin et al. (2024) for recent studies on this issue. Section IV.A of the Internet Appendix briefly reviews this literature. 

_The Global Credit Spread Puzzle_ 

157 

For instance, the _R_[2] under HM( _dGovt[FS]_[)][is][substantially][lower][than][its][counter-] part under HM( _dswap[FS]_[)][in][every][country,][except][ITA][(see][Panels][A2][and][B2] of Table IX). The intuition behind these findings is that because swap rates themselves help absorb the liquidity component (as well as the credit component) of corporate bond yields, there is less in corporate bond spreads over swap rates than corporate spreads over government bonds for search frictions to explain. 

To summarize, there is stronger evidence for a government bond–based CSP than its swap rate–based version. It is also more challenging for the BC model to explain individual IG credit spreads over government bonds than their swap rate–based counterparts. Nonetheless, incorporating search frictions into the model greatly helps mitigate the government bond–based CSP and raise the model’s explanatory power for individual IG credit spreads in every country. 

## **V. Conclusion** 

While the widely used structural approach to credit risk has been studied extensively using U.S. data, its applicability to other developed credit markets remains relatively unexplored. This paper undertakes an empirical investigation of three representative structural models of default, leveraging a comprehensive data set that encompasses global default occurrences as well as pricing data of corporate bonds from eight developed economies. Specifically, we implement two standard, pure default-risk models—those of Black and Cox (1976) and Collin-Dufresne and Goldstein (2001)—and a variant of the He and Milbradt (2014) model with endogenous corporate bond illiquidity, a model that has not been empirically tested in the literature. 

For the baseline results of the paper, we use the LIBOR swap rates as the “default-free” benchmark and examine the ability of the models to predict credit spreads over swap rates. We find strong evidence that, on average, the BC model underestimates the IG credit spread in corporate bond markets outside the United States, especially when the focus is directed toward industrial issuers and adjustments are made for the presence of negative credit spreads over swap rates. Moreover, by taking advantage of our panel data on security-level credit spreads across countries, we show that the limitation of the BC model is significantly linked to its incapacity to produce any meaningful credit spreads in the left tail of the credit spread distribution. 

To understand the sources of this swap rate–based GCSP, we explore two potential channels for improving the BC model as a result of analyzing its pricing errors. The first channel, through credit risk, is to incorporate mean-reverting leverage ratios by implementing the CDG model. Although this modification helps improve model performance, the overall improvement is limited, thereby strengthening the evidence for the GCSP. 

The second channel is to incorporate corporate bond illiquidity. To isolate the potential impact of bond illiquidity on the GCSP, we implement a reducedform variant of the He and Milbradt (2014) model such that its predicted 

_The Journal of Finance[®]_ 

158 

yield spread can be decomposed into two components: the BC model–implied credit component and a liquidity component owing to search frictions in the secondary corporate bond market. We find that this liquidity component helps capture certain determinants of such frictions and significantly improves overall model performance. In particular, augmenting the BC model with this liquidity component not only helps raise average IG spreads and mitigate the GCSP, but also enhances the model’s capability to capture the distribution of credit spreads. Perhaps even more impressively, this augmentation also yields a substantial refinement in the cross-sectional fit of individual IG credit spreads in every country. 

In light of the conventional practice of pricing corporate bonds with reference to spreads over government bonds, we revisit our baseline analysis by employing government bonds as the default-free benchmark. In this context, we identify a government bond yield–based incarnation of GCSP. Notably, the evidence substantiating this puzzle is much stronger than that for its swap rate–based counterpart, underscoring the latter as a mitigated version of the former. This finding is not surprising, however, given that swap spreads include both default-risk and nondefault-risk components. As a result, although incorporating search frictions into the BC model helps significantly mitigate the government bond yield–based GCSP as well, the puzzle poses a bigger challenge to the HM model than the swap rate–based GCSP. 

To summarize, our estimation of three distinct structural models indicates that to better capture the behavior of IG corporate bond credit spreads, especially spreads over government bonds, it is imperative to integrate elements of corporate debt illiquidity into the standard (pure) default risk models. Such integration not only elevates the average predicted IG yield spread, thereby mitigating the underprediction issue, but also markedly refines the cross-sectional alignment of IG credit spreads at the bond level. For instance, due to data limitations, this study estimates search friction parameters at the country level. Utilizing credit rating- or sector-specific estimates of these parameters could potentially provide a more effective way to capture the heterogeneity in corporate bond illiquidity across different countries. It is also important to note that, while this paper centers on the implications of the HM model concerning the levels of credit spreads, the model’s capacity to account for variation in credit spread changes warrants further investigation. Indeed, the evidence in our non-U.S. sample, which corroborates the seminal findings of Collin-Dufresne, Goldstein, and Martin (2001) on the determinants of spread changes in the U.S. market, suggests the potential of exploring the HM model’s implications for credit spread changes.[24] Besides corporate bond liquidity, incorporating additional credit risk channels such as stochastic asset volatility may also help 

24 In an earlier version of this paper (Huang, Nozawa, and Shi (2020)), we find that the explanatory variables used in Collin-Dufresne, Goldstein, and Martin (2001) and motivated by conventional structural credit risk models account for merely 6% ∼ 31% of the variation in yield spread changes in our sample. Focusing on the U.S. market, Friewald and Nagler (2019) and He, Khorrami, and Song (2022) show that various types of market frictions, including search and bargaining 

_The Global Credit Spread Puzzle_ 

159 

improve model performance, in particular, the explanatory power for IG credit spreads at the bond level.[25] We leave these questions to future research. 

Initial submission: July 2, 2020; Accepted: February 21, 2023 Editors: Stefan Nagel, Philip Bond, Amit Seru, and Wei Xiong 

## **REFERENCES** 

Albagli, Elias, Christian Hellwig, and Aleh Tsyvinski, 2014, Dynamic dispersed information and the credit spread puzzle, NBER Working Paper No. 19788. 

Albagli, Elias, Christian Hellwig, and Aleh Tsyvinski, 2024, Information aggregation with asymmetric asset payoffs, _Journal of Finance_ 79, 2715–2758. 

Ambrose, Brent W., Kelly N. Cai, and Jean Helwege, 2012, Fallen angels and price pressure, _Journal of Fixed Income_ 21, 74–86. 

Amihud, Yakov, and Haim Mendelson, 1986, Asset pricing and the bid-ask spread, _Journal of Financial Economics_ 17, 223–249. 

Augustin, Patrick, Mikhail Chernov, Lukas Schmid, and Dongho Song, 2024, The term structure of covered interest rate parity violations, _Journal of Finance_ 79, 2077–2114. 

Avramov, Doron, Gergana Jostova, and Alexander Philipov, 2007, Understanding changes in corporate credit spreads, _Financial Analysts Journal_ 63, 90–105. 

Bai, Jennie, and Pierre Collin-Dufresne, 2019, The CDS-bond basis, _Financial Management_ 48, 417–439. 

Bai, Jennie, Robert Goldstein, and Fan Yang, 2020, Is the credit spread puzzle a myth?, _Journal of Financial Economics_ 137, 297–319. 

Bakshi, Gurdip, Xiaohui Gao, and Zhaodong Zhong, 2022, Decoding default risk: A review of modeling approaches, findings, and estimation methods, _Annual Review of Financial Economics_ 14, 391–413. 

Bao, Jack, 2009, Structural models of default and the cross section of corporate bond yield spreads, Working Paper, MIT. 

Bao, Jack, and Kewei Hou, 2017, De facto seniority, credit risk, and corporate bond prices, _Review of Financial Studies_ 30, 4038–4080. 

Bao, Jack, and Jun Pan, 2013, Bond illiquidity and excess volatility, _Review of Financial Studies_ 26, 3068–3103. 

Bhamra, Harjoat S., Lars-Alexander Kuehn, and Ilya A. Strebulaev, 2010, The levered equity risk premium and credit spreads: A unified framework, _Review of Financial Studies_ 23, 645– 703. 

Black, Fischer, and John C. Cox, 1976, Valuing corporate securities: Some effects of bond indenture provisions, _Journal of Finance_ 31, 351–367. 

Bollerslev, Tim, George Tauchen, and Hao Zhou, 2009, Expected stock returns and variance risk premia, _Review of Financial Studies_ 22, 4463–4492. 

Chen, Hui, 2010, Macroeconomic conditions and the puzzles of credit spreads and capital structure, _Journal of Finance_ 65, 2171–2212. 

Chen, Hui, Rui Cui, Zhiguo He, and Konstantin Milbradt, 2018, Quantifying liquidity and default risks of corporate bonds over the business cycle, _Review of Financial Studies_ 31, 852– 897. 

frictions, constitute a substantial piece of the puzzling excess common variation in credit spread changes as documented in Collin-Dufresne, Goldstein, and Martin (2001). 

> 25 Examples of studying structural models with stochastic asset volatility include McQuade (2018), Du, Elkamhi, and Ericsson (2019), and Lotfaliei (2021). Incorporating a jump component in the asset return process may also help; however, there is evidence suggesting that we need to go beyond that in order to explain the CSP in the U.S. market (see HH) or capture the dynamic behavior of CDS spreads and equity volatility (Huang, Shi, and Zhou (2020)). 

160 

## _The Journal of Finance[®]_ 

- Chen, Long, Pierre Collin-Dufresne, and Robert Goldstein, 2009, On the relation between the credit spread puzzle and the equity premium puzzle, _Review of Financial Studies_ 22, 3367– 3409. 

- Chen, Zhihua, Aziz A. Lookman, Norman Schürhoff, and Duane J. Seppi, 2014, Rating-based investment practices and bond market segmentation, _Review of Asset Pricing Studies_ 4, 162– 205. 

- Christoffersen, Peter, Du Du, and Redouane Elkamhi, 2017, Rare disasters, credit, and option market puzzles, _Management Science_ 63, 1341–1364. 

- Collin-Dufresne, Pierre, and Robert Goldstein, 2001, Do credit spreads reflect stationary leverage ratios?, _Journal of Finance_ 56, 1929–1957. 

- Collin-Dufresne, Pierre, Robert Goldstein, and Spencer Martin, 2001, The determinants of credit spread changes, _Journal of Finance_ 56, 2177–2207. 

- Cremers, KJ Martijn, Joost Driessen, and Pascal Maenhout, 2008, Explaining the level of credit spreads: Option-implied jump risk premia in a firm value model, _Review of Financial Studies_ 21, 2209–2242. 

- Culp, Christopher L., Yoshio Nozawa, and Pietro Veronesi, 2018, Option-based credit spreads, _American Economic Review_ 108, 454–488. 

- Davydenko, Sergei A., 2013, When do firms default? A study of the default boundary, Working Paper, University of Toronto. 

- Diamond, William, and Peter Van Tassel, 2023, Risk-free rates and convenience yields around the world, Working Paper, University of Pennsylvania. 

- Dick-Nielsen, Jens, Peter Feldhütter, and David Lando, 2012, Corporate bond liquidity before and after the onset of the subprime crisis, _Journal of Financial Economics_ 103, 471–492. 

- Dick-Nielsen, Jens, and Marco Rossi, 2018, The cost of immediacy for corporate bonds, _Review of Financial Studies_ 32, 1–41. https://doi.org/10.1093/rfs/hhy080 

- Djankov, Simeon, Oliver Hart, Caralee McLiesh, and Andrei Shleifer, 2008, Debt enforcement around the world, _Journal of Political Economy_ 116, 1105–1149. 

- Du, Du, Redouane Elkamhi, and Jan Ericsson, 2019, Time-varying asset volatility and the credit spread puzzle, _Journal of Finance_ 74, 1841–1885. 

- Du, Wenxin, Joanne Im, and Jesse Schreger, 2018, The U.S. Treasury premium, _Journal of International Economics_ 112, 167–181. 

- Duffie, Darrell, Nicolae Gârleanu, and Lasse Heje Pedersen, 2005, Over-the-counter markets, _Econometrica_ 73, 1815–1847. 

- Ellul, Andrew, Chotibhak Jotikasthira, and Christian T. Lundblad, 2011, Regulatory pressure and fire sales in the corporate bond market, _Journal of Financial Economics_ 101, 596–620. 

- Eom, Young Ho, Jean Helwege, and Jing-Zhi Huang, 2004, Structural models of corporate bond pricing: An empirical analysis, _Review of Financial Studies_ 17, 499–544. 

- Feldhütter, Peter, and David Lando, 2008, Decomposing swap spreads, _Journal of Financial Economics_ 88, 375–405. https://doi.org/10.1016/j.jfineco.2007.07.004 

- Feldhütter, Peter, and Stephen Schaefer, 2018, The myth of the credit spread puzzle, _Review of Financial Studies_ 31, 2897–2942. https://doi.org/10.1093/rfs/hhy032 

- Feldhütter, Peter, and Stephen Schaefer, 2023, Debt dynamics and credit risk, _Journal of Financial Economics_ 149, 497–535. https://doi.org/10.1016/j.jfineco.2023.06.007 

- Friewald, Nils, Rainer Jankowitsch, and Marti G. Subrahmanyam, 2012, Illiquidity or credit deterioration: A study of liquidity in the U.S. corporate bond market during financial crises, _Journal of Financial Economics_ 105, 18–36. 

- Friewald, Nils, and Florian Nagler, 2019, Over-the-counter market frictions and yield spread changes, _Journal of Finance_ 74, 3217–3257. 

- Goldberg, Jonathan, and Yoshio Nozawa, 2021, Liquidity supply in the corporate bond market, _Journal of Finance_ 76, 755–796. 

- Gourio, Francois, 2013, Credit risk and disaster risk, _American Economic Journal: Macroeconomics_ 5, 1–34. 

- He, Zhiguo, Paymon Khorrami, and Zhaogang Song, 2022, Commonality in credit spread changes: Dealer inventory and intermediary distress, _Review of Financial Studies_ 35, 4630–4673. 

_The Global Credit Spread Puzzle_ 

161 

- He, Zhiguo, and Konstantin Milbradt, 2014, Endogenous liquidity and defaultable bonds, _Econometrica_ 82, 1443–1508. https://doi.org/10.3982/ECTA11039 

- He, Zhiguo, Stefan Nagel, and Zhaogang Song, 2022, Treasury inconvenience yields during the Covid-19 crisis, _Journal of Financial Economics_ 143, 57–79. 

- He, Zhiguo, and Wei Xiong, 2012, Rollover risk and credit risk, _Journal of Finance_ 67, 391–430. 

- Huang, Jing-Zhi, and Ming Huang, 2012, How much of the corporate-Treasury yield spread is due to credit risk?, _Review of Asset Pricing Studies_ 2, 153–202. 

- Huang, Jing-Zhi, Bibo Liu, and Zhan Shi, 2023, Determinants of short-term corporate yield spreads: Evidence from the commercial paper market, _Review of Finance_ 27, 539–579. 

- Huang, Jing-Zhi, Yoshio Nozawa, and Zhan Shi, 2020, The global credit spread puzzle, AFA 2020 San Diego Meetings Paper. 

- Huang, Jing-Zhi, Zhan Shi, and Hao Zhou, 2020, Specification analysis of structural credit risk models, _Review of Finance_ 24, 45–98. https://doi.org/10.1093/rof/rfz006 

- Jankowitsch, Rainer, Florian Nagler, and Marti G. Subrahmanyam, 2014, The determinants of recovery rates in the U.S. corporate bond market, _Journal of Financial Economics_ 114, 155– 177. 

- Philip Jones, E., Scott P. Mason, and Eric Rosenfeld, 1984, Contingent claims analysis of corporate capital structures: An empirical investigation, _Journal of Finance_ 39, 611–625. 

- Kang, Johnny, and Carolin E. Pflueger, 2015, Inflation risk in corporate bonds, _Journal of Finance_ 70, 115–162. 

- Klingler, Sven, and Suresh Sundaresan, 2019, An explanation of negative swap spreads: Demand for duration from underfunded pension plans, _Journal of Finance_ 74, 675–710. 

- Kriebel, Johannes, Andreas Pfingsten, and Daniel Platte, 2023, The credit spread puzzle— Evidence from multiple quasi-natural experiments, Working Paper, University of Münster. 

- Kuehn, Lars-Alexander, and Lukas Schmid, 2014, Investment-based corporate bond pricing, _Journal of Finance_ 69, 2741–2776. 

- Lagos, Ricardo, Guillaume Rocheteau, and Pierre-Olivier Weill, 2011, Crises and liquidity in overthe-counter markets, _Journal of Economic Theory_ 146, 2169–2205. 

- Leland, Hayne, and Klaus Toft, 1996, Optimal capital structure, endogenous bankruptcy, and the term structure of credit spreads, _Journal of Finance_ 51, 987–1019. 

- Li, Jian, and Haiyue Yu, 2023, Investor composition and the liquidity component in the U.S. corporate bond market, _Journal of Finance_ , forthcoming. 

- Liao, Gordon, 2020, Credit migration and covered interest rate parity, _Journal of Financial Economics_ 138, 504–525. 

- Liu, Edith X., 2016, Portfolio diversification and international corporate bonds, _Journal of Financial and Quantitative Analysis_ 51, 959–983. 

- Liu, Jun, Francis Longstaff, and Ravit Mandell, 2006, The market price of risk in interest rate swaps: The roles of default and liquidity risks, _Journal of Business_ 79, 2337–2359. 

- Longstaff, Francis, Sanjay Mithal, and Eric Neis, 2005, Corporate yield spreads: Default risk or liquidity? New evidence from the credit default swap market, _Journal of Finance_ 60, 2213– 2253. 

- Longstaff, Francis, and Eduardo Schwartz, 1995, A simple approach to valuing risky fixed and floating rate debt, _Journal of Finance_ 50, 789–820. 

- Lotfaliei, Babak, 2021, Asset variance risk premium and capital structure, _Journal of Financial and Quantitative Analysis_ 56, 647–691. 

- McQuade, Timothy J., 2018, Stochastic volatility and asset pricing puzzles, Working Paper, Stanford University. 

- Merton, Robert C., 1974, On the pricing of corporate debt: The risk structure of interest rates, _Journal of Finance_ 29, 449–470. https://doi.org/10.1111/j.1540-6261.1974.tb03058.x 

- Moody’s, 2014, Government-related issuers, Moody’s Investor Service: Rating Methodology. 

- Schaefer, Stephen M., and Ilya Strebulaev, 2008, Structural models of credit risk are useful: Evidence from hedge ratios on corporate bonds, _Journal of Financial Economics_ 90, 1–19. 

- Shi, Zhan, 2019, Time-varying ambiguity, credit spreads, and the levered equity premium, _Journal of Financial Economics_ 134, 617–646. 

162 

## _The Journal of Finance[®]_ 

- S&PGlobal, 2020, Default, transition, and recovery: 2019 Annual global corporate default study and rating transitions, S&P Global Ratings Performance Analytics 1–59. 

Valenzuela, Patricio, 2016, Rollover risk and credit spreads: Evidence from international corporate bonds, _Review of Finance_ 20, 631–661. 

## **Supporting Information** 

Additional Supporting Information may be found in the online version of this article at the publisher’s website: 

**Appendix S1:** Internet Appendix. **Replication Code.** 

