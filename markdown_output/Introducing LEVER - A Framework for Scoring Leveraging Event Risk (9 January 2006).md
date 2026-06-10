## **Fixed Income Research Quantitative Credit Strategies** 

January 9, 2006 

Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## Introducing LEVER: A Framework for Scoring LEVeraging Event Risk **[1]** 

## **January 9, 2006 QUANTITATIVE CREDIT RESEARCH** 

## **Minh Trinh** 

+1 212-526-1712 mtrinh@lehman.com 

**Bodha Bhattacharya** +1 212-526-7907 bbhattac@lehman.com 

_We introduce LEVER, a quantitative framework for measuring the relative risk of a leveraged buyout (LBO) or leveraged recapitalization in the US credit market. LEVER fits key accounting and market information into two simple risk measures: the Firm LEVERScore and the Macro LEVER-Score. The Firm LEVER-Score seeks to capture a firm’s likelihood of financial restructuring (via LBO or a leveraged recapitalization) using valuation, operation and execution variables. The Macro LEVER-Score measures the LBOfriendliness of the overall market using economic, market and financial variables. High scores on both measures suggest a higher likelihood of an LBO or leveraged recapitalization the following year. The Firm LEVER-Score showed strong predictive power in a test covering the period 1995-2005. We provide a list of issuers highlighted by our model as having significant relative LBO/recap risk exposure in 2006._ 

## **1. INTRODUCTION** 

## **QUANTITATIVE MARKET STRATEGIES** 

**Mukundan Devarajan** +44 207-102-9033 mudevara@lehman.com 

**U.S. CREDIT STRATEGY** +1 212-526-7777 

**David Heike** dheike@lehman.com 

**Marc Pomper** mpomper@lehman.com 

**Jamie Wolosky** jawolosk@lehman.com 

Investors with corporate bond portfolios are mainly exposed to default, liquidity and spread volatility risk. LBOs and leveraged recapitalizations pose an added threat because the large amount of debt raised for such transactions can lead to credit deterioration. LBO targets often fall from investment grade to BB or below. Moreover, the risk of an LBO or a leveraged recapitalization can boost spread volatility, leading to large losses in corporate bond portfolios. While actual LBOs are rare, leveraged recapitalizations occur more frequently. In the remainder of this article, the term _‘LBO’_ will be liberally used to refer both to an actual LBO transaction and a leveraged recapitalization, as they have similar implications for credit portfolios and are driven by similar considerations. 

LBOs and leveraged recapitalizations are a newly resurgent risk. They represented the second-biggest driver of investment-grade underperformance in the past year, after the US automakers. Knight Ridder was the worst-performing issuer in the Lehman Brothers US Investment Grade (IG) Index in 2005 (-1950bp excess return). Albertsons (-1275bp excess return) was at #5, followed by Kerr-McGee (-1223bp excess return), forced to recapitalize by shareholder activist Carl Icahn (Figure 1). Although our base assumption regarding leveraged transactions is that they are punitive to bondholders, we recognize that such risks can be mitigated in certain instances by tenders, exchanges and the like, particularly for issues with better covenants. 

> _1 The authors would like to thank Srivaths Balakrishnan, Margery Cunningham, Hemant Dabke, Mike Guarnieri, Mary Margiotta, Eric Miller, Vasant Naik, Marco Naldi, and Brad Rogoff for their helpful comments and assistance._ 

January 9, 2006 

1 

**Please see important analyst certification(s) on the back cover of this report.** 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

**Figure 1.  10 worst-performing Lehman US IG Credit Index issuers, 2005** 

**==> picture [356 x 183] intentionally omitted <==**

**----- Start of picture text -----**<br>
Knight Ridder<br>Ford<br>Axle<br>General Motors<br>Albertsons<br>Kerr-McGee<br>Rock-Tenn<br>Pactiv<br>Lear<br>Affiliated Computer<br>-2000 -1500 -1000 -500 0<br>Excess returns (2005), bp<br>Source:  Lehman Brothers.<br>**----- End of picture text -----**<br>


Investors were largely unprepared for this risk in early 2005, with limited incremental spread priced into the LBO and leveraged recapitalization targets. While current wider spreads for LBO-associated companies suggest that the market is better prepared for 2006, we think this risk is still not accurately priced across all firms/sectors. This is largely because of the inherent difficulty in predicting which firms will ultimately undergo an LBO or a leveraged recapitalization.[2] This is especially true for most debt investors, who typically have limited access to the standard screening process used by financial sponsors. Moreover, equity-based analysis of LBO risk is of limited use because LBOs favor shareholders over debt-holders, causing equity prices to rise in anticipation of such events. 

In this article, we propose a new framework called _LEVER_ for scoring the risk of leveraged recapitalizations which is designed to narrow this informational gap. In developing such a framework, identifying the appropriate inputs (i.e. characteristics of firms that lead them to be potential LBO or leveraged recapitalization targets) is as critical as combining these inputs in a sensible functional form. To that end, we base our framework on extensive discussions with experienced practitioners in the LBO arena. The resulting model is a quantitative representation of their collective approaches. 

There are two components to the _LEVER_ framework. The _**Firm LEVER-Score**_ identifies companies that look potentially more attractive to financial sponsors. Scores range from 0 to 10, and companies that score above 7.5 are particularly at risk. The _**Macro LEVER-Score**_ identifies market environments that are more amenable to LBOs. We test our Firm _LEVER_ - Score on the firms in the S&P 1500 between 1995 and 2005 and document strong evidence of its predictive power. 

The rest of the article is organized as follows. In **Section 2** , we present a brief overview of the variables used to calculate the Firm _LEVER_ -Score. In **Section 3** , we explain the construction of The Macro _LEVER_ -Score. In **Section 4,** we provide some results on the historical performance of our method. In **Section 5** , we discuss the LBO Outlook for 2006 and identify firms that currently appear to have significant LBO or leveraged recapitalization risk, as reflected by a high Firm _LEVER_ -Score. We present our conclusions in **Section 6** . 

> _2  Although there have been some academic studies on this subject, including that by Opler and Titman (1993), not many are focused on forecasting LBO activity. Often, such studies are focused on the post-transaction performance of an LBO target (see for instance, Long and Ravenscraft, 1993)._ 

January 9, 2006 

2 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## **Leveraged Buyouts and Leveraged Recapitalizations: An Overview** 

An LBO is a transaction in which an acquirer takes a company (or a business unit of a company) private by purchasing its stock. These transactions are typically funded with 70-80% debt, resulting in a markedly weaker credit position for outstanding bondholders. The acquirer is often referred to as a financial sponsor because it provides the initial capital for the transaction, but does not intend to remain permanently invested. Post-acquisition, the acquirer uses the cash flows generated by the target firm to service the debt and provide additional returns. Effectively, the target firm finances its own acquisition. Leveraged recapitalizations operate similarly, except that the company remains public. 

LBOs can be detrimental to prior debt holders because of the drastic increase in leverage. Investment-grade companies taken private through an LBO are usually rated B or BB after the transaction is complete. Furthermore, the new debt is often issued with covenants not offered to previously existing bondholders. As a result, the mere threat of an LBO is often a cause of increased spread volatility. 

In identifying LBO targets, financial sponsors consider the initial equity investment required and the potential for additional financing. The investment cost is determined by the total amount of debt needed to fund the acquisition and the interest costs of raising the additional debt. Sponsors also look for an absence of restrictive covenants in the existing debt of the target firm. 

Once a firm is bought out, financial sponsors can generate equity returns by improving operations, increasing incentives for the management to perform, and better utilizing free cash flows. The inherent increase in risk taking resulting from the increased leverage also creates the potential for higher returns. Finally, the financial sponsor may force corporate restructuring or asset disposals. 

Even when desirable targets can be identified, the macroeconomic environment must be amenable to LBOs for a transaction to occur. Buyout firms raise capital more easily in a growing economy. Furthermore, low interest rates facilitate LBOs by reducing the cost of issuing new debt. Conversely, when the high-yield loan or debt market is experiencing numerous corporate defaults, an LBO might be expensive to finance. 

January 9, 2006 

3 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## **2. KEY VARIABLES THAT DRIVE LBO TRANSACTIONS** 

## **2.1. Firm-level characteristics** 

Our model includes three broad categories of firm-level factors driving LBOs. The most attractive targets have below-market _valuations,_ their _operations_ generate adequate cash flows for servicing debt, and are likely to enjoy a smooth _execution_ of the transaction. We discuss these factors below. 

## **Valuation** 

The primary consideration for an LBO transaction is the potential for value creation.[3] Target firms usually have a large “value gap” between the current enterprise value and the potential value after restructuring, which can be measured by the following variables: 

## _Book-to-market ratio_ 

The book value can be used as a proxy for the disposal value of the firm’s assets, or the replacement cost of the assets. A high book-to-market ratio may indicate a mispricing between the public and private equity markets. It may also indicate the potential for improving operations under new management. 

## _Enterprise value to EBITDA[4 ] multiple_ 

The enterprise value to EBITDA multiple tends to be low when the enterprise value does not fully reflect the potential earnings capacity of the firm, or when there are concerns regarding the sustainability of recent earnings levels. In particular, the relative difference in this multiple between the firm and its sector peers may reflect an attractive opportunity for an LBO acquirer. This is especially true when the target is a division or a subsidiary, which may be unfairly bundled within a larger firm with different valuation norms. 

## **Operations** 

Targets must have sufficient cash flows to service the debt raised for funding an LBO transaction. Additionally, acquirers may look for firms whose operations are free from future capital commitments. The following variables can be used to capture these characteristics: 

## _Free cash flow yield_ 

Free cash flow yield (the ratio of free cash flow to market value) combines operational and valuation attractiveness of a potential LBO candidate. Firms with high free cash flows and low market value are attractive LBO candidates. 

## _Growth of capital expenditure (capex)_[5] 

Rising capital expenditure may indicate large operational commitments that could compete for the cash flows of the firm. However, the capex growth of a firm should be compared with its sector peers, because increased capex may result from systematic factors affecting the sector rather than the commitments of an individual firm. 

## **Execution** 

An attractive LBO target should also exhibit characteristics that enable the execution of a releveraging transaction. The following variables are indicative of these characteristics: 

> _3 See Berg and Gottschalg (2004) for a survey on value creation in buyouts._ 

> _4 Earnings Before Interests, Taxes, Depreciation and Amortization_ 

> _5 Defined as the one year change in capital expenditure_ 

January 9, 2006 

4 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## _Cash-flow variability_ 

While the size of cash flows signals operational characteristics, the stability of cash flows indicates the potential for a firm to ‘weather’ an LBO. Stable cash flows suggest that the firm may be able to provide returns to the investor net of the debt servicing cost. This is also a key variable that lenders consider before agreeing to finance an LBO transaction. 

## _Size of the firm_ 

A smaller firm is generally an easier LBO target as it requires a smaller amount of debt to fund the transaction. The size of the firm may be measured either by the market capitalization or the enterprise value. 

## **2.2. Macroeconomic characteristics** 

We examine the overall trends in the level of LBO activity over the past 15 years to assess the correlation of LBO activity with macro drivers of leveraged transactions. In Figure 2, we show the number of large LBOs (deal size >$250m) globally and in the US between 1990 and 2005. There were two peaks in the level of LBO activity, the first in 2000 and the other in 2005. The relative drop in LBO activity in 2001 coincided with the US recession in the early part of this century. 

**Figure 2.  LBO activity: 1990-2005[6]** 

**==> picture [362 x 173] intentionally omitted <==**

**----- Start of picture text -----**<br>
30<br>25<br>20<br>15<br>10<br>5<br>0<br>1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005<br>Global LBOs US LBOs<br>**----- End of picture text -----**<br>


_Source: Lehman Brothers, SDC._ 

> _6 Data for 2005 are until the third quarter of the year_ 

January 9, 2006 

5 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

Several macro factors help explain these trends. In Figure 3, we summarize the correlation of some key variables with the number of LBO transactions. 

**Figure 3.  Correlation of key variables and number and value of LBO transactions** 

**(1990-2005)** 

|**(1990-2005)**|||
|---|---|---|
|**Category**|**Variable**|**Correlation with**<br>**No. of LBOs**|
|Economic Environment|_GDP Growth_|31%|
|Yield Curve|_10 year yield change_|-29%|
||_2y-10y slope change_|-52%|
|Equity Markets|_S&P 500 Returns_|-12%|
|Macro Fundamentals|_S&P 500 Dividend Yield_|-75%|
||_S&P 500 Cash-flow Yield_|22%|
|Financial risk|_Leverage of S&P 500_|-23%|
||_Credit spread changes_|51%|
||_Amount of private equity capital raised in_||
|Technicals|_previous year_|65%|



_Source: Lehman Brothers, Bloomberg, Venture Economics._ 

## _Economic growth_ 

Overall growth (indicated by the y-o-y GDP growth) is positively correlated with the number of LBOs. Revenue and cash flow growth generally accelerate in periods of high growth, enabling more rapid debt reduction on the part of acquired companies. 

## _Interest rates_ 

In low rate and low equity risk premia environments, investors seek yield from alternative asset classes, such as private equity funds. This increases the amount of capital at the disposal of acquirers, hence accentuating LBO activity. Furthermore, low interest rates decrease the cost of financing new debt. 

## _Equity market returns_ 

A weaker equity market signals a more LBO-friendly environment since cheap target firms might be easier to find. Conversely, in periods when the equity market is strong, private equity firms must compete with strategic buyers who can use the strength of their own stock to fund acquisitions. As expected, equity market returns and the number of LBOs are negatively correlated. However, the correlation is moderate because poor equity returns are often associated with poor economic conditions that discourage LBO activity. 

## _Cash flow and dividend yield trends_ 

The number of LBO transactions is negatively correlated with the dividend yield of firms in the S&P 500 and positively correlated with their cash flow yields. High cash flow generation combined with a low dividend payout ratio leaves a lot of cash available for servicing new debt or paying out a special dividend. 

January 9, 2006 

6 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## _Financial risk_ 

Systemic financial risk, exhibited by leverage trends, shows a strong relationship with the number of LBOs. Overall leverage trends are negatively correlated with the number of LBOs because periods in which firms de-leverage are opportune for re-leveraging transactions. Wider credit spreads also reflect systemic financial risk. However, spreads have a positive correlation with LBO trends, which likely is a consequence of the endogeneity of spreads (i.e. spreads widen in anticipation of LBO transactions). Lagged correlations between credit spreads and LBO transactions are in fact negative (approximately -13%). 

## _LBO technicals_ 

The level of private equity raised in the previous year has a relatively high correlation with the number of LBOs (65%). This could explain current high levels of LBO activity, as private equity firms are raising record amounts for their funds.[7] 

## **3. SCORING LBO/RECAP RISK WITH** _**LEVER**_ 

The _LEVER_ framework processes the above firm-specific and market variables into two measures: the Firm _LEVER-Score_ and the _Macro LEVER-Score_ . The Firm _LEVER_ -Score identifies particular issuers using fundamental and market information specific to each firm. The Macro _LEVER_ -Score captures the overall attractiveness of the environment for LBO transactions. In this section, we discuss how these scores are calculated. 

## **3.1. Calculating the Firm** _**LEVER**_ **-Score** 

## **Variations across sectors** 

The likelihood of an LBO or leveraged recapitalization differs from sector to sector. Some sectors are fundamentally unsuited to re-leveraging operations because they are already very highly leveraged. Furthermore, growth sectors with low book-to-market ratios and less stable free cash flow are less attractive LBO candidates than value sectors, where cash flows can be used efficiently to service debt and generate returns. To analyze systematic patterns across sectors, Figure 4 charts the average leverage versus the average book-to-market ratio of different sectors.[8] 

> _7  See for instance “Private Equity Fundraising Activity Surpassed 2004 in First Three Quarters of 2005”, National Venture Capital Association, October 17, 2005._ 

> _8  We define leverage as the ratio of total debt to the market value of equity_ 

January 9, 2006 

7 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

**Figure 4. Sector-level LBO attractiveness** 

**==> picture [500 x 179] intentionally omitted <==**

**----- Start of picture text -----**<br>
0.7 Pre-2001 1 Post-2001<br>Utilities Consumer Non-<br>0.6 0.9 Durables<br>Financials<br>Transportation<br>0.5 Industrials 0.8 Utilities<br>Commercial<br>0.4 Electronics Consumer Non- 0.7 Transportation Industrials Financials<br>Durables<br>0.3 0.6 Commercial<br>Health<br>Electronics<br>0.2<br>0.5<br>Technology Technology<br>0.1<br>0.4<br>Health<br>0<br>0.3<br>0% 30% 60% 90% 120% 150% 180%<br>0% 30% 60% 90% 120% 150% 180%<br>Leverage Leverage<br>Book-to-Market Book-to-Market<br>**----- End of picture text -----**<br>


**==> picture [95 x 6] intentionally omitted <==**

**----- Start of picture text -----**<br>
Source:  Lehman Brothers.<br>**----- End of picture text -----**<br>


**==> picture [85 x 6] intentionally omitted <==**

**----- Start of picture text -----**<br>
Source: Lehman Brothers.<br>**----- End of picture text -----**<br>


The Financial sector consistently displays the highest leverage, making financial firms unlikely LBO candidates. Technology firms, on the other hand, show a transformation around 2001. In the pre-2001 period (which includes the Technology boom of the late 1990s), the sector had by far the lowest book-to-market ratio, implying that it was in a “growth” phase. After 2001, however, Technology transitioned to a “value” status, exhibiting a book-to-market ratio more in line with the other sectors. Since 2001, Technology firms have become inherently more attractive for LBO transactions. 

We incorporate these observations into the construction and testing of our Firm _LEVER_ - Score as follows: 

- We completely exclude financial firms from our data set. 

- We exclude observations of Technology firms prior to 2001, but retain them from 2001 onwards. 

## **Firm-level characteristics** 

After filtering the universe for certain sectors as mentioned above, we analyze firm-level characteristics to identify issuers with heightened risk of an LBO or leverage recapitalization. In Figure 5 we list the variables used to compute the Firm _LEVER_ -Score and our hypothesis for the relative magnitude of these variables for LBO vs. non-LBO names (For instance our hypothesis is that potential LBO candidates would have a high book-to-market ratio). As discussed in Section 2, we group these variables to form three component scores: the Valuation Score, Operation Score and Execution Score (Figure 5). 

**Figure 5.  Components of the Firm** _**LEVER**_ **-Score** 

|**Valuation Score**||**Operation Score**||**Execution Score**||
|---|---|---|---|---|---|
|Book to Market|↑|Free Cash Flow Yield|↑|Firm Size|↓|
|EV to EBITDA|↓|Capex Growth|↓|Free Cash Flow Variability|↓|



_Source: Lehman Brothers._ 

January 9, 2006 

8 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## **Constructing the Firm** _**LEVER**_ **-Score** 

To construct the Firm _LEVER_ -Score, we use the cross sectional-ranking of the normalized _N_ values of the variables listed in Figure 5. We define the normalized value _[V] i_ of a given variable _V_ for the _i[th]_ firm as: 

**==> picture [91 x 37] intentionally omitted <==**

Where: 

- _VUV_ is the market-value-weighted average of the variable V of the firms in the universe _UV_ . The universe _UV_ corresponding to the variable _V_ includes the entire universe of firms for the variables free cash flow yield, firm size and free cash flow variability, and is limited to the sector peers of the _i[th]_ firm for the book to market ratio, EV to EBITDA ratio and capex growth. 

- α _V_ is the desired direction for the given variable (e.g., the α _V_ corresponding to the Book to Market ratio is 1 and that corresponding to the EV to EBITDA multiple is -1). 

Along each normalized variable V[N] , the firms in the universe are ranked. The Valuation, Operation and Execution Scores for the _i[th]_ firm are an average of the rankings corresponding to the underlying variables. In other words, the Valuation score for firm _i_ is an average of its ranking along the Book to Market ratio and EV to EBITDA multiple. The Firm _LEVER_ -Score is then calculated as the average of all the variables underlying the Valuation, Operation and Execution scores.[ 9] 

## **Examples: Toys ‘R’ Us and Halliburton Co.** 

To illustrate the process of arriving at the Firm _LEVER_ -Score, let us consider two recent examples. In Figure 6a, we show the score calculation for Toys ‘R’ Us Inc. as of 4Q 2004. 

**Figure 6a.  Construction of the Firm** _**LEVER**_ **-Score for Toys ‘R’ Us Inc. (4Q 2004)** 

||**Median of UV**|**10**|**Toys R Us**|
|---|---|---|---|
|Firm_LEVER_-Score|||9.0|
|Valuation Score|||+++|
|Book-to-market|33%||97%|
|EV/EBITDA|9.9x||13.3x|
|Operation Score|||+++|
|Capex Growth|4.5%||-36%|
|Cash Flow yield|4%||10%|
|Execution Score|||++|
|Free cash flow variability|16%||8%|
|Market Value|$ 2bn||$ 4.4bn|



_Source: Lehman Brothers._ 

> _9 The scores are altered so that they are uniformly distributed in the universe. This enables us to effectively examine the performance of the score, as explained in Section 4.2._ 

> _10 We report the median of the universe for the cash flow yield, free cash flow variability and market value; and that of the firm’s sector peers for Book to Market, EV to EBITDA and capex growth._ 

January 9, 2006 

9 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

Toys ‘R’ Us Inc. had a much higher book to market ratio than its sector peers, making its valuation attractive for LBO investors. On the operations side, while the median capital expenditure of its sector peers rose 4.5% between 4Q 2003 and 4Q 2004, Toys ‘R’ Us posted a sharp fall, of 36%, in the same period. Still, it continued to generate a high level of cash flow yield, signaling strong fundamentals. In addition, the cash flows of the firm were much more stable than those of the sector. Although TOY was larger than the median value of the universe, it was not too large to deter an LBO acquirer. As a result of these characteristics, Toys ‘R’ Us Inc. had a high Firm _LEVER_ -Score of 9.0. 

In Figure 6b, we examine a case with a low score, that of Halliburton Co., as of 1Q 2005. 

**Figure 6b. Construction of the Firm** _**LEVER**_ **-Score for Halliburton Co. (1Q 2005)** 

||**Median of UV**|**Halliburton**|
|---|---|---|
|Firm_LEVER_-Score||0.9|
|Valuation Score||- -|
|Book-to-market|43%|20%|
|EV/EBITDA|9.9x|15.4x|
|Operation Score||- -|
|Capex Growth|7.3%|-14.8%|
|Cash Flow yield|3%|-3%|
|Execution Score||- - -|
|Free cash flow variability|21%|27%|
|Market Value|$ 2bn|$ 22bn|



_Source: Lehman Brothers._ 

Although Halliburton had a high EV to EBITDA multiple compared with its sector peers, it had a much lower book-to-market ratio. It also had worse free cash flow yields than other firms in its sector, making its operations unattractive. With respect to execution, HAL’s size and its high free cash flow variability would make an LBO transaction more difficult to complete. Halliburton therefore had a low Firm _LEVER_ -Score of 0.9 as of 1Q 2005. 

## **3.2. Macro** _**LEVER**_ **-Score** 

To construct the Macro _LEVER_ -Score, we perform a lagged regression of the number of LBOs on the following macro variables (Figure 7). 

**Figure 7.  Variables used in the construction of the Macro** _**LEVER**_ **-Score** 

|**Category**|**Variable**|
|---|---|
|_Economic Environment_|GDP Growth|
|_Yield Curve_|10 year yield change|
||2y-10y slope change|
|_Equity Markets_|S&P 500 Returns|
|_Macro Fundamentals_|S&P 500 Dividend Yield|
||S&P 500 Cash-flow Yield|
|_Financial risk_|Leverage of S&P 500|
||Credit spread changes|
|_Technicals_|Amount of private equity capital raised|



_Source: Lehman Brothers._ 

We extend the Macro _LEVER_ -Score to cover US and European firms. 

January 9, 2006 

10 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## **Interpreting the Firm** _**LEVER**_ **-Score with the Macro** _**LEVER**_ **-Score** 

While the Firm _LEVER_ -Score uses cross-sectional data, the Macro _LEVER_ -Score is produced using time-series analysis. Interpreting them together is therefore not completely obvious. To fully utilize the information from the top-down and bottom-up analyses of the two scores, investors should consider the following: 

- A high Macro _LEVER_ -Score indicates the possibility of a large amount of LBO activity in the year to come. This suggests that a greater weight should be placed on the Firm _LEVER_ -Score when it is analyzed in conjunction with traditional credit analyses based on other indicators. Conversely, when the Macro _LEVER_ -Score is low (during which periods the Firm _LEVER_ -Score would flag several credits as possible LBO candidates), investors could factor in the risk of LBOs selectively. 

- The Macro _LEVER_ -Score could be modified into a Sector Score if the underlying regression is performed on sector-specific transactions. In such a case, using the Macro _LEVER_ -Score directly with the Firm _LEVER_ -Score would be informative on a crosssectional basis for a given year. We note that this method may be difficult to implement, however, since LBO data within specific sectors may be sparse. 

## **4. PERFORMANCE OF THE** _**LEVER**_ **FRAMEWORK** 

## **4.1. Performance of the Macro** _**LEVER**_ **-Score** 

To examine the performance of the Macro _LEVER_ -Score, we need to assess if periods with high LBO activity were predicted by a high Macro _LEVER_ -Score one year ahead, and vice versa. In Figure 8, we report the one-year forecasts of the Macro _LEVER_ -Scores along with the annual number of LBO transactions. We can see that the profile of the Macro _LEVER_ - Score one year ahead tracks the overall number of LBOs reasonably well. 

**Figure 8.  Performance of the Macro** _**LEVER**_ **-Score (one year ahead) in predicting LBO volumes[11]** 

**==> picture [363 x 188] intentionally omitted <==**

**----- Start of picture text -----**<br>
30 10<br>25<br>8<br>20<br>6<br>15<br>4<br>10<br>2<br>5<br>0 0<br>1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005<br>No. of LBOs Macro LEVER-Score (one year ahead, RHS)<br>**----- End of picture text -----**<br>


_Source: Lehman Brothers._ 

> _11 Data for 2005 are until the third quarter of the year_ 

January 9, 2006 

11 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## **4.2. Performance of the Firm LEVER-Score** 

We use the concept of “performance curve” to quantify the predictive power of the Firm LEVER-Score.[12] The performance curve captures the efficacy of the score by measuring its Type I and Type II errors. In the current context, the two errors above would be defined as follows: 

**Type I Error** : Firms that are identified as having higher risk of an LBO or leveraged recapitalization do not get acquired or undergo any leveraged recapitalization. This is generally referred to as a _false positive_ error. 

**Type II Error:** Firms that are identified as having lower risk of an LBO or leveraged recapitalization actually go on to be acquired. This is generally referred to as a _false negative_ error. 

Since the actual number of LBO transactions observed in the market is far fewer than the size of the universe considered, it is natural that the Type I error described above is high. Furthermore, the credit spreads of a name identified wrongly as an LBO or leveraged recapitalization candidate might still widen because of market speculation about a potential LBO, thus alleviating the negative impact of a Type I Error. It is the Type II error that is crucial to minimize from the perspective of a credit portfolio. A high Type II error level would indicate the failure of the screen to flag high-risk names in a long credit portfolio. 

The performance curve is constructed as follows. We start with an empty rectangle and, on the horizontal axis, we mark the level of the score from right to left. Notice that, by construction, the Firm _LEVER_ -Score is uniformly distributed over the entire sample; for example, exactly 10% of the firms have a score between, say, 7 and 8. On the vertical axis, we read the percentage of LBOs out of the total number of LBOs that had a score above a given level. 

The first diagonal of our rectangle represents an important benchmark. A model for predicting LBO activity whose performance curve coincides with the first diagonal does not provide any improvement over the inexpensive strategy of predicting LBOs by randomly drawing company names from an urn. In fact, such a model will, on average, include 20% of the LBOs in a list of 20% of all names, 30% of the LBOs in a list of 30% of all names, and so on. 

An effective model has a performance curve that lies _above_ the first diagonal. The higher the power curve, the higher the model’s predictive power. A perfect model will capture 100% of the LBOs by short-listing 1% of all names in the dataset. Such a model will therefore display a power curve composed of two segments, the first one overlapping with the left short side of the rectangle, the second one overlapping with the upper long side. 

The share of firms that receive a high score from the model but are not LBOed measures the Type I error of the model. Symmetrically, the share of firms that receive low scores and are subsequently LBOed provides a measure of the model’s Type II error. The reader can verify that these errors can be quantified using the performance curve. 

A different way of looking at the performance curve is to size a “screen”, i.e. a short list, in terms of an absolute number of issuers, and then observe how many LBOs the model has been able to include in that short list one quarter before the event. We perform the following back-test of the Firm _LEVER_ -Score: For every quarter in the period 1995-2005, we perform a cross sectional analysis of the names in the S&P 1500 Index and assign a score to each name as described in Section 3. 

> _12 The performance curve is also called the “power curve” in Statistics._ 

January 9, 2006 

12 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

We then rank the names in descending order according to their scores, and analyze the top and bottom selections of the screen. If the screen were to perform well, the LBOs in the following quarter would predominantly fall in the top selection. In addition, only a small number of the LBOs would fall in the bottom selection. 

In Figure 9 we report the number of LBOs captured one quarter ahead of the event by selecting different screen sizes over the period 1995-2005. 

**Figure 9.  Performance of the Firm** _**LEVER**_ **-Score** 

|**Total no. of LBOs**<br>**Selection**|**Size of selection**|
|---|---|
||**100**<br>**150**<br>**200**|
|Top<br>32<br>Bottom|14<br>19<br>20<br>0<br>0<br>1|



_Source: Lehman Brothers._ 

During the 1995-2005 period, there were 32 LBOs in our sample[13] . The selection of the top 100 names based on the Firm _LEVER_ -Score in the previous quarter captured 14 of the names that were actually LBOed. In addition, no LBOed name was included in the list of the 100 names with the lowest Firm _LEVER_ -Score. Figure 9 also shows that   screening 150 names would have captured 19 LBOs, while 20 of the 32 LBOs would have been captured by shortlisting 200 issuers every quarter. Only one LBO was included in a list of 200 names with the lowest Firm _LEVER_ -Scores. Thus, not only is the Firm _LEVER_ -Score able to capture a substantial number of LBOs one quarter ahead; the score also succeeds in minimizing the disturbing Type II error. 

To analyze the profile of the scores and the degree of the Type I and II errors in further detail, we plot the performance curve of the Firm _LEVER_ -Score in Figure 10a. 

## **Figure 10a. Performance Curve of Firm** _**LEVER**_ **-Score** 

**==> picture [351 x 198] intentionally omitted <==**

**----- Start of picture text -----**<br>
100%<br>80%<br>60%<br>84% of the LBO Targets had<br>a Firm LEVER-Score of 5 or<br>40% more<br>20%<br>0%<br>10 9 8 7 6 5 4 3 2 1 0<br>Firm LEVER-Score (inverted axis)<br>**----- End of picture text -----**<br>


_Source: Lehman Brothers._ 

Figure 10a shows that the performance curve of the Firm _LEVER_ -Score is well above the first diagonal. Approximately 63% of the names in our sample that were LBOed had a Firm _LEVER_ -Score of 7.5 or more one quarter ahead of the transaction. This means that 63% of the LBOs were short listed in the top 25% of the names ranked according to our Firm 

> _13 Though we consider a universe of 1500 names, data on all the variables we consider are available for around 900 names, on average, every quarter._ 

January 9, 2006 

13 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

_LEVER_ -Score. In Figure 10b we report the Type I and Type II errors in our sample. Figure 8b shows that fewer than 6% of LBOed names had a score of 2.5 or less. 

**Figure 10b. Type I and II errors in the Firm** _**LEVER**_ **-Score** 

|||**LBO Names**|**Non-LBO Names**|
|---|---|---|---|
|Score above|7.5|63%|25%|
|Score below|2.5|6%|25%|



_Source: Lehman Brothers._ 

In Figure 11a below, we report the performance of the component scores. While all the component scores perform reasonably well, the Operation Score performs markedly better in terms of its Type II error. This is also evident in the performance curves shown in Figure 11b. 

**Figure 11a. Performance of the component scores[14]** 

|**% of LBO Targets**|**Valuation Score**|**Operation Score**|**Execution Score**|
|---|---|---|---|
|Score above 7.5|50%|50%|59%|
|Score below 2.5|9%|9%|19%|



_Source: Lehman Brothers._ 

**Figure 11b. Performance curves of component scores** 

**==> picture [398 x 288] intentionally omitted <==**

**----- Start of picture text -----**<br>
100% 100%<br>80% 80%<br>60% 60%<br>40% 40%<br>20% 20%<br>0% 0%<br>10 9 8 7 6 5 4 3 2 1 0 10 9 8 7 6 5 4 3 2 1 0<br>Valuation Score Operation Score<br>100%<br>80%<br>60%<br>40%<br>20%<br>0%<br>10 9 8 7 6 5 4 3 2 1 0<br>Execution Score<br>% of LBO Names % of LBO Names<br>% of LBO Names<br>**----- End of picture text -----**<br>


_Source: Lehman Brothers._ 

> _14 Given the construction of our scores and the small number of actual LBOs as compared to the size of the sample, there would be approximately 25% of the Non-LBO names above a score of 7.5 or below a score of 2.5._ 

January 9, 2006 

14 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## **5. LBO OUTLOOK 2006** 

As of January 2006, the Macro _LEVER_ -Score is strong at 8 (out of a maximum of 10). This is largely because of the large amount of capital raised by private equity firms, as well as low credit spreads and low long-term interest rates.  The environment seems broadly conducive to LBO activity. However, as we go into 2006 – if short-term rates were to increase and credit spreads to widen, the conduciveness of the macro environment could be slightly dampened. 

We present the Top 20 list of U.S. companies with releveraging exposure in Figure 12, with a complete list in Appendix A. Figures A1 and A2 present the Firm _LEVER_ -Scores of firms in the S&P 1500 that are members of the Lehman Brothers US IG and High Yield (HY) Credit Indices respectively. Figure A3 presents the Firm _LEVER_ -Scores of those firms in the S&P 1500 which are not members of the Lehman Brothers US IG or HY Credit Indices. We use accounting data as of 3Q05 to compute these Firm _LEVER_ -Scores as they are the most current information available. 

The power of the Firm _LEVER_ -Score lies in its ability to systematically screen event risk across a large universe of firms. While many of the highlighted companies have been discussed in the financial press as potential targets for LBOs or other shareholder-friendly releveraging actions, others have not. A systematic approach is not a substitute for fundamental analysis, although it does suggest where this research should be focused. 

The Firm _LEVER_ -Score also reveals potent sector-level trends, which reflect the concentration of releveraging risk in certain industries. Five sectors of the Investment Grade Credit Index – Technology, Food and Beverage, Supermarkets, Chemicals, and Media NonCable – represent 49% of Index issuers with Firm _LEVER_ -Scores above 7.0. By including Retailers, Paper, and Wirelines, this percentage increases to 58%. In the High Yield Credit Index, four sectors have high relative exposure – Paper, Retailers, Chemicals and Metals and Mining. 

We think that these scores are useful even if a firm does not eventually get taken private. News of a potential recapitalization can generate significant spread volatility for a firm. LBOs or recaps for related firms can also cause spill-over effects. Significant spread widening may occur in sympathy with potential LBO candidates in the same space. As a result, we think that Firm _LEVER_ -Scores can be used to help identify mispricing and trade opportunities for a fairly broad universe of companies. 

January 9, 2006 

15 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

**Figure 12. Issuers among those in the Lehman US Investment Grade & High Yield Credit Index with the Top 20 Firm** _**LEVER**_ **-Scores (as of 3Q05)** 

|**US IG CREDIT INDEX**|**US HYCREDIT INDEX**|
|---|---|
|**Ticker **<br>**COMPANY**<br>**Firm**<br>**_LEVER_-**<br>**Score**|**Ticker **<br>**COMPANY**<br>**Firm**<br>**_LEVER_-**<br>**Score**|
|SCHL<br>Scholastic Corp.<br>9.9<br>SVU<br>SUPERVALU Inc.<br>9.9<br>CYT<br>Cytec Industries Inc.<br>9.7<br>CTL<br>CenturyTel Inc.<br>9.7<br>PAS<br>PepsiAmericas Inc.<br>9.6<br>CPO<br>Corn Products International Inc.<br>9.5<br>CCE<br>Coca-Cola Enterprises Inc.<br>9.4<br>AET<br>Aetna Inc.<br>9.3<br>FD<br>Federated Department Stores<br>Inc.<br>9.2<br>PTV<br>Pactiv Corp.<br>9.0<br>ARW<br>Arrow Electronics Inc.<br>9.0<br>ABS<br>Albertsons Inc.<br>8.9<br>TSN<br>Tyson Foods Inc.<br>8.9<br>ROH<br>Rohm & Haas Co.<br>8.8<br>LZ<br>Lubrizol Corp.<br>8.8<br>TRB<br>Tribune Co.<br>8.6<br>KMT<br>Kennametal Inc.<br>8.5<br>CSX<br>CSX Corp.<br>8.5<br>JNY<br>Jones Apparel Group Inc.<br>8.5<br>IP<br>International Paper Co.<br>8.4|OSG<br>Overseas Shipholding Group<br>Inc.<br>10.0<br>MOVI<br>Movie Gallery Inc.<br>10.0<br>LNY<br>Landry's Restaurants Inc.<br>9.9<br>SXT<br>Sensient Technologies Corp.<br>9.9<br>BKI<br>Buckeye Technologies Inc.<br>9.8<br>BTH<br>BLYTH Inc.<br>9.8<br>STLD<br>Steel Dynamics Inc.<br>9.8<br>SAH<br>Sonic Automotive Inc.<br>9.7<br>GP<br>Georgia-Pacific Corp.<br>9.7<br>GPI<br>Group 1 Automotive Inc.<br>9.6<br>NDC<br>NDCHealth Corp.<br>9.6<br>POL<br>PolyOne Corp.<br>9.6<br>GLT<br>Glatfelter<br>9.5<br>BOW<br>Bowater Inc.<br>9.5<br>ALO<br>Alpharma Inc.<br>9.5<br>VMI<br>Valmont Industries Inc.<br>9.5<br>HCA<br>HCA Inc.<br>9.4<br>PSS<br>Payless Shoesource Inc.<br>9.3<br>LYO<br>Lyondell Chemical Co.<br>9.3<br>CENX<br>CenturyAluminum Co.<br>9.1|



_Source: Lehman Brothers._ 

## **6. CONCLUSION** 

In this article, we proposed a systematic approach to identifying issuers with heightened leveraged recapitalization risk and quantifying the overall conduciveness of the market for releveraging transactions. There are limitations to such a screen. First, it is liable to overpredict the risk of LBOs. Second, there may be important qualitative variables (e.g., openness of a firm’s management to a buy-out) that are difficult to capture in a quantitative framework. It is therefore necessary for such a screen to be complemented by a subjective analysis of the firms in the universe. Nevertheless, our historical test shows that there is value to such an approach. 

January 9, 2006 

16 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## **REFERENCES** 

Berg, Achim and Oliver Gottschalg (2004), “Understanding Value Generation in Buyouts”, Journal of Restructuring Finance, Vol.1, No2 1-29. 

Jensen, Michael (1986), “Agency Cost of Free Cash Flow, Corporate Finance and Takeovers”, _American Economic Review_ 76, 323-329. 

Jin, Li and Fiona Wang (2002), “Leveraged Buyouts: Inception, Evolution, and Future Trends”, _Perspectives_ , vol.3, No.6 

Long, William and David Ravenscraft (1993), “The Financial Performance of Whole Company LBOs”, CES 93-16 discussion paper. 

Opler, Tim and Sheridan Titman (1993), “The Determinants of Leveraged Buyout Activities: Free Cash Flow vs. Financial Distress Costs”, _Journal of Finance_ , vol XLVIII No 5, 19851999. 

Smith, Roy C. (1990), The Money Wars: The Rise & Fall of the Great Buyout Boom of the 1980s, Dutton. 

January 9, 2006 

17 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## **APPENDIX A: FIRM** _**LEVER**_ **-SCORES AS OF Q3 2005** 

## **Figure A1: Issuers in the Lehman US IG Credit Index among the names scored** 

|||||**Valuation**|**Valuation**|**Operation**|**Operation**|**Execution**|**Execution**|
|---|---|---|---|---|---|---|---|---|---|
|||**Firm****_LEVER_**||**Book to**|**EV /**|**FCF**|**Capex**|**Mkt**|**FCF**|
|**Ticker**|**COMPANY**|**Score**|**Sector No**|**Market**|**EBITDA**|**Yield**|**Growth**|**Value**|**Variability**|
|AA|Alcoa Inc.|**1.0**|4|64%|8.0|-4%|32%|21,312|32%|
|ABS|Albertsons Inc.|**8.9**|6|58%|6.5|3%|-9%|9,439|4%|
|ABT|Abbott Laboratories|**4.2**|3|22%|11.1|3%|4%|65,772|4%|
|ACS|Affiliated Computer Services Inc.|**6.6**|2|43%|8.1|7%|11%|6,786|52%|
|ADM|Archer-Daniels-Midland Co.|**6.1**|10|54%|9.3|4%|22%|16,107|13%|
|AET|Aetna Inc.|**9.3**|3|38%|9.9|6%|-10%|24,637|2%|
|AHC|Amerada Hess Corp.|**2.6**|4|43%|4.9|-3%|12%|12,792|26%|
|ALB|Albemarle Corp.|**7.8**|10|52%|9.1|3%|40%|1,758|4%|
|AMGN|Amgen Inc.|**4.2**|3|21%|18.3|4%|-2%|98,313|2%|
|AN|AutoNation Inc.|**8.1**|6|88%|8.6|7%|71%|5,220|4%|
|APA|Apache Corp.|**3.5**|4|39%|5.0|0%|13%|24,769|9%|
|APC|Anadarko Petroleum Corp.|**3.5**|4|47%|5.4|0%|11%|22,520|12%|
|ARW|Arrow Electronics Inc.|**9.0**|5|61%|9.8|15%|-27%|3,747|24%|
|ASD|American Standard Cos. Inc.|**4.3**|10|10%|9.6|5%|26%|9,780|5%|
|AT|Alltel Corp.|**3.9**|13|52%|8.3|-1%|-1%|24,932|17%|
|AVP|Avon Products Inc.|**0.3**|6|7%|9.8|3%|54%|12,377|63%|
|AVY|Avery Dennison Corp.|**6.2**|10|31%|9.3|2%|-11%|5,252|7%|
|AZO|AutoZone Inc.|**5.8**|6|6%|7.4|6%|15%|6,372|5%|
|BA|Boeing Co.|**1.0**|13|18%|14.0|7%|32%|52,362|30%|
|BAX|Baxter International Inc.|**7.1**|3|18%|12.9|5%|-29%|24,854|0%|
|BDK|Black & Decker Corp.|**3.0**|8|24%|7.8|6%|15%|6,444|72%|
|BHI|Baker Hughes Inc.|**2.1**|10|22%|13.3|2%|-14%|20,399|10%|
|BLS|BellSouth Corp.|**6.7**|13|50%|7.1|2%|0%|48,155|3%|
|BMS|Bemis Co. Inc.|**7.6**|10|52%|7.6|4%|26%|2,601|13%|
|BMY|Bristol-Myers Squibb Co.|**4.7**|3|24%|9.5|-2%|-28%|47,085|18%|
|BNI|Burlington Northern Santa Fe Corp.|**7.4**|9|45%|7.5|4%|-12%|22,314|2%|
|BR|Burlington Resources Inc.|**4.3**|4|26%|7.4|5%|-17%|30,742|9%|
|BSX|Boston Scientific Corp.|**2.0**|3|20%|8.7|4%|46%|19,151|24%|
|BUD|Anheuser-Busch Cos. Inc.|**2.4**|6|10%|9.4|2%|10%|33,413|3%|
|CAG|ConAgra Foods Inc.|**3.4**|6|39%|9.7|0%|8%|12,837|7%|
|CAT|Caterpillar Inc.|**0.5**|10|21%|10.8|-16%|20%|39,962|26%|
|CBE|Cooper Industries Inc.|**2.8**|10|38%|11.3|3%|29%|6,335|19%|
|CCE|Coca-Cola Enterprises Inc.|**9.4**|6|62%|7.9|8%|-14%|9,233|4%|
|CCL|Carnival Corp.|**0.8**|6|42%|13.8|1%|43%|40,384|16%|
|CCU|Clear Channel Communications Inc.|**7.3**|6|49%|11.3|5%|-5%|17,778|1%|
|CD|Cendant Corp.|**2.0**|6|53%|7.6|1%|51%|21,143|47%|
|CL|Colgate-Palmolive Co.|**1.8**|6|5%|12.0|3%|15%|27,348|1%|
|CLX|Clorox Co.|**1.0**|6|-6%|10.8|2%|-14%|8,370|84%|
|CMCSA|Comcast Corp.|**6.7**|6|65%|9.6|3%|-12%|63,521|6%|
|CNF|CNF Inc.|**6.1**|9|30%|6.8|1%|10%|2,740|2%|
|COP|ConocoPhillips|**3.6**|4|50%|4.3|1%|54%|100,299|9%|
|COST|Costco Wholesale Corp.|**3.8**|6|44%|10.2|3%|-1%|20,359|23%|
|CPB|Campbell Soup Co.|**2.7**|6|10%|10.2|3%|5%|12,138|7%|
|CPO|Corn Products International Inc.|**9.5**|10|83%|6.9|4%|25%|1,462|5%|
|CSC|Computer Sciences Corp.|**8.1**|2|72%|5.0|8%|21%|8,751|37%|
|CSX|CSX Corp.|**8.5**|9|77%|6.8|2%|-3%|10,097|0%|
|CTL|CenturyTel Inc.|**9.7**|13|77%|5.9|11%|2%|4,582|3%|
|CTX|Centex Corp.|**4.7**|8|57%|7.8|-18%|-21%|8,249|9%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

18 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|||**Firm****_LEVER_**||**Book to**|**EV /**|**FCF**|**Capex**|||
|---|---|---|---|---|---|---|---|---|---|
|**Ticker**|**COMPANY**|**Score**|**Sector No**|**Market**|**EBITDA**|**Yield**|**Growth**|**Mkt Value FCF Variability**||
|CVG|Convergys Corp.|8.3|2|68%|6.1|-2%|-10%|2,007|25%|
|CVS|CVS Corp.|1.5|6|33%|11.1|-3%|20%|23,616|5%|
|CVX|Chevron Corp.|3.8|4|41%|5.6|5%|12%|145,318|21%|
|CYT|Cytec Industries Inc.|9.7|10|61%|8.7|6%|-5%|2,000|0%|
|DD|E.I. DuPont de Nemours & Co.|2.5|10|30%|9.2|-1%|-28%|38,976|37%|
|DE|Deere & Co.|5.0|10|47%|9.3|-2%|19%|14,761|5%|
|DELL|Dell Inc.|0.9|13|7%|16.0|6%|-21%|82,593|415%|
|DGX|Quest Diagnostics Inc.|7.9|3|28%|9.5|5%|1%|10,199|4%|
|DHR|Danaher Corp.|1.9|10|30%|12.8|6%|44%|16,585|29%|
|DIS|Walt Disney Co.|6.4|6|54%|4.7|4%|33%|48,434|10%|
|DLX|Deluxe Corp.|4.9|1|-5%|6.7|3%|99%|2,036|3%|
|DOV|Dover Corp.|2.8|10|40%|12.2|4%|11%|8,267|52%|
|DOW|Dow Chemical Co.|6.4|10|36%|6.0|5%|21%|40,217|9%|
|DVN|Devon Energy Corp.|5.8|4|46%|5.5|3%|20%|30,497|1%|
|EAT|Brinker International Inc.|7.2|6|31%|7.3|5%|1%|3,232|13%|
|EDS|Electronic Data Systems Corp.|8.2|2|64%|8.1|4%|-5%|11,689|11%|
|EFX|Equifax Inc.|6.0|1|15%|10.1|6%|13%|4,535|6%|
|EMN|Eastman Chemical Co.|8.1|10|42%|5.1|3%|8%|3,822|8%|
|EMR|Emerson Electric Co.|3.5|10|25%|11.5|3%|22%|29,485|1%|
|ETN|Eaton Corp.|5.7|10|39%|8.0|5%|21%|9,405|20%|
|FD|Federated Department Stores Inc.|9.2|6|58%|6.8|10%|-9%|11,493|10%|
|FDX|FedEx Corp.|1.7|9|38%|7.3|2%|26%|26,404|28%|
|FO|Fortune Brands Inc.|0.6|8|30%|13.5|3%|25%|11,883|24%|
|GCI|Gannett Co. Inc.|7.8|6|46%|9.4|6%|-1%|16,600|2%|
|GD|General Dynamics Corp.|3.8|13|33%|11.2|6%|19%|24,059|8%|
|GE|General Electric Co.|3.0|10|32%|14.7|5%|34%|355,763|1%|
|GIS|General Mills Inc.|6.8|6|30%|9.1|6%|-22%|17,111|7%|
|GPS|Gap Inc.|3.6|6|35%|6.0|6%|43%|15,358|113%|
|GR|Goodrich Corp.|2.9|13|27%|10.1|2%|22%|5,450|7%|
|GTK|GTECH Holdings Corp.|5.8|6|22%|9.1|4%|6%|3,970|4%|
|HAL|Halliburton Co.|0.3|10|15%|14.9|-3%|12%|35,151|26%|
|HD|Home Depot Inc.|0.9|6|31%|8.3|1%|16%|81,734|172%|
|HET|Harrah's Entertainment Inc.|0.7|6|49%|14.0|-7%|61%|11,980|15%|
|HLT|Hilton Hotels Corp.|3.3|6|32%|11.2|0%|-12%|8,514|9%|
|HON|Honeywell International Inc.|5.8|10|36%|10.1|3%|-4%|31,603|4%|
|HPQ|Hewlett-Packard Co.|2.7|13|45%|12.6|6%|7%|83,746|49%|
|HRB|H&R Block Inc.|5.1|6|23%|6.4|4%|21%|7,892|11%|
|HRL|Hormel Foods Corp.|4.6|6|33%|9.5|5%|20%|4,543|14%|
|HRS|Harris Corp.|2.7|13|27%|14.8|5%|1%|5,550|19%|
|HSY|Hershey Co.|0.7|6|7%|13.1|0%|-17%|13,644|41%|
|HUG|Hughes Supply Inc.|7.2|5|61%|10.0|7%|55%|2,174|13%|
|HUM|Humana Inc.|4.2|3|30%|13.8|9%|13%|7,793|26%|
|IBM|International Business Machines Corp.|5.9|2|24%|8.4|6%|-1%|126,709|13%|
|IP|International Paper Co.|8.4|10|61%|8.6|5%|8%|14,614|6%|
|IR|Ingersoll-Rand Co. Ltd.|5.4|10|44%|9.7|3%|1%|12,648|15%|
|ITT|ITT Industries Inc.|2.5|10|24%|12.0|4%|7%|10,491|20%|
|ITW|Illinois Tool Works Inc.|3.7|10|32%|9.5|5%|9%|23,094|35%|
|JBL|Jabil Circuit Inc.|1.7|13|34%|12.8|5%|60%|6,323|26%|
|JNJ|Johnson & Johnson|3.6|3|20%|11.7|3%|-4%|188,259|16%|
|JNY|Jones Apparel Group Inc.|8.5|6|80%|8.0|11%|6%|3,335|48%|
|JWN|Nordstrom Inc.|4.1|6|21%|9.4|4%|-9%|9,393|20%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

19 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|||**Firm****_LEVER_**||**Book to**|**EV /**|**FCF**|**Capex**|||
|---|---|---|---|---|---|---|---|---|---|
|**Ticker**|**COMPANY**|**Score**|**Sector No**|**Market**|**EBITDA**|**Yield**|**Growth**|**Mkt Value FCF Variability**||
|K|Kellogg Co.|2.1|6|14%|10.5|3%|13%|19,093|6%|
|KMB|Kimberly-Clark Corp.|5.1|6|22%|9.3|4%|-39%|27,967|8%|
|KMT|Kennametal Inc.|8.5|10|54%|7.8|4%|37%|1,886|5%|
|KO|Coca-Cola Co.|0.9|6|16%|13.4|4%|-7%|102,683|62%|
|KR|Kroger Co.|7.6|6|26%|7.1|6%|-13%|14,887|6%|
|LH|Laboratory Corp. of America Holdings|7.1|3|33%|8.9|6%|14%|6,508|9%|
|LLY|Eli Lilly & Co.|0.2|3|19%|14.5|-2%|11%|60,832|25%|
|LMT|Lockheed Martin Corp.|3.5|13|29%|9.4|8%|12%|26,617|28%|
|LOW|Lowe's Cos.|1.9|6|26%|10.4|1%|16%|50,232|4%|
|LTD|Limited Brands Inc.|0.7|6|27%|7.6|-4%|34%|8,197|98%|
|LUV|Southwest Airlines Co.|2.9|9|57%|9.5|6%|43%|11,772|56%|
|LZ|Lubrizol Corp.|8.8|10|53%|8.0|7%|51%|2,946|4%|
|MAR|Marriott International Inc.|0.9|6|25%|14.8|1%|-14%|13,127|62%|
|MAS|Masco Corp.|5.5|10|38%|8.8|5%|14%|13,074|16%|
|MCD|McDonald's Corp.|4.9|6|34%|9.5|4%|9%|42,147|5%|
|MCK|McKesson Corp.|3.7|5|40%|10.6|20%|16%|14,615|278%|
|MDC|M.D.C. Holdings Inc.|1.4|8|50%|5.7|-12%|341%|3,517|26%|
|MDT|Medtronic Inc.|0.2|3|16%|17.7|2%|9%|64,827|54%|
|MHK|Mohawk Industries Inc.|5.6|8|55%|8.2|3%|-7%|5,368|19%|
|MMM|3M Co.|1.3|10|18%|9.9|4%|38%|55,749|27%|
|MO|Altria Group Inc.|2.1|6|23%|9.4|1%|-3%|153,334|12%|
|MON|Monsanto Co.|4.7|10|33%|12.7|8%|10%|16,829|13%|
|MOT|Motorola Inc.|5.8|13|29%|9.1|3%|-25%|54,872|0%|
|MRK|Merck & Co. Inc.|7.2|3|30%|6.7|5%|-10%|59,581|37%|
|MRO|Marathon Oil Corp.|2.7|4|42%|5.5|2%|18%|25,261|18%|
|MUR|Murphy Oil Corp.|5.2|4|36%|5.2|-2%|0%|9,252|1%|
|MWV|MeadWestvaco Corp.|6.7|10|70%|7.2|-2%|4%|5,012|17%|
|NBL|Noble Energy Inc.|1.9|4|34%|7.6|4%|25%|8,216|21%|
|NBR|Nabors Industries Ltd.|1.9|10|31%|12.3|1%|54%|11,330|4%|
|NCR|NCR Corp.|6.7|13|38%|9.1|7%|6%|5,862|9%|
|NEM|Newmont Mining Corp.|0.9|4|40%|12.0|0%|42%|21,075|7%|
|NOC|Northrop Grumman Corp.|8.4|13|88%|8.2|6%|6%|19,278|8%|
|NSC|Norfolk Southern Corp.|5.3|9|54%|8.3|6%|45%|16,484|7%|
|NUE|NuCor Corp.|5.9|4|45%|4.1|15%|33%|9,180|79%|
|NWL|Newell Rubbermaid Inc.|5.6|8|28%|10.0|6%|-59%|6,217|13%|
|NYT|New York Times Co.|3.1|6|35%|9.1|0%|27%|4,318|8%|
|ODP|Office Depot Inc.|0.7|6|32%|12.0|2%|85%|9,141|14%|
|OXY|Occidental Petroleum Corp.|4.6|4|41%|4.9|6%|15%|34,343|47%|
|PAS|PepsiAmericas Inc.|9.6|6|52%|8.2|8%|-23%|3,059|3%|
|PBG|Pepsi Bottling Group Inc.|7.5|6|30%|7.1|7%|11%|6,909|5%|
|PBI|Pitney Bowes Inc.|3.2|10|14%|9.5|1%|11%|9,522|4%|
|PEP|PepsiCo Inc.|1.5|6|15%|12.7|3%|3%|94,195|9%|
|PG|Procter & Gamble Co.|0.8|6|10%|13.0|3%|20%|141,376|7%|
|PNR|Pentair Inc.|5.7|10|42%|10.8|2%|12%|3,719|6%|
|PTV|Pactiv Corp.|9.0|10|35%|8.0|6%|-11%|2,514|6%|
|PX|Praxair Inc.|6.0|10|25%|9.9|3%|-32%|15,448|4%|
|Q|Qwest Communications International Inc.|6.9|13|-36%|6.0|5%|-17%|7,617|5%|
|RIG|Transocean Inc.|2.3|10|41%|20.8|3%|-74%|20,237|50%|
|ROH|Rohm & Haas Co.|8.8|10|42%|7.4|6%|-5%|9,111|7%|
|ROK|Rockwell Automation Inc.|4.8|13|17%|10.6|4%|-2%|9,506|0%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

20 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|||**Firm****_LEVER_**||**Book to**|**EV /**|**FCF**|**Capex**|||
|---|---|---|---|---|---|---|---|---|---|
|**Ticker**|**COMPANY**|**Score**|**Sector No**|**Market**|**EBITDA**|**Yield**|**Growth**|**Mkt Value FCF Variability**||
|RRD|R.R. Donnelley & Sons Co.|8.0|1|49%|7.9|3%|31%|8,055|1%|
|RSG|Republic Services Inc.|7.4|10|33%|8.4|5%|4%|4,933|6%|
|RSH|RadioShack Corp.|3.0|6|15%|6.9|2%|21%|3,339|18%|
|RTN|Raytheon Co.|8.3|13|62%|10.2|10%|-15%|16,984|6%|
|S|Sprint Nextel Corp.|5.6|13|74%|9.7|6%|138%|69,269|2%|
|SCHL|Scholastic Corp.|9.9|6|60%|6.9|9%|-27%|1,533|7%|
|SGP|Schering-Plough Corp.|2.3|3|19%|24.6|-2%|-30%|31,112|5%|
|SII|Smith International Inc.|2.5|10|22%|10.3|1%|13%|6,675|13%|
|SLE|Sara Lee Corp.|4.1|6|16%|8.9|3%|-16%|14,393|11%|
|SON|Sonoco Products Co.|7.6|10|46%|7.5|2%|5%|2,707|10%|
|SPLS|Staples Inc.|1.7|6|26%|10.5|5%|17%|15,662|31%|
|SUN|Sunoco Inc.|2.3|4|20%|5.9|9%|96%|10,332|18%|
|SVU|SUPERVALU Inc.|9.9|6|61%|6.2|12%|-18%|4,238|3%|
|SWK|Stanley Works|2.8|8|35%|9.0|5%|21%|3,903|32%|
|SWY|Safeway Inc.|6.5|6|41%|7.7|6%|30%|11,502|5%|
|SYY|Sysco Corp.|1.8|5|14%|11.2|3%|-5%|19,530|26%|
|T|AT&T Inc.|5.9|13|51%|7.1|2%|-2%|78,652|9%|
|TAP|Molson Coors Brewing Co.|5.7|6|98%|9.6|0%|-12%|5,463|37%|
|TGT|Target Corp.|2.3|6|29%|10.4|0%|0%|45,942|7%|
|TIN|Temple-Inland Inc.|5.8|10|46%|12.9|5%|66%|4,585|1%|
|TMO|Thermo Electron Corp.|1.4|13|55%|13.1|0%|8%|5,011|208%|
|TRB|Tribune Co.|8.6|6|63%|7.8|5%|12%|10,487|1%|
|TSG|Sabre Holdings Corp.|8.1|1|63%|9.7|6%|9%|2,661|36%|
|TSN|Tyson Foods Inc.|8.9|6|73%|7.5|6%|20%|6,408|2%|
|TWX|Time Warner Inc.|8.0|6|75%|7.1|4%|10%|84,704|3%|
|TXT|Textron Inc.|4.6|10|34%|11.1|4%|0%|9,494|14%|
|UNH|UnitedHealth Group Inc.|4.3|3|16%|13.5|6%|-1%|70,587|12%|
|UNP|Union Pacific Corp.|4.1|9|70%|8.9|-2%|7%|18,982|11%|
|UPS|United Parcel Service Inc.|0.6|9|22%|10.8|2%|9%|76,181|31%|
|UST|UST Inc.|1.0|6|1%|8.3|2%|56%|6,847|17%|
|UTX|United Technologies Corp.|2.4|10|30%|10.0|4%|50%|52,807|15%|
|UVN|Univision Communications Inc.|3.5|6|63%|15.0|4%|113%|8,197|7%|
|VAL|Valspar Corp.|7.2|10|45%|9.7|4%|20%|2,265|10%|
|VFC|VF Corp.|6.6|6|43%|7.5|6%|-6%|6,428|61%|
|VLO|Valero Energy Corp.|3.0|4|39%|7.2|9%|32%|34,859|20%|
|VMC|Vulcan Materials Co.|1.3|4|29%|11.6|2%|5%|7,557|18%|
|VZ|Verizon Communications Inc.|5.2|13|43%|4.3|2%|12%|90,387|10%|
|WFT|Weatherford International Ltd.|2.6|10|46%|16.1|0%|3%|11,934|12%|
|WHR|Whirlpool Corp.|2.8|8|37%|5.4|1%|21%|5,077|42%|
|WLP|WellPoint Inc.|5.0|3|45%|13.8|6%|24%|46,713|5%|
|WMI|Waste Management Inc.|8.0|10|39%|7.9|4%|5%|15,838|0%|
|WMT|Wal-Mart Stores Inc.|1.9|6|26%|9.6|0%|22%|182,409|2%|
|WPO|Washington Post Co.|0.9|6|33%|10.9|3%|63%|7,702|39%|
|WWY|WM. Wrigley Jr. Co.|0.2|6|14%|18.2|1%|0%|16,121|232%|
|WY|Weyerhaeuser Co.|5.2|4|60%|7.0|3%|-19%|16,993|15%|
|WYE|Wyeth|4.4|3|18%|11.5|0%|-34%|62,095|7%|
|XOM|Exxon Mobil Corp.|2.6|4|27%|6.1|7%|-7%|395,371|231%|
|XTO|XTO Energy Inc.|0.2|4|22%|9.3|-9%|124%|16,458|6%|
|YUM|Yum! Brands Inc.|3.0|6|12%|9.3|5%|-3%|13,748|25%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

21 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

## **Figure A2: Issuers in the Lehman US HY Credit Index among the names scored** 

|||||**Valuation**|**Valuation**|**Operation**|**Operation**|**Execution**|**Execution**|
|---|---|---|---|---|---|---|---|---|---|
|||**Firm****_LEVER_**||**Book to**|**EV /**|**FCF**|**Capex**|**Mkt**||
|**Ticker**|**COMPANY**|**Score**|**Sector No**|**Market**|**EBITDA**|**Yield**|**Growth**|**Value**|**FCF Variability**|
|ACI|Arch Coal Inc.|**0.2**|4|27%|16.7|-1%|121%|4,367|14%|
|AH|Armor Holdings Inc.|**4.4**|13|44%|7.8|2%|124%|1,501|17%|
|ALO|Alpharma Inc.|**9.5**|3|64%|6.8|15%|16%|1,330|10%|
|AM|American Greetings Corp.|**8.6**|6|73%|7.8|14%|28%|1,801|23%|
|AMD|Advanced Micro Devices Inc.|**0.4**|13|29%|9.1|-3%|153%|10,129|27%|
|AOI|Alliance One International Inc.|**7.5**|6|166%|16.4|-12%|-19%|336|12%|
|ARG|Airgas Inc.|**5.2**|10|39%|8.7|2%|85%|2,277|5%|
|ARM|ArvinMeritor Inc.|**8.2**|10|74%|8.1|-18%|-18%|1,175|16%|
|ARS|Aleris International Inc.|**4.7**|4|48%|6.4|3%|115%|853|14%|
|ATI|Allegheny Technologies Inc.|**3.7**|4|24%|9.1|4%|-33%|3,025|27%|
|ATK|Alliant Techsystems Inc.|**6.3**|13|26%|9.5|8%|9%|2,736|11%|
|AVT|Avnet Inc.|**8.5**|5|72%|12.1|8%|-5%|3,567|11%|
|AW|Allied Waste Industries Inc.|**8.6**|10|89%|6.8|-2%|19%|2,794|2%|
|AXE|Anixter International Inc.|**7.1**|5|44%|10.3|1%|-44%|1,541|18%|
|AZR|Aztar Corp.|**7.1**|6|57%|9.1|0%|9%|1,099|8%|
|BGG|Briggs & Stratton Corp.|**2.9**|8|50%|6.9|2%|49%|1,794|72%|
|BKI|Buckeye Technologies Inc.|**9.8**|10|91%|8.1|4%|28%|305|0%|
|BLL|Ball Corp.|**3.9**|10|23%|7.6|5%|43%|3,860|40%|
|BOW|Bowater Inc.|**9.5**|10|87%|8.7|1%|-61%|1,622|3%|
|BTH|BLYTH Inc.|**9.8**|6|55%|6.8|8%|5%|914|6%|
|BTU|Peabody Energy Corp.|**0.4**|4|18%|16.3|0%|70%|11,085|5%|
|BWS|Brown Shoe Co. Inc.|**8.4**|6|66%|7.4|4%|47%|608|11%|
|BYD|Boyd Gaming Corp.|**0.9**|6|28%|9.9|-5%|230%|3,846|9%|
|CBB|Cincinnati Bell Inc.|**9.0**|13|-77%|7.1|14%|6%|1,086|0%|
|CEM|Chemtura Corp.|**7.0**|10|64%|12.4|-4%|-26%|2,980|3%|
|CENX|Century Aluminum Co.|**9.1**|4|61%|8.5|20%|-19%|723|15%|
|CHB|Champion Enterprises Inc.|**1.8**|8|12%|19.2|4%|41%|1,122|15%|
|CHD|Church & Dwight Co.|**6.8**|6|29%|11.3|5%|9%|2,376|0%|
|CHE|Chemed Corp.|**6.8**|3|34%|11.7|5%|64%|1,116|7%|
|CKH|SEACOR Holdings Inc.|**4.1**|10|71%|11.1|-6%|24%|1,815|33%|
|CMI|Cummins Inc.|**9.1**|10|45%|4.8|10%|36%|3,951|3%|
|CSAR|Caraustar Industries Inc.|**8.9**|10|69%|10.2|0%|4%|316|6%|
|CVH|Coventry Health Care Inc.|**2.9**|3|26%|11.7|8%|12%|9,316|120%|
|CYH|Community Health Systems Inc.|**6.3**|3|39%|9.6|5%|103%|3,473|10%|
|CZN|Citizens Communications Co.|**6.1**|13|25%|7.4|5%|-1%|4,534|15%|
|DDS|Dillard's Inc.|**7.0**|6|135%|6.2|-8%|18%|1,723|19%|
|DF|Dean Foods Co.|**6.2**|6|38%|9.6|8%|22%|5,539|9%|
|DG|Dollar General Corp.|**2.3**|6|28%|8.2|4%|76%|5,887|19%|
|DNR|Denbury Resources Inc.|**0.3**|4|23%|10.2|-5%|26%|2,889|58%|
|DRS|DRS Technologies Inc.|**8.2**|13|52%|10.0|6%|38%|1,383|3%|
|DY|Dycom Industries Inc.|**5.0**|10|56%|7.4|2%|83%|988|454%|
|DYN|Dynegy Inc.|**6.2**|5|92%|64.7|-29%|-7%|1,883|1%|
|EK|Eastman Kodak Co.|**3.2**|8|33%|5.5|0%|-9%|6,983|52%|
|EMMS|Emmis Communications Corp.|**8.2**|6|10%|14.9|12%|-13%|814|0%|
|ESL|Esterline Technologies Corp.|**8.8**|13|63%|9.9|5%|29%|959|4%|
|FCX|Freeport-McMoRan Copper & Gold Inc.|**3.8**|4|4%|5.4|8%|1%|8,943|46%|
|FL|Foot Locker Inc.|**5.7**|6|55%|6.5|0%|5%|3,442|36%|
|FSH|Fisher Scientific International Inc.|**6.6**|3|55%|10.8|5%|16%|7,601|11%|
|FST|Forest Oil Corp.|**7.5**|4|47%|6.0|9%|-45%|3,235|59%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

22 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|||**Firm****_LEVER_**||**Book to**|**EV /**|**FCF**|**Capex**|||
|---|---|---|---|---|---|---|---|---|---|
|**Ticker**|**COMPANY**|**Score**|**Sector No**|**Market**|**EBITDA**|**Yield**|**Growth**|**Mkt Value FCF Variability**||
|FTO|Frontier Oil Corp.|2.2|4|19%|6.6|9%|38%|2,507|137%|
|GLT|Glatfelter|9.5|10|67%|7.2|-3%|-72%|621|8%|
|GM|General Motors Corp.|3.7|8|130%|12.2|-117%|16%|17,310|2%|
|GNCMA|General Communication Inc.|7.7|13|44%|7.2|1%|79%|544|0%|
|GP|Georgia-Pacific Corp.|9.7|10|73%|6.2|9%|0%|8,825|4%|
|GPI|Group 1 Automotive Inc.|9.6|6|93%|8.0|9%|37%|674|6%|
|GRP|Grant Prideco Inc.|1.3|10|17%|16.4|3%|-9%|5,226|34%|
|GT|Goodyear Tire & Rubber Co.|6.8|8|11%|4.5|11%|38%|2,744|10%|
|HC|Hanover Compressor Co.|8.4|10|65%|9.4|-2%|-36%|1,414|10%|
|HCA|HCA Inc.|9.4|3|29%|7.2|6%|-18%|21,692|2%|
|HET|Harrah's Entertainment Inc.|0.7|6|49%|14.0|-7%|61%|11,980|15%|
|HNT|Health Net Inc.|6.7|3|28%|11.1|4%|-31%|5,413|42%|
|HOT|Starwood Hotels & Resorts Worldwide Inc.|4.8|6|43%|13.5|3%|8%|12,536|1%|
|HPC|Hercules Inc.|6.0|10|5%|7.9|5%|60%|1,378|7%|
|JCP|J.C. Penney Co. Inc.|3.1|6|36%|8.4|-4%|-9%|12,140|25%|
|KMG|Kerr-McGee Corp.|3.3|4|12%|6.6|11%|29%|11,263|10%|
|KSU|Kansas City Southern|2.5|9|74%|17.6|-1%|48%|1,908|11%|
|KTO|K2 Inc.|7.5|8|129%|7.4|-7%|75%|535|5%|
|LEA|Lear Corp.|7.0|10|77%|6.2|-7%|14%|2,282|18%|
|LFB|Longview Fibre Co.|8.1|10|46%|8.8|5%|92%|995|7%|
|LLL|L-3 Communications Holdings Inc.|6.3|13|45%|13.2|7%|-3%|9,491|7%|
|LNY|Landry's Restaurants Inc.|9.9|6|81%|9.0|5%|-32%|633|2%|
|LYO|Lyondell Chemical Co.|9.3|10|39%|6.4|13%|-69%|7,067|13%|
|MEE|Massey Energy Co.|0.2|4|23%|13.6|-2%|111%|3,928|15%|
|MOVI|Movie Gallery Inc.|10.0|6|101%|3.7|7%|-68%|329|457%|
|MRD|MacDermid Inc.|8.6|10|40%|8.7|4%|-1%|803|18%|
|MTW|Manitowoc Co.|5.1|10|35%|10.3|2%|39%|1,520|7%|
|MYG|Maytag Corp.|3.3|8|-7%|10.0|0%|-53%|1,464|20%|
|MZ|Milacron Inc.|3.0|10|-118%|10.3|-3%|35%|89|18%|
|NAV|Navistar International Corp.|8.3|10|30%|7.5|8%|12%|2,273|10%|
|NDC|NDCHealth Corp.|9.6|3|46%|13.5|12%|-34%|685|27%|
|NFX|Newfield Exploration Co.|1.5|4|34%|6.8|4%|61%|6,246|24%|
|OCR|Omnicare Inc.|5.4|3|36%|17.5|3%|5%|5,993|0%|
|OMG|OM Group Inc.|6.4|10|89%|6.7|1%|69%|582|417%|
|OMN|Omnova Solutions Inc.|4.0|10|25%|10.7|-4%|34%|180|16%|
|OSG|Overseas Shipholding Group Inc.|10.0|9|77%|4.8|18%|-32%|2,301|9%|
|OXM|Oxford Industries Inc.|4.3|6|42%|7.7|-1%|133%|769|19%|
|PKG|Packaging Corp. of America|8.3|10|38%|9.2|4%|-4%|2,099|5%|
|PNK|Pinnacle Entertainment Inc.|1.6|6|56%|15.8|-35%|153%|750|22%|
|POL|PolyOne Corp.|9.6|10|72%|7.9|-6%|-18%|557|1%|
|PPP|Pogo Producing Co.|5.3|4|59%|7.0|11%|20%|3,531|83%|
|PSS|Payless Shoesource Inc.|9.3|6|55%|6.6|14%|-3%|1,187|52%|
|PVH|Phillips-Van Heusen Corp.|8.4|6|40%|7.8|6%|36%|1,300|5%|
|PXD|Pioneer Natural Resources Co.|4.9|4|29%|7.1|3%|-6%|7,327|1%|
|PXP|Plains Exploration & Production Co.|0.1|4|19%|-24.1|-2%|76%|3,355|26%|
|RAI|Reynolds American Inc.|5.9|6|51%|2.9|3%|31%|12,238|19%|
|RCI|Renal Care Group Inc.|3.9|3|22%|10.6|2%|62%|3,234|3%|
|RML|Russell Corp.|8.7|6|127%|6.8|-5%|-8%|464|48%|
|RT|Ryerson Tull Inc.|7.8|4|99%|7.0|6%|68%|538|20%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

23 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|||**Firm****_LEVER_**||**Book to**|**EV /**|**FCF**|**Capex**|||
|---|---|---|---|---|---|---|---|---|---|
|**Ticker**|**COMPANY**|**Score**|**Sector No**|**Market**|**EBITDA**|**Yield**|**Growth**|**Mkt Value FCF Variability**||
|S|Sprint Nextel Corp.|5.6|13|74%|9.7|6%|138%|69,269|2%|
|SAH|Sonic Automotive Inc.|9.7|6|89%|9.6|14%|9%|930|3%|
|SFD|Smithfield Foods Inc.|8.3|6|58%|7.1|2%|6%|3,297|2%|
|SFY|Swift Energy Co.|5.6|4|43%|5.6|4%|37%|1,313|22%|
|SKS|Saks Inc.|7.9|6|81%|6.4|4%|14%|2,625|30%|
|STLD|Steel Dynamics Inc.|9.8|4|56%|3.8|11%|-26%|1,464|15%|
|STR|Questar Corp.|1.2|5|18%|11.1|-3%|38%|7,515|5%|
|STZ|Constellation Brands Inc.|6.9|6|49%|10.7|5%|20%|5,744|1%|
|SXT|Sensient Technologies Corp.|9.9|10|73%|8.6|6%|-33%|892|8%|
|TKR|Timken Co.|6.0|10|51%|5.8|1%|33%|2,739|23%|
|TRI|Triad Hospitals Inc.|6.6|3|73%|8.0|1%|55%|3,898|6%|
|TXI|Texas Industries Inc.|5.6|4|30%|5.9|35%|23%|1,244|79%|
|UIS|Unisys Corp.|6.0|2|-6%|11.7|11%|-45%|2,266|30%|
|UNH|UnitedHealth Group Inc.|4.3|3|16%|13.5|6%|-1%|70,587|12%|
|USPI|United Surgical Partners Inc.|8.7|3|30%|12.2|5%|-43%|1,729|17%|
|VMI|Valmont Industries Inc.|9.5|10|44%|8.0|10%|-3%|720|22%|
|VPI|Vintage Petroleum Inc.|1.2|4|26%|7.1|0%|76%|3,061|8%|
|VRX|Valeant Pharmaceuticals International|2.6|3|26%|15.6|0%|51%|1,860|1%|
|VTRU|Vertrue Inc.|5.5|1|-10%|6.7|4%|44%|353|24%|
|WLV|Wolverine Tube Inc.|4.1|10|174%|39.8|-13%|89%|113|15%|
|WMB|Williams Cos.|5.3|10|36%|11.3|2%|-18%|14,351|3%|
|X|United States Steel Corp.|8.6|4|93%|3.2|11%|83%|4,802|14%|
|XRX|Xerox Corp.|8.9|13|50%|8.0|10%|4%|13,109|0%|
|ZQK|Quiksilver Inc.|2.1|6|40%|13.9|3%|59%|1,750|19%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

24 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

**Figure A3: Firm** _**LEVER**_ **-Scores for firms which are not issuers in the Lehman IG or HY Credit Index** 

|||||**Valuation**|**Valuation**|**Operation**|**Operation**|**Execution**|**Execution**|
|---|---|---|---|---|---|---|---|---|---|
|||**Firm****_LEVER_**||**Book to**||**FCF**|**Capex**|**Mkt**||
|**Ticker**|**COMPANY**|**Score**|**Sector No**|**Market**|**EV / EBITDA**|**Yield**|**Growth**|**Value**|**FCF Variability**|
|206488|AT&T|**9.6**|13|50%|3.8|13%|-42%|15,900|4%|
|A|Agilent Technologies Inc.|**1.8**|13|24%|20.7|4%|-42%|16,179|33%|
|AAI|AirTran Holdings Inc.|**3.0**|9|31%|33.8|2%|-29%|1,112|29%|
|AAP|Advance Auto Parts Inc.|**1.3**|6|22%|9.3|4%|78%|4,217|29%|
|ABFS|Arkansas Best Corp.|**7.6**|9|60%|4.0|4%|17%|880|165%|
|ACLS|Axcelis Technologies Inc.|**6.6**|13|82%|14.1|2%|11%|527|19%|
|ACO|AMCOL International Corp.|**1.5**|4|43%|9.6|-2%|37%|568|105%|
|ACXM|Acxiom Corp.|**9.4**|2|39%|6.6|14%|-8%|1,593|27%|
|AD|Advo Inc.|**6.1**|1|19%|9.6|0%|23%|983|2%|
|ADPT|Adaptec Inc.|**3.6**|13|85%|63.1|-8%|63%|434|15%|
|ADS|Alliance Data Systems Corp.|**4.4**|2|30%|12.0|6%|3%|3,159|151%|
|ADTN|Adtran Inc.|**2.0**|13|21%|17.0|3%|6%|2,393|24%|
|AEIS|Advanced Energy Industries Inc.|**6.3**|13|52%|17.8|5%|-32%|477|464%|
|AG|AGCO Corp.|**7.8**|10|93%|6.5|-1%|0%|1,647|45%|
|AGN|Allergan Inc.|**2.2**|3|11%|17.8|3%|-12%|12,057|21%|
|AHG|Apria Healthcare Group Inc.|**9.4**|3|30%|6.7|5%|-2%|1,581|9%|
|AIN|Albany International Corp.|**8.7**|10|48%|7.9|6%|10%|1,188|25%|
|AIR|AAR Corp.|**7.3**|13|56%|11.8|2%|15%|567|5%|
|AIT|Applied Industrial Technologies Inc.|**7.3**|5|37%|10.3|5%|-13%|1,073|55%|
|ALEX|Alexander & Baldwin Inc.|**3.4**|9|43%|9.7|-7%|-29%|2,337|28%|
|ALK|Alaska Air Group Inc.|**8.7**|9|87%|4.9|-16%|-49%|802|37%|
|ALOG|Analogic Corp.|**2.1**|3|57%|26.2|0%|8%|696|1663%|
|AMAT|Applied Materials Inc.|**1.8**|13|33%|13.1|5%|-10%|27,517|71%|
|AME|Ametek Inc.|**6.0**|10|25%|13.3|5%|-1%|3,016|3%|
|AMED|Amedisys Inc.|**2.8**|3|30%|12.0|3%|192%|616|309%|
|AMHC|American Healthways Inc.|**0.5**|3|14%|18.1|4%|24%|1,434|10139%|
|AMSG|Amsurg Corp.|**9.0**|3|35%|5.9|5%|11%|812|8%|
|ANDW|Andrew Corp.|**3.4**|13|87%|11.0|1%|68%|1,794|33%|
|ANT|Anteon International Corp.|**3.1**|2|20%|12.6|3%|30%|1,589|8%|
|AOS|A.O. Smith Corp.|**9.3**|10|72%|8.2|13%|8%|858|65%|
|APD|Air Products & Chemicals Inc.|**5.7**|10|37%|8.0|1%|20%|12,236|3%|
|APH|Amphenol Corp.|**3.7**|13|18%|10.9|5%|47%|3,585|2%|
|APN|Applica Inc.|**9.2**|8|156%|13.1|25%|-21%|40|101%|
|APOG|Apogee Enterprises Inc.|**4.5**|10|39%|10.5|2%|49%|477|39%|
|APPB|Applebee's International Inc.|**4.3**|6|30%|7.8|5%|27%|1,601|141%|
|ARB|Arbitron Inc.|**1.7**|1|6%|11.6|6%|90%|1,229|69%|
|ARJ|Arch Chemicals Inc.|**7.4**|10|68%|8.1|-12%|-10%|549|70%|
|ARXX|Aeroflex Inc.|**3.9**|13|64%|11.2|3%|52%|699|219%|
|ASF|Administaff Inc.|**1.4**|1|15%|20.4|2%|-6%|1,068|240%|
|ASH|Ashland Inc.|**3.1**|10|91%|4.5|-11%|87%|4,099|473%|
|ASHW|Ashworth Inc.|**5.6**|6|109%|17.3|-12%|506%|96|0%|
|ASTE|Astec Industries Inc.|**2.0**|10|40%|11.9|1%|211%|595|64%|
|ASVI|A.S.V. Inc.|**0.4**|10|24%|14.9|-1%|168%|608|1654%|
|ATMI|ATMI Inc.|**1.2**|13|39%|18.1|0%|10%|1,171|1630%|
|ATML|Atmel Corp.|**4.8**|13|90%|6.2|-12%|275%|995|40%|
|ATR|AptarGroup Inc.|**8.0**|10|46%|7.6|4%|55%|1,738|5%|
|ATSN|Artesyn Technologies Inc.|**4.5**|10|38%|10.2|1%|213%|371|13%|
|AWR|American States Water Co.|**5.0**|5|47%|12.4|-8%|47%|562|2%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

25 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|||**Firm****_LEVER_**||**Book to**||**FCF**|**Capex**|**Mkt**||
|---|---|---|---|---|---|---|---|---|---|
|**Ticker**|**COMPANY**|**Score**|**Sector No**|**Market**|**EV / EBITDA**|**Yield**|**Growth**|**Value**|**FCF Variability**|
|AYI|Acuity Brands Inc.|7.3|10|41%|9.8|6%|40%|1,334|12%|
|B|Barnes Group Inc.|4.9|8|46%|10.4|3%|55%|854|5%|
|BBOX|Black Box Corp.|6.5|2|71%|10.8|6%|208%|719|58%|
|BBY|Best Buy Co. Inc.|5.0|6|22%|10.6|4%|-13%|21,436|2%|
|BC|Brunswick Corp.|8.1|8|54%|6.7|4%|7%|3,662|1%|
|BCO|Brink's Co.|7.2|1|32%|6.9|3%|9%|2,410|24%|
|BCR|C.R. Bard Inc.|2.2|3|22%|14.1|3%|3%|6,924|36%|
|BDC|Belden CDT Inc.|9.9|10|88%|7.7|5%|-5%|872|6%|
|BEC|Beckman Coulter Inc.|4.1|3|35%|12.7|5%|19%|3,352|31%|
|BELFB|Bel Fuse Inc.|3.6|13|46%|11.2|6%|111%|420|4399%|
|BELM|Bell Microproducts Inc.|5.4|5|77%|17.2|-7%|23%|299|9%|
|BEZ|Baldor Electric Co.|4.8|10|35%|11.3|0%|20%|841|13%|
|BF.B|Brown-Forman Corp.|4.5|6|17%|14.1|3%|-40%|7,266|1%|
|BGP|Borders Group Inc.|8.3|6|62%|5.5|3%|6%|1,556|23%|
|BID|Sotheby's Holdings Inc.|1.6|6|8%|10.1|5%|104%|961|81%|
|BIIB|Biogen Idec Inc.|1.6|3|51%|12.8|3%|20%|13,400|1063%|
|BJ|BJ's Wholesale Club Inc.|7.4|6|51%|6.3|3%|-13%|1,895|1014%|
|BKS|Barnes & Noble Inc.|7.4|6|42%|5.9|14%|7%|2,557|3855%|
|BMET|Biomet Inc.|2.2|3|18%|13.1|3%|31%|8,645|3%|
|BMHC|Building Materials Holding Corp.|6.6|10|33%|6.7|9%|74%|1,340|50%|
|BN|Banta Corp.|8.5|1|43%|7.9|2%|-8%|1,220|21%|
|BNE|Bowne & Co.|6.3|1|71%|11.0|-7%|0%|470|115%|
|BOBE|Bob Evans Farms Inc.|7.3|6|82%|8.4|-6%|13%|805|13%|
|BRC|Brady Corp.|5.9|10|33%|11.1|5%|14%|1,524|17%|
|BRL|Barr Pharmaceuticals Inc.|5.0|3|24%|11.9|5%|-20%|5,729|539%|
|BSTE|Biosite Inc.|6.1|3|27%|10.9|2%|-6%|1,073|206%|
|BW|Brush Engineered Materials Inc.|8.4|4|71%|7.9|5%|-83%|305|125%|
|BWA|BorgWarner Inc.|7.1|10|51%|6.3|3%|19%|3,219|21%|
|CAI|CACI International Inc.|7.6|2|36%|12.0|8%|-16%|1,825|34%|
|CAM|Cooper Cameron Corp.|4.9|10|35%|14.8|7%|-17%|4,189|46%|
|CAS|A.M. Castle & Co.|9.7|5|57%|4.7|6%|3%|276|19%|
|CASY|Casey's General Stores Inc.|7.2|6|42%|9.3|3%|24%|1,166|2%|
|CBM|Cambrex Corp.|8.6|10|73%|8.9|-2%|4%|503|12%|
|CBR|CIBER Inc.|8.8|2|81%|9.8|6%|67%|464|15%|
|CBRL|CBRL Group Inc.|8.5|6|55%|6.6|5%|19%|1,569|19%|
|CC|Circuit City Stores Inc.|0.8|6|61%|11.9|-3%|45%|3,131|1059%|
|CCBL|C-COR Inc.|1.7|13|63%|-23.0|-6%|32%|323|6453%|
|CCRN|Cross Country Healthcare Inc.|8.0|1|60%|17.7|3%|29%|598|2%|
|CDIS|Cal Dive International Inc.|3.3|10|23%|9.1|-2%|-46%|2,465|82%|
|CDNS|Cadence Design Systems Inc.|5.2|13|41%|14.5|7%|-25%|4,585|27%|
|CEC|CEC Entertainment Inc.|8.8|6|32%|6.3|5%|-15%|1,090|28%|
|CECO|Career Education Corp.|3.3|6|28%|7.4|7%|42%|3,484|292%|
|CEN|Ceridian Corp.|5.8|2|42%|10.6|8%|8%|3,005|369%|
|CEPH|Cephalon Inc.|1.5|3|22%|12.7|1%|24%|2,681|19%|
|CERN|Cerner Corp.|6.1|3|21%|13.2|3%|-32%|3,323|15%|
|CEY|Certegy Inc.|5.4|2|17%|10.8|2%|-7%|2,486|5%|
|CGX|Consolidated Graphics Inc.|10.0|1|50%|6.5|11%|6%|587|9%|
|CHIR|Chiron Corp.|0.3|3|31%|74.3|0%|32%|8,230|23%|
|CHP|C&D Technologies Inc.|8.5|10|87%|11.4|8%|115%|239|16%|
|CHUX|O'Charley's Inc.|9.9|6|106%|6.0|2%|-11%|328|6%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

26 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|||**Firm****_LEVER_**||**Book to**||**FCF**|**Capex**|**Mkt**||
|---|---|---|---|---|---|---|---|---|---|
|**Ticker**|**COMPANY**|**Score**|**Sector No**|**Market**|**EV / EBITDA**|**Yield**|**Growth**|**Value**|**FCF Variability**|
|CIEN|Ciena Corp.|3.2|13|65%|-15.4|-13%|12%|1,523|12%|
|CKFR|CheckFree Corp.|3.2|2|40%|12.4|5%|20%|3,429|177%|
|CKP|Checkpoint Systems Inc.|5.7|13|43%|11.8|4%|-11%|911|63%|
|CLC|CLARCOR Inc.|1.1|8|32%|11.3|4%|71%|1,490|102%|
|CMC|Commercial Metals Co.|7.8|10|46%|4.7|4%|32%|1,961|16%|
|CMTL|Comtech Telecommunications Corp.|2.2|13|21%|16.1|5%|50%|936|27%|
|CMX|Caremark Rx Inc.|1.4|3|36%|14.5|5%|27%|22,198|73%|
|CNC|Centene Corp.|3.8|3|31%|11.8|5%|31%|1,067|1230%|
|CNCT|Connetics Corp.|1.9|3|20%|18.6|4%|696%|595|37%|
|CNMD|CONMED Corp.|9.0|3|60%|8.9|5%|33%|808|8%|
|COA|Coachmen Industries Inc.|4.6|8|115%|-101.1|3%|37%|182|101%|
|COCO|Corinthian Colleges Inc.|4.0|6|35%|9.1|4%|48%|1,213|45%|
|COG|Cabot Oil & Gas Corp.|1.1|4|20%|9.2|0%|70%|2,473|6%|
|COH|Coach Inc.|0.1|6|10%|16.4|4%|30%|11,934|3621%|
|COL|Rockwell Collins Corp.|0.6|13|11%|12.3|5%|27%|8,335|129%|
|COO|Cooper Cos.|1.6|3|37%|19.6|2%|20%|3,385|22%|
|CPN|Calpine Corp.|7.0|5|253%|18.4|-112%|-18%|1,475|5%|
|CPWM|Cost Plus Inc.|6.4|6|74%|6.9|-13%|151%|400|14%|
|CPY|CPI Corp.|6.2|6|12%|5.3|-2%|-11%|138|55%|
|CR|Crane Co.|9.2|10|41%|7.4|6%|-20%|1,787|13%|
|CRDN|Ceradyne Inc.|1.6|13|17%|11.9|0%|116%|904|8%|
|CRL|Charles River Laboratories International Inc.|4.7|3|57%|12.4|4%|39%|3,151|29%|
|CRS|Carpenter Technology Corp.|7.1|4|51%|6.3|6%|32%|1,470|14%|
|CRY|CryoLife Inc.|2.3|3|29%|-36.3|-11%|-1%|168|274%|
|CSGS|CSG Systems International Inc.|6.9|2|28%|9.8|9%|7%|1,060|51%|
|CSK|Chesapeake Corp.|9.9|10|176%|7.0|3%|-32%|362|9%|
|CSL|Carlisle Cos.|4.8|10|37%|9.4|2%|71%|1,946|7%|
|CSTR|Coinstar Inc.|9.2|6|52%|7.2|8%|72%|473|8%|
|CTAS|Cintas Corp.|2.0|6|30%|11.2|3%|11%|6,906|26%|
|CTB|Cooper Tire & Rubber Co.|4.0|8|103%|11.0|-39%|3%|936|71%|
|CTCO|Commonwealth Telephone Enterprises Inc.|3.2|13|6%|6.4|-25%|-8%|823|102%|
|CTS|CTS Corp.|8.9|13|74%|8.8|3%|41%|437|5%|
|CTV|CommScope Inc.|5.3|13|52%|8.8|5%|148%|954|29%|
|CW|Curtiss-Wright Corp.|6.7|13|46%|10.4|2%|-3%|1,342|8%|
|CY|Cypress Semiconductor Corp.|0.5|13|31%|30.3|-3%|69%|2,037|17%|
|CYBX|Cyberonics Inc.|1.1|3|8%|-30.7|-4%|-7%|748|931%|
|CYMI|Cymer Inc.|7.0|13|46%|17.8|8%|-69%|1,115|52%|
|CYTC|Cytyc Corp.|1.0|3|18%|16.1|4%|398%|3,056|28%|
|DAKT|Daktronics Inc.|0.7|13|23%|16.2|0%|54%|462|161%|
|DBRN|Dress Barn Inc.|9.1|6|46%|8.5|11%|-39%|687|92%|
|DCI|Donaldson Co. Inc.|3.6|10|21%|12.8|3%|4%|2,536|10%|
|DEL|Deltic Timber Corp.|3.8|4|35%|16.4|1%|-15%|566|31%|
|DJ|Dow Jones & Co. Inc.|0.3|6|4%|14.7|2%|36%|3,173|49%|
|DJO|DJ Orthopedics Inc.|8.0|3|33%|10.7|5%|12%|633|14%|
|DLP|Delta & Pine Land Co.|3.2|10|17%|12.9|2%|-20%|953|79%|
|DLTR|Dollar Tree Stores Inc.|8.8|6|47%|6.2|7%|-6%|2,348|43%|
|DNB|Dun & Bradstreet Corp.|5.5|1|0%|10.9|6%|10%|4,373|2%|
|DNEX|Dionex Corp.|0.4|13|17%|15.5|4%|111%|1,087|2257%|
|DPHIQ|Delphi Corp.|0.7|10|-343%|24.6|-74%|-4%|1,551|22%|
|DRI|Darden Restaurants Inc.|7.7|6|28%|7.8|7%|-12%|4,571|12%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

27 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|||**Firm****_LEVER_**||**Book to**||**FCF**|**Capex**|**Mkt**||
|---|---|---|---|---|---|---|---|---|---|
|**Ticker**|**COMPANY**|**Score**|**Sector No**|**Market**|**EV / EBITDA**|**Yield**|**Growth**|**Value**|**FCF Variability**|
|DRQ|Dril-Quip Inc.|0.4|10|28%|18.0|-3%|105%|848|100%|
|DRTE|Dendrite International Inc.|3.4|3|30%|10.7|4%|213%|869|607%|
|DST|DST Systems Inc.|7.3|2|11%|10.0|4%|-31%|3,959|0%|
|DV|DeVry Inc.|5.5|6|39%|14.5|3%|-1%|1,344|10%|
|EAGL|EGL Inc.|3.5|9|39%|10.0|9%|39%|1,285|380%|
|EASI|Engineered Support Systems Inc.|4.5|13|26%|11.7|6%|-17%|1,715|62%|
|EC|Engelhard Corp.|6.9|10|43%|8.5|3%|8%|3,346|11%|
|ECL|Ecolab Inc.|2.9|10|20%|10.8|3%|30%|8,175|5%|
|EFD|eFunds Corp.|4.0|2|50%|8.9|0%|31%|860|1053%|
|ELY|Callaway Golf Co.|0.3|8|58%|16.8|-3%|233%|1,062|166782%|
|EMC|EMC Corp.|2.1|13|39%|13.7|6%|1%|30,936|63%|
|EME|EMCOR Group Inc.|9.3|10|66%|7.3|11%|-10%|921|4531%|
|EOG|EOG Resources Inc.|0.2|4|21%|8.0|1%|18%|18,092|93%|
|EPIQ|EPIQ Systems Inc.|7.1|2|38%|11.9|5%|44%|393|10%|
|ESRX|Express Scripts Inc.|3.5|3|15%|13.9|7%|-3%|9,058|71%|
|ESV|ENSCO International Inc.|0.3|10|34%|15.4|-2%|63%|7,138|47%|
|ETH|Ethan Allen Interiors Inc.|5.3|8|39%|8.2|6%|6%|1,046|584%|
|ETM|Entercom Communications Corp.|9.7|6|66%|10.8|8%|-30%|1,451|3%|
|EW|Edwards Lifesciences Corp.|2.7|3|25%|12.7|4%|12%|2,653|32%|
|EYE|Advanced Medical Optics Inc.|2.4|3|39%|16.2|0%|39%|2,532|10%|
|FBN|Furniture Brands International Inc.|10.0|8|101%|6.9|12%|-26%|923|0%|
|FCS|Fairchild Semiconductor International Inc.|6.5|13|57%|11.5|3%|40%|1,781|1%|
|FEIC|FEI Co.|7.6|13|48%|17.0|2%|-50%|648|6%|
|FISV|Fiserv Inc.|4.6|2|29%|10.3|6%|12%|8,513|22%|
|FLIR|Flir Systems Inc.|2.4|13|17%|17.1|2%|-5%|2,071|12%|
|FLO|Flowers Foods Inc.|3.2|6|33%|10.5|3%|6%|1,556|368%|
|FLR|Fluor Corp.|1.4|10|27%|13.6|6%|32%|5,589|215%|
|FMC|FMC Corp.|9.5|10|44%|6.7|6%|-2%|2,171|6%|
|FOSL|Fossil Inc.|2.5|8|44%|8.5|0%|-2%|1,290|2400%|
|FRED|Fred's Inc.|8.5|6|65%|8.0|2%|-22%|498|90%|
|FRNT|Frontier Airlines Inc.|5.1|9|69%|22.1|-20%|-30%|354|35%|
|FSS|Federal Signal Corp.|6.8|10|50%|29.0|7%|15%|822|17%|
|FTI|FMC Technologies Inc.|1.9|10|25%|20.3|0%|-23%|2,893|23%|
|FUL|H.B. Fuller Co.|10.0|10|64%|7.5|8%|-20%|904|5%|
|FWRD|Forward Air Corp.|0.1|9|14%|15.3|2%|290%|1,146|2396%|
|GAP|Great Atlantic & Pacific Tea Co.|5.6|6|66%|5.3|-20%|26%|1,157|53%|
|GB|Greatbatch Inc.|6.2|10|46%|14.1|3%|222%|594|0%|
|GDI|Gardner Denver Inc.|7.9|10|55%|13.7|7%|64%|1,158|2%|
|GDT|Guidant Corp.|1.4|3|20%|20.2|4%|-15%|22,829|227%|
|GENZ|Genzyme Corp.|2.6|3|27%|21.1|3%|-28%|18,499|43%|
|GFF|Griffon Corp.|7.8|10|48%|8.3|2%|11%|752|22%|
|GGC|Georgia Gulf Corp.|8.6|10|42%|4.7|4%|-3%|821|46%|
|GGG|Graco Inc.|1.6|10|12%|11.6|4%|9%|2,349|858%|
|GILD|Gilead Sciences Inc.|0.5|3|12%|22.5|2%|-68%|22,306|107824%|
|GISX|Global Imaging Systems Inc.|9.8|1|51%|8.3|7%|18%|790|2%|
|GKSRA|G&K Services Inc.|9.3|1|60%|9.2|3%|-25%|835|21%|
|GLW|Corning Inc.|0.1|13|18%|17.2|1%|134%|29,343|14%|
|GPC|Genuine Parts Co.|5.4|5|36%|10.6|4%|-2%|7,444|11%|
|GPN|Global Payments Inc.|1.1|2|20%|14.3|7%|39%|3,044|5807%|
|GRB|Gerber Scientific Inc.|8.9|13|62%|9.1|7%|35%|175|19%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

28 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|**Ticker**|**COMPANY**|**Firm****_LEVER_**<br>**Score**|**Sector No**|**Book to**<br>**Market**|**EV / EBITDA**|**FCF**<br>**Yield**|**Capex**<br>**Growth**|**Mkt**<br>**Value**|**FCF Variability**|
|---|---|---|---|---|---|---|---|---|---|
|GTRC|Guitar Center Inc.|2.2|6|26%|10.9|1%|8%|1,435|50%|
|GVA|Granite Construction Inc.|4.8|10|37%|9.3|0%|43%|1,595|9%|
|GWW|W.W. Grainger Inc.|1.2|5|39%|9.2|3%|73%|5,627|2029%|
|GY|GenCorp Inc.|3.6|13|10%|57.8|-3%|-57%|1,022|5%|
|HAE|Haemonetics Corp.|4.0|3|31%|13.4|4%|21%|1,258|25%|
|HAIN|Hain Celestial Group Inc.|9.1|6|76%|13.0|4%|4%|716|2%|
|HAR|Harman International Industries Inc.|0.7|8|15%|14.6|4%|22%|6,742|28%|
|HAS|Hasbro Inc.|4.1|8|48%|8.7|9%|26%|3,508|88%|
|HCR|Manor Care Inc.|7.0|3|25%|8.6|5%|49%|3,023|1%|
|HDI|Harley-Davidson Inc.|2.9|8|22%|8.3|5%|-6%|13,302|32%|
|HH|Hooper Holmes Inc.|5.2|3|89%|10.6|0%|29%|258|695%|
|HHS|Harte-Hanks Inc.|5.2|1|26%|10.4|6%|10%|2,188|114%|
|HKF|Hancock Fabrics Inc.|7.0|6|92%|47.7|-16%|9%|129|3%|
|HLIT|Harmonic Inc.|1.0|13|27%|21.3|4%|88%|428|1346%|
|HNI|HNI Corp.|1.9|10|22%|12.2|4%|-7%|3,299|928%|
|HSC|Harsco Corp.|5.0|10|35%|7.4|1%|42%|2,737|11%|
|HSIC|Henry Schein Inc.|5.5|5|32%|13.1|5%|-3%|3,726|11%|
|HTCH|Hutchinson Technology Inc.|5.5|13|83%|6.0|-11%|91%|665|59%|
|HUB.B|Hubbell Inc.|2.1|10|34%|10.8|1%|42%|2,844|27%|
|HVT|Haverty Furniture Cos. Inc.|6.3|6|98%|7.0|-3%|108%|281|45%|
|IART|Integra LifeSciences Holdings Corp.|3.3|3|29%|16.1|4%|121%|1,076|14%|
|IDXX|IDEXX Laboratories Inc.|0.4|3|18%|16.0|4%|72%|2,151|8130%|
|IEX|IDEX Corp.|5.1|10|36%|11.8|5%|4%|2,220|35%|
|IFF|International Flavors & Fragrances Inc.|3.0|6|28%|10.0|3%|7%|3,325|24%|
|IHP|IHOP Corp.|9.1|6|40%|9.4|4%|-79%|765|9%|
|IMDC|Inamed Corp.|0.1|3|18%|23.2|3%|55%|2,755|661%|
|IMGC|Intermagnetics General Corp.|2.3|3|36%|23.3|0%|58%|788|14%|
|INSU|Insituform Technologies Inc.|4.7|10|64%|21.5|0%|77%|466|9%|
|INT|World Fuel Services Corp.|6.0|1|43%|15.5|1%|-27%|801|62%|
|INTC|Intel Corp.|1.7|13|25%|9.0|5%|5%|148,590|177%|
|IO|Input/Output Inc.|5.5|10|50%|17.8|-5%|9%|629|7%|
|IRF|International Rectifier Corp.|3.7|13|46%|12.3|2%|40%|3,189|6%|
|IRN|Rewards Networks Inc.|6.4|6|51%|25.4|-2%|-4%|179|10%|
|ISCA|International Speedway Corp.|0.6|6|35%|9.8|-5%|86%|2,798|62%|
|IT|Gartner Inc.|3.9|1|9%|17.6|1%|-13%|1,327|6%|
|ITRI|Itron Inc.|2.9|13|26%|13.5|5%|33%|1,132|43%|
|IVC|Invacare Corp.|7.3|3|58%|11.3|3%|35%|1,322|7%|
|IVGN|Invitrogen Corp.|6.6|3|51%|15.6|6%|21%|3,974|1%|
|IVX|IVAX Corp.|1.7|3|25%|21.6|2%|4%|7,213|12%|
|JAKK|JAKKS Pacific Inc.|9.6|8|116%|4.5|22%|32%|437|53%|
|JAS|Jo-Ann Stores Inc.|7.5|6|105%|4.8|-5%|41%|394|28%|
|JBHT|J.B. Hunt Transport Services Inc.|1.5|9|27%|5.9|2%|42%|2,940|236%|
|JBLU|JetBlue Airways Corp.|2.0|9|42%|17.5|-46%|9%|1,857|8%|
|JCOM|j2 Global Communications Inc.|0.8|2|19%|15.0|5%|96%|1,000|3722%|
|JILL|J. Jill Group Inc.|4.9|6|51%|13.6|-2%|-16%|322|258%|
|JLG|JLG Industries Inc.|2.6|10|25%|13.1|5%|36%|1,890|39%|
|JOYG|Joy Global Inc.|1.1|10|13%|15.1|2%|-32%|4,088|295%|
|KAMN|Kaman Corp.|6.8|13|60%|28.7|4%|-17%|472|44%|
|KEA|Keane Inc.|8.8|2|66%|10.2|2%|-33%|675|28%|
|KELYA|Kelly Services Inc.|4.2|1|60%|12.5|-1%|18%|1,097|113%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

29 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|**Ticker**|**COMPANY**|**Firm**|**Sector**|**Book to**|**EV / EBITDA**|**FCF**|**Capex**|**Mkt Value **|**FCF Variability**|
|---|---|---|---|---|---|---|---|---|---|
|||**_LEVER_**|**No**|**Market**||**Yield**|**Growth**|||
|||**Score**||||||||
|KEM|Kemet Corp.|4.4|13|71%|-81.1|-3%|51%|727|6%|
|KEX|Kirby Corp.|4.8|9|40%|8.5|2%|29%|1,247|9%|
|KFY|Korn/Ferry International|7.9|1|40%|8.7|8%|76%|668|45%|
|KG|King Pharmaceuticals Inc.|8.1|3|55%|5.9|13%|8%|3,719|90%|
|KMX|CarMax Inc.|0.5|6|27%|14.5|-4%|31%|3,272|21%|
|KWD|Kellwood Co.|7.4|6|90%|14.8|5%|23%|720|16%|
|KWR|Quaker Chemical Corp.|9.3|10|71%|7.3|-8%|-31%|169|14%|
|LAUR|Laureate Education Inc.|4.5|1|38%|16.7|2%|24%|2,437|7%|
|LAWS|Lawson Products Inc.|7.4|5|54%|8.0|0%|-11%|331|979%|
|LBY|Libbey Inc.|7.7|8|72%|7.6|1%|63%|212|3%|
|LCAV|LCA-Vision Inc.|1.3|3|18%|13.5|3%|38%|767|337%|
|LDL|Lydall Inc.|7.5|10|100%|8.2|-3%|56%|144|25%|
|LEG|Leggett & Platt Inc.|6.3|8|62%|7.8|3%|15%|3,769|7%|
|LFUS|Littelfuse Inc.|4.0|10|45%|10.0|2%|57%|628|145%|
|LII|Lennox International Inc.|7.4|10|36%|8.4|2%|-2%|1,785|9%|
|LIN|Linens 'N Things Inc.|2.7|6|66%|8.2|-4%|46%|1,211|35767%|
|LIZ|Liz Claiborne Inc.|5.1|6|47%|7.4|6%|39%|4,227|82%|
|LNCE|Lance Inc.|3.3|6|39%|8.3|0%|63%|521|76%|
|LNCR|Lincare Holdings Inc.|9.2|3|29%|8.9|7%|-30%|3,992|13%|
|LNX|Lenox Group Inc.|6.3|8|91%|12.5|3%|-12%|174|880%|
|LPNT|Lifepoint Hospitals Inc.|7.4|3|50%|13.0|4%|17%|2,497|1%|
|LPX|Louisiana-Pacific Corp.|5.9|4|67%|5.1|7%|71%|2,927|73%|
|LRW|Labor Ready Inc.|3.3|1|24%|12.9|6%|19%|1,367|5037%|
|LSI|LSI Logic Corp.|4.8|13|41%|16.7|5%|-33%|3,857|20%|
|LSS|Lone Star Technologies Inc.|6.7|10|33%|8.0|4%|-10%|1,697|69%|
|LSTR|Landstar System Inc.|1.6|9|9%|13.4|6%|15%|2,338|75%|
|LTXX|LTX Corp.|2.6|13|40%|-14.5|-26%|-8%|260|41%|
|LXK|Lexmark International Inc.|1.1|13|22%|9.0|6%|111%|7,082|199%|
|LZB|La-Z-Boy Inc.|7.7|8|76%|8.8|3%|3%|683|14%|
|MAG|MagneTek Inc.|8.1|10|48%|9.4|-7%|0%|97|10%|
|MAN|Manpower Inc.|8.9|1|54%|9.0|5%|22%|3,876|0%|
|MANH|Manhattan Associates Inc.|4.2|2|34%|13.4|5%|13%|645|10452%|
|MANT|ManTech International Corp.|4.7|2|43%|10.9|5%|45%|856|81%|
|MAT|Mattel Inc.|2.5|8|34%|8.1|3%|-28%|6,737|192%|
|MATK|Martek Biosciences Corp.|0.6|3|41%|28.4|-6%|299%|1,114|91%|
|MCDTA|McDATA Corp.|6.8|13|69%|22.6|-2%|-45%|804|9%|
|MCHP|Microchip Technology Inc.|1.3|13|25%|14.9|4%|-12%|6,327|145%|
|MCO|Moody's Corp.|0.5|1|3%|16.0|4%|19%|15,090|39%|
|MCRL|Micrel Inc.|2.6|13|27%|15.6|4%|-20%|969|22841%|
|MCRS|Micros Systems Inc.|0.8|2|20%|17.6|5%|33%|1,673|1278%|
|MDP|Meredith Corp.|4.1|6|27%|10.0|3%|-5%|2,460|37%|
|MDS|Midas Inc.|3.1|6|16%|11.1|2%|11%|320|51%|
|MEAD|Meade Instruments Corp.|4.5|8|115%|63.1|-5%|27%|53|23%|
|MEG|Media General Inc.|6.5|6|65%|9.0|3%|35%|1,395|14%|
|MENT|Mentor Graphics Corp.|7.1|13|63%|12.4|1%|4%|681|7%|
|MHP|McGraw-Hill Cos.|1.4|1|18%|10.5|6%|21%|18,010|1904%|
|MIL|Millipore Corp.|4.1|3|24%|16.7|3%|-11%|3,273|55%|
|MKC|McCormick & Co. Inc.|5.0|6|19%|11.7|5%|-24%|4,368|12%|
|MLHR|Herman Miller Inc.|2.0|10|8%|13.1|3%|11%|2,108|27%|
|MLI|Mueller Industries Inc.|4.7|10|39%|8.5|-13%|-27%|1,017|1671%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

30 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|**Ticker**|**COMPANY**|**Firm**|**Sector No**|**Book to**|**EV / EBITDA**|**FCF**|**Capex**|**Mkt Value **|**FCF Variability**|
|---|---|---|---|---|---|---|---|---|---|
|||**_LEVER_**||**Market**||**Yield**|**Growth**|||
|||**Score**||||||||
|MLM|Martin Marietta Materials Inc.|1.4|4|33%|8.5|2%|35%|3,633|15%|
|MLNM|Millennium Pharmaceuticals Inc.|5.9|3|74%|-33.5|-4%|-5%|2,893|7%|
|MMS|Maximus Inc.|8.2|1|53%|9.4|7%|22%|767|302%|
|MNC|Monaco Coach Corp.|5.1|8|72%|12.0|-2%|-37%|436|191%|
|MNT|Mentor Corp.|3.7|3|10%|19.4|3%|-32%|2,390|15%|
|MOD|Modine Manufacturing Co.|8.4|10|43%|7.8|6%|13%|1,264|32%|
|MOGN|MGI Pharma Inc.|0.5|3|9%|41.6|-4%|43%|1,676|3%|
|MRCY|Mercury Computer Systems Inc.|7.2|13|37%|12.1|6%|45%|553|3%|
|MRX|Medicis Pharmaceutical Corp.|5.6|3|29%|12.9|8%|26%|1,771|14%|
|MTX|Minerals Technologies Inc.|4.2|10|67%|8.4|-2%|102%|1,149|67%|
|MU|Micron Technology Inc.|7.2|13|71%|6.2|2%|21%|8,195|8%|
|MVK|Maverick Tube Corp.|8.4|10|56%|6.1|6%|67%|1,288|23%|
|MYE|Myers Industries Inc.|9.9|10|83%|7.4|8%|29%|405|5%|
|NAFC|Nash Finch Co.|9.6|5|56%|7.4|4%|-45%|557|20%|
|NCS|NCI Building Systems Inc.|9.8|10|53%|9.3|6%|-48%|865|7%|
|NDSN|Nordson Corp.|5.8|10|31%|11.0|7%|51%|1,381|15%|
|NE|Noble Corp.|3.4|10|28%|17.6|1%|-15%|9,373|2%|
|NEWP|Newport Corp.|3.1|13|67%|15.5|0%|96%|556|23%|
|NKE|NIKE Inc.|3.2|6|28%|9.4|4%|18%|21,269|12%|
|NMG.A|Neiman Marcus Group Inc.|2.8|6|32%|9.7|12%|34%|4,892|261%|
|NOV|National Oilwell Varco Inc.|0.8|10|36%|25.0|0%|20%|11,463|17%|
|NOVL|Novell Inc.|6.9|2|48%|28.7|16%|-32%|2,843|62%|
|NOVN|Noven Pharmaceuticals Inc.|1.5|3|41%|15.2|-5%|48%|330|7448%|
|NPO|EnPro Industries Inc.|7.0|10|74%|6.7|1%|77%|699|30%|
|NSIT|Insight Enterprises Inc.|7.9|6|63%|8.0|3%|-18%|883|314%|
|NSM|National Semiconductor Corp.|1.5|13|22%|14.4|5%|-19%|9,004|646%|
|NVLS|Novellus Systems Inc.|5.1|13|57%|13.0|8%|2%|3,345|176%|
|NWK|Network Equipment Technologies Inc.|6.7|13|95%|-31.0|-5%|-29%|113|19%|
|NWS.A|News Corp.|2.4|6|56%|12.2|4%|73%|50,749|11%|
|NX|Quanex Corp.|7.9|4|37%|5.9|9%|-32%|1,673|39%|
|ODFL|Old Dominion Freight Line Inc.|7.7|9|40%|6.8|-5%|-8%|832|4%|
|ODSY|Odyssey HealthCare Inc.|8.7|3|29%|11.1|10%|-8%|581|450577%|
|OII|Oceaneering International Inc.|4.3|10|36%|9.7|3%|97%|1,425|16%|
|OLN|Olin Corp.|6.6|4|32%|5.7|9%|0%|1,362|64%|
|OMC|Omnicom Group Inc.|2.5|1|25%|11.7|5%|13%|15,079|72%|
|OMX|OfficeMax Inc.|2.0|6|77%|13.2|-30%|31%|2,240|32%|
|ORCL|Oracle Corp.|1.5|2|18%|12.7|5%|-21%|63,848|1654%|
|ORLY|O'Reilly Automotive Inc.|1.1|6|35%|11.3|1%|27%|3,158|59%|
|OSI|Outback Steakhouse Inc.|2.5|6|43%|7.6|-1%|31%|2,732|83%|
|OSK|Oshkosh Truck Corp.|2.4|10|26%|10.5|5%|28%|3,164|267%|
|OSTE|Osteotech Inc.|6.0|3|83%|-61.4|3%|15%|99|19%|
|PCH|Potlatch Corp.|3.8|10|45%|11.4|-20%|-39%|1,522|199%|
|PD|Phelps Dodge Corp.|3.4|4|44%|4.8|10%|101%|13,188|107%|
|PDCO|Patterson Cos. Inc.|1.0|5|19%|17.3|2%|65%|5,521|5%|
|PDLI|Protein Design Labs Inc.|0.3|3|18%|463.7|-1%|5%|3,154|51%|
|PDX|Pediatrix Medical Group Inc.|8.7|3|38%|10.5|8%|-54%|1,836|2048%|
|PEGS|Pegasus Solutions Inc.|9.6|2|94%|7.5|4%|17%|186|8%|
|PENX|Penford Corp.|9.8|10|84%|7.9|8%|34%|119|11%|
|PFCB|P.F. Chang's China Bistro Inc.|0.8|6|24%|10.3|1%|32%|1,182|11168%|
|PFGC|Performance Food Group Co.|8.7|5|69%|11.4|53%|-26%|1,185|759%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

31 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|**Ticker**|**COMPANY**|**Firm**|**Sector No**|**Book to**|**EV / EBITDA**|**FCF**|**Capex**|**Mkt Value **|**FCF Variability**|
|---|---|---|---|---|---|---|---|---|---|
|||**_LEVER_**||**Market**||**Yield**|**Growth**|||
|||**Score**||||||||
|PH|Parker Hannifin Corp.|8.9|10|45%|6.5|8%|-1%|7,702|12%|
|PHS|PacifiCare Health Systems Inc.|4.4|3|36%|10.8|14%|40%|7,008|97%|
|PII|Polaris Industries Inc.|1.2|8|17%|7.4|3%|45%|2,072|932%|
|PIR|Pier 1 Imports Inc.|5.5|6|64%|9.2|-8%|-9%|978|150%|
|PKI|PerkinElmer Inc.|7.7|3|56%|11.8|5%|14%|2,655|6%|
|PLAB|Photronics Inc.|9.1|13|70%|6.6|4%|70%|800|4%|
|PLL|Pall Corp.|4.4|3|33%|11.7|1%|9%|3,419|10%|
|PLMD|PolyMedica Corp.|5.4|5|22%|7.0|0%|-46%|845|1889%|
|PLNR|Planar Systems Inc.|8.0|13|108%|10.4|28%|42%|121|2793%|
|POOL|SCP Pool Corp.|2.9|5|16%|13.6|3%|-27%|1,843|64%|
|POP|Pope & Talbot Inc.|4.0|10|89%|20.0|-20%|36%|167|35%|
|POS|Catalina Marketing Corp.|7.6|1|13%|7.8|6%|-32%|1,092|79%|
|PPD|Pre-Paid Legal Services Inc.|6.2|6|7%|10.4|5%|-60%|598|40%|
|PPDI|Pharmaceutical Product Development Inc.|0.4|3|23%|15.3|3%|53%|3,324|1658%|
|PPG|PPG Industries Inc.|5.9|10|34%|6.4|4%|12%|9,886|20%|
|PRGO|Perrigo Co.|6.9|3|44%|17.3|5%|-9%|1,339|578%|
|PRGX|PRG-Schultz International Inc.|7.0|1|39%|24.8|-5%|-1%|187|3%|
|PRX|Par Pharmaceutical Companies Inc.|2.3|3|51%|24.3|-6%|7%|911|51%|
|PRXL|PAREXEL International Corp.|5.9|3|40%|9.6|0%|3%|531|7478%|
|PSEM|Pericom Semiconductor Corp.|4.3|13|78%|40.9|2%|18%|232|171%|
|PVA|Penn Virginia Corp.|5.6|4|24%|7.6|2%|-2%|1,073|1%|
|PWAV|Powerwave Technologies Inc.|1.8|13|40%|18.2|-2%|225%|1,436|3%|
|PWR|Quanta Services Inc.|3.8|10|45%|18.6|1%|8%|1,510|17%|
|PXR|Paxar Corp.|9.3|13|67%|8.4|5%|18%|687|6%|
|PZZA|Papa John's International Inc.|4.6|6|21%|9.0|8%|28%|855|108%|
|RADS|Radiant Systems Inc.|4.3|13|26%|17.7|3%|-43%|306|57%|
|RARE|Rare Hospitality International Inc.|6.2|6|48%|7.7|2%|26%|856|33%|
|RBK|Reebok International Ltd.|3.0|6|43%|11.7|5%|25%|3,387|45%|
|RDC|Rowan Cos. Inc.|4.8|10|40%|14.0|0%|-45%|3,879|10%|
|RDK|Ruddick Corp.|6.5|6|56%|6.3|0%|30%|1,094|20%|
|REGN|Regeneron Pharmaceuticals Inc.|5.2|3|26%|-11.1|-5%|-79%|533|10%|
|RESP|Respironics Inc.|0.7|3|22%|16.1|2%|21%|3,039|44%|
|RFMD|RF Micro Devices Inc.|2.1|13|52%|22.3|-7%|11%|1,068|53%|
|RGS|Regis Corp.|7.5|6|46%|8.4|6%|16%|1,712|20%|
|RHB|RehabCare Group Inc.|6.7|3|66%|7.2|3%|34%|345|1084%|
|RHI|Robert Half International Inc.|1.1|1|15%|14.4|3%|-10%|6,026|1385%|
|RI|Ruby Tuesday Inc.|6.1|6|42%|7.5|0%|3%|1,362|30%|
|RMD|ResMed Inc.|0.6|3|19%|20.2|0%|17%|2,723|15%|
|ROP|Roper Industries Inc.|5.2|10|36%|14.1|6%|16%|3,371|11%|
|ROST|Ross Stores Inc.|3.1|6|23%|8.8|4%|4%|3,463|72%|
|RPM|RPM International Inc.|7.6|10|50%|8.6|1%|15%|2,166|4%|
|RRGB|Red Robin Gourmet Burgers Inc.|2.8|6|26%|11.3|-2%|29%|753|10%|
|RS|Reliance Steel & Aluminum Co.|6.3|4|55%|5.8|12%|72%|1,746|45%|
|RSYS|Radisys Corp.|8.7|13|53%|16.6|6%|29%|399|0%|
|RX|IMS Health Inc.|3.4|3|7%|11.1|3%|-5%|5,832|34%|
|RYAN|Ryan's Restaurant Group Inc.|9.4|6|85%|6.8|-2%|-1%|490|7%|
|SAFM|Sanderson Farms Inc.|4.9|6|44%|5.8|-3%|18%|758|770%|
|SBL|Symbol Technologies Inc.|3.9|13|48%|14.5|2%|51%|2,441|3%|
|SBUX|Starbucks Corp.|0.0|6|11%|16.8|2%|23%|19,224|17353%|
|SCHS|School Specialty Inc.|6.5|5|52%|11.3|5%|60%|1,115|9%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

32 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|**Ticker**|**COMPANY**|**Firm**|**Sector No**|**Book to**|**EV / EBITDA**|**FCF**|**Capex**|**Mkt Value **|**FCF Variability**|
|---|---|---|---|---|---|---|---|---|---|
|||**_LEVER_**||**Market**||**Yield**|**Growth**|||
|||**Score**||||||||
|SCSC|ScanSource Inc.|7.5|5|38%|9.9|3%|-25%|618|57%|
|SEE|Sealed Air Corp.|9.0|10|35%|8.4|7%|-17%|3,904|4%|
|SEIC|SEI Investments Co.|2.7|1|11%|12.5|5%|-40%|3,725|500%|
|SEPR|Sepracor Inc.|0.1|3|-3%|-165.1|-1%|143%|6,229|9%|
|SFA|Scientific-Atlanta Inc.|0.6|13|36%|13.1|5%|93%|5,760|1295%|
|SFCC|SFBC International Inc.|5.4|3|37%|14.9|2%|307%|821|2%|
|SFN|Spherion Corp.|9.7|1|97%|9.1|12%|-80%|455|989%|
|SGR|Shaw Group Inc.|4.2|10|59%|13.2|3%|13%|1,947|87%|
|SHFL|Shuffle Master Inc.|2.2|6|2%|19.7|3%|36%|926|6%|
|SHLM|A. Schulman Inc.|9.0|10|84%|7.9|2%|16%|551|13%|
|SHW|Sherwin-Williams Co.|5.3|6|29%|7.9|5%|-8%|6,033|54%|
|SIAL|Sigma-Aldrich Corp.|1.9|10|28%|11.2|4%|22%|4,305|82%|
|SIE|Sierra Health Services Inc.|3.4|3|13%|9.8|10%|20%|1,988|157%|
|SJM|J.M. Smucker Co.|4.2|6|60%|10.2|2%|25%|2,836|26%|
|SKE|Spinnaker Exploration Co.|1.8|4|39%|8.4|-1%|4%|2,210|60%|
|SKO|ShopKo Stores Inc.|9.4|6|86%|5.2|14%|33%|770|34%|
|SKYW|SkyWest Inc.|3.5|9|55%|12.5|-6%|-71%|1,552|76%|
|SLB|Schlumberger Ltd.|1.7|10|15%|14.0|2%|9%|49,707|1%|
|SLR|Solectron Corp.|6.1|13|65%|11.2|21%|7%|3,745|125%|
|SM|St. Mary Land & Exploration Co.|2.2|4|25%|6.5|2%|34%|2,069|15%|
|SMP|Standard Motor Products Inc.|4.6|8|130%|15.2|-49%|10%|159|56%|
|SNA|Snap-On Inc.|3.1|8|49%|9.4|1%|32%|2,092|13%|
|SNIC|Sonic Solutions|0.8|13|20%|28.6|4%|65%|533|7360%|
|SPSS|SPSS Inc.|4.6|2|34%|11.0|8%|113%|425|718%|
|SPW|SPX Corp.|5.4|10|85%|10.7|-10%|-43%|3,024|64%|
|SQA.A|Sequa Corp.|7.8|13|104%|6.8|-3%|27%|630|22%|
|SR|Standard Register Co.|9.2|1|46%|8.7|2%|27%|431|0%|
|SRCL|Stericycle Inc.|2.4|3|21%|15.3|4%|59%|2,531|8%|
|SRCP|SOURCECORP Inc.|9.7|1|98%|8.6|12%|1%|334|56%|
|SRNA|SERENA Software Inc.|6.4|2|34%|12.5|9%|43%|819|15%|
|SSD|Simpson Manufacturing Co.|1.0|10|29%|11.1|3%|113%|1,885|621%|
|STGS|Stage Stores Inc.|7.9|6|68%|5.8|3%|4%|733|968%|
|STJ|St. Jude Medical Inc.|0.0|3|16%|19.7|3%|81%|17,108|147%|
|SVC|Stewart & Stevenson Services Inc.|6.9|10|43%|6.8|-8%|-33%|694|170%|
|SWFT|Swift Transportation Co. Inc.|6.8|9|64%|4.7|-10%|37%|1,289|8%|
|SWM|Schweitzer-Mauduit International Inc.|9.8|10|87%|5.4|2%|-49%|340|14%|
|SXI|Standex International Corp.|9.5|10|55%|8.3|6%|6%|327|17%|
|SYK|Stryker Corp.|0.0|3|16%|15.9|2%|30%|19,965|2763%|
|SYMC|Symantec Corp.|4.4|2|60%|22.3|5%|-36%|25,313|91%|
|SYMM|Symmetricom Inc.|5.7|13|63%|16.6|5%|27%|358|90%|
|SYNA|Synaptics Inc.|3.3|13|30%|9.7|8%|566%|455|818%|
|TALX|TALX Corp.|4.4|2|24%|13.5|3%|34%|699|8%|
|TBCC|TBC Corp|8.1|5|44%|8.7|3%|21%|775|3%|
|TDW|Tidewater Inc.|3.7|9|55%|11.8|0%|-19%|2,797|33%|
|TDY|Teledyne Technologies Inc.|7.9|13|28%|9.8|6%|-7%|1,157|5%|
|TECD|Tech Data Corp.|9.8|5|83%|8.7|6%|-9%|2,124|1%|
|TECH|Techne Corp.|4.4|3|13%|20.1|3%|-20%|2,215|11%|
|TECUA|Tecumseh Products Co.|4.5|10|225%|-83.8|-50%|1%|398|58%|
|TER|Teradyne Inc.|0.1|13|32%|65.1|-4%|104%|3,248|57%|
|TFX|Teleflex Inc.|9.2|10|40%|9.7|7%|-41%|2,854|6%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

33 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|**Ticker**|**COMPANY**|**Firm**|**Sector No**|**Book to**|**EV / EBITDA**|**FCF**|**Capex**|**Mkt Value **|**FCF Variability**|
|---|---|---|---|---|---|---|---|---|---|
|||**_LEVER_**||**Market**||**Yield**|**Growth**|||
|||**Score**||||||||
|TG|Tredegar Corp.|9.4|10|97%|7.0|-5%|-15%|503|9%|
|TGI|Triumph Group Inc.|9.4|13|91%|12.2|4%|-29%|591|6%|
|TIF|Tiffany & Co.|2.8|6|30%|13.7|1%|-33%|5,663|17%|
|TJX|TJX Cos.|2.4|6|16%|7.5|3%|4%|9,542|62%|
|TNB|Thomas & Betts Corp.|7.8|10|49%|10.9|4%|-11%|2,090|14%|
|TNL|Technitrol Inc.|3.9|13|67%|19.2|4%|42%|621|105%|
|TNM|Thomas Nelson Inc.|6.9|6|47%|8.4|1%|-2%|281|78%|
|TQNT|Triquint Semiconductor Inc.|9.0|13|90%|21.5|3%|-9%|493|1%|
|TR|Tootsie Roll Industries Inc.|1.2|6|36%|15.6|2%|48%|1,699|30%|
|TRDO|Intrado Inc.|8.0|13|36%|9.1|10%|-23%|321|389%|
|TRMB|Trimble Navigation Ltd.|1.3|13|30%|14.0|4%|17%|1,811|10612%|
|TSCO|Tractor Supply Co.|0.4|6|25%|11.8|1%|90%|1,795|80%|
|TTC|Toro Co.|8.2|10|26%|7.8|8%|-9%|1,568|29%|
|TTI|Tetra Technologies Inc.|1.6|10|24%|12.9|-1%|385%|1,083|8%|
|TUP|Tupperware Corp.|4.5|8|23%|8.8|3%|9%|1,367|10%|
|TXN|Texas Instruments Inc.|0.2|13|22%|13.3|5%|62%|54,852|208%|
|UFPI|Universal Forest Products Inc.|7.7|4|39%|8.6|7%|0%|1,054|7%|
|UHS|Universal Health Services Inc.|9.1|3|47%|6.3|7%|3%|2,599|24%|
|UNFI|United Natural Foods Inc.|1.2|5|20%|18.9|-2%|64%|1,460|5%|
|URS|URS Corp.|8.6|10|65%|9.5|7%|15%|1,999|19%|
|USTR|United Stationers Inc.|6.4|5|49%|8.1|11%|36%|1,553|1962%|
|UTEK|Ultratech Inc.|1.3|13|52%|78.8|-2%|62%|376|166%|
|UTSI|UTStarcom Inc.|6.4|13|100%|-23.8|-8%|10%|981|1%|
|UVV|Universal Corp.|7.3|6|83%|7.9|-11%|9%|999|14%|
|VARI|Varian Inc.|7.7|13|48%|10.5|5%|-11%|1,030|26%|
|VCI|Valassis Communications Inc.|2.6|1|6%|11.8|3%|4%|1,881|36%|
|VECO|Veeco Instruments Inc.|4.9|13|51%|21.8|2%|92%|481|4%|
|VIA.B|Viacom Inc.|8.5|6|79%|10.1|5%|-22%|51,245|4%|
|VOL|Volt Information Sciences Inc.|8.8|1|92%|4.9|5%|71%|312|129%|
|VOXX|Audiovox Corp.|8.3|13|129%|-96.2|44%|-12%|317|860%|
|VRTX|Vertex Pharmaceuticals Inc.|1.1|3|6%|-22.6|-9%|-28%|2,210|28%|
|VSH|Vishay Intertechnology Inc.|5.7|13|132%|9.8|0%|25%|2,200|16%|
|VTS|Veritas DGC Inc.|9.5|10|46%|5.2|10%|-3%|1,255|22%|
|WAT|Waters Corp.|1.2|3|8%|15.2|5%|92%|4,611|16%|
|WCN|Waste Connections Inc.|9.3|10|44%|9.7|7%|1%|1,625|2%|
|WDC|Western Digital Corp.|3.6|13|28%|6.7|6%|89%|2,773|128%|
|WDFC|WD-40 Co.|8.2|10|29%|9.9|3%|19%|442|1%|
|WEN|Wendy's International Inc.|3.7|6|38%|9.6|0%|0%|5,238|18%|
|WFR|MEMC Electronic Materials Inc.|0.6|13|14%|14.7|2%|76%|4,770|9%|
|WHQ|W-H Energy Services Inc.|6.2|10|34%|8.3|-4%|20%|925|8%|
|WIND|Wind River Systems Inc.|4.0|2|25%|32.7|3%|-59%|1,100|79%|
|WLM|Wellman Inc.|9.6|10|117%|5.1|-24%|-3%|205|5%|
|WMS|WMS Industries Inc.|0.9|8|33%|11.7|-5%|58%|891|24%|
|WNC|Wabash National Corp.|8.9|10|43%|8.0|7%|138%|614|4%|
|WON|Westwood One Inc.|6.5|6|40%|11.8|6%|35%|1,767|4%|
|WOOF|VCA Antech Inc.|2.2|3|14%|14.4|4%|55%|2,107|7%|
|WOR|Worthington Industries Inc.|3.9|4|45%|7.1|5%|39%|1,852|52%|
|WPI|Watson Pharmaceuticals Inc.|9.2|3|51%|9.8|8%|-54%|4,057|55%|
|WPP|Wausau Paper Corp.|6.5|10|52%|6.7|-5%|22%|642|55%|
|WSM|Williams-Sonoma Inc.|1.8|6|23%|10.2|2%|-5%|4,465|71%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

34 

**Lehman Brothers** | Introducing LEVER: A Framework for Scoring LEVeraging Event Risk 

|**Ticker**|**COMPANY**|**Firm****_LEVER_**<br>**Score**|**Sector No**|**Book to**<br>**Market**|**EV / EBITDA**|**FCF**<br>**Yield**|**Capex**<br>**Growth**|**Mkt**<br>**Value**|**FCF Variability**|
|---|---|---|---|---|---|---|---|---|---|
|WSO|Watsco Inc.|2.7|10|31%|13.7|4%|58%|1,465|28%|
|WTR|Aqua America Inc.|0.7|5|21%|17.7|-5%|20%|3,666|9%|
|WTS|Watts Water Technologies Inc.|8.3|10|54%|9.8|4%|5%|939|17%|
|WWW|Wolverine World Wide Inc.|5.3|6|39%|9.3|5%|13%|1,196|216%|
|XRAY|Dentsply International Inc.|8.2|3|30%|13.3|4%|-27%|4,235|4%|
|YELL|Yellow Roadway Corp.|7.8|9|79%|5.5|6%|95%|2,406|15%|
|YHOO|Yahoo! Inc.|0.0|2|16%|18.3|3%|109%|47,636|93%|
|YRK|York International Corp.|5.3|10|39%|11.6|3%|-2%|2,408|20%|
|ZBRA|Zebra Technologies Corp.|0.4|13|30%|14.5|4%|93%|2,750|19099%|
|ZIXI|Zix Corp.|0.1|2|5%|-3.8|-34%|51%|82|1421%|
|ZLC|Zale Corp.|9.1|6|59%|6.3|6%|39%|1,393|6%|
|ZMH|Zimmer Holdings Inc.|0.5|3|26%|13.7|4%|52%|17,071|641%|



_Source: Lehman Brothers, Compustat._ 

## **Figure A4: Median values of variables for sector sub-groups of the S&P 1500 Index** 

|**Sector No.**|**Sector**|**Book to Market**|**EV / EBITDA**|**FCF Yield**|**Capex growth**|**Mkt Value ($MM) FCF Variability**|**Mkt Value ($MM) FCF Variability**|
|---|---|---|---|---|---|---|---|
|Universe|S&P 1500|39%|10.0|3.4%|12.7%|2,348|19.0%|
|1|Commercial Services|38%|10.1|3.5%|10.1%|1,097|35.9%|
|2|Technology Services|34%|11.7|5.3%|12.5%|1,673|50.5%|
|3|Health Services|29%|13.5|3.5%|13.6%|3,056|22.4%|
|4|Non-Energy Minerals|39%|7.0|3.5%|25.3%|3,928|19.8%|
|5|Distribution Services|44%|10.6|2.9%|-4.5%|1,553|13.5%|
|6|Consumer Non-Durables|40%|9.3|3.0%|11.3%|3,325|18.4%|
|8|Consumer Durables|49%|8.8|2.6%|15.6%|1,464|26.0%|
|9|Transportation|45%|8.9|1.8%|9.2%|2,301|28.0%|
|10|Industrial Services|41%|15.1|3.0%|11.7%|1,961|13.6%|
|13|Communications|44%|12.6|3.9%|11.9%|1,436|19.6%|



_Source: Lehman Brothers, Compustat._ 

January 9, 2006 

35 

**==> picture [612 x 121] intentionally omitted <==**

The views expressed in this report accurately reflect the personal views of Mukundan Devarajan, Cong Minh Trinh, Bodha Bhattacharya, David Heike and Mark Pomper, the primary analysts responsible for this report, about the subject securities or issuers referred to herein, and no part of such analyst's compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed herein. 

Any reports referenced herein published after 14 April 2003 have been certified in accordance with Regulation AC. To obtain copies of these reports and their certifications, please contact Valerie Monchi (vmonchi@lehman.com; 212-526-3173) or Larry Pindyck (lpindyck@lehman.com; 212-526-6268). 

Lehman Brothers Inc. and any affiliate may have a position in the instruments or the Company discussed in this report. The Firm's interests may conflict with the interests of an investor in those instruments. 

The research analysts responsible for preparing this report receive compensation based upon various factors, including, among other things, the quality of their work, firm revenues, including trading, competitive factors and client feedback. 

Lehman Brothers usually makes a market in the securities mentioned in this report. These companies are current investment banking clients of Lehman Brothers or companies for which Lehman Brothers would like to perform investment banking services. 

This material has been prepared and/or issued by Lehman Brothers Inc., member SIPC, and/or one of its affiliates (“Lehman Brothers”) and has been approved by Lehman Brothers International (Europe), authorised and regulated by the Financial Services Authority, in connection with its distribution in the European Economic Area. This material is distributed in Japan by Lehman Brothers Japan Inc., and in Hong Kong by Lehman Brothers Asia Limited. This material is distributed in Australia by Lehman Brothers Australia Pty Limited, and in Singapore by Lehman Brothers Inc., Singapore Branch (LBIS). Where this material is distributed by LBIS, please note that it is intended for general circulation only and the recommendations contained herein do not take into account the specific investment objectives, financial situation or particular needs of any particular person. An investor should consult his Lehman Brothers representative regarding the suitability of the product and take into account his specific investment objectives, financial situation or particular needs before he makes a commitment to purchase the investment product. This material is distributed in Korea by Lehman Brothers International (Europe) Seoul Branch. This document is for information purposes only and it should not be regarded as an offer to sell or as a solicitation of an offer to buy the securities or other instruments mentioned in it. No part of this document may be reproduced in any manner without the written permission of Lehman Brothers. We do not represent that this information, including any third party information, is accurate or complete and it should not be relied upon as such. It is provided with the understanding that Lehman Brothers is not acting in a fiduciary capacity. Opinions expressed herein reflect the opinion of Lehman Brothers and are subject to change without notice. The products mentioned in this document may not be eligible for sale in some states or countries, and they may not be suitable for all types of investors. If an investor has any doubts about product suitability, he should consult his Lehman Brothers representative. The value of and the income produced by products may fluctuate, so that an investor may get back less than he invested. Value and income may be adversely affected by exchange rates, interest rates, or other factors. Past performance is not necessarily indicative of future results. If a product is income producing, part of the capital invested may be used to pay that income. Lehman Brothers may, from time to time, perform investment banking or other services for, or solicit investment banking or other business from any company mentioned in this document. © 2006 Lehman Brothers. All rights reserved. Additional information is available on request. Please contact a Lehman Brothers entity in your home jurisdictio **n.** 

