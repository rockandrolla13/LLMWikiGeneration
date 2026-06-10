NB: Open with an advanced pdf reader (e.g., Acrobat to have animations) 

0 / 91 

## **Conformal prediction - A tutorial** 

Aymeric DIEULEVEUT Professor, Ecole[´] Polytechnique July 8, 2025 Hi! PARIS Summer School 

## **Why are we all here today?** 

**(Slides available on my webpage)** 

1 / 91 

## **Why are we all here today?** 

## **(Slides available on my webpage)** 

- Because Conformal Prediction has been a **popular** topic recently. 

**==> picture [281 x 22] intentionally omitted <==**

**----- Start of picture text -----**<br>
E. Candès keynote at NeurIPS<br>CMU's team (Jing Lei & Larry Wasserman)  J. Lei et al., JASA Y. Romano et al., NeurIPS<br>dives into conformal pedagogical paper boost paper<br>**----- End of picture text -----**<br>


Vovk et al. (2005) algorithmic learning in a random world cite count. 

1 / 91 

## **Why are we all here today?** 

**(Slides available on my webpage)** 

- Because Conformal Prediction has been a **popular** topic recently. 

- Because we believe that conformal methods are **important** tools, whose strengths and limitations are sometimes misunderstood. 

## Successfully applied to 

- Medical applications 

- Markets / demand forecasting 

- Computer Vision 

1 / 91 

## **Why are we all here today?** 

**(Slides available on my webpage)** 

- Because Conformal Prediction has been a **popular** topic recently. 

- Because we believe that conformal methods are **important** tools, whose strengths and limitations are sometimes misunderstood. 

- To be part of the **diffusion** effort that many colleagues are making. 

**==> picture [345 x 16] intentionally omitted <==**

**----- Start of picture text -----**<br>
Book reference: Vovk et al. (2005) A gentle tutorial: Angelopoulos and Bates (2023) R. J. Tibshirani<br>(new edition in 2022) + Videos playlist introductive lecture’s notes<br>**----- End of picture text -----**<br>


1 / 91 

## **Why are we all here today?** 

**(Slides available on my webpage)** 

- Because Conformal Prediction has been a **popular** topic recently. 

- Because we believe that conformal methods are **important** tools, whose strengths and limitations are sometimes misunderstood. 

- To be part of the **diffusion** effort that many colleagues are making. 

**Margaux Zaffran UC Berkeley** _PhD at_ Ecole[´] Polytechnique, Polytechnique Institute of Paris, Inria, and EDF 

- _→_ Based on our tutorial with Margaux Zaffran at UAI and ICML, `slides here` 

- _→_ Builds upon earlier material accessible on `this webpage` 

1 / 91 

**Goals and disclaimers** 

## **Goals** 

- Provide a detailed introduction to the basics 

- Demystify the results: fair introduction with limits 

- Give you insights on how to leverage those techniques in your own fields 

2 / 91 

## **On the importance of quantifying uncertainty** 

- **Obvious in most applications - weather, medical, markets** 

3 / 91 

## **On the importance of quantifying uncertainty** 

## • **Obvious in most applications - weather, medical, markets** 

## • **Mathematically** 

**==> picture [378 x 81] intentionally omitted <==**

**----- Start of picture text -----**<br>
10 10 10<br>5 5 5<br>0 0 0<br>− 5 − 5 − 5<br>− 10 − 10 − 10<br>0 2 4 0 2 4 0 2 4<br>X X X<br>Y Y Y<br>**----- End of picture text -----**<br>


_�→_ Same “best” predictor, yet 3 distinct underlying phenomena! 

3 / 91 

## **On the importance of quantifying uncertainty** 

## • **Obvious in most applications - weather, medical, markets** 

## • **Mathematically** 

**==> picture [378 x 81] intentionally omitted <==**

**----- Start of picture text -----**<br>
10 10 10<br>5 5 5<br>0 0 0<br>− 5 − 5 − 5<br>− 10 − 10 − 10<br>0 2 4 0 2 4 0 2 4<br>X X X<br>Y Y Y<br>**----- End of picture text -----**<br>


_�→_ Same “best” predictor, yet 3 distinct underlying phenomena! 

= _⇒_ Quantifying uncertainty conveys this information. 

3 / 91 

## **Quantifying predictive uncertainty** 

- ( _X , Y_ ) _∈_ R _[d] ×_ R random variables 

- _n_ training samples ( _Xi , Yi_ ) _[n] i_ =1 

- Goal: predict an unseen point _Yn_ +1 at _Xn_ +1 with **confidence** 

- How? Given a miscoverage level _α ∈_ [0 _,_ 1], build a predictive set _Cα_ such that: 

P _{Yn_ +1 _∈Cα_ ( _Xn_ +1) _} ≥_ 1 _− α,_ (1) 

and _Cα_ should be as small as possible, in order to be informative _For example: α_ = 0 _._ 1 and obtain a 90% coverage interval 

4 / 91 

## **Quantifying predictive uncertainty** 

- ( _X , Y_ ) _∈_ R _[d] ×_ R random variables 

- _n_ training samples ( _Xi , Yi_ ) _[n] i_ =1 

- Goal: predict an unseen point _Yn_ +1 at _Xn_ +1 with **confidence** 

- How? Given a miscoverage level _α ∈_ [0 _,_ 1], build a predictive set _Cα_ such that: 

P _{Yn_ +1 _∈Cα_ ( _Xn_ +1) _} ≥_ 1 _− α,_ (1) 

and _Cα_ should be as small as possible, in order to be informative _For example: α_ = 0 _._ 1 and obtain a 90% coverage interval 

- Construction of the predictive intervals should be 

   - agnostic to the model 

   - agnostic to the data distribution 

- _Validity_ should be ensured 

   - in finite samples 

   - for all data distribution and underlying model 

4 / 91 

## **Our afternoon!** 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method 

Intro II: Overview of some challenges in Conformal Prediction Advanced I: Towards conditional coverage 

Advanced II: Avoiding data splitting: full conformal and out-of-bags approaches Advanced III: Beyond exchangeability 

Applications & Methods I: Some case studies Applications & Methods II: Some methodological advances 

Concluding remarks 

5 / 91 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method Intro II: Overview of some challenges in Conformal Prediction Advanced I: Towards conditional coverage Advanced II: Avoiding data splitting: full conformal and out-of-bags approaches Advanced III: Beyond exchangeability Applications & Methods I: Some case studies Applications & Methods II: Some methodological advances Concluding remarks 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method Standard regression case Conformalized Quantile Regression (CQR) SCP - Multi class Classification On the design choices of conformity scores and (empirical) conditional guarantees 

**Split Conformal Prediction (SCP) (Vovk et al., 2005) without anim** ~~i~~ 

6 / 91 

**without anim** 

## **SCP: implementation details** 

## Calib. Train 

1. Randomly split the training data into a proper training set (size #Tr) and a calibration set (size #Cal) 

7 / 91 

**SCP: implementation details** 

**without anim** 

## Calib. Train 

1. Randomly split the training data into a proper training set (size #Tr) and a calibration set (size #Cal) 

2. Get _µ_ ˆ _by training the algorithm A on the proper training set_ 

7 / 91 

**SCP: implementation details** 

**without anim** 

## Calib. 

## Train 

1. Randomly split the training data into a proper training set (size #Tr) and a calibration set (size #Cal) 

2. Get _µ_ ˆ _by training the algorithm A on the proper training set_ 

3. On the calibration set, get prediction values with _µ_ ˆ 

7 / 91 

**SCP: implementation details** 

**without anim** 

## Calib. 

## Train 

1. Randomly split the training data into a proper training set (size #Tr) and a calibration set (size #Cal) 

2. Get _µ_ ˆ _by training the algorithm A on the proper training set_ 

3. On the calibration set, get prediction values with _µ_ ˆ 

4. Obtain a set of #Cal + 1 conformity scores : 

ˆ _S_ = _{Si_ = _|µ_ ( _Xi_ ) _− Yi |, i ∈_ Cal _} ∪{_ + _∞}_ 

- (+ worst-case scenario) 

7 / 91 

**SCP: implementation details** 

**without anim** 

## Calib. Train 

1. Randomly split the training data into a proper training set (size #Tr) and a calibration set (size #Cal) 

2. Get _µ_ ˆ _by training the algorithm A on the proper training set_ 

3. On the calibration set, get prediction values with _µ_ ˆ 

4. Obtain a set of #Cal + 1 conformity scores : 

**==> picture [194 x 11] intentionally omitted <==**

(+ worst-case scenario) 

5. Compute the 1 _− α_ quantile of these scores, noted _q_ 1 _−α_ ( _S_ )[1] 

- 1Equivalently, let _S_ be the set of #Cal conformity scores (i.e. without adding _{_ + _∞}_ ). Compute 

- the (1 _− α_ ) (1 _/_ #Cal + 1) quantile of these scores _S_ . 

7 / 91 

**without anim** 

## **SCP: implementation details** 

## Calib. Train 

1. Randomly split the training data into a proper training set (size #Tr) and a calibration set (size #Cal) 

2. Get _µ_ ˆ _by training the algorithm A on the proper training set_ 

3. On the calibration set, get prediction values with _µ_ ˆ 

4. Obtain a set of #Cal + 1 conformity scores : 

**==> picture [194 x 11] intentionally omitted <==**

**==> picture [100 x 11] intentionally omitted <==**

5. Compute the 1 _− α_ quantile of these scores, noted _q_ 1 _−α_ ( _S_ )[1] 

6. For a new point _Xn_ +1, return 

**==> picture [255 x 15] intentionally omitted <==**

- 1Equivalently, let _S_ be the set of #Cal conformity scores (i.e. without adding _{_ + _∞}_ ). Compute 

- the (1 _− α_ ) (1 _/_ #Cal + 1) quantile of these scores _S_ . 

7 / 91 

**SCP: theoretical foundation** 

**==> picture [1609 x 1931] intentionally omitted <==**

8 / 91 

**==> picture [1608 x 1826] intentionally omitted <==**

## **SCP: theoretical foundation** 

## **Exchangeability** 

( _Xi , Yi_ ) _[n] i_ =1[are][exchangeable][if,][for][any][permutation] _[σ]_[of][�][1] _[,][ n]_[�][:] _d_ (( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ )) = �� _Xσ_ (1) _, Yσ_ (1)� _, . . . ,_ � _Xσ_ ( _n_ ) _, Yσ_ ( _n_ )�� _._ 

8 / 91 

**==> picture [1608 x 1826] intentionally omitted <==**

## **SCP: theoretical foundation** 

**==> picture [380 x 99] intentionally omitted <==**

**----- Start of picture text -----**<br>
Exchangeability<br>( Xi , Yi ) [n] i =1 [are] [exchangeable] [if,] [for] [any] [permutation] [σ] [of] [�][1] [,][ n] [�][:]<br>d<br>(( X 1 , Y 1)  , . . . ,  ( Xn, Yn )) = �� Xσ (1) , Yσ (1)� , . . . , � Xσ ( n ) , Yσ ( n )�� .<br>Toy case: Z 1 and Z 2 are exchangeable if ( Z 1 , Z 2) = ( [d] Z 2 , Z 1).<br>**----- End of picture text -----**<br>


8 / 91 

## **SCP: theoretical foundation** 

**Exchangeability** ( _Xi , Yi_ ) _[n] i_ =1[are][exchangeable][if,][for][any][permutation] _[σ]_[of][�][1] _[,][ n]_[�][:] _d_ (( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ )) = �� _Xσ_ (1) _, Yσ_ (1)� _, . . . ,_ � _Xσ_ ( _n_ ) _, Yσ_ ( _n_ )�� _._ **Toy case:** _Z_ 1 and _Z_ 2 are exchangeable if ( _Z_ 1 _, Z_ 2) = ( _[d] Z_ 2 _, Z_ 1). 

**==> picture [380 x 114] intentionally omitted <==**

**----- Start of picture text -----**<br>
exchangeable sequences<br>• i.i.d. samples<br>**----- End of picture text -----**<br>


8 / 91 

## **SCP: theoretical foundation** 

## **Exchangeability** 

( _Xi , Yi_ ) _[n] i_ =1[are][exchangeable][if,][for][any][permutation] _[σ]_[of][�][1] _[,][ n]_[�][:] _d_ (( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ )) = �� _Xσ_ (1) _, Yσ_ (1)� _, . . . ,_ � _Xσ_ ( _n_ ) _, Yσ_ ( _n_ )�� _._ **Toy case:** _Z_ 1 and _Z_ 2 are exchangeable if ( _Z_ 1 _, Z_ 2) = ( _[d] Z_ 2 _, Z_ 1). 

## **exchangeable sequences** 

**==> picture [259 x 80] intentionally omitted <==**

**----- Start of picture text -----**<br>
• i.i.d. samples<br> m   σ [2] <br>   <br> ...   ... γ [2] <br>• The components of N   ,  <br>   <br> ...   γ [2] ... <br>m σ [2]<br>   <br>**----- End of picture text -----**<br>


8 / 91 

## **SCP: theoretical guarantees** 

SCP enjoys finite sample guarantees proved in Vovk et al. (2005); Lei et al. (2018). 

**Marginal validity** Suppose ( _Xi , Yi_ ) _[n] i_ =1[+1][are][exchangeable] _[a]_[.][SCP][applied][on][(] _[X][i][,][ Y][i]_[)] _[n] i_ =1[outputs] � _Cα_ ( _·_ ) such that: P _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _≥_ 1 _− α._ � � 

## **SCP: theoretical guarantees** 

SCP enjoys finite sample guarantees proved in Vovk et al. (2005); Lei et al. (2018). 

## **Marginal validity** 

Suppose ( _Xi , Yi_ ) _[n] i_ =1[+1][are][exchangeable] _[a]_[.][SCP][applied][on][(] _[X][i][,][ Y][i]_[)] _[n] i_ =1[outputs] � _Cα_ ( _·_ ) such that: P _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _≥_ 1 _− α._ � � Additionally, if the scores _{Si }i∈_ Cal _∪{Sn_ +1 _}_ are a.s. distinct: 1 P _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _≤_ 1 _− α_ + � � #Cal + 1 _[.] a_ Only the calibration and test data need to be exchangeable. 

9 / 91 

## **Proof architecture of SCP guarantees** 

## **Quantile lemma** 

If ( _U_ 1 _, . . . , Un, Un_ +1) are exchangeable, then for any _β ∈_ ]0 _,_ 1[: 

P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ )) _≥ β._ 

Additionally, if _U_ 1 _, . . . , Un, Un_ +1 are almost surely distinct, then: 

1 P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ )) _≤ β_ + _n_ + 1 _[.]_ 

10 / 91 

## **Proof architecture of SCP guarantees** 

## **Quantile lemma** 

If ( _U_ 1 _, . . . , Un, Un_ +1) are exchangeable, then for any _β ∈_ ]0 _,_ 1[: 

P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ )) _≥ β._ 

Additionally, if _U_ 1 _, . . . , Un, Un_ +1 are almost surely distinct, then: 

1 P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ )) _≤ β_ + _n_ + 1 _[.]_ 

( _Xi , Yi_ ) _[n] i_ =1[+1][exchangeable] _[⇒{][S][i][}][i][∈]_[Cal] _[ ∪{][S][n]_[+1] _[}]_[exchangeable.] 

10 / 91 

## **Proof architecture of SCP guarantees** ~~ee~~ 

**Quantile lemma** If ( _U_ 1 _, . . . , Un, Un_ +1) are exchangeable, then for any _β ∈_ ]0 _,_ 1[: 

P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ )) _≥ β._ 

Additionally, if _U_ 1 _, . . . , Un, Un_ +1 are almost surely distinct, then: 

**==> picture [215 x 24] intentionally omitted <==**

( _Xi , Yi_ ) _[n] i_ =1[+1][exchangeable] _[⇒{][S][i][}][i][∈]_[Cal] _[ ∪{][S][n]_[+1] _[}]_[exchangeable.] 

quantile lemma to the scores gives the result. 

**==> picture [255 x 58] intentionally omitted <==**

10 / 91 

## **Proof of the quantile lemma** 

**Def:** Empirical quantile _qβ_ ( _U_ 1 _, . . . , Uk_ ) := _⌈β × k⌉_ smallest value of ( _U_ 1 _, . . . , Uk_ ) 

11 / 91 

## **Proof of the quantile lemma** 

**Def:** Empirical quantile _qβ_ ( _U_ 1 _, . . . , Uk_ ) := _⌈β × k⌉_ smallest value of ( _U_ 1 _, . . . , Uk_ ) First note that _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ ) _⇐⇒ Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1). 

11 / 91 

**lower bound** 

## **Proof of the quantile lemma** 

**Def:** Empirical quantile _qβ_ ( _U_ 1 _, . . . , Uk_ ) := _⌈β × k⌉_ smallest value of ( _U_ 1 _, . . . , Uk_ ) First note that _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ ) _⇐⇒ Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1). By exchangeability, for any _i ∈_ �1 _, n_ + 1�: P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)) =P ( _Ui ≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)). 

11 / 91 

**upper bound** 

## **Proof of the quantile lemma** 

**Def:** Empirical quantile _qβ_ ( _U_ 1 _, . . . , Uk_ ) := _⌈β × k⌉_ smallest value of ( _U_ 1 _, . . . , Uk_ ) First note that _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ ) _⇐⇒ Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1). By exchangeability, for any _i ∈_ �1 _, n_ + 1�: P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)) =P ( _Ui ≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)). Thus: 

_n_ +1 1 P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)) = _n_ + 1 � P ( _Ui ≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)) _i_ =1 

11 / 91 

## **Proof of the quantile lemma** 

**==> picture [378 x 154] intentionally omitted <==**

11 / 91 

## **Proof of the quantile lemma** 

**==> picture [378 x 209] intentionally omitted <==**

proving the first statement. 

11 / 91 

## **Proof of the quantile lemma** 

**==> picture [378 x 209] intentionally omitted <==**

proving the second statement. 

11 / 91 

## **SCP: theoretical guarantees** 

SCP enjoys finite sample guarantees proved in Vovk et al. (2005); Lei et al. (2018). 

## **Marginal validity Vovk et al. (2005)** 

Suppose ( _Xi , Yi_ ) _[n] i_ =1[+1][are][exchangeable] _[d]_[.][SCP][applied][on][(] _[X][i][,][ Y][i]_[)] _[n] i_ =1[outputs] � _Cα_ ( _·_ ) such that: P _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _≥_ 1 _− α._ � � Additionally, if the scores _{Si }i∈_ Cal _∪{Sn_ +1 _}_ are a.s. distinct: 1 P _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _≤_ 1 _− α_ + � � #Cal + 1 _[.] d_ Only the calibration and test data need to be exchangeable. 

12 / 91 

## **SCP: theoretical guarantees** 

SCP enjoys finite sample guarantees proved in Vovk et al. (2005); Lei et al. (2018). 

## **Marginal validity Vovk et al. (2005)** 

**==> picture [377 x 143] intentionally omitted <==**

✓ Distribution free, model (regressor) free, finite sample average validity guarantee. 

12 / 91 

**Standard mean-regression SCP – strength: validity – good vs bad estimator** ~~Oe~~ 

13 / 91 

## **SCP: theoretical guarantees** 

SCP enjoys finite sample guarantees proved in Vovk et al. (2005); Lei et al. (2018). 

**==> picture [380 x 160] intentionally omitted <==**

**==> picture [300 x 21] intentionally omitted <==**

14 / 91 

**– Standard mean-regression SCP weakness: not adaptive** ~~eee~~ 

- Predict with _µ_ ˆ 

- ˆ 

- ▶ Build _C_[�] _α_ ( _x_ ): [ _µ_ ( _x_ ) _± q_ 1 _−α_ ( _S_ )] 

15 / 91 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method Standard regression case Conformalized Quantile Regression (CQR) SCP - Multi class Classification On the design choices of conformity scores and (empirical) conditional guarantees 

**Conformalized Quantile Regression (CQR) (Romano et al., 2019)** ~~OOO~~ 

16 / 91 

**without anim** 

## **Conformalized Quantile Regression (CQR)** 

� _Cα_ ( _x_ ) = [ lower[(] _[x]_[)] _[ −][q]_ 1 _−α_[(] _[S]_[)][;] � QRupper( _x_ ) + _q_ 1 _−α_ ( _S_ )] 

Thus 

_Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) = _{Sn_ +1 _≤ q_ 1 _−α_ ( _S_ ) _} ._ 

- ⇝ Marginal validity is ensured, independently of the underlying quantile level or 

regressor quality. ✓ 

17 / 91 

**CQR: under vs over coverage** ~~ee~~ 

18 / 91 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method Standard regression case Conformalized Quantile Regression (CQR) 

SCP - Multi class Classification On the design choices of conformity scores and (empirical) conditional guarantees 

**==> picture [1790 x 1805] intentionally omitted <==**

**----- Start of picture text -----**<br>
i.e.,<br>Yn +1 ∈ C [�] α  ( Xn +1)<br>� �<br>**----- End of picture text -----**<br>


## **SCP: standard classification** 

- _Y ∈{_ 1 _, . . . , C }_ 

- _A_[ˆ] ( _X_ ) = ( _p_ ˆ1( _X_ ) _, . . . ,_ ˆ _pC_ ( _X_ )) 

( _C_ classes) (estimated probabilities) 

19 / 91 

**==> picture [1790 x 1805] intentionally omitted <==**

**----- Start of picture text -----**<br>
i.e.,<br>Yn +1 ∈ C [�] α  ( Xn +1)<br>� �<br>**----- End of picture text -----**<br>


## **SCP: standard classification** 

- _Y ∈{_ 1 _, . . . , C }_ 

• _A_[ˆ] ( _X_ ) = ( _p_ ˆ1( _X_ ) _, . . . ,_ ˆ _pC_ ( _X_ )) 

( _C_ classes) (estimated probabilities) 

- Score ? 

19 / 91 

## **SCP: standard classification** 

- _Y ∈{_ 1 _, . . . , C }_ 

• _A_[ˆ] ( _X_ ) = ( _p_ ˆ1( _X_ ) _, . . . ,_ ˆ _pC_ ( _X_ )) 

( _C_ classes) (estimated probabilities) 

- Score 

s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y_ 

19 / 91 

## **SCP: standard classification** 

- _Y ∈{_ 1 _, . . . , C }_ 

- • _A_[ˆ] ( _X_ ) = ( _p_ ˆ1( _X_ ) _, . . . ,_ ˆ _pC_ ( _X_ )) 

( _C_ classes) (estimated probabilities) 

- Score 

s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y_ 

- For a new point _Xn_ +1, return 

   - 

   - _Cα_ ( _Xn_ +1) = _{y_ such that s ( _A_[ˆ] ( _Xn_ +1) _, y_ ) _≤ q_ 1 _−α_ ( _S_ ) _}_ 

i.e., 

**==> picture [205 x 21] intentionally omitted <==**

19 / 91 

**==> picture [3586 x 3655] intentionally omitted <==**

**----- Start of picture text -----**<br>
Pred on Cal i = 1 2 3 Cal<br>p ˆdog( Xi ) 0.95 0.90 0.85 0.15 0.15 0.20 0.15 0.15 0.25 0.20<br>p ˆtiger( Xi ) 0.02 0.05 0.10 0.60 0.55 0.60 0.65 0.10 0.35 0.45<br>p ˆcat( Xi ) 0.03 0.05 0.05 0.25 0.30 0.20 0.20 0.75 0.40 0.35<br>• Scores on the calibration set s ( A [ˆ] ( X ) , Y  ) := 1  − ( A [ˆ] ( X )) Y<br>⇒ q 1 −α ( S Cal) = 0.65<br>Pred. on Test n  + 1<br>p ˆdog( Xn +1) 0.03<br>p ˆtiger( Xn +1) 0.37<br>p ˆcat( Xn +1) 0.60<br>A ˆ( Xn +1) = (0 . 03 ,  0 . 37 ,  0 . 60) C � α ( Xn +1) =  { “tiger”, “cat” }<br>**----- End of picture text -----**<br>


## **SCP: standard classification in practice** 

Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

20 / 91 

**==> picture [3586 x 3655] intentionally omitted <==**

**----- Start of picture text -----**<br>
• Scores on the calibration set s ( A [ˆ] ( X ) , Y  ) := 1  − ( A [ˆ] ( X )) Y<br>⇒ q 1 −α ( S Cal) = 0.65<br>Pred. on Test n  + 1<br>p ˆdog( Xn +1) 0.03<br>p ˆtiger( Xn +1) 0.37<br>p ˆcat( Xn +1) 0.60<br>A ˆ( Xn +1) = (0 . 03 ,  0 . 37 ,  0 . 60) C � α ( Xn +1) =  { “tiger”, “cat” }<br>**----- End of picture text -----**<br>


## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.25<br>0.20<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.35<br>0.45<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.40<br>0.35|
|||



20 / 91 

**==> picture [3586 x 3648] intentionally omitted <==**

**----- Start of picture text -----**<br>
• Scores on the calibration set s ( A [ˆ] ( X ) , Y  ) := 1  − ( A [ˆ] ( X )) Y<br>⇒ q 1 −α ( S Cal) = 0.65<br>Pred. on Test n  + 1<br>p ˆdog( Xn +1) 0.03<br>p ˆtiger( Xn +1) 0.37<br>p ˆcat( Xn +1) 0.60<br>A ˆ( Xn +1) = (0 . 03 ,  0 . 37 ,  0 . 60) C � α ( Xn +1) =  { “tiger”, “cat” }<br>**----- End of picture text -----**<br>


## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.25<br>0.20<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.35<br>0.45<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.40<br>0.35|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|||



20 / 91 

**==> picture [3586 x 3648] intentionally omitted <==**

**----- Start of picture text -----**<br>
• Scores on the calibration set s ( A [ˆ] ( X ) , Y  ) := 1  − ( A [ˆ] ( X )) Y<br>⇒ q 1 −α ( S Cal) = 0.65<br>Pred. on Test n  + 1<br>p ˆdog( Xn +1) 0.03<br>p ˆtiger( Xn +1) 0.37<br>p ˆcat( Xn +1) 0.60<br>A ˆ( Xn +1) = ( 0.03 ,  0 . 37 ,  0 . 60) C � α ( Xn +1) =  { “tiger”, “cat” }<br>**----- End of picture text -----**<br>


## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.25<br>0.20<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.35<br>0.45<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.40<br>0.35|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|||



20 / 91 

**==> picture [3570 x 3633] intentionally omitted <==**

**----- Start of picture text -----**<br>
⇒ q 1 −α ( S Cal) = 0.65<br>Pred. on Test n  + 1<br>p ˆdog( Xn +1) 0.03<br>p ˆtiger( Xn +1) 0.37<br>p ˆcat( Xn +1) 0.60<br>A ˆ( Xn +1) = (0 . 03 ,  0.37 ,  0 . 60) C � α ( Xn +1) =  { “tiger”, “cat” }<br>**----- End of picture text -----**<br>


## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.25<br>0.20<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.35<br>0.45<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.40<br>0.35|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|||



## • Scores on the calibration set s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y_ 

20 / 91 

**==> picture [3586 x 3641] intentionally omitted <==**

**----- Start of picture text -----**<br>
⇒ q 1 −α ( S Cal) = 0.65<br>Pred. on Test n  + 1<br>p ˆdog( Xn +1) 0.03<br>p ˆtiger( Xn +1) 0.37<br>p ˆcat( Xn +1) 0.60<br>A ˆ( Xn +1) = (0 . 03 ,  0 . 37 ,  0.60 ) C � α ( Xn +1) =  { “tiger”, “cat” }<br>**----- End of picture text -----**<br>


## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.25<br>0.20<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.35<br>0.45<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.40<br>0.35|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|_Si_|0.05<br>0.10<br>0.15<br>0.40<br>0.45<br>0.40<br>0.35<br>0.25<br>0.60<br>0.65|



• Scores on the calibration set s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y_ 

20 / 91 

**==> picture [3586 x 3641] intentionally omitted <==**

**----- Start of picture text -----**<br>
Pred. on Test n  + 1<br>p ˆdog( Xn +1) 0.03<br>p ˆtiger( Xn +1) 0.37<br>p ˆcat( Xn +1) 0.60<br>A ˆ( Xn +1) = (0 . 03 ,  0 . 37 ,  0 . 60) C � α ( Xn +1) =  { “tiger”, “cat” }<br>**----- End of picture text -----**<br>


## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.25<br>0.20<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.35<br>0.45<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.40<br>0.35|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|_Si_|0.05<br>0.10<br>0.15<br>0.40<br>0.45<br>0.40<br>0.35<br>0.25<br>0.60<br>0.65|



• Scores on the calibration set s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y ⇒ q_ 1 _−α_ ( _S_ Cal) = 0.65 

20 / 91 

**==> picture [1586 x 1641] intentionally omitted <==**

## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.25<br>0.20<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.35<br>0.45<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.40<br>0.35|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|_Si_|0.05<br>0.10<br>0.15<br>0.40<br>0.45<br>0.40<br>0.35<br>0.25<br>0.60<br>0.65|



- Scores on the calibration set s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y_ 

- _⇒ q_ 1 _−α_ ( _S_ Cal) = 0.65 

|_⇒q_1_−α_(_S_Cal|)=<br>0.|
|---|---|
|Pred. on Test|_n_+ 1|
|ˆ_p_dog(_Xn_+1)|0.03|
|ˆ_p_tiger(_Xn_+1)|0.37|
|ˆ_p_cat(_Xn_+1)|0.60|



_A_ ˆ( _Xn_ +1) = (0 _._ 03 _,_ 0 _._ 37 _,_ 0 _._ 60) 

20 / 91 

## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.25<br>0.20<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.35<br>0.45<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.40<br>0.35|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|_Si_|0.05<br>0.10<br>0.15<br>0.40<br>0.45<br>0.40<br>0.35<br>0.25<br>0.60<br>0.65|



- Scores on the calibration set s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y_ 

- _⇒ q_ 1 _−α_ ( _S_ Cal) = 0.65 

|Pred. on Test|_n_+ 1||
|---|---|---|
|ˆ_p_dog(_Xn_+1)|0.03|s (ˆ_A_(_Xn_+1)_,_“dog”) = 0_._97|
|ˆ_p_tiger(_Xn_+1)|0.37|s (ˆ_A_(_Xn_+1)_,_“tiger”) = 0_._63|
|ˆ_p_cat(_Xn_+1)|0.60|s ( ˆ_A_(_Xn_+1)_,_“cat”)= 0_._40|



_A_ ˆ( _Xn_ +1) = (0 _._ 03 _,_ 0 _._ 37 _,_ 0 _._ 60) 

20 / 91 

## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.25<br>0.20<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.35<br>0.45<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.40<br>0.35|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|_Si_|0.05<br>0.10<br>0.15<br>0.40<br>0.45<br>0.40<br>0.35<br>0.25<br>0.60<br>0.65|



- Scores on the calibration set s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y_ 

- _⇒ q_ 1 _−α_ ( _S_ Cal) = 0.65 

Pred. on Test _n_ + 1 ˆ _p_ dog( _Xn_ +1) 0.03 s ( _A_[ˆ] ( _Xn_ +1) _,_ “dog”) = 0 _._ 97 _> q_ 1 _−α_ ( _S_ Cal) ˆ _p_ tiger( _Xn_ +1) 0.37 s ( _A_[ˆ] ( _Xn_ +1) _,_ “tiger”) = 0 _._ 63 _≤ q_ 1 _−α_ ( _S_ ) ˆ _p_ cat( _Xn_ +1) 0.60 s ( _A_[ˆ] ( _Xn_ +1) _,_ “cat”) = 0 _._ 40 _≤ q_ 1 _−α_ ( _S_ Cal) 

_A_ ˆ( _Xn_ +1) = (0 _._ 03 _,_ 0 _._ 37 _,_ 0 _._ 60) 

20 / 91 

## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.25<br>0.20<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.35<br>0.45<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.40<br>0.35|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|_Si_|0.05<br>0.10<br>0.15<br>0.40<br>0.45<br>0.40<br>0.35<br>0.25<br>0.60<br>0.65|



**==> picture [277 x 14] intentionally omitted <==**

_⇒ q_ 1 _−α_ ( _S_ Cal) = 0.65 

Pred. on Test _n_ + 1 ˆ _p_ dog( _Xn_ +1) 0.03 s ( _A_[ˆ] ( _Xn_ +1) _,_ “dog”) = 0 _._ 97 _> q_ 1 _−α_ ( _S_ Cal) “dog” _∈/ C_[�] _α_ ( _Xn_ +1) ˆ _p_ tiger( _Xn_ +1) 0.37 s ( _A_[ˆ] ( _Xn_ +1) _,_ “tiger”) = 0 _._ 63 _≤ q_ 1 _−α_ ( _S_ ) “tiger” _∈ C_[�] _α_ ( _Xn_ +1) ˆ _p_ cat( _Xn_ +1) 0.60 s ( _A_[ˆ] ( _Xn_ +1) _,_ “cat”) = 0 _._ 40 _≤ q_ 1 _−α_ ( _S_ Cal) “cat” _∈ C_[�] _α_ ( _Xn_ +1) � _Xnn_ +1) = (0) = (0 _._ 03 _,_ 0 _._ 37 _,_ 0 _._ 60) _Cα_ ( _Xn_ +1) = _{_ “tiger”, “cat” _}_ 20 / 91 

_A_ ˆ( _Xnn_ +1) = (0) = (0 _._ 03 _,_ 0 _._ 37 _,_ 0 _._ 60) 

## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.05<br>0.05<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.15<br>0.05<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.80<br>0.90|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|_Si_|0.05<br>0.10<br>0.15<br>0.40<br>0.45<br>0.40<br>0.35<br>0.25<br>-|



• Scores on the calibration set s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y ⇒ q_ 1 _−α_ ( _S_ Cal) = 0.65 

|Pred. on Test|_n_+ 1||||
|---|---|---|---|---|
|ˆ_p_dog(_Xn_+1)|0.03|s (ˆ_A_(_Xn_+1)_,_“dog”) = 0_._97|_> q_1_−α_(_S_Cal)|“dog” _/∈_�_Cα_(_Xn_+1)|
|ˆ_p_tiger(_Xn_+1)|0.37|s (ˆ_A_(_Xn_+1)_,_“tiger”) = 0_._63|_≤q_1_−α_(_S_)|“tiger” _∈_�_Cα_(_Xn_+1)|
|ˆ_p_cat(_Xn_+1)|0.60|s ( ˆ_A_(_Xn_+1)_,_“cat”)= 0_._40|_≤q_1_−α_(_S_Cal)|“cat”_∈_�_Cα_(_Xn_+1)|



**==> picture [131 x 14] intentionally omitted <==**

**==> picture [134 x 15] intentionally omitted <==**

20 / 91 

## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.05<br>0.05<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.15<br>0.05<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.80<br>0.90|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|_Si_|0.05<br>0.10<br>0.15<br>0.40<br>0.45<br>0.40<br>0.35<br>0.25<br>0.2<br>0.1|



• Scores on the calibration set s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y ⇒ q_ 1 _−α_ ( _S_ Cal) = 0.65 

|Pred. on Test|_n_+ 1||||
|---|---|---|---|---|
|ˆ_p_dog(_Xn_+1)|0.03|s (ˆ_A_(_Xn_+1)_,_“dog”) = 0_._97|_> q_1_−α_(_S_Cal)|“dog” _/∈_�_Cα_(_Xn_+1)|
|ˆ_p_tiger(_Xn_+1)|0.37|s (ˆ_A_(_Xn_+1)_,_“tiger”) = 0_._63|_≤q_1_−α_(_S_)|“tiger” _∈_�_Cα_(_Xn_+1)|
|ˆ_p_cat(_Xn_+1)|0.60|s ( ˆ_A_(_Xn_+1)_,_“cat”)= 0_._40|_≤q_1_−α_(_S_Cal)|“cat”_∈_�_Cα_(_Xn_+1)|



**==> picture [131 x 14] intentionally omitted <==**

**==> picture [134 x 15] intentionally omitted <==**

20 / 91 

## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.05<br>0.05<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.15<br>0.05<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.80<br>0.90|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|_Si_|0.05<br>0.10<br>0.15<br>0.40<br>0.45<br>0.40<br>0.35<br>0.25<br>0.2<br>0.1|



• Scores on the calibration set s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y ⇒ q_ 1 _−α_ ( _S_ Cal) = 0.45 

|Pred. on Test|_n_+ 1||||
|---|---|---|---|---|
|ˆ_p_dog(_Xn_+1)|0.03|s (ˆ_A_(_Xn_+1)_,_“dog”) = 0_._97|_> q_1_−α_(_S_Cal)|“dog” _/∈_�_Cα_(_Xn_+1)|
|ˆ_p_tiger(_Xn_+1)|0.37|s (ˆ_A_(_Xn_+1)_,_“tiger”) = 0_._63|_≤q_1_−α_(_S_)|“tiger” _∈_�_Cα_(_Xn_+1)|
|ˆ_p_cat(_Xn_+1)|0.60|s ( ˆ_A_(_Xn_+1)_,_“cat”)= 0_._40|_≤q_1_−α_(_S_Cal)|“cat”_∈_�_Cα_(_Xn_+1)|



**==> picture [131 x 14] intentionally omitted <==**

**==> picture [134 x 15] intentionally omitted <==**

20 / 91 

## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.05<br>0.05<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.15<br>0.05<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.80<br>0.90|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|_Si_|0.05<br>0.10<br>0.15<br>0.40<br>0.45<br>0.40<br>0.35<br>0.25<br>0.2<br>0.1|



• Scores on the calibration set s ( _A_[ˆ] ( _X_ ) _, Y_ ) := 1 _−_ ( _A_[ˆ] ( _X_ )) _Y ⇒ q_ 1 _−α_ ( _S_ Cal) = 0.45 

|Pred. on Test|_n_+ 1||||||
|---|---|---|---|---|---|---|
|ˆ_p_dog(_Xn_+1)|0.03|s (ˆ_A_(_Xn_+1)_,_“dog”) = 0_._97|_> q_1_−α_(_S_Cal)|“dog” _/∈_�_Cα_(_Xn_+1)|||
|ˆ_p_tiger(_Xn_+1)|0.37|s (ˆ_A_(_Xn_+1)_,_“tiger”) = 0_._63|_> q_1_−α_(_S_Cal)|“tiger”|_/∈_�_Cα_(_Xn_+1)||
|ˆ_p_cat(_Xn_+1)|0.60|s( ˆ_A_(_Xn_+1)_,_“cat”)= 0_._40|_≤q_1_−α_(_S_Cal)|“cat”_∈_�_Cα_(_Xn_+1)|||



_A_ ˆ( _Xn_ +1) = (0 _._ 03 _,_ 0 _._ 37 _,_ 0 _._ 60) 

� _Cα_ ( _Xn_ +1) = _{_ “tiger”, “cat” _}_ 

20 / 91 

## **SCP: standard classification in practice** 

## Ex: _Yi ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

|Ex: _Yi ∈{_“d|og”_,_“tiger”_,_“cat”_}_, with _α_= 0_._1|
|---|---|
|Pred on Cal<br>ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|_i_ = 1<br>2<br>3<br>Cal<br>0.95<br>0.90<br>0.85<br>0.15<br>0.15<br>0.20<br>0.15<br>0.15<br>0.05<br>0.05<br>0.02<br>0.05<br>0.10<br>0.60<br>0.55<br>0.60<br>0.65<br>0.10<br>0.15<br>0.05<br>0.03<br>0.05<br>0.05<br>0.25<br>0.30<br>0.20<br>0.20<br>0.75<br>0.80<br>0.90|
|Y_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|_Si_|0.05<br>0.10<br>0.15<br>0.40<br>0.45<br>0.40<br>0.35<br>0.25<br>0.2<br>0.1|



|• Scores on the|calibration set|calibration set|s ( ˆ_A_(_X_)_, Y_)|:= 1_−_( ˆ_A_(_X_))_Y_||||
|---|---|---|---|---|---|---|---|
|_⇒q_1_−α_(_S_Cal)=||0.45||||||
|Pred. on Test<br>_n_+||1||||||
|ˆ_p_dog(_Xn_+1)<br>0.03||s (ˆ_A_(_Xn_+1)_,_|“dog”) = 0_._97|_> q_1_−α_(_S_Cal)|“dog” _/∈_�_Cα_(_Xn_+1)|||
|ˆ_p_tiger(_Xn_+1)<br>0.37||s (ˆ_A_(_Xn_+1)_,_|“tiger”) = 0_._63|_> q_1_−α_(_S_Cal)|“tiger”|_/∈_�_Cα_(_Xn_+1)||
|ˆ_p_cat(_Xn_+1)<br>0.60||s( ˆ_A_(_Xn_+1)_,_|“cat”)= 0_._40|_≤q_1_−α_(_S_Cal)|“cat”_∈_�_Cα_(_Xn_+1)|||
|ˆ_A_(_Xn_+1) = (0_._03_,_0_._37_,_0_._60)||||�_Cα_(_Xn_+1) =_{_“cat”_}_||||



_A_ ˆ( _Xn_ +1) = (0 _._ 03 _,_ 0 _._ 37 _,_ 0 _._ 60) 

20 / 91 

## **SCP: limits of the standard classification case** 

## **efficiency yet non-adaptivity of the simplest classification scores** 

- ✓ Outputs the most efficient set possible (i.e. achieving the smallest average set size, Sadinle et al., 2018), 

✗ Does not allow to discriminate between “easy” and “hard” test point. In practice, it leads to predictive sets that under-cover (resp. over-cover) on “hard” (resp. “easy”) subgroups. 

This is due to the fact that the same threshold _q_ 1 _−α_ ( _S_ ) is applied to any test point. 

21 / 91 

**==> picture [1859 x 1826] intentionally omitted <==**

**----- Start of picture text -----**<br>
Figure highly inspired by Angelopoulos and Bates (2023).<br>Cat Tiger Dog Cat Tiger Dog<br>Estimated probabilities Cumulative estimated probabilities<br>**----- End of picture text -----**<br>


## **SCP: classification with Adaptive Prediction Sets**[8] 

1. Sort in decreasing order _p_ ˆ _σx_ (1)( _x_ ) _≥ . . . ≥ p_ ˆ _σx_ ( _C_ )( _x_ ) 

- 8Romano et al. (2020b), _Classification with Valid and Adaptive Coverage_ , NeurIPS 

22 / 91 

**==> picture [1859 x 1826] intentionally omitted <==**

**----- Start of picture text -----**<br>
Figure highly inspired by Angelopoulos and Bates (2023).<br>Cat Tiger Dog Cat Tiger Dog<br>Estimated probabilities Cumulative estimated probabilities<br>**----- End of picture text -----**<br>


## **SCP: classification with Adaptive Prediction Sets**[8] 

1. Sort in decreasing order _p_ ˆ _σx_ (1)( _x_ ) _≥ . . . ≥ p_ ˆ _σx_ ( _C_ )( _x_ ) 

_x_ ( _y_ ) ˆ 2. s ( _x, y_ ; ˆ _p_ ) :=[�] _k[σ]_ =1 _[−]_[1] _pσx_ ( _k_ )( _x_ ) (sum of the estimated probabilities associated to classes at least as large as that of the true class _Y_ ) 

- 8Romano et al. (2020b), _Classification with Valid and Adaptive Coverage_ , NeurIPS 

22 / 91 

**==> picture [1859 x 1826] intentionally omitted <==**

**----- Start of picture text -----**<br>
Figure highly inspired by Angelopoulos and Bates (2023).<br>Cat Tiger Dog Cat Tiger Dog<br>Estimated probabilities Cumulative estimated probabilities<br>**----- End of picture text -----**<br>


## **SCP: classification with Adaptive Prediction Sets**[8] 

**==> picture [252 x 14] intentionally omitted <==**

**==> picture [372 x 19] intentionally omitted <==**

associated to classes at least as large as that of the true class _Y_ ) 

**==> picture [281 x 14] intentionally omitted <==**

**==> picture [243 x 34] intentionally omitted <==**

> 8Romano et al. (2020b), _Classification with Valid and Adaptive Coverage_ , NeurIPS 

22 / 91 

## **SCP: classification with Adaptive Prediction Sets**[8] 

**==> picture [252 x 14] intentionally omitted <==**

**==> picture [372 x 19] intentionally omitted <==**

associated to classes at least as large as that of the true class _Y_ ) 

**==> picture [281 x 14] intentionally omitted <==**

**==> picture [243 x 146] intentionally omitted <==**

> 8Romano et al. (2020b), _Classification with Valid and Adaptive Coverage_ , NeurIPS Figure highly inspired by Angelopoulos and Bates (2023). 

22 / 91 

## **SCP: classification with Adaptive Prediction Sets in practice** 

## Ex: _Y ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

## • Scores on the calibration set 

|Cal_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|---|---|
|ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|0.95<br>0.02<br>0.03<br>0.90<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.80<br>0.15<br>0.05<br>0.75<br>0.20<br>0.10<br>0.75<br>0.15<br>0.25<br>0.40<br>0.35<br>0.10<br>0.30<br>0.60<br>0.15<br>0.30<br>0.55|
|_Si_|0.95<br>0.90<br>0.85<br>0.85<br>0.80<br>0.75<br>0.75<br>0.75<br>0.60<br>0.55|



23 / 91 

## **SCP: classification with Adaptive Prediction Sets in practice** 

## Ex: _Y ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

## • Scores on the calibration set 

|Cal_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|---|---|
|ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|0.95<br>0.02<br>0.03<br>0.90<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.80<br>0.15<br>0.05<br>0.75<br>0.20<br>0.10<br>0.75<br>0.15<br>0.25<br>0.40<br>0.35<br>0.10<br>0.30<br>0.60<br>0.15<br>0.30<br>0.55|
|_Si_|0.95<br>0.90<br>0.85<br>0.85<br>0.80<br>0.75<br>0.75<br>0.75<br>0.60<br>0.55|



## • _q_ 1 _−α_ ( _S_ ) = 0 _._ 95 

23 / 91 

## **SCP: classification with Adaptive Prediction Sets in practice** 

## Ex: _Y ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

## • Scores on the calibration set 

|Cal_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|---|---|
|ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|0.95<br>0.02<br>0.03<br>0.90<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.80<br>0.15<br>0.05<br>0.75<br>0.20<br>0.10<br>0.75<br>0.15<br>0.25<br>0.40<br>0.35<br>0.10<br>0.30<br>0.60<br>0.15<br>0.30<br>0.55|
|_Si_|0.95<br>0.90<br>0.85<br>0.85<br>0.80<br>0.75<br>0.75<br>0.75<br>0.60<br>0.55|



## • _q_ 1 _−α_ ( _S_ ) = 0 _._ 95 

## _�→_ Ex 1: _A_[ˆ] ( _Xn_ +1) = (0 _._ 05 _,_ 0 _._ 45 _,_ 0 _._ 5) 

23 / 91 

## **SCP: classification with Adaptive Prediction Sets in practice** 

## Ex: _Y ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

## • Scores on the calibration set 

|Cal_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|---|---|
|ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|0.95<br>0.02<br>0.03<br>0.90<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.80<br>0.15<br>0.05<br>0.75<br>0.20<br>0.10<br>0.75<br>0.15<br>0.25<br>0.40<br>0.35<br>0.10<br>0.30<br>0.60<br>0.15<br>0.30<br>0.55|
|_Si_|0.95<br>0.90<br>0.85<br>0.85<br>0.80<br>0.75<br>0.75<br>0.75<br>0.60<br>0.55|



• _q_ 1 _−α_ ( _S_ ) = 0 _._ 95 _�→_ Ex 1: _A_[ˆ] ( _Xn_ +1) = (0 _._ 05 _,_ 0 _._ 45 _,_ 0 _._ 5) _, r[⋆]_ = 2 

� _Cα_ ( _Xn_ +1) = _{_ “tiger”, “cat” _}_ 

23 / 91 

## **SCP: classification with Adaptive Prediction Sets in practice** 

## Ex: _Y ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

## • Scores on the calibration set 

|Cal_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|---|---|
|ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|0.95<br>0.02<br>0.03<br>0.90<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.80<br>0.15<br>0.05<br>0.75<br>0.20<br>0.10<br>0.75<br>0.15<br>0.25<br>0.40<br>0.35<br>0.10<br>0.30<br>0.60<br>0.15<br>0.30<br>0.55|
|_Si_|0.95<br>0.90<br>0.85<br>0.85<br>0.80<br>0.75<br>0.75<br>0.75<br>0.60<br>0.55|



• _q_ 1 _−α_ ( _S_ ) = 0 _._ 95 _�→_ Ex 1: _A_[ˆ] ( _Xn_ +1) = (0 _._ 05 _,_ 0 _._ 45 _,_ 0 _._ 5) _, r[⋆]_ = 2 

� _Cα_ ( _Xn_ +1) = _{_ “tiger”, “cat” _}_ 

- _�→_ Ex 2: _A_[ˆ] ( _Xn_ +1) = (0 _._ 03 _,_ 0 _._ 95 _,_ 0 _._ 02) 

23 / 91 

## **SCP: classification with Adaptive Prediction Sets in practice** 

## Ex: _Y ∈{_ “dog” _,_ “tiger” _,_ “cat” _}_ , with _α_ = 0 _._ 1 

## • Scores on the calibration set 

|Cal_i_|“dog”<br>“dog”<br>“dog”<br>“tiger” “tiger” “tiger” “tiger” “cat”<br>“cat”<br>“cat”|
|---|---|
|ˆ_p_dog(_Xi_)<br>ˆ_p_tiger(_Xi_)<br>ˆ_p_cat(_Xi_)|0.95<br>0.02<br>0.03<br>0.90<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.80<br>0.15<br>0.05<br>0.75<br>0.20<br>0.10<br>0.75<br>0.15<br>0.25<br>0.40<br>0.35<br>0.10<br>0.30<br>0.60<br>0.15<br>0.30<br>0.55|
|_Si_|0.95<br>0.90<br>0.85<br>0.85<br>0.80<br>0.75<br>0.75<br>0.75<br>0.60<br>0.55|



- _q_ 1 _−α_ ( _S_ ) = 0 _._ 95 _�→_ Ex 1: _A_[ˆ] ( _Xn_ +1) = (0 _._ 05 _,_ 0 _._ 45 _,_ 0 _._ 5) _, r[⋆]_ = 2 

   - _�→_ Ex 2: _A_[ˆ] ( _Xn_ +1) = (0 _._ 03 _,_ 0 _._ 95 _,_ 0 _._ 02) _, r[⋆]_ = 1 

� _Cα_ ( _Xn_ +1) = _{_ “tiger”, “cat” _}_ � _Cα_ ( _Xn_ +1) = _{_ “tiger” _}_ 

23 / 91 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method Standard regression case Conformalized Quantile Regression (CQR) SCP - Multi class Classification On the design choices of conformity scores and (empirical) conditional guarantees 

## **SCP: what choices for the regression scores?** 

**==> picture [253 x 21] intentionally omitted <==**

24 / 91 

## **SCP: what choices for the regression scores?** ~~ee~~ 

# � _Cα_ ( _Xn_ +1) = _{y_ such that s _Xn_ +1 _, y_ ; _A ≤ q_ 1 _−α_ ( _S_ ) _}_ 

**Standard SCP** Vovk et al. (2005) ~~aa~~ s ( _A_[ˆ] ( _X_ ) _, Y_ ) _|µ_ ˆ( _X_ ) _− Y |_ 

� ˆ _Cα_ ( _x_ ) [ _µ_ ( _x_ ) _± q_ 1 _−α_ ( _S_ )] 

Visu. ~~a~~ ✓ black-box around a “usable” prediction ✗ not adaptive | | 

24 / 91 

## **SCP: what choices for the regression scores?** ~~ee~~ 

� _Cα_ ( _Xn_ +1) = _{y_ such that s _Xn_ +1 _, y_ ; _A ≤ q_ 1 _−α_ ( _S_ ) _}_ 

**Standard SCP CQR** ~~pp~~ Vovk et al. (2005) Romano et al. (2019) s ( _A_[ˆ] ( _X_ ) _, Y_ ) _|µ_ ˆ( _X_ ) _− Y |_ max(QR[�] lower( _X_ ) _− Y , Y −_ QR[�] upper( _X_ )) � ˆ [QR[�] lower( _x_ ) _− q_ 1 _−α_ ( _S_ ); _Cα_ ( _x_ ) [ _µ_ ( _x_ ) _± q_ 1 _−α_ ( _S_ )] � QRupper( _x_ ) + _q_ 1 _−α_ ( _S_ )] Visu. ✓ black-box around a “usadaptive able” prediction ~~OO~~ ✗ not adaptive no black-box around a “usable” prediction 

24 / 91 

**SCP: what choices for the regression scores?** ~~a~~ 

� _Cα_ ( _Xn_ +1) = _{y_ such that s _Xn_ +1 _, y_ ; _A ≤ q_ 1 _−α_ ( _S_ ) _}_ 

|~~**e**e~~|**Standard SCP**<br>Vovk et al. (2005)|**Locally weighted SCP**<br>**CQR**<br>Lei et al. (2018)<br>Romano et al. (2019)<br>~~)~~<br>~~s~~|**Locally weighted SCP**<br>**CQR**<br>Lei et al. (2018)<br>Romano et al. (2019)<br>~~)~~<br>~~s~~|
|---|---|---|---|
|s ( ˆ_A_(_X_)_, Y_)|_|_ˆ_µ_(_X_)_−Y |_|_|_ˆ_µ_(_X_)_−Y |_<br>ˆ_ρ_(_X_)|max( �<br>QRlower(_X_)_−Y ,_<br>_Y −_�<br>QRupper(_X_))|
|�_Cα_(_x_)|[ˆ_µ_(_x_)_± q_1_−α_(_S_)]|[ˆ_µ_(_x_)_± q_1_−α_(_S_)ˆ_ρ_(_x_)]|[ �<br>QRlower(_x_)_−q_1_−α_(_S_);<br>�<br>QRupper(_x_) +_q_1_−α_(_S_)]|
|Visu.<br>✓<br>~~a~~|black-box around a “us-<br>able” prediction|black-box around a “usable”<br>prediction|adaptive|
|✗|not adaptive|limited adaptiveness|not black-box around a “us-|
||||able” prediction|



24 / 91 

## **Split Conformal Prediction: summary** 

# • **Simple** procedure which quantifies the uncertainty of **any** predictive model _A_[ˆ] by returning predictive regions 

- **Finite-sample** guarantees 

- **Distribution-free** as long as the data are exchangeable (and so are the scores) 

25 / 91 

## **Split Conformal Prediction: summary** 

- **Simple** procedure which quantifies the uncertainty of **any** predictive model _A_[ˆ] by returning predictive regions 

- **Finite-sample** guarantees 

- **Distribution-free** as long as the data are exchangeable (and so are the scores) 

- **Marginal** theoretical guarantee over the joint ( _X , Y_ ) distribution, and not con- 

   - ditional, i.e., no guarantee that for any _x_ : 

**==> picture [200 x 21] intentionally omitted <==**

25 / 91 

## **Split Conformal Prediction: summary** 

- **Simple** procedure which quantifies the uncertainty of **any** predictive model _A_[ˆ] by returning predictive regions 

- **Finite-sample** guarantees 

- **Distribution-free** as long as the data are exchangeable (and so are the scores) 

- **Marginal** theoretical guarantee over the joint ( _X , Y_ ) distribution, and not conditional, i.e., no guarantee that for any _x_ : 

**==> picture [200 x 21] intentionally omitted <==**

- _�→_ marginal also over the whole calibration set and the test point! 

25 / 91 

**Lab** ~~eee~~ 

**Figure 1:** Lab - CP - classification - with solution 

**==> picture [21 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
Link<br>**----- End of picture text -----**<br>


**Figure 2:** Lab - CP - classification - with parts to fill 

**==> picture [20 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
Link<br>**----- End of picture text -----**<br>


26 / 91 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method 

Intro II: Overview of some challenges in Conformal Prediction Advanced I: Towards conditional coverage Advanced II: Avoiding data splitting: full conformal and out-of-bags approaches Advanced III: Beyond exchangeability Applications & Methods I: Some case studies Applications & Methods II: Some methodological advances Concluding remarks 

Intro II: Overview of some challenges in Conformal Prediction Conditional coverage Data-splitting: Computational cost vs statistical power Beyond exchangeability 

## **Conditional coverage** 

Ultimately, we would love to get: 

**==> picture [221 x 20] intentionally omitted <==**

However: 

- _Xn_ +1-conditional validity is not possible (informatively) in full generality 

   - (hardness results) 

27 / 91 

## **Conditional coverage** 

Ultimately, we would love to get: 

**==> picture [221 x 20] intentionally omitted <==**

## However: 

- _Xn_ +1-conditional validity is not possible (informatively) in full generality 

   - (hardness results) 

- It is possible to aim for group-coditional validity, or asymptotic results, for example with universal quantile learner. 

27 / 91 

## **Conditional coverage** 

Ultimately, we would love to get: 

**==> picture [221 x 20] intentionally omitted <==**

However: 

- _Xn_ +1-conditional validity is not possible (informatively) in full generality (hardness results) 

- It is possible to aim for group-coditional validity, or asymptotic results, for example with universal quantile learner. 

- It is possible to achieve PAC-type results that hold with high probability 

   - w.r.t. the Cal set. 

27 / 91 

Intro II: Overview of some challenges in Conformal Prediction Conditional coverage Data-splitting: Computational cost vs statistical power Beyond exchangeability 

**==> picture [1954 x 1874] intentionally omitted <==**

**----- Start of picture text -----**<br>
Can we avoid splitting the data set? SCP CV+ Jackknife+<br>• Full Conformal Prediction<br>Nested Conformal Prediction<br>◦ avoids data splitting<br>• Jackknife+: (Barber et al., 2021b)<br>◦ Based on leave-one-out (LOO) residuals<br>Non exhaustive references.<br>**----- End of picture text -----**<br>


## **Avoiding data splitting: full conformal and out-of-bags approaches** 

## **SCP suffers from data splitting** : 

- lower statistical efficiency (lower model accuracy and higher predictive set size) 

- higher statistical variability 

28 / 91 

## **Avoiding data splitting: full conformal and out-of-bags approaches** 

SCP suffers from data splitting: 

- lower statistical efficiency (lower model accuracy and higher predictive set size) 

- higher statistical variability 

Can we avoid splitting the data set? 

- Full Conformal Prediction 

Statistical efficiency 

**==> picture [186 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
Computational efficiency<br>SCP CV+ Jackknife+ FCP<br>Nested Conformal Prediction<br>**----- End of picture text -----**<br>


   - avoids data splitting 

   - at the cost of many more model fits 

- Jackknife+: (Barber et al., 2021b) 

   - Based on leave-one-out (LOO) residuals 

28 / 91 

## **Avoiding data splitting: full conformal and out-of-bags approaches** 

SCP suffers from data splitting: 

- lower statistical efficiency (lower model accuracy and higher predictive set size) 

- higher statistical variability 

Can we avoid splitting the data set? 

- Full Conformal Prediction 

Statistical efficiency 

**==> picture [186 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
Computational efficiency<br>SCP CV+ Jackknife+ FCP<br>Nested Conformal Prediction<br>**----- End of picture text -----**<br>


   - avoids data splitting 

   - at the cost of many more model fits 

- Jackknife+: (Barber et al., 2021b) 

   - Based on leave-one-out (LOO) residuals 

Non exhaustive references. 

28 / 91 

Intro II: Overview of some challenges in Conformal Prediction Conditional coverage Data-splitting: Computational cost vs statistical power Beyond exchangeability 

## **Exchangeability does not hold in many practical applications** 

- CP requires exchangeable data points to ensure validity 

29 / 91 

## **Exchangeability does not hold in many practical applications** 

- CP requires exchangeable data points to ensure validity 

- ✗ Covariate shift, i.e. _LX_ changes but _LY |X_ stays constant 

   - ↬ (Tibshirani et al., 2019) (based on modeling and estimating the shifts, then reweighting) 

29 / 91 

## **Exchangeability does not hold in many practical applications** 

- CP requires exchangeable data points to ensure validity 

- ✗ Covariate shift, i.e. _LX_ changes but _LY |X_ stays constant 

   - ↬ (Tibshirani et al., 2019) (based on modeling and estimating the shifts, then reweighting) 

- ✗ Label shift, i.e. _LY_ changes but _LX |Y_ stays constant 

   - ↬ Similar approach by (Podkopaev and Ramdas, 2021). 

29 / 91 

## **Exchangeability does not hold in many practical applications** 

- CP requires exchangeable data points to ensure validity 

- ✗ Covariate shift, i.e. _LX_ changes but _LY |X_ stays constant 

   - ↬ (Tibshirani et al., 2019) (based on modeling and estimating the shifts, then reweighting) 

- ✗ Label shift, i.e. _LY_ changes but _LX |Y_ stays constant 

   - ↬ Similar approach by (Podkopaev and Ramdas, 2021). 

- ✗ Arbitrary distribution shift 

↬ see Cauchois et al. (2020) (distributionally robust optimization) Chernozhukov et al. (2018) (strongly mixing case), Barber et al. (2022) (quantifying non ex changeability) 

29 / 91 

## **Exchangeability does not hold in many practical applications** 

- CP requires exchangeable data points to ensure validity 

✗ Covariate shift, i.e. _LX_ changes but _LY |X_ stays constant 

   - ↬ (Tibshirani et al., 2019) (based on modeling and estimating the shifts, then reweighting) 

- ✗ Label shift, i.e. _LY_ changes but _LX |Y_ stays constant 

   - ↬ Similar approach by (Podkopaev and Ramdas, 2021). 

- ✗ Arbitrary distribution shift 

↬ see Cauchois et al. (2020) (distributionally robust optimization) Chernozhukov et al. (2018) (strongly mixing case), Barber et al. (2022) (quantifying non ex changeability) 

- ✗ Possibly many shifts, not only one 

29 / 91 

## **Summary:** _→_ **A more complete tutorial on conformal methods** 

**==> picture [400 x 242] intentionally omitted <==**

**----- Start of picture text -----**<br>
Conformal methods<br>• Marginal validity<br>Quantile regression no guarantee<br>• Model/distribution agnostic<br>• Finite sample<br>SCP Full CP JK/CV<br>+ no retraining + no split + balance cost<br>- split - prohibitive cost - requires stability or 1  − 2 α<br>Various scores<br>• Based on µ ˆ( x )<br>• Based on QR [�] ( x )<br>• Based on P [ˆ] ( y |x )<br>Limit 1: only marginal guarantee Limit 2: requires exch.<br>• Hardness of conditional coverage • Distribution shifts<br>• Asymptotic results / Adaptive • Online methods<br>methods<br>Case Studies<br>**----- End of picture text -----**<br>


30 / 91 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method Intro II: Overview of some challenges in Conformal Prediction 

Advanced I: Towards conditional coverage Advanced II: Avoiding data splitting: full conformal and out-of-bags approaches Advanced III: Beyond exchangeability Applications & Methods I: Some case studies Applications & Methods II: Some methodological advances Concluding remarks 

Advanced I: Towards conditional coverage 

On distribution-free _X_ -conditional validity Impact of the calibration set on the coverage 

## **Definition of distribution-free features conditional validity** 

_Cα_ = estimated predictive set based on _n_ data points. 

**==> picture [380 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
Distribution-free X -conditional validity<br>�<br>Cα achieves distribution-free X -conditional validity if:<br>• for any distribution D ,<br>• for any associated exchangeable joint distribution D [exch][(] [n] [+1)] ,<br>we have that:<br>a.s.<br>P D exch( n +1) Yn +1 ∈ C [�] α  ( Xn +1)  |Xn +1 ≥ 1  − α.<br>� �<br>**----- End of picture text -----**<br>


31 / 91 

**==> picture [1630 x 1766] intentionally omitted <==**

## **Informative conditional coverage as such is impossible** 

## **Impossibility results Vovk (2012); Lei and Wasserman (2014)** 

If _C_[�] _α_ is distribution-free _X_ -conditionally valid, then, for any _D_ , for _DX_ –almost all _DX_ –non-atoms _x ∈X_ , it holds: � P _D⊗_ ( _n_ ) mes _Cα_ ( _x_ ) = _∞ ≥_ 1 _− α._ � � � � 

Analogous statement is also available for the classification framework. 

32 / 91 

**==> picture [1630 x 1766] intentionally omitted <==**

## **Informative conditional coverage as such is impossible** 

**Impossibility results Vovk (2012); Lei and Wasserman (2014)** 

**==> picture [349 x 62] intentionally omitted <==**

_�→_ distribution-free _X_ -conditional hardness result applies beyond CP 

Analogous statement is also available for the classification framework. 

32 / 91 

**==> picture [1630 x 1766] intentionally omitted <==**

## **Informative conditional coverage as such is impossible** 

## **Impossibility results Vovk (2012); Lei and Wasserman (2014)** 

**==> picture [349 x 62] intentionally omitted <==**

_�→_ distribution-free _X_ -conditional hardness result applies beyond CP 

- _�→ X_ -conditional estimators are overly large even on easy cases 

Analogous statement is also available for the classification framework. 

32 / 91 

## **Informative conditional coverage as such is impossible** 

## **Impossibility results Vovk (2012); Lei and Wasserman (2014)** 

**==> picture [349 x 62] intentionally omitted <==**

- _�→_ distribution-free _X_ -conditional hardness result applies beyond CP 

- _�→ X_ -conditional estimators are overly large even on easy cases 

- _�→_ the lower bound is tight 

## **Naive estimator** 

- _Cα_ ( _·_ ; _ξ_ ) _≡Y_ 1 _{ξ ≤_ 1 _− α}_ + _∅_ 1 _{ξ > α}_ , where _ξ ∼U_ ([0 _,_ 1]). 

Analogous statement is also available for the classification framework. 

32 / 91 

**==> picture [1608 x 1794] intentionally omitted <==**

**----- Start of picture text -----**<br>
�→<br>**----- End of picture text -----**<br>


## **Weaker notion of** _X_ **-conditional validity (Barber et al., 2021a)** 

**distribution-free** (1 _− α, δ_ ) **–** _X_ **-conditional validity** 

Let _δ >_ 0 be a tolerance level. An estimator _C_[�] _α_ achieves distribution-free (1 _− α, δ_ )– _X_ -conditional validity if for any distribution _D_ , for any X _⊆X_ such that P _DX_ ( _X ∈_ X) _≥ δ_ , and for any associated exchangeable joint distribution _D_[exch(] _[n]_[+1)] , we have: P _D_ exch( _n_ +1) _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _|Xn_ +1 _∈_ X _≥_ 1 _− α._ � � 

33 / 91 

## **Weaker notion of** _X_ **-conditional validity (Barber et al., 2021a)** 

**distribution-free** (1 _− α, δ_ ) **–** _X_ **-conditional validity** 

Let _δ >_ 0 be a tolerance level. 

**==> picture [349 x 77] intentionally omitted <==**

**Informal theorem (lower bound on** (1 _− α, δ_ ) **–** _X_ **-cond. valid efficiency)** An estimator achieving (1 _− α, δ_ )– _X_ -conditional validity can not be more efficient than an estimator achieving **distribution-free marginal validity at the level** 1 _− αδ_ . 

- _�→_ In practice, consider small _δ →_ unefficient predictive sets. 

33 / 91 

**Getting closer to** _X_ **-conditional coverage** 

34 / 91 

**Getting closer to** _X_ **-conditional coverage** 

## • Approximate conditional coverage 

- _�→_ Romano et al. (2020a); Guan (2022); Jung et al. (2023); Gibbs et al. (2023) Target P( _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _|Xn_ +1 _∈R_ ( _x_ )) _≥_ 1 _− α_ 

Non exhaustive references. 

34 / 91 

## **Getting closer to** _X_ **-conditional coverage** 

- Approximate conditional coverage 

   - _�→_ Romano et al. (2020a); Guan (2022); Jung et al. (2023); Gibbs et al. (2023) Target P( _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _|Xn_ +1 _∈R_ ( _x_ )) _≥_ 1 _− α_ 

- Asymptotic (with the sample size) conditional coverage 

   - _�→_ Romano et al. (2019); Kivaranovic et al. (2020); Chernozhukov et al. 

(2021); Sesia and Romano (2021); Izbicki et al. (2022) 

Non exhaustive references. 

34 / 91 

## **Getting closer to** _X_ **-conditional coverage** 

- Approximate conditional coverage 

   - _�→_ Romano et al. (2020a); Guan (2022); Jung et al. (2023); Gibbs et al. (2023) Target P( _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _|Xn_ +1 _∈R_ ( _x_ )) _≥_ 1 _− α_ 

- Asymptotic (with the sample size) conditional coverage 

   - _�→_ **Romano et al. (2019)** ; Kivaranovic et al. (2020); Chernozhukov et al. (2021); Sesia and Romano (2021); Izbicki et al. (2022) 

Non exhaustive references. 

34 / 91 

Advanced I: Towards conditional coverage On distribution-free _X_ -conditional validity Impact of the calibration set on the coverage 

## **Probably Approximately Correct bounds on calibration-conditional coverage (Vovk, 2012; Bian and Barber, 2023)** 

**==> picture [380 x 93] intentionally omitted <==**

**----- Start of picture text -----**<br>
calibration conditional validity of SCP<br>SCP outputs C [�] α such that for any distribution D and any 0  < δ ≤ 0 . 5:<br>P D⊗ ( n +1) P D Yn +1 ∈/ C [�] n,α  ( Xn +1)  |  ( Xi , Yi ) [n] i =1 ≤ α  + log(1 /δ ) ≥ 1 −δ.<br>� � � � 2#Cal �<br>**----- End of picture text -----**<br>


- _�→_ controls the deviation of miscoverage with respect to the nominal level of a predictive set built on a given calibration set. 

35 / 91 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method 

Intro II: Overview of some challenges in Conformal Prediction 

Advanced I: Towards conditional coverage 

Advanced II: Avoiding data splitting: full conformal and out-of-bags approaches Advanced III: Beyond exchangeability 

Applications & Methods I: Some case studies 

Applications & Methods II: Some methodological advances 

Concluding remarks 

Advanced II: Avoiding data splitting: full conformal and out-of-bags approaches Full Conformal Prediction Jackknife+ 

## **Splitting the data might not be desired** 

## **SCP suffers from data splitting** : 

- lower statistical efficiency (lower model accuracy and higher predictive set size) 

- higher statistical variability 

36 / 91 

## **Splitting the data might not be desired** 

SCP suffers from data splitting: 

- lower statistical efficiency (lower model accuracy and higher predictive set size) 

- higher statistical variability 

Can we avoid splitting the data set? 

36 / 91 

**==> picture [1758 x 1868] intentionally omitted <==**

**----- Start of picture text -----**<br>
✗ A [ˆ] obtained w. the training set<br>“Naive Idea” sets with<br>Assume A interpolates:<br>• A [ˆ]  =  A  (( x 1 , y 1) , . . . ,  ( xn,<br>• A [ˆ] ( xk )  − yk = 0 for any k<br>**----- End of picture text -----**<br>


## **The naive idea does not enjoy valid coverage (even empirically)** 

## • A naive idea: 

_◦_ Get _A_[ˆ] by training the algorithm _A_ on _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ . 

**==> picture [1631 x 1820] intentionally omitted <==**

## **The naive idea does not enjoy valid coverage (even empirically)** 

## • A naive idea: 

_◦_ Get _A_[ˆ] by training the algorithm _A_ on _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ . 

_◦_ compute the empirical quantile _q_ 1 _−α_ ( _S_ ) of the set of scores 

**==> picture [139 x 20] intentionally omitted <==**

37 / 91 

**==> picture [1630 x 1819] intentionally omitted <==**

## **The naive idea does not enjoy valid coverage (even empirically)** 

## • A naive idea: 

_◦_ Get _A_[ˆ] by training the algorithm _A_ on _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ . 

_◦_ compute the empirical quantile _q_ 1 _−α_ ( _S_ ) of the set of scores 

**==> picture [139 x 20] intentionally omitted <==**

**==> picture [255 x 19] intentionally omitted <==**

37 / 91 

## **The naive idea does not enjoy valid coverage (even empirically)** 

## • A naive idea: 

_◦_ Get _A_[ˆ] by training the algorithm _A_ on _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ . 

_◦_ compute the empirical quantile _q_ 1 _−α_ ( _S_ ) of the set of scores 

**==> picture [255 x 49] intentionally omitted <==**

**==> picture [332 x 14] intentionally omitted <==**

## **“Naive Idea” sets with an interpolating algorithm** 

Assume _A_ interpolates: 

**==> picture [131 x 13] intentionally omitted <==**

**==> picture [151 x 13] intentionally omitted <==**

_⇒_ Naive method above _(with MAE score functions)_ outputs _{A_[ˆ] ( _Xn_ +1) _}_ (a single point) for any new test point! 

37 / 91 

## **Full CP (Vovk et al., 2005) does not discard training points!** 

- Full Conformal Prediction 

_◦_ avoids data splitting 

38 / 91 

## **Full CP (Vovk et al., 2005) does not discard training points!** 

- Full Conformal Prediction 

_◦_ avoids data splitting 

- at the cost of many more model fits 

38 / 91 

## **Full CP (Vovk et al., 2005) does not discard training points!** 

- Full Conformal Prediction 

   - avoids data splitting 

   - at the cost of many more model fits 

• **Idea** : the most probable labels _Yn_ +1 live in _Y_ , and have a low enough conformity score. By looping over all possible _y ∈Y_ , the ones leading to the smallest conformity scores will be found. 

38 / 91 

**==> picture [1833 x 1862] intentionally omitted <==**

**----- Start of picture text -----**<br>
i =1<br>and compute their 1  − α empirical quantile q 1 −<br>Output the set y such that s Xn +1 , y ; A [ˆ] y ≤ q 1<br>� � �<br>✓ Test point treated in the same way than train<br>✓ Any score works<br>✗ Computationally costly<br>**----- End of picture text -----**<br>


## **Full CP: recovering exchangeability** 

For any candidate ( _Xn_ +1 _, y_ ): 

1. Get _A_[ˆ] _y_ by training _A_ on _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _} ∪{_ ( _Xn_ +1 _, y_ ) _}_ 

39 / 91 

## **Full CP: recovering exchangeability** 

For any candidate ( _Xn_ +1 _, y_ ): 

1. Get _A_[ˆ] _y_ by training _A_ on _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _} ∪{_ ( _Xn_ +1 _, y_ ) _}_ 

2. Obtain a set of training scores 

**==> picture [243 x 22] intentionally omitted <==**

**==> picture [270 x 21] intentionally omitted <==**

39 / 91 

## **Full CP: recovering exchangeability** 

For any candidate ( _Xn_ +1 _, y_ ): 

1. Get _A_[ˆ] _y_ by training _A_ on _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _} ∪{_ ( _Xn_ +1 _, y_ ) _}_ 

2. Obtain a set of training scores 

**==> picture [243 x 22] intentionally omitted <==**

**==> picture [305 x 50] intentionally omitted <==**

39 / 91 

## **Full CP: recovering exchangeability** 

For any candidate ( _Xn_ +1 _, y_ ): 

1. Get _A_[ˆ] _y_ by training _A_ on _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _} ∪{_ ( _Xn_ +1 _, y_ ) _}_ 

2. Obtain a set of training scores 

**==> picture [243 x 22] intentionally omitted <==**

**==> picture [270 x 21] intentionally omitted <==**

**==> picture [305 x 21] intentionally omitted <==**

✓ Test point treated in the same way than train points 

39 / 91 

## **Full CP: recovering exchangeability** 

For any candidate ( _Xn_ +1 _, y_ ): 

1. Get _A_[ˆ] _y_ by training _A_ on _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _} ∪{_ ( _Xn_ +1 _, y_ ) _}_ 

2. Obtain a set of training scores 

**==> picture [243 x 22] intentionally omitted <==**

**==> picture [270 x 21] intentionally omitted <==**

**==> picture [305 x 21] intentionally omitted <==**

✓ Test point treated in the same way than train points 

✓ Any score works 

39 / 91 

## **Full CP: recovering exchangeability** 

For any candidate ( _Xn_ +1 _, y_ ): 

1. Get _A_[ˆ] _y_ by training _A_ on _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _} ∪{_ ( _Xn_ +1 _, y_ ) _}_ 

2. Obtain a set of training scores 

**==> picture [243 x 22] intentionally omitted <==**

**==> picture [270 x 21] intentionally omitted <==**

**==> picture [305 x 21] intentionally omitted <==**

✓ Test point treated in the same way than train points 

✓ Any score works 

- ✗ Computationally costly 

39 / 91 

**==> picture [1785 x 1875] intentionally omitted <==**

**----- Start of picture text -----**<br>
If the algorithm A : ( U 1 , . . . , Un ) �→<br>exchangeable, then S 1 , . . . , Sn +1 are<br>Si := s Xi ,<br>�<br>Moreover<br>Yn +1 ∈ C [�] α [Full] ( Xn +1) := y such that<br>�<br>⇔ s Xn +1 , Yn +1; A [ˆ] Yn +1 ≤ q 1<br>� �<br>⇔ Sn +1 ≤ q 1 −α ( S 1 , . . . , Sn, Sn<br>**----- End of picture text -----**<br>


## **Full CP: theoretical foundation** 

## **Symmetrical algorithm** 

A deterministic algorithm _A_ : ( _U_ 1 _, . . . , Un_ ) _�→ A_[ˆ] is symmetric if for any permutation _σ_ of �1 _, n_ �: _A_ ( _U_ 1 _, . . . , Un_ )[a.s.] = _A_ � _Uσ_ (1) _, . . . , Uσ_ ( _n_ )� _._ 

40 / 91 

**==> picture [1655 x 1741] intentionally omitted <==**

**----- Start of picture text -----**<br>
⇔<br>**----- End of picture text -----**<br>


## **Full CP: theoretical foundation** 

**Symmetrical algorithm** A deterministic algorithm _A_ : ( _U_ 1 _, . . . , Un_ ) _�→ A_[ˆ] is symmetric if for any permutation _σ_ of �1 _, n_ �: _A_ ( _U_ 1 _, . . . , Un_ )[a.s.] = _A_ � _Uσ_ (1) _, . . . , Uσ_ ( _n_ )� _._ 

**==> picture [380 x 93] intentionally omitted <==**

**----- Start of picture text -----**<br>
Exchangeable scores<br>If the algorithm A : ( U 1 , . . . , Un ) �→ A [ˆ] is symmetric, and ( Xi , Yi ) [n] i =1 [+1] [are]<br>exchangeable, then S 1 , . . . , Sn +1 are exchangeable, with<br>Si := s Xi , Yi ; A [ˆ] Yn +1 .<br>� �<br>**----- End of picture text -----**<br>


40 / 91 

## **Full CP: theoretical foundation** 

## **Symmetrical algorithm** 

A deterministic algorithm _A_ : ( _U_ 1 _, . . . , Un_ ) _�→ A_[ˆ] is symmetric if for any permutation _σ_ of �1 _, n_ �: _A_ ( _U_ 1 _, . . . , Un_ )[a.s.] = _A_ � _Uσ_ (1) _, . . . , Uσ_ ( _n_ )� _._ 

## **Exchangeable scores** 

If the algorithm _A_ : ( _U_ 1 _, . . . , Un_ ) _�→ A_[ˆ] is symmetric, and ( _Xi , Yi_ ) _[n] i_ =1[+1][are] exchangeable, then _S_ 1 _, . . . , Sn_ +1 are exchangeable, with 

**==> picture [114 x 20] intentionally omitted <==**

## Moreover 

**==> picture [338 x 62] intentionally omitted <==**

40 / 91 

## **Full CP: theoretical guarantees** 

Full CP enjoys finite sample guarantees proved in Vovk et al. (2005). 

**Marginal validity of Full CP Vovk et al. (2005)** Suppose that (i) ( _Xi , Yi_ ) _[n] i_ =1[+1][are][exchangeable][,] (ii) the algorithm _A_ is symmetric. Full CP applied on ( _Xi , Yi_ ) _[n] i_ =1 _[∪{][X][n]_[+1] _[}]_[outputs] _[C]_[�] _[α]_[ (] _[·]_[)][such][that:] P _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _≥_ 1 _− α._ � � Additionally, if the scores are a.s. distinct: 1 P _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _≤_ 1 _− α_ + � � _n_ + 1 _[.]_ 

41 / 91 

## **Full CP: theoretical guarantees** 

Full CP enjoys finite sample guarantees proved in Vovk et al. (2005). 

**Marginal validity of Full CP Vovk et al. (2005)** 

Suppose that (i) ( _Xi , Yi_ ) _[n] i_ =1[+1][are][exchangeable][,] (ii) the algorithm _A_ is symmetric. Full CP applied on ( _Xi , Yi_ ) _[n] i_ =1 _[∪{][X][n]_[+1] _[}]_[outputs] _[C]_[�] _[α]_[ (] _[·]_[)][such][that:] P _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1) _≥_ 1 _− α._ � � 

Additionally, if the scores are a.s. distinct: 

**==> picture [192 x 24] intentionally omitted <==**

**==> picture [300 x 21] intentionally omitted <==**

41 / 91 

## **Interpolation regime** 

**FCP sets with an interpolating algorithm** Assume _A_ interpolates: 

- _A_[ˆ] = _A_ (( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn_ +1 _, yn_ +1)) 

- _A_[ˆ] ( _xk_ ) _− yk_ = 0 for any _k ∈_ �1 _, n_ + 1� 

**Interpolation regime** 

## **FCP sets with an interpolating algorithm** 

## Assume _A_ interpolates: 

   - _A_[ˆ] = _A_ (( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn_ +1 _, yn_ +1)) 

   - _A_[ˆ] ( _xk_ ) _− yk_ = 0 for any _k ∈_ �1 _, n_ + 1� 

- _⇒_ Full Conformal Prediction _(with standard score functions)_ outputs _Y_ (the whole label space) for any new test point! 

42 / 91 

Advanced II: Avoiding data splitting: full conformal and out-of-bags approaches Full Conformal Prediction Jackknife+ 

**==> picture [1609 x 1782] intentionally omitted <==**

## **Jackknife: the naive idea does not enjoy valid coverage** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 37] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

43 / 91 

**==> picture [1608 x 1780] intentionally omitted <==**

## **Jackknife: the naive idea does not enjoy valid coverage** 

- Based on leave-one-out (LOO) residuals 

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- • Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) • LOO scores _S_ = _|A_[ˆ] _−i_ ( _Xi_ ) _− Yi |_ � � _i[∪{]_[+] _[∞}]_ 

**==> picture [85 x 37] intentionally omitted <==**

(in standard mean regression) 

43 / 91 

**==> picture [1608 x 1780] intentionally omitted <==**

## **Jackknife: the naive idea does not enjoy valid coverage** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 37] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- • Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) • LOO scores _S_ = _|A_[ˆ] _−i_ ( _Xi_ ) _− Yi |_ (in standard mean regression) � � _i[∪{]_[+] _[∞}]_ 

- Get _A_[ˆ] by training _A_ on _Dn_ 

43 / 91 

**==> picture [1608 x 1780] intentionally omitted <==**

## **Jackknife: the naive idea does not enjoy valid coverage** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 37] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

• LOO scores _S_ = _|A_[ˆ] _−i_ ( _Xi_ ) _− Yi |_ (in standard mean regression) � � _i[∪{]_[+] _[∞}]_ 

- Get _A_[ˆ] by training _A_ on _Dn_ 

ˆ • Build the predictive interval: _A_ ( _Xn_ +1) _± q_ 1 _−α_ ( _S_ ) � � 

43 / 91 

## **Jackknife: the naive idea does not enjoy valid coverage** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 37] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

• LOO scores _S_ = _|A_[ˆ] _−i_ ( _Xi_ ) _− Yi |_ (in standard mean regression) � � _i[∪{]_[+] _[∞}]_ • Get _A_[ˆ] by training _A_ on _Dn_ ˆ • Build the predictive interval: _A_ ( _Xn_ +1) _± q_ 1 _−α_ ( _S_ ) � � 

## **Warning** 

No guarantee on the prediction of _A_[ˆ] with scores based on ( _A_[ˆ] _−i_ ) _i_ , without assuming a form of **stability** on _A_ . 

43 / 91 

**Jackknife+ (Barber et al., 2021b)** ~~ee~~ 

44 / 91 

**==> picture [1608 x 1781] intentionally omitted <==**

## **Jackknife+ (Barber et al., 2021b)** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

45 / 91 

**==> picture [1608 x 1781] intentionally omitted <==**

## **Jackknife+ (Barber et al., 2021b)** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

• LOO predictions / predictive intervals ˆ _S_ up _/_ down = � _A−i_ ( _Xn_ +1) _± |A_ ˆ _−i_ ( _Xi_ ) _− Yi |_ � _i[∪{±∞}]_ (in standard mean regression) 

45 / 91 

**==> picture [1608 x 1781] intentionally omitted <==**

## **Jackknife+ (Barber et al., 2021b)** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

• LOO predictions / predictive intervals ˆ _S_ up _/_ down = � _A−i_ ( _Xn_ +1) _± |A_ ˆ _−i_ ( _Xi_ ) _− Yi |_ � _i[∪{±∞}]_ (in standard mean regression) 

- Build the predictive interval: [ _qα,_ inf( _S_ down); _q_ 1 _−α_ ( _S_ up)] 

Recall _qβ,_ inf( _X_ 1 _, . . . , Xk_ ) := _⌊β × k⌋_ smallest value of ( _X_ 1 _, . . . , Xk_ ) 

45 / 91 

## **Jackknife+ (Barber et al., 2021b)** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

• LOO predictions / predictive intervals ˆ _S_ up _/_ down = � _A−i_ ( _Xn_ +1) _± |A_ ˆ _−i_ ( _Xi_ ) _− Yi |_ � _i[∪{±∞}]_ (in standard mean regression) 

- Build the predictive interval: [ _qα,_ inf( _S_ down); _q_ 1 _−α_ ( _S_ up)] 

**==> picture [264 x 21] intentionally omitted <==**

**----- Start of picture text -----**<br>
Marginal validity of Jackknife+ Barber et al. (2021b)<br>**----- End of picture text -----**<br>


If _Dn ∪_ ( _Xn_ +1 _, Yn_ +1) are exchangeable and _A_ is symmetric: P( _Yn_ +1 _∈ C_[�] _α_ ( _Xn_ +1)) _≥_ 1 _−_ 2 _α_ . 

Recall _qβ,_ inf( _X_ 1 _, . . . , Xk_ ) := _⌊β × k⌋_ smallest value of ( _X_ 1 _, . . . , Xk_ ) 

45 / 91 

## **General overview** 

Statistical efficiency 

**==> picture [296 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
Computational efficiency<br>SCP CV+ Jackknife+ FCP<br>**----- End of picture text -----**<br>


Nested Conformal Prediction 

46 / 91 

## **General overview** 

Statistical efficiency 

**==> picture [296 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
Computational efficiency<br>SCP CV+ Jackknife+ FCP<br>**----- End of picture text -----**<br>


Nested Conformal Prediction 

- Generalized framework encapsulating out-of-sample methods: Nested CP (Gupta et al., 2022) _→_ extends _JK+/CV+ for any score._ 

46 / 91 

## **General overview** 

Statistical efficiency 

**==> picture [296 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
Computational efficiency<br>SCP CV+ Jackknife+ FCP<br>**----- End of picture text -----**<br>


Nested Conformal Prediction 

- Generalized framework encapsulating out-of-sample methods: Nested CP (Gupta et al., 2022) _→_ extends _JK+/CV+ for any score._ 

- Accelerating FCP: Nouretdinov et al. (2001); Lei (2019); Ndiaye and Takeuchi (2019); Cherubin et al. (2021); Ndiaye and Takeuchi (2022); Ndiaye (2022) 

Non exhaustive references. 

46 / 91 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method 

Intro II: Overview of some challenges in Conformal Prediction Advanced I: Towards conditional coverage 

Advanced II: Avoiding data splitting: full conformal and out-of-bags approaches Advanced III: Beyond exchangeability Applications & Methods I: Some case studies 

Applications & Methods II: Some methodological advances Concluding remarks 

## **Exchangeability does not hold in many practical applications** 

- CP requires exchangeable data points to ensure validity 

47 / 91 

## **Exchangeability does not hold in many practical applications** 

- CP requires exchangeable data points to ensure validity 

✗ Covariate shift, i.e. _LX_ changes but _LY |X_ stays constant 

47 / 91 

## **Exchangeability does not hold in many practical applications** 

- CP requires exchangeable data points to ensure validity 

✗ Covariate shift, i.e. _LX_ changes but _LY |X_ stays constant 

- ✗ Label shift, i.e. _LY_ changes but _LX |Y_ stays constant 

47 / 91 

## **Exchangeability does not hold in many practical applications** 

- CP requires exchangeable data points to ensure validity 

✗ Covariate shift, i.e. _LX_ changes but _LY |X_ stays constant 

- ✗ Label shift, i.e. _LY_ changes but _LX |Y_ stays constant 

- ✗ Arbitrary distribution shift 

47 / 91 

## **Exchangeability does not hold in many practical applications** 

- CP requires exchangeable data points to ensure validity 

- ✗ Covariate shift, i.e. _LX_ changes but _LY |X_ stays constant 

- ✗ Label shift, i.e. _LY_ changes but _LX |Y_ stays constant 

- ✗ Arbitrary distribution shift 

- ✗ Possibly many shifts, not only one 

47 / 91 

## **Covariate shift (Tibshirani et al., 2019)** 

• Setting: _i.i.d. ◦_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _∼ PX × PY |X ◦_ ( _Xn_ +1 _, Yn_ +1) _∼ P_[˜] _X × PY |X_ 

48 / 91 

## **Covariate shift (Tibshirani et al., 2019)** 

- Setting: 

_i.i.d. ◦_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _∼ PX × PY |X ◦_ ( _Xn_ +1 _, Yn_ +1) _∼ P_[˜] _X × PY |X_ 

- Idea: give more importance to calibration points that are closer in distribution to the test point 

Similar approach for Label shift (Podkopaev and Ramdas, 2021). 

48 / 91 

## **Covariate shift (Tibshirani et al., 2019)** 

- Setting: 

_i.i.d. ◦_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _∼ PX × PY |X ◦_ ( _Xn_ +1 _, Yn_ +1) _∼ P_[˜] _X × PY |X_ 

- Idea: give more importance to calibration points that are closer in distribution to the test point 

- In practice: 

1. estimate the likelihood ratio _w_ ( _Xi_ ) =[d] d _[P] P_[ ˜] _[X] X_[ (] ( _[X] X[i] i_[)] ) 

Similar approach for Label shift (Podkopaev and Ramdas, 2021). 

48 / 91 

## **Covariate shift (Tibshirani et al., 2019)** 

- Setting: 

_i.i.d. ◦_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _∼ PX × PY |X_ 

**==> picture [123 x 14] intentionally omitted <==**

- Idea: give more importance to calibration points that are closer in distribution to the test point 

- In practice: 

**==> picture [201 x 18] intentionally omitted <==**

**==> picture [227 x 19] intentionally omitted <==**

Similar approach for Label shift (Podkopaev and Ramdas, 2021). 

48 / 91 

**Covariate shift (Tibshirani et al., 2019)** 

- Setting: 

**==> picture [169 x 29] intentionally omitted <==**

- Idea: give more importance to calibration points that are closer in distribution to the test point 

- In practice: 

**==> picture [227 x 37] intentionally omitted <==**

**==> picture [100 x 14] intentionally omitted <==**

**==> picture [237 x 30] intentionally omitted <==**

Similar approach for Label shift (Podkopaev and Ramdas, 2021). 

48 / 91 

**Generalizations** 

- Arbitrary distribution shift: Cauchois et al. (2020) leverages ideas from the distributionally robust optimization literature 

- Two major general theoretical results beyond exchangeability: 

49 / 91 

## **Generalizations** 

- Arbitrary distribution shift: Cauchois et al. (2020) leverages ideas from the distributionally robust optimization literature 

- Two major general theoretical results beyond exchangeability: 

   - Chernozhukov et al. (2018) 

      - _�→_ If the learnt model is accurate and the data noise is strongly mixing, then CP is valid asymptotically ✓ 

49 / 91 

**Generalizations** 

- Arbitrary distribution shift: Cauchois et al. (2020) leverages ideas from the distributionally robust optimization literature 

- Two major general theoretical results beyond exchangeability: 

   - Chernozhukov et al. (2018) 

_�→_ If the learnt model is accurate and the data noise is strongly mixing, then CP is valid asymptotically ✓ 

- Barber et al. (2022) 

   - _�→_ Quantifies the coverage loss depending on the strength of exchangeability violation 

**==> picture [250 x 16] intentionally omitted <==**

- _�→_ proposed algorithm: reweighting again! 

e.g., in a temporal setting, give higher weights to more recent points. 

49 / 91 

## **Online setting** 

- Data: _T_ 0 random variables ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _XT_ 0 _, YT_ 0) in R _[d] ×_ R 

- Aim: predict the response values as well as predictive intervals for _T_ 1 subsequent observations _XT_ 0+1 _, . . . , XT_ 0+ _T_ 1 sequentially: at any prediction step _t ∈_ � _T_ 0 + 1 _, T_ 0 + _T_ 1�, _Yt−T_ 0 _, . . . , Yt−_ 1 have been revealed 

- Build the smallest interval _C_[�] _α[t]_[such][that:] 

**==> picture [255 x 21] intentionally omitted <==**

often relaxed in: 

**==> picture [174 x 34] intentionally omitted <==**

50 / 91 

## **Online setting** 

- Data: _T_ 0 random variables ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _XT_ 0 _, YT_ 0) in R _[d] ×_ R 

- Aim: predict the response values as well as predictive intervals for _T_ 1 subsequent observations _XT_ 0+1 _, . . . , XT_ 0+ _T_ 1 sequentially: at any prediction step _t ∈_ � _T_ 0 + 1 _, T_ 0 + _T_ 1�, _Yt−T_ 0 _, . . . , Yt−_ 1 have been revealed 

- Build the smallest interval _C_[�] _α[t]_[such][that:] 

**==> picture [255 x 21] intentionally omitted <==**

often relaxed in: 

**==> picture [174 x 34] intentionally omitted <==**

- ⇝ More during the case study! 

50 / 91 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method 

Intro II: Overview of some challenges in Conformal Prediction Advanced I: Towards conditional coverage Advanced II: Avoiding data splitting: full conformal and out-of-bags approaches Advanced III: Beyond exchangeability Applications & Methods I: Some case studies Applications & Methods II: Some methodological advances Concluding remarks 

## Applications & Methods I: Some case studies 

Healthcare Electricity 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

- Medical application 

- Image based task 

- Pixel by pixel analysis ⇝ 

   - applications to segmentation for self-driving cars 

51 / 91 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

- Medical application 

- Image based task 

• Pixel by pixel analysis ⇝ applications to segmentation for self-driving cars 

1. **Task** : _Image to Image regression_ – for each pixel of an image, predict a real valued output from the entire image. 

2. **UQ Goal:** provide a predictive interval for each pixel, such that the output is in the interval at least 90% of the time. 

51 / 91 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

- Medical application 

- Image based task 

• Pixel by pixel analysis ⇝ applications to segmentation for self-driving cars 

1. **Task** : _Image to Image regression_ – for each pixel of an image, predict a real valued output from the entire image. 

2. **UQ Goal:** provide a predictive interval for each pixel, such that the output is in the interval at least 90% of the time. 

**Figure 3:** Image from Angelopoulos et al. (2022b) 

51 / 91 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

## **Method:** 

1. Split conformal prediction method - isolate calibration set 

2. On the proper training set, learn: 

   - ˆ 

   - • Mean regressor - _µ_ : R _[NM] →_ [0; 1] 

52 / 91 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

## **Method:** 

1. Split conformal prediction method - isolate calibration set 

2. On the proper training set, learn: 

   - ˆ 

   - • Mean regressor - _µ_ : R _[NM] →_ [0; 1] 

   - Heuristic notion of uncertainty: _u_ ˜ _, ℓ_[˜] : R _[NM] →_ [0; 1], such that 

[ _µ_ ˆ( _X_ ) _− ℓ_[˜] ( _X_ ); ˆ _µ_ ( _X_ ) + _u_ ˜( _X_ )] 

_→_ 3 regressors are used 

- 4 techniques are experimented for these regressors, including QR. 

52 / 91 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

## **Method:** 

1. Split conformal prediction method - isolate calibration set 

2. On the proper training set, learn: 

   - ˆ 

   - • Mean regressor - _µ_ : R _[NM] →_ [0; 1] 

   - Heuristic notion of uncertainty: _u_ ˜ _, ℓ_[˜] : R _[NM] →_ [0; 1], such that 

[ _µ_ ˆ( _X_ ) _− ℓ_[˜] ( _X_ ); ˆ _µ_ ( _X_ ) + _u_ ˜( _X_ )] 

_→_ 3 regressors are used 

      - 4 techniques are experimented for these regressors, including QR. 

3. Calibration step: leverage the calibration set. 

   - In spirit, almost equivalent to CQR but with a multiplicative form. 

   - Precisely, relies on RCPS (Bates et al., 2021a) 

52 / 91 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

## **Method:** 

1. Split conformal prediction method - isolate calibration set 

2. On the proper training set, learn: 

   - ˆ 

   - • Mean regressor - _µ_ : R _[NM] →_ [0; 1] 

   - Heuristic notion of uncertainty: _u_ ˜ _, ℓ_[˜] : R _[NM] →_ [0; 1], such that 

[ _µ_ ˆ( _X_ ) _− ℓ_[˜] ( _X_ ); ˆ _µ_ ( _X_ ) + _u_ ˜( _X_ )] 

_→_ 3 regressors are used 

      - 4 techniques are experimented for these regressors, including QR. 

3. Calibration step: leverage the calibration set. 

   - In spirit, almost equivalent to CQR but with a multiplicative form. 

   - Precisely, relies on RCPS (Bates et al., 2021a) 

## **Guarantee:** 

P [E [Average miscoverage on all pixels of a test image _|_ Cal] _≥ α_ ] _≤ δ_ 

- _→_ Marginal validity on the test, with high probability w.r.t. the calibration set. 

52 / 91 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

## How do you understand that? 

53 / 91 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

- Not a conditional coverage claim! 

- The statement is on-average on the test point - easy or hard. 

- Hard problem (impossibility results!) 

- Introduce metrics to see _if_ and _on_ 

How do you understand that? 

_which underlying regressors_ such problem happens. 

53 / 91 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

**Example of such metrics** (see also Feldman et al., 2021) **:** 

- Link between the size of the PI and the coverage level _−→_ 

54 / 91 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

## **Example of such metrics** (see also Feldman et al., 2021) **:** 

## • Link between the size of the PI and the coverage level _−→_ • Localization of the errors _↓_ 

## **Figure 4:** All images from Angelopoulos et al. (2022b) 

54 / 91 

## **– Image to Image regression with DF-UQ Angelopoulos et al. (2022b)** 

**Example of such metrics** (see also Feldman et al., 2021) **:** 

- Link between the size of the PI and 

   - the coverage level _−→_ 

- Localization of the errors _↓_ 

**Figure 4:** All images from Angelopoulos et al. (2022b) 

## **Take aways:** 

- Elegant application of SCP with CQR type score 

- Test marginal and calibration + train conditional validity guarantees with HP 

- Main problem is Test conditionality _→_ look at metrics to evaluate which 

   - methods performs best! 

54 / 91 

Applications & Methods I: Some case studies Healthcare 

Electricity 

**==> picture [1666 x 1807] intentionally omitted <==**

**----- Start of picture text -----**<br>
2016<br>To which extent<br>�→ forecasts<br>**----- End of picture text -----**<br>


## **Forecasting French spot electricity prices** 

Hourly day-ahead market prices (between producers and suppliers) 

55 / 91 

## **Forecasting French spot electricity prices** 

## Hourly day-ahead market prices (between producers and suppliers) 

**==> picture [377 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
3000<br>2500<br>2000<br>1500<br>1000 2 017 − 01 2017 − 07 2018 − 01 2018 − 07 2019 − 01 2019 − 07 2020 − 01 2020 − 07 2021 − 01<br>Date<br>500<br>0<br>2016 2017 2018 2019 2020 2021 2022 2023 2024<br>Date<br>/MWh)<br>€(<br>price<br>Spot<br>**----- End of picture text -----**<br>


55 / 91 

## **Forecasting French spot electricity prices** 

## Hourly day-ahead market prices (between producers and suppliers) 

**==> picture [377 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
3000<br>2500<br>2000<br>1500<br>1000 2 017 − 01 2017 − 07 2018 − 01 2018 − 07 2019 − 01 2019 − 07 2020 − 01 2020 − 07 2021 − 01<br>Date<br>500<br>0<br>2016 2017 2018 2019 2020 2021 2022 2023 2024<br>Date<br>/MWh)<br>€(<br>price<br>Spot<br>**----- End of picture text -----**<br>


## _To which extent are they forecastable?_ 

## _�→_ forecasts errors **no lower than 10%** of the realized price! 

55 / 91 

## **Temporal splitting strategies: Online Sequential Split Conformal Prediction (OSSCP, Zaffran et al., 2022; Dutot et al., 2024)** 

Unused data Proper training set Calibration set Test point 

(a) OSSCP 

**==> picture [76 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
(b) OSSCP-horizon<br>**----- End of picture text -----**<br>


56 / 91 

## **Temporal splitting strategies: Online Sequential Split Conformal Prediction (OSSCP, Zaffran et al., 2022; Dutot et al., 2024)** 

Unused data Proper training set Calibration set Test point 

**==> picture [240 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) OSSCP (b) OSSCP-horizon<br>**----- End of picture text -----**<br>


`OSSCP` improves robustness in temporal settings; 

56 / 91 

## **Temporal splitting strategies: Online Sequential Split Conformal Prediction (OSSCP, Zaffran et al., 2022; Dutot et al., 2024)** 

Unused data Proper training set Calibration set Test point 

**==> picture [240 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) OSSCP (b) OSSCP-horizon<br>**----- End of picture text -----**<br>


`OSSCP` improves robustness in temporal settings; `OSSCP-horizon` drastically improves robustness in non-stationary temporal settings. 

56 / 91 

## **Zoom on Adaptive Conformal Inference (ACI, Gibbs and Cand`es, 2021)** 

Adaptive Conformal Inference (ACI) was initially proposed to handle distribution shift. 

57 / 91 

## **Zoom on Adaptive Conformal Inference (ACI, Gibbs and Cand`es, 2021)** 

Adaptive Conformal Inference (ACI) was initially proposed to handle distribution shift. 

It relies on updating online an _effective miscoverage rate αt_ , with the scheme 

**==> picture [218 x 20] intentionally omitted <==**

and _α_ 1 = _α_ , _γ ≥_ 0. 

57 / 91 

## **Zoom on Adaptive Conformal Inference (ACI, Gibbs and Cand`es, 2021)** 

Adaptive Conformal Inference (ACI) was initially proposed to handle distribution shift. 

It relies on updating online an _effective miscoverage rate αt_ , with the scheme 

**==> picture [218 x 20] intentionally omitted <==**

and _α_ 1 = _α_ , _γ ≥_ 0. 

**Intuition:** if we did make an error, the interval was too small so we want to increase its length by taking a higher quantile (a smaller _αt_ ). Reversely if we included the point. 

57 / 91 

## **Zoom on Adaptive Conformal Inference (ACI, Gibbs and Cand`es, 2021)** 

Adaptive Conformal Inference (ACI) was initially proposed to handle distribution shift. 

It relies on updating online an _effective miscoverage rate αt_ , with the scheme 

**==> picture [218 x 20] intentionally omitted <==**

and _α_ 1 = _α_ , _γ ≥_ 0. 

**Intuition:** if we did make an error, the interval was too small so we want to increase its length by taking a higher quantile (a smaller _αt_ ). Reversely if we included the point. 

57 / 91 

## **Zoom on Adaptive Conformal Inference (ACI, Gibbs and Cand`es, 2021)** 

Adaptive Conformal Inference (ACI) was initially proposed to handle distribution shift. 

It relies on updating online an _effective miscoverage rate αt_ , with the scheme 

**==> picture [218 x 20] intentionally omitted <==**

and _α_ 1 = _α_ , _γ ≥_ 0. 

**Intuition:** if we did make an error, the interval was too small so we want to increase its length by taking a higher quantile (a smaller _αt_ ). Reversely if we included the point. 

**Guarantee:** Asymptotic validity result for any sequence of observations. 

**==> picture [220 x 35] intentionally omitted <==**

57 / 91 

## **Zoom on Adaptive Conformal Inference (ACI, Gibbs and Cand`es, 2021)** 

Adaptive Conformal Inference (ACI) was initially proposed to handle distribution shift. 

It relies on updating online an _effective miscoverage rate αt_ , with the scheme 

**==> picture [218 x 20] intentionally omitted <==**

and _α_ 1 = _α_ , _γ ≥_ 0. 

**Intuition:** if we did make an error, the interval was too small so we want to increase its length by taking a higher quantile (a smaller _αt_ ). Reversely if we included the point. 

**Guarantee:** Asymptotic validity result for any sequence of observations. 

**==> picture [246 x 40] intentionally omitted <==**

57 / 91 

## **Zoom on Adaptive Conformal Inference (ACI, Gibbs and Cand`es, 2021)** 

Adaptive Conformal Inference (ACI) was initially proposed to handle distribution shift. 

It relies on updating online an _effective miscoverage rate αt_ , with the scheme 

**==> picture [218 x 20] intentionally omitted <==**

and _α_ 1 = _α_ , _γ ≥_ 0. 

**Intuition:** if we did make an error, the interval was too small so we want to increase its length by taking a higher quantile (a smaller _αt_ ). Reversely if we included the point. 

**Guarantee:** Asymptotic validity result for any sequence of observations. 

**==> picture [246 x 40] intentionally omitted <==**

_⇒_ favors large _γ_ . 

57 / 91 

## **Visualisation of ACI procedure** 

**==> picture [351 x 65] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>0<br>− 1<br>0 100 200 300 400 500<br>t<br>εt<br>**----- End of picture text -----**<br>


58 / 91 

## **Visualisation of ACI procedure** 

**==> picture [352 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>0<br>− 1<br>0 100 200 300 400 500<br>t<br>1<br>0<br>− 1<br>500 550 600 650 700 750 800 850 900 950 1000<br>t<br>εt<br>εt<br>**----- End of picture text -----**<br>


**Figure 5:** Visualisation of ACI with different values of _γ_ ( _γ_ = 0, _γ_ = 0 _._ 01, _γ_ = 0 _._ 05) 

58 / 91 

## `AgACI` **: adaptive wrapper around ACI, upper bound (Zaffran et al., 2022)** 

Experts **. . . . . .** 

59 / 91 

## `AgACI` **: adaptive wrapper around ACI, upper bound (Zaffran et al., 2022)** 

**==> picture [92 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
Experts Previous upper<br>bounds<br>O n a “yp°<br>Tot+1 t<br>. .<br>. .<br>. .<br>ae me i<br>.<br>To+1 t<br>. .<br>. .<br>. .<br>**----- End of picture text -----**<br>


59 / 91 

## `AgACI` **: adaptive wrapper around ACI, upper bound (Zaffran et al., 2022)** 

**==> picture [137 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
Experts Previous upper Weights<br>bounds<br>ae _<br>¥<br>. . .<br>. . .<br>. To+1 . t i} .<br>i<br>To+1 t<br>. . .<br>. . .<br>. . .<br>**----- End of picture text -----**<br>


59 / 91 

## `AgACI` **: adaptive wrapper around ACI, upper bound (Zaffran et al., 2022)** 

**==> picture [233 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
Experts Previous upper Weights Experts<br>bounds<br>O na ”aeow:¥_ (i)<br>. . . .<br>. . . .<br>. To+1 . t i} . .<br>i<br>To+1 t<br>. . . .<br>. . . .<br>. . . .<br>**----- End of picture text -----**<br>


59 / 91 

## `AgACI` **: adaptive wrapper around ACI, upper bound (Zaffran et al., 2022)** 

**==> picture [233 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
Experts Previous upper Weights Forecasts Experts<br>bounds at t + 1<br>ae _<br>¥<br>. . . . .<br>. . . . .<br>. To+1 . t i} . t+] . .<br>i<br>Tot+1 t t+<br>. . . . .<br>. . . . .<br>. . . . .<br>**----- End of picture text -----**<br>


59 / 91 

## `AgACI` **: adaptive wrapper around ACI, upper bound (Zaffran et al., 2022)** 

**==> picture [233 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
Experts Previous upper Weights Weighted Forecasts Experts<br>bounds mean at t + 1<br>E * é a iL<br>tee<br>To+1 t t+]<br>. . . . .<br>. . . . .<br>. . . . .<br>To+1 ey” NL<br>. . . . .<br>. . . . .<br>. . . . .<br>t ( | t+]<br>(me h QgaMy i hs \ @ (_ >-X ) <——<br>**----- End of picture text -----**<br>


59 / 91 

## **Experimental take-away messages (Zaffran et al., 2022; Dutot et al., 2024)** 

• 2019: `AgACI` provides validity with a reasonable efficiency; 

**==> picture [281 x 99] intentionally omitted <==**

**----- Start of picture text -----**<br>
800<br>600<br>400<br>200<br>0<br>2016 2017 2018 2019 2020 2021 2022<br>Date<br>/MWh)<br>(€<br>price<br>Spot<br>**----- End of picture text -----**<br>


60 / 91 

## **Experimental take-away messages (Zaffran et al., 2022; Dutot et al., 2024)** 

- 2019: `AgACI` provides validity with a reasonable efficiency; 

- 2020 and 2021: `AgACI` fails to ensure validity, and the various forecasting models considered[9] behave differently. 

**==> picture [281 x 99] intentionally omitted <==**

**----- Start of picture text -----**<br>
800<br>600<br>400<br>200<br>0<br>2016 2017 2018 2019 2020 2021 2022<br>Date<br>/MWh)<br>(€<br>price<br>Spot<br>**----- End of picture text -----**<br>


> 9Quantile Random Forests, Quantile Generalized Additive Models, Quantile Gradient Boosting, etc. 

60 / 91 

**==> picture [1893 x 1881] intentionally omitted <==**

**----- Start of picture text -----**<br>
QRF (50 %) QGB (50 %) Lasso QR (50 %) Linear QR (50 %)<br>QRF (25 %) QGB (25 %) Lasso QR (25 %) Linear QR (25 %)<br>1  − α  = 0.6 1  − α  = 0.9 1  − α  = 0.95<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-11<br>bound<br>Upper<br>bound<br>Lower<br>**----- End of picture text -----**<br>


## **Improving adaptiveness for high non-stationarity (Dutot et al., 2024)** 

Online aggregation of various `AgACI` , each of them being trained with different underlying forecasting models, for each bound independently. 

61 / 91 

**==> picture [1893 x 1881] intentionally omitted <==**

**----- Start of picture text -----**<br>
QRF (50 %) QGB (50 %) Lasso QR (50 %) Linear QR (50 %)<br>QRF (25 %) QGB (25 %) Lasso QR (25 %) Linear QR (25 %)<br>1  − α  = 0.6 1  − α  = 0.9 1  − α  = 0.95<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-11<br>bound<br>Upper<br>bound<br>Lower<br>**----- End of picture text -----**<br>


## **Improving adaptiveness for high non-stationarity (Dutot et al., 2024)** 

Online aggregation of various `AgACI` , each of them being trained with different underlying forecasting models, for each bound independently. 

✓ Retrieves validity even in the most hazardous period of 2020 and 2021. 

61 / 91 

**==> picture [1893 x 1881] intentionally omitted <==**

**----- Start of picture text -----**<br>
QRF (50 %) QGB (50 %) Lasso QR (50 %) Linear QR (50 %)<br>QRF (25 %) QGB (25 %) Lasso QR (25 %) Linear QR (25 %)<br>1  − α  = 0.6 1  − α  = 0.9 1  − α  = 0.95<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-11<br>bound<br>Upper<br>bound<br>Lower<br>**----- End of picture text -----**<br>


## **Improving adaptiveness for high non-stationarity (Dutot et al., 2024)** 

Online aggregation of various `AgACI` , each of them being trained with different underlying forecasting models, for each bound independently. 

✓ Retrieves validity even in the most hazardous period of 2020 and 2021. 

✓ Analyzing its weights provides interpretability. 

61 / 91 

## **Improving adaptiveness for high non-stationarity (Dutot et al., 2024)** 

Online aggregation of various `AgACI` , each of them being trained with different underlying forecasting models, for each bound independently. 

✓ Retrieves validity even in the most hazardous period of 2020 and 2021. ✓ Analyzing its weights provides interpretability. 

**==> picture [338 x 166] intentionally omitted <==**

**----- Start of picture text -----**<br>
QRF (75 %) QGB (75 %) Lasso QR (75 %) Linear QR (75 %) QGAM (75 %)<br>QRF (50 %) QGB (50 %) Lasso QR (50 %) Linear QR (50 %) QGAM (50 %)<br>QRF (25 %) QGB (25 %) Lasso QR (25 %) Linear QR (25 %) QGAM (25 %)<br>1  − α  = 0.6 1  − α  = 0.9 1  − α  = 0.95 1  − α  = 0.98<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02<br>bound<br>Upper<br>bound<br>Lower<br>**----- End of picture text -----**<br>


61 / 91 

**Highlights and perspectives** 

Aggregating the two bounds independently (as in `AgACI` and beyond): 

62 / 91 

## **Highlights and perspectives** 

Aggregating the two bounds independently (as in `AgACI` and beyond): 

✓ Allows more flexible and adaptive behavior in practice, catching the varying nature of the predictive distribution tails 

62 / 91 

## **Highlights and perspectives** 

Aggregating the two bounds independently (as in `AgACI` and beyond): 

- ✓ Allows more flexible and adaptive behavior in practice, catching the varying nature of the predictive distribution tails 

- ✗ Prevents from obtaining theoretical guarantees (by opposition to Gibbs and Cand`es, 2022) 

62 / 91 

## **Highlights and perspectives** 

Aggregating the two bounds independently (as in `AgACI` and beyond): 

- ✓ Allows more flexible and adaptive behavior in practice, catching the varying nature of the predictive distribution tails 

- ✗ Prevents from obtaining theoretical guarantees (by opposition to Gibbs and Cand`es, 2022) 

- _�→_ Weaken the objective and consider a more practical theoretical aim? 

62 / 91 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method 

Intro II: Overview of some challenges in Conformal Prediction Advanced I: Towards conditional coverage Advanced II: Avoiding data splitting: full conformal and out-of-bags approaches Advanced III: Beyond exchangeability Applications & Methods I: Some case studies Applications & Methods II: Some methodological advances Concluding remarks 

Applications & Methods II: Some methodological advances Conformal prediction and UQ with missing values Valid Selection among Conformal Sets 

**Conformal prediction and UQ with missing values** ~~ee~~ 

**Margaux Zaffran** 

**Yaniv Romano** 

**Julie Josse** 

_Conformal Prediction with Missing Values_ , ICML 2023, MZ, AD, JJ, YR. _Predictive Uncertainty Quantification with Missing Covariates_ , 2024, MZ, JJ, YR, AD. 

## **Missing values are ubiquitous and challenging** 

|**Data:**<br>�<br>_X_ (_k_)_,_<br>_Y_ (_k_)�_n_<br>_k_=1|_Y_|_X_1<br>_X_2<br>_X_3|
|---|---|---|
||22<br>5<br>6<br>3<br>19<br>6<br>8<br>`NA`<br>19<br>5<br>3<br>6<br>7<br>`NA`<br>9<br>`NA`<br>13<br>4<br>9<br>0<br>20<br>`NA`<br>`NA`<br>1<br>9<br>8<br>`NA`<br>4||



63 / 91 

## **Missing values are ubiquitous and challenging** 

**Data:** � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1 

|_Y_<br>_X_1<br>_X_2<br>_X_3<br>22<br>5<br>6<br>3<br>19<br>6<br>8<br>`NA`<br>19<br>5<br>3<br>6<br>7<br>`NA`<br>9<br>`NA`<br>13<br>4<br>9<br>0<br>20<br>`NA`<br>`NA`<br>1<br>9<br>8<br>`NA`<br>4|Mask _M_ =<br>(_M_1<br>_M_2<br>_M_3)|
|---|---|
||0<br>0<br>0<br>0<br>0<br>1<br>0<br>0<br>0<br>1<br>0<br>1<br>0<br>0<br>0<br>1<br>1<br>0<br>0<br>1<br>0|



63 / 91 

## **Missing values are ubiquitous and challenging** 

**Data:** � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1 

|_Y_<br>_X_1<br>_X_2<br>_X_3<br>22<br>5<br>6<br>3<br>19<br>6<br>8<br>`NA`<br>19<br>5<br>3<br>6<br>7<br>`NA`<br>9<br>`NA`<br>13<br>4<br>9<br>0<br>20<br>`NA`<br>`NA`<br>1<br>9<br>8<br>`NA`<br>4|Mask _M_ =<br>(_M_1<br>_M_2<br>_M_3)|
|---|---|
||0<br>0<br>0<br>0<br>0<br>1<br>0<br>0<br>0<br>1<br>0<br>1<br>0<br>0<br>0<br>1<br>1<br>0<br>0<br>1<br>0|



_�→_ 2 _[d]_ potential masks. 

63 / 91 

## **Missing values are ubiquitous and challenging** 

**Data:** � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1 

|_Y_<br>_X_1<br>_X_2<br>_X_3<br>22<br>5<br>6<br>3<br>19<br>6<br>8<br>`NA`<br>19<br>5<br>3<br>6<br>7<br>`NA`<br>9<br>`NA`<br>13<br>4<br>9<br>0<br>20<br>`NA`<br>`NA`<br>1<br>9<br>8<br>`NA`<br>4|Mask _M_ =<br>(_M_1<br>_M_2<br>_M_3)|
|---|---|
||0<br>0<br>0<br>0<br>0<br>1<br>0<br>0<br>0<br>1<br>0<br>1<br>0<br>0<br>0<br>1<br>1<br>0<br>0<br>1<br>0|



_�→_ 2 _[d]_ potential masks. 

_�→ M_ can depend on _X_ or _Y_ (depending on the missing mechanism (Rubin 1976) 

63 / 91 

## **Missing values are ubiquitous and challenging** 

**Data:** � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1 

|_Y_<br>_X_1<br>_X_2<br>_X_3<br>22<br>5<br>6<br>3<br>19<br>6<br>8<br>`NA`<br>19<br>5<br>3<br>6<br>7<br>`NA`<br>9<br>`NA`<br>13<br>4<br>9<br>0<br>20<br>`NA`<br>`NA`<br>1<br>9<br>8<br>`NA`<br>4|Mask _M_ =<br>(_M_1<br>_M_2<br>_M_3)|
|---|---|
||0<br>0<br>0<br>0<br>0<br>1<br>0<br>0<br>0<br>1<br>0<br>1<br>0<br>0<br>0<br>1<br>1<br>0<br>0<br>1<br>0|



_�→_ 2 _[d]_ potential masks. 

- _�→ M_ can depend on _X_ or _Y_ (depending on the missing mechanism (Rubin 1976) _◦_ **Missing Completely At Random** (MCAR): _M ⊥⊥ X_ 

_◦_ **Missing At Random** (MAR): missingness depends on the observed variables _◦_ **Missing Non At Random** (MNAR) 

63 / 91 

## **Missing values are ubiquitous and challenging** 

**Data:** � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1 

|_Y_<br>_X_1<br>_X_2<br>_X_3<br>22<br>5<br>6<br>3<br>19<br>6<br>8<br>`NA`<br>19<br>5<br>3<br>6<br>7<br>`NA`<br>9<br>`NA`<br>13<br>4<br>9<br>0<br>20<br>`NA`<br>`NA`<br>1<br>9<br>8<br>`NA`<br>4|Mask _M_ =<br>(_M_1<br>_M_2<br>_M_3)|
|---|---|
||0<br>0<br>0<br>0<br>0<br>1<br>0<br>0<br>0<br>1<br>0<br>1<br>0<br>0<br>0<br>1<br>1<br>0<br>0<br>1<br>0|



- _�→_ 2 _[d]_ potential masks. 

- _�→ M_ can depend on _X_ or _Y_ (depending on the missing mechanism (Rubin 1976) 

_◦_ Missing Completely At Random (MCAR): _M ⊥⊥ X_ 

_◦_ Missing At Random (MAR): missingness depends on the observed variables _◦_ Missing Non At Random (MNAR) 

- _Y ⊥⊥M |X_ ? 

63 / 91 

## **Conceptually: a structured distribution shift situation** 

1. For each pattern _m_ , we have a different distribution for ( _X_ obs(M) _, Y_ ) _|M_ = _m_ . 

2. Those distributions are connected. 

3. Reasonable model of the link between pattern and the uncertainty. 

64 / 91 

**==> picture [1609 x 1899] intentionally omitted <==**

**----- Start of picture text -----**<br>
For<br>→<br>**----- End of picture text -----**<br>


## **Goals of predictive uncertainty quantification with missing values** 

**Goal:** predict _Y_[(] _[n]_[+1)] with **confidence** 1 _− α_ , i.e. build the smallest _Cα_ such that: 

65 / 91 

**==> picture [1608 x 1817] intentionally omitted <==**

**----- Start of picture text -----**<br>
→<br>**----- End of picture text -----**<br>


## **Goals of predictive uncertainty quantification with missing values** 

**==> picture [380 x 74] intentionally omitted <==**

**----- Start of picture text -----**<br>
Goal: predict Y [(] [n] [+1)] with confidence 1  − α , i.e. build the smallest Cα such that:<br>1. Marginal Validity (MV)<br>P Y [(] [n] [+1)] ∈Cα X [(] [n] [+1)] , M [(] [n] [+1)][��] ≥ 1  − α. (MV)<br>� �<br>**----- End of picture text -----**<br>


_For example: α_ = 0 _._ 1 and obtain a 90% coverage interval. 

65 / 91 

## **Goals of predictive uncertainty quantification with missing values** 

**==> picture [380 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
Goal: predict Y [(] [n] [+1)] with confidence 1  − α , i.e. build the smallest Cα such that:<br>1. Marginal Validity (MV)<br>P Y [(] [n] [+1)] ∈Cα X [(] [n] [+1)] , M [(] [n] [+1)][��] ≥ 1  − α. (MV)<br>� �<br>2. Mask-Conditional-Validity (MCV)<br>P Y [(] [n] [+1)] ∈Cα X [(] [n] [+1)] , M [(] [n] [+1)][�] |M [(] [n] [+1)][�] [a] ≥ [.][s][.] 1  − α. (MCV)<br>� �<br>**----- End of picture text -----**<br>


65 / 91 

## **Goals of predictive uncertainty quantification with missing values** 

**==> picture [380 x 157] intentionally omitted <==**

**----- Start of picture text -----**<br>
Goal: predict Y [(] [n] [+1)] with confidence 1  − α , i.e. build the smallest Cα such that:<br>1. Marginal Validity (MV)<br>P Y [(] [n] [+1)] ∈Cα X [(] [n] [+1)] , M [(] [n] [+1)][��] ≥ 1  − α. (MV)<br>� �<br>2. Mask-Conditional-Validity (MCV)<br>P Y [(] [n] [+1)] ∈Cα X [(] [n] [+1)] , M [(] [n] [+1)][�] |M [(] [n] [+1)][�] [a] ≥ [.][s][.] 1  − α. (MCV)<br>� �<br>**----- End of picture text -----**<br>


_→_ Let us start by considering marginal validity! 

65 / 91 

## **Achieving marginal validity through impute then conformalize** 

Test point NA NA 2 palm [| 

Calibration set 

66 / 91 

## **Achieving marginal validity through impute then conformalize** 

Test point Test point t Ree] I NA NA 2 “9. EEE 1 4 32 3 1 75 3175 Y BEE Sr PE j 1 2 41 1 2 41 ere} 9 fell ete] β I NA 2 7 ~— [bbe 1 2 2 7 14 1» 4 habe NANA be I Fie 4 I I I *e1 [a3 NA 3 [0 0 fo[NA] SBbE 9 3 03 Calibration set Calibration set 

66 / 91 

## **Achieving marginal validity through impute then conformalize** 

Test point Test point t ome) I NA NA 2 | eee 1 4 32 ” BLEE 3 1 75 GLEE 3175 j 1 2 41 1 2 41 PoRhh| oo | flekdd atte] β I NA 2 7 ——| [ber 1 2 2 7 14 8 [alle 4 NANA eo I eh 4 I I I “Lol NA 3 3 [ 0 [a[NA] Bao 9 3 03 he Calibration set Calibration set Exchangeable! 

**Lemma: Exchangeability after imputation (Zaffran, D., Josse and Romano, 2023)** 

Assume _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] _[n] k_ =1[are][i.i.d.][or][exchangeable.][Then,][for][any][missing][mechanism][,] _n_ for almost all imputation function _ϕ_ : | _ϕ_ ( _X_ obs([(] _[k]_[)] _M_[(] _[k]_[)] ) _[,][ M]_[(] _[k]_[)][)] _[,][ Y]_[ (] _[k]_[)] | _k_ =1[are] **[exchangeable]**[.] 

66 / 91 

## **Achieving marginal validity through impute then conformalize** 

Test point 2) Test point I NA NA 2 —— 1 4 32 3 1 75 3175 Tati [zs | fas Vole} 1 2 41 2g Pi 1 feta 2 [7 [s| 41 fa | I [ewfe NA 2 [7] 7 ——> [1 1 [2 2 [2[[7] 2 7 4 NANA I 4 I I I [-4[ wale [1 | ee [fs ft] [we] NA 3 3 [0 0 [ova[NA] | [5 9 [3 3 fo 03 [s | Calibration set Calibration set Exchangeable! Any CP algorithm 

**Lemma: Exchangeability after imputation (Zaffran, D., Josse and Romano, 2023)** Assume ( _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] ) _[n] k_ =1[are][i.i.d.][or][exchangeable.][Then,][for][any][missing][mechanism,] _n_ for almost all imputation function _ϕ_ : _ϕ_ ( _X_ obs([(] _[k]_[)] _M_[(] _[k]_[)] ) _[,][ M]_[(] _[k]_[)][)] _[,][ Y]_[ (] _[k]_[)] _k_ =1[are] **[exchangeable]**[.] 

66 / 91 

## **Achieving marginal validity through impute then conformalize** 

E.g., Split SCP w. _| · |_ scores es) Test point 2) Test point x I NA NA 2 —— 1 43 2 3 1 75 3175 f M Tati [zs | fas [7 [s| j 1 2 41 1 2 41 Vole} 2g Pi fetafa | [i β I [ewfe NA 2 [7] 7 ——> [1 1 [2 2 [2[[7] 2 7 14 Mt [-4[ 4 NA wale NA [1 I | ee 4 [fs I I ft] I x! [we] NA 3 3 [0 0 [ova[NA] | [5 9 [3 3 fo 03 [s | f Calibration set Calibration set Exchangeable! Any CP algorithm **Lemma: Exchangeability after imputation (Zaffran, D., Josse and Romano, 2023)** Assume ( _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] ) _[n] k_ =1[are][i.i.d.][or][exchangeable.][Then,][for][any][missing][mechanism,] _n_ for almost all imputation function _ϕ_ : _ϕ_ ( _X_ obs([(] _[k]_[)] _M_[(] _[k]_[)] ) _[,][ M]_[(] _[k]_[)][)] _[,][ Y]_[ (] _[k]_[)] _k_ =1[are] **[exchangeable]**[.] 

66 / 91 

## **Achieving marginal validity through impute then conformalize** 

E.g., Split SCP w. _| · |_ scores Test point 2) Test point I NA NA 2 —— 1 4 32 Tati 3175 [zs | fas 3175 [7 [s| 53 1 2 41 1 2 41 Vole} 2g Pi fetafa | I [ewfe NA 2 [7] 7 ——> [1 1 [2 2 [2[[7] 2 7 4 NANA I 4 I I I [-4[ wale [1 | ee [fs ft] [we] NA 3 3 [0 0 [ova[NA] | [5 9 [3 3 fo 03 [s | 34 Calibration set Calibration set Exchangeable! Any CP algorithm 

**Lemma: Exchangeability after imputation (Zaffran, D., Josse and Romano, 2023)** Assume ( _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] ) _[n] k_ =1[are][i.i.d.][or][exchangeable.][Then,][for][any][missing][mechanism,] _n_ for almost all imputation function _ϕ_ : _ϕ_ ( _X_ obs([(] _[k]_[)] _M_[(] _[k]_[)] ) _[,][ M]_[(] _[k]_[)][)] _[,][ Y]_[ (] _[k]_[)] _k_ =1[are] **[exchangeable]**[.] 

66 / 91 

## **Achieving marginal validity through impute then conformalize** 

E.g., Split SCP w. _| · |_ scores Test point Test point es) t 2) x I NA NA 2 —— 1 4 32 “teh 3175 [2 [5] fas 3 [7 7 [s| 5 j Ly! 53 5s | 49 51 s =[4] j 1 2 41 1 2 41 Vole} 2g Pi feta fa | Y 7 [i I [ewfe NA 2 [7] 7 ——> [1 1 [2 2 [2[[7] 2 7 14 Mt [-4[ 4 NA wale NA [1 I | ee 4 [fs I I ft] I x! [we] NA 3 3 [0 0 [ova[NA] | [5 9 [3 3 fo 03 [s | 34 Calibration set Calibration set Exchangeable! Any CP algorithm **Lemma: Exchangeability after imputation (Zaffran, D., Josse and Romano, 2023)** Assume ( _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] ) _[n] k_ =1[are][i.i.d.][or][exchangeable.][Then,][for][any][missing][mechanism,] _n_ for almost all imputation function _ϕ_ : _ϕ_ ( _X_ obs([(] _[k]_[)] _M_[(] _[k]_[)] ) _[,][ M]_[(] _[k]_[)][)] _[,][ Y]_[ (] _[k]_[)] _k_ =1[are] **[exchangeable]**[.] 

66 / 91 

## **Achieving marginal validity through impute then conformalize** 

**==> picture [381 x 251] intentionally omitted <==**

**----- Start of picture text -----**<br>
E.g., Split SCP w. | · | scores<br>Test point Test point<br>es) t 2)<br>x I NA NA 2 —— 1 43 2<br>“teh 3175 [2 [5] fas 3175  [7 [s| f 53 49 51 s = [4]<br>j 1 2 41 1 2 41<br>Vole} 2g Pi feta fa | Y 7 .<br>[i I [ewfe NA 2  [7] 7  ——> [1 1  [2 2 [2 [[7] 2 7<br>1141 4 NANA I 4 I I I<br>Mt [-4[ wale [1 | ee [fs ft]<br>x! [we] NA 3 3 [0 0 [ova [NA]  | [5 9 [3 3  fo 03 [s | 34 37 s=3 3<br>Calibration set Calibration set Y y<br>Exchangeable! Any CP algorithm<br>Lemma: Exchangeability after imputation (Zaffran, D., Josse and Romano, 2023)<br>Assume ( X [(] [k] [)] , M [(] [k] [)] , Y [(] [k] [)] ) [n] k =1 [are] [i.i.d.] [or] [exchangeable.] [Then,] [for] [any] [missing] [mechanism,]<br>n<br>for almost all imputation function ϕ : ϕ ( X obs( [(] [k] [)] M [(] [k] [)] ) [,][ M] [(] [k] [)][)] [,][ Y] [ (] [k] [)] k =1 [are] [exchangeable] [.]<br>**----- End of picture text -----**<br>


66 / 91 

## **Achieving marginal validity through impute then conformalize** 

E.g., Split SCP w. _| · |_ scores Test point Test point q "ot) I NA NA 2 # iY 1 43 2 À } 41 Y BPP 3175 BLP 3175 f 53 : 49 51[4] j 1 2 41 1 2 41 Y ehtehh| oo | ele “ otek] I NA 2 7 —— [bkry 1 2 2 7 no| 1141 4 NANA I 4 I I I Palba hbk |, *e! Lata NA 3 0[NA] 9 3 03 34 37 3 [o [ua lest | Vt opabe <-s Calibration set Calibration set Y > Exchangeable! Any CP algorithm **Lemma: Exchangeability after imputation (Zaffran, D., Josse and Romano, 2023)** Assume _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] _[n] k_ =1[are][i.i.d.][or][exchangeable.][Then,][for][any][missing][mechanism,] _n_ for almost all imputation function _ϕ_ : _ϕ_ ( _X_ obs([(] _[k]_[)] _M_[(] _[k]_[)] ) _[,][ M]_[(] _[k]_[)][)] _[,][ Y]_[ (] _[k]_[)] _k_ =1[are] **[exchangeable]**[.] 

66 / 91 

## **Achieving marginal validity through impute then conformalize** 

**==> picture [381 x 251] intentionally omitted <==**

**----- Start of picture text -----**<br>
E.g., Split SCP w. | · | scores<br>ĉ<br>0 Test point 0 Test point an<br>I NA NA 2 1 43 2 8 41 Scd<br>‘ ——- fu] = 91 4,. [a]  (Sa)<br>3175 3175 j 53 49 51 [4]<br>oeae j  a EEE 1 2 41 BP 1 2  Pfs} 41 Y |5-4<br>ef [efel?}] I NA 2 7 ——> [pete 1 2 2 7 |<br>1141 cy aN 4 NANA I PAE 4 I I I<br>1 [ras NA 3 0 [NA] 9 3 03 f 34 37<br>[o fon EGE Uy 53<br>Calibration set Calibration set Y 1<br>Exchangeable! Any CP algorithm<br>Lemma: Exchangeability after imputation (Zaffran, D., Josse and Romano, 2023)<br>Assume ( X [(] [k] [)] , M [(] [k] [)] , Y [(] [k] [)] ) [n] k =1 [are] [i.i.d.] [or] [exchangeable.] [Then,] [for] [any] [missing] [mechanism,]<br>n<br>for almost all imputation function ϕ : | ϕ ( X obs( [(] [k] [)] M [(] [k] [)] ) [,][ M] [(] [k] [)][)] [,][ Y] [ (] [k] [)] , k =1 [are] [exchangeable] [.]<br>**----- End of picture text -----**<br>


66 / 91 

## **CP is marginally valid** (MV) **after imputation** 

## **Lemma: Exchangeability after imputation (Zaffran, D., Josse and Romano, 2023)** 

Assume � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[are i.i.d. or exchangeable.][Then, for any missing mech-] anism, for almost all imputation function _ϕ_ : � _ϕ_ ( _X_ obs([(] _[k]_[)] _M_[(] _[k]_[)] ) _[,][ M]_[(] _[k]_[)][)] _[,][ Y]_[ (] _[k]_[)][�] _[n] k_ =1[are] **[ex-] changeable** . 

_⇒_ CQR, and Conformal Prediction, applied on an imputed data set still enjoys marginal guarantees 

**==> picture [210 x 21] intentionally omitted <==**

66 / 91 

## **CQR is marginally valid on imputed data sets** 

## _Y_ = _β[T] X_ + _ε_ , _β_ = (1 _,_ 2 _, −_ 1) _[T]_ , _X_ and _ε_ Gaussian. 

**==> picture [202 x 125] intentionally omitted <==**

**----- Start of picture text -----**<br>
CQR (marginal validity)<br>1 . 0<br>1  − α<br>0 . 8<br>0 . 6<br>Marginal<br>coverage<br>Average<br>**----- End of picture text -----**<br>


- ✓ Marginal (i.e. average) coverage (MV) is indeed recovered! 

67 / 91 

## **CQR is marginally valid on imputed data sets** 

## _Y_ = _β[T] X_ + _ε_ , _β_ = (1 _,_ 2 _, −_ 1) _[T]_ , _X_ and _ε_ Gaussian. 

**==> picture [202 x 151] intentionally omitted <==**

**----- Start of picture text -----**<br>
CQR (marginal validity)<br>1 . 0<br>1  − α<br>0 . 8<br>0 . 6<br>Marginalfullyobserved X 1missing , X 2)missing X 2missing , X 3)missing X 3missing , X 3)missing<br>X X 1 X 2 X 1<br>( ( (<br>coverage<br>Average<br>**----- End of picture text -----**<br>


- ✓ Marginal (i.e. average) coverage (MV) is indeed recovered! 

✗ Mask-conditional-validity (MCV) is not attained 

- _�→_ Missing values induce heteroskedasticity _(supported by theory under (non-)parametric assumptions)_ 

67 / 91 

**==> picture [1592 x 1842] intentionally omitted <==**

## **Challenges and limits** 

## 1. Splitting the calibration set by mask is infeasible (lack of data)! 

**==> picture [230 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initial calibration set<br>Test point Test point<br>-1 -10 6 1<br>3 6 0 1 3 1<br>4 -2 2<br>5 1 1 Calibration set used Calibration set used<br>0 1 -1 -10 6 1 0 1<br>**----- End of picture text -----**<br>


68 / 91 

## **Challenges and limits** 

## 1. Splitting the calibration set by mask is infeasible (lack of data)! 

**==> picture [230 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initial calibration set<br>Test point Test point<br>-1 -10 6 1<br>3 6 0 1 3 1<br>4 -2 2<br>5 1 1 Calibration set used Calibration set used<br>0 1 -1 -10 6 1 0 1<br>**----- End of picture text -----**<br>


## 2. Fully distribution-free MCV is necessarily uninformative 

**General MCV hardness result (Zaffran, Josse, Romano and D., 2024)**[10] 

If any _C_[�] _α_ is distribution-free MCV then for any distribution _P_ , for any mask _m_ such that _PM_ ( _m_ ) _>_ 0, it holds: 

**==> picture [271 x 24] intentionally omitted <==**

68 / 91 

## **Challenges and limits** 

## 1. Splitting the calibration set by mask is infeasible (lack of data)! 

**==> picture [230 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initial calibration set<br>Test point Test point<br>-1 -10 6 1<br>3 6 0 1 3 1<br>4 -2 2<br>5 1 1 Calibration set used Calibration set used<br>0 1 -1 -10 6 1 0 1<br>**----- End of picture text -----**<br>


## 2. Fully distribution-free MCV is necessarily uninformative 

**General MCV hardness result (Zaffran, Josse, Romano and D., 2024)**[10] 

If any _C_[�] _α_ is distribution-free MCV then for any distribution _P_ , for any mask _m_ such that _PM_ ( _m_ ) _>_ 0, it holds: 

**==> picture [271 x 24] intentionally omitted <==**

## 1. Similar result if we assume _M ⊥⊥ X_ . 

68 / 91 

## **Challenges and limits** 

## 1. Splitting the calibration set by mask is infeasible (lack of data)! 

**==> picture [230 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initial calibration set<br>Test point Test point<br>-1 -10 6 1<br>3 6 0 1 3 1<br>4 -2 2<br>5 1 1 Calibration set used Calibration set used<br>0 1 -1 -10 6 1 0 1<br>**----- End of picture text -----**<br>


## 2. Fully distribution-free MCV is necessarily uninformative 

**General MCV hardness result (Zaffran, Josse, Romano and D., 2024)**[10] 

If any _C_[�] _α_ is distribution-free MCV then for any distribution _P_ , for any mask _m_ such that _PM_ ( _m_ ) _>_ 0, it holds: 

**==> picture [271 x 24] intentionally omitted <==**

1. Similar result if we assume _M ⊥⊥ X_ . 

2. Similar result if we assume _Y ⊥⊥M |X_ 

68 / 91 

## **Challenges and limits** 

## 1. Splitting the calibration set by mask is infeasible (lack of data)! 

**==> picture [230 x 61] intentionally omitted <==**

**----- Start of picture text -----**<br>
Initial calibration set<br>Test point Test point<br>-1 -10 6 1<br>3 6 0 1 3 1<br>4 -2 2<br>5 1 1 Calibration set used Calibration set used<br>0 1 -1 -10 6 1 0 1<br>**----- End of picture text -----**<br>


## 2. Fully distribution-free MCV is necessarily uninformative 

**General MCV hardness result (Zaffran, Josse, Romano and D., 2024)**[10] 

If any _C_[�] _α_ is distribution-free MCV then for any distribution _P_ , for any mask _m_ such that _PM_ ( _m_ ) _>_ 0, it holds: 

**==> picture [271 x 24] intentionally omitted <==**

1. Similar result if we assume _M ⊥⊥ X_ . 

   - _⇒_ need to restrict both the link between _M_ and _X_ , as well as between _M_ and _Y_ . 

2. Similar result if we assume _Y ⊥⊥M |X_ 

68 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 1: **Missing data augmentation** . 

Test point 

Calibration set 

69 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask b> Solution 1: **Missing data augmentation** . 

Test point 

Calibration set 

69 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 1: **Missing data augmentation** . 

Test point 

Calibration set Overmasked cal. 

69 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 1: **Missing data augmentation** . 

Test point 

Calibration set Overmasked cal. 

69 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask 

## Solution 1: **Missing data augmentation** . 

Test point 

Calibration set Overmasked cal. 

Exchangeable! i Marginal distribution = dist of ( _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)] _, Y[n]_[+1] ) _|M[n]_[+1] 

69 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask 

## Solution 1: **Missing data augmentation** . 

Test point 

Calibration set Overmasked cal. Exchangeable! _→_ Any CP algorithm ensures MCV Marginal distribution = dist of ( _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)] _, Y[n]_[+1] ) _|M[n]_[+1] 

69 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask 

## Solution 1: **Missing data augmentation** . 

Test point I[NA][NA] L I[NA][NA] L I[NA][NA] 2 COCO NS ee EMI 3 1 7 5 51 3 NANA S S NANA S _a.s._ E28 fats] ™ [fon I NANA fons I | I NANA I P { _Y_[(] _[n]_[+1)] _∈C/ α_ ( _X_[(] _[n]_[+1)] _, m_ ) _|M_[(] _[n]_[+1)] 4 _≤ α._ n'a wale fait NANANA 7 4 NANA [7 I -—ppen fon p fn p [2m 4 NANA I [a NA fivafon 3 0 [oP NA I fea NA foal[NANA][NA] [oP foe NA finan[NANA] fo[NA] [on 3 ]o fn} | Calibration set Overmasked cal. Exchangeable! _→_ Any CP algorithm ensures MCV Marginal distribution = dist of ( _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)] _, Y[n]_[+1] ) _|M[n]_[+1] 

69 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 1: **Missing data augmentation** . 

**==> picture [396 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
Test point<br>I [NA][NA] L I [NA][NA] L I [NA][NA] 2<br>COCO NS ee EMI<br>3 1 7 5 51 3 NANA S S NANA S a.s.<br>E28 fats]  ™ [fon I NANA fons I  | I NANA I P { Y [(] [n] [+1)] ∈C/ α ( X [(] [n] [+1)] , m ) |M [(] [n] [+1)] 4 ≤ α.<br>n'a<br>wale  fait NANANA 7<br>4 NANA [7 I  -—ppen fon p fn  p [2m 4 NANA I<br>[a NA  fivafon  3 0  [oP NA I fea NA  foal [NANA][NA] [oP foe NA  finan [NANA] fo [NA]<br>[on 3 ]o fn} |<br>Calibration set Overmasked cal.<br>Exchangeable! → Any CP algorithm ensures MCV<br>Marginal distribution<br>= dist of ( X [(] [n] [+1)] , M [(] [n] [+1)] , Y [n] [+1] ) |M [n] [+1]<br>**----- End of picture text -----**<br>


Problem: still far too few points for patterns with few missing data. 

69 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask b> Solution 2: **Missing data augmentation + keeping more points** . 

Test point 

Calibration set Overmasked cal. Keep any subselection! 

70 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

Test point 

Calibration set Overmasked cal. Keep any subselection! 

70 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

**==> picture [196 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
Test point<br>I [NA][NA] L I [NA][NA] L I [NA][NA] 2<br>Ghee] Ebb) Epp le|<br>3175<br>(stefats] * [sfafofs] [Ls fon fons|<br>fefefet| Le feefeafy<br>[n'a] la [24] f<br>Jon fon 2 [7 pon [on [on | | ponfa  fofo n  fee[os [|| 9<br> [oafivafon 4 NANA fr] I  feafivafonfn] [oa f [afin]<br>NA 3 0 NA I<br>[on] 3] [vn] ae [on [ua fonfval |[1]<br>Ee I 4 9 [NA]<br>Calibration set Overmasked cal. Keep any<br>subselection!<br>**----- End of picture text -----**<br>


70 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

**==> picture [202 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
Test point<br>I [NA][NA] L I [NA][NA] L EAC I [NA][NA] 2<br>“GOPE) n'a rhh) 31 7 175 51 *GEhE]flab) flabbyGEepEe<br>A<br>flee} falafel} ote lebae]<br>4 NANA I<br>Faeabefr) — Falabebe)  Falabebe]<br>NA 3 0 NA I<br>(als [opal Sfofafafa) |<br>I 4 9 [NA]<br>Calibration set Overmasked EISEN cal. Em Keep ETE any<br>subselection!<br>**----- End of picture text -----**<br>


70 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

Test point I[NA][NA] L I[NA][NA] L I[NA][NA] 2 [4 Jo fon [2 | 31 7 5 51 fsttais| = [sfonfofs] [sf foals[n'a] fenlaTefetet A 17 | fi febe ff feeb 4 NANA [2 I Pye fon? Pen forfo] [ea NA Toa] 3 vafua 0 fr] NA I fea fvafonfr] feafvaloefn] fo [ua] fon fonfonfvaf 1 4 9[NA] Calibration set Overmasked ja fon fon fen] cal. [a Keep fre fon any fue]la y subselection! 

70 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

**==> picture [196 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
Test point<br>I [NA][NA] L I [NA][NA] L I [NA][NA] 2<br>[4 [vn [va [a |<br>3 1 7 5 51<br>{stelz[s] = {sfafofs] [sf foals<br>N'A ifeleh} 24 17 bebe} Lfefef}<br>Jon[eale A [7 -— mle foalf? ofrfonfn[2]<br>NA [eafvafonfof 4 NA 3 NA0 fr] [NA] l [eafvafn I fn] etofe]<br>3 fo fon] Se [wnfonfoafunf<br>1 4 9 [NA]<br>[4 Joosfonfie} [a five fn fo<br>Calibration set Overmasked cal. Keep any<br>subselection!<br>**----- End of picture text -----**<br>


70 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

**==> picture [196 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
Test point<br>I [NA][NA] L I [NA][NA] L I [NA][NA] 2<br>PAC<br>3 1 7 5 51<br>{stelz[s] = {sfafofs] [sf foals<br>[n'a] Jon[ealeifeleh} A [7 17  -— mlebebe} foalf? ofrLfefef}fonfn[2]<br>NA [eafvafonfof 4 NA 3 NA0 fr] NAI [eafvafn I fn] etofe]<br>3 fo fon] Se [wnfonfoafunf<br>1 4 9 [NA]<br>[4 Joosfonfie} [a five fn fo<br>Calibration set Overmasked cal. Keep any<br>subselection!<br>**----- End of picture text -----**<br>


70 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

**==> picture [196 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
Test point<br>I [NA][NA] L I [NA][NA] L PACS I [NA][NA] 2<br>3 1 7 5 51<br>stele[s] = [sfafofs] [Lsfeafoals<br>ifeleh| feb} Lfefef<br>[n'a] Jon[wale A [2][ᵈ] [7 7 -—rloe foal? ofrfonfn[2]<br>NA [eafvafonfof 4 NA 3 NA0 fr] NAI [eafvafn I fn] eatenfe]<br>3 [0 fon] See [wnfonfoafwnf<br>1 4 9 [NA]<br>[4 Joosfonfie} [a five fn fo<br>Calibration set Overmasked cal. Keep any<br>subselection!<br>**----- End of picture text -----**<br>


70 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

Test point I[NA][NA] L I[NA][NA] L PACS I[NA][NA] 2 3 1 7 5 51 stele[s] = [sfafofs] [Lsfeafoals[n'a] Jon[waleifeleh A [7 17 |-—rloefeb} foal? ofrLfefeffonfn[2] NA [eafvafonfof 4 NA 3 NA0 fr] NAI [eafvafn I fn] eatenfe] 3 [0 fon] See [wnfonfoafwnf 1 4 9[NA] [4 Joosfonfie} [a five fn fo Calibration set Overmasked cal. Keep any subselection! 

Problem: scores cannot simply be aggregated and used, no guarantee on that! 

70 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

Test point I[NA][NA] L I[NA][NA] L I[NA][NA] L [2 Toa ]oe [2 | YGUGE) 3 1 75 x̅ *EEEE) BEET PERhh) Ebsbeh) Epapat[n'a] n 24 f [on [on] | [eefwafon 4 NANA [Fo I fin on fin | pen fo fon | [a] Eafwafon[a] a fafon[5] NA 3 0 NA I te I 4 9[NA] ts te) Gaffe] [a[oof] i] Calibration set Overmasked cal. Keep any subselection! 

/ 

Combine _identical_ missing patterns 

71 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask b> Solution 2: **Missing data augmentation + keeping more points** . 

Test point I[NA][NA] L I[NA][NA] L Be I[NA][NA] L 3 7 5 51 tis] *(sfefefs] eps fo[s][n'a] enfenfefefet n 24 f | ff} fofn [J [x epee enfin etalon 4 NANA I [of fo fo | NA [oul 3 0 NA fr] Feefeafon[a] a naff 3 [0 foe] SP [vefonfonfonp | 1 4 9[NA] fete} Cefeebelee] [a fof] Calibration set Overmasked cal. Keep any subselection! 

/ 

Combine _identical_ missing patterns 

71 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

Test point I[NA][NA] 2 I[NA][NA] L CII I[NA][NA] L YGUGE) 3 1 75 x̅ *EEEE) BEET eTtteh[n'a] foals n 24 f | ffefah] fi fefah [a }-—ofeelenfn [ohio 4 NANA I Fever] Fefeen ler] Fence NA 3 0 NA Tals Toa) = fonfaf fap ENTREN 1 4 9[NA] eS Cs Od Calibration set Overmasked cal. Keep any subselection! 

/ 

Combine _identical_ missing patterns 

71 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask b> Solution 2: **Missing data augmentation + keeping more points** . 

## Test point 

Calibration set Overmasked cal. Keep any subselection! 

/ 

Combine _identical_ missing patterns 

71 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask b> Solution 2: **Missing data augmentation + keeping more points** . 

## Test point 

Calibration set Overmasked cal. Keep any subselection! 

/ 

Combine _identical_ missing patterns 

71 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask b> Solution 2: **Missing data augmentation + keeping more points** . 

## Test point 

Calibration set Overmasked cal. Keep any subselection! 

/ 

Combine _identical_ missing patterns 

71 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask b> Solution 2: **Missing data augmentation + keeping more points** . 

## Test point 

I 4 9[NA] Ca feeede] [a[Due]] Calibration set Overmasked cal. Keep any subselection! 

/ 

Combine _identical_ missing patterns 

71 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

## **Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

**==> picture [196 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
Test point<br>I [NA][NA] L I [NA][NA] L JoJo] I [NA][NA] 2<br>|<br>“ChE 3175 À<br>s|] *hh—] BPP]<br>a<br> [eole[e [n'a][ LA][ 24] f<br>[2 -—o fon fess of [fn]<br> 23 4 NANA I<br>NA we]  3 3 [0 0 [va] NA xf wa wa [on [ova |<br>1 4 9 [NA]<br>ja fuefenfee] [a foe fon fue]<br>Calibration set Overmasked cal. Keep any<br>subselection!<br>**----- End of picture text -----**<br>


/ 

Combine _identical_ missing patterns 

71 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

**Idea:** for each test point, modify the calibration points to mimic the test mask b> Solution 2: **Missing data augmentation + keeping more points** . 

Test point 

Calibration set Overmasked cal. Keep any subselection! 

/ 

Combine _identical_ missing patterns 

71 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

## **Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

**==> picture [196 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
Test point<br>I [NA][NA] L I [NA][NA] L I [NA][NA] 2<br>FACIE<br>Tali 3175  le[s] x̅ = [3 fom foa[s|<br>fefati| fa fefnfpLfentonfa<br>[n'a] rfoafe [ LA] 7<br>[a4[wel NA4  foeafon  NA 3  3[o NA0 []}-—[val NA rf I  efiSe fea[oafonfonfvmp eel} foeafonrf [eaeben felonfer<br>1 4 9 [NA] ja foefonfve] [4 [vere[ve<br>Calibration set Overmasked cal. Keep any<br>subselection!<br>**----- End of picture text -----**<br>


**==> picture [5 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
/<br>**----- End of picture text -----**<br>


Combine _identical_ missing patterns 

71 / 91 

## `CP-MDA-Nested` _[⋆]_ **(Missing Data Augmentation)** 

## **Idea:** for each test point, modify the calibration points to mimic the test mask > Solution 2: **Missing data augmentation + keeping more points** . 

**==> picture [196 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
Test point<br>EReE) I [NA][NA] L GEePE) I [NA][NA] L Gere I [NA][NA] 2<br>Tali 3175  le[s] x̅ = [3 fom foa[s|<br>fefati| fa fefnfpLfenton<br>[n'a][ LA] 7 fa<br>Joon [wn]<br>[a4[wel NA4  foeafon  NA 3  3[o NA0 2 |[val NA rf I heSe fea[oafonfonfvmp | foeafonwn fn |?rf ne[ea felon| we fo ||fer<br>FES 1 4 9 [NA] CO<br>Calibration set Overmasked cal. Keep any<br>subselection!<br>**----- End of picture text -----**<br>


/ 

Combine _identical_ missing patterns 

71 / 91 

## `CP-MDA-Nested` _[⋆]_ **achieves Mask-Conditional-Validity** (MCV) 

**Mask-conditional-validity of** `CP-MDA-Nested` _[⋆]_ **(Zaffran, Josse, Romano and D., 2024)** Under the assumptions that: 

**==> picture [349 x 115] intentionally omitted <==**

**----- Start of picture text -----**<br>
• M ⊥⊥ X , Y  ,<br>• � X [(] [k] [)] , M [(] [k] [)] , Y [(] [k] [)][�] [n] k [+1] =1 [are] [i.i.d.,]<br>• the subsampling scheme is independent of � X [(] [k] [)] , Y [(] [k] [)][�] [n] k [+1] =1 [,]<br>then, for almost all imputation function,  CP-MDA-Nested [⋆] reaches (MCV) at<br>the level 1  − 2 α , that is:<br>P Y [(] [n] [+1)] ∈ C [�] α X [(] [n] [+1)] , m |M [(] [n] [+1)][�] [a] ≥ [.][s][.] 1  − 2 α.<br>� � �<br>**----- End of picture text -----**<br>


72 / 91 

## `CP-MDA-Nested` _[⋆]_ **achieves Mask-Conditional-Validity** (MCV) 

## **Mask-conditional-validity of** `CP-MDA-Nested` _[⋆]_ 

**(Zaffran, Josse, Romano and D., 2024)** 

Under the assumptions that: 

• _M ⊥⊥ X , Y_ , • � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_[+1] =1[are][i.i.d.,] • the subsampling scheme is independent of � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_[+1] =1[,] 

then, for almost all imputation function, `CP-MDA-Nested` _[⋆]_ reaches (MCV) at the level 1 _−_ 2 _α_ , that is: 

P _Y_[(] _[n]_[+1)] _∈ C_[�] _α X_[(] _[n]_[+1)] _, m |M_[(] _[n]_[+1)][�] _[a] ≥[.][s][.]_ 1 _−_ 2 _α._ � � � 

Proof relates `CP-MDA-Nested` _[⋆]_ to JK+ type algorithms. 

Non-absolute value scores and classification are also encompassed. 

72 / 91 

**Link to Jackknife+ (Barber et al., 2021b)** ~~ee~~ 

73 / 91 

## **Link to JK+** 

1. When training on _Dn[−][i]_[,][we][sample][a][mask] _[M]_[(] _[i]_[)][,][and][the][trained][predictor][is] 

**==> picture [126 x 14] intentionally omitted <==**

2. The randomness of the training is coupled with the randomness of the Masks in the calibration dataset. 

3. We directly recognize an instance of JK+. 

74 / 91 

**Experiments on** _M ⊥⊥_ ( _X , Y_ ) **Gaussian linear data in dimension 10** 

**==> picture [101 x 133] intentionally omitted <==**

20% of missing values 

75 / 91 

**Experiments on** _M ⊥⊥_ ( _X , Y_ ) **Gaussian linear data in dimension 10** 

**==> picture [192 x 133] intentionally omitted <==**

20% of missing values 

75 / 91 

## **Experiments on** _M ⊥⊥_ ( _X , Y_ ) **Gaussian linear data in dimension 10** 

20% of missing values 

75 / 91 

## **Experiments on** _M ⊥⊥_ ( _X , Y_ ) **Gaussian linear data in dimension 10** 

**==> picture [373 x 140] intentionally omitted <==**

**----- Start of picture text -----**<br>
CQR-MDA-Nested [⋆] subsampling<br>CQR CQR-MDA-Exact points with at most 2 more  NA s CQR-MDA-Nested<br>1 . 0<br>0 . 8<br>Hi bberserode! retecdeegel ctreeegeege<br>0 . 6<br>Hen<br>15 Oracle length<br>10<br>* if vad cau!<br>5<br>ogg9e0080d! ley gggett bog ehttttt | leeeet tiie<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


## 20% of missing values 

75 / 91 

## **Experiments on** _M ⊥⊥_ ( _X , Y_ ) **Gaussian linear data in dimension 10** 

**==> picture [373 x 140] intentionally omitted <==**

**----- Start of picture text -----**<br>
CQR-MDA-Nested [⋆] subsampling<br>CQR CQR-MDA-Exact points with at most 2 more  NA s CQR-MDA-Nested<br>1 . 0 7 oY? o V7V Org )<br>00 .. 86 | '<br>15 Oracle length<br>10<br>5<br>eqogegenonl) reel | [Mbeertieet) Peete<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


40% of missing values 

75 / 91 

## **Experiments on** _M ⊥⊥_ ( _X , Y_ ) **Gaussian linear data in dimension 10** 

**==> picture [373 x 140] intentionally omitted <==**

**----- Start of picture text -----**<br>
CQR-MDA-Nested [⋆] subsampling<br>CQR CQR-MDA-Exact points with at most 2 more  NA s CQR-MDA-Nested<br>1 . 0<br>0 . 8 ohttted oUt, TEEPOt RAG) [Treen eng<br>0 . 6 | | 1 '<br>15 Oracle length 6 6<br>10 A |<br>5<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


40% of missing values 

## **Experiments beyond independenc** e 

_→_ Under various MAR and MNAR mechanisms, `CP-MDA-Nested` _[⋆]_ maintains empirical MCV; 

75 / 91 

## **Take-home-messages : Conformal prediction and UQ with missing values** 

- CP marginal guarantees hold on the imputed data set. 

- Missingness introduces additional heteroskedasticity and is a fun case to study shifts. 

- CQR (and more generally CP) fails to attain coverage conditional on the missing pattern, i.e. MCV. 

- MCV is impossible to ensure in an informative way without restricting both the dependence between _M_ and _X_ , and between _M_ and _Y_ . 

- `CP-MDA-Nested` _[⋆]_ (Missing Data Augmentation) is the first method to output predictive intervals with missing values. 

- `CP-MDA-Nested` _[⋆]_ attains conditional coverage with respect to the missing pattern (in MCAR and _Y ⊥⊥M |X_ setting). 

- `CP-MDA-Nested` _[⋆]_ is empirically robust to non-MCAR scenarii. 

76 / 91 

Applications & Methods II: Some methodological advances Conformal prediction and UQ with missing values Valid Selection among Conformal Sets 

## **Valid Selection among Conformal Sets** 

**Mahmoud Hegazy Liviu Aolaritei** _´Ecole Polytechnique UC Berkeley_ 

**Mickael I Jordan** _UC Berkeley INRIA Paris_ 

_Valid Selection among Conformal Sets_ , 2025, MH, LA, MJ, AD 

## **Summary:** 

- **Question:** When multiple valid sets exist, to which extent can we select the smallest (most informative) one ? 

   - _→_ Selection after observation of length can break the coverage guarantee. 

77 / 91 

## **Summary:** 

- **Question:** When multiple valid sets exist, to which extent can we select the smallest (most informative) one ? 

   - _→_ Selection after observation of length can break the coverage guarantee. 

**Remark:** line of work by Liang et al. (2024); Yang and Kuchibhotla (2024), that try to select the smallest set marginally on _X_ , as well as Gasparin and Ramdas (2024a) in an online framework. 

_→_ We aim for pointwise selection. 

- _→_ we show how to combine approaches 

77 / 91 

## **Summary:** 

- **Question:** When multiple valid sets exist, to which extent can we select the smallest (most informative) one ? 

   - _→_ Selection after observation of length can break the coverage guarantee. 

**Remark:** line of work by Liang et al. (2024); Yang and Kuchibhotla (2024), that try to select the smallest set marginally on _X_ , as well as Gasparin and Ramdas (2024a) in an online framework. 

- _→_ We aim for pointwise selection. 

- _→_ we show how to combine approaches 

## **Our Approach:** 

1. Use algorithmic stability in a randomized selection framework and adjust the 

   - coverage guarantee 

## **or** 

2. Define a meta-score incorporating the selection. [opt.] 

77 / 91 

## **Selection among Conformal Sets: Selecting the Smallest Prediction Set** 

- Given _K_ prediction sets _{Ci[α]_[(] _[X]_[)] _[}][K] i_ =1[,][the][goal][is][to][select][the][smallest][one.] 

78 / 91 

## **Selection among Conformal Sets: Selecting the Smallest Prediction Set** 

- Given _K_ prediction sets _{Ci[α]_[(] _[X]_[)] _[}][K] i_ =1[,][the][goal][is][to][select][the][smallest][one.] 

- **Issue:** Naively selecting the smallest set can invalidate the coverage 

   - guarantee. 

78 / 91 

## **Selection among Conformal Sets: Selecting the Smallest Prediction Set** 

- Given _K_ prediction sets _{Ci[α]_[(] _[X]_[)] _[}][K] i_ =1[,][the][goal][is][to][select][the][smallest][one.] 

- **Issue:** Naively selecting the smallest set can invalidate the coverage 

   - guarantee. 

- Let _i[∗]_ ( _X_ ) = argmin _i λ_ ( _Ci[α]_[(] _[X]_[)).] 

**==> picture [132 x 21] intentionally omitted <==**

78 / 91 

## **Selection among Conformal Sets: Selecting the Smallest Prediction Set** 

- Given _K_ prediction sets _{Ci[α]_[(] _[X]_[)] _[}][K] i_ =1[,][the][goal][is][to][select][the][smallest][one.] 

- **Issue:** Naively selecting the smallest set can invalidate the coverage 

   - guarantee. 

- Let _i[∗]_ ( _X_ ) = argmin _i λ_ ( _Ci[α]_[(] _[X]_[)).] 

**==> picture [132 x 21] intentionally omitted <==**

Obviously similar to _multiple tests_ , or _inference after selection_ , etc. 

78 / 91 

**Algorithmic Stability** 

## **Definition: (Indistinguishability)** 

A r.v. _S_ is _η, τ_ indistinguishable from _S_ 0, denoted _S ≈η,τ S_ 0 if for all measurable _O_ , P _{S ∈O} ≤ e[η]_ P _{S_ 0 _∈O}_ + _τ._ 

79 / 91 

## **Algorithmic Stability** 

## **Definition: (Indistinguishability)** 

A r.v. _S_ is _η, τ_ indistinguishable from _S_ 0, denoted _S ≈η,τ S_ 0 if for all measurable _O_ , 

P _{S ∈O} ≤ e[η]_ P _{S_ 0 _∈O}_ + _τ._ 

- Intuitively: _S_ and _S_ 0 are “close” in distribution. 

79 / 91 

## **Algorithmic Stability** 

## **Definition: (Indistinguishability)** 

A r.v. _S_ is _η, τ_ indistinguishable from _S_ 0, denoted _S ≈η,τ S_ 0 if for all measurable _O_ , 

P _{S ∈O} ≤ e[η]_ P _{S_ 0 _∈O}_ + _τ._ 

- Intuitively: _S_ and _S_ 0 are “close” in distribution. 

- Smaller _η_ : greater similarity; _τ_ : small additive difference. 

79 / 91 

## **Algorithmic Stability** 

## **Definition: (Indistinguishability)** 

A r.v. _S_ is _η, τ_ indistinguishable from _S_ 0, denoted _S ≈η,τ S_ 0 if for all measurable _O_ , 

P _{S ∈O} ≤ e[η]_ P _{S_ 0 _∈O}_ + _τ._ 

- Intuitively: _S_ and _S_ 0 are “close” in distribution. 

- Smaller _η_ : greater similarity; _τ_ : small additive difference. 

- Conditional notation: _S ≈[|] η,τ[ξ][S]_ 0[to][hold][conditionally][to] _[ξ]_[.] 

79 / 91 

## **Algorithmic Stability** 

We are ready to define the stability of a randomized algorithm, 

**==> picture [68 x 12] intentionally omitted <==**

(Zrnic and Jordan, 2023; Bassily et al., 2016; Bassily and Freund, 2016)[11] . 

- _ξ ∈_ Ξ: input data (e.g., sizes of conformal sets). 

• _E_ : algorithm’s internal randomness. 

**Algorithmic Stability (specific** _ν_ = 0 **case)** 

_S_ ˆ : Ξ _× E →S_ is ( _η, τ, ν_ = 0)-stable if _∃S_ 0 

**==> picture [96 x 16] intentionally omitted <==**

_→_ Quantifies how close the algorithm’s output is from a fixed distribution for most (here all) inputs. 11Many similar definitions in many subfields of ML 

80 / 91 

**==> picture [1608 x 1935] intentionally omitted <==**

## **From Stability to Valid Conformal Coverage** 

81 / 91 

## **From Stability to Valid Conformal Coverage** 

**Theorem: (Valid Stable Selection)** Assume each _C[α]_[satisfies][the][coverage][guarantee:] _i_[(] _[X]_[)] _∀i,_ P _{Y ∈/ Ci[α]_[(] _[X]_[)] _[} ≤][α.]_ If _S_[ˆ] : Ξ _× E →S_ is ( _η, τ_ )-stable, then P _{Y ∈_ C _[α] S_ ˆ( _ξ,ϵ_ )[(] _[X]_[)] _[} ≥]_[1] _[ −][α][e][η][ −][τ.]_ 

- Standard 1 _− α_ coverage: adjust individual sets to 1 _−_ ( _α − τ_ ) _e[−][η]_ . 

81 / 91 

## **From Stability to Valid Conformal Coverage** 

## **Theorem: (Valid Stable Selection)** 

Assume each _C[α]_[satisfies][the][coverage][guarantee:] _i_[(] _[X]_[)] _∀i,_ P _{Y ∈/ Ci[α]_[(] _[X]_[)] _[} ≤][α.]_ If _S_[ˆ] : Ξ _× E →S_ is ( _η, τ_ )-stable, then P _{Y ∈_ C _[α] S_ ˆ( _ξ,ϵ_ )[(] _[X]_[)] _[} ≥]_[1] _[ −][α][e][η][ −][τ.]_ 

- Standard 1 _− α_ coverage: adjust individual sets to 1 _−_ ( _α − τ_ ) _e[−][η]_ . 

- Stable selection: favours smaller sets, controls coverage. 

81 / 91 

## **From Stability to Valid Conformal Coverage** 

## **Theorem: (Valid Stable Selection)** 

Assume each _C[α]_[satisfies][the][coverage][guarantee:] _i_[(] _[X]_[)] _∀i,_ P _{Y ∈/ Ci[α]_[(] _[X]_[)] _[} ≤][α.]_ 

If _S_[ˆ] : Ξ _× E →S_ is ( _η, τ_ )-stable, then P _{Y ∈_ C _[α] S_ ˆ( _ξ,ϵ_ )[(] _[X]_[)] _[} ≥]_[1] _[ −][α][e][η][ −][τ.]_ 

- Standard 1 _− α_ coverage: adjust individual sets to 1 _−_ ( _α − τ_ ) _e[−][η]_ . 

- Stable selection: favours smaller sets, controls coverage. 

- Requires to increase set size 

81 / 91 

## **From Stability to Valid Conformal Coverage** 

## **Theorem: (Valid Stable Selection)** 

Assume each _C[α]_[satisfies][the][coverage][guarantee:] _i_[(] _[X]_[)] 

_∀i,_ P _{Y ∈/ Ci[α]_[(] _[X]_[)] _[} ≤][α.]_ 

If _S_[ˆ] : Ξ _× E →S_ is ( _η, τ_ )-stable, then 

P _{Y ∈_ C _[α] S_ ˆ( _ξ,ϵ_ )[(] _[X]_[)] _[} ≥]_[1] _[ −][α][e][η][ −][τ.]_ 

- Standard 1 _− α_ coverage: adjust individual sets to 1 _−_ ( _α − τ_ ) _e[−][η]_ . 

- Stable selection: favours smaller sets, controls coverage. 

- Requires to increase set size 

- Can be shown to be tight in the worst case. 

81 / 91 

## **From Stability to Valid Conformal Coverage** 

## **Theorem: (Valid Stable Selection)** 

Assume each _C[α]_[satisfies][the][coverage][guarantee:] _i_[(] _[X]_[)] 

_∀i,_ P _{Y ∈/ Ci[α]_[(] _[X]_[)] _[} ≤][α.]_ 

If _S_[ˆ] : Ξ _× E →S_ is ( _η, τ_ )-stable, then 

P _{Y ∈_ C _[α] S_ ˆ( _ξ,ϵ_ )[(] _[X]_[)] _[} ≥]_[1] _[ −][α][e][η][ −][τ.]_ 

- Standard 1 _− α_ coverage: adjust individual sets to 1 _−_ ( _α − τ_ ) _e[−][η]_ . 

- Stable selection: favours smaller sets, controls coverage. 

- Requires to increase set size 

- Can be shown to be tight in the worst case. 

- _→_ Proposed Stable rule? 

81 / 91 

**==> picture [1608 x 1859] intentionally omitted <==**

## **Algorithmic Stability: Stable Minimum Selection** 

Let 

_ξ_ ( _X_ ) = ( _λ_ ( _C_ 1 _[α]_[(] _[X]_[))] _[ , . . . , λ]_[ (] _[C] K[ α]_[(] _[X]_[)))] _[ .]_ 

_→_ Minimum Stable Expectation (MinSE) mechanism achieves **stability** . 

**Idea:** pick a prior _b ∈_ ∆ _[K][−]_[1] (prior knowledge on set choice). Then, minimizes expected size while ensuring ( _η, τ_ )-stability. This turns out to be a linear program 

82 / 91 

## **Algorithmic Stability: Stable Minimum Selection** 

**==> picture [277 x 16] intentionally omitted <==**

_→_ Minimum Stable Expectation (MinSE) mechanism achieves **stability** . **Idea:** pick a prior _b ∈_ ∆ _[K][−]_[1] (prior knowledge on set choice). Then, minimizes expected size while ensuring ( _η, τ_ )-stability. This turns out to be a linear program 

**==> picture [377 x 165] intentionally omitted <==**

**----- Start of picture text -----**<br>
MinSE Mechanism<br>Let<br>K<br>p [⋆] ( b, ξ ) = argmin p � pi λ ( Ci [α] [(] [X] [))]<br>i =1<br>s . t .p ∈ ∆ [K] [−] [1] , s ∈ R [K] + [,] pi ≤ e [η] bi +  si , � si ≤ τ<br>i∈ [ K ]<br>Selection rule such that<br>ˆ<br>• P S ( ξ, ϵ )= i|ξ =  p [⋆] ( b, ξ ) i<br>� �<br>• is η, τ -stable.<br>**----- End of picture text -----**<br>


82 / 91 

## **Limit cases of MinSE Mechanism (1)** 

**==> picture [288 x 16] intentionally omitted <==**

**==> picture [193 x 73] intentionally omitted <==**

83 / 91 

## **Limit cases of MinSE Mechanism (1)** 

**==> picture [288 x 16] intentionally omitted <==**

**==> picture [193 x 73] intentionally omitted <==**

Thus _S_[ˆ] ( _ξ, ϵ_ ) = argmin _i λ_ ( _Ci[α]_[(] _[X]_[))][we][select][the][minimal][length][set.] 

83 / 91 

## **Limit cases of MinSE Mechanism (1)** 

**==> picture [288 x 16] intentionally omitted <==**

**==> picture [193 x 73] intentionally omitted <==**

Thus _S_[ˆ] ( _ξ, ϵ_ ) = argmin _i λ_ ( _Ci[α]_[(] _[X]_[))][we][select][the][minimal][length][set.] 

- _→_ To ensure 1 _− α_ coverage of the corresponding set, we need 1 _− α/K_ individual coverage. 

83 / 91 

## **Limit cases of MinSE Mechanism (1)** 

**==> picture [288 x 16] intentionally omitted <==**

**==> picture [193 x 52] intentionally omitted <==**

**==> picture [80 x 11] intentionally omitted <==**

Thus _S_[ˆ] ( _ξ, ϵ_ ) = argmin _i λ_ ( _Ci[α]_[(] _[X]_[))][we][select][the][minimal][length][set.] 

- _→_ To ensure 1 _− α_ coverage of the corresponding set, we need 1 _− α/K_ individual coverage. 

- _→_ Akin to Bonferoni correction 

83 / 91 

## **Limit cases of MinSE Mechanism (1)** 

**==> picture [288 x 16] intentionally omitted <==**

**==> picture [193 x 52] intentionally omitted <==**

**==> picture [80 x 11] intentionally omitted <==**

Thus _S_[ˆ] ( _ξ, ϵ_ ) = argmin _i λ_ ( _Ci[α]_[(] _[X]_[))][we][select][the][minimal][length][set.] 

- _→_ To ensure 1 _− α_ coverage of the corresponding set, we need 1 _− α/K_ individual coverage. 

- _→_ Akin to Bonferoni correction 

- _→_ Beneficial if at any _X_ , one set with coverage 1 _− α/K_ is much smaller than the average length of sets with coverage 1 _− α_ . 

83 / 91 

## **Limit cases of MinSE Mechanism (2)** 

2 _b_ any prior and _e[η]_ = 1 _, τ_ = 0 : 

_K p[⋆]_ ( _b_ 0 _, ξ_ ) =argmin _p_ � _pi λ_ ( _Ci[α]_[(] _[X]_[))] _i_ =1 s _._ t _.p ∈_ ∆ _[K][−]_[1] _, pi ≤ bi_ = _b_ 

83 / 91 

## **Limit cases of MinSE Mechanism (2)** 

2 _b_ any prior and _e[η]_ = 1 _, τ_ = 0 : 

**==> picture [165 x 68] intentionally omitted <==**

**==> picture [327 x 14] intentionally omitted <==**

83 / 91 

## **Limit cases of MinSE Mechanism (2)** 

2 _b_ any prior and _e[η]_ = 1 _, τ_ = 0 : 

**==> picture [165 x 68] intentionally omitted <==**

- _⇒ S_[ˆ] ( _ξ, ϵ_ ) picks without data dependence, just sampling from a prior _b_ . 

_→_ To ensure 1 _− α_ coverage of the corresponding set, we need 1 _− α_ individual coverage. 

83 / 91 

## **Limit cases of MinSE Mechanism (3)** 

**==> picture [281 x 16] intentionally omitted <==**

**==> picture [172 x 53] intentionally omitted <==**

83 / 91 

## **Limit cases of MinSE Mechanism (3)** 

**==> picture [281 x 16] intentionally omitted <==**

**==> picture [172 x 53] intentionally omitted <==**

**==> picture [289 x 14] intentionally omitted <==**

83 / 91 

## **Limit cases of MinSE Mechanism (3)** 

**==> picture [281 x 16] intentionally omitted <==**

**==> picture [172 x 53] intentionally omitted <==**

   - _⇒ S_[ˆ] ( _ξ, ϵ_ ) only picks among half the sets with smallest lengths. 

- _→_ To ensure 1 _− α_ coverage of the corresponding set, we need 1 _− α/_ 2 individual coverage. 

83 / 91 

## **Limit cases of MinSE Mechanism (3)** 

**==> picture [281 x 16] intentionally omitted <==**

**==> picture [172 x 53] intentionally omitted <==**

   - _⇒ S_[ˆ] ( _ξ, ϵ_ ) only picks among half the sets with smallest lengths. 

- _→_ To ensure 1 _− α_ coverage of the corresponding set, we need 1 _− α/_ 2 individual coverage. 

- _→_ Beneficial if at any _X_ , sets with coverage 1 _− α/_ 2 are much smaller than the average length of sets with coverage 1 _− α_ . 

83 / 91 

## **Limit cases of MinSE Mechanism (3)** 

**==> picture [281 x 16] intentionally omitted <==**

**==> picture [172 x 53] intentionally omitted <==**

- _⇒ S_[ˆ] ( _ξ, ϵ_ ) only picks among half the sets with smallest lengths. 

_→_ To ensure 1 _− α_ coverage of the corresponding set, we need 1 _− α/_ 2 individual coverage. 

_→_ Beneficial if at any _X_ , sets with coverage 1 _− α/_ 2 are much smaller than the average length of sets with coverage 1 _− α_ . 

- ↬ Overall, as expected, useful when conformal sets perform “heterogeneously”. 

83 / 91 

## **Toy example: Split Input** 

## • **Setup:** _Y_ = _|X |_ + _N_ (0 _,_ 0 _._ 25), _X ∼_ Uniform([ _−_ 1 _,_ 1]). 

84 / 91 

## **Toy example: Split Input** 

## • **Setup:** _Y_ = _|X |_ + _N_ (0 _,_ 0 _._ 25), _X ∼_ Uniform([ _−_ 1 _,_ 1]). • **Predictors:** 

84 / 91 

## **Toy example: Split Input** 

## • **Setup:** _Y_ = _|X |_ + _N_ (0 _,_ 0 _._ 25), _X ∼_ Uniform([ _−_ 1 _,_ 1]). • **Predictors:** • _f_ 1( _X_ ) = _X_ : Good for _X ≥_ 0. 

84 / 91 

## **Toy example: Split Input** 

## • **Setup:** _Y_ = _|X |_ + _N_ (0 _,_ 0 _._ 25), _X ∼_ Uniform([ _−_ 1 _,_ 1]). • **Predictors:** • _f_ 1( _X_ ) = _X_ : Good for _X ≥_ 0. • _f_ 2( _X_ ) = _−X_ : Good for _X ≤_ 0. 

84 / 91 

## **Toy example: Split Input** 

## • **Setup:** _Y_ = _|X |_ + _N_ (0 _,_ 0 _._ 25), _X ∼_ Uniform([ _−_ 1 _,_ 1]). • **Predictors:** • _f_ 1( _X_ ) = _X_ : Good for _X ≥_ 0. • _f_ 2( _X_ ) = _−X_ : Good for _X ≤_ 0.[(] _[X]_[)] _[|]_ • Sets obtained SCP with score _s_ ( _X , Y_ ) = _[|][Y][ −] ρ_ ˆ( _[f] X_[ˆ] ) 

84 / 91 

## **Toy example: Split Input** 

- **Setup:** _Y_ = _|X |_ + _N_ (0 _,_ 0 _._ 25), _X ∼_ Uniform([ _−_ 1 _,_ 1]). 

- **Predictors:** 

   - _f_ 1( _X_ ) = _X_ : Good for _X ≥_ 0. 

   - _f_ 2( _X_ ) = _−X_ : Good for _X ≤_ 0. 

- [(] _[X]_[)] _[|]_ 

- • Sets obtained SCP with score _s_ ( _X , Y_ ) = _[|][Y][ −] ρ_ ˆ( _[f] X_[ˆ] ) 

- Complementary strengths. 

84 / 91 

## **Toy example: Split Input** 

- **Setup:** _Y_ = _|X |_ + _N_ (0 _,_ 0 _._ 25), _X ∼_ Uniform([ _−_ 1 _,_ 1]). 

- **Predictors:** 

   - _f_ 1( _X_ ) = _X_ : Good for _X ≥_ 0. 

   - _f_ 2( _X_ ) = _−X_ : Good for _X ≤_ 0. 

- [(] _[X]_[)] _[|]_ 

- • Sets obtained SCP with score _s_ ( _X , Y_ ) = _[|][Y][ −] ρ_ ˆ( _[f] X_[ˆ] ) 

- Complementary strengths. 

- **Stable Selection:** allows pointwise selection which is better than picking the best on average as in Liang et al. (2024); Yang and Kuchibhotla (2024). 

84 / 91 

## **Extensions and improvements: 1 - AdaMinSE** 

1. Tradeoff between _η_ and _τ_ still not clear. 

2. **Adaptive** MinSE (AdaMinSE): optimize over _η_ and _τ_ , to achieve a desired target miscoverage level _α_ , given that original sets miscoverage is _α[′]_ . 

3. This is also a linear program: 

## **AdaMinSE Mechanism** 

**==> picture [328 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
K<br>d [∗] ( b, ξ ) = argmin d � di λ ( Ci [α] [(] [X] [))]<br>i =1<br>s . t . d ∈ ∆ [K] [−] [1] , s ∈ R [K] + [, τ, η] [≥] [0]<br>di ≤ e [η] bi +  si , � si ≤ τ, e [η] α [′] +  τ ≤ α<br>i∈ [ K ]<br>Selection rule such that<br>ˆ<br>• P S ( ξ, ϵ )= i|ξ =  d [∗] ( b, ξ ) i<br>� �<br>• is η, τ -stable.<br>**----- End of picture text -----**<br>


85 / 91 

## **Extensions and improvements: 2- Improving the Prior** 

- **Data-Dependent Prior:** a uniform prior _b_ 0 can be used in MinSE and AdaMinSE but can be suboptimal. 

86 / 91 

## **Extensions and improvements: 2- Improving the Prior** 

- **Data-Dependent Prior:** a uniform prior _b_ 0 can be used in MinSE and AdaMinSE but can be suboptimal. 

- Construct the prior using cross-validation on the training data, _D_ train 

   - or 

86 / 91 

## **Extensions and improvements: 2- Improving the Prior** 

- **Data-Dependent Prior:** a uniform prior _b_ 0 can be used in MinSE and AdaMinSE but can be suboptimal. 

- Construct the prior using cross-validation on the training data, _D_ train 

   - or 

- Construct the prior in an online fashion, incorporating techniques like COMA Gasparin and Ramdas (2024a). 

86 / 91 

## **Experiments: UCI Datasets Setup** 

**Baselines:** YK (Yang and Kuchibhotla, 2024, EFCP), LZB (Liang et al., 2024, ModSel-CP). 

## **Heterogeneous training sets** 

**Metrics:** Coverage ( _≥_ 1 _− α_ ) & Normalized Interval Length (smaller is better) 

87 / 91 

## **Take-home-messages : Valid Selection among Conformal Sets** 

1. Coverage after selection requires care ! 

2. We leverage both stability based - and recalibration based methods can bring improvements. 

3. Those techniques enable to favor pointwise smallest sets - they come at a cost. 

4. Stability based method easily incorporate prior (e.g. in online) information. 

5. Overall, expected to be favorable in heterogeneous training setups. 

88 / 91 

Intro I: Split Conformal Prediction (SCP) - the simplest CP method 

Intro II: Overview of some challenges in Conformal Prediction Advanced I: Towards conditional coverage Advanced II: Avoiding data splitting: full conformal and out-of-bags approaches Advanced III: Beyond exchangeability Applications & Methods I: Some case studies Applications & Methods II: Some methodological advances Concluding remarks 

## **Summary: Uncertainty quantification through conformal methods** 

**==> picture [400 x 242] intentionally omitted <==**

**----- Start of picture text -----**<br>
Conformal methods<br>• Marginal validity<br>Quantile regression no guarantee<br>• Model/distribution agnostic<br>• Finite sample<br>SCP Full CP JK/CV<br>+ no retraining + no split + balance cost<br>- split - prohibitive cost - requires stability or 1  − 2 α<br>Various scores<br>• Based on µ ˆ( x )<br>• Based on QR [�] ( x )<br>• Based on P [ˆ] ( y |x )<br>Limit 1: only marginal guarantee Limit 2: requires exch.<br>• Hardness of conditional coverage • Distribution shifts<br>• Asymptotic results / Adaptive • Online methods<br>methods<br>Case Studies<br>**----- End of picture text -----**<br>


89 / 91 

## **Some (other, non-exhaustives) current open directions** 

- Outlier detection (Vovk et al., 2003; Bates et al., 2023) 

- Selective inference, false discovery rate guarantees (Marandon et al., 2024; Gazin et al., 2024) 

- Beyond the indicator loss (Angelopoulos et al., 2022a; Bates et al., 2021b; Angelopoulos et al., 2023; Lekeufack et al., 2024) 

- Aggregating predictive sets (Gasparin and Ramdas, 2024c,b; Gasparin et al., 2024) 

90 / 91 

## **Acknowledgments** 

## For discussion and feedback, thanks to 

- Julie Josse 

- Claire Boyer 

- Etienne[´] Roquain 

## **Questions?** 

91 / 91 

## **References i** 

Angelopoulos, A. N. and Bates, S. (2023). Conformal prediction: A gentle introduction. _Foundations and Trends® in Machine Learning_ , 16(4). Angelopoulos, A. N., Bates, S., Cand`es, E. J., Jordan, M. I., and Lei, L. (2022a). Learn then test: Calibrating predictive algorithms to achieve risk control. Angelopoulos, A. N., Bates, S., Fisch, A., Lei, L., and Schuster, T. (2023). Conformal risk control. 

Angelopoulos, A. N., Kohli, A. P., Bates, S., Jordan, M., Malik, J., Alshaabi, T., Upadhyayula, S., and Romano, Y. (2022b). Image-to-image regression with distribution-free uncertainty quantification and applications in imaging. In _International Conference on Machine Learning_ , pages 717–730. PMLR. 

Barber, R. F., Cand`es, E. J., Ramdas, A., and Tibshirani, R. J. (2021a). The limits of distribution-free conditional predictive inference. _Information and Inference: A Journal of the IMA_ , 10(2). 

Barber, R. F., Cand`es, E. J., Ramdas, A., and Tibshirani, R. J. (2021b). Predictive inference with the jackknife+. _The Annals of Statistics_ , 49(1). 

## **References ii** 

Barber, R. F., Cand`es, E. J., Ramdas, A., and Tibshirani, R. J. (2022). Conformal prediction beyond exchangeability. To appear in _Annals of Statistics (2023)_ . Bassily, R. and Freund, Y. (2016). Typical stability. _arXiv preprint arXiv:1604.03336_ . 

Bassily, R., Nissim, K., Smith, A., Steinke, T., Stemmer, U., and Ullman, J. (2016). Algorithmic stability for adaptive data analysis. In _Proceedings of the forty-eighth annual ACM symposium on Theory of Computing_ , pages 1046–1059. Bates, S., Angelopoulos, A., Lei, L., Malik, J., and Jordan, M. (2021a). Distribution-free, risk-controlling prediction sets. _Journal of the ACM (JACM)_ , 68(6):1–34. Bates, S., Angelopoulos, A., Lei, L., Malik, J., and Jordan, M. (2021b). Distribution-free, risk-controlling prediction sets. _J. ACM_ , 68(6). Bates, S., Cand`es, E., Lei, L., Romano, Y., and Sesia, M. (2023). Testing for outliers with conformal p-values. _The Annals of Statistics_ , 51(1):149 – 178. 

## **References iii** 

Bian, M. and Barber, R. F. (2023). Training-conditional coverage for distribution-free predictive inference. _Electronic Journal of Statistics_ , 17(2):2044 – 2066. 

Cauchois, M., Gupta, S., Ali, A., and Duchi, J. C. (2020). Robust Validation: Confident Predictions Even When Distributions Shift. arXiv: 2008.04267. Chernozhukov, V., W¨uthrich, K., and Yinchu, Z. (2018). Exact and Robust Conformal Inference Methods for Predictive Machine Learning with Dependent Data. In _Conference On Learning Theory_ . PMLR. Chernozhukov, V., W¨uthrich, K., and Zhu, Y. (2021). Distributional conformal prediction. _Proceedings of the National Academy of Sciences_ , 118(48). Cherubin, G., Chatzikokolakis, K., and Jaggi, M. (2021). Exact optimization of conformal predictors via incremental and decremental learning. In _Proceedings of the 38th International Conference on Machine Learning_ . PMLR. Dutot, G., Zaffran, M., F´eron, O., and Goude, Y. (2024). Adaptive probabilistic forecasting of french electricity spot prices. 

## **References iv** 

Feldman, S., Bates, S., and Romano, Y. (2021). Improving Conditional Coverage via Orthogonal Quantile Regression. _arXiv:2106.00394 [cs]_ . arXiv: 2106.00394. Gasparin, M. and Ramdas, A. (2024a). Conformal online model aggregation. _arXiv preprint arXiv:2403.15527_ . 

Gasparin, M. and Ramdas, A. (2024b). Conformal online model aggregation. Gasparin, M. and Ramdas, A. (2024c). Merging uncertainty sets via majority vote. Gasparin, M., Wang, R., and Ramdas, A. (2024). Combining exchangeable p-values. 

Gazin, U., Blanchard, G., and Roquain, E. (2024). Transductive conformal inference with adaptive scores. 

Gibbs, I. and Cand`es, E. (2021). Adaptive conformal inference under distribution shift. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc. 

Gibbs, I. and Cand`es, E. (2022). Conformal inference for online prediction with arbitrary distribution shifts. arXiv: 2208.08401. 

## **References v** 

Gibbs, I., Cherian, J. J., and Cand`es, E. J. (2023). Conformal prediction with conditional guarantees. arXiv: 2305.12616. 

Guan, L. (2022). Localized conformal prediction: a generalized inference framework for conformal prediction. _Biometrika_ , 110(1). Gupta, C., Kuchibhotla, A. K., and Ramdas, A. (2022). Nested conformal prediction and quantile out-of-bag ensemble methods. _Pattern Recognition_ , 127. Izbicki, R., Shimizu, G., and Stern, R. B. (2022). CD-split and HPD-split: Efficient conformal regions in high dimensions. _Journal of Machine Learning Research_ , 23(87). 

Jung, C., Noarov, G., Ramalingam, R., and Roth, A. (2023). Batch multivalid conformal prediction. In _International Conference on Learning Representations_ . Kivaranovic, D., Johnson, K. D., and Leeb, H. (2020). Adaptive, Distribution-Free Prediction Intervals for Deep Networks. In _International Conference on Artificial Intelligence and Statistics_ . PMLR. 

## **References vi** 

Lei, J. (2019). Fast exact conformalization of the lasso using piecewise linear homotopy. _Biometrika_ , 106(4). 

Lei, J., G’Sell, M., Rinaldo, A., Tibshirani, R. J., and Wasserman, L. (2018). Distribution-Free Predictive Inference for Regression. _Journal of the American Statistical Association_ . 

Lei, J. and Wasserman, L. (2014). Distribution-free prediction bands for non-parametric regression. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 76(1). 

Lekeufack, J., Angelopoulos, A. N., Bajcsy, A., Jordan, M. I., and Malik, J. (2024). Conformal decision theory: Safe autonomous decisions from imperfect predictions. 

Liang, R., Zhu, W., and Barber, R. F. (2024). Conformal prediction after efficiency-oriented model selection. _arXiv preprint arXiv:2408.07066_ . 

## **References vii** 

Marandon, A., Lei, L., Mary, D., and Roquain, E. (2024). Adaptive novelty detection with false discovery rate guarantee. _The Annals of Statistics_ , 52(1):157 – 183. 

Ndiaye, E. (2022). Stable conformal prediction sets. In _Proceedings of the 39th International Conference on Machine Learning_ . PMLR. 

Ndiaye, E. and Takeuchi, I. (2019). Computing full conformal prediction set with approximate homotopy. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc. 

Ndiaye, E. and Takeuchi, I. (2022). Root-finding approaches for computing conformal prediction set. _Machine Learning_ , 112(1). 

Nouretdinov, I., Melluish, T., and Vovk, V. (2001). Ridge regression confidence machine. In _Proceedings of the 18th International Conference on Machine Learning_ . 

Papadopoulos, H., Proedrou, K., Vovk, V., and Gammerman, A. (2002). Inductive Confidence Machines for Regression. In _Machine Learning: ECML_ . Springer. 

## **References viii** 

Podkopaev, A. and Ramdas, A. (2021). Distribution-free uncertainty quantification for classification under label shift. In _Proceedings of the Thirty-Seventh Conference on Uncertainty in Artificial Intelligence_ . PMLR. Romano, Y., Barber, R. F., Sabatti, C., and Cand`es, E. (2020a). With Malice Toward None: Assessing Uncertainty via Equalized Coverage. _Harvard Data Science Review_ , 2(2). 

Romano, Y., Patterson, E., and Cand`es, E. (2019). Conformalized Quantile Regression. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc. 

Romano, Y., Sesia, M., and Candes, E. (2020b). Classification with valid and adaptive coverage. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc. 

Sadinle, M., Lei, J., and Wasserman, L. (2018). Least ambiguous set-valued classifiers with bounded error levels. _Journal of the American Statistical Association_ , 114(525):223–234. 

## **References ix** 

Sesia, M. and Romano, Y. (2021). Conformal prediction using conditional histograms. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc. 

Tibshirani, R. J., Barber, R. F., Candes, E., and Ramdas, A. (2019). Conformal Prediction Under Covariate Shift. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc. Vovk, V. (2012). Conditional Validity of Inductive Conformal Predictors. In _Asian Conference on Machine Learning_ . PMLR. 

Vovk, V., Gammerman, A., and Shafer, G. (2005). _Algorithmic Learning in a Random World_ . Springer US. 

Vovk, V., Nouretdinov, I., and Gammerman, A. (2003). Testing exchangeability on-line. In _Proceedings of the Twentieth International Conference on International Conference on Machine Learning_ , ICML’03, page 768–775. AAAI Press. 

**References x** 

Yang, Y. and Kuchibhotla, A. K. (2024). Selection and aggregation of conformal prediction sets. _Journal of the American Statistical Association_ , pages 1–13. Zaffran, M., F´eron, O., Goude, Y., Josse, J., and Dieuleveut, A. (2022). Adaptive conformal predictions for time series. In _Proceedings of the 39th International Conference on Machine Learning_ . PMLR. Zrnic, T. and Jordan, M. I. (2023). Post-selection inference via algorithmic stability. _The Annals of Statistics_ , 51(4):1666–1691. 

## **Proof of the quantile lemma** 

**Def:** Empirical quantile _qβ_ ( _U_ 1 _, . . . , Uk_ ) := _⌈β × k⌉_ smallest value of ( _U_ 1 _, . . . , Uk_ ) 

## **Proof of the quantile lemma** 

**Def:** Empirical quantile _qβ_ ( _U_ 1 _, . . . , Uk_ ) := _⌈β × k⌉_ smallest value of ( _U_ 1 _, . . . , Uk_ ) First note that _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ ) _⇐⇒ Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1). 

## **Proof of the quantile lemma** 

## **lower bound** 

**Def:** Empirical quantile _qβ_ ( _U_ 1 _, . . . , Uk_ ) := _⌈β × k⌉_ smallest value of ( _U_ 1 _, . . . , Uk_ ) First note that _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ ) _⇐⇒ Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1). By exchangeability, for any _i ∈_ �1 _, n_ + 1�: P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)) =P ( _Ui ≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)). 

## **Proof of the quantile lemma** 

## **upper bound** 

**Def:** Empirical quantile _qβ_ ( _U_ 1 _, . . . , Uk_ ) := _⌈β × k⌉_ smallest value of ( _U_ 1 _, . . . , Uk_ ) First note that _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ ) _⇐⇒ Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1). By exchangeability, for any _i ∈_ �1 _, n_ + 1�: P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)) =P ( _Ui ≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)). Thus: _n_ +1 1 P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)) = _n_ + 1 � P ( _Ui ≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)) _i_ =1 

## **Proof of the quantile lemma** 

**==> picture [378 x 154] intentionally omitted <==**

## **Proof of the quantile lemma** 

**==> picture [378 x 209] intentionally omitted <==**

proving the first statement. 

## **Proof of the quantile lemma** 

**==> picture [378 x 209] intentionally omitted <==**

proving the second statement. 

**==> picture [1609 x 1782] intentionally omitted <==**

## **Jackknife: the naive idea does not enjoy valid coverage** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

**==> picture [1608 x 1781] intentionally omitted <==**

## **Jackknife: the naive idea does not enjoy valid coverage** 

- Based on leave-one-out (LOO) residuals 

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- • Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) • LOO scores _S_ = _|A_[ˆ] _−i_ ( _Xi_ ) _− Yi |_ � � _i[∪{]_[+] _[∞}]_ 

**==> picture [85 x 36] intentionally omitted <==**

(in standard mean regression) 

**==> picture [1608 x 1781] intentionally omitted <==**

## **Jackknife: the naive idea does not enjoy valid coverage** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- • Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) • LOO scores _S_ = _|A_[ˆ] _−i_ ( _Xi_ ) _− Yi |_ (in standard mean regression) � � _i[∪{]_[+] _[∞}]_ 

- Get _A_[ˆ] by training _A_ on _Dn_ 

**==> picture [1608 x 1781] intentionally omitted <==**

## **Jackknife: the naive idea does not enjoy valid coverage** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

• Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) • LOO scores _S_ = _|A_[ˆ] _−i_ ( _Xi_ ) _− Yi |_ (in standard mean regression) � � _i[∪{]_[+] _[∞}]_ • Get _A_[ˆ] by training _A_ on _Dn_ ˆ • Build the predictive interval: _A_ ( _Xn_ +1) _± q_ 1 _−α_ ( _S_ ) � � 

## **Jackknife: the naive idea does not enjoy valid coverage** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

• LOO scores _S_ = _|A_[ˆ] _−i_ ( _Xi_ ) _− Yi |_ (in standard mean regression) � � _i[∪{]_[+] _[∞}]_ • Get _A_[ˆ] by training _A_ on _Dn_ ˆ • Build the predictive interval: _A_ ( _Xn_ +1) _± q_ 1 _−α_ ( _S_ ) � � 

## **Warning** 

No guarantee on the prediction of _A_[ˆ] with scores based on ( _A_[ˆ] _−i_ ) _i_ , without assuming a form of **stability** on _A_ . 

**Jackknife+ (Barber et al., 2021b)** ~~ee~~ 

**==> picture [1608 x 1782] intentionally omitted <==**

## **Jackknife+ (Barber et al., 2021b)** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

**==> picture [1608 x 1782] intentionally omitted <==**

## **Jackknife+ (Barber et al., 2021b)** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

• LOO predictions / predictive intervals ˆ _S_ up _/_ down = � _A−i_ ( _Xn_ +1) _± |A_ ˆ _−i_ ( _Xi_ ) _− Yi |_ � _i[∪{±∞}]_ (in standard mean regression) 

**==> picture [1608 x 1782] intentionally omitted <==**

## **Jackknife+ (Barber et al., 2021b)** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

- Get _A_[ˆ] _−i_ by training _A_ on _Dn \_ ( _Xi , Yi_ ) 

• LOO predictions / predictive intervals ˆ _S_ up _/_ down = � _A−i_ ( _Xn_ +1) _± |A_ ˆ _−i_ ( _Xi_ ) _− Yi |_ � _i[∪{±∞}]_ (in standard mean regression) 

- Build the predictive interval: [ _qα,_ inf( _S_ down); _q_ 1 _−α_ ( _S_ up)] 

Recall _qβ,_ inf( _X_ 1 _, . . . , Xk_ ) := _⌊β × k⌋_ smallest value of ( _X_ 1 _, . . . , Xk_ ) 

## **Jackknife+ (Barber et al., 2021b)** 

- Based on leave-one-out (LOO) residuals 

**==> picture [85 x 36] intentionally omitted <==**

- _Dn_ = _{_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _}_ training data 

**==> picture [380 x 181] intentionally omitted <==**

**----- Start of picture text -----**<br>
• Get A [ˆ] −i by training A on Dn \  ( Xi , Yi )<br>• LOO predictions / predictive intervals<br>ˆ<br>S up / down = � A−i ( Xn +1)  ± |A  ˆ −i ( Xi )  − Yi | � i [∪{±∞}]<br>(in standard mean regression)<br>• Build the predictive interval: [ qα, inf( S down);  q 1 −α ( S up)]<br>Marginal validity of Jackknife+ Barber et al. (2021b)<br>If Dn ∪ ( Xn +1 , Yn +1) are exchangeable and A is symmetric:<br>P( Yn +1 ∈ C [�] α ( Xn +1))  ≥ 1  − 2 α .<br>Recall qβ, inf( X 1 , . . . , Xk ) :=  ⌊β × k⌋ smallest value of ( X 1 , . . . , Xk )<br>**----- End of picture text -----**<br>


**Recalibration: Approach** 

- **Split conformal** with calibration data _D_ cal = _{_ ( _Xi , Yi_ ) _}[m] i_ =1[+][test][(] _[X][,][ Y]_[ ),] all ( _m_ +1) points exchangeable. 

- _K_ base predictors _f_ 1 _, . . . , fK_ with non-conformity scores ( _sk_ ) _k∈_ [ _K_ ]. 

- **Rank–parameterised sets:** 

**==> picture [179 x 14] intentionally omitted <==**

- Choosing _Rα_ = _⌈_ (1 _− α_ )( _m_ + 1) _⌉_ gives ( _Ck[α]_[)] _[k][∈][K]_ 

**==> picture [131 x 14] intentionally omitted <==**

- **After-selection challenge:** A stochastic rule _S_[ˆ] (depending on _X_ ) picks a predictor; vanilla coverage can break—needs new calibration. 

## **Recalibration via Effective Ranks** 

- For each calibration point, set the (meta-score) 

**==> picture [78 x 17] intentionally omitted <==**

i.e., the rank of the _i_ -th point’s score calculated using the selected predictor _S_ ( _Xi , εi_ ) 

- Let _R_[ˆ] (1) _≤· · · ≤ R_[ˆ] ( _m_ ) be the order statistics and _τα_ = _⌈_ (1 _− α_ )( _m_ + 1) _⌉_ . 

**Recalibration.** 

If _S_[ˆ] _⊥D_ cal then 

**==> picture [171 x 20] intentionally omitted <==**

Gives _exact_ , finite-sample, distribution-free coverage for the _selected_ predictor, without conservative inflation. 

## **Implementing an Independent Selection Rule** 

- Independence is essential: meta-scores must stay exchangeable. 

- Use an **auxiliary dataset** _D_ aux (disjoint from _D_ cal). 

Extraslides no animations 

Extraslides no animations 

SCP CQR 

**Split Conformal Prediction (SCP)**[1] _[,]_[2] _[,]_[3] **: toy example** 

**==> picture [294 x 176] intentionally omitted <==**

**----- Start of picture text -----**<br>
Train Cal Test<br>2<br>0<br>− 2<br>0 1 2 3 4 5<br>X<br>Y<br>**----- End of picture text -----**<br>


- 1Vovk et al. (2005), _Algorithmic Learning in a Random World_ 

2 Papadopoulos et al. (2002), _Inductive Confidence Machines for Regression_ , ECML 

> 3Lei et al. (2018), _Distribution-Free Predictive Inference for Regression_ , JRSS B 

**Split Conformal Prediction (SCP)**[1] _[,]_[2] _[,]_[3] **: toy example** 

**training step** 

**==> picture [218 x 148] intentionally omitted <==**

**----- Start of picture text -----**<br>
2<br>0<br>− 2<br>0 2 4<br>X<br>Y<br>**----- End of picture text -----**<br>


   - Learn (or get) _µ_ ˆ 

- 1Vovk et al. (2005), _Algorithmic Learning in a Random World_ 

2 Papadopoulos et al. (2002), _Inductive Confidence Machines for Regression_ , ECML 

- 3Lei et al. (2018), _Distribution-Free Predictive Inference for Regression_ , JRSS B 

**calibration step** 

## **Split Conformal Prediction (SCP)**[1] _[,]_[2] _[,]_[3] **: toy example** 

**==> picture [386 x 148] intentionally omitted <==**

**----- Start of picture text -----**<br>
▶ Predict with µ ˆ<br>2<br>▶ Get the | residuals | , a.k.a.<br>conformity scores<br>0<br>▶ Compute the (1  − α ) empirical<br>− 2 quantile of<br>S =  {| residuals |} Cal  ∪{ + ∞} ,<br>noted q 1 −α  ( S )<br>0 2 4<br>X<br>Y<br>**----- End of picture text -----**<br>


- 1Vovk et al. (2005), _Algorithmic Learning in a Random World_ 

- 2 Papadopoulos et al. (2002), _Inductive Confidence Machines for Regression_ , ECML 

- 3Lei et al. (2018), _Distribution-Free Predictive Inference for Regression_ , JRSS B 

**prediction step** 

## **Split Conformal Prediction (SCP)**[1] _[,]_[2] _[,]_[3] **: toy example** 

**==> picture [218 x 169] intentionally omitted <==**

**----- Start of picture text -----**<br>
2<br>0<br>− 2<br>0 2 4<br>X<br>Back to SCP<br>Y<br>**----- End of picture text -----**<br>


   - Predict with _µ_ ˆ 

   - ˆ 

   - ▶ Build _C_[�] _α_ ( _x_ ): [ _µ_ ( _x_ ) _± q_ 1 _−α_ ( _S_ )] 

- 1Vovk et al. (2005), _Algorithmic Learning in a Random World_ 

- 2 Papadopoulos et al. (2002), _Inductive Confidence Machines for Regression_ , ECML 

- 3Lei et al. (2018), _Distribution-Free Predictive Inference for Regression_ , JRSS B 

Extraslides no animations 

SCP CQR 

**Conformalized Quantile Regression (CQR)**[5] 

**==> picture [294 x 176] intentionally omitted <==**

**----- Start of picture text -----**<br>
Train Cal Test<br>2<br>0<br>− 2<br>− 4<br>0 1 2 3 4 5<br>X<br>Y<br>**----- End of picture text -----**<br>


> 5Romano et al. (2019), _Conformalized Quantile Regression_ , NeurIPS 

**Conformalized Quantile Regression (CQR)**[5] 

**training step** 

**==> picture [218 x 148] intentionally omitted <==**

**----- Start of picture text -----**<br>
2<br>0<br>− 2<br>− 4<br>0 2 4<br>X<br>Y<br>**----- End of picture text -----**<br>


**==> picture [136 x 32] intentionally omitted <==**

**----- Start of picture text -----**<br>
▶ Learn (or get) QR [�] lower and<br>�<br>QRupper<br>**----- End of picture text -----**<br>


> 5Romano et al. (2019), _Conformalized Quantile Regression_ , NeurIPS 

**calibration step** 

## **Conformalized Quantile Regression (CQR)**[5] 

**==> picture [363 x 129] intentionally omitted <==**

**----- Start of picture text -----**<br>
+ + + + + +<br>+ + ▶ Predict with QR [�] lower and<br>�<br>QRupper<br>▶ Get the scores<br>- - S =  {Si } Cal  ∪{ + ∞}<br>-<br>- - +<br>- ▶ Compute the (1  − α ) empirical<br>+<br>quantile of S , noted q 1 −α  ( S )<br>**----- End of picture text -----**<br>


� _�→ Si_ := max QRlower ( _Xi_ ) _− Yi , Yi −_ QR[�] upper ( _Xi_ ) � � 

Back to Generalization SCP 

- 5Romano et al. (2019), _Conformalized Quantile Regression_ , NeurIPS 

## **Label shift (Podkopaev and Ramdas, 2021)** 

- Setting: 

_i.i.d. ◦_ ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _∼ PX |Y × PY ◦_ ( _Xn_ +1 _, Yn_ +1) _∼ PX |Y × P_[˜] _Y ◦_ Classification 

## **Label shift (Podkopaev and Ramdas, 2021)** 

- Setting: 

**==> picture [169 x 41] intentionally omitted <==**

- Idea: give more importance to calibration points that are closer in distribution to the test point 

## **Label shift (Podkopaev and Ramdas, 2021)** 

- Setting: 

**==> picture [169 x 28] intentionally omitted <==**

      - Classification 

- Idea: give more importance to calibration points that are closer in distribution 

   - to the test point 

- Trouble: the actual test labels are unknown 

## **Label shift (Podkopaev and Ramdas, 2021)** 

- Setting: 

**==> picture [169 x 15] intentionally omitted <==**

**==> picture [123 x 13] intentionally omitted <==**

   - Classification 

- Idea: give more importance to calibration points that are closer in distribution to the test point 

- Trouble: the actual test labels are unknown 

- In practice: 

   1. estimate the likelihood ratio _w_ ( _Yi_ ) =[d] d _[P] P_[ ˜] _[Y] Y_[ (] ( _[Y] Y[i] i_[)] )[using][algorithms][from][the][existing] label shift literature 

## **Label shift (Podkopaev and Ramdas, 2021)** 

- Setting: 

**==> picture [169 x 15] intentionally omitted <==**

**==> picture [123 x 13] intentionally omitted <==**

**==> picture [66 x 10] intentionally omitted <==**

- Idea: give more importance to calibration points that are closer in distribution to the test point 

- Trouble: the actual test labels are unknown 

- In practice: 

   1. estimate the likelihood ratio _w_ ( _Yi_ ) =[d] d _[P] P_[ ˜] _[Y] Y_[ (] ( _[Y] Y[i] i_[)] )[using][algorithms][from][the][existing] label shift literature 

**==> picture [255 x 18] intentionally omitted <==**

## **Label shift (Podkopaev and Ramdas, 2021)** 

**==> picture [47 x 11] intentionally omitted <==**

**==> picture [169 x 41] intentionally omitted <==**

- Idea: give more importance to calibration points that are closer in distribution to the test point 

- Trouble: the actual test labels are unknown 

- In practice: 

   1. estimate the likelihood ratio _w_ ( _Yi_ ) =[d] d _[P] P_[ ˜] _[Y] Y_[ (] ( _[Y] Y[i] i_[)] )[using][algorithms][from][the][existing] label shift literature 

**==> picture [289 x 67] intentionally omitted <==**

