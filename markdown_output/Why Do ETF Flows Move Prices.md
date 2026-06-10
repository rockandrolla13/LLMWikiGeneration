Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

## Deutsche Bank Research 

North America 

Quantitative Strategy The Quant View 

Date 9 May 2019 

## Why Do ETF Flows Move Prices? 

## Alex Chao 

## Decomposing ETF Flows 

Previous research by Chao et al (2018a, 2018b) suggests that ETF flows defined as the difference in total dollar amount owned by ETFs scaled by firm market capitalization are negatively related to expected returns. This research delves deeper by breaking the ETF flow measures into three components: (i) allocation, (ii) weight reconstitution and (iii) index reconstitution. 

## What Drives ETF Flows? 

As we show, allocation flows are frequent, small and affect many stocks. Weight reconstitution flows are periodic, different-sized and affect many stocks. Index reconstitution flows are periodic, vary in size and affect few stocks. 

## Why Should ETF Flows Affect Prices? 

The return attribution to different types of flows suggests that the “ETF Contraflow effect” associated with positioning against ETF flows is largely driven by index reconstitution, and to a more minor extent driven by weight reconstitution particularly in more recent years. Our evidence is less consistent with the idea that allocation flows have a meaningful impact on stock prices. 

Quantitative Strategist +1-212-250-9329 

Ronnie Shah Quantitative Strategist +1-212-250-1173 

Hallie Martin Strategist +1-212-250-7994 

Shuan Wei Quantitative Strategist 212-250-2098 

Jessica Zhang Quantitative Strategist +1-212-250-2835 

Deutsche Bank Securities Inc. 

Note to U.S. investors: US regulators have not approved most foreign listed stock index futures and options for US investors. Distributed on: 09/05/2019 12:54:10 GMT Eligible investors may be able to get exposure through over-the-counter products. Deutsche Bank does and seeks to do business with companies covered in its research reports. Thus, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. DISCLOSURES AND ANALYST CERTIFICATIONS ARE LOCATED IN APPENDIX 1.MCI (P) 091/04/2018. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## ETF Contraflow Strategy: A Review 

The DB Quant Research team published a paper on July 16, 2018 which suggested that ETFs were affecting underlying stock prices. The measure we used to define ETF flows is shown in the equation below: 

In our original paper we focused on a 12-month window to capture ETF flows. In this article, we have instead chosen to focus on a six month window as the shorter horizon focuses on more recent flows. Each month, we sort Russell 3000 stocks into ten equal groups within each sector based on six month ETF flow. We then form a dollar-neutral equal-weight portfolio that is long the bottom decile of stocks (largest ETF outflow) and short the top decile of stocks (largest ETF inflow). 

Figure 1: Annualized returns for portfolios formed on ETF flow (Jan 2006 – Dec 2018) 

Figure 2: Growth in wealth for portfolios formed on ETF flow 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0002-07.png)


**----- Start of picture text -----**<br>
14.0% 4.5<br>11.9%<br>12.0% 11.3% 4<br>10.2% 9.8%<br>10.0% 9.0% 8.8% 3.5<br>8.1% SR = 1.29<br>8.0% 7.6% 7.6% 3<br>2.5<br>6.0%<br>3.7% 2<br>4.0%<br>1.5<br>2.0%<br>1<br>0.0%<br>Low 2 3 4 5 6 7 8 9 High Low - 0.5<br>High 0<br>ETF Flow 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018<br>Low ETF Flow High ETF Flow Low - High<br>Source : Deutsche Bank Quantitative Strategy, Compustat, S&P, Russell, Axioma, IHS Markit Source : Deutsche Bank Quantitative Strategy, Compustat, S&P, Russell, Axioma, IHS Markit<br>Wealth ($)<br>Annualized Returns<br>**----- End of picture text -----**<br>


As we show, stocks with high ETF flows, have much lower average returns when compared to stocks with low ETF flows. The long/short return performance of a “contraflow” strategy that is long stocks with low ETF flows and short stocks with high ETF flows performs (i) strongly in 2009 and in recent periods (last 5 years). 

## What Drives Variation in ETF Flow? 

There are two reasons that stocks experience ETF flows as defined above. First, investors may change their allocation to ETFs causing flows to the underlying stocks. For example, if an investor sells a Russell 1000 ETF and buys a Russell 2000 ETF, large capitalization stocks will have out-flows and small capitalization stocks will have in-flows. Second, stocks may be added, deleted or re-weighted due to reconstitution of the ETF’s underlying benchmark index. If a stock migrates from the Russell 1000 to Russell 2000, the stock will have an outflow (for leaving Russell 1000) that is equal to its current weight (which is a function of its market capitalization relative to others in the index) multiplied by AUM of the relevant Russell 1000 ETFs. The stock will also have a corresponding inflow for entering into the Russell 2000. For non-capitalization weighted indices, there will also be reconstitution flows when the indices rebalance infrequently as stocks return back to target 

Page 2 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

weights. There are generally no weight adjustments for price drift for capitalizationweighted indices.[1] 

The decomposition of the ETF flow into allocation and reconstitution flow can be found below: 

We can further decompose flows into index and weight reconstitution flows. Index reconstitution involves a stock being added or deleted from an index (for example when a stock gets upgraded from the Russell 2000 to the Russell 1000). Weight reconstitution is generally related to stocks that are changing weights for a nonmarket capitalization weighted index. 

Our first new analysis shown in Figure 3 and 4 decomposes ETF flow cross-sectional variance into the three components listed above: allocation, weight reconstitution and index reconstitution flows. 

Our results suggest that ETF flow variation has increased substantially as the assets invested in ETFs have grown. Over the entire period, allocation, index and weight reconstitution drives 29%, 45% and 25% of total ETF flows, respectively. Allocation flows seem to be higher during specific periods that are associated with exceptional market stress (when potentially many ETFs exchanged hands as investors reallocated capital); generally, allocation flows do not have much variation across stocks. Index reconstitution flows while ever-present during our sample tend to be larger in the second half of the year compared to the first six months. Weight reconstitution is quite small earlier in the sample period, but increase substantially over the past two years, accounting for 39% of the variation in total cross-sectional ETF flow. 

> 1 Other stocks in Russell 1000 and Russell 2000 will be re-weighted dependent on the relative market-caps of additions and deletions and changes in free float, however these re-weighting flows across other index constituents are generally small for market-cap weight indices where generally no adjustment for price drift is needed. 

Page 3 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

Figure 3: Decomposition of Cross-sectional six-month ETF ~~es~~ Flow Variance (Jan 2006 – Dec 2018) 

Figure 4: Decomposition of Cross-sectional Monthly ETF Flow Variance per Calendar Month (Jan 2006 – Dec 2018) 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0004-04.png)


**----- Start of picture text -----**<br>
0.012% 0.004%<br>0.010% 0.003%<br>0.003%<br>0.008%<br>0.002%<br>0.006%<br>0.002%<br>0.004%<br>0.001%<br>0.002%<br>0.001%<br>0.000% 0.000%<br>2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec<br>Index Reconstitution Weight Reconstitution Allocation Index Reconstitution Weight Reconstitution Allocation<br>Cross-sectional Variation<br>Cross-sectional Flow Variance<br>**----- End of picture text -----**<br>


> _Source : Deutsche Bank Quantitative Strategy, Compustat, S&P, Russell, Axioma, IHS Markit_ ~~cd~~ _Source : Deutsche Bank Quantitative Strategy, Compustat, S&P, Russell, Axioma, IHS Markit_ 

Figure 5 reports the non-market capitalization assets under management and that number as a percentage of all equity ETFs AUM from 2004 to 2018 using a classification provided by Bloomberg. The assets of non-market capitalization-weighted ETFs have tripled since 2013, and these ETFs now make up close to 14% of the total amount invested in ETFs. The growing importance of re-weighting flows in our flow attribution reported in Figure 3 coincides with the growth in non-market capitalization-weighted ETF products. 

Figure 4 displays the average flows by calendar month. Index reconstitution flows are the largest in June due to the annual Russell rebalances followed by December due to MSCI’s semi-annual reviews. Index reconstitution flows are also higher in March and to a lesser extent September due to MSCI and S&P’s quarterly rebalances. The large flows in June explain why six-month ETF flows reported in Figure 3 are larger in the second half of each year. The weight reconstitution flows for most calendar months are small, but are large at the end of the calendar quarters. Overall, there isn’t much seasonality in allocation flows. 

Figure 5: Historical ETF AUM by Index Weighting from 2004 to 2018 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0004-09.png)


**----- Start of picture text -----**<br>
350 15%<br>300 14%<br>13%<br>250<br>12%<br>200 11%<br>150 10%<br>9%<br>100<br>8%<br>50 7%<br>0 6%<br>2004 2006 2008 2010 2012 2014 2016 2018<br>4 Non-Mktcap ETF AUM (LHS) d<br>Non-MktCap ETF AUM as % Total AUM (RHS)<br>Source : Deutsche Bank Quantitative Strategy, Compustat, S&P,<br>Russell, Axioma, IHS Markit, DB Delta1 Strategy<br>|<br>AUM ($bn) % of Total ETF AUM<br>**----- End of picture text -----**<br>


## Which Types of ETF Flows Are Large? 

Next, we examine the distribution of flows in a single month – specifically, we examine June 2018 as the larger ETF flows tend to occur in June and 2018 is the most recent year in our study. Figures 6, 7 and 8 calculates the June 2018 allocation, index and weight reconstitution and allocation flows for each stock in the Russell 3000 plotted in ascending order from smallest to largest flow. 

Deutsche Bank Securities Inc. 

Page 4 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

~~Oo~~ Figure 6: Monthly allocation flows for Russell 3000 stocks (June 2018) 

12% 10% 8% 6% 4% 2% 0% -2% -4% -6% -8% 

_Source : Deutsche Bank Quantitative Strategy, Compustat, S&P, Russell, Axioma, IHS Markit_ Figure 7: Monthly index reconstitution flows for Russell 3000 stocks (June ~~———~~ 2018) 12% 10% 8% 6% 4% 2% 0% -2% -4% oo -6% -8% 

- _Source : Deutsche Bank Quantitative Strategy, Compustat, S&P, Russell, Axioma, IHS Markit_ Figure 8: Monthly weight reconstitution flows for Russell 3000 stocks (June 

- ~~=~~ 2018) 

8% 6% 4% 2% 0% -2% -4% -6% 

-8% 

_Source : Deutsche Bank Quantitative Strategy, Compustat, S&P, Russell, Axioma, IHS Markit_ 

12% 10% 

Deutsche Bank Securities Inc. 

Page 5 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

As we show, allocation flows (Figure 6) increase gradually and generally show small differences between extremes. This is not the case for index reconstitution flows (Figure 6) which are essentially zero for the entire interquartile range. The distribution in flows is highly leptokurtic, which significant flows that are as much as 5% of market capitalization. Weight reconstitution (Figure 7) has a distribution which is similar to Index reconstitution but the fat tails are not as large and certain elements of the interquartile range are not zero. 

## **Allocation Flow** 

Allocation flows occur often, have small relative differences across stocks and affect most stocks. For example, when an investor allocates $1 BN USD to a Russell 1000 ETF, all stocks receive inflows that are proportional to their weight in the index. Apple, one of the larger stocks in the index has a market capitalization of approximately $960 BN, with a weight of 3.6% in the index. As a result, approximately $36 MM of the flow should be allocated to Apple. The $36 MM flow is not material for Apple as the company is very large. Since the Russell 1000 is capitalization-weighted, a stock with a $9.6 BN market capitalization will likely have a flow of $360,000. Since allocation flows are spread pro-rata according to market capitalization among many stocks, either huge differences in ETF allocations or sufficient flows into ETFs with highly concentrated stocks need to occur for these flows to be material on the single-stock level.[2] 

## **Index vs. Weight Reconstitution Flow** 

Index reconstitution flows are periodic, have large differences across stocks and affect few stocks. 

Weight reconstitution flows are periodic, vary in size and affect many stocks. For a capitalization-weighted index such as the S&P 500 or Russell 1000 there are very little weight changes during reconstitutions that are not related to stocks changing indices. These changes come into play mainly when there are indices which are not capitalization weighted (e.g. equal weight for factor weight). Our research suggests the assets tracking non-market capitalization weighted ETFs were quite small before 2012 but have grown substantially in recent years (see figure 5). 

## **Scenerio 1: Stock exits cap-weighted index a and enters cap-weighted index b** 

> 2 Note that our study examines allocation flows over a six-month window, industry-neutralizing flows by GICS sector. We did not examine short-term effects originating in large ETF allocation flows. We also by construction did not analyze the effect of Sector/Industry flows – for example, during the latest US election were very large and had potentially impacted industry stock returns. 

Page 6 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

The above equation shows that index reconstitution flow associated with a stock moving from index a to index b is proportional to the difference of the assets under management divided by the aggregate market capitalization of each index. For index a, we discount the assets under management at time t by the return on the index at time t. Our analysis suggests that if the aggregate market capitalization of Russell 2000 is $3 TN and the aggregate market capitalization of Russell 1000 is $ 30TN – the assets under management for the Russell 1000 must be 10x the assets in Russell 2000 to avoid an index reconstitution flow. Our research generally finds that the ratio of the capital invested in small capitalization ETF to large capitalization ETFs is greater than the ratio of aggregate market capitalization represented by these indices leading to a “Big Fish, Small Pond” effect or ETF outflows (inflows) when stocks are upgraded (downgraded) to large (small) capitalization index. 

## **Scenerio 2: Non-cap-weighted index c rebalances** 

_*Assume no dividends or corporate actions from t to t-1_ 

The second equation shows that weight reconstitution flow associated with a noncapitalization-weighted index rebalancing is (i) positively related to the assets tracking the ETF relative to the market capitalization of the underlying stock, the (ii) weight increase (wi,t –wi,t-1) and (iii) negatively related to the stock return relative to the underlying index return. Thus, if the stock out-performs the index and it’s weight doesn’t rise as fast, there will be an ETF outflow which is clearly expressed in the last equation. 

## How do ETF Flows Push Prices? 

Figure 9 applies the same decomposition methodology to examining whether certain components of ETF flows have a larger impact on expected returns. While the ETF contraflow strategy of taking long positions in low ETF flow stocks and short positions in high ETF flow stocks generates a Sharpe ratio of 1.29. Focusing on index reconstitution alone yields a Sharpe ratio of 0.82, while sorting stocks on weight reconstitution produces a Sharpe ratio of 0.51. Allocation flows while additive, have lower return predictability (SR=0.30). 

Deutsche Bank Securities Inc. 

Page 7 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 

The Quant View 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0008-03.png)


**----- Start of picture text -----**<br>
Figure 9: Annualized returns for portfolios formed on six-month ETF flow, recon-<br>stitution, and allocation flows (Jan 2006 - Dec 2018)<br>14%<br>SR = 0.82<br>SR = 1.29<br>12%<br>10% SR = 0.30<br>SR = 0.51<br>8%<br>6%<br>4%<br>2%<br>0%<br>Low 2 3 4 5 6 7 8 9 High Low -<br>Decile High<br>dunititty ETF Flows Allocation Index Reconstitution Weight Reconstitution<br>Source : Deutsche Bank Quantitative Strategy, Compustat, S&P, Russell, Axioma, IHS Markit<br>Figure 10: Growth in wealth for portfolios formed on ETF flows, reconstitution,<br>and allocation flows<br>Annualized Returns<br>**----- End of picture text -----**<br>



![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0008-04.png)


**----- Start of picture text -----**<br>
2.8<br>2.3<br>1.8<br>1.3<br>0.8<br>2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018<br>ETF Flows Allocation Index Reconstitution Weight Reconstitution<br>Wealth ($1)<br>**----- End of picture text -----**<br>


_Source : Deutsche Bank Quantitative Strategy, Compustat, S&P, Russell, Axioma, IHS Markit_ 

Figure 10 reports the growth in wealth for monthly rebalanced portfolios formed on ETF, allocation, index and weight reconstitution flows. Most of the returns are driven by reconstitution flows, particularly index reconstitution. Weight reconstitution appears to perform better in recent years, as figure 5 reports an increase in non-market-cap weighted products (e.g. equal weight and factor-weight ETFs). Performance for the allocation strategy is much weaker but still additive. 

Page 8 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## Conclusion 

In this short note, we examine the various explanations for why ETF contraflow strategies explain variation in stock returns. Our analysis suggest that ETF contraflow strategies are likely driven by both index and weight changes associated with periodic rebalances. Like most structural anomalies, the performance of this strategy is likely contingent on the assets tracking strategies like ETF contraflow and the size of passive instruments such as ETFs relative to the overall market. 

Page 9 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## Macro update 

Turning our attention to the bigger picture, we also take the opportunity to update our favorite top-down market indicators. 

## Our favorite market timing indicator 

Our Variance Risk Premium (VRP) indicator is a contrarian indicator that measures market overreaction and underreaction to realized risk. In simple terms, VRP is the difference between options-implied risk (i.e., the VIX index) and realized risk (i.e., the actual risk in the market, historically measured over the last month). If VRP is high, we see this as a buying opportunity for risky assets, like equities and high-yield bonds. Why? Our reasoning is as follows: when VRP is high, VIX has typically shot up dramatically (i.e., the market is in panic mode). At the same time, realized risk has probably also risen, but not to the same extent. In other words, the market has overreacted relative to what the actual realized data is telling us. Our research shows that such episodes are good buying opportunities for risky assets on about a threemonth horizon. On the other hand, when VRP is low, it tends to be a complacency indicator – investors are failing to price rising realized risk into the market, and as a result, we favor selling risky assets like equities. 

Our VRP indicator is at -1.2, less than the long-term average of 12. This reading signals slightly bearish sentiment. Generally, we pay attention to the VRP when it hits extreme levels (like +/- 2 standard deviations, or outside -10 and 34). 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0010-07.png)


**----- Start of picture text -----**<br>
Figure 11: Variance Risk Premium (VRP) Figure 12: Recent VRP (lagged) and market returns<br>3000 250 15% 100<br>280026002400 — High VRP =  Buy Risky Assets (e.g. Equities) 200150 10% ee High VRP =  Buy Risky Assets ee 80<br>22002000 — os 100 5% ee ee ee ee 60<br>1800 50 40<br>16001400 0 0% 20<br>1200 -50 0<br>1000800 -100 -5% -20<br>6004002000 Aes Low VRP = Sell Risky Assets (e.g. Equities) -150-200-250 -10%-15% ee Low VRP = Sell Risky Assets ee -40-60<br>Jan-11 Dec-11 Nov- Oct-13 Sep-14 Aug- Jul-16 Jun-17 May-<br>12 15 18<br>S&P 500 Index VRP S&P 500 Return VRP (lagged 1M)<br>Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,  Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,<br>Deutsche Bank Deutsche Bank<br>S&P 500 VRP VRP<br>S&P 500 Monthly Return<br>Jan-90 May-91 Sep-92 Jan-94 May-95 Sep-96 Jan-98 May-99 Sep-00 Jan-02 May-03 Sep-04 Jan-06 May-07 Sep-08 Jan-10 May-11 Sep-12 Jan-14 May-15 Sep-16 Jan-18<br>**----- End of picture text -----**<br>


## The opportunity set for investors 

Another metric that we watch closely is the so-called “opportunity set” for investors. Think of this as the total alpha on the table. Our main interest is to understand what is driving that opportunity, because this can allow us to position our strategies to ‘pick the juiciest fruit in the orchard.’ In Figure 6, we show the opportunity set for global equity investors, and in Figure 7, we show the same for Emerging Market equity investors. 

Page 10 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 

The Quant View 

Figure 13: Global opportunity set 

Figure 14: Emerging Markets opportunity set 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0011-05.png)


**----- Start of picture text -----**<br>
100% 100%<br>90% 90%<br>80% 80%<br>70% 70%<br>60% 60%<br>50% 50%<br>40% 40%<br>30% 30%<br>20% 20%<br>10% 10%<br>0% 0%<br>PS SH MP SH HG SS MP OS Ny NV NP sh NP NO SN Nb WD PS SH MP SH HF GS HP OS Ny NV NP sh NP NO SN Nb WD<br>FFF AH FH PH FF WH FF FF FF FV FFF HF FH PMH a FH FF FF FF FV<br>a Stock-Specific a Global a Style a Industry | Country a Currency a Stock-Specific a EM Global a Style a Industry a Country a Currency<br>Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,  Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,<br>Deutsche Bank Deutsche Bank<br>**----- End of picture text -----**<br>


_Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope, Deutsche Bank_ 

The key result is the size of the blue portion relative to the other colors. The blue area represents the opportunity explained by stock selection, whereas we can think of the other colors as representing the opportunity from top-down calls, like picking the right countries, industries and styles. When the financial crisis occurred in 2008, we moved into a much more macro-dominated world. As a result, the portion of overall opportunity that could be explained by individual company characteristics (e.g., valuation, growth profile and earnings quality, etc.) shrunk sharply. For example, few investors cared if a stock looked good on fundamentals if it was exposed to Europe. Such an environment was challenging for quants and non-quants alike, since both camps tend to use stock-specific information to differentiate between stocks. 

## The small-cap opportunity set 

In Figure 8, we show the opportunity set for the large-cap universe, and in Figure 9, we show the opportunity set for the small-cap universe. 

Figure 15: Large-cap opportunity set Figure 16: Small- cap opportunity set 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0011-11.png)


**----- Start of picture text -----**<br>
100% 100%<br>90% 90%<br>80% 80%<br>70% 70%<br>60% 60%<br>50% 50%<br>40% 40%<br>30% 30%<br>20% 20%<br>10% 10%<br>0% 0%<br>PS SH MP SH LS HH OS Ny NV NP sh NP NO SN Nb WD PS Sy MP MF SL Sb HM WO ny Nv 8 A ND NO SY NPD<br>FFB AHF PF FF FF FF FF FF VF FFF BHF FF FF FFF FF VF<br>a Stock-Specific a Style a Industry a Russell 1000 a Stock-Specific a Style a Industry a Russell 2000<br>Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,  Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,<br>Deutsche Bank Deutsche Bank<br>**----- End of picture text -----**<br>


Both charts show that bottom-up stock picking is making a strong comeback. The blue area in both charts has reached levels last seen in 2007. The crucial observation is that the relative opportunity coming from stock selection is higher for small-cap stocks. In other words, this universe is particularly fruitful for managers with skill in picking individual stocks. We note that the relative opportunity set has remained fairly steady during the past month for small caps. 

Deutsche Bank Securities Inc. 

Page 11 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## Valuation spreads 

Similar to the opportunity set, valuation spreads allow investors to gauge the level of stock selection opportunity in the market. Widening valuation spreads typically indicate more stock-level differentiation, and consequently, a better environment for stock selection. On the other hand, narrowing valuation spreads are indicative of lower levels of stock differentiation. Figure 10 and Figure 11 show the median 25th percentile and 75th percentile of trailing price to earnings for the Russell 1000 and 2000 index constituents. Interestingly, we see that valuation spreads are wider on a more consistent basis for small-cap stocks. This reinforces the earlier evidence we saw in the opportunity set – the small-cap space is rich with opportunity for skilled stock pickers. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0012-04.png)


**----- Start of picture text -----**<br>
Figure 17: Large cap valuation spreads Figure 18: Small cap valuation spreads<br>50x 50x<br>45x 45x<br>40x 40x<br>35x 35x 2 s oe 8 ,<br>a % . .<br>30x 30x<br>25x 25x<br>20x one i AL ke, i eel a | 20x - ey oh baal whe We al Teach ae *<br>15x10x willilnwt“rarer ie ml nTInv ae M/ ul Misiall helie4 sil!allrf joy9MAit- illPi diatllllaiity)PrisHy P 15x10x Mifn FNfi t wy" |!AV oljr povasNay *siilWa iWils Vtj pl) eiNU MlMePalMal\,<br>5x 5x<br>0x 0x<br>FEESPEISL SV EIDD SEKSINIDD NMP S MPE SSLLS VD H LSSWO AADN  nrISSah O SSN xBD SPSSPoSsOhWMobSSSWM" WV" SEESWR" WR" FPP SI Mw oy<br>~~ 25th Percentile Median 75th Percentile 25th Percentile Median 75th Percentile<br>Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,  Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,<br>Deutsche Bank Deutsche Bank<br>Trailing 12 Month P/E Spread<br>Trailing 12 Month P/E Spread<br>**----- End of picture text -----**<br>


## Keeping an eye on correlations 

The median pairwise correlation among stocks in the market is closely related to the opportunity set and valuation spreads. This is calculated by taking every possible pair of stocks and computing the correlation of their monthly returns based on the past 24 months of data, and then taking the median across all the pairs. Figure 12 shows the median pairwise correlation for large caps. In general, median pairwise correlations for small-cap stocks (shown in Figure 13) tend to be lower when compared with large-cap stocks. This tells us that small-cap names tend to trade more on their own merits, rather than being driven by common factors. 

Page 12 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 

The Quant View 

Figure 19: Median pairwise correlation for large caps 

Figure 20: Median pairwise correlation for small caps 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0013-05.png)


**----- Start of picture text -----**<br>
70% 70%<br>60% Median pairwise correlations tend to  60% Median pairwisecorrelations tend<br>50% be higher oo oH es 50% | to be lower pe<br>40% 40%<br>30% 30%<br>20% ie A OY eS 20% Py eccle - ee Me Bae<br>10% 10%<br>0% 0%<br>-10% -10%<br>25th Percentile Median 75th Percentile 25th Percentile Median 75th Percentile<br>Pairwise Correlation<br>Jan-91 Jan-92 Jan-93 Jan-98 Jan-99 Jan-00 Jan-06 Jan-07 Jan-13 Jan-14 Jan-90 Jan-91 Jan-92 Jan-93 Jan-94 Jan-95 Jan-96 Jan-97 Jan-98 Jan-99 Jan-00 Jan-01 Jan-02 Jan-03 Jan-04 Jan-05 Jan-06 Jan-07 Jan-08 Jan-09 Jan-10 Jan-11 Jan-12 Jan-13 Jan-14 Jan-15 Jan-16 Jan-17 Jan-18 Jan-19<br>Pairwise Correlation<br>Jan-90 Jan-94 Jan-95 Jan-96 Jan-97 Jan-01 Jan-02 Jan-03 Jan-04 Jan-05 Jan-08 Jan-09 Jan-10 Jan-11 Jan-12 Jan-15 Jan-16 Jan-17 Jan-18 Jan-19<br>**----- End of picture text -----**<br>


_Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope, Deutsche Bank_ 

_Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope, Deutsche Bank_ 

Page 13 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## The DB Quant Dashboard 

## Which styles have been working around the world? 

The DB Quant Dashboard is an easy-to-use ‘cheat sheet’ that shows which styles have been working in key markets around the world. We track cumulative factor performance year-to-date. For those who prefer the previous tabular format (which includes more factors), those results can be found in Appendix A. 

## For more details see our website 

For the most recent weekly factor performance, as well as factor performance delineated by different universes (e.g., large cap, small cap) and regions, please contact us at DBEQS.Americas@db.com  to be added to our Weekly Dashboard distribution list. 

Deutsche Bank Securities Inc. 

Page 14 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## Figure 21: Global YTD cumulative factor performance (Q10-Q1 return spread) 

_Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope, Deutsche Bank_ 

Deutsche Bank Securities Inc. 

Page 15 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## Bottom-up stock selection 

## N-LASR global stock selection model 

- n The N-LASR model is our flagship stock selection model for global equities. 

- n The model is based on a machine learning algorithm called AdaBoost, and is designed to adaptively learn which factors to use, often in a non-linear way. 

- n For complete details on the model, please see Wang et al, Signal Processing: The Rise of the Machines, 5 June 2012. 

## Current stock recommendations 

Figure below shows the best 20 Buy and sell ideas from today's model. We note that a complete ranking for all global stocks is available in a spreadsheet format. If you would like to get a copy of the spreadsheet, please contact us at DBEQS.Americas@db.com 

~~es~~ Figure 22: Current N-LASR model stock recommendations 

||**BEST BUY IDEAS**|**BEST BUY IDEAS**||||||**BEST SELL IDEAS**|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||**N-LASR Score**|||||||**N-LASR Score**|
||**Ticker**|**Name**|**SEDOL**|**Country**|**(higher is better long)**|||**Ticker**|**Name**|**SEDOL**|**Country**|**(lower is better short)**|
||ABBV|ABBVIE INC|B92SR70|USA|2.33|||TRXC|TRANSENTERIX INC|BLBP5R2|USA|-2.30|
||DPZ|DOMINO'S PIZZA INC|B01SD70|USA|2.16|||IWCB MK|Iskandar Waterfront City Berhad|638135|Malaysia|-2.24|
||9843 JT|Nitori Holdings Co|664480|Japan|2.07|||IRDM|IRIDIUM COMMUNICATIONS INC|B2QH310|USA|-2.23|
||GUD AU|GUD Hldgs Ltd|635800|Australia|2.01|||JKBK IB|Jammu & Kashmir Bank Ltd|BQQF4T|India|-2.13|
||ILMN|ILLUMINA INC|2613990|USA|1.93|||POWF IB|Power Finance Corp Ltd|B1S722|India|-2.11|
||6869 JT|Sysmex Corp|688380|Japan|1.86|||197210 KS|LEED Corp|BR1714|Korea|-2.06|
||PAYX|PAYCHEX INC|2674458|USA|1.86|||735 HK|China Power Clean Energy Developmen BDT7WY||China|-2.06|
||WSU GY|Washtec AG|535543|Germany|1.85|||ALBK IB|Allahabad Bank|670828|India|-2.06|
||TLKM IJ|Telekomunikasi Indonesia Tbk PT|BD4T6W|Indonesia|1.84|||3753 JT|Flight Holdings Inc|B031SF|Japan|-2.06|
||NTAP|NETAPP INC|2630643|USA|1.83|||2395 JT|Shin Nippon Biomedical Laboratories|673890|Japan|-2.04|
||BH TB|Bumrungrad Hospital PCL|B0166D|Thailand|1.83|||CRPBK IB|Corp Bank|BVFYBZ|India|-2.01|
||CLX|CLOROX CO/DE|2204026|USA|1.83|||020560 KS|Asiana Airlines|620020|Korea|-2.01|
||ZTS|ZOETIS INC|B95WG16|USA|1.81|||1076 HK|Imperial Pacific International Holdings|BYM8MQ|China|-1.98|
||JNJ|JOHNSON & JOHNSON|2475833|USA|1.80|||168330 KS|Naturalendo Tech Co Ltd|BG48DT|Korea|-1.97|
||T.|TELUS CORP|2381093|Canada|1.79|||UT IB|Unitech Ltd|B17MRV|India|-1.96|
||AMGN|AMGEN INC|2023607|USA|1.78|||3049 TT|HannStar Touch Solution Incorporated|654504|Taiwan|-1.96|
||KINDSDB SS|Kindred Group|BYSY2K|Sweden|1.77|||1068 HK|China Yurun Food Group Ltd.|B0D01C|China|-1.95|
||080160 KS|Modetour Network|B0FBSF|Korea|1.77|||YNHB MK|YNH Property Bhd|671236|Malaysia|-1.91|
||MMM|3M CO|2595708|USA|1.76|||BOI IB|Bank of India|609978|India|-1.91|
||LLY|LILLY(ELI)& CO|2516152|USA|1.76|||5227 TT|Advanced Lithium Electrochemistry (Ca|BGH182|Taiwan|-1.90|
|_Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope, Deutsche Bank_<br>_The recommendations in the table above may or may not reflect those of DB's fundamental analysts, given the different criteria used in evaluating the stocks._<br>~~ee~~|||||||||||||



## Model performance 

Figures below show the average pure signal performance, measured as a monthly rank information coefficient (IC) in different regions and the performance of a global model portfolio after costs, based on a realistically-optimized, market-neutral strategy. 

_Past performance is no guarantee of future results. Transaction costs can vary. Additional information is available upon request._ 

Page 16 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

Figure 23: Regional model performance, average rank IC 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0017-03.png)


**----- Start of picture text -----**<br>
14.0<br>12.0<br>10.0<br>8.0<br>6.0<br>4.0<br>2.0<br>0.0<br>-2.0<br>-4.0<br>iT fuuut<br>US EU ex Asia ex Japan EM Canada UK Aus/NZ Global<br>UK Japan<br>a Long-Term Average Rank IC a 12M Average Rank IC<br>Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,<br>Deutsche Bank<br>Average Rank IC (%)<br>**----- End of picture text -----**<br>


Figure 24: Global portfolio active return, after costs 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0017-05.png)


**----- Start of picture text -----**<br>
8.0<br>6.0<br>4.0<br>2.0<br>0.0<br>(2.0)<br>(4.0)<br>(6.0)<br>DS PP Sy PB YP NSN GD Sy<br>FF KF KF KF KK<br>Lt Active Return _ 12M Avg<br>Active Return<br>**----- End of picture text -----**<br>


_Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope, Deutsche Bank_ 

Figures below show the cumulative performance of the optimized strategy, and the annualized Sharpe Ratio (after costs) by calendar year. 

Figure 25: Global portfolio cumulative, after costs 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0017-09.png)


**----- Start of picture text -----**<br>
3000<br>2500<br>2000<br>1500<br>1000<br>500<br>0<br>SSCiaSx\ iaSPo) F&Fa Ss SS YFa<o) SFe) KK S<\ YP2) KK HY\ MKKY> KgKYI SN4)<br>Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,<br>Deutsche Bank<br>**----- End of picture text -----**<br>


Figure 26: Annualized Sharpe Ratio, after costs 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0017-11.png)


**----- Start of picture text -----**<br>
20.0<br>18.0<br>16.0<br>14.0<br>12.0<br>10.0<br>8.0<br>6.0<br>4.0<br>2.0<br>0.0<br>Sharpe Ratio<br>**----- End of picture text -----**<br>


_Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope, Deutsche Bank_ 

Deutsche Bank Securities Inc. 

Page 17 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## Top-down country rotation 

## CCRM country rotation model 

- n Our Composite Country Rotation Model (CCRM) uses three sets of inputs to dynamically rotate between countries in the MSCI All Country World Index. 

- n The inputs include top-down macro signals (e.g., VRP, Kelly’s Tail Risk), aggregate bottom-up fundamental signals (e.g., country-level valuation and momentum) and lead-lag signals, based on economic trade linkages. 

- n For complete details on the model, please see Luo et al, Signal Processing: New Insights in Country Rotation, 9 February 2012. 

## Current recommendations 

Figures below show the top and bottom third of countries, as ranked currently by our CCRM model. The bars show what is driving these calls. 

Figure 27: Top tercile countries 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0018-10.png)


**----- Start of picture text -----**<br>
6.0<br>5.0<br>4.0<br>3.0<br>2.0<br>1.0<br>0.0<br>(1.0)<br>(2.0)<br>(3.0)<br>PSFB SS ACRN a FE@ SELESo os Sw SHGyo<br>SF EFF BFF HOP PHF FPO SF SK<br>. Wt OE LS S < &<br>a 8 x<br>. Kelly . VRP . MCRM . Momentum . Valuation 1. Sentiment e CCRM<br>**----- End of picture text -----**<br>


Figure 28: Bottom tercile countries 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0018-12.png)


**----- Start of picture text -----**<br>
3.0<br>2.0<br>1.0<br>0.0<br>(1.0)<br>(2.0)<br>(3.0)<br>(4.0)<br>FF> .® x Sf> FC> SF\ €—SH #¥WwW FSFGG CF~@ SHSNV 6 2<br>OP LF FH KM KM SK NM s ARCOM)<br>Ce SN Se wT ye” &<br>S Ss<br>. Kelly 1. VRP . MCRM . Momentum . Valuation 1. Sentiment e CCRM<br>**----- End of picture text -----**<br>


_Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope, Deutsche Bank_ 

_Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope, Deutsche Bank_ 

Page 18 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 9 May 2019 The Quant View 

## Model performance 

Figures below show the performance of the model over time. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0019-03.png)


**----- Start of picture text -----**<br>
a Figure 29: Long/Short portfolio return (%) Figure 30: Model performance with rank IC<br>Composite CRM, equally w eighted six-factor model Composite CRM, equally w eighted six-factor model<br>10 80<br>5<br>40<br>0<br>0<br>-5<br>-10 Avg = 0.66%  -40 Avg = 5.48%<br>Std. Dev. = 3.12%  Std. Dev. = 27.86%<br>Min = -10.18%  Min = -62%<br>-15 Avg/Std. Dev.= 0.21 -80 Avg/Std. Dev.= 0.2<br>notin 2004 2006 2008 2010 2012 2014 2016 2018 uasanadiad 2004 2006 2008 2010 2012 2014 2016 2018<br>Long/short quantile portfolio return (%), Ascending order Spearman rank IC (%), Ascending order<br>12-month moving average 12-month moving average<br>Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,  Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,<br>Deutsche Bank Deutsche Bank<br>es<br>(%) (%)<br>**----- End of picture text -----**<br>


Page 19 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## Top-down asset allocation 

## Quant Tactical Asset Allocation (QTAA) model 

- n Our Quantitative Tactical Asset Allocation (QTAA) model uses a model-ofmodels methodology to rotate between six asset classes. 

- n The model uses a wide range of fundamental and market-based factors as inputs, and dynamically selects a subset of those factors to use at each point in time. 

- n For complete details on the model, please see Luo et al, Signal Processing: Quant Tactical Asset Allocation, 19 September 2011. 

## Current recommendations and performance 

Figures below show the current ranking of our six asset classes, ranked from best to worst in terms of month-ahead forecast returns and the monthly performance of the QTAA model over time. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0020-09.png)


**----- Start of picture text -----**<br>
es Figure 31: Current QTAA forecasts Figure 32: Performance of QTAA model<br>Cross sectional IC (%)<br>Crude Oil<br>100<br>Equity (S&P 500)<br>50<br>High Yield (DB USD High Yield)<br>Bond (DB USD Agg. Bond) 0<br>Commodities (S&P GSCI) -50 Avg = 6.48%<br>Std. Dev. = 54.81%<br>Gold Min = -95.82%<br>-100 Avg/Std. Dev.= 0.12<br>0.0 = 0.1 0.2 0.3 0.4 0.5 0.6 0.7 ldtudatal 2006 2008 2010 2012 2014 2016 2018<br>Forecast Return (%) QTAA 12-month moving average<br>Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,  Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,<br>Deutsche Bank Deutsche Bank<br>a<br>(%)<br>**----- End of picture text -----**<br>


Page 20 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## Top-down style rotation 

## Style rotation model 

- n Our Style Rotation model dynamically rotates between 12 “typical” quant factors. 

- n The model uses market-based and macroeconomic inputs to predict month-ahead factor returns using a backward stepwise linear regression model. 

- n For complete details on the model, please see Luo et al, Signal Processing: Style Rotation, 7 September 2010. 

## Current recommendations and performance 

Figures below show the current ranking of our 12 factors, ranked from best to worst in terms of month-ahead forecast performance and the monthly performance of the Style Rotation model over time. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/Why_Do_ETF_Flows_Move_Prices_images/Why_Do_ETF_Flows_Move_Prices.pdf-0021-09.png)


**----- Start of picture text -----**<br>
a Figure 33: Current Style Rotation forecasts Figure 34: Performance of style rotation model<br>Linear regression model<br>12M-1M Momentum [Ascending]<br>3M EPS Revision [Ascending] 100<br>Size [Ascending]<br>IBES 5Y EPS growth [Ascending] 50<br>HLOOKUP(I5,$B$1:$M$3,2,FALSE)<br>Price to Book [Descending] 0<br>Accruals  [Descending]<br>Net Ext. Financing/NOA [Descending] -50 Avg = 13.13%<br>Sales to Total Assets [Ascending] Std. Dev. = 43.24%<br>Long-Term Debt/Equity [Ascending]CAPM Idio. Vol  [Descending] -100 Min = -89.51% Avg/Std. Dev.= 0.3<br>00 02 04 06 08 10 12 14 16 18<br>Lottery Factor [Descending]<br>2<br>aaa<br>(10.0) (5.0) 0.0 5.0 10.0 15.0 Style IC 12-month moving average<br>Forecast IC (%)<br>Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,  Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope,<br>Deutsche Bank Deutsche Bank<br>|<br>(%)<br>**----- End of picture text -----**<br>


Page 21 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

~~ee~~ Figure 35: US factor performance, measured as rank IC (Russell 3000 universe) 

## Appendix A: Factor performance 

|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~a0~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**1. Value**||||||||||||||||
|1 Dividend yield, trailing 12M|Ascending|2,949|5.07|3.47|1.48|2.81|13.87|0.20|42.59|(33.26)|0.00|376|2,892|55.05|98.15|
|2 Expected dividend yield|Ascending|2,949|5.57|3.56|1.63|3.04|14.35|0.21|44.46|(33.89)|0.00|376|2,892|54.52|98.85|
|3 Price-to-operating EPS, trailing 12M, Basic|Descending|2,119|14.37|(3.55)|(0.58)|2.21|10.45|0.21|30.82|(32.28)|0.00|300|2,321|56.00|93.56|
|4 Operating earnings yield, trailing 12M, Basic|Ascending|2,917|20.63|2.22|2.71|4.53|12.38|0.37|47.24|(33.30)|0.00|300|2,887|62.33|95.30|
|5 Earnings yield, forecast FY1 mean|Ascending|2,790|23.75|0.88|2.43|4.27|11.96|0.36|48.88|(34.61)|0.00|376|2,578|62.77|94.66|
|6 Earnings yield, forecast FY2 mean|Ascending|2,774|24.43|(0.82)|1.99|3.68|11.66|0.32|47.02|(34.31)|0.00|376|2,494|62.77|94.29|
|7 Earnings yield x IBES 5Y growth|Ascending|1,079|12.76|(4.51)|0.13|1.44|10.21|0.14|41.11|(26.63)|0.02|300|1,813|58.33|93.21|
|8 Sector-rel Operating earnings yield, trailing 12M, Basic|Ascending|2,916|5.62|3.47|2.74|4.16|8.06|0.52|28.96|(14.90)|0.00|300|2,884|69.00|94.95|
|9 Hist-rel Operating earnings yield, trailing 12M, Basic|Ascending|2,322|5.53|0.51|0.82|1.38|6.23|0.22|20.73|(18.74)|0.00|206|2,124|60.19|95.89|
|10 Operating cash flow yield (income stmt def)|Ascending|2,949|17.55|(0.16)|1.02|3.70|10.73|0.35|47.14|(32.67)|0.00|376|2,892|62.50|94.78|
|11 Cash flow yield, FY1 mean|Ascending|1,737|10.98|(4.59)|(2.49)|1.98|16.78|0.12|66.06|(54.29)|0.03|346|945|54.91|94.54|
|12 Free cash flow yield|Ascending|2,860|16.73|1.64|2.08|4.62|7.85|0.59|31.93|(22.64)|0.00|339|2,580|73.45|94.44|
|13 Price-to-sales, trailing 12M|Descending|2,830|8.11|(3.36)|(1.76)|1.29|10.93|0.12|30.02|(41.46)|0.02|376|2,813|55.05|98.56|
|14 Price-to-book|Descending|2,794|6.44|(4.15)|(1.88)|0.46|10.85|0.04|26.28|(35.75)|0.41|376|2,776|47.61|95.73|
|15 EBITDA/EV|Ascending|2,912|15.25|(0.11)|0.89|3.76|9.74|0.39|39.32|(27.15)|0.00|376|2,842|64.10|91.21|
|16 Price-to-book adj for ROE, sector adj|Descending|2,645|2.86|(3.63)|(2.22)|0.20|8.65|0.02|22.50|(33.21)|0.66|376|2,467|47.87|95.76|
|**2. Growth**||||||||||||||||
|17 Hist 5Y operating EPS growth|Descending|2,820|13.41|2.76|1.69|1.38|8.35|0.17|30.58|(22.70)|0.01|288|2,760|56.25|95.36|
|18 Hist 5Y operating EPS acceleration|Ascending|2,820|(0.03)|(0.77)|0.64|0.85|6.25|0.14|25.31|(16.13)|0.02|288|2,760|55.90|93.09|
|19 IBES 5Y EPS growth|Ascending|2,240|15.57|2.91|2.43|1.17|7.82|0.15|21.65|(27.86)|0.00|376|2,299|56.65|98.08|
|20 IBES 5Y EPS growth/stability|Ascending|2,240|18.08|3.88|3.30|1.67|7.64|0.22|20.64|(19.20)|0.00|376|2,298|59.04|98.37|
|21 IBES LTG EPS mean|Descending|1,318|(3.43)|(0.05)|(1.73)|1.34|14.77|0.09|37.64|(52.38)|0.08|376|2,074|48.67|97.03|
|22 IBES FY2 mean DPS growth|Ascending|2,204|8.75|1.78|1.59|1.42|8.39|0.17|24.12|(21.96)|0.02|203|1,715|53.69|84.08|
|23 IBES FY1 mean EPS growth|Ascending|2,754|6.43|(1.20)|1.46|1.13|7.17|0.16|20.76|(24.42)|0.00|376|2,549|61.44|88.82|
|24 Year-over-year quarterly EPS growth|Ascending|2,920|5.52|(0.41)|0.76|2.37|6.67|0.36|23.85|(21.12)|0.00|300|2,895|65.00|79.06|
|25 IBES FY1 mean CFPS growth|Descending|1,638|(6.87)|(0.32)|(1.48)|0.12|10.23|0.01|38.08|(42.07)|0.84|303|742|49.83|92.20|
|26 IBES SUE, amortized|Ascending|2,611|(1.14)|1.46|2.10|1.08|6.15|0.17|20.62|(16.30)|0.00|315|1,416|56.83|73.22|
|**3. Price Momentum and Reversal**||||||||||||||||
|27 Total return, 1D|Descending|2,949|1.73|(0.35)|1.35|4.56|7.14|0.64|16.33|(33.75)|0.00|376|2,892|76.06|1.88|
|28 Total return, 21D (1M)|Descending|2,948|9.94|2.90|1.73|1.81|10.60|0.17|29.03|(43.69)|0.00|376|2,891|56.12|1.03|
|29 Maximum daily return in last 1M (lottery factor)|Descending|2,940|12.83|5.42|3.99|5.08|14.54|0.35|39.13|(56.07)|0.00|376|2,786|64.10|50.27|
|30 21D volatility of volume/price|Descending|2,949|6.28|2.66|1.03|0.47|6.54|0.07|24.16|(21.49)|0.17|376|2,883|52.13|52.25|
|31 Total return, 252D (12M)|Ascending|2,845|(8.09)|(0.66)|0.23|2.85|14.00|0.20|39.62|(57.00)|0.00|376|2,803|61.97|89.70|
|32 12M-1M total return|Ascending|2,845|(6.14)|(0.11)|0.61|3.61|13.14|0.27|37.65|(49.06)|0.00|376|2,803|62.50|88.30|
|33 Price-to-52 week high|Ascending|2,901|1.52|3.25|2.66|3.18|17.42|0.18|49.63|(62.50)|0.00|376|2,112|61.17|84.57|
|34 Total return, 1260D (60M)|Ascending|2,340|11.35|3.88|3.29|1.47|10.98|0.13|25.63|(35.41)|0.01|364|2,255|57.42|97.26|
|**4. Sentiment**||||||||||||||||
|35 IBES LTG Mean EPS Revision, 3M|Ascending|1,301|0.24|(0.27)|(0.26)|0.75|3.82|0.20|11.16|(12.06)|0.00|376|2,046|60.64|59.05|
|36 IBES FY1 Mean EPS Revision, 3M|Ascending|2,750|2.41|(0.28)|0.85|2.64|8.16|0.32|29.96|(33.00)|0.00|376|2,520|65.16|71.67|
|37 IBES FY1 EPS up/down ratio, 3M|Ascending|2,717|(1.59)|0.41|1.14|2.80|7.61|0.37|27.54|(24.41)|0.00|376|2,398|67.02|78.93|
|38 Expectation gap, short-term - long-term|Descending|2,127|5.59|3.63|1.59|1.24|5.37|0.23|11.80|(19.91)|0.00|376|2,128|58.24|91.11|
|39 IBES FY1 Mean CFPS Revision, 3M|Ascending|1,689|6.94|0.91|1.38|1.97|14.55|0.14|69.38|(75.04)|0.01|345|878|63.19|61.46|
|40 IBES FY1 Mean SAL Revision, 3M|Ascending|2,705|0.49|(1.48)|1.34|1.27|7.72|0.16|27.43|(24.32)|0.01|275|2,296|61.45|67.82|
|41 IBES FY1 Mean FFO Revision, 3M|Ascending|174|6.48|2.18|1.79|2.51|19.38|0.13|71.43|(80.00)|0.02|348|100|56.90|68.00|
|42 IBES FY1 Mean DPS Revision, 3M|Ascending|1,326|3.24|(0.28)|0.66|0.72|5.12|0.14|14.91|(17.55)|0.05|200|1,109|59.00|63.83|
|43 IBES FY1 Mean ROE Revision, 3M|Ascending|2,099|2.51|0.64|1.20|1.00|6.15|0.16|23.70|(22.19)|0.02|200|1,869|60.00|60.33|
|44 Recommendation, mean|Descending|2,791|2.28|(0.78)|0.78|0.70|7.46|0.09|21.85|(19.41)|0.10|305|2,696|57.38|94.90|
|45 Mean recommendation revision, 3M|Descending|2,781|(1.99)|0.22|0.39|0.99|3.86|0.26|19.86|(11.55)|0.00|302|2,682|61.59|60.82|
|46 Target price implied return|Descending|2,771|1.83|3.99|1.49|0.44|16.04|0.03|60.74|(39.59)|0.67|241|2,537|48.96|81.22|
|47 Mean target price revision, 3M|Ascending|2,760|(1.60)|1.40|1.36|2.15|12.37|0.17|30.14|(41.94)|0.01|238|2,524|60.92|74.70|
|**5. Quality**||||||||||||||||
|48 ROE, trailing 12M|Ascending|2,774|18.84|4.55|3.20|3.83|10.04|0.38|33.42|(29.52)|0.00|300|2,852|65.33|93.78|
|49 Return on invested capital (ROIC)|Ascending|2,901|16.94|4.16|3.43|4.12|10.20|0.40|33.02|(31.24)|0.00|300|2,871|68.67|95.62|
|50 Sales to total assets (asset turnover)|Ascending|2,828|0.06|2.02|0.86|1.39|8.47|0.16|22.78|(22.02)|0.00|376|2,825|55.59|99.20|
|51 Operating profit margin|Ascending|2,825|7.44|3.25|3.53|1.41|5.62|0.25|16.98|(14.17)|0.00|376|2,747|60.90|97.85|
|52 Current ratio|Descending|2,213|8.80|1.76|0.19|1.67|10.09|0.17|31.95|(38.66)|0.00|376|2,244|54.52|97.54|
|53 Long-term debt/equity|Ascending|2,776|6.44|1.56|(0.52)|0.71|9.29|0.08|35.65|(28.14)|0.14|376|2,760|49.73|96.82|
|54 Altman's z-score|Ascending|2,084|4.72|4.60|3.59|0.76|9.18|0.08|31.74|(30.44)|0.11|376|2,159|51.86|97.61|
|55 Merton's distance to default|Ascending|2,374|4.30|7.07|4.62|3.61|12.23|0.30|35.09|(41.45)|0.00|376|2,351|66.22|94.43|
|56 Ohlson default model|Descending|2,181|7.40|3.65|2.94|2.38|6.57|0.36|16.95|(25.59)|0.00|339|2,140|67.85|98.08|
|57 Accruals (Sloan 1996 def)|Descending|2,133|1.61|(0.85)|(0.83)|0.25|4.22|0.06|12.07|(15.48)|0.25|376|2,141|53.46|87.95|
|58 Firm-specific discretionary accruals|Descending|993|1.45|(0.89)|(0.96)|0.16|3.70|0.04|10.45|(12.89)|0.44|316|1,925|53.80|65.00|
|59 Hist 5Y operating EPS stability, coef of determination|Ascending|2,820|10.57|0.81|0.99|0.93|4.93|0.19|20.01|(12.27)|0.00|288|2,760|52.43|97.11|
|60 IBES 5Y EPS stability|Descending|2,240|12.98|3.34|2.61|1.40|8.27|0.17|25.00|(34.33)|0.00|376|2,299|55.59|98.89|
|61 IBES FY1 EPS dispersion|Descending|2,790|9.32|7.32|4.53|2.03|9.46|0.22|31.67|(28.25)|0.00|376|2,578|60.90|83.00|
|62 Payout on trailing operating EPS|Ascending|2,119|(9.67)|2.72|(0.25)|0.72|12.94|0.06|38.55|(30.91)|0.28|376|2,203|49.20|97.07|
|63 YoY change in # of shares outstanding|Descending|2,902|14.39|4.39|2.16|2.60|8.85|0.29|19.53|(46.21)|0.00|376|2,789|60.11|92.09|
|64 YoY change in debt outstanding|Descending|2,345|(4.49)|(1.86)|(1.67)|0.01|4.06|0.00|13.07|(10.40)|0.95|376|2,230|52.93|89.44|
|65 Net external financing/net operating assets|Ascending|2,935|12.45|2.45|0.80|2.29|8.41|0.27|44.61|(21.76)|0.00|376|2,858|60.64|94.61|
|66 Piotroski's F-score|Ascending|2,949|10.00|0.83|1.42|2.81|8.02|0.35|29.20|(27.83)|0.00|376|2,894|67.29|88.79|
|67 Mohanram's G-score|Ascending|550|(5.89)|3.48|2.85|2.57|9.82|0.26|35.27|(32.14)|0.00|288|422|58.33|95.56|
|**6. Technicals**||||||||||||||||
|68 # of days to cover short|Descending|315|7.72|3.02|2.45|2.25|7.29|0.31|33.80|(25.16)|0.00|376|2,026|59.84|91.99|
|69 CAPM beta, 5Y monthly|Descending|4,032|(0.22)|0.77|0.81|0.98|12.70|0.08|40.19|(42.70)|0.17|317|3,075|50.79|96.29|
|70 CAPM idosyncratic vol, 1Y daily|Descending|3,062|14.16|7.32|4.78|5.28|17.55|0.30|42.60|(60.80)|0.00|364|2,912|62.09|98.76|
|71 Realized vol, 1Y daily|Descending|2,899|11.55|6.77|4.49|5.12|18.25|0.28|42.69|(59.63)|0.00|376|2,807|61.17|98.59|
|72 Skewness, 1Y daily|Descending|2,899|4.95|2.28|1.06|1.15|5.37|0.21|13.93|(22.86)|0.00|376|2,807|56.38|89.89|
|73 Kurtosis, 1Y daily|Descending|2,899|(1.17)|(0.70)|(0.21)|1.31|5.58|0.24|15.28|(15.82)|0.00|376|2,807|60.90|91.54|
|74 Idiosyncratic vol surprise|Descending|2,919|(7.98)|(0.69)|(0.41)|2.47|7.60|0.32|22.66|(33.71)|0.00|363|2,866|63.64|87.79|
|75 Normalized abnormal volume|Ascending|2,949|6.03|3.92|1.61|2.22|6.38|0.35|23.10|(16.38)|0.00|376|2,885|64.89|64.58|
|76 Float turnover, 12M|Descending|3,186|6.65|1.69|1.66|0.59|11.03|0.05|29.93|(31.61)|0.31|365|2,846|49.32|99.24|
|77 Moving average crossover, 15W-36W|Ascending|2,888|2.47|2.62|1.69|2.14|13.05|0.16|46.29|(55.07)|0.00|376|2,593|59.57|91.08|
|78 Log float-adj capitalization|Ascending|2,949|1.54|4.08|1.09|3.15|11.00|0.29|29.53|(40.68)|0.00|376|2,888|61.17|99.47|
|79 # of month in the database|Ascending|2,949|4.28|2.18|0.68|2.09|8.52|0.25|35.61|(23.86)|0.00|376|2,892|56.38|99.99|
|80 DB composite options factor|Ascending|1,701|0.95|(0.03)|0.55|1.03|3.65|0.28|13.99|(13.88)|0.00|213|1,917|63.38|26.39|



**Note:** 

1 Direction indicates how the factor scores are sorted. Ascending order means higher factors scores are likely to be associated with higher subsequent stock returns, and vice versa for descending order. 

2 P-value indicates the statistical significance of the factor's performance. A smaller p-value suggests that is it more likely the factor's performance is different from zero. 

3 This is the autocorrelation of the factor scores over time. Higher serial correlation indicates lower portfolio turnover based on the factor. 

_Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope, Deutsche Bank_ 

Page 22 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 9 May 2019 The Quant View ~~ee~~ Figure 36: Global factor performance, measured as rank IC (S&P BMI World universe) ~~2~~ 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|**Since Inception**<br>**Current**<br>**Average IC(%)**<br>**Avg /**<br>**# of**<br>**Avg # of**<br>**Hit**<br>**Serial**<br>**Factor Name**<br>**Direction1**<br>**# of Stocks**<br>**Last M**<br>**12M Avg**<br>**3Y Avg**<br>**Avg**<br>**Std Dev**<br>**Std Dev**<br>**Max**<br>**Min**<br>**p-value2**<br>**Months**<br>**Stocks**<br>**Rate (%)**<br>**Corr (%)3**<br>~~SS]~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**1. Value**||||||||||||||||
|1 Dividend yield, trailing 12M|Ascending|10,928|5.06|4.99|4.30|4.17|9.93|0.42|36.88|(23.89)|0.00|352|8,558|65.06|97.85|
|2 Dividend yield, FY1|Ascending|8,332|3.89|3.03|2.39|3.83|10.20|0.38|32.17|(22.90)|0.00|295|5,941|63.05|98.26|
|3 Dividend yield, FY2|Ascending|8,237|4.02|2.74|2.35|3.67|10.29|0.36|33.19|(24.39)|0.00|285|5,921|62.81|98.27|
|4 Price/Earnings|Descending|9,088|2.81|(0.80)|1.24|3.36|12.24|0.27|39.66|(50.73)|0.00|345|6,813|59.42|96.38|
|5 Price-to-FY0 EPS|Descending|8,728|6.98|(1.37)|0.26|2.26|9.96|0.23|28.98|(37.08)|0.00|352|6,488|59.09|96.55|
|6 Earnings yield, FY0|Ascending|9,945|9.08|1.13|2.17|3.58|8.76|0.41|31.67|(18.68)|0.00|352|7,515|62.50|96.48|
|7 Earnings yield, forecast FY1 mean|Ascending|9,027|10.81|(0.45)|1.97|4.14|10.39|0.40|35.35|(22.20)|0.00|352|6,943|62.78|95.81|
|8 Earnings yield, forecast FY2 mean|Ascending|8,918|10.81|(1.91)|1.39|3.66|11.36|0.32|37.31|(31.50)|0.00|352|6,781|60.23|95.96|
|9 Cash flow yield, FY0|Ascending|7,161|4.42|(1.22)|0.03|2.92|6.70|0.44|26.42|(12.09)|0.00|228|5,598|67.98|97.41|
|10 Cash flow yield, FY1 mean|Ascending|6,297|4.78|(2.83)|(0.53)|1.34|9.49|0.14|31.42|(32.01)|0.02|284|4,946|54.23|96.03|
|11 Price/Sales|Descending|10,445|4.15|(3.16)|0.43|1.25|9.09|0.14|26.48|(31.59)|0.01|352|8,031|55.40|99.27|
|12 Price/Book|Descending|10,537|(0.88)|(2.05)|(0.14)|0.82|10.19|0.08|31.56|(37.54)|0.13|352|8,087|54.55|98.46|
|13 Est Book-to-price, median|Ascending|7,833|1.64|(2.97)|(0.85)|0.42|9.66|0.04|30.37|(26.29)|0.50|236|6,109|51.69|98.30|
|14 EBITDA to EV|Ascending|3,158|13.84|(0.62)|1.22|3.78|10.62|0.36|36.69|(26.20)|0.00|352|4,978|62.50|95.67|
|15 Sales/EV|Ascending|10,274|4.11|(3.10)|0.90|1.80|7.47|0.24|24.81|(20.06)|0.00|352|7,979|61.65|99.05|
|**2. Growth**||||||||||||||||
|16 IBES 5Y EPS growth|Ascending|8,915|5.53|1.71|1.80|1.25|5.81|0.22|19.09|(21.86)|0.00|352|6,698|60.80|98.03|
|17 EPS Growth|Ascending|9,797|2.85|0.79|0.89|1.98|6.33|0.31|29.72|(28.97)|0.00|336|7,444|64.88|87.88|
|18 IBES LTG EPS mean|Descending|3,849|(1.65)|1.03|(0.65)|1.07|11.15|0.10|28.22|(40.36)|0.07|352|4,275|50.85|96.50|
|19 IBES FY1 mean EPS growth|Ascending|8,771|0.92|(1.18)|0.02|0.33|5.77|0.06|14.44|(20.10)|0.29|352|6,780|53.98|88.67|
|20 IBES FY1 mean CFPS growth|Descending|5,213|(0.78)|0.73|0.35|1.42|3.97|0.36|7.47|(11.39)|0.00|228|4,335|61.84|91.68|
|21 IBES FY2 mean DPS growth|Ascending|8,226|2.74|(0.99)|0.71|2.01|10.07|0.20|38.85|(31.49)|0.00|294|5,803|58.50|88.42|
|22 Asset growth|Descending|10,413|1.49|0.08|0.12|0.58|7.86|0.07|21.57|(27.36)|0.17|352|7,849|51.99|93.70|
|**3. Price Momentum and Reversal**||||||||||||||||
|23 Total return, 1D|Descending|10,947|(0.59)|1.82|1.65|3.35|6.99|0.48|21.94|(41.58)|0.00|352|8,654|70.45|1.95|
|24 Weekly Total Return|Descending|10,946|(2.51)|2.89|2.57|2.71|8.31|0.33|30.60|(33.64)|0.00|352|8,653|63.64|1.47|
|25 Total return, 21D (1M)|Ascending|10,943|(9.55)|(3.03)|(2.21)|0.02|10.78|0.00|27.69|(44.07)|0.97|352|8,648|51.99|3.89|
|26 Total return, 252D (12M)|Ascending|10,704|(5.81)|(0.30)|1.47|4.02|13.74|0.29|41.64|(46.50)|0.00|352|8,434|66.19|90.62|
|27 12M-1M total return|Ascending|10,704|(2.65)|0.81|2.27|4.59|13.22|0.35|40.96|(42.52)|0.00|352|8,434|67.61|88.94|
|28 Total return, 1260D (60M)|Ascending|9,204|(1.57)|0.81|1.10|1.55|13.20|0.12|40.32|(44.84)|0.03|352|6,944|58.81|97.72|
|**4. Sentiment**||||||||||||||||
|29 IBES LTG Mean EPS Revision, 1M|Ascending|3,838|(2.25)|(0.18)|(0.10)|0.61|2.57|0.24|7.26|(8.59)|0.00|352|4,240|61.36|1.33|
|30 IBES LTG Mean EPS Revision, 3M|Ascending|3,820|(2.84)|0.90|0.46|0.80|3.33|0.24|11.05|(10.26)|0.00|352|4,187|61.36|60.76|
|31 IBES FY1 EPS up/down ratio, 1M|Ascending|6,188|(2.46)|0.51|1.39|3.38|5.33|0.63|17.76|(13.76)|0.00|352|4,626|74.43|34.22|
|32 IBES FY1 EPS up/down ratio, 3M|Ascending|7,900|(2.86)|1.13|1.70|3.43|5.63|0.61|17.92|(12.36)|0.00|352|6,248|73.86|78.22|
|33 IBES FY1 Mean EPS Revision, 1M|Ascending|8,891|(1.77)|0.78|1.21|2.64|4.95|0.53|16.50|(12.79)|0.00|352|6,792|71.02|23.24|
|34 IBES FY1 Mean EPS Revision, 3M|Ascending|8,822|(1.47)|0.94|1.61|3.18|6.38|0.50|19.37|(20.12)|0.00|352|6,695|72.16|73.78|
|35 IBES FY1 Mean CFPS Revision, 3M|Ascending|6,105|0.79|0.84|1.15|2.23|5.16|0.43|15.81|(23.83)|0.00|274|4,757|74.45|63.44|
|36 IBES FY1 Mean DPS Revision, 1M|Ascending|6,671|(3.88)|0.76|1.25|1.68|4.12|0.41|12.65|(16.63)|0.00|293|4,881|72.70|11.09|
|37 IBES FY1 Mean DPS Revision, 3M|Ascending|6,620|(3.99)|0.64|1.37|2.13|5.51|0.39|19.08|(24.51)|0.00|291|4,822|71.13|65.99|
|38 IBES FY1 Mean FFO Revision, 1M|Ascending|7,943|(1.14)|0.73|1.19|2.00|3.94|0.51|11.73|(8.89)|0.00|220|5,267|75.00|13.62|
|39 IBES FY1 Mean FFO Revision, 3M|Ascending|7,830|(1.36)|1.16|1.54|2.67|5.46|0.49|16.27|(14.53)|0.00|217|5,168|71.89|67.93|
|40 IBES FY1 Mean ROE Revision, 1M|Ascending|8,865|(3.23)|0.51|1.13|1.69|4.05|0.42|13.70|(10.51)|0.00|272|6,222|67.65|15.65|
|41 IBES FY1 Mean ROE Revision, 3M|Ascending|8,790|(2.95)|0.39|1.37|2.12|5.00|0.42|15.70|(13.58)|0.00|270|6,100|68.52|69.56|
|42 Target price implied return|Descending|8,808|(5.17)|1.20|0.18|1.05|13.18|0.08|55.58|(36.25)|0.22|236|7,033|54.24|83.08|
|43 Recommendation, mean|Descending|9,129|(0.24)|(1.64)|0.01|1.47|6.54|0.22|17.41|(16.84)|0.00|305|7,624|63.28|94.79|
|44 Mean recommendation revision, 3M|Descending|9,102|(0.37)|0.33|0.35|1.59|2.82|0.56|10.01|(10.13)|0.00|302|7,598|71.52|60.32|
|**5. Quality**||||||||||||||||
|45 Return on Equity|Ascending|10,383|9.69|4.30|3.67|4.08|9.33|0.44|30.68|(34.69)|0.00|304|8,194|69.41|97.19|
|46 return on capital|Ascending|10,443|7.29|3.17|3.06|4.20|11.36|0.37|49.47|(34.02)|0.00|352|7,586|66.48|98.00|
|47 Return on Assets|Ascending|10,558|12.54|6.91|4.03|4.68|12.49|0.37|44.20|(30.31)|0.00|352|7,706|65.34|98.05|
|48 Asset Turnover|Ascending|10,463|11.21|5.36|2.94|2.75|15.81|0.17|44.64|(51.55)|0.00|352|8,084|58.24|99.86|
|49 Gross margin|Ascending|9,883|4.82|3.77|1.80|1.78|5.52|0.32|16.60|(13.45)|0.00|352|7,426|63.64|98.96|
|50 EBITDA margin|Ascending|10,486|13.97|6.34|2.73|3.87|13.18|0.29|42.97|(41.30)|0.00|352|8,108|59.94|96.70|
|51 Berry Ratio|Ascending|8,632|1.21|2.71|1.69|2.51|8.86|0.28|29.57|(20.79)|0.00|352|5,897|59.09|97.95|
|52 IBES FY1 EPS dispersion|Descending|9,027|2.41|3.48|1.42|0.91|9.41|0.10|32.68|(25.37)|0.07|352|6,943|52.84|88.06|
|53 IBES 5Y EPS growth/stability|Ascending|8,913|7.40|2.92|2.38|1.62|5.71|0.28|18.66|(20.47)|0.00|352|6,697|61.65|98.29|
|54 YoY change in debt outstanding|Descending|8,791|(2.20)|(1.03)|(0.52)|0.18|3.64|0.05|11.51|(11.34)|0.35|352|6,724|52.84|91.50|
|55 Current ratio|Descending|8,808|1.96|(0.05)|(0.16)|0.53|8.36|0.06|27.86|(27.01)|0.24|352|6,633|49.72|98.54|
|56 Long-term debt/equity|Ascending|10,338|5.56|2.12|1.18|0.81|6.26|0.13|22.37|(18.17)|0.02|352|7,990|54.55|98.91|
|57 Merton's distance to default|Ascending|8,933|(0.50)|4.73|3.03|2.92|10.78|0.27|31.19|(31.18)|0.00|352|6,924|61.65|93.17|
|58 Capex to Dep|Descending|8,574|2.53|2.73|1.39|1.51|6.54|0.23|22.38|(19.93)|0.00|352|5,794|60.51|97.13|
|**6. Technicals**||||||||||||||||
|59 Realized vol, 1Y daily|Descending|10,706|4.75|7.74|5.50|5.31|14.36|0.37|29.45|(44.64)|0.00|352|8,439|63.07|98.97|
|60 Skewness, 1Y daily|Descending|10,706|8.12|4.43|3.41|1.83|5.22|0.35|15.03|(32.98)|0.00|352|8,439|65.91|90.14|
|61 Moving average crossover, 15W-36W|Ascending|10,634|(7.76)|0.04|1.80|2.86|13.74|0.21|37.15|(45.46)|0.00|352|7,595|63.35|91.34|
|62 Normalized abnormal volume|Ascending|10,924|6.20|4.24|3.52|2.56|6.33|0.40|20.47|(14.71)|0.00|352|8,453|63.92|66.98|



**Note:** 

- 1 Direction indicates how the factor scores are sorted. Ascending order means higher factors scores are likely to be associated with higher subsequent stock returns, and vice versa for descending order. 

- 2 P-value indicates the statistical significance of the factor's performance. A smaller p-value suggests that is it more likely the factor's performance is different from zero. 

3 This is the autocorrelation of the factor scores over time. Higher serial correlation indicates lower portfolio turnover based on the factor. 

_Source : Bloomberg Finance LP, Compustat, IBES, MSCI, Russell, S&P, Thomson Reuters, Worldscope, Deutsche Bank_ 

Page 23 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## References 

Alex Chao, Ronnie Shah, Pam Finelli, Hallie Martin, Chin Okoro, Srineel Jalagani, George Zhao, David Elledge. “Signal Processing: What Happens When the World Goes Passive? Active ETF Strategies”, Deutsche Bank Quantitative Strategy (2018). 

Alex Chao, Ronnie Shah, George Zhao, David Elledge. “The Quant View: What Happens When the Rest of the World Goes Passive?”, Deutsche Bank Quantitative Strategy (2018). 

Ben-David, Itzhak and Franzoni, Francesco A. and Moussawi, Rabih, Do ETFs Increase Volatility? (November 30, 2017). Journal of Finance, Forthcoming; Fisher College of Business Working Paper No. 2011-03-20; Swiss Finance Institute Research Paper No. 11-66; AFA 2013 San Diego Meetings Paper; Charles A. Dice Center Working Paper No. 2011-20. 

Daniel, Kent D. and Moskowitz, Tobias J., Momentum Crashes (September 30, 2013). Swiss Finance Institute Research Paper No. 13-61; Columbia Business School Research Paper No. 14-6; Fama-Miller Working Paper. 

Frazzini, Andrea and Lamont, Owen A., Dumb Money: Mutual Fund Flows and the Cross-Section of Stock Returns (August 2005). NBER Working Paper No. w11526. 

Glosten, L., S. Nallareddy, and Y. Zou. 2016. ETF trading and informational efficiency of underlying securities. Working paper. Columbia University. September. 

Israeli, Doron and Lee, Charles M.C. and Sridharan, Suhas A., Is There a Dark Side to Exchange Traded Funds? An Information Perspective (January 13, 2017). Review of Accounting Studies, Vol. 22, Pages 1048-1083, 2017. 

Wermers, Russ, and Jinming Xue, 2015, Intraday ETF Trading and the Volatility of the Underlying, Working Paper, University of Maryland. 

Page 24 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## Appendix 1 

## Important Disclosures 

## *Other information available upon request 

*Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors . Other information is sourced from Deutsche Bank, subject companies, and other sources. For disclosures pertaining to recommendations or estimates made on securities other than the primary subject of this research, please see the most recently published company report or visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/CompanySearch. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Topics/Equities?topicId=RB0002. Investors are strongly encouraged to review this information before investing. 

## Analyst Certification 

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst(s). In addition, the undersigned lead analyst(s) has not and will not receive any compensation for providing a specific recommendation or view in this report. Alex Chao, Ronnie Shah, Hallie Martin, Shuan Wei, Jessica Zhang. 

## Hypothetical Disclaimer 

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis. 

## Additional ETF Information 

Information on ETFs is provided strictly for illustrative purposes and should not be deemed an offer to sell or a solicitation of an offer to buy shares of any fund that is described in this document. Consider carefully any fund's investment objectives, risk factors, and charges and expenses before investing. This and other information can be found in the fund's prospectus. Prospectuses about db X-trackers funds and Powershares DB funds can be obtained by calling 1-877-369-4617 or by visiting www.DBXUS.com. Read prospectuses carefully before investing. Past performance is not necessarily indicative of future results. Investing involves risk, including possible loss of principal. To better understand the similarities and differences between investments, including investment objectives, risks, fees and expenses, it is important to read the products' prospectuses. Shares of ETFs may be sold throughout the day on an exchange through any brokerage account. However, shares may only be redeemed directly from an ETF by authorized participants, in very large creation/redemption units. Transactions in shares of ETFs will result in brokerage commissions and will generate tax consequences. ETFs are obliged to distribute portfolio gains to shareholders. Deutsche Bank may be an issuer, advisor, manager, distributor or administrator of, or provide other services to, an ETF included in this report, for which it receives compensation. db X-trackers and Powershares DB funds are distributed by ALPS Distributors, Inc. The opinions expressed are those of the authors and do not necessarily reflect the views of DB, ALPS or their affiliates. 

Aside from within this report, important conflict disclosures can also be found at https://gm.db.com/equities under the 'Disclosures Lookup' and 'Legal' tabs. Investors are strongly encouraged to review this information before investing. 

Page 25 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

## Additional Information 

The information and opinions in this report were prepared by Deutsche Bank AG or one of its affiliates (collectively 'Deutsche Bank'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, Deutsche Bank makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. Deutsche Bank neither endorses the content nor is responsible for the accuracy or security controls of those websites. 

If you use the services of Deutsche Bank in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a Deutsche Bank analyst,  Deutsche Bank may act as principal for its own account or as agent for another person. 

Deutsche Bank may consider this report in deciding to trade as principal.  It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report.  Others within Deutsche Bank, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. Deutsche Bank issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communication may differ from recommendations contained in others, whether as a result of differing time horizons, methodologies, perspectives or otherwise. Deutsche Bank and/or its affiliates may also be holding debt or equity securities of the issuers it writes on. Analysts are paid in part based on the profitability of Deutsche Bank AG and its affiliates, which includes investment banking, trading and principal trading revenues. 

Opinions, estimates and projections constitute the current judgment of the author as of the date of this report. They do not necessarily reflect the opinions of Deutsche Bank and are subject to change without notice. Deutsche Bank provides liquidity for buyers and sellers of securities issued by the companies it covers. Deutsche Bank research analysts sometimes have shorter-term trade ideas that may be inconsistent with Deutsche Bank's existing longer-term ratings. Some trade ideas for equities are listed as Catalyst Calls on the Research Website (https://research.db.com/Research/) , and can be found on the general coverage list and also on the covered company’s page. A Catalyst Call represents a high-conviction belief by an analyst that a stock will outperform or underperform the market and/or a specified sector over a time frame of no less than two weeks and no more than three months. In addition to Catalyst Calls, analysts may occasionally discuss with our clients, and with Deutsche Bank salespersons and traders, trading strategies or ideas that reference catalysts or events that may have a nearterm or medium-term impact on the market price of the securities discussed in this report, which impact may be directionally counter to the analysts' current 12-month view of total return or investment return as described herein. Deutsche Bank has no obligation to update, modify or amend this report or to otherwise notify a recipient thereof if an opinion, forecast or estimate changes or becomes inaccurate. Coverage and the frequency of changes in market conditions and in both general and company-specific economic prospects make it difficult to update research at defined intervals.  Updates are at the sole discretion of the coverage analyst or of the Research Department Management, and the majority of reports are published at irregular intervals. This report is provided for informational purposes only and does not take into account the particular investment objectives, financial situations, or needs of individual clients. It is not an offer or a solicitation of an offer to buy or sell any financial instruments or to participate in any particular trading strategy. Target prices are inherently imprecise and a product of the analyst’s judgment.  The financial instruments discussed in this report may not be suitable for all investors, and investors must make their own informed investment decisions. Prices and availability of financial instruments are subject to change without notice, and investment transactions can lead to losses as a result of price fluctuations and other factors.  If a financial instrument is denominated in a currency other than an investor's currency, a change in exchange rates may adversely affect the investment.  Past performance is not necessarily indicative of future results. Performance calculations exclude transaction costs, unless otherwise indicated. Unless otherwise indicated, prices are current as of the end of the previous trading session and are sourced from local exchanges via Reuters, Bloomberg and other vendors.  Data is also sourced from Deutsche Bank, subject companies, and other parties. 

The Deutsche Bank Research Department is independent of other business divisions of the Bank. Details regarding our organizational arrangements and information barriers we have to prevent and avoid conflicts of interest with respect to our research are available on our website (https://research.db.com/Research/) under Disclaimer. 

Macroeconomic fluctuations often account for most of the risks associated with exposures to instruments that promise to pay fixed or variable interest rates. For an investor who is long fixed-rate instruments (thus receiving these cash flows), increases in interest rates naturally lift the discount factors applied to the expected cash flows and thus cause a loss. The longer the maturity of a certain cash flow and the higher the move in the discount factor, the higher will be the loss. Upside surprises in inflation, fiscal funding needs, and FX depreciation rates are among the most common adverse macroeconomic shocks to receivers. But counterparty exposure, issuer creditworthiness, client segmentation, regulation (including changes in assets holding limits for different types of investors), changes in tax policies, currency convertibility (which may constrain currency conversion, repatriation of profits and/or liquidation of positions), and settlement issues related to local clearing houses are also important risk factors. The sensitivity of fixed-income instruments to macroeconomic shocks may be mitigated by indexing the contracted cash flows to inflation, to FX depreciation, or to specified interest rates – these are common in emerging markets.  The index fixings may – by construction – lag or mis-measure the actual move in the underlying variables they are intended to track. The choice of the proper fixing (or metric) is particularly important in swaps markets, where floating coupon rates (i.e., coupons indexed to a typically short-dated interest rate reference index) are exchanged for fixed coupons. Funding in a currency that differs from the currency in which coupons are denominated carries FX risk. Options on swaps (swaptions) the risks typical to options in addition to the risks related to rates movements. 

Derivative transactions involve numerous risks including market, counterparty default and illiquidity risk.  The appropriateness 

Page 26 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

of these products for use by investors depends on the investors' own circumstances, including their tax position, their regulatory environment and the nature of their other assets and liabilities; as such, investors should take expert legal and financial advice before entering into any transaction similar to or inspired by the contents of this publication. The risk of loss in futures trading and options, foreign or domestic, can be substantial. As a result of the high degree of leverage obtainable in futures and options trading, losses may be incurred that are greater than the amount of funds initially deposited – up to theoretically unlimited losses. Trading in options involves risk and is not suitable for all investors. Prior to buying or selling an option, investors must review the 'Characteristics and Risks of Standardized Options”, at http://www.optionsclearing.com/ about/publications/character-risks.jsp.  If you are unable to access the website, please contact your Deutsche Bank representative for a copy of this important document. 

Participants in foreign exchange transactions may incur risks arising from several factors, including the following: (i) exchange rates can be volatile and are subject to large fluctuations; (ii) the value of currencies may be affected by numerous market factors, including world and national economic, political and regulatory events, events in equity and debt markets and changes in interest rates; and (iii) currencies may be subject to devaluation or government-imposed exchange controls, which could affect the value of the currency. Investors in securities such as ADRs, whose values are affected by the currency of an underlying security, effectively assume currency risk. 

Unless governing law provides otherwise, all transactions should be executed through the Deutsche Bank entity in the investor's home jurisdiction. Aside from within this report, important conflict disclosures can also be found at https:// research.db.com/Research/ on each company’s research page. Investors are strongly encouraged to review this information before investing. 

Deutsche Bank (which includes Deutsche Bank AG, its branches and affiliated companies) is not acting as a financial adviser, consultant or fiduciary to you or any of your agents (collectively, “You” or “Your”) with respect to any information provided in this report. Deutsche Bank does not provide investment, legal, tax or accounting advice, Deutsche Bank is not acting as your impartial adviser, and does not express any opinion or recommendation whatsoever as to any strategies, products or any other information presented in the materials.  Information contained herein is being provided solely on the basis that the recipient will make an independent assessment of the merits of any investment decision, and it does not constitute a recommendation of, or express an opinion on, any product or service or any trading strategy. 

The information presented is general in nature and is not directed to retirement accounts or any specific person or account type, and is therefore provided to You on the express basis that it is not advice, and You may not rely upon it in making Your decision. The information we provide is being directed only to persons we believe to be financially sophisticated, who are capable of evaluating investment risks independently, both in general and with regard to particular transactions and investment strategies, and who understand that Deutsche Bank has financial interests in the offering of its products and services. If this is not the case, or if You are an IRA or other retail investor receiving this directly from us, we ask that you inform us immediately. 

In July 2018, Deutsche Bank revised its rating system for short term ideas whereby the branding has been changed to Catalyst Calls (“CC”) from SOLAR ideas; the rating categories for Catalyst Calls originated in the Americas region have been made consistent with the categories used by Analysts globally; and the effective time period for CCs has been reduced from a maximum of 180 days to 90 days. 

**United States** : Approved and/or distributed by Deutsche Bank Securities Incorporated, a member of FINRA, NFA and SIPC. Analysts located outside of the United States are employed by non-US affiliates that are not subject to FINRA regulations. 

**Germany** : Approved and/or distributed by Deutsche Bank AG, a joint stock corporation with limited liability incorporated in the Federal Republic of Germany with its principal office in Frankfurt am Main. Deutsche Bank AG is authorized under German Banking Law and is subject to supervision by the European Central Bank and by BaFin, Germany’s Federal Financial Supervisory Authority. 

**United Kingdom** : Approved and/or distributed by Deutsche Bank AG acting through its London Branch at Winchester House, 1 Great Winchester Street, London EC2N 2DB. Deutsche Bank AG in the United Kingdom is authorised by the Prudential Regulation Authority and is subject to limited regulation by the Prudential Regulation Authority and Financial Conduct Authority. Details about the extent of our authorisation and regulation are available on request. 

**Hong Kong** : Distributed by Deutsche Bank AG, Hong Kong Branch or Deutsche Securities Asia Limited (save that any research relating to futures contracts within the meaning of the Hong Kong Securities and Futures Ordinance Cap. 571 shall be distributed solely by Deutsche Securities Asia Limited). The provisions set out above in the 'Additional Information' section shall apply to the fullest extent permissible by local laws and regulations, including without limitation the Code of Conduct for Persons Licensed or Registered with the Securities and Futures Commission. 

**India** : Prepared by Deutsche Equities India Private Limited (DEIPL) having CIN: U65990MH2002PTC137431 and registered office at 14th Floor, The Capital, C-70, G Block, Bandra Kurla Complex Mumbai (India) 400051. Tel: + 91 22 7180 4444. It is registered by the Securities and Exchange Board of India (SEBI) as a Stock broker bearing registration no.: INZ000252437; Merchant Banker bearing SEBI Registration no.: INM000010833 and Research Analyst bearing SEBI Registration no.: INH000001741. DEIPL may have received administrative warnings from the SEBI for breaches of Indian regulations. Deutsche Bank and/or its affiliate(s) may have debt holdings or positions in the subject company.  With regard to information on - associates, please refer to the “Shareholdings” section in the Annual Report at: https://www.db.com/ir/en/annual reports.htm. 

Page 27 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

**Japan** : Approved and/or distributed by Deutsche Securities Inc.(DSI). Registration number - Registered as a financial instruments dealer by the Head of the Kanto Local Finance Bureau (Kinsho) No. 117. Member of associations: JSDA, Type II Financial Instruments Firms Association and The Financial Futures Association of Japan. Commissions and risks involved in stock transactions - for stock transactions, we charge stock commissions and consumption tax by multiplying the transaction amount by the commission rate agreed with each customer. Stock transactions can lead to losses as a result of share price fluctuations and other factors. Transactions in foreign stocks can lead to additional losses stemming from foreign exchange fluctuations. We may also charge commissions and fees for certain categories of investment advice, products and services. Recommended investment strategies, products and services carry the risk of losses to principal and other losses as a result of changes in market and/or economic trends, and/or fluctuations in market value. Before deciding on the purchase of financial products and/or services, customers should carefully read the relevant disclosures, prospectuses and other documentation. 'Moody's', 'Standard  Poor's', and 'Fitch' mentioned in this report are not registered credit rating agencies in Japan unless Japan or 'Nippon' is specifically designated in the name of the entity. Reports on Japanese listed companies not written by analysts of DSI are written by Deutsche Bank Group's analysts with the coverage companies specified by DSI. Some of the foreign securities stated on this report are not disclosed according to the Financial Instruments and Exchange Law of Japan. Target prices set by Deutsche Bank's equity analysts are based on a 12-month forecast period.. 

## **Korea** : Distributed by Deutsche Securities Korea Co. 

**South Africa** : Deutsche Bank AG Johannesburg is incorporated in the Federal Republic of Germany (Branch Register Number in South Africa: 1998/003298/10). 

**Singapore** :  This report is issued by Deutsche Bank AG, Singapore Branch or Deutsche Securities Asia Limited, Singapore Branch (One Raffles Quay #18-00 South Tower Singapore 048583, +65 6423 8001), which may be contacted in respect of any matters arising from, or in connection with, this report.  Where this report is issued or promulgated by Deutsche Bank in Singapore to a person who is not an accredited investor, expert investor or institutional investor  (as defined in the applicable Singapore laws and regulations), they accept legal responsibility to such person for its contents. 

**Taiwan** : Information on securities/investments that trade in Taiwan is for your reference only. Readers should independently evaluate investment risks and are solely responsible for their investment decisions. Deutsche Bank research may not be distributed to the Taiwan public media or quoted or used by the Taiwan public media without written consent. Information on securities/instruments that do not trade in Taiwan is for informational purposes only and is not to be construed as a recommendation to trade in such securities/instruments. Deutsche Securities Asia Limited, Taipei Branch may not execute transactions for clients in these securities/instruments. 

**Qatar** : Deutsche Bank AG in the Qatar Financial Centre (registered no. 00032) is regulated by the Qatar Financial Centre Regulatory Authority. Deutsche Bank AG - QFC Branch may undertake only the financial services activities that fall within the scope of its existing QFCRA license. Its principal place of business in the QFC: Qatar Financial Centre, Tower, West Bay, Level 5, PO Box 14928, Doha, Qatar. This information has been distributed by Deutsche Bank AG. Related financial products or services are only available only to Business Customers, as defined by the Qatar Financial Centre Regulatory Authority. 

**Russia** : The information, interpretation and opinions submitted herein are not in the context of, and do not constitute, any appraisal or evaluation activity requiring a license in the Russian Federation. 

**Kingdom of Saudi Arabia** : Deutsche Securities Saudi Arabia LLC Company (registered no. 07073-37) is regulated by the Capital Market Authority. Deutsche Securities Saudi Arabia may undertake only the financial services activities that fall within the scope of its existing CMA license. Its principal place of business in Saudi Arabia: King Fahad Road, Al Olaya District, P.O. Box 301809, Faisaliah Tower - 17th Floor, 11372 Riyadh, Saudi Arabia. 

**United Arab Emirates** : Deutsche Bank AG in the Dubai International Financial Centre (registered no. 00045) is regulated by the Dubai Financial Services Authority. Deutsche Bank AG - DIFC Branch may only undertake the financial services activities that fall within the scope of its existing DFSA license. Principal place of business in the DIFC: Dubai International Financial Centre, The Gate Village, Building 5, PO Box 504902, Dubai, U.A.E. This information has been distributed by Deutsche Bank AG. Related financial products or services are available only to Professional Clients, as defined by the Dubai Financial Services Authority. 

**Australia and New Zealand** :  This research is intended only for 'wholesale clients' within the meaning of the Australian Corporations Act and New Zealand Financial Advisors Act, respectively. Please refer to Australia-specific research disclosures and related information at https://australia.db.com/australia/content/research-information.html Where research refers to any particular financial product recipients of the research should consider any product disclosure statement, prospectus or other applicable disclosure document before making any decision about whether to acquire the product. In preparing this report, the primary analyst or an individual who assisted in the preparation of this report has likely been in contact with the company that is the subject of this research for confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance.  Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption (“ABC”) team, analysts may not accept perks or other items of value for their personal use from issuers they cover. 

Additional information relative to securities, other financial products or issuers discussed in this report is available upon 

Page 28 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

9 May 2019 The Quant View 

request. This report may not be reproduced, distributed or published without Deutsche Bank's prior written consent. 

Copyright © 2019 Deutsche Bank AG 

Page 29 

Deutsche Bank Securities Inc. 

Provided for the exclusive use of hugues.demurard@exoduspoint.com on 2020-09-20T18:50+00:00. DO NOT REDISTRIBUTE 

## David Folkerts-Landau 

Group Chief Economist and Global Head of Research 

Pam Finelli Global Chief Operating Officer Research Anthony Klarman Global Head of Debt Research 

Michael Spencer Head of APAC Research 

Kinner Lakhani Head of EMEA Equity Research 

Steve Pollard 

Head of Americas Research Global Head of Equity Research 

Joe Liew Head of APAC Equity Research 

Jim Reid Francis Yared Global Head of Global Head of Rates Research Thematic Research 

George Saravelos Head of FX Research 

Peter Hooper Global Head of Economic Research 

Andreas Neubauer Head of Germany Research 

Spyros Mesomeris Global Head of Quantitative and QIS Research 

## International Production Locations 

Deutsche Bank AG Deutsche Bank Place Level 16 Corner of Hunter & Phillip Streets Sydney, NSW 2000 Australia Tel: (61) 2 8258 1234 

Deutsche Bank AG Equity Research Mainzer Landstrasse 11-17 60329 Frankfurt am Main Germany Tel: (49) 69 910 00 

Deutsche Bank AG Filiale Hongkong International Commerce Centre, 1 Austin Road West,Kowloon, Hong Kong Tel: (852) 2203 8888 

Deutsche Securities Inc. 2-11-1 Nagatacho Sanno Park Tower Chiyoda-ku, Tokyo 100-6171 Japan Tel: (81) 3 5156 6770 

Deutsche Bank AG London Deutsche Bank Securities Inc. 1 Great Winchester Street 60 Wall Street London EC2N 2EQ New York, NY 10005 United Kingdom United States of America Tel: (44) 20 7545 8000 Tel: (1) 212 250 2500 

