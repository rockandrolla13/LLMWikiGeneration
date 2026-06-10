Rainer Pullirsch 

## **Measuring Credit-Spread Risk on a Single Issuer Basis** 

## **Abstract** 

In diesem Artikel präsentieren wir ein Modell zur Messung von Credit-Spread Risiko auf Einzelemittentenbasis. Wir beschreiben detailiert eine Methode zur Berechnung von Zero-Coupon-Credit-Spreadkurven aus Bondquotierungen. Besonders betrachten wir die numerische Stabilität des Schätzverfahrens. Weiters berichten wir, weshalb Residualvarianzen benötigt werden, um das individuelle Verhalten einer spezifischen Anleihe zu berücksichtigen. Die Methode zur Berechnung der Residualvarianzen wird vorgestellt. Im Anschluss präsentieren wir das Verfahren der Abbildung einzelner Positionen im Portfolio auf die zur Verfügung stehenden Credit-Spreadkurven. Abschliessend zeigen wir noch ein paar Credit-Spread-Zeitreihen und beschreiben noch kurz die Value-atRisk (VAR) Berechnung. 

**Rainer Pullirsch** Bank Austria Creditanstalt 

_In this article we present a model for measuring credit-spread risk on a single issuer basis. We describe in detail a method to calculate zero-coupon credit-spread curves from bond quotations and focus especially on the numerical stability of the estimation procedure. We further report why residual variances are needed to take into account the individual behavior of a specific bond. The method how these residual variances are obtained is described. We continue by presenting the procedure of how the positions in the portfolio are mapped onto the available credit-spread curves. Finally we depict some credit-spread time-series and briefly describe the value-at-risk (VAR) calculation._ 

## **1 Introduction** 

Over the last decade of the previous millennium a rapid growth of the market for financial instruments related to credit risk was seen. At the beginning of this millennium the market for credit derivatives started booming. This development called for the need to quantify market risks for the trading of such instruments. The first credit derivatives which showed up on the financial markets were credit default swaps (CDS). A couple of years ago it was very hard to obtain market data for CDS which fulfilled the needs of risk management. That was the starting point to develop a model to measure credit-spread risk. The aim of the model was purely to capture the risk induced by changes of the credit-spreads, i.e. the market risk but not default risk. All products whose prices are determined or influenced by creditspreads needed to be covered. At that time these products were mainly bonds and CDS. The natural starting point therefore was to estimate credit-spread from bond quotations and build up time-series. In order to be able to price bonds and CDS the term-structure of credit-spreads is needed. This lead us to the necessity to model credit-spread curves. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

91 

Rainer Pullirsch 

The aim of the model which we describe in the following is to determine directly the zero coupon credit-spread curve for as many companies as possible from its traded bonds. To achieve this we strongly depend on the availability of liquidly traded bonds. In order to also take into account companies whose bonds are not traded liquidly we introduce a three level mapping procedure. 

In the following we start our presentation by explaining how we calculate zero coupon creditspread curves numerically from bond quotations. We continue by discussing the numerical stability and we introduce a measure to control it. We proceed with a section on the qualitative criteria for the input bond quotations. Furthermore, we present how we take into account pricing errors and the individual behavior of single bonds via residual variances. We continue by giving a detailed introduction to the mapping procedure. Finally we present typical time-series data of credit-spread curves and we briefly describe the value-at-risk calculation. 

## **2 Direct determination of zero coupon credit-spread curves** 

## **2.1 Riskless interest rates** 

The credit-spread of a bond is defined as the risk premium the issuer of a bond has to pay to the buyer. This risk premium induces an additional interest rate payment to the riskless interest rate and therefore a lower price of the bond. Thus in order to obtain credit-spreads one has to fix the riskless interest rate. A natural choice is offered by interest rates derived from government bonds. Nevertheless, investors have shifted to using (plain vanilla) interest rate swaps as the reference riskless curve. This shift could have resulted from several factors, see e.g. in Duffee 1996, Hull et. al. 2005, and Geyer et. al. 2004. 

A disadvantage of the swap-rate is that it actually entails credit risk from two sources, namely counterparty risk and the underlying floating payments being indexed to a defaultable LIBOR or EURIBOR rates. Nevertheless, interest rate swaps are the most liquidly traded interest rate products and reflect the current term structure of riskless interest rates most accurately on a slightly higher level. For this reason we employ riskless zero-coupon term structures derived from swap-rates. 

## **2.2 Algorithm to estimate zero-coupon credit-spread curves** 

In this section we describe the algorithm to estimate zero-coupon credit-spread curves for individual issuers from bond quotations. Using the face value _N_ , the time to maturity _T_ , the coupon _C_ and the zero-coupon swap-rate _r(t)_ the theoretical price _f_ of a bond follows from discounting its future cash-flows 

**==> picture [351 x 23] intentionally omitted <==**

where the index _i_ indicates the i-th bond of an issuer. To determine the values of the zero-coupon swap-rate at the cash-flow dates we use a cubic-spline interpolation method. To get the credit- 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

92 

Measuring Credit-Spread Risk on a Single Issuer Basis 

spread curve we add the credit-spread _s(t)_ to the zero-coupon swap-rate which modifies the price in Eq. (1) to 

**==> picture [351 x 22] intentionally omitted <==**

Using this price we obtain the credit-spread curve by minimizing the error function 

**==> picture [350 x 22] intentionally omitted <==**

where _P_ is the traded/quoted price. To make _E =_ 0 a determined system of equations for the creditspread curve one needs for a company which has emitted _Q_ bonds exactly _m = Q_ grid points for the credit-spread curve. The choice of the grid points takes the minimum and maximum time to maturity of the bonds into account. We use five different schemes to select equidistant grid points with distance _d_ . 

**==> picture [274 x 14] intentionally omitted <==**

- _tk_ = [ _{_ 0 _}, d,_ 2 _d, ..., md, {md_ + _}, {_ ( _m_ +1) _d}_ ] _, d_ =[max] _[i]_[(] _[ceil] m_[(] _[T][i]_[))] 

**==> picture [322 x 59] intentionally omitted <==**

- _tk_ = [ _{_ 0 _}, G,_ ( _G_ + _d_ ) _,_ ( _G_ +2 _d_ ) _, ...,_ ( _G_ +( _m−_ 1) _d_ ) _, {G_ +( _m−_ 1) _d_ + _}, {D}_ ] _, G_ =min _i_ ( _ceil_ ( _Ti_ )) _, D_ =max _i_ ( _ceil_ ( _Ti_ )) _, d_ =[max] _[i]_[(] _[f][loor] m−_ 1[(] _[T][i]_[))] _[−][G]_ 

Here ceil of a number is the closest larger integer and floor of a number denotes the closest smaller integer. Given a set of seven bonds with the following times to maturity in years: 1.2300; 3.4630; 2.1235; 19.1463; 12.4558; 9.1250; 6.4236. The above algorithm will yield the following grid points: 

- Schema 1: 0.0; 3.333; 6.667; 10.0; 13.333; 16.667; 20.0; {20.001}; {23.333}. 

- Schema 2: {0.0}; 2.857; 5.714; 8.571; 11.429; 14.286; 17.143; 20.0; {20.001}; {22.857}. 

- Schema 3: {0.0}; 2.5; 5.0; 7.5; 10.0; 12.5; 15.0; 17.5; {17.501}; {20.0}. 

- Schema 4: {0.0}; 1.0; 4.167; 7.333; 10.5; 13.667; 16.833; 20.0; {20.001}; {23.167}. 

- Schema 5: {0.0}; 2.0; 4.833; 7.667; 10.5; 13.333; 16.167; 19.0; {19.001}; {20.0}. 

The value of the credit-spread curve at the points in {} is not independently varied but is set to a fixed value. For the schemes 2–5 at _t =_ 0 the value is either calculated as the linearly extrapolated value from the second grid point using the average slope between the second and the third grid point or is set equal to zero if the resulting value is negative although the rest of the curve is positive. The value at the last two grid points is always set equal to the value at the preceding grid point. As we choose the spacing _є_ between the last grid point where the value is varied and 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

93 

Rainer Pullirsch 

_є_ = 0.001 the first where the value is fixed to be very small, e.g. , and by further setting the first derivative at the last point equal to zero. Thus we guarantee that we approximately continue the credit-spread curve constant. Here one should mention that the first derivative is also set to zero at _t =_ 0 . Although this cannot be justified by a specific model it actually does not have much influence on the curve. Between the grid points of the credit-spread curve the same interpolation method (i.e. cubic-spline interpolation) as used for the zero-coupon swap-rate is applied. 

From the credit-spread curve obtained we determine the values of the credit-spread curve at _t_ Є [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 25] (but within the actual maximum maturity of the underlying bonds) as the risk-factors in the value-at-risk calculation. 

## **2.3 Numerical stability** 

The choice of the grid points is further influenced by the numerical stability of the system of equations under consideration. To estimate the numerical stability the following criteria are taken into account (in the implemented algorithm only method (ii) is used): 

i) Condition number of a system of equations 

Given a determined system of linear equations _Ax = a_ the condition number _K = cond(A) ≥_ 1 of the matrix _A_ gives an estimate of the stability of the solution vector _x_ . Ideally _K =_ 1 should be fulfilled. In practice it is sufficient that the condition number is smaller than a least upper bound _Kmax_ , i.e. _K < Kmax_ . 

ii) Estimation of the variation of the credit-spread curve if the coupon is varied 

Given an under-determined system of equations to estimate the stability we have chosen the following approach. From the minimization 

**==> picture [351 x 26] intentionally omitted <==**

where[→] _s_ characterizes the values of the credit-spread curve at the grid points, it follows that 

**==> picture [352 x 31] intentionally omitted <==**

where the index _j_ of the spread indicates grid point _j_ . Under the assumption of a linear pricing function _f[ˆ] i_ ([→] _s_ ), which is roughly fulfilled for small credit-spreads _s_ and nottoo long time to maturity _Ti_ 

**==> picture [352 x 22] intentionally omitted <==**

This is just the expansion of the pricing function around[→] _s_ = 0 up to first order. Therefore it follows that 

**==> picture [345 x 29] intentionally omitted <==**

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

94 

Measuring Credit-Spread Risk on a Single Issuer Basis 

Using this in Eq. (5) one receives 

**==> picture [426 x 192] intentionally omitted <==**

With 

**==> picture [270 x 59] intentionally omitted <==**

and 

**==> picture [266 x 25] intentionally omitted <==**

it follows that 

**==> picture [403 x 28] intentionally omitted <==**

Since under the assumptions above 

**==> picture [278 x 22] intentionally omitted <==**

it follows that 

**==> picture [259 x 26] intentionally omitted <==**

and thus 

**==> picture [270 x 25] intentionally omitted <==**

Finally by using Γ( _Ci_ ) _∼_ Γ( _Ci_ + ∆ _Ci_ ) one obtains 

**==> picture [294 x 25] intentionally omitted <==**

if the system is numerically stable. Further if one uses a linear interpolation method (e.g. linear interpolation, cubic-spline interpolation)[] _i_[∆] _[i][s][j]_[= 1][ has to hold.] 

In our calculation of the credit-spread curve we use 

**==> picture [260 x 16] intentionally omitted <==**

with the condition 

**==> picture [232 x 10] intentionally omitted <==**

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

95 

Rainer Pullirsch 

This Δ can be regarded as the maximum sensitivity of the credit-spread with respect to a variation of the coupon. Following this estimation we use the grid point scheme with the smallest Δ. If Eq. (20) is not fulfilled by any scheme we reduce the number of grid points _m_ → _m_ – 1 . The number of grid points is reduced until Eq. (20) holds for at least one scheme of grid points. This procedure not only leads to improvement of the numerical stability but also smooths the creditspread curve. By reducing the number of grid points one also reduces the accuracy of the prices which are obtained from the resulting credit-spread curve. We allow here for a maximum deviation of 5% between the price obtained from the resulting credit-spread curve and the average price calculated from the quoted prices. 

**Figure 1:** Effects of the reduction of the number of grid points. The credit-spread curve clearly gets smoother when reducing the number of grid points from six (S-shaped solid curve) via five (dashed curve) and four (dotted curve) to three (smoothest solid curve). 

**==> picture [431 x 250] intentionally omitted <==**

**----- Start of picture text -----**<br>
 1<br> 0.9<br> 0.8<br>s  [%]<br> 0.7<br> 0.6<br> 1  2  3  4  5  6  7  8  9  10<br>t<br>**----- End of picture text -----**<br>


To illustrate how the above procedure works we give an example. Given a set of the six zerocoupon bonds as outlined in Tab. 1 and calculating the credit-spread curve with six, five, four, and three grid points 

**Table 1:** Details of the bonds. 

|**Table 1:**Details of the bonds.|||||||
|---|---|---|---|---|---|---|
|Maturity in years|1.2|2.8|4.6|5.9|7.2|9.8|
|Riskless zero-coupon interest rate<br>at maturity|3.00%|3.20%|3.55%|3.70%|3.80%|3.85%|
|Price|95.7720|89.4044|81.8649|76.2312|71.0348|62.1699|



we obtain for the relative pricing errors the values depicted in Tab. 2. Even for a reduction of the grid points to only three the relative pricing errors are very low. The resulting credit-spread curves 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

96 

Measuring Credit-Spread Risk on a Single Issuer Basis 

are plotted in Fig. 1. It is obvious that the unnatural shape obtained with six grid points is more and more smoothed out when reducing the number of grid points. For three grid points the creditspread curve seems most realistic. 

**Table 2:** Pricing errors in %. 

|**Table 2:**Prici|ng errors in %|.|||||
|---|---|---|---|---|---|---|
|6 grid points|0.00003|-0.00006|0.000002|-0.00002|0.00007|0.00001|
|5 grid points|-0.037|0.080|-0.134|0.124|-0.045|0.003|
|4 grid points|-0.095|0.155|-0.144|0.040|0.025|-0.008|
|3 grid points|-0.059|0.149|-0.180|0.032|0.071|-0.022|



## **3 Input bond quotations** 

In order to get correct credit-spread curves which are not influenced by wrong quotations special care has to be taken concerning the liquidity of the traded bonds. One would like to have at least three contributors per bond which submit at least three quotations in the desired time window. Concerning the limited liquidity of corporate bonds we had to weaken this condition. In order to have enough data to work with we reduced the requirement to the following of having at least one quotation in the time interval of interest which was checked carefully for plausibility. 

To calculate the credit-spread with respect to the swap-rate we need the bond quotations and the swap-rate simultaneously. We have chosen to load our data at 4 p.m. CET (CEST) from Reuters. For the swap-rate for the relevant currencies we use a snapshot at 4 p.m. CET (CEST) also from Reuters. For the bond quotations it is not possible to get enough data just taking a snapshot. Also to apply some liquidity and plausibility checks we use quotations which were provided within a time slot of +/ – 1.5 hours relative to the swap-rates. In the calculation the mean of all quotations in the relevant time window of a specific bond is used. 

To eliminate possible data errors and possible quotations from issuers who are very close to default we use an upper bound _β_ for the maximum bid-ask-spread on a single day for each bond: 

**==> picture [281 x 12] intentionally omitted <==**

Currently we are working with _β_ = 4 . If only one quotation does not fulfill this criterion it is eliminated from averaging. 

The second restriction we applied to the data source is that we introduced an upper bound _µ_ for the deviation of individual bid-ask mean values _m_ from the overall mean of the quotations of a specific bond _m¯_ so that 

**==> picture [281 x 11] intentionally omitted <==**

Currently we are working with _µ_ = 2. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

97 

Rainer Pullirsch 

## **4 Residual variance** 

It is known from the literature that bonds of a company issued in different currencies are traded with slightly different credit-spreads, see Berger et. al. 2003 and Jankowitsch/Pichler 2005. Since corporates quite often issue their bonds in various currencies it is essential to calculate the credit-spread curves currency independently. Otherwise the number of corporates for which we can estimate credit-spread curves would be too small. So to take into account the fact that our credit-spread curves are sometimes obtained from bonds issued in various currencies and to take into account further bond price driving factors (e.g. liquidity) we calculate residual variances from pricing errors in the credit-spread curve generation. 

**Figure 2:** Schematic illustration of the modeling of residual variances as independent shifts of the creditspread curve. For bond 1 the credit-spread curve needs to be shifted upwards to exactly price bond 1 and for bond 2 the credit-spread curve needs to be shifted downwards to exactly price bond 2. 

**==> picture [422 x 251] intentionally omitted <==**

**----- Start of picture text -----**<br>
 1<br>volatility of spread shift bond 1<br> 0.8 spread shift bond 1<br>spread curve spread shift bond 2<br> 0.6<br>s  [%]<br>volatility of spread shift bond 2<br> 0.4<br> 0.2<br> 0<br> 0  1  2  3  4  5  6  7<br>t<br>**----- End of picture text -----**<br>


## **4.1 Issuer credit-spread curves** 

To obtain the residual variances we do not start generating the credit-spread curves with the same number of grid-points _mt_ as the number of bonds _nt_ available for one issuer at day _t_ . For _nt_ > 3 we start with _mt_ = 3 and for _nt_ = 3 with _mt_ = 2 . Thus we obtain a credit-spread curve which for _nt_ > 2 slightly miss-prices all the bonds used in its generation. These small pricing errors are then converted into small parallel shifts ξ of the credit-spread curve for all the bonds as illustrated in Fig. 4. This conversion of the pricing errors is done in the following way: For each bond we calculate the necessary parallel shift of the credit-spread curve to exactly price the specific bond. From these shifts we compute weighted returns _ηb,t_ for the _b_[th] bond on the _t_[th] day in the time-series as 

**==> picture [270 x 25] intentionally omitted <==**

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

98 

Measuring Credit-Spread Risk on a Single Issuer Basis 

This takes into account that the difference _kt = nt – mt_ influences these shifts which may be illustrated by the following: Consider that in the minimization procedure we use as many grid-points _mt_ as available bonds _nt_ for the credit-spread curve under consideration. This would effectively mean that all errors are set to zero since we have as many parameters as degrees of freedom. Reducing the number of gridpoints means that effectively only _kt = nt – mt_ components of the n-dimensional pricing-error are set to zero and thus the errors have to be rescaled by a factor of  _nktt_ in order to have normalized errors. Only from these normalized errors are we able to calculate the daily changes of credit-spread shifts. From these weighted returns we calculate a time-weighted variance 

**==> picture [281 x 30] intentionally omitted <==**

where the time-weighted mean is 

**==> picture [279 x 38] intentionally omitted <==**

In all our calculations we use λ = 0.97. 

Finally, we compute the mean of the issuer credit-spread curves 

**==> picture [280 x 29] intentionally omitted <==**

as the bond-specific residual variance for the issuer credit-spread curve under consideration where we have used _nt_ being the number of bonds contributing to the curve under consideration. In case a issuer credit-spread curve is generated from only two bonds we calculate the returns 

**==> picture [270 x 11] intentionally omitted <==**

as the change of the differences 

**==> picture [266 x 11] intentionally omitted <==**

of the single bond credit-spreads _sb,t_ . From these returns the residual variance is determined in the same way as described above. 

## **4.2 Synthetic credit-spread curves** 

As sometimes we are confronted with the problem that for some issuers we only have one or two bonds available which are traded liquidly on the market, we decided to group issuers regarding their industrial sector, their rating and the region where they have their strongest market exposure. Thus we obtain curves e.g. for A-rated German banks. In this case each individual bond which now contributes to this curve has an individual behavior with respect to the curve resulting from its specific issuer which behaves individually with respect to the curve and its own individual behavior with respect to its issuer. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

99 

Rainer Pullirsch 

For synthetic credit-spread curves we thus have to take into account a bond and a company specific residual variance. To estimate the residual variances we calculate the credit-spread shift again which now also depends on the specific company _c_ . Thus the returns are now given by 

**==> picture [279 x 25] intentionally omitted <==**

To concentrate on the important factors we suppress the time-series index _t_ in the following. We begin with splitting the residual returns according to 

**==> picture [18 x 11] intentionally omitted <==**

**==> picture [65 x 9] intentionally omitted <==**

We continue by calculating an estimator _ηˆc_ for _ηc_ 

**==> picture [280 x 29] intentionally omitted <==**

where _nc_ is the number of bonds for company _c_ . From the time-series of the _ηˆc_ we compute an estimator of the variance _σˆ[2] c_[. For the bond specific residual changes] 

**==> picture [278 x 14] intentionally omitted <==**

**==> picture [426 x 109] intentionally omitted <==**

The derivation of this result is illustrated in the appendix. The residual variance _σ[2] c_[ is calculated ] from 

**==> picture [281 x 28] intentionally omitted <==**

In case of a negative correlation of the _ηb,c_ the variance _σ[2] c_[ has negative values and is set to ] zero. Eventually the bond-specific residual variance _σB[2]_[ for the synthetic credit-spread curve under ] consideration is determined as the mean of all _σ[2] b_[ and the company-specific residual variance ] _σC[2]_[for the synthetic credit-spread curve under consideration is determined as the mean of all ] _[σ][2] c_[.] 

## **5 Mapping procedure in the risk calculation** 

For the VAR calculation we need to map the bonds in the portfolio onto the available creditspread curves. This mapping procedure is done in a threefold way. 

Issuers whose credit-spread curve time-series are available are mapped in the VAR calculation onto their curve. In this case one has only to ensure that the time to maturity of the bond in the 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

100 

Measuring Credit-Spread Risk on a Single Issuer Basis 

portfolio corresponds with the time to maturities of the bonds which entered the issuer creditspread curve generation. 

For corporations whose credit-spread curves cannot be determined in the above described way we have chosen the following approach. Taking into account the industry sector the rating and the region we calculate synthetic index credit-spread curves (e.g. Banks-Germany-AA). These curves are determined by exactly the same procedure as described above (also including the residual variance). Again in this case we have to ensure that the time to maturity of the bond in the portfolio corresponds with the time to maturities of the bonds which entered the synthetic credit-spread curve generation. 

For those issuers which still cannot be mapped either onto an issuer curve or onto a synthetic curve we have chosen an implicit rating procedure, i.e. by taking into account the industry sector and the times to maturity we dynamically map these issuers to the credit-spread curve which best reproduces the traded/quoted prices of the bonds under consideration. This is done in the following way. If for example we have a bond from a bank in the portfolio and we cannot apply the two above described mapping procedures, then we use all available credit-spread curves from banks with consistent maturities to calculate theoretical prices for this bond. All these prices are then compared to the actual traded/quoted prices. For the risk calculation we then use the credit-spread curve for which the theoretical price was closest to the traded/quoted price. Thus we effectively apply the curve with the closest level of creditspreads. This dynamical mapping can therefore be regarded as a mapping according to an implicit rating. 

The residual variance for this dynamic mapping is obtained from the time-series of bond prices which neither contribute to an issuer credit-spread curve nor to a synthetic credit-spread curve. These bonds are mapped dynamically to those credit-spread curves which best explain the corresponding bond price. We further calculate the pricing error by mapping the bond onto the same curve as it was mapped the day before. In this way we build time-series from the pricing errors _ξb,d,t_ (shifts) resulting from the dynamic mapping procedure for a specified credit-spread curve _d_ and from the shifts we compute returns _ηb,d,t_ for the _b_[th] bond (being mapped dynamically onto curve _d_ ) on the _t_[th] day in the time-series for the curve _d_ as 

**==> picture [280 x 12] intentionally omitted <==**

From these returns we calculate a time-weighted variance 

**==> picture [274 x 30] intentionally omitted <==**

where the time-weighted mean is defined as 

**==> picture [281 x 38] intentionally omitted <==**

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

101 

Rainer Pullirsch 

In this case the weight λ is taken to be 1, i.e. all returns are equally weighted. Finally we compute the mean 

**==> picture [280 x 29] intentionally omitted <==**

as the residual variance for the dynamic mapping procedure for the credit-spread curve under consideration where _nt_ is the number of bonds contributing to the curve under consideration. 

## **6 Time-series of credit-spreads** 

In this section we just give three examples of time-series of credit-spreads. The first example Philip Morris shows several jumps in the time development of the credit-spreads which is due to news from lawsuits against Philip Morris, see Fig. 3. 

The second example shows the time-series of the Republic of Turkey credit-spreads. This is a typical example of time-series where suddenly there is some bad news on the creditworthiness of the issuer but which then recovers again, see Fig 4. 

The last example shows the time-series which is typical for most issuers for the last three years. No specific event occurred which induced any jump of the levels of credit-spreads. What nevertheless is worth mentioning is the decrease of the credit-spreads during 2003. This period was characterized by the tightening of credit-spreads which then from 2004 to 2006 stayed at a very low level. The example given here in Fig. 5 shows the time-series of France Telecom credit-spreads. 

**Figure 3:** Time-series of Philip Morris credit-spreads (in %) for various maturities from 1 to 20 years reflected by the different curves. In this time-series of credit-spreads for Philip Morris jumps are visible at several times. These reflect the markets reaction to news from lawsuits from smokers and US states against the tobacco industry. 

**Philip Morris** Credit-Spread Time-Series, January 30[th] , 2003 to September 28[th] , 2004 

**==> picture [421 x 228] intentionally omitted <==**

**----- Start of picture text -----**<br>
 8<br>"PHILIPMORRIS" u 1<br>"PHILIPMORRIS" u 2<br>"PHILIPMORRIS" u 3<br> 7 "PHILIPMORRIS" u 4<br>"PHILIPMORRIS" u 5<br>"PHILIPMORRIS" u 6<br>"PHILIPMORRIS" u 7<br> 6 "PHILIPMORRIS" u 8<br>"PHILIPMORRIS" u 9<br>"PHILIPMORRIS" u 10<br>"PHILIPMORRIS" u 11<br> 5 "PHILIPMORRIS" u 12<br>"PHILIPMORRIS" u 13<br>"PHILIPMORRIS" u 14<br>"PHILIPMORRIS" u 15<br>s  [%]  4 "PHILIPMORRIS" u 16"PHILIPMORRIS" u 17<br>"PHILIPMORRIS" u 18<br>"PHILIPMORRIS" u 19<br>"PHILIPMORRIS" u 20<br> 3<br> 2<br> 1<br> 0<br> 0  100  200  300  400  500<br>trading day number<br>**----- End of picture text -----**<br>


Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

102 

Measuring Credit-Spread Risk on a Single Issuer Basis 

## **7 Value-at-risk calculation** 

For the VAR calculation we now have all the necessary ingredients, i.e. the time-series of the creditspread curves. In our VAR calculation we deploy a Monte Carlo simulation. We generate 1000 credit-spread curve scenarios with the correct correlation to all other risk-factors using the volatility and the correlation from the time-series. The credit-spreads in our simulation are distributed according to a Student-t5 distribution accounting for the fat tails of credit-spread returns. In the VAR calculation the residual variances are modeled as independent parallel shifts of the credit-spread curve. This is implemented as a stochastic component in the pricing function. 

## **8 Conclusion and outlook** 

We have presented a model how to measure credit-spread risk on a single issuer basis. In this article we focused on estimating credit-spread curves from bond quotations. In the last years the liquidity of the CDS market has further improved. Therefore we now also use CDS curves as risk factors. Especially when focusing on credit derivatives CDS credit-spreads need to be taken to calculate hazard rates and default probabilities which are used in the pricing functions. With AAA-rated issuers one gets negative credit-spreads from bond quotations when calculating the credit-spread with respect to swap-rates indicating that swaps are mainly traded by AA-rated banks and thus do not reflect riskless rates. With negative credit-spreads it is not possible to calculate hazard rates for defaults. Nevertheless the model described only needed to be extended to also include CDS credit-spread curves as additional risk factors for the pricing of CDS and other credit derivatives such as CDOs or n-th-to-default-baskets. 

**Figure 4:** Time-series of the Republic of Turkey credit-spreads (in %) for various maturities from 1 to 20 years reflected by the different curves. The peak of credit-spreads going up to almost 18% in March 2003 reflects the markets reaction to the not-granting of several billion USD credits by the US government as a reaction of the Turkish refusal to let US troops use its military bases for the war against Iraq. 

**Turkey** Credit-Spread Time-Series, January 30[th] , 2003 to September 28[th] , 2004 

**==> picture [421 x 229] intentionally omitted <==**

**----- Start of picture text -----**<br>
 18<br>"TREAS TR" u 1<br>"TREAS TR" u 2<br>"TREAS TR" u 3<br> 16 "TREAS TR" u 4<br>"TREAS TR" u 5<br>"TREAS TR" u 6<br> 14 "TREAS TR" u 7<br>"TREAS TR" u 8<br>"TREAS TR" u 9<br>"TREAS TR" u 10<br> 12 "TREAS TR" u 11<br>"TREAS TR" u 12<br>"TREAS TR" u 13<br>"TREAS TR" u 14<br> 10 "TREAS TR" u 15<br>"TREAS TR" u 16<br>s  [%] "TREAS TR" u 17<br> 8 "TREAS TR" u 18<br>"TREAS TR" u 19<br>"TREAS TR" u 20<br> 6<br> 4<br> 2<br> 0<br> 0  100  200  300  400  500<br>trading day number<br>**----- End of picture text -----**<br>


Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

103 

Rainer Pullirsch 

**Figure 5:** Time-series of France Telecom credit-spreads (in %) for various maturities from 1 to 20 years reflected by the different curves. This time-series is given as an example for a typical development of the credit-spread curve for an issuer where no events trigger an abrupt jump of the level of credit-spreads. 

**France Telecom** Credit-Spread Time-Series, January 30[th] , 2003 to September 28[th] , 2004 

**==> picture [419 x 230] intentionally omitted <==**

**----- Start of picture text -----**<br>
 4<br>"FRANCETELECOM" u 1<br>"FRANCETELECOM" u 2<br>"FRANCETELECOM" u 3<br> 3.5 "FRANCETELECOM" u 4<br>"FRANCETELECOM" u 5<br>"FRANCETELECOM" u 6<br>"FRANCETELECOM" u 7<br> 3 "FRANCETELECOM" u 8<br>"FRANCETELECOM" u 9<br>"FRANCETELECOM" u 10<br>"FRANCETELECOM" u 11<br> 2.5 "FRANCETELECOM" u 12<br>"FRANCETELECOM" u 13<br>"FRANCETELECOM" u 14<br>"FRANCETELECOM" u 15<br>s  [%]  2 "FRANCETELECOM" u 16"FRANCETELECOM" u 17<br>"FRANCETELECOM" u 18<br>"FRANCETELECOM" u 19<br>"FRANCETELECOM" u 20<br> 1.5<br> 1<br> 0.5<br> 0<br> 0  100  200  300  400  500<br>trading day number<br>**----- End of picture text -----**<br>


**Acknowledgments:** I especially want to thank Peter Schaller with whom the described model was jointly developed and who contributed major ideas. Furthermore I want to thank all the people at the department of ”Operational Risk and Risk Analysis” at Bank Austria Creditanstalt for stimulating discussions and for the perfect working atmosphere which they provide. Last but not least I want to mention Gerhard Deschkan who as the head of the department creates the perfect working environment. 

## **Appendix: Determination of estimator for residual variance** 

Given an observable _v_ which fluctuates around its true value _I_ . Each measurement then yields a value _vi_ 

**==> picture [271 x 10] intentionally omitted <==**

with the fluctuation _ξi_ . 

One can calculate an estimator _J_ for the true value _I_ as 

**==> picture [276 x 36] intentionally omitted <==**

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

104 

Measuring Credit-Spread Risk on a Single Issuer Basis 

Further one can express the deviation _єi_ from the estimator _J_ for each measurement as a function of the true error as 

**==> picture [407 x 37] intentionally omitted <==**

Since all the fluctuations are independent the expectation values < _єi єi_ > is given by 

**==> picture [432 x 57] intentionally omitted <==**

## **References** 

Berger, L., Goldberg, L., Kercheval, A., 2003, Modelling credit risk: currency dependence in global credit markets, Journal of Portfolio Management, 29. 

Duffee, G. R., 1996, Idiosyncratic Variation of Treasury Bill Yields, Journal of Finance, 51, 527-551. 

Geyer, A., Kossmeier, S., Pichler, S., 2004, Measuring Systematic Risk in EMU Government Yield Spreads, Review of Finance, 8. 

Hull, J., Predescu, M., White, A., 2005, Bond Prices, Default Probabilities and Risk Premiums, Journal of Credit Risk, 1, 53-60. 

Jankowitsch, R., Pichler, S., 2005, Currency Dependence of Corporate Credit Spreads, Journal of Risk, 8. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

105 

## Chaker Aloui / Mondher Bellalah 

## **Long Range Memory on Emerging Stock Market Volatility and Value at Risk: Estimations for Long and Short Trading Positions** 

## **Abstract** 

Diese Arbeit beschäftigt sich mit langfristigen Abhängigkeiten im Zusammenhang mit der Value at Risk Schätzung für tägliche Veränderungen von Aktienindizes von Wachstumsmärkten. Können die Schätzungen verbessert werden, wenn solche Abhängigkeiten angenommen werden? Zur Beantwortung dieser Frage, werden mehrere GARCH-basierte (inklusive das RiskMetrics Modell) und FIGARCHbasierte Modelle angewandt, um den VaR für mehrere Konfidenzniveaus für die Aktienindizes von 25 Schwellenländern zu schätzen. Sowohl Kaufpositionen als auch Leerverkaufspositionen (long positions _und_ short positions) _werden_ berücksichtigt. Wir verwenden die Normalverteilung, die Student-Verteilung und die schiefe Student-Verteilung (skewed Student distribution) für die GARCHbasierten Modelle. Die Güte der GARCH-basierten Modelle wird anhand des Kupiec Tests bestimmt. Weiters werden die Risikomaße expected short-fall und average multiple of tail event to risk für jedes der GARCH-basierten Modelle berechnet. Die Ergebnisse weisen darauf hin, dass in den meisten Fällen die schiefe Student t-Verteilung sowohl für Kauf- als auch für Leerverkaufspositionen die besten Ergebnisse liefert. 

**Chaker Aloui** The Faculty of Management and Economic Sciences of Tunis 

**Mondher Bellalah** ISC Group, Paris 

_In this paper, we explore the long range dependency in daily emerging stock indexes Value at Risk estimation. Can we do better if long range memory is assumed? To investigate this question, several GARCH-type models including RiskMetrics and FIGARCH are applied to twenty five emerging stock market VaR estimations at various confidence levels. Both long and short trading positions are considered. For these two types of trading positions, we suggest using Normal, Student and skewed Student distributions for various GARCH-type models. The performance of all the GARCH-type models are assessed by estimating the failure rate for the stock returns based on Kupiec test. We also compute the expected short-fall and the average multiple of tail event to risk measure for each GARCH-type model. Our results pointed out that in major cases, the skewed Student FIGARCH model presents the best performance in VaR estimations for both short and long trading positions._ 

## **1. Introduction** 

Investment and commercial banks, as well as treasury departments of many firms, hold portfolios of complex securities whose value depends on exogenous state variables such as interest and exchange rates. To allocate capital and measure the profitability of different business operations, managers and regulators quantify the magnitude and likelihood of possible portfolio changes for various forecast horizons. This process is often referred to as “measuring market risk”. To 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

107 

Chaker Aloui / Mondher Bellalah 

date, measurement of market risk has focused on one particular metric called “Value at Risk” (henceforth, VaR). VaR models have been developed since 1994, when J.P. Morgan developed the first set of standardized assumptions called “RiskMetrics” (henceforth, RM). The common RM model assumes that the financial asset return can be described by a conditional normal distribution with zero mean and variance being expressed as exponentially weighted moving average of historical squared returns. This model has two disadvantages. Firstly, it is well documented that returns are often non-normally distributed. Daily stock returns are commonly found to be leptokurtic. Leptokurtic returns have a peaked mean and fatter tails than normal distributions. In practice, observations nearer to and farther from the mean are more common than what a normal distribution would predict. Secondly, recent empirical studies have found that many financial asset returns may exhibit long range dependency on stock market volatilities. Amongst these studies are Cheung and Lai (1995), Barkoulas and Baum (1996), Barkoulas, Baum and Travlos (2000), Sadique and Silvapulle (2001), Wright (2001), Henry (2002) and Aloui et _al._ (2005). So, it is interesting to see whether accounting for long range dependency of emerging stock market volatilities can improve the measurement of stock risk in the context of VaR. Methodologically, we detect a potential presence of long-range volatilities in emerging stock markets. Then we compare the performance of seven GARCH-type models (including two long-memory GARCH models). In this paper, only a conditional normal distribution is considered. While most empirical studies focus only on holding a long position of a portfolio, we also consider a short position. In fact, most models in the literature focus on the computation of the VaR for negative returns. It is commonly assumed that traders or portfolio managers have long trading positions, (i.e. they bought the traded asset and are concerned when the price of the asset falls). In this paper, we focus on modelling the VaR for portfolios with long and short positions. In the first case, the risk comes from a drop in stock price, while the trader loses money when the price increases in the second case. Thus, the trader would have to buy back the asset at a higher price than the one he got when he sold it. The rest of the paper is as follows: Section 2 briefly reviews the long memory GARCH-type models and the VaR models. In section 3, the data set and methodology are presented. Empirical findings are reported in section 4. Section 5 contains some concluding remarks. 

## **2. Theoretical considerations** 

## **2.1. Defining and measuring long-memory** 

**==> picture [429 x 77] intentionally omitted <==**

where _0 < d < 0.5_ and c is some positive constant. The ACF in (1) displays a very slow rate of � decay to zero as _k_ goes to infinity and � _k_ ��� ��� _k_ � � .  This slow rate of decay can be contrasted with ARMA processes which have an exponential rate of decay, and satisfy the following bound: 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

108 

Long Range Memory on Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

**==> picture [250 x 15] intentionally omitted <==**

**==> picture [429 x 54] intentionally omitted <==**

A simple example of long-memory is the fractionally integrated noise process, _I (d)_ , with _0 < d < 1_ Which is 

**==> picture [250 x 14] intentionally omitted <==**

where _L_ is the lag operator, and _ut_ ~ _iid_ � _0,_ � _2_ �. This model includes the traditional extremes of a stationary process, _I (0)_ , and a nonstationary process _I (1)_ . The fractional difference operator _(1 – L)[d]_ is well defined for a fractional _d_ and the ACF of this process displays a hyperbolic decay consistent with equation (1). A model that incorporates the fractional differencing operator is a natural starting point to capture long-memory. This is the underlying idea of the ARFIMA and FIGARCH class of processes. In practice we must resort to estimating the ACF with usual sample quantities 

**==> picture [253 x 46] intentionally omitted <==**

A second approach to measure the degree of long-memory is to use semi-parametric methods. This allows one to review the specific parametric form, which is potentially misspecified and could lead to an inconsistent estimate of the long memory parameter. In this paper, we consider the two most frequently used estimators of the long memory parameter d. The first is the Geweke and Porter-Hudack (1983) (henceforth, GPH) estimator, based on a log-periodogram regression. Suppose _y0 , y1 ,...yT_ � _1_[is the dataset and define the periodogram for the first ] _[m]_[ ordinates as] 

**==> picture [250 x 33] intentionally omitted <==**

where � _j_ � _2_ � _j/T , j_ � _12,,...m,_ .  The estimate of _(d)_ can then be derived from linear regression of _log I j_ on a constant and the variable _X j_ � _log 2 sin_ �� _j / 2_ � , which gives 

**==> picture [250 x 41] intentionally omitted <==**

Robinson (1995) provides formal proofs of consistency and asymptotic normality for the Gauss case with – _0.5 < d < 0.5_ . The asymptotic standard error is � _/ 24m_ .  The bandwidth parameter _m_ must converge infinitely with the sample size, but at a slower rate than _T_ .  Clearly, a larger choice of _m_ reduces the asymptotic standard error, but the bias may increase. The bandwidth parameter was set to _(T)_ in Geweke and Porter-Hudack (1983). While Hurvich, Deo and Brodsky (1998) show the optimal rate to be _O (T_[4/5] _)_ . Recently, Hurvich and Deo (1999) have shown that the 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

109 

Chaker Aloui / Mondher Bellalah 

GPH estimator is also valid for some non Gaussian time-series. Velasco (1999) has shown that consistency extends to _0.5 < d < 1_ and asymptotic normality to _0.5 < d < 0.75_ . The other popular semiparametric estimator was developed by Robinson (1995). Essentially, this estimator is based on the log-periodogram and solves: 

**==> picture [247 x 59] intentionally omitted <==**

The estimator is asymptotically more efficient than the GPH estimator and consistency and asymptotic normality of _d[ˆ]_ are available under weaker assumptions than the Gaussian hypothesis. The asymptotic standard error for _d[ˆ]_ is _1/_ � _2 m_ �. Robinson and Henry (1999) have shown that this estimator is valid in the presence of some forms of conditional heteroskedasticity. Traditionally, the time series econometrics centred itself around an alternative: the presence of a unit root, indicating a no-stationnarity of the set, on the one hand, and the absence of such a unit root indicating that the set is stationary, on the other hand. These two cases correspond to cases of processes of short memory of ARIMA (p,d,q) and ARMA(p,q). These classic modeling approaches do not take in account the intermediate cases to know the existence of a fractional integration parameter. However, the presence of such a coefficient is especially interesting since it permits to characterize processes of long memory. These processes, called ARFIMA, have been introduced by Granger and Joyeux (1980) and Hosking (1981). They present the interest to simultaneously take into account the short term behaviour of the set through autoregressive and mobile average and the behaviour of long term by means of the fractional integration parameter. The ARFIMA(p,d,q) process can be defined as follows: 

**==> picture [255 x 14] intentionally omitted <==**

Here _�_ �� _L_[and ] _�_[��] _L_[are lag polynomials of p and q respectively. ] _[εt ]_[is a white noise process, and ] 

**==> picture [232 x 25] intentionally omitted <==**

ARFIMA (p,d,q) processes are stationary and inversible when _d_ � �� _1/21,/2_ � and _d_ � _0_ . 

## **2.2. Short and long term memory and GARCH-type models** 

Considering a possible fractional integration of the conditional variance has initially been suggested by Ding, Granger and Engle (1993). FIGARCH processes were introduced by Baillie, Bollerslev and Mikkelsen (1996). 

- The starting point is a GARCH (p,q) process. It can be written as follows: 

**==> picture [321 x 28] intentionally omitted <==**

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

110 

Long Range Memory on Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

where _α_[2] is the conditional variance, _α0>0,αi≥0andβj≥0,i=1,...,q._ A GARCH(p,q) process is a short memory process since the effect of a shock on the conditional variance decreases at an exponential rate. GARCH(p,q) can be also written as follows: 

**==> picture [324 x 14] intentionally omitted <==**

Consequently, when the lag polynomial _[1–α(L)–β(L)]_ contains a unit root, the GARCH process becomes an integrated GARCH process, denoted as IGARCH(p,q). 

- An IGARCH(p,q) process can be written as: 

**==> picture [325 x 14] intentionally omitted <==**

with 

**==> picture [140 x 14] intentionally omitted <==**

FIGARCH processes constitute an alternative between GARCH processes and IGARCH processes and result in the equation (4) by replacing the operator _(1 – L)_ by the operator _(1 – L)[d]_ , where _d_ is the fractional integration parameter. 

- A FIGARCH process can be written as follows: 

**==> picture [325 x 14] intentionally omitted <==**

roots of _Φ(L)_ and _[1–β(L)]_ polynomials being outside the unit circle. Thus, if _d = 0_ , FIGARCH(p,d,q) process will be reduced to a GARCH(p,q). If _d = 1_ , the FIGARCH process is an IGARCH process. By replacing _μt_ by its value according to _σ[2] t_[, one can write equation (5) as follows:] 

**==> picture [322 x 19] intentionally omitted <==**

The variance equation is then given by: 

**==> picture [325 x 14] intentionally omitted <==**

with 

**==> picture [151 x 19] intentionally omitted <==**

� � _1L_ � � _2L_ � _..._ and � _k_[�] _0_ et _k_ � _12,,...,n_ . 

Baillie, Bollerslev et Mikkelsen (1996) note that the effects of a shock on the conditional variance of FIGARCH(p,d,q) decreases at an hyperbolic rate when _0 ≤ d < 1._ 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

111 

Chaker Aloui / Mondher Bellalah 

## **2.3. Tests for long-range memory** 

## **A. Lo’s (1991) Modified Rescaled Range test** 

_R / S_ test Before estimating FIGARCH processes, we proceed to the application of the modified (Lo (1991)) in order to detect the presence, if any, of long-range memory in emerging stock market _R / S_ statistic is known volatility series. Let us recall that the limiting distribution of the modified and that it is thus possible to test the null hypothesis of short-term memory against the alternative of long-term memory. The critical values of this statistic have been tabulated by Lo (1991). The author demonstrated that this statistic is not robust to short range dependence, and proposed the following one: 

**==> picture [228 x 31] intentionally omitted <==**

which consists of replacing the variance by the HAC variance estimator in the denominator of the statistic. If _q = 0_ , Lo’s statistic _R / S_ reduces to Hurst’s statistic. Unlike spectral analysis which detects periodic cycles in a series, the _R / S_ analysis has been advocated by Mandelbrot for detecting non periodic cycles. Under the null hypothesis of no long-memory, the statistic _T_[–1 / 2] _Qn_ converges to a distribution equal to the range of a Brownian bridge on the unit interval: 

**==> picture [101 x 18] intentionally omitted <==**

Where _W[0] (t)_ is a Brownian bridge defined as _W[0] (t)=W(t) – tW(1)_ , W(t) being the standard Brownian motion. The distribution function is given in Siddiqui (1976), and is tabulated in Lo (1991). This statistic is extremely sensitive to the order of truncation but there are no statistical criteria for choosing _q_ in the framework of this statistic. Given that the power of a useful test should be greater than its size, this statistic is not very helpful. For that reason, Teverovsky, Taqqu and Willinger (1999) suggest to use this statistic with other tests. Since there is no data driven guidance for the choice of this parameter, we consider the default values for _q = 5, 10, 25, 50_ . 

## **B. Geweke Porter-Hudack (1983) tests** 

In this respect, two procedures have been retained: the GPH method and the maximum likelihood technique. The GPH method is founded on the behaviour of the spectral density around low frequencies. It is a two-step technique since one estimates, in the first stage, the fractional integration parameter  and, in the second stage the parameter of the GARCH model. Concerning the maximum likelihood procedure (Sowel (1992)), it is a one-step procedure: all the parameters of the FIGARCH(p,d,q) specification are estimated simultaneously. Let us recall that the function _g(T)_ used in the spectral technique, corresponds to the number of periodogram ordinates. _T_ is the number of observations. In order to examine the stability of the estimation when the number of periodogram ordinates vary, we have chosen different values: _T[0.45] , T[0.5] , T[0.55]_ and _T[0.8]_ . 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

112 

Long Range Memory on Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

## **2.4. VaR and RM** 

## **A. VaR** 

The VaR is a commonly used statistic for measuring potential risk of economic losses in financial markets. VaR models can help portfolio managers to specify the minimum amount that is expected to be lost with a given level of probability ( _α_ ) and for a given time horizon ( _k_ ) (usually, one day, one week or 10 days). For a given density function of an asset return, VaR can be illustrated as follows: 

**Figure 1.** 

VaR of a portfolio 

For instance, for a given confidence level (95%), we can find in figure 1 a point where there is a 5% probability of experiencing a lower return. This number is -2.5, as occurrences of returns less than -2.5 add up to 5% of the total number of observations (see e.g. Giot and Laurent, 2001, p.1). 

**Figure 2.** 

VaR for a €100 millions 

There is only a 5% chance that the portfolio will lose by more than €100 million times -2.5%, or 2.5 € million. The VaR is € 2.5 million. 

Formally, let _Pt_ be the price of a financial asset on day ( _t_ ). A _k_ - day VaR of a long position on day ( _t_ ) is defined as follows: 

**==> picture [322 x 14] intentionally omitted <==**

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

113 

Chaker Aloui / Mondher Bellalah 

Given a distribution of return, VaR can be determined and expressed in terms of a percentile of the return distribution. Specifically, if _qα_ is the _α_ -percentile of the continuously compounded returns defined as _Log(Pt)–Log(Pt-k)_ , then the VaR can be written as follows: 

**==> picture [323 x 17] intentionally omitted <==**

The above expression implies that a good VaR estimate can only be produced with accurate forecasts of the percentiles _qα_ , which depends on appropriate volatility modelling. 

## **B. RiskMetrics** 

The RM model assumes that returns are distributed as follows: 

**==> picture [319 x 35] intentionally omitted <==**

where _rt_ is the continuously compounded return; _Ω1_ is the information set up to time _t_ ; _λ_ is a smoothing parameter, _0 ≤ λ ≤ 1._ Equation (19) implies that the conditional distribution of returns is normal with mean zero. In fact, the RM model implies that the conditional variance can be expressed as an exponentially weighted moving average (EWMA) of the past squared innovations or returns, which is: 

**==> picture [324 x 17] intentionally omitted <==**

The smaller the smoothing parameter, the greater the weight that is given to recent data. RM (1996) suggests that we can use _λ_ = 0.94 for daily data and _λ_ = 0.97 for monthly data. According to Fleming, Kirby and Ostdiek (2001), a smoothing parameter equal to 0.94 seems to produce very good forecasts for one-day volatility. Under the RM model hypothesis, equation (18) giving the one-day VaR on day _t_ can be expressed as follows: 

**==> picture [328 x 18] intentionally omitted <==**

_zα_ is the 100 _α_ th percentile of _N_ (0,1). 

## **3. Data and Methodology** 

## **3.1. Data** 

The sample under consideration consists of twenty five emerging securities markets, namely, Egypt (EGY), Morocco (MOR), South Africa (S. AFR), China (CHN), India (IND), Pakistan (PKS), Indonesia (INDO), South Korea (S. KOR), Malaysia (MAL), the Philippines (PHN), Taiwan (TWN), Thailand (THA), Jordan (JOR), Turkey (TUR), Hungary (HUN), Poland (POL), Russia (RUS), Argentina (ARG), Brazil (BRA), Colombia (COL), Mexico (MEX), Peru (PER), Chile 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

114 

Long Range Memory on Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

(CHL), Venezuela (VEN) and the Czech Republic (CZE). The behaviour of each of these markets is summarized by the MSCI web site EQUITY MARKETS. It is measured in local currency and —published daily in the MSCI DATA BASE. The sample period extends from January 31, 1997, through November 31, 2004. We focus our attention on the series of returns defined as _rt =_ 100x _(logPt –log Pt-1)_ , where _rt_ and _Pt_ are the return in percent and the index on day t, respectively. 

## **3.2. Methodology** 

## **A. VaR for short and long trading positions** 

As we mentioned above, both RM and GARCH-type models are tested with a VaR level _α_ which ranges from 1% to 5% and their performance is then assessed by computing the failure rate for the returns _rt_ . By definition, the failure rate is the number of times returns exceed (in absolute value) the forecasted VaR. If the VaR model is correctly specified, the failure rate should be equal to the specified VaR level. In our empirical study, we define a failure rate _f l_ for the long trading positions; which is equal to the percentage of negative returns smaller than one-step-ahead VaR for long positions. In that order, we define _fs_ as the failure rate for short trading positions as the percentage of positive returns larger than the one-step-ahead VaR for short positions. Because the computation of the empirical failure rate defines a sequence of yes/no observations, we test the following hypothesis: _H0 : f = α_ against _Ha: f � α_ , where _f_ is the failure rate. We should note that the estimated failure rate _f_[ˆ] is given by the Kupiec (1995) LR test. For example, at the 5% level and if _T_ yes/no observations are available, a confidence interval for _f[ˆ]_ is given by: 

**==> picture [194 x 34] intentionally omitted <==**

Let us recall that the Kupiec test is one of the most popular tests applied in back testing. Let _x_ be the number of failures (that is the number of cases in which the loss exceeds the one forecasted by the VaR model) for a sample size _n_ . If the VaR model is correctly specified, _x_ follows the binominal distribution with parameter _(n,x)_ . The null hypothesis is that the forecasting model is correct; the TR statistic is expressed as follows: 

**==> picture [326 x 34] intentionally omitted <==**

where _p[*]_ is the loss probability of the VaR model to be tested. Under the null hypothesis, the Kupiec test statistic presented in equation (22) follows a chi-square distribution with one degree of freedom. 

## **B. The expected short-fall** 

According to Scaillet (2000), it is interesting to estimate the expected short-fall and the average multiple of tail event to risk measure. He defined the expected short-fall as the expected value of the losses conditioned on the loss being larger than the VaR. For a long trading position, it is 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

115 

Chaker Aloui / Mondher Bellalah 

computed as the average of the observed returns smaller than the long VaR. Correspondingly, the expected short-fall for the short VaR is computed as the average of the observed returns larger than the short VaR. 

## **4. Empirical findings** 

## **4.1. Preliminary results** 

Descriptive characteristics for the return series are given in Table 1. They show that the twenty five return series share similar statistical properties as far as third and fourth moments are concerned. More specifically, sixteen of the twenty five return series are negatively skewed and the large returns (either positive or negative) lead to a large degree of kurtosis. Descriptive Figures for level time series indexes are reported in appendix 1. Daily return figures[1] clearly show the volatility clustering. To detect long range dependency on emerging stock market volatilities, we apply the two usual tests, GPH and Lo’s (1991). We should note that volatility has been approximated by centred return _(rt – r[–] )_ , squared return _(rt – r[–] )[2]_ , absolute return / _rt – r[–]_ / and logarithm of absolute return _ln_ ( / _rt – r[–]_ /) . The results are reported in Tables 2 and 3. Table 2 presents the spectral regression estimates of the fractional differencing parameter _(d)_ for all the 25 stock indexes and volatility measures. A choice must be made with respect to the number of low-frequency periodogram ordinates used in the spectral regression. We should note that inclusion of medium or highfrequency periodogram ordinates will contaminate the estimate of _(d)_ ; at the same time too small a regression sample will lead to imprecise estimates. In light of the suggested choice by GPH (1983), we apply fractional differencing estimates for _T[0.5]_ , _T[0.55]_ and _T[0.8 ]_[2] to evaluate the sensitivity of our results to the choice of the sample size of the spectral regression. As shown in Table 2, there is evidence that all the twenty five stock returns exhibit fractional dynamics with long memory features. The fractional differencing parameters are statistically significant at the 1% level. They can be taken as strong evidence of the presence of long memory in these series[3] . Also, these parameters are similar in value across the various sample sizes of the spectral regression. All the twenty five series have long memory with positive value of _d_ varying from 0.2236 (Indonesia) to 0.7755 (Korea). Our results are consistent with Crato (1994), Cheung and Lai (1995), Barkoulas, Baum, and Travlos (2000), Sadique and Silvapulle (2001), Wright (2001) and Aloui et al. (2005). 

|Table 1.<br>Descriptive statistics|Table 1.<br>Descriptive statistics|Table 1.<br>Descriptive statistics|Table 1.<br>Descriptive statistics|Table 1.<br>Descriptive statistics|
|---|---|---|---|---|
|**Country**|**Mean**|**S.D**|**Skew.**|**Excess K.**|
|EGYPT|0.00995|1.60495|0.2159|6.56077|
|MOROCCO|0.00397|0.82821|0.4262|8.25716|
|S. AFRICA|0.01346|1.57670|-0.6450|8.47157|
|CHINA|0.05184|2.25678|0.04135|6.94287|



- 1 To reserve space, descriptive graphs for emerging markets daily returns are not shown here. They are available upon request. 

- 2 GPH test results for T[0.55] and T[0.8] are not shown here. They are available upon request. 

- 3 Similar results are obtained with T[0.55] and T[0.8] . 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

116 

Long Range Memory on Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

|**Country**|**Mean**|**S.D**|**Skew.**|**Excess K.**|
|---|---|---|---|---|
|INDIA|0.02462|1.69479|-0.35748|6.72894|
|PAKISTAN|0.00343|2.12293|-0.46788|10.1058|
|INDONESIA|-0.05389|3.62117|-0.99854|22.7491|
|S. KOREA|0.02477|26.8808|0.29072|11.4571|
|MALAYSIA|-0.03428|2.419147|-0.72214|49.8244|
|PHILLIPPINES|-0.0788|1.962528|1.126392|17.3046|
|TAIWAN|-0.0190|1.914551|-0.00028|5.14020|
|THAILAND|-0.03220|2.591373|0.879950|10.3469|
|JORDAN|0.03164|0.86348|0.44663|14.1470|
|TURKEY|0.013890|3.60606|-0.10851|8.75709|
|HUNGARY|0.051009|2.00060|-0.82562|13.2434|
|POLAND|0.00106|1.97079|-0.18588|5.50644|
|RUSSIA|0.036397|3.514770|-0.04060|11.6127|
|CZECH REP.|0.04498|1.63470|-0.13334|4.50926|
|ARGENTINA|-0.01642|2.57706|-1.45577|26.3649|
|BRASIL|0.00093|2.40281|-0.01753|8.877626|
|COLOMBIA|0.028294|2.402814|0.27946|10.0818|
|MEXICO|0.03684|1.90720|-0.72140|49.8244|
|PERU|0.01893|1.43687|-0.17551|9.397341|
|CHILE|0.00512|1.19765|-0.1223|6.06350|
|VENEZUELA|-0.00477|2.69484|-1.99877|53.3797|
|Note: S.D. is the standard deviation. Skew. Is the Skewness statistic. Excess K. is the excess<br>of Kurtosis. All the values are computed using STATA package.|||||



|**Table 2.**<br>Results of GPH test for_T 0.5_|**Table 2.**<br>Results of GPH test for_T 0.5_|**Table 2.**<br>Results of GPH test for_T 0.5_|**Table 2.**<br>Results of GPH test for_T 0.5_|**Table 2.**<br>Results of GPH test for_T 0.5_|
|---|---|---|---|---|
|Country|_(rt – r–)_|_(rt – r–)2_|/_rt – r–_/|_ln_(/_rt – r–_/)|
|EGYPT|0.3857†<br>(3.51)|0.3182†<br>(2.00)|0.3757†<br>(3.51)|0.3954†<br>(3.60)|
|MOROCCO|0.1319<br>(1.20)|0.2004<br>(1.82)|0.1323<br>(1.20)|0.11<br>(1.00)|
|S. AFRICA|0.3253†<br>(2.96)|0.301†<br>(2.74)|0.3305†<br>(2.96)|0.2485‡<br>(2.26)|
|CHINA|0.3124†<br>(5.31)|0.2316†<br>(2.26)|0.2789†<br>(3.01)|0.2768†<br>(3.09)|
|INDIA|0.3124†<br>(4.01)|0.3302†<br>(3.01)|0.2876†<br>(2.79)|0.2909†<br>(2.65)|



Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

117 

Chaker Aloui / Mondher Bellalah 

|Country|_(rt – r–)_|_(rt – r–)2_|/_rt – r–_/|_ln_(/_rt – r–_/)|
|---|---|---|---|---|
|PAKISTAN|0.3294†<br>(3.00)|0.4269†<br>(3.89)|0.3394†<br>(3.00)|0.1983<br>(1.80)|
|INDONESIA|0.2455†<br>(3.21)|0.48†<br>(4.37)|0.2347†<br>(2.99)|0.2236†<br>(3.34)|
|S. KOREA|0.7555†<br>(7.07)|0.5903†<br>(5.38)|0.7755†<br>(7.07)|0.5312†<br>(4.84)|
|MALAYSIA|0.5679†<br>(5.36)|0.3254†<br>(2.96)|0.5879†<br>(5.36)|0.5004†<br>(4.56)|
|PHILLIPPINES|0.2709‡<br>(2.46)|0.1369<br>(1.24)|0.2703‡<br>(2.46)|0.2613‡<br>(2.38)|
|TAIWAN|0.3374‡<br>(3.25)|0.3746†<br>(3.41)|0.3574†<br>(3.25)|0.1947<br>(1.77)|
|THAILAND|0.3721†<br>(3.36)|0.2845†<br>(2.59)|0.3685†<br>(3.36)|0.1882<br>(1.71)|
|JORDAN|0.2821†<br>(2.67)|0.0329<br>(0.30)|0.2932†<br>(2.67)|0.3128†<br>(2.85)|
|TURKEY|0.355†<br>(3.44)|0.2674‡<br>(2.43)|0.378†<br>(3.44)|0.2849†<br>(2.59)|
|HUNGARY|0.2966†<br>(2.68)|0.2499‡<br>(2.27)|0.2948†<br>(2.68)|0.3517†<br>(3.20)|
|POLAND|0.3301†<br>(3.095)|0.3182†<br>(2.00)|0.3393†<br>(3.09)|0.1923<br>(1.75)|
|RUSSIA|0.5121†<br>(4.68)|0.2991†<br>(2.72)|0.5135†<br>(4.68)|0.3052†<br>(2.78)|
|CZECH  REP.|0.2663‡<br>(2.34)|0.4786†<br>(4.36)|0.2576‡<br>(2.34)|0.2238‡<br>(2.56)|
|ARGENTINA|0.3398†<br>(3.00)|0.2289<br>(2.08)|0.3292†<br>(3.00)|0.1111<br>(1.01)|
|BRASIL|0.2561‡<br>(2.54)|0.3737†<br>(3.40)|0.2561‡<br>(2.33)|0.1908<br>(1.74)|
|COLOMBIA|0.0892<br>(0.81)|0.2274‡<br>(2.07)|0.092<br>(0.81)|-0.0154<br>(-0.14)|
|MEXICO|0.253‡<br>(2.30)|0.0511<br>(0.466)|0.253‡<br>(2.30)|0.3751†<br>(3.42)|
|PERU|0.3833†<br>(3.51)|0.1031<br>(0.94)|0.3857†<br>(3.51)|0.3954†<br>(3.60)|
|CHILE|0.2367‡<br>(3.02)|0.3182†<br>(2.90)|0.2341<br>(1.55)|0.2037<br>(1.85)|
|VENEZUELA|0.2869†<br>(2.61)|0.2946†<br>(2.68)|0.2863†<br>(2.61)|0.3138†<br>(2.86)|
|Note: *, ‡ and † designed respectively the signifcance level of 10%, 5% and 1%.|||||



Results reported in Table 3 indicate that all volatility proxies in all emerging stock markets series display a strong dependent structure. The R/S modified tests are statistically significant at the 1% level. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

118 

Long Range Memory on Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

**Table 3.** Results of Lo R/S modified test[4 ] _(q = 10)_ 

|**Table 3.**<br>Results of Lo R/S modifed test4_(q = 10)_|**Table 3.**<br>Results of Lo R/S modifed test4_(q = 10)_|**Table 3.**<br>Results of Lo R/S modifed test4_(q = 10)_|**Table 3.**<br>Results of Lo R/S modifed test4_(q = 10)_|**Table 3.**<br>Results of Lo R/S modifed test4_(q = 10)_|
|---|---|---|---|---|
|Country|_(rt – r–)_|_(rt – r–)2_|/_rt – r–_/|_ln_(/_rt – r–_/)|
|EGYPT|2.8551†|2.1825†|2.8551†|3.1073†|
|MOROCCO|2.5791†|2.1153†|2.5791†|2.0999†|
|S. AFRICA|2.5042†|2.5038†|2.5042†|2.3405†|
|CHINA|2.5563†|2.6543†|2.5044†|2.4657†|
|INDIA|2.5567†|2.5407†|3.0124†|3.0356†|
|PAKISTAN|2.8314†|2.5414†|2.8314†|2.3804†|
|INDONESIA|3.0324†|3.0605†|3.1121†|3.0313†|
|S. KOREA|3.8592†|2.7285†|3.8592†|3.7813†|
|MALAYSIA|4.5852†|3.0158†|4.5852†|4.5598†|
|PHILLIPPINES|3.6083†|2.3198†|3.6083†|3.2935†|
|TAIWAN|2.6175†|2.0371†|2.6175†|1.9262‡|
|THAILAND|4.0544†|3.3379†|4.0544†|4.0231†|
|JORDAN|1.9073‡|1.2974|1.9073‡|2.1546†|
|TURKEY|2.6143†|2.054†|2.6143†|2.5862†|
|HUNGARY|2.9569†|2.7742†|2.9569†|2.713†|
|POLAND|3.4827†|3.1108†|3.4827†|3.0425†|
|RUSSIA|4.1650†|3.2679†|4.1650†|3.7966†|
|CZECH REP.|2.7343†|2.5525†|2.7343†|1.7311|
|ARGENTINA|2.5911†|2.316†|2.5911†|1.9978|
|BRASIL|2.4054†|2.2246†|2.4054†|1.5521|
|COLOMBIA|2.4486†|2.4181†|2.4486†|1.7694|
|MEXICO|3.5289†|2.3962†|3.5289†|3.2697†|
|PERU|2.8551†|2.1825†|2.8551†|3.1073†|
|CHILE|2.3345†|2.3554†|2.2349†|1.4948|
|VENEZUELA|1.6367†|1.1053|1.6367|1.6347|
|Notes: string vector containing the estimated statistic with its corresponding order. If the esti-<br>mated statistic is outside the interval (0.809, 1.862), which is the 95 percent confdence interval<br>for no long-memory, a star symbol † is displayed. The other critical values are in Lo‘s paper.|||||



> 4 R/S modified tests were applied with various q values (Q=5, 15, 20, 50). The obtained results are quite similar. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

119 

Chaker Aloui / Mondher Bellalah 

In our empirical study, the whole sample was subdivided into sub-samples. Time series in the first sub-sample, running from 01/31/1997 to 07/31/2002 and totalling 1437 observations, were used for estimating unknown parameters of GARCH, IGARCH and FIGARCH models. The VaR estimates of the second sub-sample, running from 08/01/2002 to 11/19/2004 and totalling 600 observations, were then computed based on the parameter estimates obtained from the first sub-sample. These estimates were used to evaluate the out-of-sample performance of the diverse GARCH-type models in forecasting VaR. We adopted jointly the conditional variance given by GARCH-type models (GARCH(1,1), IGARCH(1,1), FIGARCH(1,d,1)) and the RM model. We should note that only a the standardized normal distribution for _εt_ was assumed for GARCHtype models. Thus, we consider four VaR estimation methods based on four models. As we have noted above, the parameter _λ_ was taken as 0.94 as suggested by RM (1996). Maximum likelihood estimation was performed for the three GARCH-type models. 

## **4.2. In sample VaR computation** 

In this subsection, we compute the one-step-ahead VaR for both GARCH-type and RM models. As we have noted above, the emerging stock market returns exhibit fat tails[5] . We expect poor performance by the models based on the normal distribution[6] . All the models are tested with a VaR level _α_ which ranges from 5% to 0.5%. Then we assess the failure rate _f l_ and _fs_ for long and short trading positions respectively. In Table 4, we present p-values for Kupiec LR test for EGYPT and MOROCCO. In Tables 5.a. and 5.b., we report summary results for all twenty five emerging stock market indexes for long and short trading positions respectively. So, we computed the number of times (out of 100) that the null hypothesis _f l_ = _α_ ( _fs_ = _α_ , respectively) is not rejected for the combined four possible values of _α_ ( _α = 5%, 2.5%, 1% and 0.5%_ ) at a significance level of 5%. 

For, EGYPT and MOROCCO[7] , the results indicate that 

1. VaR models based on the normal distribution (RM and GARCH-type models) cannot capture large returns, with large positive returns (i.e. short VaR) being somewhat better handled than large negative returns (i.e. long VaR). 

2. For the two countries and for long and short trading positions, the GARCH-type models with standardized skewed Student-t distributions, the performance improves considerably when compared to that of models based on the normal distribution. 

3. The skewed Student IGARCH model work better than all symmetric GARCH-type models and the RM model. The model performs correctly in 87.5% of all cases for negative returns (long VaR) and for positive returns (short VaR). 

4. The skewed Student FIGARCH model presents the best performance. It performs correctly in 100% of all cases for the two countries and for the two trading positions. 

> 5 This ist confirmed by descriptive properties of the data given in Table 1. 

> 6 This result was confirmed by Giot and Laurent (2001). Their empirical evidence was conducted on daily major stock indexes for the entire period 1984-2000. 

> 7 Complete in sample VaR results are available for all indexes on request. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

120 

Long Range Memory on Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

5. Tables 5.a. and 5.b. display the mean success rate for respectively long and short trading positions for all twenty five emerging stock indexes. As indicated in these Tables, the Skewed student FIGARCH performs correctly in 91% (mean success rate) of all cases for negative returns (i.e. long trading position). The mean success rates for skewed-Student GARCH and IGARCH models are 47% and 73% respectively. For positive returns (short trading position), the mean success rates are equal to 33%, 47% and 71% for respectively skewed Student GARCH, IGARCH and FIGARCH models. In sum, the skewed Student FIGARCH model has a significant effect on VaRs performances for both positive and negative stock returns. 

## **4.3. Out sample VaR computations** 

At this stage, we will test the out of sample performance of both GARCH-type and RM models. In fact, it will be interesting to test different GARCH-type models in a “real life situation”. VaR models have to give out–of-sample forecasts. VaR models are estimated on the known stock index returns (for example, up to time _t_ ) and then VaR forecasts are made for an _h_ time horizon (i.e. for the period _[t_ + 1 _, t + h]_ ). In our validation exercise, one day estimates are given for long and short trading positions ( _h = 1 day_ ). The out of sample VaR estimations were applied only on the skewed student FIGARCH model. Methodologically, we apply an iterative procedure[8] where, in the first iteration, the skewed Student FIGARCH model is estimated to predict the one-day-ahead VaR. As we have noted above, the first estimation sample covers the period from 01/31/1997 to 07/31/2002. The out of sample period covers the period from 08/01/2002 to 11/19/2004. The predicted one-day-ahead VaR is then compared with the observed returns and both results are recorded for later evaluation using appropriate statistical tests. In the second iteration, the estimation sample is augmented to include one more day, the model is re-estimated and the VaRs are predicted and recorded. The iterative procedure continues until the last observation in the sample. Then, the corresponding failure rates are computed by comparing the long and the short forecasts _VaRt+1_ with the observed _t + 1_ return for all the days of the out of sample period. The same statistics as in the sample tests were employed. The out sample VaR computations for long and short trading positions are displayed in Table 6.a. and 6.b. respectively. Briefly speaking, these results are quite similar to those obtained for the in-sample tests. The skewed-Student FIGARCH process performs rather well for out-sample VaR predictions for both long and short trading positions. The success rate is in the majority of cases close to 75% at a 5% significance level. 

## **4.4. The expected short-fall results** 

For the expected short-fall, we report complete results only[9] for EGYPT and MORROCO stock indexes in Table 7. Briefly, these results can be summarized as follows: The expected short-fall, expressed in terms of absolute value, is in most cases larger for the models based on the skewed Student distribution than for models based on normal distribution. It should be noted that the 

> 8 See, for example, Giot and Laurent (2001). 

> 9 Estimations results for the rest of stock indexes are quite similar and are not reported here. They are available from the co-authors upon request. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

121 

Chaker Aloui / Mondher Bellalah 

expected short-fall is not a tool to rank VaR models or assess the performance of models. It is very important for risk managers to answer the following question: “If the losses exceed the VaR, how much do I lose on average?” (See e.g. Giot and Laurent 2001, p.11). 

## **5. Summary and concluding remarks** 

VaR is a quantitative measure, which predicts the financial loss on an asset or portfolio over a time horizon at a given probability. This measure helps financial managers to asses their risks or a regulatory committees to set margin requirements. By its nature, VaR estimation depends on accurate predictions of uncommon events. It is commonly admitted in the literature that over short-term horizons conditional VaR models are usually found to be good candidates for forecasting possible trading positions’ loss-quantiles. In this paper, we extend the analysis by introducing long range dependence on stock indexes volatilities in conditional VaR models. We also take short and long trading positions into account. To consider jointly these trading positions brought us to look for a statistical model that correctly models the left and the right tails of the distribution of returns. Six GARCH-type (GARCH, IGARCH and FIGARCH) and RM models are proposed. Standardized normal, Student and skewed Student distributions were assumed for the GARCH-type models. We focused on four extreme percentiles ranging from 5% to 0.5%. All models were applied to daily data for twenty five emerging stock indexes covering the period 1997-2004. Methodologically, we proceeded in three stages. In the first stage, in-sample tests were conducted in order to estimate unknown parameters of the GARCH-type models. These estimates were used, in the second stage, to assess the out-of-sample performance of various GARCH models in forecasting VaR. In the last stage, we computed the expected short-fall and the average multiple of tail event to risk measure for the models. Our results show that in the majority of cases, the skewed Student FIGARCH model performs correctly for negative returns and positive returns. The skewed Student FIGARCH models seem to capture both long range dependence of emerging stock market volatility for all VaR levels for long and short trading positions. 

## **Appendices** 

**Figure 1:** Emerging markets stock indexes (1997:01-2004:11), daily frequency 

**==> picture [419 x 171] intentionally omitted <==**

**----- Start of picture text -----**<br>
Egypt Stock Index PriceFigure 1. Morocco Stock Index PriceFigure 2. South Africa Stock Index PriceFigure 3. China Stock Index PriceFigure 4.<br>31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04<br>Figure 6. Figure 8.<br>Figure 5. Pakistan Stock Index Price Figure 7. South Corea Stock Index Price<br>India Stock Index Price Indonesia Stock Index Price<br>31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04<br>Figure 9. Figure 10. Figure 11. Figure 12<br>300 300 300 120<br>250 250 250 100<br>200 80<br>Stock Index 150 Stock Index 200 Stock Index 200 Stock Index 60<br>100 150 150 40<br>20<br>50 100 100<br>120 200<br>250 800<br>100 150<br>200 600<br>80<br>Stock Index 150 Stock Index 60 Stock Index 400 Stock Index 100<br>100 40 200 50<br>50 20 0 0<br>**----- End of picture text -----**<br>


Wirtsch ~~a~~ ft und Management · Jahrga ~~n~~ g 3 · Nr. 5 · November 2006 

122 

Long Range Memory ~~o~~ n Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

**==> picture [428 x 422] intentionally omitted <==**

**----- Start of picture text -----**<br>
Malaisia Stock Index PriceFigure 9. Philippines Stock Index PriceFigure 10. Taiwan Stock Index PriceFigure 11. Thailand Stock Index PriceFigure 12.<br>31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04<br>Turkey Stock Index PriceFigure 14. Hungary Stock Index PriceFigure 15. Poland Stock Index PriceFigure 16. Russia Stock Index PriceFigure 17.<br>31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04<br>Argentina Stock Index PriceFigure 18. Figure 19. Colombia Stock Index PriceFigure 20. Mexico Stock Index PriceFigure 21.<br>Brasil Stock Index Price<br>31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04<br>Peru Stock Index PriceFigure 22. Chile Stock Index PriceFigure 23. Venezuela Stock Index PriceFigure 24. Czech. Republic Stock Index PriceFigure 25.<br>31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04 31 Jan 97 Date 18 Nov 04<br>Figure 13.<br>Jordan Stock Index Price<br>31 Jan 97 18 Nov 04<br>Date<br>500 800 500 300<br>400 600 400 250<br>300 200<br>400 300<br>Stock Index 200 Stock Index Stock Index Stock Index 150<br>100 200 200 100<br>0 0 100 50<br>600 600 700 600<br>500 500 600<br>400 400 500 400<br>Stock Index 300 Stock Index 300 Stock Index Stock Index<br>400 200<br>200 200<br>100 100 300 0<br>2000 1500 250 2500<br>1500 200 2000<br>1000<br>1000 150 1500<br>Stock Index Stock Index Stock Index Stock Index<br>500 500 100 1000<br>0 0 50 500<br>350 1000 300 250<br>300 250 200<br>250 800 200<br>150<br>Stock Index 200 Stock Index 600 Stock Index 150 Stock Index<br>150 100 100<br>100 400 50 50<br>160<br>140<br>120<br>Stock Index 100<br>80<br>60<br>**----- End of picture text -----**<br>


## **Table 4.** 

|**Table 4.**|**Table 4.**|**Table 4.**|
|---|---|---|
|VaRestimationsfor MOROCCO andEGYPT(insa|||
|_α_|5%|2.5%<br>1%|
|VaR for long trading position|||
|MORROCCO|||
|N-GARCH|0.00|4<br>0.001<br>0.0|
|RM|0.00|1<br>0.000<br>0.0|
|t-GARCH|0.00|2<br>0.003<br>0.0|
|t-IGARCH|0.04|5<br>0.001<br>0.0|
|sk-t-GARC|H<br>0.06|4<br>0.032<br>0.0|
|sk-t-IGAR|CH<br>0.44|3<br>0.332<br>0.4|
|sk-t-FIGA|RCH<br>0.56|7<br>0.443<br>0.4|
|EGYPT|||
|N-GARCH|0.00|3<br>0.031<br>0.0|
|RM|0.0|0<br>0.006<br>0.0|



Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

123 

Chaker Aloui / Mondher Bellalah 

|_α_|5%|2.5%|1%|0.5%|
|---|---|---|---|---|
|t-GARCH|0.001|0.023|0.006|0.043|
|t-IGARCH|0.023|0.022|0.032|0.043|
|sk-t-GARCH|0.043|0.066|0.124|0.234|
|sk-t-IGARCH|0.032|0.343|0.221|0.332|
|sk-t-FIGARCH|0.236|0.432|0.193|0.213|
|VaR for short trading position|||||
|MOROCCO|||||
|N-GARCH|0.000|0.000|0.0321|0.011|
|RM|0.001|0.023|0.043|0.003|
|t-GARCH|0.000|0.000|0.000|0.001|
|t-IGARCH|0.021|0.011|0.000|0.000|
|sk-t-GARCH|0.213|0.063|0.032|0.032|
|sk-t-IGARCH|0.332|0.024|0.442|0.332|
|sk-t-FIGARCH|0.554|0.543|0.091|0.469|
|EGYPT|||||
|N-GARCH|0.002|0.000|0.000|0.012|
|RM|0.032|0.021|0.022|0.011|
|t-GARCH|0.000|0.061|0.000|0.000|
|t-IGARCH|0.055|0.321|0.432|0.014|
|sk-t-GARCH|0.076|0.000|0.335|0.033|
|sk-t-IGARCH|0.432|0.433|0.446|0.789|
|sk-t-FIGARCH|0.561|0.211|0.436|0.678|
|Notes: P-values for the null hypothesis_fl = α_(i.e. failure rate for the long trading positions is<br>equal to_α_, top of the table) and_fs = α_(i.e. failure rate for the short trading positions is equal<br>to_α_, bottom of the table)._α_is equal successively to 5%, 2.5%, 1% and 0.5%. The models are<br>successively Normal-GARCH, RiskMetrics, Student-GARCH, Student-IGARCH, skewed Stu-<br>dend GARCH, skewed Student IGARCH and skewed Student FIGARCH.|||||



**Table 5.a.** 

In sample VaR results for all emerging stock markets indexes (long trading position) 

|**Table 5.a.**<br>In sample VaR results for all emergingstock markets indexes(longtradingposition)|**Table 5.a.**<br>In sample VaR results for all emergingstock markets indexes(longtradingposition)|**Table 5.a.**<br>In sample VaR results for all emergingstock markets indexes(longtradingposition)|**Table 5.a.**<br>In sample VaR results for all emergingstock markets indexes(longtradingposition)|**Table 5.a.**<br>In sample VaR results for all emergingstock markets indexes(longtradingposition)|**Table 5.a.**<br>In sample VaR results for all emergingstock markets indexes(longtradingposition)|**Table 5.a.**<br>In sample VaR results for all emergingstock markets indexes(longtradingposition)|**Table 5.a.**<br>In sample VaR results for all emergingstock markets indexes(longtradingposition)|
|---|---|---|---|---|---|---|---|
||N-GARCH|RM|t-GARCH|t-IGARCH|skew-t-<br>GARCH|skew-t-<br>IGARCH|skew-t-<br>FIGARCH|
|EGYPT|0|25|0|0|25|100|100|
|MOROCCO|0|0|0|0|50|75|100|
|S. AFRICA|0|0|0|25|50|75|100|
|CHINA|25|0|25|25|50|100|75|
|INDIA|25|0|50|0|50|75|75|
|PAKISTAN|25|0|50|0|75|100|50|
|INDONESIA|0|25|0|0|25|25|100|



Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

124 

Long Range Memory on Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

||N-GARCH|RM|t-GARCH|t-IGARCH|skew-t-<br>GARCH|skew-t-<br>IGARCH|skew-t-<br>FIGARCH|
|---|---|---|---|---|---|---|---|
|S. KOREA|0|25|0|25|50|50|100|
|MALAYSIA|25|25|25|25|25|100|100|
|PHILLIPPINES|25|50|0|50|0|75|100|
|TAIWAN|25|50|25|25|100|50|75|
|THAILAND|25|0|0|50|100|50|50|
|JORDAN|25|0|25|50|50|75|100|
|TURKEY|0|0|0|25|0|100|100|
|HUNGARY|0|0|0|75|25|50|100|
|POLAND|0|25|0|0|25|75|100|
|RUSSIA|25|0|0|0|50|75|100|
|CZECH REP.|50|0|25|50|25|75|100|
|ARGENTINA|50|25|50|25|50|75|100|
|BRASIL|25|0|0|25|100|50|100|
|COLOMBIA|25|50|0|0|50|25|75|
|MEXICO|25|25|0|0|0|100|75|
|PERU|50|0|25|50|50|100|100|
|CHILE|0|25|0|75|75|75|100|
|VENEZUELA|25|0|0|50|75|75|100|
|**Mean of**<br>**success rate**|**19%**|**14%**|**12%**|**26%**|**47%**|**73%**|**91%**|
|Notes: Number of times (out of 100) that the null hypothesis_fl = α_(i.e. failure rate for the long<br>trading positions is equal to_α_, top of the table) is not rejected  for the combined four possible<br>values of_α_(the level of signifcance is 5%). The models are successively Normal-GARCH,<br>RiskMetrics, Student-GARCH, Student-IGARCH, skewed Studend GARCH, skewed Student<br>IGARCH and skewed Student FIGARCH.||||||||



**Table 5.b.** 

In sample VaR results for all emerging stock market indexes (short trading position) 

|**Table 5.b.**<br>In sample VaR results for all emergingstock market indexes(short tradingposition)|**Table 5.b.**<br>In sample VaR results for all emergingstock market indexes(short tradingposition)|**Table 5.b.**<br>In sample VaR results for all emergingstock market indexes(short tradingposition)|**Table 5.b.**<br>In sample VaR results for all emergingstock market indexes(short tradingposition)|**Table 5.b.**<br>In sample VaR results for all emergingstock market indexes(short tradingposition)|**Table 5.b.**<br>In sample VaR results for all emergingstock market indexes(short tradingposition)|**Table 5.b.**<br>In sample VaR results for all emergingstock market indexes(short tradingposition)|**Table 5.b.**<br>In sample VaR results for all emergingstock market indexes(short tradingposition)|
|---|---|---|---|---|---|---|---|
||N-GARCH|RM|t-GARCH|t-IGARCH|skew-t-<br>GARCH|skew-t-<br>IGARCH|skew-t-<br>FIGARCH|
|EGYPT|0|0|0|50|50|100|100|
|MOROCCO|0|0|0|0|25|75|100|
|S. AFRICA|0|0|0|25|0|50|100|
|CHINA|0|0|50|50|50|75|100|
|INDIA|25|25|25|50|25|50|75|
|PAKISTAN|0|50|25|25|50|25|50|
|INDONESIA|25|0|25|25|25|25|100|



Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

125 

Chaker Aloui / Mondher Bellalah 

||N-GARCH|RM|t-GARCH|t-IGARCH|skew-t-<br>GARCH|skew-t-<br>IGARCH|skew-t-<br>FIGARCH|
|---|---|---|---|---|---|---|---|
|S. KOREA|25|25|0|25|0|50|50|
|MALAYSIA|0|0|0|50|50|25|75|
|PHILLIPPINES|0|25|25|25|50|25|25|
|TAIWAN|0|0|25|25|50|50|100|
|THAILAND|25|25|50|25|25|25|75|
|JORDAN|50|0|25|50|25|25|50|
|TURKEY|50|0|25|0|25|25|100|
|HUNGARY|0|0|25|0|50|25|75|
|POLAND|0|0|0|25|50|50|50|
|RUSSIA|0|0|0|25|75|25|25|
|CZECH REP.|0|25|0|50|75|25|50|
|ARGENTINA|0|25|25|25|50|75|50|
|BRASIL|0|0|50|25|25|50|100|
|COLOMBIA|25|50|25|25|25|50|50|
|MEXICO|0|0|0|50|0|75|25|
|PERU|0|0|0|25|0|50|75|
|CHILE|0|0|0|0|25|100|100|
|VENEZUELA|0|0|0|0|0|25|75|
|**Mean of**<br>**success rate**|**9**|**10**|**16**|**27**|**33**|**47**|**71**|
|Number of times (out of 100) that the null hypothesis_fl = α_(i.e. failure rate for the long trading<br>positions is equal to_α_, top of the table) is not rejected for the combined four possible values of<br>_α_(the level of signifcance is 5%). The models are successively Normal-GARCH, RiskMetrics,<br>Student-GARCH, Student-IGARCH, skewed Studend GARCH, skewed Student IGARCH and<br>skewed Student FIGARCH.||||||||



**Table 6.a** 

Out sample VaR results for the skewed student FIGARCH model  (All emerging markets stock indexes,  long trading position) 

|**Table 6.a**<br>Out sample VaR results for the skewed student FIGARCH model  (All emerging markets<br>stock indexes,  long trading position)|**Table 6.a**<br>Out sample VaR results for the skewed student FIGARCH model  (All emerging markets<br>stock indexes,  long trading position)|**Table 6.a**<br>Out sample VaR results for the skewed student FIGARCH model  (All emerging markets<br>stock indexes,  long trading position)|**Table 6.a**<br>Out sample VaR results for the skewed student FIGARCH model  (All emerging markets<br>stock indexes,  long trading position)|**Table 6.a**<br>Out sample VaR results for the skewed student FIGARCH model  (All emerging markets<br>stock indexes,  long trading position)|
|---|---|---|---|---|
|_α_|5%|2.5%|1%|0.5%|
|EGYPT|0.211|0.312|0.056|0.541|
|MOROCCO|0.002|0.092|0.331|0.442|
|S. AFRICA|0.562|0.751|0.521|0.265|
|CHINA|0.245|0.355|0.015|0.115|
|INDIA|0.333|0.151|0.542|0.000|
|PAKISTAN|0.541|0.736|0.874|0.012|
|INDONESIA|0.001|0.932|0.942|0.254|
|S. KOREA|0.04|0.234|0.774|0.354|
|MALAYSIA|0.211|0.520|0.335|0.215|



Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

126 

Long Range Memory on Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

|_α_|5%|2.5%|1%|0.5%|
|---|---|---|---|---|
|PHILLIPPINES|0.005|0.335|0.226|0.005|
|TAIWAN|0.069|0.652|0.002|0.224|
|THAILAND|0.024|0.664|0.154|0.542|
|JORDAN|0.245|0.002|0.135|0.447|
|TURKEY|0.009|0.119|0.554|0.751|
|HUNGARY|0.542|0.448|0.591|0.031|
|POLAND|0.664|0.412|0.005|0.022|
|RUSSIA|0.652|0.321|0.021|0.123|
|CZECH REP.|0.713|0.551|0.332|0.456|
|ARGENTINA|0.428|0.410|0.004|0.421|
|BRASIL|0.495|0.086|0.251|0.428|
|COLOMBIA|0.020|0.195|0.661|0.782|
|MEXICO|0.000|0.216|0.014|0.665|
|PERU|0.013|0.298|0.552|0.742|
|CHILE|0.055|0.335|0.011|0.445|
|VENEZUELA|0.251|0.541|0.000|0.515|
|Notes: P-values for the null hypothesis_fl = α_(i.e. failure rate for the long trading positions is<br>equal to_α_,_α_is equal successively to 5%, 2.5%, 1% and 0.5%). The failure rates are computed<br>for the skewed Student FIGARCH model (out of sample estimation).|||||



**Table 6.b** 

Out sample VaR results for the skewed Studend FIGARCH model  (All emerging markets stock indexes,  short trading position) 

|**Table 6.b**<br>Out sample VaR results for the skewed Studend FIGARCH model  (All emerging markets<br>stock indexes,  short trading position)|**Table 6.b**<br>Out sample VaR results for the skewed Studend FIGARCH model  (All emerging markets<br>stock indexes,  short trading position)|**Table 6.b**<br>Out sample VaR results for the skewed Studend FIGARCH model  (All emerging markets<br>stock indexes,  short trading position)|**Table 6.b**<br>Out sample VaR results for the skewed Studend FIGARCH model  (All emerging markets<br>stock indexes,  short trading position)|**Table 6.b**<br>Out sample VaR results for the skewed Studend FIGARCH model  (All emerging markets<br>stock indexes,  short trading position)|
|---|---|---|---|---|
|_α_|5%|2.5%|1%|0.5%|
|EGYPT|0.021|0.520|0.221|0.112|
|MOROCCO|0.115|0.697|0.512|0.005|
|S. AFRICA|0.335|0.255|0.332|0.026|
|CHINA|0.544|0.542|0.214|0.842|
|INDIA|0.551|0.332|0.224|0.693|
|PAKISTAN|0.066|0.006|0.558|0.568|
|INDONESIA|0.009|0.135|0.651|0.712|
|S. KOREA|0.089|0.054|0.006|0.000|
|MALAYSIA|0.632|0.004|0.010|0.449|
|PHILLIPPINES|0.421|0.054|0.278|0.334|
|TAIWAN|0.126|0.557|0.624|0.209|
|THAILAND|0.134|0.711|0.364|0.105|
|JORDAN|0.442|0.115|0.255|0.332|
|TURKEY|0.236|0.216|0.842|0.447|



Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

127 

Chaker Aloui / Mondher Bellalah 

|_α_|5%|2.5%|1%|0.5%|
|---|---|---|---|---|
|HUNGARY|0.512|0.225|0.002|0.876|
|POLAND|0.001|0.331|0.331|0.665|
|RUSSIA|0.005|0.412|0.114|0.705|
|CZECH REP.|0.514|0.235|0.322|0.099|
|ARGENTINA|0.489|0.551|0.229|0.282|
|BRASIL|0.875|0.005|0.558|0.641|
|COLOMBIA|0.544|0.101|0.154|0.209|
|MEXICO|0.214|0.901|0.099|0.334|
|PERU|0.256|0.662|0.103|0.645|
|CHILE|0.548|0.052|0.532|0.439|
|VENEZUELA|0.338|0.441|0.241|0.554|
|Notes: P-values for the null hypothesis_fs = α_(i.e. failure rate for the short trading positions is<br>equal to_α_),_α_is equal successively to 5%, 2.5%, 1% and 0.5%). The failure rates are computed<br>for the skewed Student FIGARCH model (out of sample estimation).|||||



|**Table 7.**<br>The expected short-fall for MOROCCO and EGYPT(in sample)|**Table 7.**<br>The expected short-fall for MOROCCO and EGYPT(in sample)|**Table 7.**<br>The expected short-fall for MOROCCO and EGYPT(in sample)|**Table 7.**<br>The expected short-fall for MOROCCO and EGYPT(in sample)|**Table 7.**<br>The expected short-fall for MOROCCO and EGYPT(in sample)|
|---|---|---|---|---|
|_α_|5%|2.5%|1%|0.5%|
|_Expected short-fall for long trading position_|||||
|MORROCCO|||||
|N-GARCH|-0.0321|-0.0421|-0.4532|-0.4867|
|RM|-0.0245|-0.0324|-0.0387|-0.0523|
|t-GARCH|-0.0342|-0.0423|-0.0457|-0.0498|
|t-IGARCH|-0.0466|-0.0487|-0.0532|-0.0556|
|sk-t-GARCH|-0.0343|-0.0367|-0.0412|-0.0436|
|sk-t-IGARCH|-0.0311|-0.0337|-0.0378|-0.0398|
|sk-t-FIGARCH|-0.0322|-0.0331|-0.3421|-0.3566|
|EGYPT|||||
|N-GARCH|-0.0443|-0.0467|-0.0489|-0.0512|
|RM|-0.0403|-0.0421|-0.0446|-0.0473|
|t-GARCH|-0.0456|-0.0466|-0.0476|-0.0501|
|t-IGARCH|-0.0447|-0.0455|-0.0476|-0.0488|



Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

128 

Long Range Memory on Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

|_α_|5%|2.5%|1%|0.5%|
|---|---|---|---|---|
|sk-t-GARCH|-0.0450|-0.0460|-0.0466|-0.0493|
|sk-t-IGARCH|-0.0422|-0.0447|-0.0486|-0.0491|
|sk-t-FIGARCH|-0.0443|-0.0452|-0.0467|-0.0488|
|_Expected short-fall for short trading position_|||||
|MOROCCO|||||
|N-GARCH|0.0324|0.0411|0.0435|0.0441|
|RM|0.0265|0.0332|0.0354|0.0378|
|t-GARCH|0.0344|0.0444|0.0467|0.0488|
|t-IGARCH|0.0487|0.0521|0.0533|0.0559|
|sk-t-GARCH|0.0553|0.0576|0.0601|0.0632|
|sk-t-IGARCH|0.0314|0.0433|0.0488|0.0465|
|sk-t-FIGARCH|0.0444|0.0466|0.0476|0.5022|
|EGYPT|||||
|N-GARCH|0.0433|0.0454|0.0465|0.0499|
|RM|0.0433|0.0455|0.0467|0.0498|
|t-GARCH|0.0446|0.0487|0.0489|0.0501|
|t-IGARCH|0.0501|0.0502|0.0511|0.0532|
|sk-t-GARCH|0.0433|0.0442|0.0477|0.0499|
|sk-t-IGARCH|0.0445|0.0476|0.0488|0.0490|
|sk-t-FIGARCH|0.0433|0.0456|0.0478|0.5019|
|Notes: The expected short-fall for the long and short VaR (at level_α_) given by Normal-GARCH,<br>RiskMetrics, Student-GARCH, Student-IGARCH, skewed Student GARCH, skewed Student<br>IGARCH and skewed Student FIGARCH.|||||



## **References** 

Aloui, C., E. Abaoub and M. Bellalah, 2005, “Long Range Dependence on Tunisian Stock Market Volatility”, _International Journal of Business,_ 10, 4, 1-26. 

Baillie, R.T., T. Bollerslev, and H.O. Mikkelsen, 1996, “Fractionally Integrated Generalized Autoregressive Conditional Heteroskedasticity”, _Journal of Econometrics,_ 73, 3-20. 

Barkoulas, J. T., and C. F. Baum, 1996, “Long term Dependence in Stock Returns”, _Economics Letters,_ 53, 253-259. 

Barkoulas, J. T., C. F. Baum, and N. Travlos, 2000, “Long Memory in the Greek Stock Market”, _Applied Financial Economics,_ 10, 177-184. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

129 

Chaker Aloui / Mondher Bellalah 

Crato, N., 1994, “Some International Evidence Regarding the Stochastic Behavior of Stock Returns”, _Applied Financial Economics,_ 4, 33-39. 

Cheung, Y-W., and K.S. Lai, 1995, “A Search for Long Memory in International Stock Market Returns”, _Journal of International Money and Finance,_ 14, 597-615. 

Ding, Z., C. W. J. Granger, and R.F. Engle, 1993, “A Long Memory Property of Stock Markets Returns and a New Model”, _Journal of Empirical Finance,_ 1, 83-106. 

Ding, Z., and Granger, C.W.J. 1996, “Modeling Volatility Persistence of Speculative returns: A New Approach”, _Journal of Econometrics,_ 73, 185-215. 

Geweke, J. and S. Porter-Hudack, 1983, “The Estimation and Application of Long Memory Time Series Models”, _Journal of Time Series Analysis,_ 4, 221-238. 

Giot, P. and S. Laurent, 2001, “Value-at-Risk for Long and Short Trading Positions”, CORE Discussion Working Paper, 22. 

Granger, C.W.J. and R. Joyeux, R., 1980, “An Introduction to Long Memory Time Series Models and Fractional Differencing”, _Journal of Time Series Analysis,_ 1, 15-29. 

Henry, O.T., 2002, “Long Memory in Stock Returns: Some International Evidence”, _Applied Financial Economics,_ 12, 725-729 

Hosking, J.R.M., 1981, “Fractional Differencing”, _Biometrika,_ 68,165-176. 

Hurvich, C.M., R.S. Deo, and J. Brodsky, 1998, “The Mean Squared Error of Geweke and PorterHudack’s Estimator of the Memory Parameter of Long Memory Time Series”, _Journal of Time Series Analysis,_ 19, 19-46. 

Hurvich, C.M and R.S. Deo, 1999, “Plug in Selection of Numbers of Frequencies in Regression Estimates of the Memory Parameter of Long Memory Time Series”, _Journal of Time Series Analysis,_ 20, 331-341. 

Kupiec, P. 1995, “Techniques for Verifying the Accuracy of Risk Measurement Models, _Journal of Derivatives,_ 2, 173-184. 

Lo, A.W., 1991, “Long Term Memory in Stock Market Prices”, _Econometrica,_ 59, 1279-1313. 

RiskMetrics, 1996, Risk Publications, “Value at Risk” Risk supplement. 

Robinson, P. M., 1995, “Gaussian Semiparametric Estimation of Long Range Dependence” _Annals of Statistics,_ 23, 1630-1661. 

Robinson, P.M., and M. Henry, 1996, Bandwidth Choice In Gaussian Semiparametric Estimation of Long Range Dependence, in P.M. Robinson and M. Rosenblatt eds. Athens Conference on Applied Probability in Time Series Analysis, II, New York, 220-232. 

Sadique, S. and P. Sillvapulle, 2001, “Long-term Memory in Stock Market Returns: International Evidence”, _International Journal of Finance and Economics_ , 6, 59-67. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

130 

Long Range Memory on Emerging Stock Market Volatility and Value at Risk. Estimations for Long and Short Trading Positions 

Scaillet, O. 2000, “Nonparametric Estimation and Sensivity Analysis of Expected Shortfall”, Mimeo, Université Catholique de Louvain, IRES. 

Siddiqui, M. 1976,”The Asymptotic Distribution of the Range and Other Functions of Partial Sums of Stationary Processes”, _Water Resources Research,_ 12, 1271-1276. 

Sowel, F., 1992, “Modeling Long-run Behavior with the Fractional ARIMA Models”, _Journal of Monetary Economics,_ 29, 277-302. 

Teverovsky, V. Taqqu M.S. and W. Willinger, 1999, “A Critical Look at Lo’s Modified R/S Statistic”, Journal of Statistical Planning and Inference, 80, 211-227. 

Wright, J.H. 2001, “Long Memory in Emerging Market Stock Returns”, _Emerging Markets_ Quarterly, 5, 50-55. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

131 

## Alois Strobl 

## **Soft Facts Rating** 

Nachdem die neuen Eigenkapitalvorschriften für Banken zu Beginn des Jahres 2006 vom österreichischen Nationalrat gebilligt worden sind, steht diese Thematik hier vor ihrer unmittelbaren praktischen Anwendung. In zahlreichen nationalen und internationalen Studien wurden diverse Aspekte von Basel II erhoben. Das Schwergewicht dieser Untersuchungen lag bis ca. 2002 auf einer Informationseinholung über notwendige Anpassungen und den Kenntnisstand bezüglich Basel II und verlagerte sich danach auf Untersuchungen der konkreten Maßnahmen für Banken und Unternehmen, die sich aus den neuen Eigenkapitalvorschriften ergeben. Diese Maßnahmen sind sehr eng mit den sogenannten „Hard Facts“ verknüpft. Hard Facts sind messbare Kennzahlen eines potentiellen Kreditnehmers, die in das Rating durch die Bank einfließen. „Soft Facts“ sind Ergebnisse einer qualitativen Bonitätsanalyse eines potentiellen Kreditnehmers, die nur schwer messbar sind [z.B. Managementqualität, (Unternehmens-)Strategie]. Den schwieriger zu messenden Soft Facts wurde bisher weniger Beachtung geschenkt. Gemeinsam mit Studierenden der Fachhochschule des bfi Wien und der Basel II Experts Group der Wirtschaftskammer Österreich (WKO) wurde zur Forschungsfrage **„Unterschiede im Verständnis des Soft Facts Ratings zwischen Banken und Unternehmen und Unterschiede im Verständnis der Auswirkungen des Soft Facts Ratings zwischen Banken und Unternehmen in Österreich“** eine Befragung für Unternehmen (KMU) und eine für Banken entwickelt und durchgeführt. Daraus wurden in einem weiteren Schritt Verbesserungspotentiale in der Kommunikation zwischen Banken und Unternehmen abgeleitet. Ziel ist es, den akkreditierten Basel II ExpertInnen der WKO auf Basis der Analysen das Wissen zum besseren Verständnis der Problematik zu geben, das diese im täglichen Beratungsalltag brauchen und einsetzen können. Die Ergebnisse der Studie werden im Herbst 2006 präsentiert. 

## **Rückfragehinweis:** 

Forschungsprojekt im Auftrag der Basel II Experts Group der Fachgruppe Unternehmensberatung und Informationstechnologie (UBIT) der WKO. 

Geplante Laufzeit: April 2006 bis Oktober 2006 

Projektleitung: Dipl. Ing. Alois Strobl, E-Mail: alois.strobl@fh-vie.ac.at 

Kooperationspartner: Basel II Experts Group der Fachgruppe UBIT der WKO 

Johannes Jäger 

## **Global Finance and the European Economy: the Struggle over Banking Regulation** 

Es wird weithin angenommen, dass der Globalisierungsprozess im Finanzsektor wesentlich durch das Dollar Wall Street Regime bestimmt wird. Es ist jedoch weniger klar, welche Rolle der Europäischen Union in diesem Prozess zukommt. Während einerseits die Europäische Union 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

133 

eher als passive Kraft angesehen wird, die sich einfach dem externen Druck der Globalisierung im Finanzsektor anpasst, so wird andererseits ebenso die wichtige Rolle der EU im Prozess globaler Regulierung hervorgehoben. Die konkrete Analyse der Auseinandersetzung um neue Grundlagen für eine Modernisierung der Bankenregulierung – Basel II – zielt darauf ab, dieser Frage nach der Rolle der EU bezogen auf die Globalisierung im Finanzsektor nachzugehen. Dies ist für die Abschätzung zukünftiger Regulierungsdynamik zentral. Die Analyse der Auseinandersetzungen um Basel II erfolgt überdies vor dem Hintergrund möglicher Wirkungen des neuen Regelwerks auf die europäische Wirtschaft. Analytisch erfolgt damit eine Verbindung in der Untersuchung von Form und Inhalt sich ändernder Regulierungsmuster. 

## **Rückfragehinweis:** 

Forschungsprojekt im Rahmen des durch die Österreichische Forschungsförderungsgesellschaft geförderten Programms FHplus zum Thema „Auswirkungen von Basel II auf Banken und in Folge auf Unternehmen (insbesondere KMU)“ 

Geplante Laufzeit: März 2006 bis Dezember 2006 

Projektleitung: Dr. Johannes Jäger, E-Mail: johannes.jaeger@fh-vie.ac.at 

Kooperationspartner: Prof. Dr. Hans-Jürgen Bieling, Universität Marburg (D) 

Johannes Jäger 

## **Transformation of Global Financial Governance:** 

## **global-local and local-global linkages** 

Gegenstand des Forschungsprojektes ist es, die aktuellen Entwicklungen in der Transformation globaler Governance im Finanzbereich in historischer Perspektive zu analysieren. Dies soll theoretisch durch die Synthetisierung bestehender Theorieansätze und empirisch durch die Analyse von zwei konkreten Fallstudien, geschehen. Ziel des Projektes ist es, GovernanceProzesse systematisch in ökonomische Strukturen einzubetten, um Determinanten und Wirkungen der Veränderungen von Financial Governance Prozessen umfassend zu analysieren. Überdies umfasst die Analyse die lokale und die globale Ebene in multi-skalarer Herangehensweise. Die erhofften Ergebnisse sollen dazu beitragen, die sich verändernden Formen und Ausmaße von Governance-Prozessen im Finanzbereich besser zu verstehen. Ein solches Verständnis kann eine wichtige Grundlage für die Antizipation von Trends in der Entwicklung von Finanzsystemen für ökonomische Akteure darstellen und soll diesen ermöglichen, Regulierungs- und Intervention smöglichkeiten auf unterschiedlichen räumlichen Ebenen noch besser auszuloten. 

## **Rückfragehinweis:** 

Forschungsprojekt gefördert durch den Jubiläumsfonds der Oesterreichischen Nationalbank Geplante Laufzeit: Juli 2006 bis Juni 2009 

Projektleitung: Rektor (FH) Prof. (FH) Dkfm. Dr. Rudolf Stickler E-Mail: rudolf.stickler@fh-vie.ac.at 

ProjektmitarbeiterInnen: Mag. Karen Imhof, Dr. Johannes Jäger 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

134 

## Robert Schwarz 

## **Branchenrisiko in Österreich** 

Ziel dieser Projektes ist, das Unternehmenswertmodell von Merton, das für die Modellierung von Ausfallsrisiken von Unternehmen konzipiert wurde, auf einer höheren Stufe, nämlich auf Branchenebene, die bei der Modellierung des Kreditrisikos im Vergleich zum Länderrisiko immer mehr an Bedeutung gewinnt, anzuwenden. Die Bedeutung des Branchenrisikos kann man auch daran erkennen, dass Moody’s/KMV in ihrem Tool RISKCALC[TM] die Branche als Kontrollvariable einführen und damit eine signifikant verbesserte Prognose von Ausfallswahrscheinlichkeiten feststellbar ist. Zu diesem Zweck werden alle relevanten Daten auf Branchenebene betrachtet, d.h. es wird eine Branche als ein Unternehmen modelliert und das Ausfallsrisiko des z.B. Unternehmens ‚Bauwirtschaft’ in Österreich berechnet. Die notwendigen Unternehmenskennzahlen wie EBITDA und die Kapitalstruktur der österreichischen Unternehmen stellt der österreichische Kreditschutzverband von 1870 zur Verfügung. 

## **Rückfragehinweis:** 

Forschungsprojekt im Rahmen des durch die Österreichische Forschungsförderungsgesellschaft geförderten Programms FHplus zum Thema „Auswirkungen von Basel II auf Banken und in Folge auf Unternehmen (insbesondere KMU)“ 

Projektleitung: Mag. Robert Schwarz E-Mail: robert.schwarz@fh-vie.ac.at Kooperationspartner: Kreditschutzverband von 1870 (KSV) 

Emel Kis 

## **Erasmus – Curriculum Development Project: ARIMA – Master Programme Quantitative Asset and Risk Management** 

Um dem Leitgedanken der Fachhochschule des bfi Wien **„Studieren auf europäischem Niveau“** gerecht zu werden, wird der studentischen Mobilität an der Fachhochschule des bfi Wien höchste Priorität gegeben. Deshalb werden die Schaffung eines europaweiten Netzwerkes und eine intensive und nachhaltige Zusammenarbeit mit europäischen Hochschulen angestrebt. 

Im Frühjahr 2006 hat die Fachhochschule des bfi Wien als Koordinatorin das Erasmus – Curriculum-Entwicklungsprojekt **„ARIMA – Master Programme Quantitative Asset and Risk Management“** bei der Europäischen Kommission erfolgreich eingereicht. Die Genehmigung zur Durchführung wurde im Sommer 2006 von der Europäischen Kommission erteilt. 

Inhaltlicher Projektleiter ist der Rektor (FH) und Leiter des Studiengangs „Bank- und Finanzwirtschaft“, Prof. (FH) Dr. Rudolf Stickler. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

135 

Ziel dieses Projektes ist die **Entwicklung und die Umsetzung eines gemeinsamen europäischen Master Programms** mit folgenden Hochschulen: 

- **Thames Valley University,** London, Großbritannien 

- **The New Anglo-American College in Prague,** Tschechische Republik 

- **Marmara University,** Istanbul, Türkei 

Bei der Wahl der Hochschulen wurde besonders auf die geografische Streuung der Partner geachtet, um so die europäische Dimension zu garantieren. 

Die Projektlaufzeit dieses Erasmus – Curriculum Entwicklungsprojektes beträgt 3 Jahre, wobei die ersten beiden Jahre für die gemeinsame Konzeption und das letzte Jahr für die gemeinsame Umsetzung des Master Programms vorgesehen sind. Mit den Arbeiten zur Entwicklung des Curriculums wurde im Oktober 2006 begonnen. **Im Wintersemester 2008/09 wird das Master Programm an allen beteiligten Hochschulen starten.** 

Die Fachhochschule des bfi Wien bietet seit 1998 den Studiengang „Bank- und Finanzwirtschaft“ und seit 2003 den postgradualen Lehrgang MBA Risk Management erfolgreich an. Darüber hinaus legt die Fachhochschule des bfi Wien seit mehreren Jahren den Fokus auf die angewandte Forschung im Bereich des Risikomanagements. Namhafte österreichische Banken wie Bank Austria-Creditanstalt, Erste Bank, Raiffeisen Zentralbank und nicht zuletzt die Oesterreichische Nationalbank zählen zu den Kooperationspartnern. Aber auch mit Organisationen wie dem Kreditschutzverband von 1870, der Basel II Experts Group der Wirtschaftskammer Österreich oder der Telekom Austria wurde bzw. wird auf Forschungsebene zusammengearbeitet. 

An den Partnerhochschulen wird ebenfalls bereits seit Jahren die Studienrichtung „Bank- und Finanzwirtschaft“ angeboten. 

Die Studierenden werden die Möglichkeit haben, im Rahmen dieses **viersemestrigen Master Programms** ein **Doppeldiplom**[1] zu erhalten. Dazu ist für sie ein Auslandssemester an einer Partnerhochschule verpflichtend. Weiters sind DozentInnenmobilität und Fernlehrelemente wie E-Learning vorgesehen. Unterrichtssprache des Master Programms wird in allen beteiligten Ländern Englisch sein. 

Folgende Module sind im Rahmen des Master Programms geplant: 

- Special Field 1: Quantitative Methods and Financial Theory 

- Special Field 2: Quantitative Risk Measurement 

- Special Field 3: Quantitative Asset Management 

- Special Field 4: Private Banking and Fund Management 

- Special Field 5: Risk Management in Banks and Integrated Bank Management 

- Special Field 6: Risk Management for Insurance Companies and Integrated Insurance Management 

> 1 Ein Doppelabschlussabkommen bietet Studierenden ohne wesentliche Verlängerung der Studiendauer die Möglichkeit, einen zweiten internationalen Grad an einer Partnerhochschule zu erwerben. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

136 

Neben einer nationalen ist auch eine **internationale Akkreditierung** des Master Programms vorgesehen. Voraussetzung für die Teilnahme am Master Programm ist ein Bachelorabschluss. AbsolventInnen dieses Master Programms können mit einem PhD-Studium[2] fortsetzen. 

## **Rückfragehinweis:** 

Projekt gefördert im Rahmen von Erasmus. Laufzeit: Oktober 2006 bis September 2009 Mag. Emel Kis, International Office der Fachhochschule des bfi Wien E-Mail: emel.kis@fh-vie.ac.at, Tel. ++43/1/720 12 86-85 

> 2 Laut neuer Abschlussarchitektur sind die Inhaber/innen eines Diplomgrades oder eines Mastergrades (einschließlich Fachhochschul-Diplomgraden oder Fachhochschul-Mastergraden) zur Zulassung zum Doktoratsstudium an einer Universität berechtigt. Der Doktorgrad (mit dem Wortlaut „Doktor/in ...“) wird nach einem Studium mit 120 ECTSAnrechnungspunkten, der akademische Grad „Doctor of Philosophy“ („PhD“) nach einem forschungsorientierten Studium mit 240 ECTS-Anrechnungspunkten verliehen (vgl. Bundesministerium für Bildung Wissenschaft und Kultur: Anhang zum Diplom / Diploma Supplement. 8. Das österreichische Hochschulsystem. Stand: Juli 2006. http://www. bmbwk.gv.at/universitaeten/diplomasupplement/DasDiplomaSupplement/Anhang_zum_Diplom__Diplo7750.xml) 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

137 

## **Veröffentlichungen der Fachhochschule des bfi Wien** 

_In diesem Abschnitt von „Wirtschaft und Management“ stellen wir Ihnen Arbeiten von FH-MitarbeiterInnen vor, die im Jahr 2006 zum Themenkomplex Basel II/Risikomanagement publiziert wurden bzw. werden._ 

## Christian Butschek 

## **Vertragsanpassung nach Basel II** 

In: BankArchiv. Zeitschrift für das gesamte Bank- und Börsenwesen. Veröffentlichung in Kürze. 

## _Abstract_ 

## _Adjustment of Contracts after Basel II_ 

Pursuant to the new capital adequancy rules the standard risk costs and the equity capital costs of a credit have to be calculated differently: the credit risk has to be taken into account to a greater extent than before. Loans for “bad” debtors will become more expensive, such for “good” debtors will become cheaper. What impact does this have on existing long-term contracts? Can – or even: must – a bank “transmit” different costs to the customer according to contractual clauses, especially to the “General Conditions of Banking”? Since we have to expect new contractual clauses enabling the bank to adjust the agreed interest rate to the current rating, another question will be, how such clauses have to be designed. The article analyses, if such clauses are valid under §§ 864 a, 879 Para 3 of the Austrian Civil Code and § 6 Para 1 No. 5 of the Consumer Protection Act and will try to make use of recent Supreme Court decisions concerning interest rate adjustment clauses, especially in consumer loans. 

Contact: christian.butschek@fh-vie.ac.at 

Article written in German. The article is to be published soon in BankArchiv. Zeitschrift für das gesamte Bank- und Börsenwesen. 

## Barbara Cucka 

## **Maßnahmen zur Ratingverbesserung. Empfehlungen von Wirtschaftstreuhändern** 

Working Paper. Juli 2006. 

## _Abstract_ 

## _Measures to improve corporate ratings_ 

This study analyses how tax consultants, auditors and chartered accountants in Austria and Switzerland advise their clients on questions regarding bank-ratings and points out differences and similarities in these two countries. The paper focuses on the question of how the above mentioned consultants advise their clients in their preparation for a rating process in connection with the application for bank loans and which measures they suggest to improve results from an earlier 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

139 

rating. The underlying research was imbedded in an ongoing cooperation project between the University of Applied Sciences bfi Vienna and the University of Applied Sciences Northwestern Switzerland. 

Contact: barbara.cucka@fh-vie.ac.at 

Working Paper written in German. 

Download: http://www.fh-vie.ac.at/files/workingpapers/0068181405.pdf 

## Stephanie Messner 

## **Offenlegungserfordernisse für Banken nach Basel II (Säule 3) und IFRS –** 

## **Die doppelte Herausforderung** 

In: BankArchiv. Zeitschrift für das gesamte Bank- und Börsenwesen. Veröffentlichung in Kürze. 

## _Abstract_ 

## _Disclosure requirements for banks according to Basel II (pillar 3) and IFRS – the twofold challenge_ 

European banks are facing a twofold challenge. The first-time implementation of the Basel Capital Accord (Basel II) in 2007 closely coincides with the mandatory IFRS-reporting beginning with 2005 and 2007 respectively. Both frameworks include regulations concerning the disclosure of certain information by banks, which, however, overlap to some extent. The paper at hand presents an overview of the disclosure-requirements of banks concerning equity capital, risks taken and the like. It compares the regulations of the third pillar of Basel II with those of the IFRS and especially focuses on the necessity of harmonizing the two frameworks. 

Contact: stephanie.messner@fh-vie.ac.at 

Article written in German. The article is to be published soon in BankArchiv. Zeitschrift für das gesamte Bank- und Börsenwesen. 

## Robert Schwarz 

## **Der Doppelausfalleffekt und Basel II** 

In: Fachhochschule des bfi Wien (Hg.), Wirtschaft und Management. Jahrgang 3, Nr. 3, November 2005. S. 37-46. 

## _Abstract_ 

## _Double Default Effects_ 

In July 2005 the Basel Committee on Banking Supervision (BCBS) issued a consultation paper with the title ‘The Application of Basel II to Trading Acitivities and the Treatment of Double Default Effects’ in cooperation with the International Organization of Securities Commissions (IOSCO). In 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

140 

this revised framework the treatment of the double-default effect for covered exposures in Basel II is an important issue. Double default means the risk associated with a loan that both the obligor and the guarantor default in the same time span. This paper analyzes the new approach to the treatment of double default in Basel II and shows possible impacts on the regulatory capital. 

Contact: robert.schwarz@fh-vie.ac.at 

Article written in German. Download: http://basel2.fh-vie.at/files/0051128103625.pdf 

Thomas Wala/Stephanie Messner 

## **Die Berücksichtigung von Ungewissheit und Risiko in der Investitionsrechnung** 

## _Abstract_ 

## _Uncertainty and risk when evaluating investment projects_ 

The article illustrates the methods that can be used to account for uncertainty and risk when evaluating investment projects. Chapter 2 presents the net present value as the most important tool in modern investment analysis. Chapter 3 focuses on the difference between uncertainty and risk and its consequences for investment decisions. The different methods available to account for uncertainty and risk (sensitivity analyses, CAPM etc.) are outlined in chapter 4 of this paper. Chapter 5 gives a short summary of the contents presented. This article is not supposed to find answers to particular scientific problems. The main emphasis is rather put on giving a simple and practical guideline to dealing with risk and uncertainty in modern investment analysis. 

Contact: thomas.wala@fh-vie.ac.at, stephanie.messner@fh-vie.ac.at 

Article written in German. Download: http://basel2.fh-vie.at/files/U1_Ausgabe4.pdf 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

141 

## **Literaturhinweise** 

## **Finanzmarktregulierung** 

Walter Herzog/Miriam Mansel/Katja Schmidt (Hrsg.) (2006) 

## **Handbuch der Offenlegungsvorschriften für Kreditinstitute. Corporate Governance,** 

## **IFRS, Basel II** 

ISBN 3791025341, Schaeffer-Poeschel 

Kai-Oliver Klauck/Claus Stegmann (2006) 

## **Stresstests in Banken. Von Basel II bis ICAAP** 

ISBN 3791025201, Schaeffer-Poeschel 

Peter Mooslechner/Helene Schuberth/Beat Weber (Hrsg.) (2006) 

## **The Political Economy of Financial Market Regulation. The Dynamics of Inclusion and** 

## **Exclusion** 

ISBN: 139781845425180, Edward Elgar 

Axel Becker/Markus Gaulke/Martin Wolf (Hrsg.) (2005) 

## **Praktiker-Handbuch Basel II. Kreditrisiko, operationelles Risiko, Überwachung,** 

## **Offenlegung** 

ISBN: 3791019856, Schaeffer-Poeschel 

Axel Becker/Martin Wolf (2005) 

**Prüfungen in Kreditinstituten und Finanzdienstleistungsunternehmen. Interne und externe Revision, Jahresabschlussprüfung, Bankenaufsicht** 

ISBN 3865561160, Bank-Verlag 

## **Quantitative Methoden** 

Roger B. Nelsen (2006, 2nd edition) 

## **An Introduction to Copulas** 

ISBN: 0387286594, Springer 

Alexander McNeil/ Rüdiger Frey/ Paul Embrechts (2005) 

## **Quantitative Risk Management: Concepts, Techniques and Tools** 

ISBN: 0691122555, Princeton University Press 

## **Qualitative Methoden** 

Christian Einhaus (2006) 

## **Potenziale des Wissensmanagements zur Behandlung operationeller Risiken in der** 

## **Kreditwirtschaft** 

ISBN: 9783937519531, Bankakademie-Verlag 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

142 

## **Verzeichnis der AutorInnen** 

## **AutorInnen der Beiträge** 

## **Chaker Aloui** 

A Doctor of International Finance, Aloui Chaker has taught International Finance, Derivative Products, Portfolio Management, Managing Financial Risks and the Master’s Seminar in International Finance at the Faculty of Management and Economic Sciences of Tunis (El ManarUniversity) for 12 years. He has published several papers in “International Journal of Business”, “Revue Economie Internationale”, “Quantitative Finance”, “Revue du Financier”, “Revue Gestion 2000”, “Euromediterranean Economic and Finance Review” and several books including _Finance internationale_ (CPU, first edition 2003) and _Les options réelles_ (forthcoming, 2007, CPU edition). He has created the first research group specializing in international finance (INTERNATIONAL FINANCE GROUP-TUNISIA) in Tunisia. 

## **Mondher Bellalah** 

is a Professor of Finance. He has published more than 120 papers in leading finance journals and 12 books. He is the President of the Euro-Mediterranean Network. His research interests cover corporate finance and financial markets. 

## **Mag. Thomas Happ** 

ist seit September 2006 bei der AKRON Management Holding als Assistent des CFO beschäftigt. In den Jahren 1998 bis August 2006 war Thomas Happ bei der Telekom Austria tätig. Von Mitte 2005 bis August 2006 lag der Schwerpunkt seiner Tätigkeit im Bereich Corporate Finance (Rating, EMTN-Programm). Im Zeitraum Oktober 2000 bis Mitte 2005 waren seine Aufgabenschwerpunkte das Risikomanagement, die Implementierung eines webbasierten Reportingtools, die Einführung eines integrierten Treasury-Management-Systems sowie SOA-IKS. Davor war Thomas Happ im Vertrieb der Telekom Austria tätig (1998 – 2000). Das Studium der Betriebswirtschaftslehre absolvierte er von 1998 bis 2003 an der Wirtschaftsuniversität Wien und der Universität Innsbruck. Forschungsschwerpunkt war hier das Thema „Value Reporting“. 

## **o.Univ.-Prof. Dr. Gerwald Mandl** 

ist seit 1978 ordentlicher Universitätsprofessor und seit 1986 Vorstand des Instituts für Revisions-, Treuhand- und Rechnungswesen an der Karl-Franzens-Universität Graz, u. a. Gastprofessor an der Universität Münster, Vorsitzender des Arbeitskreises Unternehmensbewertung des Fachsenats für Betriebswirtschaft und Organisation der Kammer der Wirtschaftstreuhänder. Autor, Co-Autor und Herausgeber zahlreicher Fachpublikationen insbesondere zur Unternehmensbewertung. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

143 

## **Dr. Georg von Pföstl** 

ist seit September 2006 in der Oesterreichischen Nationalbank (OeNB), Abteilung für Bankenanalyse und -revision tätig. Vor seiner Tätigkeit in der OeNB arbeitete er bei Accenture Wien im Bereich Financial Services mit Hauptfokus Basel II. Georg von Pföstl absolvierte ein BWL-Studium, das er an der WU-Wien mit den Schwerpunkten Bankbetriebslehre sowie Finanzierung und Kapitalmärkte abschloss. An derselben Universität promovierte er mit einer Dissertation zum Thema Kreditrisiko und Rating im Rahmen von Basel II. Die Themen seiner Forschungsprojekte liegen im Bereich der internationalen Bank- und Finanzmärkte. 

## **Dr. Rainer Pullirsch** 

ist Mitarbeiter in der Abteilung Operationales Risiko und Modellentwicklung der Bank Austria Creditanstalt. Nach dem Diplomstudium der technischen Physik arbeitete er als Forschungsassistent an der Technischen Universität Wien und promovierte im Jahre 2001 in theoretischer Physik. 

In letzter Zeit beschäftigt sich Rainer Pullirsch hauptsächlich mit dem Marktrisiko und der Bewertung von Kreditderivaten. 

## **Dr. Tatjana Eva Putz** 

ist Managerin im Bereich Strategie/Financial Services bei Accenture im Wiener Büro. Sie ist spezialisiert auf Risikomanagement und beschäftigt sich insbesondere mit Basel II sowie Finance und Performance Management. Sie absolvierte das Studium der Mathematik an der Universität Wien und promovierte an der Wirtschaftsuniversität Wien. 

## **Ass. Prof. Mag. Dr. Klaus Rabel** 

ist Assistenzprofessor am Institut für Revisions-, Treuhand- und Rechnungswesen der KarlFranzens-Universität Graz. Er arbeitet als geschäftsführender Gesellschafter der BDO Graz Wirtschaftsprüfungs- und Steuerberatungsgesellschaft mbH, der BDO Rabel & Pilz Wirtschaftstreuhand und Steuerberatungs GmbH, sowie der Kommunalconsult Wirtschaftstreuhand & Steuerberatungs GmbH. Klaus Rabel absolvierte sein Studium der Betriebwirtschaftslehre an der Karl-Franzens-Universität Graz. 

## **Dipl. Kfm. Oliver Scheil, MBA** 

ist Manager im Bereich Strategie/Financial Services und bei Accenture im Münchener Büro. Er ist spezialisiert auf die Analyse und Entwicklung von Bankbetriebsmodellen und Geschäftsmodellen, Banksteuerung und Controlling, Finance & Accounting sowie die Erstellung von Wirtschaftlichkeitsberechnungen (Business Cases). Herr Scheil hat einen Abschluss als Diplom-Kaufmann der Universität Regensburg, einen Abschluss als Master of Business Administration (Murray State University, USA) sowie eine Ausbildung zum Bankkaufmann. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

144 

## **Dipl.-Vw. Hans-Joachim Schramm** 

ist Fachbereichsleiter für Logistik, Transport und Verkehr sowie Lektor in den Studiengängen „Logistik und Transportmanagement“ und „Europäische Wirtschaft und Unternehmensführung“ an der Fachhochschule des bfi Wien. Daneben ist er regelmäßig als Dozent an der Wirtschaftsuniversität Wien und der Donauuniversität Krems tätig. Seine fachlichen Schwerpunkte liegen im Bereich Güterverkehrs- und Speditionswesen sowie internationales Transport- und Logistikmanagement. 

## **Mag. Robert Schwarz** 

arbeitet seit Oktober 2006 bei der Bank Austria-Creditanstalt im Bereich Strategisches Risikomanagement. Nach dem Studium der Volkswirtschaftslehre an der Universität Innsbruck war er in der Mathematikabteilung einer österreichischen Versicherung und zuletzt als wissenschaftlicher Mitarbeiter an der Fachhochschule des bfi Wien mit Forschungsschwerpunkt Kreditrisiko tätig. 

## **Erich Stark** 

ist seit Dezember 2003 bei der Telekom Austria in der Abteilung Corporate Finance des Bereiches Group Finance & Treasury beschäftigt. Seine Aufgabenschwerpunkte sind die Analyse und Bewertung von Finanzinstrumenten und Finanzierungen sowie Fragestellungen zum Thema Kapitalkosten für die gesamte Telekom Austria Gruppe. Zuvor absolvierte er das Studium der Betriebswirtschaftslehre an der Universität Wien unter Spezialisierung auf die Gebiete Kapitalmärkte und Risikomanagement. 

## **AutorInnen der Berichte und redaktionellen Beiträge** 

## **Dr. Christian Butschek, LL.M.** 

ist seit 2001 hauptamtlicher Lektor an der Fachhochschule des bfi Wien. Er hält Lehrveranstaltungen zum bürgerlichen und Unternehmensrecht, darunter Bankvertragsrecht und zum europäischen Wirtschaftsrecht in den Studiengängen „Bank- und Finanzwirtschaft“, „Europäische Wirtschaft und Unternehmensführung“ sowie „Logistik und Transportmanagement“. Publikationen in den erwähnten Fachgebieten. Davor arbeitete er als Rechtsanwalt mit Tätigkeitsschwerpunkt Wirtschaftsrecht. 

## **Mag. (FH) Barbara Cucka** 

ist Lektorin des Fachhochschul-Studiengangs „Europäische Wirtschaft und Unternehmensführung“ an der Fachhochschule des bfi Wien mit Spezialgebiet Basel II und Unternehmen, insbesondere Ratingverbesserung und Finanzierungsalternativen. Sie leitet ein Kooperationsprojekt zum Thema Risikobewertung und Risikoverbesserung für KMUs. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

145 

## **Dr. Johannes Jäger** 

ist Lektor an der Fachhochschule des bfi Wien. Im Anschluss an das Studium der Volkswirtschaft war er als Assistent an der Wirtschaftsuniversität Wien sowie als Wissenschaftlicher Mitarbeiter an der Österreichischen Akademie der Wissenschaften tätig. Seine Forschungsschwerpunkte liegen in den Bereichen Finanzsysteme und Regulation sowie Internationale Politische Ökonomie und Regionalökonomie. 

## **Mag. Emel Kis** 

ist EU-Projektbeauftragte im International Office an der Fachhochschule des bfi Wien und die Organisatorische Leiterin des Erasmus Curriculum Development (CD) Projektes „ARIMA – Master Programme Quantitative Asset and Risk Management“ und des Erasmus Intensiv Programms (IP) „Central and South Eastern European Management“. 

## **Dr. Stephanie Messner** 

ist Lektorin an den Fachhochschul-Studiengängen „Bank- und Finanzwirtschaft“ sowie „Projektmanagement und Informationstechnik“ an der Fachhochschule des bfi Wien. Daneben ist sie als selbständige Trainerin in der Erwachsenenbildung tätig. Ihre fachlichen Schwerpunkte liegen in den Bereichen Rechnungslegung, Kostenrechnung und Controlling. 

## **D.I. Alois Strobl** 

ist Lektor an der Fachhochschule des bfi Wien mit den Schwerpunkten Mathematik und Statistik. Nach der Offiziersausbildung im ÖBH absolvierte er das Studium der Nuklearphysik an der TU-Wien. Im Anschluss daran arbeitete er im Marketing bei Siemens, später als Außendienstmitarbeiter und Sales Manager bei verschiedenen Unternehmen der Pharmabranche. Nach dem Abschluss des MBA-Studiums in Minneapolis (USA) und einem längeren Auslandsaufenthalt begann er seine Tätigkeit an der Fachhochschule des bfi Wien. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

146 

## **Working Papers und Studien der Fachhochschule des bfi Wien** 

**Die aufgelisteten Titel stehen auf der Homepage der Fachhochschule des bfi Wien http://www.fh-vie.ac.at/ unter dem Menüpunkt Forschung als Downloads zur Verfügung.** 

## **2006 erschienene Titel** 

## **Working Paper Series No. 22** 

Thomas Wala: Steueroptimale Rechtsform. Wien Mai 2006. 

## **Working Paper Series No. 23** 

Thomas Wala: Planung und Budgetierung. Entwicklungsstand und Perspektiven. Wien Mai 2006. 

## **Working Paper Series No. 24** 

Thomas Wala: Verrechnungsproblematik in dezentralisierten Unternehmen. Wien Mai 2006. 

## **Working Paper Series No. 25** 

Felix Butschek: The Role of Women in Industrialization. Mai 2006. 

## **Working Paper Series No. 26** 

Thomas Wala: Anmerkungen zum Fachhochschul-Ranking der Zeitschrift INDUSTRIEMAGAZIN. Mai 2006. 

## **Working Paper Series No. 27** 

Thomas Wala/Nina Miklavc: Betreuung von Diplomarbeiten an Fachhochschulen. Juni 2006. 

## **Working Paper Series No. 28** 

Grigori Feiguine: Auswirkungen der Globalisierung auf die Entwicklungsperspektiven der russischen Volkswirtschaft. Juli 2006. 

## **Working Paper Series No. 29** 

Barbara Cucka: Maßnahmen zur Ratingverbesserung. Juli 2006. 

## **Working Paper Series No. 30** 

Evamaria Schlattau: Wissensbilanzierung an Hochschulen. Oktober 2006. 

## **Studien** 

Andreas Breinbauer/Gabriele Bech (Hg.): „Gender Mainstreaming“. Chancen und Perspektiven für die Logistik- und Transportbranche in Österreich und insbesondere in Wien. Studie. März 2006. 

Andreas Breinbauer/ Michael Paul (Hg): Marktstudie Ukraine. Zusammenfassung von Forschungsergebnissen sowie Empfehlungen für einen Markteintritt. Juli 2006. 

Katharina Kotratschek/Andreas Breinbauer: Markt-, Produkt- und KundInnenanforderungen an Transportlösungen. Abschlussbericht. Ableitung eines Empfehlungskataloges für den Wiener Hafen hinsichtlich der Wahrnehmung des Binnenschiffverkehrs auf der Donau und Definition der Widerstandsfunktion, inklusive Prognosemodellierung bezugnehmend auf die verladende Wirtschaft mit dem Schwerpunkt des Einzugsgebietes des Wiener Hafens. August 2006. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

147 

## **2005 erschienene Titel** 

## **Working Paper Series No. 10** 

Thomas Wala: Aktuelle Entwicklungen im Fachhochschul-Sektor und die sich ergebenden Herausforderungen für berufsbegleitende Studiengänge. Wien Jänner 2005. 

## **Working Paper Series No. 11** 

Martin Schürz: Monetary Policy’s New Trade-Offs? Wien Jänner 2005. 

## **Working Paper Series No. 12** 

Christian Mandl: 10 Jahre Österreich in der EU. Auswirkungen auf die österreichische Wirtschaft. Wien Februar 2005. 

## **Working Paper Series No. 13** 

Walter Wosner: Corporate Governance im Kontext investorenorientierter Unternehmensbewertung. Mit Beleuchtung Prime Market der Wiener Börse. Wien März 2005. 

## **Working Paper Series No. 14** 

Stephanie Messner: Die Ratingmodelle österreichischer Banken. Eine empirische Untersuchung im Studiengang Bank- und Finanzwirtschaft der Fachhochschule des bfi Wien. Wien April 2005. 

## **Working Paper Series No. 15** 

Christian Cech/Michael Jeckle: Aggregation von Kredit und Marktrisiko. Wien Mai 2005. 

## **Working Paper Series No. 16** 

Thomas Benesch/ Franz Ivancsich: Aktives versus passives Portfoliomanagement. Wien Juni 2005. 

## **Working Paper Series No. 17** 

Franz Krump: Ökonomische Abschreibung als Ansatz zur Preisrechtfertigung in regulierten Märkten. Wien August 2005. 

## **Working Paper Series No. 18** 

Nathalie Homlong/Elisabeth Springler: Thermentourismus in der Ziel 1-Region Burgenland und in Westungarn als Mittel für nachhaltige Regionalentwicklung? Wien September 2005. 

## **Working Paper Series No. 19** 

Thomas Wala/Stephanie Messner: Die Berücksichtigung von Ungewissheit und Risiko in der Investitionsrechnung. Wien November 2005. 

## **Working Paper Series No. 20** 

Daniel Bösch/Carmen Cobe: Structuring the uses of Innovation Performance Measurement Systems. Wien November 2005. 

## **Working Paper Series No. 21** 

Julia Lechner/Thomas Wala: Wohnraumförderung und Wohnraumversorgung in Wien Dezember 2005. 

## **Studien** 

Johannes Jäger (ed.): Basel II: Perspectives of Austrian Banks and medium sized enterprises. Study. Vienna March 2005. 

Stephanie Messner/Dora Hunziker: Ratingmodelle österreichischer und schweizerischer Banken. Eine ländervergleichende empirische Untersuchung in Kooperation der Fachhochschule des bfi Wien mit der Fachhochschule beider Basel. Studie. Wien Juni 2005. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

148 

Michael Jeckle/Patrick Haas/Michael Palmosi: Regional Banking Study. Ertragskraft-Untersuchung 2005. Studie (Kooperation zwischen Finance Trainer und Fachhochschule des bfi Wien). Wien November 2005. 

## **2004 erschienene Titel** 

## **Working Paper Series No. 1** 

Christian Cech: Die IRB-Formel zur Berechnung der Mindesteigenmittel für Kreditrisiko. Laut Drittem Konsultationspapier und laut „Jänner-Formel“ des Baseler Ausschusses. Wien März 2004. 

## **Working Paper Series No. 2** 

Johannes Jäger: Finanzsystemstabilität und Basel II - Generelle Perspektiven. Wien März 2004. 

## **Working Paper Series No. 3** 

Robert Schwarz: Kreditrisikomodelle mit Kalibrierung der Input-Parameter. Wien Juni 2004. 

## **Working Paper Series No. 4** 

Markus Marterbauer: Wohin und zurück? Die Steuerreform 2005 und ihre Kritik. Wien Juli 2004. 

## **Working Paper Series No. 5** 

Thomas Wala/Leonhard Knoll/Stephanie Messner/Stefan Szauer: Europäischer Steuerwettbewerb, Basel II und IAS/IFRS. Wien August 2004. 

## **Working Paper Series No. 6** 

Thomas Wala/Leonhard Knoll/Stephanie Messner: Temporäre Stilllegungsentscheidung mittels stufenweiser Grenzkostenrechnung. Wien Oktober 2004. 

## **Working Paper Series No. 7** 

Johannes Jäger/Rainer Tomassovits: Wirtschaftliche Entwicklung, Steuerwettbewerb und politics of scale. Wien Oktober 2004. 

## **Working Paper Series No. 8** 

Thomas Wala/Leonhard Knoll: Finanzanalyse - empirische Befunde als Brennglas oder Zerrspiegel für das Bild eines Berufstandes? Wien Oktober 2004. 

## **Working Paper Series No. 9** 

Josef Mugler/Clemens Fath: Added Values durch Business Angels. Wien November 2004. 

## **Studien** 

Andreas Breinbauer/Rudolf Andexlinger (Hg.): Logistik und Transportwirtschaft in Rumänien. Marktstudie durchgeführt von StudentInnen des ersten Jahrgangs des FH-Studiengangs „Logistik und Transportmanagement“ in Kooperation mit Schenker & Co AG. Wien Juni 2004. 

Christian Cech/Michael Jeckle: Integrierte Risikomessung für den österreichischen Bankensektor aus Analystenperspektive. Studie in Kooperation mit Walter Schwaiger (TU Wien). Wien November 2004. 

Robert Schwarz/Michael Jeckle: Gemeinsame Ausfallswahrscheinlichkeiten von österreichischen Klein- und Mittelunternehmen. Studie in Kooperation mit dem „Österreichischen Kreditschutzverband von 1870“. Wien November 2004. 

Wirtschaft und Management · Jahrgang 3 · Nr. 5 · November 2006 

149 

Fachhochschule des bfi Wien Gesellschaft m.b.H. A-1020 Wien, Wohlmutstraße 22 Tel.:  +43/1/720 12 86 Fax:  +43/1/720 12 86-19 E-Mail: info@fh-vie.ac.at www.fh-vie.ac.at 

**==> picture [125 x 66] intentionally omitted <==**

Eine Gesellschaft des 

F A C H H O C H S C H U L E BD E S F I W I E N 

