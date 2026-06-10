**European Single Names – Framework/Template for Fundamental Analysis** 

## **Table of Contents** 

**[Defining the universe and sector/country classification]** .............................................................. 1 Step 1: Building the factset ..................................................................................................................... 1 _Step 1A: Accounting/Fundamental Data_ ............................................................................................ 1 _Step 1B: Forward-looking estimates/Forecasts_ .................................................................................. 2 _Step 1C: Sector/Industry/Macroeconomic Data_ ................................................................................. 4 Step 2: Calculating key ratios/multiples ................................................................................................. 5 _Step 2A: Key ratios/Growth rates_ ....................................................................................................... 5 _Step 2B: Valuation/Multiples_ .............................................................................................................. 7 Step 3: “ Static” relative value analysis ................................................................................................... 8 _Step 3A: Pricing data – CDS spreads_ ................................................................................................... 8 _Step 3B: Spread per turn of leverage (LTM & NTM)_ ........................................................................... 8 _Step 3C: Spread vs. interest coverage ratio (LTM & NTM)_ .................................................................. 9 _Step 3D: Spread vs. rating_ ................................................................................................................. 10 _[Step 3E: Spread vs. absolute level of total debt (size of capital structure)]_ ..................................... 10 _[Step 3F: Composite relative value metric]_ ....................................................................................... 10 Step 4: “Dynamic” relative value analysis – Model inferences/Stress tests ......................................... 11 _Step 4A: Lehman Lever_ ...................................................................................................................... 11 _Step 4B: Cyclicality vs. Liquidity_ ........................................................................................................ 11 _Step 4C: Ratings drifts screen_ ............................................................................................................ 12 _[Step 4D: To come]_ ............................................................................................................................ 13 Step 5: Outputs and report generation ................................................................................................ 14 _Step 5A: Universe-/Sector-level time series outputs_ ......................................................................... 14 _Step 5B: Cross-sectional reports of sectors based on current data_ ................................................... 14 _Step 5C: Intra-sector reports based on current data_ ........................................................................ 14 

## **European Single Names – Framework/Template for Fundamental Analysis** 

Purpose: The purpose of this document is to lay out a detailed outline/specification that would allow us to build a comprehensive and relatively “hands-free” framework for analysing European single names (primarily corporates) from a fundamental credit analysis perspective. There are two primary work streams relating to this project: (a) gathering, organizing, storing and maintaining the required data (building the “ factset”) and (b) developing, testing and refining a set of tools and models that would enable us to translate the fundamental data into various measures of value (and, in particular, for assessing relative value). 

## ****[Defining the universe and sector/country classification]**** 

## **Step 1: Building the factset** 

To start building a factset from scratch, we need to consider three things: (a) the type of data we will need, (b) sources of that data and (c) the time period for which we will require that information. These are outlined in the table below and explained in further detail in the following sections. 

|**Date Type**|**Source**|**Required History**|
|---|---|---|
|Single Names – Accounting/<br>Fundamental|Bloomberg, Capital IQ, CS Holt|Minimum of 3 years<br>(in some cases,7-10years)|
|Single Names – Forward-looking<br>estimates/Forecasts|Bloomberg, Capital IQ, Analyst<br>research reports|Not applicable|
|Sector/Industry/<br>Macroeconomic|Analyst research reports,<br>Datamonitor-like publications,<br>Rating agency research|Not applicable|



## _Step 1A: Accounting/Fundamental Data_ 

Accounting/fundamental data is the most crucial as well as the bulk of the information we will need for single name fundamental analysis. This is also the “easiest” data to acquire – as it is directly sourced from publicly available company financial statements. 

We can separate out the sources of this data into two broad categories. Bloomberg offers a relatively easy way for downloading this information at no additional cost, through their Excel AddIns. The biggest advantage of services like Capital IQ and CS Holt over Bloomberg is that they provide the data in a cleaned format – in particular, they make apples to apples comparison across companies and sectors easier/more robust by applying filters that standardize and account for name/sector-specific considerations. 

At the outset, we can begin by using Bloomberg data for our purposes while allowing us the flexibility – in terms of database structure and analytical process – to add higher quality data at a subsequent stage. 

With reference to the required history of information, for a large part of what we need to do, the last three years of history (i.e., annual financial statements for 2009, 2010 and 2011) and quarterly data for the most recent year (2011 and Q1 2012 as and when it starts to become available) should 

1 

be adequate. Note that we will need the quarterly period data in order to calculate figures on a LTM (last-twelve-months) basis. See table below for the exact list/specification of data we will need to download from Bloomberg. 

However, there are certain performance and valuation measures (e.g. EBITDA, EV/EBITDA) that we will need to download for a longer period of time (7-10 years). These are highlighted in the table accordingly. One of the reasons for downloading a longer time series with respect to these measures is that it will allow us to analyse/stress companies across the business cycle by looking at prior experiences of peak to trough changes in performance and valuation (also useful for debt vs. equity analysis as it allows us to gauge which market may be relatively more optimistic/pessimistic with respect to the future prospects of a company). 

_Table 1: Single-name accounting data to be downloaded from Bloomberg **[Attach spreadsheet]**_ 

|**Date Type**|**Bloomberg Syntax**|**Required History**|
|---|---|---|
|Total Revenue|[…]|3 years|
|[…]|[…]|[…]|
|EBITDA|[…]|[7 – 10 years]|
|[…]|[…]|[…]|
|Total cash and short-term<br>investments|[…]|3 years|
|[…]|[…]|[…]|
|Net debt|[…]|[7 – 10 years]|
|[…]|[…]|[…]|
|Cash from operations|[…]|3 years|
|Free cash flow|[…]|[7 – 10 years]|
|Debt schedule in Year 1|[…]|[…]|
|[…]|[…]|[…]|
|Market capitalisation|[…]|Current|



**[Need to consider specific sector issues – e.g., operating leases/rent for retail/consumer]** 

_Step 1B: Forward-looking estimates/Forecasts_ 

Once we have the historical data on hand, the next step of the process is to gather forward-looking estimates/forecasts from analysts – again, this is focused on data at the single name/company level. We can separate this process into two buckets. 

With reference to the first bucket, we can again use Bloomberg to download forecasts in a relatively easy fashion. However, there are two points to note here: (a) these estimates flow through from equity research analysts only and (b) they are not always very detailed (and in cases where they are, the quality is questionable as it may be based on too few analysts – not all equity analysts submit 

2 

detailed forecasts to Bloomberg). The table below contains the forward-looking estimates that we will need to download from Bloomberg – they are all income statement items. Note that annual forecasts will be adequate – it will not be necessary to download quarterly estimates. 

_Table 2: Single-name forward-looking estimates/forecasts to be downloaded from Bloomberg **[Attach spreadsheet]**_ 

|**Date Type**|**Bloomberg Syntax**|**Number of years out**|
|---|---|---|
|Total revenue|[…]|3 years|
|Gross profit|[…]|3 years|
|EBIT|[…]|3 years|
|EBITDA|[…]|3 years|
|Net income|[…]|[…]|



The second bucket then addresses the shortcomings discussed above by including credit analyst estimates. This is a more labour-intensive process as this data is not available in any electronic form. For most of the names in the universe, we are likely to get only one set of estimates/financial model per year (in the annual outlook); some others may be periodic. 

In order to gather this data, we can do a one-time exercise of extracting all the estimates from the annual outlooks with respect to the names in our universe. We can then, on a [monthly] basis, gather updates to the extent they are available. 

_Figure 1: Example of credit analyst forecast model for single name_ 

3 

**[Add section on what we need to do to simplify the forecast information – i.e. we calculate min, max, median from all the estimates and use that for the analysis. For example, we can take median net debt estimates and median EBITDA estimates to work out estimates of net leverage (how does this compare to just taking median of available net leverage estimates]** 

## _Step 1C: Sector/Industry/Macroeconomic Data_ 

The final step of the data collection process is gathering more macro data – sector- or economy-wide – and is also likely to be the most ad hoc part of the process. The primary reason for this part of this exercise is to allow us to sense check/stress individual company estimates vs. sector/macro trends. For example, analyst estimates suggest that revenue growth at Fiat will be x%; is this reasonable given what we know about forecasts for auto production and estimates for growth in markets that Fiat is present in? 

Certain components of the data can once again be downloaded from Bloomberg; for example, individual country growth rates. 

**[Add table 3 outlining what data to download from Bloomberg – syntax, forecast period, etc.]** _**[Attach spreadsheet]**_ 

|**Date Type**|**Bloomberg Syntax**|**Number of years**|
|---|---|---|
|[…]|[…]|[…]|
|[…]|[…]|[…]|



The remainder of the data will come from analyst research reports. As discussed in section above, we can review this research to gather updates on a [monthly] basis. 

4 

_Figure 2: Example of industry forecast data in credit analyst research report_ 

## **Step 2: Calculating key ratios/multiples** 

After collecting the “raw” data, we need to then transform these figures into more meaningful metrics that we can use to analyse companies both from a historical perspective as well as a on a cross-section basis. In general, the ratios and growth rates identified below are operational metrics relating to solvency and profitability, whereas the multiples are valuation measures. The tables that follow provide a detailed outline of all the metrics we need to calculate, the formula for calculating them, as well as the time period for which we require those calculations. 

## _Step 2A: Key ratios/Growth rates_ 

_Table 4: Capitalisation and long-term solvency_ 

|**Metric**|**Formula**(Update using exact<br>syntax from Table 1)|**Period**|
|---|---|---|
|Total debt/Equity||LTM/-3y/+3y|
|Long-term debt/Equity||LTM/-3y/+3y|
|Liabilities/Assets||LTM/-3y/+3y|
|EBIT/Interest expense||[7 -10 years]|
|EBITDA/Interest expense||LTM/-3y/+3y|
|(EBITDA – Capex)/Interest expense||LTM/-3y/+3y|
|Funds from operations/net debt||LTM/-3y/+3y|
|Funds from operations/total debt||LTM/-3y/+3y|
|Total debt/EBITDA||[7 -10 years]|
|Net debt/EBITDA||[7 -10 years]|
|[Z-Score]||LTM/-3y/+3y|
|[Operating leverage]||[…]|
|[Financial leverage]||[…]|



5 

_Table 5: Liquidity_ 

|**Metric**|**Formula**(Update using exact<br>syntax from Table 1)|**Period**|
|---|---|---|
|Current ratio||LTM/-3y/+3y|
|Quick ratio||LTM/-3y/+3y|
|Cash from operations/Current<br>liabilities||LTM/-3y/+3y|
|Average days sales outstanding||LTM/-3y/+3y|
|Average days inventory outstanding||LTM/-3y/+3y|
|Average days payables outstanding||LTM/-3y/+3y|
|Average cash conversion cycle||LTM/-3y/+3y|



_Table 6: Profitability and margins_ 

|**Metric**|**Formula**(Update using exact<br>syntax from Table 1)|**Period**|
|---|---|---|
|Return on assets||LTM/-3y/+3y|
|Return on capital||LTM/-3y/+3y|
|Return on equity||LTM/-3y/+3y|
|Gross margin||LTM/-3y/+3y|
|EBITDA margin||LTM/-3y/+3y|
|EBIT margin||LTM/-3y/+3y|
|Net income margin||LTM/-3y/+3y|
|Free cash flow margin||LTM/-3y/+3y|



6 

_Table 7: Growth rates/CAGR **[Need to define over what period]**_ 

|**Metric**|**Formula**(Update using exact<br>syntax from Table 1)|**Period**|
|---|---|---|
|Revenue||YoY;-3y/+3y|
|Gross profit||YoY;-3y/+3y|
|EBITDA||[YoY;-[ ]y/+[ ]y]|
|EBIT||[YoY;-[ ]y/+[ ]y]|
|Net income||YoY;-3y/+3y|
|Book value||YoY;-3y/+3y|
|Cash flow from operations||YoY;-3y/+3y|
|Capex||YoY;-3y/+3y|
|Free cash flow||[YoY;-[ ]y/+[ ]y]|



_Step 2B: Valuation/Multiples_ 

_Table 8: Valuation multiples_ 

|**Metric**|**Formula**(Update using exact<br>syntax from Table 1)|**Period**|
|---|---|---|
|Enterprise value/Total revenue||LTM/NTM;-1y/+1y|
|Enterprise value/EBITDA||LTM/NTM;-1y/+1y|
|Enterprise value/EBIT||LTM/NTM;-1y/+1y|
|Price/Earning||LTM/NTM;-1y/+1y|
|Price/Book value||LTM/NTM;-1y/+1y|
|[Value (Enterprise/Equity)/Cash flow]||LTM/NTM;-1y/+1y|



7 

**Step 3: “ Static” relative value analysis** 

The next step in the process s is to marry the accounting/fundamental data gathered in steps 1 and 2 with pricing data. The basic framework here is to express credit spreads (current pricing) relative to various relevant accounting measures/ratios. This then allows for comparisons both inter- and intrasectors. See Step 3B for a hypothetical example. 

## _Step 3A: Pricing data – CDS spreads_ 

For the universe defined earlier, we need to download pricing data – for static relative value purposes, most recent price points will be adequate. However, we should download historical data (suggest three to five years) so that we can look at how each of the measures highlighted below and have changed through time. 

Initially, we can make do with 5Y CDS data, which we can download quite easily from Bloomberg. ** [Add/attach excel spreadsheet template for downloading historical end of day CDS levels for the defined universe]** At a later stage, we can expand this analysis to include bond pricing/spread data as well. 

## _Step 3B: Spread per turn of leverage (LTM & NTM)_ 

In Step 2A; Table 4 we calculate net debt/EBITDA – this is the leverage ratio which we will use. In addition, from Step 3A, we will have 5Y CDS levels. From this we can calculate spread per turn of leverage: 

Spread per turn of leverage (SPL) = 5Y CDS Spread / (Net Debt/EBITDA). 

While we will be using this measure for various reports/outputs as outlined in Section 5 (e.g., ranking names by SPL for a given sector), the most direct/immediate use of this information will be for relative value analysis within a given sector. More specifically, we will look at the magnitude of the differential between the SPL of a single company and the SPL of the sector to (a) identify names which are either expensive or cheap vs. sector and (b) derive a crude approximation of what the theoretical valuation of a company would be if we price the company’s leverage ratio based on the sector-level statistic. 

Note that we will look at this measure in two ways: (a) using historical data, i.e., the most recent net debt/EBITDA ratio available and (b) also using forecasted net debt/EBITDA ratio, which we will have from Step 1B. 

8 

_Table 9: Stylised example of SPL relative value analysis_ 

|**Company X**|**Spread**|**Net debt/EBITDA**<br>**(LTM)**|**SPL**|**Average SPL**<br>**(ex-Company X)**|**“Predicted”**<br>**Spread**|**Actual -**<br>**Predicted**|
|---|---|---|---|---|---|---|
|A|240|1.50x|160|173|260|(20)|
|B|350|2.25x|156|174|393|(43)|
|C|330|1.65x|200|163|270|60|
|D|290|1.75x|166|172|301|(11)|
|E|310|1.80x|172|170|307|3|
|Average|304|1.79x|171|n/a|n/a|n/a|



Based on the results in Table 9 above, we can infer that Company C is relatively cheap whereas Company B is expensive relative to the sector. 

The second part of this analysis will use net debt/EBITDA forecast from analyst estimates as the denominator in the calculation so that we can make inferences about relative valuation given market expectations about the companies’ deleveraging/releveraging prospects over the next year. 

_Step 3C: Spread vs. interest coverage ratio (LTM & NTM)_ 

Spread vs. interest coverage ratio is another tool we will use to assess relative value. The framework is identical to that described above for SPL; with the difference being that we will use a different denominator for the calculation – the interest coverage ratio, which will have computed in Step 2A; Table 4. Unlike in the case of SPL, we would expect a negative correlation between spreads and the interest coverage ratio. Specifically, the formula for this measure is: 

Spread vs. Interest coverage ratio (ICR) = 5Y CDS Spread / (EBIT/Interest expense) 

9 

_Step 3D: Spread vs. rating_ 

**[…take average of three and round down to derive numerical bucket?... ]** 

_Table 10: Mapping credit agency ratings to numerical buckets_ 

|**Bucket**|**S&P**|**Moody’s**|**Fitch**|
|---|---|---|---|
|1|AAA|Aaa|AAA|
|2|AA+|Aa1|AA+|
|3|AA|Aa2|AA|
|4|AA-|Aa3|AA-|
|5|A+|A1|A+|
|6|A|A2|A|
|7|A-|A3|A|
|8|BBB+|Baa1|BBB+|
|9|BBB|Baa2|BBB|
|10|BBB-|Baa3|BBB-|
|11|BB+|Ba1|BB+|
|12|BB|Ba2|BB|
|13|BB-|Ba3|BB-|
|14|B+|B1|B+|
|15|B|B2|B|
|16|B-|B3|B-|
|17|CCC+|Caa1|CCC|
|18|CCC|Caa2|n/a|
|19|CCC-|Caa3|n/a|



_[Step 3E: Spread vs. absolute level of total debt (size of capital structure)]_ 

[ ] 

_[Step 3F: Composite relative value metric]_ 

**[Do we average predicted spreads across these other measures? What are the alternatives to simplify the above criteria to a more easily screen-able metric? Weights for the different metrics...? ]** 

10 

## **Step 4: “Dynamic” relative value analysis – Model inferences/Stress tests** 

## [ ] 

_Step 4A: Lehman Lever_ 

## [ ] 

_Step 4B: Cyclicality vs. Liquidity_ 

[…particularly relevant for trades relating to theme of shorter/more volatile business cycles] 

- Goal: Identify level of decline in EBITDA over two-year period that will force companies to come to market for financing (measure of liquidity strength) 

- Inputs: cash on balance sheet, LTM EBITDA, LTM interest expense and LTM capex 

- Output: Estimate of available liquidity over two-year period 

- Assumptions : Company will need refinancing if (a) negative free cash flow (FCF) over the period burns through cash on balance sheet (i.e., cash balance on balance sheet becomes negative) or (b) available liquidity (cash on balance sheet) cannot cover bond and loan maturities over the period 

- Caveats: Data limitations on loan maturities and on liquidity available from revolving credit facilities and/or parent [How can we address this? Where can we get this data?] 

## [ ] 

## _Figure [ ]: Example of required output from cyclicality vs. liquidity analysis_ 

11 

_Step 4C: Ratings drifts screen_ 

[...derive regression-based relationships of credit ratings vs. fundamental credit ratings by sector; identify companies whose model ratings deviate significantly from actual rating  higher probability of ratings change; also helps differentiate between similarly rated credits in same sector] 

[Model derived for US issuers; what do we need to take into consideration to optimize this for European companies?] 

Two trade templates: 

- Focus on companies identified by model as upgrade or downgrade candidates but that are not currently on watch or outlook status even though the market is pricing in some rating change (evaluate using Moody’s bond market implied ratings) [Need to explain how we do this] 

- Look at companies where the market is not pricing in any rating change even though they are identified as potential upgrade or downgrade candidates by the model 

First Step – Model Specification 

- Explanatory variables: As defined in table below on a sector basis; based on LTM data 

- Dependent variable: Mapped credit rating (refer to Step 3D) 

## _Figure [ ]: Model specification for ratings drift screen_ 

12 

Second Step – Apply sector regression to single names and compare model ratings to actual ratings 

_Figure [ ]: Example output for ratings drift screen_ 

_[Step 4D: To come]_ 

[ ] 

13 

## **Step 5: Outputs and report generation** 

## [ ] 

_Step 5A: Universe-/Sector-level time series outputs_ 

_Figure [ ]: Indicative outputs of time-series data_ 

_Step 5B: Cross-sectional reports of sectors based on current data_ 

## [ ] 

_Step 5C: Intra-sector reports based on current data_ 

[ ] 

14 

