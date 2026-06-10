SPONSORED EDUCATIONAL FEATURE 

## Next-generation credit curves 

Risk _has carried much debate recently about the curves to be used for discounting derivatives transactions. Here, Lindsey Matthews and Luca Bosatta from UBS Delta, the portfolio analysis system provider, present a related new methodology for calibrating credit curves – for issuers, sectors and markets_ 

Fixed-income risk analysis requires credit curves to be built from market prices daily, ideally for every issuer and seniority. In practice, spread curves are often built for groups of issuers, by rating and industry, due to the lack of liquid data points. Where individual spread curves are built (such as in UBS Delta), they are separated by currency due to apparent differences between trading of bonds in different currencies, and bond spread curves are built separately from credit default swap (CDS) curves. 

Based on detailed analysis of thousands of bond and CDS price histories, UBS Delta has developed a new approach for bootstrapping credit fixed-income curves, building unified hazard rate curves for each issuer and seniority, by combining market prices of CDSs and bonds across multiple currencies. The basis between currencies and instruments – bond versus CDS – is estimated simultaneously and consistently. 

We use these individual issuer curves to derive more stable and robust market, sector and region curves (‘market curves’). Comparing individual issuers with market curves also allows us to show market-implied ratings. 

## **Single-issuer curves** 

We believe – and the experience of the last few years bears out – that credit fixed-income risk analysis should be based on calibrations at the level of the individual issuer and seniority. Broadrating or sector-based approaches do not capture issuer level idiosyncrasies and diversification, and do not support analysis of issuer risk or concentration risk. 

There are, however, many examples of issuers only issuing a few bonds in a given currency, where our current approach is to use comparable securities and build a market/sector curve to complete the issuer curve. For example, figure 1 shows a bond spread curve for such an issuer – BMW issuing in GBP. The grey squares represent asset swap margins over Libor for bonds, the red line is the z-spread curve over Libor for BMW in GBP, and the blue curve is a proxy curve – in this case GBP corporate single A rated issuers. Beyond six years, the BMW curve is extrapolated using the proxy curve, enabling the risk management of positions that have longerdated, unlisted or illiquid GBP exposure to BMW. 

**==> picture [245 x 309] intentionally omitted <==**

**----- Start of picture text -----**<br>
1  Spread curve for BMW in GBP, 28 August 2012<br>240<br>200<br>160<br>g 120<br>F 80 ——— BMW GBP bond z-spread curve<br>GBP Corp single-A z-spread curve<br>40<br>0<br>0 10 20 30 40 50<br>Maturity<br>2 BMW senior CDSs and spreads to Libor in GBP and EUR,<br>28 August 2012<br>180 BMW AG (EUR, senior bond) August 28, 2012<br>BMW AG (EUR, CDS), August 28, 2012<br>140 BMW AG (GBP, senior bond), August 28, 2012<br>100<br>60<br>20<br>    0<br>0 2 4 6 8 10<br>Source: UBS Delta<br>Source: UBS Delta, Markit<br>**----- End of picture text -----**<br>


quite distinctly in different currencies even for the same issuer. Figure 2 shows this for BMW issuing in GBP and EUR and for BMW CDSs. Note that these three curves are built independently, without any of them influencing any other. 

Based on histories of the five-year tenor, the average correlation between the spread moves on these curves is less than 30%. A fixed-income risk model based on spreads at the individual issuer level would likely treat these as three separate sources of risk. 

## **Single issuer – Multiple currencies and instruments** 

Single-issuer curves, such as that presented in figure 1, could be improved by using other currencies of bonds issued by the same entity, as well as CDSs referencing that entity. However, this has historically proven difficult to implement. Spreads on bonds can differ quite significantly from CDS premia, and bond spreads trade 

## **A new approach – Unified hazard-rate curves** 

We address these and related risk-modelling problems by implementing a unified hazard-rate-based approach that jointly estimates curves across multiple currencies of bonds and CDSs, rather than building totally separate spread curves (see figure 3). Bond spreads and CDS quotes are not directly comparable due 

OTC DERIVATIVES CLEARING 

SPONSORED ROUNDTABLE 

**==> picture [227 x 150] intentionally omitted <==**

**----- Start of picture text -----**<br>
3 BMW GBP hazard rate curve, 28 August 2012<br>300<br>250<br>200<br>150 GBP bond<br>AUD bond<br>CAD bond<br>100 CHF bondEUR bond<br>NOK bond<br>EUR CDS<br>50 Unified<br>Europe ex-UK/<br>automobiles & parts/A2<br>0<br>0  5   10   15   20   25   30<br>Maturity<br>Hazard rate<br>Source: UBS Delta, Markit<br>**----- End of picture text -----**<br>


to differences in how the instruments are funded and differences in cashflow structure. To tackle this, we treat bonds consistently with CDSs by allowing two scenarios – default and no default – and discounting the probability weighted values. Using this approach, we infer a term structure of market-implied default probabilities from the prices of instruments. Deriving hazard rates puts the various instruments in comparable terms, especially as the discounting rates we use to bootstrap the hazard rates are market funding rates, derived from overnight indexed swap rates and from cross-currency basis swaps. 

For each issuer, we use bond prices in all issued currencies and CDS quotes as inputs to the joint estimation of one hazardrate curve and the basis for each currency and instrument type. Figure 3 shows the hazard-rate curve for BMW issuing in GBP for August 28, 2012. This is built using bond prices for BMW senior debt issued in GBP, as well as AUD, CAD, CHF, EUR and NOK, along with the CDS quotes referencing BMW senior debt. The two blue squares represent two of the three BMW GBP bonds that were used previously. In this new approach, bringing more data points to an issuer’s curve, we are able to raise the minimum liquidity requirements and the third bond is no longer used. The other points are the other quotes adjusted by their basis to GBP to show 

**==> picture [244 x 131] intentionally omitted <==**

**----- Start of picture text -----**<br>
4 History of five-year implied CDS for five currencies<br>of issue<br>1.60 AUD bonds EUR bonds GBP bonds<br>JPY bonds USD bonds<br>1.40<br>1.20<br>1.00<br>0.80<br>0.60<br>0.40<br>0.20<br>0.00<br>Aug 2011 Nov 2011 Feb 2012 May 2012 Aug 2012<br>Five-year CDS implied by hazard rate (%)<br>Source: UBS Delta<br>**----- End of picture text -----**<br>


how they contribute to the _shape_ of the GBP curve. 

Through the joint estimation process, the hazard rates implied by all of the other asset prices provide ‘support’ to the GBP curve, enabling a more robust and stable curve to be built. If one of the GBP bonds was to become illiquid or experience a price spike, we would not see the whole curve shift as significantly as we would have seen under a traditional methodology, as detailed above. For comparison, the hazard rate at the long end of the curve translates to a z-spread of approximately 115 basis points (bp) over Libor for BMW in GBP versus more than 200bp seen using the sector proxy curve in figure 1. 

## **Why hazard rates?** 

Hazard-rate curves can be translated into implied CDS terms as seen in figure 4, which shows implied CDS levels, derived from the unified hazard-rate curve and the basis for each of five currencies of issue, for another high-grade issuer. The implied CDS curves in figure 4 show very similar behaviour over time. The correlation between the spread moves is now averaging well over 60% and the unified hazard-rate process has much greater explanatory power for the issuer’s credit risk than traditional single currency spread to Libor curves (such as z-spread). Figure 5 shows the z-spreads over Libor for the five curves above, and we see much less correlation between these spreads than we do with the hazard rates – with the average now below 30%. 

## UBS Delta & D-Curves 

UBS Delta is our award-winning[1] portfolio analysis and risk management system. Clients use UBS Delta to measure and manage risk, attribute performance and optimise portfolios across asset classes. Risk measures include sensitivities, deltas and other greeks, value-at-risk, volatility and tracking error, full revaluation scenario analysis, solvency and shortfall risk, capital analytics, and liquidity scoring. 

UBS Delta’s new _“D-Curves – the next generation in fixed-income credit curves”_ were used to generate the illustrations in this article. These have been developed to ensure UBS Delta’s fixed-income model best represents the risk exposures of our clients. D-Curves will soon be available to view as part of the UBS Delta service or independently. 

## This new approach has many advantages: 

have much greater correlation at the issuer level, improving risk modelling. We can show bond-implied CDS curves for issuers that have no CDS trades referencing them. 

Market curves are built as consistent surfaces for every rating and maturity, giving greater granularity of coverage and significantly reducing jumps due to rating migration. 

CDS or spread curves can be calibrated for sectors and ratings where there are few or no traded instruments. 

Market-implied ratings are generated by comparing issue curves with market curves. 

## It should be noted that there are disadvantages: 

~~oo~~ Unified curves use more data points and so give more robust and stable Embracing this approach is challenging as it requires a revision to the way issuer curves, requiring less recourse to broad market proxy curves. people think about credit valuation and credit spreads. 

~~o~~ Hazard rates, combined with market-derived funding curves, allow bond Oo and CDS levels to be directly compared using a consistent measure. 

Using these curves for portfolio risk would entail alterations to the risk model to fit the methodology. 

Credit instruments are benchmarked against market-derived funding curves, across multiple currencies, giving greater insight into how markets actually trade. 

Past performance is not necessarily indicative of future performance. Prior to entering into a transaction, you should consult with your own legal, regulatory, tax, financial and accounting advisers to the extent you deem necessary to make your own investment, hedging and trading decisions. 

> _1 Recent award wins include Best actuarial software/risk engine by_ Insurance Risk _2012 Awards and Best broker-supplied tool/technology in the 2012_ Buy-Side Technology _Awards_ 

We derive currency-specific spread curves and implied CDS curves, which 

SPONSORED EDUCATIONAL FEATURE 

**==> picture [241 x 345] intentionally omitted <==**

**----- Start of picture text -----**<br>
5 History of five-year z-spreads to Libor<br>1.10 AUD bonds EUR bonds GBP bonds<br>JPY bonds USD bonds<br>0.90<br>0.70<br>0.50<br>0.30<br>0.10<br>-0.10<br>-0.30<br>-0.50<br>6 Market surface for Europe ex-UK, automobiles and<br>parts, 28 August 2012<br>Europe ex-UK autos sector 1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>24 18 0.1<br>14<br>10<br>Maturity (years) 6 2 0<br>0<br>Composite rating<br>Aug-11 Nov-11 Feb-12 May-12 Aug-12<br>AAA   AA1   AA2   AA3   A1     A2     A3     BBB1  BBB2  BBB3  BB1   BB2   BB3   B1     B2     B3     CCC1  CCC2  CCC3  CC    C<br>Five-year z-spreads (%)<br>Source: UBS Delta<br>Cumulative default probability<br>Source: UBS Delta<br>**----- End of picture text -----**<br>


We build a unified hazard-rate curve and the basis for each currency and instrument type, every day, for thousands of issuers. Each of these can be viewed as hazard rate, implied CDS, par spread or z-spread curves, each with multi-year daily histories. 

## **Market surfaces and artificial ratings migration volatility** 

Using the issuer curves constructed above, we build curves for sectors and whole markets, such as the Europe ex-UK/automobiles and parts/A2 curve shown as the dotted line in figure 3. A traditional approach is to build an independent market curve for each sector and rating. These sector-ratings curves often exhibit large step jumps and high volatility – not due to underlying market moves, but purely from ratings jumps and classification changes. In order to make market curves more useful, we actually build market surfaces, populating every rating and maturity. The sector curve shown in figure 3 is a line for that rating drawn across the hazardrate surface. We only build a market surface for a region/sector where we have sufficient data to populate the whole surface. Figure 6 shows the market surface for Europe ex-UK/automobiles and parts, rescaled to show cumulative default frequency. Key to our approach is that this surface is built as one surface, not rating by rating. In constructing the surface, each rating point influences the surface at the ratings points either side of them, with this influence reducing as the distance increases. The surface is calibrated as a whole, rather than each rating slice in isolation. This, together with the more robust underlying issuer curves, gives us market curves that are much more granular than with the traditional approach. 

**==> picture [201 x 34] intentionally omitted <==**

**----- Start of picture text -----**<br>
7 Market-implied rating history for an A3-rated<br>automobiles/parts sector issuer, five-year point,<br>August 2011 – August 2012<br>**----- End of picture text -----**<br>


**==> picture [245 x 154] intentionally omitted <==**

**----- Start of picture text -----**<br>
2012<br>AAA<br>AA1<br>AA2<br>AA3<br>A1<br>A2<br>A3<br>BBB1<br>BBB2<br>BBB3<br>BB1<br>BB2<br>BB3<br>B1<br>B2 Composite/median<br>B3<br>Global/all industries<br>CCC1<br>CCC2 Europe ex-UK/<br>CCC3 automobiles & parts<br>CC<br>C<br>Shown versus both the European automobiles and the global all-industries surfaces<br>Market-implied rating<br>Source: UBS Delta<br>**----- End of picture text -----**<br>


This approach also reduces the artificial jumps seen in ratingsbased curves from rating migrations, and it allows for the generation of market CDS curves for region-sector-rating combinations where no names are actually trading, such as the A1 curve that could be drawn across this surface. This has applications in many situations including, for example, marking of credit valuation adjustment. 

## **Market-implied ratings** 

Comparing hazard rate tenor points from individual issuer curves with the hazard-rate market surfaces allows us to derive market-implied ratings. These are the ratings that would make the individual issuer curve lie on the market surface at that tenor. Market-implied ratings can be based on the user’s chosen market curve, as shown in figure 7. 

_This material has no regard to the specific investment objectives, financial situation or particular needs of any specific recipient and is published solely for information purposes. No representation or warranty, either express or implied, is provided in relation to the accuracy, completeness or reliability of the information contained herein, nor is it intended to be a complete statement or summary of the developments referred to in this material. This material does not constitute an offer to sell or a solicitation to offer to buy or sell any securities or investment instruments, to effect any transactions or to conclude any legal act of any kind whatsoever. Nothing herein shall limit or restrict the particular terms of any specific offering. No offer of any interest in any product will be made in any jurisdiction in which the offer, solicitation or sale is not permitted, nor to any person to whom it is unlawful to make such offer, solicitation or sale. Not all products and services are available to citizens or residents of all countries. Any opinions expressed in this material are subject to change without notice and may differ or be contrary to opinions expressed by other business areas or divisions of UBS AG or its affiliates (UBS) as a result of using different assumptions and criteria. UBS is under no obligation to update or keep current the information contained herein. Neither UBS AG nor any of its affiliates, directors, employees or agents accepts any liability for any loss or damage arising out of the use of all or any part of this material._ 

_© UBS 2012. The key symbol and UBS are among the registered and unregistered trademarks of UBS. Other marks may be trademarks of their respective owners. All rights reserved._ 

## Contact 

Lindsey Matthews Managing Director, Head of Client Development, UBS Delta 

Luca Bosatta Managing Director, Head of Risk Modelling, UBS Delta E: delta@ubs.com _www.ubs.com/delta_ 

See UBS Delta on _risklibrary.net_ – more on curves coming in January 2013 

Reproduced with permission of the copyright owner. Further reproduction prohibited without permission. 

