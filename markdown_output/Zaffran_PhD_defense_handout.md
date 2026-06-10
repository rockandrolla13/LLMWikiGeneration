## **Post-hoc predictive uncertainty quantification: methods with applications to electricity price forecasting** 

Margaux Zaffran — June 25, 2024 — Ph.D. defense 

Jury members Ph.D. advisors Reviewers Examiners Aymeric Dieuleveut Pierre Pinson Emmanuel Cand`es Julie Josse ´Etienne Roquain Florence Forbes Olivier F´eron ´Eric Moulines Yannig Goude Aaditya Ramdas 

## **Forecasting French spot electricity prices** 

## Hourly day-ahead market prices (between producers and suppliers) 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0002-02.png)


**----- Start of picture text -----**<br>
3000<br>2500<br>2000<br>1500<br>1000 2 017 − 01 2017 − 07 2018 − 01 2018 − 07 2019 − 01 2019 − 07 2020 − 01 2020 − 07 2021 − 01<br>Date<br>500<br>0<br>2016 2017 2018 2019 2020 2021 2022 2023 2024<br>Date<br>/MWh)<br>€(<br>price<br>Spot<br>**----- End of picture text -----**<br>


_To which extent are they forecastable?_ 

_�→_ forecasts errors **no lower than 10%** of the realized price! 

1 / 37 

**Forecasting French electricity spot prices with confidence** 

**goal** 

## New goal: 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0003-03.png)


**----- Start of picture text -----**<br>
Observed price<br>125 Predicted price<br>Predicted interval<br>100<br>75<br>50<br>2019-01-212019-01-222019-01-232019-01-242019-01-252019-01-26<br>/MWh)<br>(€<br>price<br>Spot<br>**----- End of picture text -----**<br>


Quantify predictive uncertainty with: 

- **Theoretically grounded tools** 

- **Light assumptions on the underlying data distribution** 

- **Guarantees agnostic to the prediction algorithm** 

   - ⇝ Post-hoc approach (i.e. no modification of the existing operational pipeline) 

2 / 37 

**challenges** 

## **Forecasting French electricity spot prices with confidence** 

## **Time series** 

_▷_ Temporal structure (trend, seasonality, dependence, etc.) 

_▷_ Non-stationarity 

**Missing values** Improve forecasts by leveraging the _emergence of open data platforms_ (ENTSO-E Transparency, Eco2Mix, etc.) 

- Missing covariates by aggregating different data sources 

3 / 37 

## **Approach: black-box post-processing of existing probabilistic forecasts** 

Important literature on intervals forecast, emerging from the electrical application (Hong et al., 2016; Hong and Fan, 2016), but also from renewable energies and meteorology (Wan et al., 2014; Wang et al., 2017). 

- Wide range of models, mainly based on the _pinball loss_ , such as 

   - Quantile Random Forests, 

   - Quantile Generalized Additive Models, 

   - Quantile Regression Averaging, 

   - intervals from Gaussian Auto-Regressive models with exogenous variables, 

   - Deep Learning Probabilistic, 

etc. ⇝ in practice uncalibrated. 

**Black-box post-processing of available probabilistic forecasts** 

▶ Post-hoc approach: plug-in on top of any of these models 

- Guarantees: in finite sample and distribution-free 

4 / 37 

## **Quantifying predictive uncertainty** 

• ( _X , Y_ ) _∈_ R _[d] ×_ R random variables • _n_ training samples � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0006-02.png)


and _Cα_ should be as small as possible, in order to be informative[1] . 

▶ Construction of the predictive intervals should be 

   - agnostic to the model[2] 

   - agnostic to the data distribution 

   - valid in finite samples 

- 1Analogous to Gneiting et al. (2007). 

- 2The underlying model can be any probabilistic model tailored for the application task at hand. 

5 / 37 

**Conformalized Quantile Regression (CQR)**[3] 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0007-01.png)


**----- Start of picture text -----**<br>
Train Cal Test<br>2<br>0<br>− 2<br>− 4<br>0 1 2 3 4 5<br>X<br>Y<br>**----- End of picture text -----**<br>


> 3Romano et al. (2019), _Conformalized Quantile Regression_ , NeurIPS 

6 / 37 

**Conformalized Quantile Regression (CQR)**[3] 

**training step** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0008-02.png)


**----- Start of picture text -----**<br>
2<br>0<br>− 2<br>− 4<br>0 2 4<br>X<br>Y<br>**----- End of picture text -----**<br>



![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0008-03.png)


**----- Start of picture text -----**<br>
▶ Learn (or get) QR [�] lower and<br>�<br>QRupper<br>**----- End of picture text -----**<br>


> 3Romano et al. (2019), _Conformalized Quantile Regression_ , NeurIPS 

6 / 37 

**calibration step** 

## **Conformalized Quantile Regression (CQR)**[3] 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0009-02.png)


**----- Start of picture text -----**<br>
+ + + + + +<br>+ + ▶ Predict with QR [[�]] lower and<br>�<br>QRupperupper<br>▶ Get the scores<br>- - S = � S [[(]] [[k]] [[)][�]][[�]] Cal [[∪{]] [[+]] [[∞}]]<br>-<br>- - +<br>- ▶ Compute the (1  − α )<br>+<br>quantile of S , noted q 1 −α<br>�<br>�→ S [(] [k] [)] := max QRlower X [(] [k] [)][�] − Y [(] [k] [)] , Y [(] [k] [)] − QR [�] upper X [(] [k] [)][��]<br>� � �<br>**----- End of picture text -----**<br>


▶ Predict with QR[[�]] lower and � QRupperupper ▶ Get the scores _S_ = � _S_[[(]] _[[k]]_[[)][�]][[�]] Cal _[[∪{]]_[[+]] _[[∞}]]_ ▶ Compute the (1 _− α_ ) empirical quantile of _S_ , noted _q_ 1 _−α_ ( _S_ ) 

- 3Romano et al. (2019), _Conformalized Quantile Regression_ , NeurIPS 

6 / 37 

**prediction step** 

## **Conformalized Quantile Regression (CQR)**[3] 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0010-02.png)


**----- Start of picture text -----**<br>
2<br>0<br>▶ Predict with QR [�] lower and<br>�<br>− 2 QRupper<br>− 4<br>0 2 4<br>X<br>▶ Build<br>�<br>Cα ( x ) = [QR � lower( x )  − q 1 −α  ( S ); QR [�] upper( x ) +  q 1 −α  ( S )]<br>Y<br>**----- End of picture text -----**<br>


> 3Romano et al. (2019), _Conformalized Quantile Regression_ , NeurIPS 

6 / 37 

## **CQR theoretical foundation** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0011-01.png)


**----- Start of picture text -----**<br>
Exchangeability<br>� X [(] [k] [)] , Y [(] [k] [)][�] [n] k =1 [are][ exchangeable][ if for any permutation] [ σ] [of][ �][1] [,][ n] [�] [we have:]<br>X [(1)] , Y [(1)][�] , . . . , X [(] [n] [)] , Y [(] [n] [)][�] = [d] X [(] [σ] [(1))] , Y [(] [σ] [(1))][�] , . . . , X [(] [σ] [(] [n] [))] , Y [(] [σ] [(] [n] [))][�] .<br>� � � �<br>**----- End of picture text -----**<br>



![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0011-02.png)


**----- Start of picture text -----**<br>
�→ i.i.d. ⇒ exchangeability<br>**----- End of picture text -----**<br>


7 / 37 

## **CQR theoretical guarantees** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0012-01.png)


**----- Start of picture text -----**<br>
CQR marginal validity (Romano et al., 2019)<br>Suppose � X [(] [k] [)] , Y [(] [k] [)][�] [n] k [+1] =1 [are] [exchangeable] [(or] [i.i.d.)] [a] [.]<br>CQR applied on � X [(] [k] [)] , Y [(] [k] [)][�] [n] k =1 [outputs] [C] [�] [α] [ (] [·] [)] [such] [that:]<br>P Y [(] [n] [+1)] ∈ C [�] α X [(] [n] [+1)][��] ≥ 1  − α.<br>� �<br>a Only the calibration and test data need to be exchangeable.<br>**----- End of picture text -----**<br>


Marginal coverage: P _Y_[(] _[n]_[+1)] _∈ C_[�] _α_ � _X_[(] _[n]_[+1)][�] _|X_[(] _[n]_[+1)] = _x ≥_ 1 _− α_ . � � 

8 / 37 

## **Definition of distribution-free features conditional validity** 

- 

- _Cα_ = estimated predictive set based on _n_ data points. 

## **Distribution-free** _X_ **-conditional validity** 

- 

- _Cα_ achieves distribution-free _X_ -conditional validity if: 

   - for any distribution _D_ , 

   - for any associated exchangeable joint distribution _D_[exch][(] _[n]_[+1)] , 

- we have that: 

P _D_ exch( _n_ +1) _Y_[(] _[n]_[+1)] _∈ C_[�] _α X_[(] _[n]_[+1)][�] _|X_[(] _[n]_[+1)][�] _[a] ≥[.][s][.]_ 1 _− α._ � � 

9 / 37 

## **Informative conditional coverage as such is impossible** 

## **Impossibility results (Vovk, 2012; Lei and Wasserman, 2014)** 

If _C_[�] _α_ is distribution-free _X_ -conditionally valid, then, for any _D_ , for _DX_ –almost all _DX_ –non-atoms _x ∈X_ , it holds: 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0014-03.png)


- Approximate conditional coverage 

_�→_ Romano et al. (2020); Guan (2022); Jung et al. (2023); Gibbs et al. (2023) Target P( _Y_[(] _[n]_[+1)] _∈ C_[�] _α_ � _X_[(] _[n]_[+1)][�] _|X_[(] _[n]_[+1)] _∈R_ ( _x_ )) _≥_ 1 _− α_ 

- Asymptotic (with the sample size) conditional coverage 

_�→_ **Romano et al. (2019)** ; Kivaranovic et al. (2020); Chernozhukov et al. (2021); Sesia and Romano (2021); Izbicki et al. (2022) 

Non exhaustive references. 

10 / 37 

## **Contributions and outline** 

## **Part I: time series** 

- Adaptive Conformal Predictions for Time Series. In _ICML_ . 

(Z., F´eron, Goude, Josse, and Dieuleveut, 2022) 

_▷_ Adaptive Probabilistic Forecasting of French Electricity Spot Prices. Submitted to _Applied Energy_ . (Dutot _[∗]_ , Z. _[∗]_ , F´eron, and Goude, 2024) 

**Part II: missing values** 

- Conformal Prediction with Missing Values. In _ICML_ . 

(Z., Dieuleveut, Josse, and Romano, 2023) 

_▷_ Predictive Uncertainty Quantification with Missing Covariates. Submitted to _Journal of Machine Learning Research_ . (Z., Josse, Romano, and Dieuleveut, 2024) 

11 / 37 

Introduction 

Time series 

Theoretical analysis of ACI’s length `AgACI` Numerical experiments Simulated data and French electricity price forecasting 

Missing values Conclusion and perspectives 

## **Online framework** 

- Data: _T_ 0 random variables ( _X_[(1)] _, Y_[(1)] ) _, . . . ,_ ( _X_[(] _[T]_[0][)] _, Y_[(] _[T]_[0][)] ) in R _[d] ×_ R 

• Aim: predict the response values as well as predictive intervals for _T_ 1 subsequent observations _X_[(] _[T]_[0][+1)] _, . . . , X_[(] _[T]_[0][+] _[T]_[1][)] **sequentially** : at any prediction step _t ∈_ � _T_ 0 + 1 _, T_ 0 + _T_ 1�, _Y_[(] _[t][−][T]_[0][)] _, . . . , Y_[(] _[t][−]_[1)] have been revealed 

- Build the smallest interval _C_[�] _α[t]_[such][that:] 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0017-04.png)


often relaxed in: 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0017-06.png)


12 / 37 

## **Extensions of CP to forecasting time series (as of 2021)** 

- Theory (Chernozhukov et al., 2018) 

- Applications (Wisniewski et al., 2020; Kath and Ziel, 2021) 

- Gibbs and Cand`es (2021) 

13 / 37 

**Extensions of CP to forecasting time series (as of 2021)** 

**ACI** 

- Theory (Chernozhukov et al., 2018) 

- Applications (Wisniewski et al., 2020; Kath and Ziel, 2021) 

- Gibbs and Cand`es (2021) 

Adaptive Conformal Inference (ACI) was initially proposed to handle distribution shift. 

It relies on updating online an _effective miscoverage rate αt_ , with the scheme 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0019-07.png)


and _α_ 1 = _α_ , _γ ≥_ 0. 

**Intuition:** if we did make an error, the interval was too small so we want to increase its length by taking a higher quantile (a smaller _αt_ ). Reversely if we included the point. 

13 / 37 

## **Visualisation of ACI procedure** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0020-01.png)


**----- Start of picture text -----**<br>
1<br>0<br>− 1<br>0 100 200 300 400 500<br>t<br>1<br>0<br>− 1<br>500 550 600 650 700 750 800 850 900 950 1000<br>t<br>εt<br>εt<br>**----- End of picture text -----**<br>


**Figure 1:** Visualisation of ACI with different values of _γ_ ( _γ_ = 0, _γ_ = 0 _._ 01, _γ_ = 0 _._ 05) 

14 / 37 

**ACI asymptotic result** 

Gibbs and Cand`es (2021) provide an asymptotic validity result for any sequence of observations. 

1 _T_ 0+ _T_ 1 2 ������ _T_ 1 _t_ =� _T_ 0+1 1 � _Y_[(] _[t]_[)] _∈ C_[�] _αt_ � _X_[(] _[t]_[)][��] _−_ (1 _− α_ )������ _≤ γT_ 1 

_⇒_ favors large _γ_ . But, the higher _γ_ , the more frequent are the infinite intervals. 

15 / 37 

Introduction 

Time series 

Theoretical analysis of ACI’s length `AgACI` Numerical experiments Simulated data and French electricity price forecasting 

Missing values Conclusion and perspectives 

## **Approach** 

Aim: derive theoretical results on the average length of ACI depending on _γ_ 

- _�→_ guideline for choosing _γ_ 

## Approach: 

- consider extreme cases (useful in an online context) with simple theoretical 

   - distributions 

1. exchangeable 

   2. Auto-Regressive case (AR(1)) 

- assume the calibration is perfect, to rely on Markov Chain Theory 

   - _�→_ the empirical quantiles correspond to the exact scores’ quantile distribution _Q_ 

16 / 37 

## **Theoretical analysis of ACI’s length: exchangeable case** 

## 

- _L_ ( _αt_ ) = 2 _Q_ (1 _− αt_ ) the adaptive algorithm’s interval’s length at time _t_ , 

- _L_ 0 = 2 _Q_ (1 _− α_ ) the non-adaptive algorithm’s interval’s length (i.e. _γ_ = 0). 

**Limit length under exchangeability (Z., F´eron, Goude, Josse, and Dieuleveut, 2022)** 

Assume the scores are exchangeable with quantile function Q perfectly estimated at each time, and other technical assumptions. 

Then, for all _γ >_ 0, ( _αt_ ) _t>_ 0 forms a Markov Chain, that admits a stationary distribution _πγ_ , and 

_T_ 1 _a.s. T_ � _L_ ( _αt_ ) _T−→→_ + _∞_[E] _[π][γ]_[[] _[L]_[]][not.] = E _α_ ˜ _∼πγ_ [ _L_ (˜ _α_ )] _. t_ =1 Moreover, as _γ →_ 0, E _πγ_ [ _L_ ] = _L_ 0 + _Q[′′]_ (1 _− α_ ) _[γ]_ 2 _[α]_[(1] _[ −][α]_[) +] _[ O]_[(] _[γ]_[3] _[/]_[2][)] _[.]_ 

17 / 37 

## **Theoretical and numerical analysis of ACI’s length: AR(1) case** 

**Convergence under AR(1) (Z., F´eron, Goude, Josse, and Dieuleveut, 2022)** ˆ ˆ Assume the residuals follow an AR(1) process: _ε_[(] _[t]_[+1)] = _ϕε_[(] _[t]_[)] + _ξ_[(] _[t]_[+1)] with ( _ξ_[(] _[t]_[)] ) _t_ i.i.d. random variables and other technical assumptions, we have: 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0025-02.png)


**----- Start of picture text -----**<br>
T<br>1 a.s.<br>T � L ( αt ) T−→→ + ∞ [E] [π][γ][,][ϕ] [[] [L] []] [not.] = E α ˜ ∼πγ,ϕ [ L (˜ α )] .<br>t =1<br>0 . 08<br>0 . 06<br>0 . 04<br>0 . 02<br>0 . 00<br>0.0 0.6 0.85 0.95 0.98 0.99 0.997 0.999<br>ϕ<br>∗γ<br>**----- End of picture text -----**<br>


**Figure 2:** _γ[∗]_ minimizing the average length for each _ϕ_ . 

18 / 37 

Introduction 

Time series 

Theoretical analysis of ACI’s length `AgACI` Numerical experiments Simulated data and French electricity price forecasting 

Missing values Conclusion and perspectives 

## `AgACI` **: adaptive wrapper around ACI** 

Online aggregation under expert advice (Cesa-Bianchi and Lugosi, 2006) computes an optimal weighted mean of experts. `AgACI` performs 2 independent aggregations: one for each bound (the upper and lower ones), based on the corresponding pinball losses. 

19 / 37 

## `AgACI` **: adaptive wrapper around ACI, scheme (upper bound)** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0028-01.png)


**----- Start of picture text -----**<br>
Experts Previous upper Weights Weighted Forecasts Experts<br>bounds mean at t + 1<br>aA ae ° (<\—<br>eeAci a<br>. . . . .<br>. . . . .<br>. To+1 . t i] . t+] . .<br>i [ -<br>¥ NL<br>. . . . .<br>. . . . .<br>. . . . .<br>To+1 t | t+1<br>2 fe<br>Py; N\ a y<br>**----- End of picture text -----**<br>


20 / 37 

Introduction 

Time series Theoretical analysis of ACI’s length `AgACI` 

Numerical experiments Simulated data and French electricity price forecasting 

Missing values Conclusion and perspectives 

## **Experimental take-away messages** 

• **Synthetic data with ARMA noise** (Z., F´eron, Goude, Josse, and Dieuleveut, 2022) _◦_ Benchmarks are not robust to the increase in the temporal dependence; 

_◦_ ACI is robust, maintaining validity, with an appropriate _γ_ ; _◦_ `AgACI` is robust, maintaining validity, not the smallest. 

- **French electricity spot prices** 

   - 2019: `AgACI` provides validity with a reasonable efficiency; 

(Z., F´eron, Goude, Josse, and Dieuleveut, 2022) 

- 2020 and 2021: `AgACI` fails to ensure validity, and the various forecasting models considered behave differently. (Dutot _[∗]_ , Z. _[∗]_ , F´eron, and Goude, 2024) 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0030-07.png)


**----- Start of picture text -----**<br>
800<br>600<br>400<br>200<br>0<br>2016 2017 2018 2019 2020 2021 2022<br>Date<br>/MWh)<br>(€<br>price<br>Spot<br>**----- End of picture text -----**<br>


21 / 37 

**Improving adaptiveness for high non-stationarity (Dutot** _[∗]_ **, Z.** _[∗]_ **, F´eron, and Goude, 2024)** 

Online aggregation of various `AgACI` , each of them being trained with different underlying forecasting models, for each bound independently. 

- Retrieves validity even in the most hazardous period of 2020 and 2021. Analyzing its weights provides interpretability. 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0031-03.png)


**----- Start of picture text -----**<br>
QRF (75 %) QGB (75 %) Lasso QR (75 %) Linear QR (75 %) QGAM (75 %)<br>QRF (50 %) QGB (50 %) Lasso QR (50 %) Linear QR (50 %) QGAM (50 %)<br>QRF (25 %) QGB (25 %) Lasso QR (25 %) Linear QR (25 %) QGAM (25 %)<br>1  − α  = 0.6 1  − α  = 0.9 1  − α  = 0.95 1  − α  = 0.98<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02<br>bound<br>Upper<br>bound<br>Lower<br>**----- End of picture text -----**<br>


22 / 37 

**Highlights and perspectives** 

Aggregating the two bounds independently (as in `AgACI` and beyond): 

- Allows more flexible and adaptive behavior in practice, catching the varying nature of the predictive distribution tails 

- Prevents from obtaining theoretical guarantees (by opposition to Gibbs and Cand`es, 2022) 

- _�→_ Weaken the objective and consider a more practical theoretical aim? 

23 / 37 

Introduction 

Time series 

Missing values 

Goals and challenges for predictive uncertainty quantification Is MCV a too lofty goal?! Achieving MCV under _M⊥⊥X_ and _Y ⊥⊥M |X_ 

Conclusion and perspectives 

## **Missing values are ubiquitous and challenging** 

**Data:** � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1 

|_Y_<br>_X_1<br>_X_2<br>_X_3<br>22.42<br>0.55<br>0.67<br>0.03<br>8.26<br>0.72<br>0.18<br>0.55<br>19.41<br>0.60<br>0.58<br>`NA`<br>19.75<br>0.54<br>0.43<br>0.96<br>7.32<br>`NA`<br>0.19<br>`NA`<br>13.55<br>0.65<br>0.69<br>0.50<br>20.75<br>`NA`<br>`NA`<br>0.61<br>9.26<br>0.89<br>`NA`<br>0.84<br>9.68<br>0.963<br>0.45<br>0.65|Mask _M_ =<br>(_M_1<br>_M_2<br>_M_3)|
|---|---|
||0<br>0<br>0<br>0<br>0<br>0<br>0<br>0<br>1<br>0<br>0<br>0<br>1<br>0<br>1<br>0<br>0<br>0<br>1<br>1<br>0<br>0<br>1<br>0<br>0<br>0<br>0|



_�→_ 2 _[d]_ potential masks. _�→ M_ can depend on _X_ or _Y_ . 

_⇒_ Statistical and computational challenges. 

24 / 37 

## **Supervised learning with missing values: impute-then-regress** 

Impute-then-regress procedures are widely used. 

1. Replace `NA` using an imputation function (e.g. the mean), noted _φ_ . 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0035-03.png)


**----- Start of picture text -----**<br>
-1 -10 6 0 -1 -10 6 0<br>4 -2 2 4 -4.5 -2 2<br>5 1 2 5 1 2 1<br>0 1 0 -4.5 1<br>**----- End of picture text -----**<br>



![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0035-04.png)


**----- Start of picture text -----**<br>
2. Train your algorithm (Random Forest, Neural Nets, etc.) on the imputed<br>  n<br>data: � φ � X obs( [(] [k] [)] M �� [(] [k] [)] ) [,][ M] [(] [k] [)][�] � , Y [(] [k] [)]  .<br> U [(] [k] [)] =imputed X [(] [k] [)]  k =1<br>**----- End of picture text -----**<br>


- _�→_ we consider an impute-then-regress pipeline in this work. 

25 / 37 

Introduction 

Time series 

Missing values 

Goals and challenges for predictive uncertainty quantification Is MCV a too lofty goal?! 

Achieving MCV under _M⊥⊥X_ and _Y ⊥⊥M |X_ 

Conclusion and perspectives 

## **Goals of predictive uncertainty quantification with missing values** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0037-01.png)


**----- Start of picture text -----**<br>
Goal: predict Y [(] [n] [+1)] with confidence 1  − α , i.e. build the smallest Cα such that<br>for any D and any associated D [exch][(] [n] [+1)] :<br>Marginal Validity (MV)<br>P D exch( n +1) Y [(] [n] [+1)] ∈Cα X [(] [n] [+1)] , M [(] [n] [+1)][��] ≥ 1  − α. (MV)<br>� �<br>Mask-Conditional-Validity (MCV)<br>P D exch( n +1) Y [(] [n] [+1)] ∈Cα X [(] [n] [+1)] , M [(] [n] [+1)][�] |M [(] [n] [+1)][�] [a] ≥ [.][s][.] 1  − α. (MCV)<br>� �<br>M forms meaningful categories<br>**----- End of picture text -----**<br>


_�→_ Even if _M⊥⊥X_ and _Y ⊥⊥M |X_ (e.g. **equity standpoint** ) 

26 / 37 

**CP is marginally valid** (MV) **after imputation** 

## **Exchangeability after imputation (Z., Dieuleveut, Josse and Romano, 2023)** 

Assume � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[are][i.i.d.][(or][exchangeable).] Then, for any missing mechanism, for almost all imputation function _[a] φ_ : � _φ_ � _X_ obs([(] _[k]_[)] _M_[(] _[k]_[)] ) _[,][ M]_[(] _[k]_[)][�] _, Y_[(] _[k]_[)][�] _[n] k_ =1[are] **[exchangeable]**[.] 

> _a_ Even if the imputation is not accurate, the guarantee will hold. 

_⇒_ CQR, and Conformal Prediction, applied on an imputed data set still enjoys marginal guarantees[4] : 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0038-05.png)


> 4The upper bound also holds under continuously distributed scores. 

27 / 37 

## **CQR is marginally valid on imputed data sets** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0039-01.png)


**----- Start of picture text -----**<br>
Y =  β [T] X +  ε , β = (1 ,  2 , − 1) [T] , X and ε Gaussian.<br>CQR (marginal validity)<br>1 . 0<br>1  − α<br>0 . 8<br>0 . 6<br>Marginal (i.e. average) coverage (MV) is indeed recovered!<br>Mask-conditional-validity (MCV) is not attained<br>�→ Missing values induce heteroskedasticity<br>(supported by theory under (non-)parametric assumptions)<br>Marginalfullyobserved X 1missing , X 2)missing X 2missing , X 3)missing X 3missing , X 3)missing<br>X X 1 X 2 X 1<br>( ( (<br>coverage<br>Average<br>**----- End of picture text -----**<br>


28 / 37 

## **Conformalization step is independent of the important variable: the mask!** 

**Observation:** the _α_ -correction term is computed among all the data points, regardless of their mask! 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0040-02.png)


**----- Start of picture text -----**<br>
2<br>0<br>− 2<br>− 4<br>0 2 4<br>X<br>Y<br>**----- End of picture text -----**<br>


**Warning:** 2 _[d]_ possible masks 

_⇒_ Splitting the calibration set by mask is infeasible (lack of data)! 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0040-05.png)


**----- Start of picture text -----**<br>
Initial calibration set Test point Test point<br>-1 -10 6 1 3 6 0 1 3 1<br>4 -2 2 Calibration set used Calibration set used<br>5 1 1 0 -1 -10 6 1 0 1<br>0 1 5 1 1 0<br>**----- End of picture text -----**<br>


**Question:** for low probability masks (i.e. _DM_ ( _m_ ) := P _D_ ( _M_ = _m_ ) is small), is it possible to learn from the predictive distributions conditional on other masks? 

29 / 37 

Introduction 

Time series 

Missing values 

Goals and challenges for predictive uncertainty quantification Is MCV a too lofty goal?! Achieving MCV under _M⊥⊥X_ and _Y ⊥⊥M |X_ 

Conclusion and perspectives 

## **Fully distribution-free MCV is necessarily uninformative** 

**General MCV hardness result (Z., Josse, Romano and Dieuleveut, 2024)**[5] 

If any _C_[�] _α_ is distribution-free MCV then **for any distribution** _D_ , for any mask _m_ such that _DM_ ( _m_ ) := P _D_ ( _M_ = _m_ ) _>_ 0, it holds: 

� P _D⊗_ ( _n_ +1) �mes � _Cα_ � _X_[(] _[n]_[+1)] _, m_ �[�] = _∞_ � _≥_ 1 _− α −_ ∆ _m,n ≥_ 1 _− α − DM_ ( _m_ ) _[√] n_ + 1 _._ 

Irreducible term: consider _C_[�] _α_ outputting _Y_ with probability 1 _− α_ and _∅_ otherwise. 

∆ _m,n_ term: smaller than _DM_ ( _m_ ) _[√] n_ + 1 

_�→_ gets negligible (making the lower bound nearly 1 _− α_ ) **only** for low probability masks compared to _n_ . 

> 5An analogous statement is also available for the classification framework. 

30 / 37 

## **Restricting the link between** _M_ **and** ( _X_ **or** _Y_ ) **does not allow informative MCV** 

_M ⊥⊥ X_ **hardness result (Z., Josse, Romano and Dieuleveut, 2024)** 

If any _C_[�] _α_ is MCV under _M⊥⊥X_ , then for any distribution _D_ such that _M⊥⊥X_ , for any mask _m_ such that _DM_ ( _m_ ) _>_ 0, it holds: � P _D⊗_ ( _n_ +1) mes _Cα X_[(] _[n]_[+1)] _, m_ = _∞ ≥_ 1 _− α −DM_ ( _m_ ) _√n_ + 1 _._ � � � �� � 

_Y ⊥⊥M |X_ **hardness result (Z., Josse, Romano and Dieuleveut, 2024)** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0043-04.png)


_⇒_ Need to restrict **both** the link between _M_ and _X_ , **as well as** between _M_ and _Y_ . 

Analogous statements are also available for the classification framework. 

31 / 37 

Introduction 

Time series 

Missing values 

Goals and challenges for predictive uncertainty quantification Is MCV a too lofty goal?! Achieving MCV under _M⊥⊥X_ and _Y ⊥⊥M |X_ 

Conclusion and perspectives 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation): three instances** 

|keep same mask|**Overmasked calibration set**<br>-1<br>1<br>0<br>4<br>2<br>1<br>0<br>1<br>-2<br>**Test mask**|**Overmasked calibration set**<br>-1<br>1<br>0<br>4<br>2<br>1<br>0<br>1<br>-2<br>**Test mask**|**Temporary test points**<br>3<br>1<br>2<br>3<br>1<br>2<br>3<br>1<br>2<br>**Test point**<br>3<br>1<br>2|coined `CP-MDA-Exact`|
|---|---|---|---|---|
||||||
|keep arbitrary selection|-1<br>1<br>4<br>2<br>5<br>0<br>1<br>-1<br>1|0<br>1<br>3<br>-2<br>0|3<br>1<br>2<br>3<br>1<br>2<br>3<br>1<br>2<br>3<br>2<br>3<br>1<br>2||
|keep all points|4<br>2<br>5|1<br>3|3<br>1<br>2<br>3<br>2|coined `CP-MDA-Nested`|
||0<br>1|-2|3<br>1<br>2|32 /|




![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0045-02.png)


**----- Start of picture text -----**<br>
Initial calibration set<br>-1 -10 6 1 0<br>4 -2 2 1<br>5 1 1 3 keep arbitrary selection<br>0 1 -2<br>-3 0<br>keep all points<br>**----- End of picture text -----**<br>


32 / 37 

## `CP-MDA-Nested` _[⋆]_ **achieves Mask-Conditional-Validity** (MCV) 

## **Mask-conditional-validity of** `CP-MDA-Nested` _[⋆]_ 

**(Z., Josse, Romano and Dieuleveut, 2024)** 

Under the assumptions that: 

- _M⊥⊥X_ , 

- _Y ⊥⊥M |X_ , 

• � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_[+1] =1[are][i.i.d.,] • the subsampling scheme is independent of � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_[+1] =1[,] then, for almost all imputation function, `CP-MDA-Nested` _[⋆]_ reaches (MCV) at the level 1 _−_ 2 _α_ , that is: P _D⊗_ ( _n_ +1) _Y_[(] _[n]_[+1)] _∈ C_[�] _α X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] _|M_[(] _[n]_[+1)][�] _[a] ≥[.][s][.]_ 1 _−_ 2 _α._ � � 

33 / 37 

## **Experiments on** _M⊥⊥X_ **and** _Y ⊥⊥M |X_ **Gaussian linear data in dimension 10** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0047-01.png)


**----- Start of picture text -----**<br>
CQR-MDA-Nested [⋆] subsampling<br>CQR CQR-MDA-Exact points with at most 2 more  NA s CQR-MDA-Nested<br>10 .. 08 TUT ABARAT<br>0 . 6 “ttt EMemA  TY PUREARALIEI<br>15 Oracle length , é<br>10<br>5 tqgcesserel tt! sheseatte caneeetsa<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


**Figure 4:** 40% of missing values 

- ⇝ `CP-MDA-Exact` outputs many **infinite intervals** on points with less than 6 `NA` s. ⇝ Compared to `CP-MDA-Nested` , `CP-MDA-Nested` _[⋆]_ selecting points with at most 2 more `NA` s **reduces the length** by: 

   - 5.5% marginally; 

   - 10% on fully observed points. 

34 / 37 

## **Experiments beyond independence** 

- Under various _M̸⊥⊥X_ (MAR and MNAR) mechanisms, `CP-MDA-Nested` _[⋆]_ maintains empirical MCV; 

- When _Y ̸⊥⊥M |X_ and the imputation is not accurate enough: 

   - `CP-MDA-Nested` _[⋆]_ fails to empirically ensure MCV, 

   - with a loss of coverage that is more critical when subsampling. 

35 / 37 

Introduction 

Time series Missing values Conclusion and perspectives 

## **Key messages and contributions** 

## **Part I: time series** 

_▷_ Impact of hyper-parameter on the intervals efficiency 

_▷_ Methodologies for online forecasting with post-hoc predictive UQ 

_▷_ Extensive benchmark on time series CP and French elec. spot prices 

**Part II: missing values** 

- Missingness and predictive uncertainty interplay’s characterization 

_▷_ Methodology to achieve MCV 

- Numerical experiments beyond the assumptions 

**Open-sourced** introductive tutorial on CP, _(to be)_ presented at: 

_▷_ MASPIN days 2023, with C. Boyer, 

- ENBIS 2023, 

- UAI 2024, with A. Dieuleveut, 

- ICML 2024, with A. Dieuleveut. 

36 / 37 

**Perspectives** 

Some direct open directions include: 

- Deeper investigation of practical time series CP (data sets, extremes, im- 

- proved model, interpertability, theoretical objective) 

- Is it possible to informatively achieve MCV under Missing At Random and 

- _Y ⊥⊥M |X_ ? 

- Multidimensional predictive uncertainty quantification 

Motivation: forecast multiple (correlated) electricity prices simultaneously 

- (e.g., different countries or market horizons) 

Challenge: capture the multivariate uncertainty 

37 / 37 

## Thank you for your attention! And many thanks to 

Aymeric Dieuleveut Olivier F´eron 

F´eron Yannig Goude " Gr´egoire Dutot Yaniv Romano and many others :) 

Julie Josse 

Claire Boyer 

## **References i** 

Angelopoulos, A. N., Cand`es, E. J., and Tibshirani, R. J. (2023). Conformal pid control for time series prediction. arXiv: 2307.16895. 

Barber, R. F., Cand`es, E. J., Ramdas, A., and Tibshirani, R. J. (2021). Predictive inference with the jackknife+. _The Annals of Statistics_ , 49(1). Barber, R. F., Cand`es, E. J., Ramdas, A., and Tibshirani, R. J. (2022). Conformal prediction beyond exchangeability. To appear in _Annals of Statistics (2023)_ . Bastani, O., Gupta, V., Jung, C., Noarov, G., Ramalingam, R., and Roth, A. (2022). Practical adversarial multivalid conformal prediction. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc. Bhatnagar, A., Wang, H., Xiong, C., and Bai, Y. (2023). Improved online conformal prediction via strongly adaptive online learning. In _Proceedings of the 40th International Conference on Machine Learning_ . PMLR. 

## **References ii** 

Cauchois, M., Gupta, S., Ali, A., and Duchi, J. C. (2020). Robust Validation: Confident Predictions Even When Distributions Shift. arXiv: 2008.04267. Cesa-Bianchi, N. and Lugosi, G. (2006). _Prediction, learning, and games_ . Cambridge University Press. 

Chernozhukov, V., W¨uthrich, K., and Yinchu, Z. (2018). Exact and Robust Conformal Inference Methods for Predictive Machine Learning with Dependent Data. In _Conference On Learning Theory_ . PMLR. Chernozhukov, V., W¨uthrich, K., and Zhu, Y. (2021). Distributional conformal prediction. _Proceedings of the National Academy of Sciences_ , 118(48). Feldman, S., Ringel, L., Bates, S., and Romano, Y. (2023). Achieving risk control in online learning settings. _Transactions on Machine Learning Research (TMLR)_ . 

## **References iii** 

Gibbs, I. and Cand`es, E. (2021). Adaptive conformal inference under distribution shift. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc. 

Gibbs, I. and Cand`es, E. (2022). Conformal inference for online prediction with arbitrary distribution shifts. arXiv: 2208.08401. 

Gibbs, I., Cherian, J. J., and Cand`es, E. J. (2023). Conformal prediction with conditional guarantees. arXiv: 2305.12616. 

Gneiting, T., Balabdaoui, F., and Raftery, A. E. (2007). Probabilistic forecasts, calibration and sharpness. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 69(2):243–268. 

Guan, L. (2022). Localized conformal prediction: a generalized inference framework for conformal prediction. _Biometrika_ , 110(1). 

## **References iv** 

Hong, T. and Fan, S. (2016). Probabilistic electric load forecasting: A tutorial review. _International Journal of Forecasting_ , 32(3):914–938. Hong, T., Pinson, P., Fan, S., Zareipour, H., Troccoli, A., and Hyndman, R. J. (2016). Probabilistic energy forecasting: Global energy forecasting competition 2014 and beyond. _International Journal of Forecasting_ , 32(3):896–913. Izbicki, R., Shimizu, G., and Stern, R. B. (2022). CD-split and HPD-split: Efficient conformal regions in high dimensions. _Journal of Machine Learning Research_ , 23(87). 

Jung, C., Noarov, G., Ramalingam, R., and Roth, A. (2023). Batch multivalid conformal prediction. In _International Conference on Learning Representations_ . Kath, C. and Ziel, F. (2021). Conformal prediction interval estimation and applications to day-ahead and intraday power markets. _International Journal of Forecasting_ . 

## **References v** 

Kivaranovic, D., Johnson, K. D., and Leeb, H. (2020). Adaptive, Distribution-Free Prediction Intervals for Deep Networks. In _International Conference on Artificial Intelligence and Statistics_ . PMLR. 

Lei, J. and Wasserman, L. (2014). Distribution-free prediction bands for non-parametric regression. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 76(1). 

Podkopaev, A. and Ramdas, A. (2021). Distribution-free uncertainty quantification for classification under label shift. In _Proceedings of the Thirty-Seventh Conference on Uncertainty in Artificial Intelligence_ . PMLR. Romano, Y., Barber, R. F., Sabatti, C., and Cand`es, E. (2020). With Malice Toward None: Assessing Uncertainty via Equalized Coverage. _Harvard Data Science Review_ , 2(2). 

## **References vi** 

Romano, Y., Patterson, E., and Cand`es, E. (2019). Conformalized Quantile Regression. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc. 

Sesia, M. and Romano, Y. (2021). Conformal prediction using conditional histograms. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc. 

Tibshirani, R. J., Barber, R. F., Candes, E., and Ramdas, A. (2019). Conformal Prediction Under Covariate Shift. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc. 

Vovk, V. (2012). Conditional Validity of Inductive Conformal Predictors. In _Asian Conference on Machine Learning_ . PMLR. 

## **References vii** 

Wan, C., Xu, Z., Pinson, P., Dong, Z. Y., and Wong, K. P. (2014). Probabilistic forecasting of wind power generation using extreme learning machine. _IEEE Transactions on Power Systems_ , 29(3):1033–1044. Wang, H., Li, G., Wang, G., Peng, J., Jiang, H., and Liu, Y. (2017). Deep learning based ensemble approach for probabilistic wind power forecasting. _Applied Energy_ , 188:56–70. 

Wisniewski, W., Lindsay, D., and Lindsay, S. (2020). Application of conformal prediction interval estimations to market makers’ net positions. Proceedings of Machine Learning Research. PMLR. 

Zaffran, M., F´eron, O., Goude, Y., Josse, J., and Dieuleveut, A. (2022). Adaptive conformal predictions for time series. In _Proceedings of the 39th International Conference on Machine Learning_ . PMLR. 

# **Time Series** 

## Time Series 

Literature on non-exchangeable CP Updating the training and calibration sets Theoretical analysis of ACI’s length Numerical experiments Missing Values 

## **Generalizing beyond exchangeability in theory** 

Two major general theoretical results beyond exchangeability: 

- Chernozhukov et al. (2018) 

_�→_ If the learnt model is accurate and the data noise is strongly mixing, then CP is valid asymptotically 

- Barber et al. (2022) 

   - _�→_ Quantifies the coverage loss depending on the strength of exchangeability violation 

P( _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1)) _≥_ 1 _− α −_[average] by[violation] each calibration[of][exchangeability] point _�→_ proposed algorithm: reweighting (again)! e.g., in a temporal setting, give higher weights to more recent points. 

## **Exchangeability does not hold in many practical applications** 

CP requires exchangeable data points to ensure validity 

Covariate shift, i.e. _LX_ changes but _LY |X_ stays constant _(see e.g., Tibshirani et al., 2019)_ 

Label shift, i.e. _LY_ changes but _LX |Y_ stays constant _(see e.g., Podkopaev and Ramdas, 2021)_ 

- Arbitrary distribution shift _(see e.g., Cauchois et al., 2020)_ 

Possibly many shifts, not only one _(main focus of this presentation)_ 

## **Recent developments** 

- Gibbs and Cand`es (2022) later on also proposes a method not requiring to choose _γ_ 

- Bhatnagar et al. (2023) enjoys **anytime** regret bound, by leveraging tools from the strongly adaptive regret minimization literature 

- Feldman et al. (2023) extends ACI to general risk control 

- Bastani et al. (2022) proposes an algorithm achieving stronger coverage guarantees (conditional on specified overlapping subsets, and threshold calibrated) without hold-out set 

- Angelopoulos et al. (2023) combines CP ideas with control theory ones, to adaptively improve the predictive intervals depending on the errors structure 

Non exhaustive references. 

## Time Series 

Literature on non-exchangeable CP Updating the training and calibration sets Theoretical analysis of ACI’s length Numerical experiments Missing Values 

## **How to adapt to time series?** 

Usual ideas from the time series literature: 

- Consider an online procedure (for each new data, re-train and re-calibrate) 

   - _�→_ update to recent observations (trend impact, period of the seasonality, dependence...) 

- Use a sequential split 

   - _�→_ use only the past so as to correctly estimate the variance of the residuals (using the future leads to optimistic residuals and underestimation of their variance) 

## **Online sequential split conformal prediction (OSSCP)** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0067-01.png)



![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0067-02.png)


**----- Start of picture text -----**<br>
t = 0 t = T0 t = T0 + T1<br>Unused data Proper training set Calibration set Test point<br>Wisniewski et al. (2020); Kath and Ziel (2021); Zaffran et al. (2022)<br>**----- End of picture text -----**<br>


_�→_ tested on real time series 

Time Series 

Literature on non-exchangeable CP Updating the training and calibration sets Theoretical analysis of ACI’s length Numerical experiments Missing Values 

## **Numerical analysis of ACI’s length: AR(1) case** 

ˆ ˆ Assume the residuals follow an AR(1) process: _εt_ +1 = _ϕεt_ + _ξt_ +1 with ( _ξt_ ) _t_ i.i.d. random variables and other assumptions, we have: 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0069-02.png)


**----- Start of picture text -----**<br>
T<br>T 1 � L ( αt ) T−→→a. + s.∞ [E] [π][γ][,][ϕ] [[] [L] []] [.]<br>t =1<br>ϕ  =0 ϕ  =0.85 ϕ  =0.98 ϕ  =0.997<br>ϕ  =0.6 ϕ  =0.95 ϕ  =0.99 ϕ  =0.999<br>Thm. 3.1 0 . 08<br>4<br>0.01 0.03 0 . 06<br>3 0 . 04<br>0 . 02<br>2<br>0 . 00<br>0 . 00 0 . 05 0 . 10 0 . 15 0 . 20 0.0 0.6 0.85 0.95 0.98 0.99 0.997 0.999<br>γ ϕ<br>Averagelength ∗γ<br>**----- End of picture text -----**<br>


**Figure 5:** Left: evolution of the mean length depending on _γ_ for various _ϕ_ . Right: _γ[∗]_ minimizing the average length for each _ϕ_ . 

Time Series 

Literature on non-exchangeable CP Updating the training and calibration sets Theoretical analysis of ACI’s length Numerical experiments Missing Values 

## Time Series 

Literature on non-exchangeable CP Updating the training and calibration sets Theoretical analysis of ACI’s length Numerical experiments Synthetic data Forecasting French electricity prices 

Missing Values 

## **Data generation and simulation settings** 

_Yt_ = 10 sin ( _πXt,_ 1 _Xt,_ 2) + 20 ( _Xt,_ 3 _−_ 0 _._ 5)[2] + 10 _Xt,_ 4 + 5 _Xt,_ 5 + _εt_ where the _Xt,· ∼U_ ([0 _,_ 1]) and _εt_ is an ARMA(1,1) process: _εt_ +1 = _ϕεt_ + _ξt_ +1 + _θξt,_ with _ξt_ is a white noise of variance _σ_[2] . 

• _ϕ_ = _θ_ range in [0 _._ 1 _,_ 0 _._ 8 _,_ 0 _._ 9 _,_ 0 _._ 95 _,_ 0 _._ 99]. 

- We fix _σ_ to keep the variance Var( _εt_ ) constant to 10 (or 1). 

- • We use random forest as regressor. 

- For each setting (pair variance and _ϕ_ , _θ_ ): 

_◦_ 300 points, the last 100 kept for prediction and evaluation, _◦_ 500 repetitions, 

- _⇒_ in total, 100 _×_ 500 = 50000 predictions are evaluated. 

**Visualisation of the results** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0073-01.png)


**----- Start of picture text -----**<br>
Coverage<br>~ validity<br>Length<br>~ efficiency<br>**----- End of picture text -----**<br>


## **Results: impact of the temporal dependence, ARMA(1,1), variance 10** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0074-01.png)


**----- Start of picture text -----**<br>
OSSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 01<br>Offline SSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 05<br>EnbPI (Xu & Xie, 2021) AgACI<br>EnbPI V2<br>14<br>ϕ  =  θ =0.1<br>13 ϕ  =  θ =0.8<br>ϕ  =  θ =0.9<br>ϕ  =  θ =0.95<br>12 0 . 895 0 . 900 0 . 905 ϕ  =  θ =0.99<br>11<br>10<br>0 . 83 0 . 84 0 . 85 0 . 86 0 . 87 0 . 88 0 . 89 0 . 90 0 . 91<br>Coverage<br>length<br>median<br>Average<br>**----- End of picture text -----**<br>


## **Summary** 

1. The temporal dependence impacts the _validity_ . 

2. Online is significantly better than offline. 

3. **OSSCP.** Achieves _valid_ coverage for _ϕ_ and _θ_ smaller than 0.9, but is not robust to the increasing dependence. 

4. **EnbPI.** Its _validity_ strongly depends on the data distribution. When the method is _valid_ , it produces the smallest intervals. EnbPI V2 method should be preferred. 

5. **ACI.** Achieves _valid_ coverage for every simulation settings with a well chosen _γ_ , or for dependence such that _ϕ <_ 0 _._ 95. It is robust to the strength of the dependence. 

6. **AgACI.** Achieves _valid_ coverage for every simulation settings, with good _efficiency_ . 

## **Empirical evaluation of ACI sensitivity to** _γ_ **and adaptive choice** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0076-01.png)


**----- Start of picture text -----**<br>
ϕ  =  θ =0.1 ϕ  =  θ =0.8<br>16<br>AgACI<br>15 Naive method<br>14<br>0 . 0700<br>13<br>0 . 0400<br>12 0 . 0100<br>Coverage Coverage<br>ϕ  =  θ =0.95 ϕ  =  θ =0.99 0 . 0070<br>16<br>0 . 0040<br>15 0 . 0010<br>14 0 . 0007<br>0 . 0004<br>13<br>0 . 0001<br>12<br>0 . 0000<br>0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90<br>Coverage Coverage<br>imputation imputation<br>after after<br>length, length,<br>Average Average<br>γ<br>imputation imputation<br>after after<br>length, length,<br>Average Average<br>**----- End of picture text -----**<br>


_⇒_ The more the dependence, the more sensitive to _γ_ is ACI. Naive method (▽): smallest among valid ones in the past _⇒_ accumulates error of the different ACI’s versions. ⋆ results. 

## **Empirical evaluation of ACI sensitivity to** _γ_ **and adaptive choice, AR(1)** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0077-01.png)


**----- Start of picture text -----**<br>
ϕ  =0.1 , θ = 0 ϕ  =0.8 , θ = 0 ϕ  =0.9 , θ = 0 ϕ  =0.95 , θ = 0 ϕ  =0.99 , θ = 0<br>14 AgACI<br>Naive method<br>13<br>0 . 0700<br>0 . 0400<br>12<br>0 . 0100<br>0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90<br>Coverage Coverage Coverage Coverage Coverage 0 . 0070<br>16 0 . 0040<br>15 0 . 0010<br>14 0 . 0007<br>0 . 0004<br>13<br>0 . 0001<br>12<br>0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 0000<br>Coverage Coverage Coverage Coverage Coverage<br>length<br>median<br>Average<br>γ<br>imputation<br>after<br>length,<br>Average<br>**----- End of picture text -----**<br>


## **Empirical evaluation of ACI sensitivity to** _γ_ **and adaptive choice, MA(1)** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0078-01.png)


**----- Start of picture text -----**<br>
ϕ  = 0 , θ =0.1 ϕ  = 0 , θ =0.8 ϕ  = 0 , θ =0.9 ϕ  = 0 , θ =0.95 ϕ  = 0 , θ =0.99<br>AgACI<br>Naive method<br>13 . 8<br>0 . 0700<br>13 . 6<br>0 . 0400<br>0 . 0100<br>0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000<br>Coverage Coverage Coverage Coverage Coverage 0 . 0070<br>0 . 0040<br>15 0 . 0010<br>0 . 0007<br>0 . 0004<br>14<br>0 . 0001<br>0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 0000<br>Coverage Coverage Coverage Coverage Coverage<br>length<br>median<br>Average<br>γ<br>imputation<br>after<br>length,<br>Average<br>**----- End of picture text -----**<br>


## **Results: impact of the temporal dependence, ARMA(1), variance 10, average length after imputation** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0079-01.png)


**----- Start of picture text -----**<br>
OSSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 01<br>Offline SSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 05<br>EnbPI (Xu & Xie, 2021) AgACI<br>EnbPI V2<br>15<br>ϕ  =  θ =0.1<br>14 ϕ  =  θ =0.8<br>ϕ  =  θ =0.9<br>13 ϕ  =  θ =0.95<br>ϕ  =  θ =0.99<br>12 0 . 895 0 . 900 0 . 905<br>11<br>10<br>0 . 83 0 . 84 0 . 85 0 . 86 0 . 87 0 . 88 0 . 89 0 . 90 0 . 91<br>Coverage<br>imputation<br>after<br>length,<br>Average<br>**----- End of picture text -----**<br>


## **Results: impact of the temporal dependence, AR(1) and MA(1), variance 10** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0080-01.png)


**----- Start of picture text -----**<br>
OSSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 01<br>Offline SSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 05<br>EnbPI (Xu & Xie, 2021) AgACI<br>EnbPI V2<br>AR(1) noise MA(1) noise<br>14<br>13 . 8 ϕ  =  θ =0.1<br>13 ϕ  =  θ =0.8<br>ϕ  =  θ =0.9<br>12 0 . 895 0 . 900 0 . 905 13 . 6 ϕϕ  = =  θ θ =0.95=0.99<br>13 . 4<br>11<br>13 . 2<br>10<br>0 . 84 0 . 86 0 . 88 0 . 90 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 9025 0 . 9050 0 . 9075<br>Coverage Coverage<br>length length<br>median median<br>Average Average<br>**----- End of picture text -----**<br>


## **Results: impact of the temporal dependence, AR(1) and MA(1), variance 10, average length after imputation** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0081-01.png)


**----- Start of picture text -----**<br>
OSSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 01<br>Offline SSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 05<br>EnbPI (Xu & Xie, 2021) AgACI<br>EnbPI V2<br>AR(1) noise MA(1) noise<br>15 14 . 4<br>14 . 2 ϕ  =  θ =0.1<br>14<br>ϕ  =  θ =0.8<br>14 . 0<br>13 ϕ  =  θ =0.9<br>13 . 8 ϕ  =  θ =0.95<br>12 0 . 895 0 . 900 0 . 905 13 . 6 ϕ  =  θ =0.99<br>11 13 . 4<br>13 . 2<br>10<br>0 . 84 0 . 86 0 . 88 0 . 90 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 9025 0 . 9050 0 . 9075<br>Coverage Coverage<br>imputation imputation<br>after after<br>length, length,<br>Average Average<br>**----- End of picture text -----**<br>


## Time Series 

Literature on non-exchangeable CP Updating the training and calibration sets Theoretical analysis of ACI’s length Numerical experiments Synthetic data Forecasting French electricity prices 

Missing Values 

## **Forecasting electricity prices with confidence in 2019** 

- Forecast for the year 2019. 

- Random forest regressor. 

- One model per hour, we concatenate the predictions afterwards. 

- _�→_ 24 models 

   - _yt ∈_ R 

   - _xt ∈_ R _[d]_ , with _d_ = 24 + 24 + 1 + 7 = 56 

   - 3 years for training/calibration, i.e. _T_ 0 = 1096 observations 

   - 1 year to forecast, i.e. _T_ 1 = 365 observations 

## **Performance on predicted French electricity Spot price for the year 2019** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0084-01.png)


**----- Start of picture text -----**<br>
OSSCP ACI γ = 0 ACI γ = 0 . 05<br>Offline SSCP ACI γ = 0 . 01 AgACI<br>EnbPI V2<br>26<br>25<br>24<br>23<br>22<br>21<br>0 . 900 0 . 905 0 . 910 0 . 915 0 . 920 0 . 925 0 . 930 0 . 935<br>Coverage<br>length<br>Median<br>**----- End of picture text -----**<br>


## **Forecasting electricity prices with confidence in 2020 and 2021, various models** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0085-01.png)


**----- Start of picture text -----**<br>
QRF QGB Linear QR Lasso QR QGAM<br>Before 2021-09-01<br>1 . 0<br>y =  x 400<br>0 . 9<br>300<br>0 . 8<br>0 . 7 200<br>0 . 6<br>100<br>0 . 5<br>0 . 4 0<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>After 2021-09-01<br>1 . 0<br>y =  x 400<br>0 . 9<br>300<br>0 . 8<br>0 . 7 200<br>0 . 6<br>100<br>0 . 5<br>0 . 4 0<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>Target coverage Target coverage<br>coverage width<br>Empirical Interval<br>coverage width<br>Empirical Interval<br>**----- End of picture text -----**<br>


## **Forecasting electricity prices with confidence in 2020 and 2021, linear models** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0086-01.png)


**----- Start of picture text -----**<br>
QR OSSCQR OSSCQR-horizon AgACI on OSSCQR-horizon<br>Before 2021-09-01<br>1 . 0<br>y =  x<br>0 . 9 150<br>0 . 8<br>100<br>0 . 7<br>0 . 6 50<br>0 . 5<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>After 2021-09-01<br>1 . 0<br>y =  x<br>0 . 9 150<br>0 . 8<br>100<br>0 . 7<br>0 . 6 50<br>0 . 5<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>Target coverage Target coverage<br>coverage width<br>Empirical Interval<br>coverage width<br>Empirical Interval<br>**----- End of picture text -----**<br>


`OSSCP-horizon` eee 

Unused data Proper training set Calibration set Test point 

(a) OSSCP 

(b) OSSCP-horizon 

## **Forecasting electricity prices with confidence in 2020 and 2021, QRF models** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0088-01.png)


**----- Start of picture text -----**<br>
QR OSSCQR OSSCQR-horizon AgACI on OSSCQR-horizon<br>Before 2021-09-01<br>1 . 0 y =  x 300<br>0 . 8 250<br>0 . 6 200<br>150<br>0 . 4<br>100<br>0 . 2<br>50<br>0 . 0<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>After 2021-09-01<br>1 . 0 y =  x 300<br>0 . 8 250<br>0 . 6 200<br>150<br>0 . 4<br>100<br>0 . 2<br>50<br>0 . 0<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>Target coverage Target coverage<br>coverage width<br>Empirical Interval<br>coverage width<br>Empirical Interval<br>**----- End of picture text -----**<br>


## **Forecasting electricity prices with confidence in 2020 and 2021, online aggregation models** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0089-01.png)


**----- Start of picture text -----**<br>
BOA on Individual forecasts BOA on Conformalized forecasts BOA on AgACI forecasts BOA on All Uniform average<br>Before 2021-09-01<br>1 . 00 y =  x 250<br>0 . 95 200<br>0 . 90<br>150<br>0 . 85<br>100<br>0 . 80<br>0 . 75 50<br>0 . 70<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>After 2021-09-01<br>1 . 00 y =  x 250<br>0 . 95 200<br>0 . 90<br>150<br>0 . 85<br>100<br>0 . 80<br>0 . 75 50<br>0 . 70<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>Target coverage Target coverage<br>coverage width<br>Empirical Interval<br>coverage width<br>Empirical Interval<br>**----- End of picture text -----**<br>


# **Missing Values** 

Time Series 

Missing Values 

Missing values and predictive uncertainty interplay `CP-MDA-Nested` _[⋆]_ Numerical experiments Towards asymptotic individualized coverage 

## **Missing values induce heteroskedasticity** 

## **Gaussian linear model** 

- _Y_ = _β[T] X_ + _ε_ , _ε ∼N_ (0 _, σε_[2][)] _[ ⊥⊥]_[(] _[X][,][ M]_[),] _[β][∈]_[R] _[d]_[.] 

- for all _m ∈{_ 0 _,_ 1 _}[d]_ , there exist _µ[m]_ and Σ _[m]_ such that 

_X |_ ( _M_ = _m_ ) _∼N_ ( _µ[m] ,_ Σ _[m]_ ) _._ 

- _�→_ **oracle** intervals: smallest predictive interval when the distribution of _Y |_ ( _X , M_ ) is known 

**Oracle int. under Gaussian lin. mod. (Z., Dieuleveut, Josse, and Romano, 2023)** _L[∗] α_[(] _[m]_[) = 2] _[ ×][ q]_ 1 _[N] −_[(0] _α/[,]_[1)] 2 _[×]_ ~~�~~ _β_ mis _[T]_ ( _m_ )[Σ] mis _[m] |_ obs _[β]_[mis][(] _[m]_[)][ +] _[ σ][ε]_[2] _[.]_ 

- Even with an homoskedastic noise, missingness generates heteroskedasticity 

- **The uncertainty increases when missing values are associated with** 

**larger regression coefficients (i.e. the most predictive variables)** 

## **Properties of isotonic predictive uncertainty** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0093-01.png)


_a.s._ IQ _β,γ_ ( _X_ obs( _m_ ) _, m_ ) _≤_ IQ _β,γ_ ( _X_ obs( _m′_ ) _, m[′]_ ) for any _m ⊂ m[′] ,_ (IQ-1) E �IQ _β,γ_ ( _X_ obs( _M_ ) _, M_ ) _|M_ = _m_ � _≤_ E �IQ _β,γ_ ( _X_ obs( _M_ ) _, M_ ) _|M_ = _m[′]_[�] for any _m ⊂ m[′] ._ (IQ-2) _a.s._ Λ( _Cα_ ( _X_ obs( _m_ ) _, m_ )) _≤_ Λ( _Cα_ ( _X_ obs( _m′_ ) _, m[′]_ )) for any _m ⊂ m[′] ,_ (Len-1) E �Λ( _Cα_ ( _X_ obs( _M_ ) _, M_ )) _|M_ = _m_ � _≤_ E �Λ( _Cα_ ( _X_ obs( _M_ ) _, M_ )) _|M_ = _m[′]_[�] for any _m ⊂ m[′] ._ (Len-2) 

## **Results** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0094-01.png)


**----- Start of picture text -----**<br>
Setup<br>GLM homoske. GLM heteroske. M⊥⊥X and Y ⊥⊥M |X<br>Property<br>Variance Var-1 Var-1 Var-2 Var-2<br>Inter-quantile IQ-1 IQ-2<br>Length of Oracle PI Len-1 Len-2 Len-2<br>**----- End of picture text -----**<br>


**Univariate heteroskedastic Gaussian linear model** 

## **Unidimensional heteroskedasticity** 

Consider the following one-dimensional model: 

- _X ∼N_ (0 _, σ_[2] ), _σ ∈_ R+; 

- _ξ ∼N_ (0 _, τ_[2] ), _τ ∈_ R+, such that _ξ ⊥⊥ X_ ; 

- _Y_ = _βX_ + _X ξ_ , with _β ∈_ R; 

- _M ∼B_ ( _ρ_ ), with _ρ ∈_ [0 _,_ 1], and _M ⊥⊥_ ( _X , Y_ ). 

Time Series 

Missing Values Missing values and predictive uncertainty interplay `CP-MDA-Nested` _[⋆]_ Numerical experiments Towards asymptotic individualized coverage 

`CP-MDA-Nested` _[⋆]_ 

**Input:** _i)_ Training set �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][��] _[n] k_ =1[.] _[ii)]_[imputation][algorithm] _[I]_[.] _[iii)]_ learning algorithm _A_ taking its values in _F_ := _Y[X×M]_ . _iv)_ calibration proportion _ρ ∈_ ]0 _,_ 1]. _v)_ Tr _,_ Cal _,_ Φ _, A_[ˆ] the output of the splitting algorithm 1 ran on � � ��� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][��] _[n] k_ =1 _[,][ I][,][ A][, ρ]_ �. _vi)_ conformity score function _s_ ( _·, ·_ ; _f_ ) for _f ∈F_ . _vii)_ significance level _α_ . _viii)_ test point � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] . _ix)_ subsampled set of calibration indices Cal[�] _⊆_ Cal **for** _k ∈_ Cal[�] : _M_[�][(] _[k]_[)] = max( _M_[(] _[k]_[)] _, M_[(] _[n]_[+1)] ) _C_ � _α_[MDA-Nested] _[⋆] X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] := _y ∈Y_ : (1 _− α_ )(1 + #Cal[�] ) _>_ � � � 1� _s_ �� _X_[(] _[k]_[)] _, M_[�][(] _[k]_[)][�] _, Y_[(] _[k]_[)] ; _A_[ˆ] (Φ ( _·, ·_ ) _, ·_ )� _< s_ �� _X_[(] _[n]_[+1)] _, M_[�][(] _[k]_[)][�] _, y_ ; _A_[ˆ] (Φ ( _·, ·_ ) _, ·_ )��[�] _k∈_ Cal 

## `CP-MDA-Nested` _[⋆]_ **inner algorithm (split and fit)** 

**Algorithm 1** Split and train 

**Input:** Imputation algorithm _I_ , learning algorithm _A_ taking its values in _F_ := _Y[X×M]_ , training set �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][��] _[n] k_ =1[,][calibration][proportion] _[ρ][ ∈]_[]0] _[,]_[ 1]] **Output:** Splitted sets of indices Tr and Cal, imputation function Φ, fitted predictor _A_ ˆ 

1: Randomly split _{_ 1 _, . . . , n}_ into 2 disjoint sets Tr & Cal of sizes #Tr = (1 _− ρ_ ) _n_ and #Cal = _ρn_ 

2: Fit the imputation function: Φ( _·, ·_ ) _←I_ ��� _X_[(] _[k]_[)] _, M_[(] _[k]_[)][�] _, k ∈_ Tr�� 3: Fit the learning algorithm _A_ : _A_[ˆ] ( _·, ·_ ) _←A_ ���Φ � _X_[(] _[k]_[)] _, M_[(] _[k]_[)][�] _, M_[(] _[k]_[)][�] _, k ∈_ Tr�� 

## `CP-MDA-Nested` _[⋆]_ **is Marginally Valid** (MV) 

`CP-MDA-Nested` _[⋆]_ **marginal validity (Z., Josse, Romano, and Dieuleveut, 2024)** 

Under the assumptions that: 

• � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_[+1] =1[are][exchangeable,] 

- the subsampling scheme keeps all of the calibration points, 

then, for almost all imputation function, `CP-MDA-Nested` _[⋆]_ reaches (MV) at the level 1 _−_ 2 _α_ , that is: 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0099-06.png)


Any missing mechanism (no need to assume _M ⊥⊥ X_ ) 

- Does not require ( _Y ⊥⊥ M_ ) _|X_ 

- Marginal guarantee 

**Proof element:** based on Jackknife+ ideas (Barber et al., 2021). 

## **MDA-Exact achieves Mask-Conditional-Validity** (MCV) 

`CP-MDA-Exact` **achieves exact MCV (Z., Dieuleveut, Josse, and Romano, 2023)** 

If: • � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_[+1] =1[are][i.i.d.,] 

• _M⊥⊥X_ , 

• _Y ⊥⊥M |X_ , 

then, for almost all imputation function, `CP-MDA-Exact` is such that for any _m ∈{_ 0 _,_ 1 _}[d]_ such that P _D_ ( _M_ = _m_ ) _>_ 0: 

P _D⊗_ ( _n_ +1) _Y_[(] _[n]_[+1)] _∈ C_[�] _α X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] _|M_[(] _[n]_[+1)] = _m ≥_ 1 _− α,_ � � � and if additionally the scores are almost surely distinct: 

P _D⊗_ ( _n_ +1) � _Y_[(] _[n]_[+1)] _∈ C_[�] _α_ � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] _|M_[(] _[n]_[+1)] = _m_ � _≤_ 1 _− α_ + #Cal1[m] +1 _[.]_ 

Time Series 

Missing Values Missing values and predictive uncertainty interplay `CP-MDA-Nested` _[⋆]_ Numerical experiments Towards asymptotic individualized coverage 

**Before more experiments,** 

Coverage _~ validity_ 

Time Series 

Missing Values Missing values and predictive uncertainty interplay `CP-MDA-Nested` _[⋆]_ 

Numerical experiments 

_M⊥⊥X_ and _Y ⊥⊥M |X_ Beyond independence Real data: TraumaBase[®] Towards asymptotic individualized coverage 

## **Semi-synthetic experiments** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0104-01.png)


**----- Start of picture text -----**<br>
concrete ( d  = 8, l  = 8)<br>60<br>55<br>QR<br>CQR<br>50<br>CQR-MDA-Exact<br>CQR-MDA-Nested<br>45<br>Marginal<br>Lowest<br>40<br>Highest<br>35<br>0 . 7 0 . 8 0 . 9<br>Average coverage<br>length<br>Average<br>**----- End of picture text -----**<br>


Time Series 

Missing Values Missing values and predictive uncertainty interplay `CP-MDA-Nested` _[⋆]_ 

Numerical experiments 

_M⊥⊥X_ and _Y ⊥⊥M |X_ 

Beyond independence Real data: TraumaBase[®] Towards asymptotic individualized coverage 

## **MAR, correlation coefficient of 0.8** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0106-01.png)


**----- Start of picture text -----**<br>
Setting 1 Setting 2 Setting 3 Setting 4 Setting 5<br>8<br>6<br>4<br>0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9<br>Average coverage Average coverage Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>length<br>Average<br>**----- End of picture text -----**<br>


## **MAR, independent features** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0107-01.png)


**----- Start of picture text -----**<br>
Setting 1 Setting 2 Setting 3 Setting 4 Setting 5<br>12<br>10<br>8<br>6<br>4<br>0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0<br>Average coverage Average coverage Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>length<br>Average<br>**----- End of picture text -----**<br>


## **MNAR self-masked, correlation coefficient of 0.8** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0108-01.png)


**----- Start of picture text -----**<br>
Setting 1 Setting 2 Setting 3 Setting 4 Setting 5<br>10<br>8<br>6<br>4<br>0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0<br>Average coverage Average coverage Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>length<br>Average<br>**----- End of picture text -----**<br>


## **MNAR self-masked, independent features** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0109-01.png)


**----- Start of picture text -----**<br>
Setting 1 Setting 2 Setting 3 Setting 4 Setting 5<br>15 . 0<br>12 . 5<br>10 . 0<br>7 . 5<br>5 . 0<br>0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0<br>Average coverage Average coverage Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>length<br>Average<br>**----- End of picture text -----**<br>


## **MNAR quantile censorship, correlation coefficient of 0.8** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0110-01.png)


**----- Start of picture text -----**<br>
Censorship at quantile level 0.5 Censorship at quantile level 0.75 Censorship at quantile level 0.8<br>7<br>6<br>5<br>4<br>Censorship at quantile level 0.85 Censorship at quantile level 0.9 Censorship at quantile level 0.95<br>7<br>6<br>5<br>4<br>0 . 8 0 . 9 0 . 8 0 . 9 0 . 8 0 . 9<br>Average coverage Average coverage Average coverage<br>length<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


## **MNAR quantile censorship, independent features** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0111-01.png)


**----- Start of picture text -----**<br>
Censorship at quantile level 0.5 Censorship at quantile level 0.75 Censorship at quantile level 0.8<br>12<br>10<br>8<br>6<br>4<br>Censorship at quantile level 0.85 Censorship at quantile level 0.9 Censorship at quantile level 0.95<br>12<br>10<br>8<br>6<br>4<br>0 . 7 0 . 8 0 . 9 1 . 0 0 . 7 0 . 8 0 . 9 1 . 0 0 . 7 0 . 8 0 . 9 1 . 0<br>Average coverage Average coverage Average coverage<br>length<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


## _Y ̸⊥⊥M |X_ **, correlation coefficient of 0.8 (** _d_ = 3 **)** 

- _ε ∼N_ (0 _,_ 1) _⊥⊥_ ( _X , M_ ), 

• _X ∼N_ ( _µ,_ Σ), _µ_ = (1 _,_ 1 _,_ 1) _[T]_ , Σ = _ϕ_ (1 _,_ 1 _,_ 1) _[T]_ (1 _,_ 1 _,_ 1) + (1 _− ϕ_ ) _Id_ , _ϕ_ = 0 _._ 8, 

• _Mi ∼B_ (0 _._ 2) for any _i ∈_ �1 _,_ 3�, independently from _X_ and _ε_ , 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0112-04.png)


**----- Start of picture text -----**<br>
• Y =  X 11  {M 1 = 0 }  + 2 X 11  {M 1 = 1 }  + 3 X 21  {M 2 = 1 , M 3 = 1 }  +  ε .<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 0<br>1  − α<br>0 . 5<br>20<br>10<br>X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


## _Y ̸⊥⊥M |X_ **, independent features (** _d_ = 3 **)** ~~ee~~ 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0113-01.png)


**----- Start of picture text -----**<br>
• ε ∼N (0 ,  1)  ⊥⊥ ( X , M ),<br>• X ∼N ( µ,  Σ), µ  = (1 ,  1 ,  1) [T] , Σ =  ϕ (1 ,  1 ,  1) [T] (1 ,  1 ,  1) + (1  − ϕ ) Id , ϕ = 0,<br>• Mi ∼B (0 . 2) for any i ∈ 1 ,  3 , independently from X and ε ,<br>• Y =  X 11  {M 1 = 0 }  + 2 X 11  {M 1 = 1 }  + 3 X 21  {M 2 = 1 , M 3 = 1 }  +  ε .<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 0<br>1  − α<br>0 . 5<br>mr<br>20<br>10<br>X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Time Series 

Missing Values Missing values and predictive uncertainty interplay `CP-MDA-Nested` _[⋆]_ 

Numerical experiments 

_M⊥⊥X_ and _Y ⊥⊥M |X_ Beyond independence Real data: TraumaBase[®] 

Towards asymptotic individualized coverage 

## **TraumaBase[®] : decision support for trauma patients** 

- 30 hospitals 

- More than 30 000 trauma patients 

- 4 000 new patients per year 

- 250 continuous and categorical variables 

   - _�→_ Many useful statistical tasks 

Predict the level of blood platelets upon arrival at hospital, given 7 pre-hospital features. 

These covariates are not always observed. 

## **Data set description i** 

- `Age` : the age of the patient (no missing values); 

- `Lactate` : the conjugate base of lactic acid, upon arrival at the hospital (17.66% missing values); 

- `Delta hemo` : the difference between the hemoglobin upon arrival at hospital and the one in the ambulance (23.82% missing values); 

- `VE` : binary variable indicating if a Volume Expander was applied in the ambulance. A volume expander is a type of intravenous therapy that has the function of providing volume for the circulatory system (2.46% missing values); 

- `RBC` : a binary index which indicates whether the transfusion of Red Blood Cells Concentrates is performed (0.37% missing values); 

## **Data set description ii** 

- `SI` : the shock index. It indicates the level of occult shock based on heart rate 

   - (HR) and systolic blood pressure (SBP), that is SI = SBPHR[,][upon][arrival][at] hospital (2.09% missing values); 

- `HR` : the heart rate measured upon arrival of hospital (1.62% missing values). 

**Real data experiment: TraumaBase[®] , critical care medicine** 


![](markdown_output/Zaffran_PhD_defense_handout_images/Zaffran_PhD_defense_handout.pdf-0118-01.png)


**----- Start of picture text -----**<br>
CQR<br>CQR-MDA-Exact<br>1 . 8<br>CQR-MDA-Nested<br>1 . 6 Marginal<br>Mask-type<br>1 . 4<br>1 . 2<br>0 . 90 0 . 92 0 . 94<br>Average coverage<br>length<br>Average<br>**----- End of picture text -----**<br>


Time Series 

Missing Values Missing values and predictive uncertainty interplay `CP-MDA-Nested` _[⋆]_ Numerical experiments 

Towards asymptotic individualized coverage 

## **Consistency of a universal quantile learner after imputation** 

Let Φ be an imputation function chosen by the user. Denote _gβ,[∗]_ Φ _[∈]_[argmin] E [ _ρβ_ ( _Y − g ◦_ Φ( _X , M_ ))] := _Rβ,φ_ ( _g_ ). _g_ :R _[d] →_ R Comparison with: argmin E [ _ρβ_ ( _Y − f_ ( _X , M_ ))] _(informal)_ . _f_ **Pinball-consistency of an universal learner (Z., Dieuleveut, Josse, and Romano, 2023)** For almost all _C[∞]_ imputation function Φ, the function _gβ,[∗]_ Φ _[◦]_[Φ][is][Bayes] optimal for the pinball-risk of level _β_ . _�→_ any universally consistent algorithm for quantile regression trained on the data imputed by Φ is pinball-Bayes-consistent. 

This is an extension of the result of **?** . 

## **Asymptotic conditional coverage of a universal quantile learner** 

## **Corollary (Z., Dieuleveut, Josse, and Romano, 2023)** 

For any missing mechanism, for almost all _C[∞]_ imputation function Φ, if _FY |_ ( _X_ obs(M) _,M_ ) is continuous, a universally consistent quantile regressor trained on the imputed data set yields asymptotic conditional coverage. 

_�→_ P( _Y ∈ C_[�] _α_ ( _x_ ) _|X_ = _x, M_ = _m_ ) _≥_ 1 _− α_ for any _m ∈M_ and any _x ∈_ R _[d]_ , asymptotically with a super quantile learner. 

