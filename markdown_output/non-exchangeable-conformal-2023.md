Published as a conference paper at ICLR 2024 

## NON-EXCHANGEABLE CONFORMAL RISK CONTROL 

**Ant´onio Farinhas[1,2] , Chrysoula Zerva[1,2] , Dennis Ulmer[3,4] , Andr´e F. T. Martins[1,2,5]** 

1Instituto de Telecomunicac¸˜oes, 

2Instituto Superior T´ecnico, Universidade de Lisboa (Lisbon ELLIS Unit), 3IT University of Copenhagen, 4Pioneer Centre for Artificial Intelligence , 5Unbabel _{_ antonio.farinhas,chrysoula.zerva,andre.t.martins _}_ @tecnico.ulisboa.pt, dennis.ulmer@mailbox.org 

## ABSTRACT 

Split conformal prediction has recently sparked great interest due to its ability to provide formally guaranteed uncertainty sets or intervals for predictions made by black-box neural models, ensuring a predefined probability of containing the actual ground truth. While the original formulation assumes data exchangeability, some extensions handle non-exchangeable data, which is often the case in many real-world scenarios. In parallel, some progress has been made in conformal methods that provide statistical guarantees for a broader range of objectives, such as bounding the best _F_ 1-score or minimizing the false negative rate in expectation. In this paper, we leverage and extend these two lines of work by proposing _nonexchangeable conformal risk control_ , which allows controlling the expected value of any monotone loss function when the data is not exchangeable. Our framework is flexible, makes very few assumptions, and allows weighting the data based on its relevance for a given test example; a careful choice of weights may result on tighter bounds, making our framework useful in the presence of change points, time series, or other forms of distribution drift. Experiments with both synthetic and real world data show the usefulness of our method. 

## 1 INTRODUCTION 

As the use of machine learning systems for automated decision-making becomes more widespread, the demand for these systems to produce reliable and trustworthy predictions has grown significantly. In this context, conformal prediction (Papadopoulos et al., 2002; Vovk et al., 2005) has recently resurfaced as an attractive framework. Instead of providing a single output, this framework creates prediction sets or intervals that inherently account for uncertainty. These sets come with a statistical guarantee known as **coverage** , which ensures that they contain the ground truth in expectation, thereby providing a formal promise of reliability. 

The standard formulation of conformal prediction has, however, important limitations. First, it assumes that all data is **exchangeable** , a condition which is often violated in practice ( _e.g._ , when there is correlation over time or space). Second, while the predicted sets/intervals provide guarantees on coverage, they do not bound arbitrary losses, some of which may be more relevant for the situation at hand ( _e.g._ , the _F_ 1-score or the false negative rate in multilabel classification problems). Several works have been proposed to improve over these two shortcomings, namely through nonexchangeable conformal prediction (Tibshirani et al., 2019; Gibbs & Candes, 2021; Barber et al., 2023) and conformal risk control (Bates et al., 2021; Angelopoulos et al., 2023a, CRC). In this paper, we extend these lines of research and propose **non-exchangeable conformal risk control** (non-X CRC). Our main contributions are: 

• We propose a new method for conformal risk control that provides formal guarantees when the data is not exchangeable, while also achieving the same guarantees as existing methods if the data is in fact exchangeable (see Table 1 where we position our work in the literature); 

• Theorem 1 establishes a new bound on the expected loss (assumed to be monotonic and bounded), allowing weighting the calibration data based on its relevance for a given test example; 

1 

Published as a conference paper at ICLR 2024 

Table 1: Our framework combines two approaches, non-exchangeable conformal prediction and conformal risk control. Through this combination we are able to control the expected value of arbitrary monotonic loss functions when the data is not exchangeable, extending both frameworks. 

|Method|Data assumptions|Loss|
|---|---|---|
|Papadopoulos et al. (2002)|exchangeable�|miscoverage|
|Barber et al. (2023)|�|miscoverage|
|Angelopoulos et al. (2023a)|exchangeable�|nonincreasing, arbitrary|
|Angelopoulos et al. (2023a, Prop. 3)|covariate shift, known likelihood ratio�|nonincreasing, arbitrary|
|**This paper**|�|nonincreasing, arbitrary|



• We demonstrate the usefulness of our framework on three tasks: multilabel classification on synthetic data by minimizing the false negative rate; monitoring electricity usage by minimizing the _λ_ -insensitive absolute loss; and open-domain question answering by bounding the best _F_ 1-score.[1] 

Throughout the paper, we use the following definition of exchangeable data distribution, which is a weaker assumption than independent and identically distributed (i.i.d.) data. 

**Definition 1** ( **Exchangeable data distribution** ) **.** _Let X and Y designate input and output spaces. A data distribution in X × Y is said to be exchangeable if and only if we have_ P(( _Xπ_ (1) _, Yπ_ (1)) _, . . . ,_ ( _Xπ_ ( _n_ ) _, Yπ_ ( _n_ ))) = P(( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ )) _for any finite sample {_ ( _Xi, Yi_ ) _}[n] i_ =1 _[⊆X][× Y][and any permutation function][ π][.][Note that if the data distribution] is i.i.d., then it is also exchangeable, since_ P(( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ )) =[�] _[n] i_ =1[P][((] _[X][i][, Y][i]_[))] _[.]_ 

## 2 BACKGROUND 

We start by providing background on conformal prediction (Papadopoulos et al., 2002; Vovk et al., 2005) in §2.1. We then discuss recent extensions of the framework—§2.2 discusses the case where the data is non-exchangeable (Barber et al., 2023), which is often the case when models are deployed in practice. Another extension pivots from guaranteeing coverage to instead constraining the expected value of any monotone loss function (Angelopoulos et al., 2023a), useful for tasks in which the natural notion of error is not miscoverage (§2.3). 

## 2.1 CONFORMAL PREDICTION 

Although other methods exist, this paper focuses on _split_ conformal prediction (Papadopoulos et al., 2002; hereinafter referred to simply as _conformal prediction_ ). We start with a pretrained model and measure its performance on a calibration set _{_ ( _Xi, Yi_ ) _}[n] i_ =1[of][paired][examples.][Under][the] assumption of exchangeable data _{_ ( _Xi, Yi_ ) _}[n] i_ =1[+1][,][conformal][prediction][constructs][prediction][sets] with the following coverage guarantee: 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0002-10.png)


where ( _Xn_ +1 _, Yn_ +1) is a new data point and _α_ a predefined confidence level. This is accomplished through the following steps: Let _s_ ( _x, y_ ) _∈_ R be a non-conformity score function, where larger scores indicate worse agreement between _x_ and _y_ . We compute the value _q_ ˆ as the[1] _/n⌈_ ( _n_ + 1)(1 _− α_ ) _⌉_ quantile of the calibration scores and construct a prediction set as follows: 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0002-12.png)


This prediction set satisfies the coverage guarantee in Eq. (1), see _e.g._ , Angelopoulos & Bates, 2021, App. D for a proof. While this guarantee helps to ensure a certain reliability of the calibrated model, the assumption of exchangeable data is often not true when models are deployed in practice, _e.g._ , due to distribution drift in time series or correlations between different data points. 

> 1 Our code is available at https://github.com/deep-spin/non-exchangeable-crc. 

2 

Published as a conference paper at ICLR 2024 

## 2.2 NON-EXCHANGEABLE CONFORMAL PREDICTION 

Let us now consider prespecified weights _{wi}[n] i_ =1 _[∈]_[[0] _[,]_[ 1]] _[n]_[and define] _[w]_[˜] _[i]_[:=] _[w][i][/]_[(1 +][ �] _[N] i_ =1 _[w][i]_[)][.] We take a look at a generalization of conformal prediction put together by Barber et al. (2023), which provides the following coverage guarantee, also valid when exchangeability is violated: 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0003-03.png)


where _Z_ := ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _,_ ( _Xn_ +1 _, Yn_ +1) is a sequence of _n_ calibration examples followed by a test example, _Z[i]_ denotes _Z_ after swapping ( _Xi, Yi_ ) with ( _Xn_ +1 _, Yn_ +1), and _d_ TV( _Z, Z[i]_ ) is the total variation (TV) distance between _Z_ and _Z[i]_ . This is accomplished by using 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0003-05.png)


to construct prediction sets the same way as in Eq. (2). See Barber et al. (2023, §4) for a proof. It is worth noting that this method recovers standard conformal prediction when _{wi}[n] i_ =1[= 1][.][Besides,] if the data is exchangeable, then the distribution of _Z_ is equal to the distribution of _Z[i]_ , and thus using a weighted procedure does not hurt coverage according to Eq. (3), since _d_ TV( _Z, Z[i]_ ) = 0 for all _i_ . Intuitively, the “closer” to exchangeable the data is, the smaller the last term will be in Eq. (3). By choosing wisely the weights _wi_ —e.g., by setting large weights to calibration points ( _xi, yi_ ) such that _Z_ and _Z[i]_ are similarly distributed and smaller weights otherwise—tighter bounds can be obtained. For example, in time series data we may want to place larger weights on more recent observations. 

## 2.3 CONFORMAL RISK CONTROL 

Let us now consider an additional parameter _λ_ and construct prediction sets of the form _Cλ_ ( _·_ ), where larger _λ_ yield larger prediction sets, _i.e._ , _λ ≤ λ[′]_ = _⇒Cλ_ ( _._ ) _⊆Cλ′_ ( _._ ) (see Angelopoulos & Bates (2021, §4.3) for an example). Let _ℓ_ be an arbitrary (bounded) loss function that shrinks as _C_ ( _Xn_ +1) grows ( _i.e._ , that is **monotonically nonincreasing** with respect to _λ_ ). We switch from conformal methods that provide prediction sets that bound the miscoverage P� _Yn_ +1 _∈C/_ ( _Xn_ +1)� _≤ α_ to conformal risk control (Angelopoulos et al., 2023a), which provides guarantees of the form 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0003-09.png)


This is accomplished as follows. Let _Li_ ( _λ_ ) = _ℓ_ ( _Cλ_ ( _Xi_ ) _, Yi_ ) _, i_ = 1 _, . . . , n_ + 1, with _Li_ : Λ _→_ ( _−∞, B_ ] and _λ_ max := sup Λ, be an exchangeable collection of nonincreasing functions of _λ_ . Choosing an optimal _λ_[ˆ] as 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0003-11.png)


yields the guarantee in Eq. (5), see Angelopoulos et al. (2023a, §2) for a proof. When _ℓ_ ( _C_ ( _Xn_ +1) _, Yn_ +1) = **1** � _Yn_ +1 _∈C/_ ( _Xn_ +1)� is the miscoverage loss, we recover standard conformal prediction (§2.1). Note that, as required, this loss is nonincreasing. Other nonincreasing losses include the false negative rate, _λ_ -insensitive absolute error, and the best token-level _F_ 1-loss, all of which used in our experiments in §4. A limitation of the construction presented in this section is that it relies on the assumption of data exchangeability, which might be violated in practical settings. Our work circumvents this requirement, as we show next. 

## 3 NON-EXCHANGEABLE CONFORMAL RISK CONTROL 

Up to this point, we have described how to construct prediction sets/intervals with coverage guarantees for non-exchangeable data, in §2.2, and how to control the expected value of arbitrary monotone loss functions, when the data is exchangeable, in §2.3. Using the same notation as before, we now 

3 

Published as a conference paper at ICLR 2024 

present our method, _non-exchangeable conformal risk control_ , which puts together these parallel lines of research, providing guarantees of the form: 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0004-02.png)


where we additionally assume _A < B < ∞_ to be a lower bound on _Li_ : Λ _→_ [ _A, B_ ]. Let us define _Nw_ :=[�] _[N] i_ =1 _[w][i]_[.][Eq. (7) is obtained by choosing an optimal][ ˆ] _[λ]_[ as] 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0004-04.png)


We can see how Eq. (7) simultaneously mirrors both Eq. (3) and Eq. (5): for an optimal choice of _λ_ , the expected risk for a new test point is bounded by _α_ plus an extra loosening term that depends on the normalized weights _{wi}[n] i_ =1[and on the total variation distance between] _[ Z]_[and] _[ Z][i]_[.][When the] data is in fact exchangeable, we have again _d_ TV( _Z, Z[i]_ ) = 0 for all _i_ , and we recover Eq. (5), _i.e._ , our method achieves the same coverage guarantees as standard conformal risk control. Although our theoretical bound in Eq. (7) holds for any choice of weights, this result is only useful when the loosening term is small, _i.e._ , if we choose small weights _wi_ for data points _Z[i]_ with large total variation distance _d_ TV( _Z, Z[i]_ ). While the true value of this term is typically unknown, in some situations, such as distribution drift in time series, we expect it to decrease with _i_ , motivating the choice of weights that increase with _i_ . The same principle can be applied in other domains ( _e.g._ , for spatial data, one may place higher weights to points close in space to the test point). We come back to this point in §3.2. 

The result in Eq. (7) is valid when the weights are fixed, _i.e._ , data-independent. However, our result still applies in the case of data-dependent weights _wi_ = _w_ ( _Xi, Xn_ +1) if we replace � _ni_ =1 _[w]_[˜] _[i][d]_[TV][(] _[Z, Z][i]_[)][by][E] �� _ni_ =1 _[w]_[˜] _[i][d]_[TV][(] _[Z, Z][i][|][w]_[1] _[, . . . , w][n]_[)] � (see Barber et al. (2023, §4.5) for more information). We experiment with this approach in §4.3, where _wi_ is a function of the embedding similarity between _Xi_ and _Xn_ +1, showing that the new bound is still useful in practice. 

## 3.1 FORMAL GUARANTEES 

Now that we have presented an overview of our method, we proceed to providing a formal proof for the guarantee in Eq. (7). We begin with a lemma, proved in App. A, that establishes a TV bound that extends the one introduced by Barber et al. (2023): 

**Lemma 1.** _Let f_ : _S →_ [ _A, B_ ] _⊂_ R _be a bounded function on a measurable space_ ( _S, A_ ) _(where A ⊆_ 2 _[S] is a σ-algebra) and let P and Q be two probability measures on_ ( _S, A_ ) _. Then_ 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0004-10.png)


Note that when _f_ ( _t_ ) = **1** � _t ∈ V_ � for some event _V ∈A_ , the left-hand side becomes _|P_ ( _V_ ) _−Q_ ( _V_ ) _|_ and we recover the bound used in the proof of Barber et al. (2023, §6.2). 

We now state the main result. The proof technique is similar to that of Barber et al. (2023), but instead of modeling the event of a variable belonging to a “strange set”, we model expectations of loss functions that depend on a calibration variable. See App. B for the full proof. 

**Theorem 1** ( **Non-exchangeable conformal risk control** ) **.** _Assume that for all_ ( _x, y_ ) _∈X × Y the loss L_ ( _λ_ ; ( _x, y_ )) _is nonincreasing in λ and bounded as A ≤ L_ ( _λ_ ; ( _x, y_ )) _≤ B for any λ. Let_ 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0004-14.png)


_be a sequence of n calibration examples followed by a test example, and let w_ 1 _, . . . , wn ∈ and_ [0 _,_ 1] _w_ ˜ _[n] nbe_ +1 _**data-independent**_ = 1 _/_ ( _Nw_ + 1) _. Let weights. α ∈_ [ _A, BDefine_ ] _be the maximum tolerable risk, and define Nw_ =[�] _[n] i_ =1 _[w][i][,][w]_[˜] _[i]_[=] _[ w][i][/]_[(] _[N][w]_[ + 1)] _[ for][ i][ ∈]_[[] _[n]_[]] 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0004-16.png)


4 

Published as a conference paper at ICLR 2024 

_where R_[ˆ] _n_ ( _λ_ ) _is the weighted empirical risk in the calibration set:_ 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0005-02.png)


_Then, we have_ 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0005-04.png)


The next section illustrates how we can make practical use of this result to minimize loss functions beyond the miscoverage loss in the presence of non-exchangeable data distributions. 

## 3.2 HOW TO CHOOSE WEIGHTS 

To make practical use of Theorem 1, we need a procedure to choose the weights _wi_ . We next ˜ suggest a strategy based on regularized minimization of the coverage gap _g_ ( ˜ _w_ 1 _, ..., wn_ ) := ( _B − A_ minimizing)[�] _[n] i_ =1 _[w]_[˜] _[i][d]_ this[TV][(] gap _[Z, Z]_ would _[i]_[)][ via the maximum entropy principle (Jaynes, 1957).] lead to _w_ ˜ _i_ = 0 for all _i ∈_ [ _n_ ] and _w_ ˜ _n_ +1 = 1, which[Note first that simply] ignores all the calibration data and leads to an infeasible _λ_[ˆ] in Eq. (6). In general, if all weights _wi_ are too small, thisweightsleadstootolargea very(e.g.large _wi w_ = _n_ +11 forandallan _i_ , unreasonablywhich leads tolarge _w_ ˜ _i_ = _λ_[ˆ] .1 _/_ On( _n_ + 1)the otherfor _i_ extreme, _∈_ [ _n_ + 1]having) ignoresall the non-exchangeability of the data and may lead to a large coverage gap. Therefore, it is necessary to find a good balance between ensuring a small coverage gap but at the same time ensuring that theby definition,distributionwe _w_ ˜must1 _, ..., w_ have˜ _n_ +1 _w_ ˜is _n_ +1not _≥_ too _w_ ˜ _i_ peaked,for all _i_ i.e., _∈_ [that _n_ ], thisit hascansufficientlybe formalizedhighasentropy.the followingSince regularized minimization problem: 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0005-08.png)


˜ where _H_ ( ˜ _w_ 1 _, ..., wn_ +1) = _−_[�] _[n] i_ =1[+1] _[w]_[˜] _[i]_[ log] _[w]_[˜] _[i]_[is][the][entropy][function][and] _[β][>]_[0][is][a][temperature] ˜ parameter. The solution of this problem is _wi ∝_ exp( _−β_ ( _B − A_ ) _d_ TV( _Z, Z[i]_ )) for _i ∈_ [ _n_ + 1]. 

Although in general _d_ TV( _Z, Z[i]_ ) is not known, it is possible in some scenarios to bound or to estimate this quantity: for example, when variables are independent but not identically distributed, it can be shown that _d_ TV( _Z, Z[i]_ ) _≤_ 2 _d_ TV( _Zi, Zn_ +1) (Barber et al., 2023, Lemma 1); and it is possible to upper bound the total variation distance as a function of the (more tractable and amenable to estimation) Kullback-Leibler divergence, e.g., via Pinsker’s or Bretagnolle-Huber’s inequalities (Bretagnolle & Huber, 1979; Csisz´ar & K¨orner, 2011), which may provide good heuristics. For example, in a time series under a distribution shift scenario bounded with a Lipschitztype condition _d_ TV( _Zi, Zn_ +1) _≤ ϵ_ ( _n_ + 1 _− i_ ) for some _ϵ >_ 0 (see e.g. (Barber et al., 2023, §4.4)), we could replace˜ _d_ TV( _Z, Z[i]_ ) in Eq. (13) by this upper bound to obtain the maxent solution _wi ∝_ exp( _−βϵ_ ( _n_ + 1 _− i_ )) = _ρ[n]_[+1] _[−][i]_ , where _ρ_ = exp( _−βϵ_ ) _∈_ (0 _,_ 1). This exponential decay of the weights was suggested by (Barber et al., 2023); our maximum entropy heuristic provides further justification for that choice. We use this strategy in some of our experiments in §4. 

## 4 EXPERIMENTS 

In this section, we turn to demonstrating the validity of our theoretical results in three different tasks using different nonincreasing losses: a **multilabel classification** problem using synthetic time series data, minimizing the false negative rate (§4.1), a problem involving **monitoring electricity usage** , minimizing the _λ_ -insensitive absolute loss (§4.2), and an **open-domain question answering** (QA) 

5 

Published as a conference paper at ICLR 2024 

task, where we control the best token-level _F_ 1-score (§4.3). Throughout, we report our method alongside a conformal risk control (CRC) baseline that predicts _λ_[ˆ] following Eq. (6). 

## 4.1 MULTILABEL CLASSIFICATION IN A TIME SERIES 

We start by validating our approach on synthetic data, before moving to real-world data in the following subsections. To this end, we modified the synthetic regression experiment of Barber et al. (2023, §5.1) to turn it into a multilabel classification problem with up to _M_ = 10 different labels. We consider three different setups: 

1. **Exchangeable (i.i.d.) data:** We sample _N_ = 2000 i.i.d. data points ( _Xi, Yi_ ) _∈_ iid 

R _[M] ×_ R _[M]_ . We sample _Xi_ from a Gaussian distribution, _Xi ∼N_ ( **0** _,_ _**I** M_ ), and we set _Yi ∼_ **sign** ( _**W** Xi_ + _**b**_ + _._ 1 _N_ ( **0** _,_ _**I** M_ )). The coefficient matrix _**W**_ is set to the identity matrix _**I** M_ and the biases to _**b**_ = _−_ **0** _._ **5** , to encourage a sparse set of labels. 

2. **Changepoints:** We follow setting (1) and sample _N_ = 2000 i.i.d. data points ( _Xi, Yi_ ), iid 

setting _Xi ∼N_ ( **0** _,_ _**I** M_ ) and _Yi ∼_ **sign** ( _**W**_[(] _[k]_[)] _Xi_ + _**b**_ + _._ 1 _N_ ( **0** _,_ _**I** M_ )), again with _**b**_ = _−_ **0** _._ **5** . We start with the same coefficients _**W**_[(0)] = _**I** M_ and for every changepoint _k >_ 0 we rotate the coefficients such that _**W** i,j_[(] _[k]_[)] = _**W** i_[(] _−[k]_ 1 _[−] ,j_[1)][for] _[i][>]_[1][and] _**[W]**_[ (] 1 _,j[k]_[)][=] _**[W]**_[ (] _M,j[k][−]_[1)] . Following Barber et al. (2023), we use two changepoints ( _k_ = 2) at timesteps 500 and 1500. 

3. **Distribution drift:** We follow setting (2) and sample _N_ = 2000 i.i.d. data points ( _Xi, Yi_ ), iid 

with _Xi ∼N_ ( **0** _,_ _**I** M_ ) and _Yi ∼_ **sign** ( _**W**_[(] _[k]_[)] _Xi_ + _**b**_ + _._ 1 _N_ ( **0** _,_ _**I** M_ )), with _**b**_ as above. Again, we start with _**W**_[(0)] = _**I** M_ but now we set _**W**_[(] _[N]_[)] to the last matrix of setting (2). We then compute each intermediate _**W**_[(] _[k]_[)] by linearly interpolating between _**W**_[(0)] and _**W**_[(] _[N]_[)] . 

After a warmup period of 200 time points, at each time step _n_ = 200 _, . . . , N −_ 1 we assign odd indices to the training set, even indices to the calibration set, and we let _Xn_ +1 be the test point. We fit _M_ independent logistic regression models to the training data to obtain predictors for each label; we let _fm_ ( _Xi_ ) denote the estimated probability of the _m_[th] label according to the model. Based on this predictor, we define prediction sets _Cλ_ ( _Xi_ ) := _{m ∈_ [ _M_ ] : _fm_ ( _Xi_ ) _≥_ 1 _− λ}_ . We compare standard CRC with non-exchangeable (non-X) CRC, for which we use weights _wi_ = 0 _._ 99 _[n]_[+1] _[−][i]_ and predict _λ_[ˆ] following Eq. (10). In both cases, we minimize the **false negative rate** (FNR):[2] 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0006-08.png)


Note that this loss is nonincreasing in _λ_ , as required. App. C contains additional experiments considering _λ_ to be the number of active labels and using _Cλ_ ( _Xi_ ) = top- _λ_ ( _**f**_ ( _Xi_ )). 

Fig. 1 shows results averaged across 10 independent trials for _α_ = 0 _._ 2, summarized in Table 2. We see that the performance of both methods is comparable when the data is i.i.d, with non-X CRC being slightly more conservative. However, when the data is not exchangeable due to the presence of changepoints or distribution drift, our proposed method is considerably better. In particular, after the changepoints in setting (2), non-X CRC is able to achieve the desired risk level more rapidly; in setting (3), the performance of standard CRC gradually drops over time—a problem that can be mitigated by accounting for non-exchangeability introduced by the distribution drift. Importantly, while the average risk is above the predefined threshold for standard CRC for settings (2) and (3) (0 _._ 246 and 0 _._ 225, respectively), our method achieves the desired risk level on average (0 _._ 196 and 0 _._ 182, respectively). 

## 4.2 MONITORING ELECTRICITY USAGE 

We use the ELEC2 dataset (Harries, 1999), which tracks electricity transfer between two states in Australia, considering the subset of the data used by Barber et al. (2023), which contains 3444 time points. The data points correspond to the 09:00am - 12:00pm timeframe and we use the price (nswprice, vicprice) and demand (nswdemand, vicdemand) variables as input features, 

> 2With some abuse of notation, we use _Yi ⊆{_ 1 _, . . . , M }_ to denote the set of gold labels with value +1. 

6 

Published as a conference paper at ICLR 2024 

Figure 1: Average loss (top) and _λ_[ˆ] (bottom) over 10 independent trials for settings (1), (2), and (3). We smooth all the curves by taking a rolling average with a window of 30 time points. 

Table 2: Scalar statistics (mean/median) for settings (1), (2), and (3) for the multilabel classification problem using synthetic time series data reported in §4.1. 

|Method|Setting 1 (i.i.d. data)|Setting 2 (changepoints)|Setting 3 (distribution drift)|
|---|---|---|---|
|CRC|0.191 / 0.183|0.246 / 0.228|0.225 / 0.218|
|non-X CRC|**0.181 / 0.175**|**0.196 / 0.183**|**0.182 / 0.175**|



_xi_ to predict the target transfer values _yi_ . We also consider a randomly permuted version of the dataset such that the exchangeability assumption is satisfied. We use the same definitions and settings of §4.1, but this time we fit a least squares regression model to predict the transfer ˆ values, _yi_ = _f_ ( _xi_ ), at each time step. For non-X CRC, we use weights _wi_ = 0 _._ 99 _[n]_[+1] _[−][i]_ and we also experiment with weighted least-squares regression, placing weights _ti_ = _wi_ on each data point (non-X CRC + WLS). For both standard and non-X CRC we control the residual (distance) with respect to the confidence interval _Cλ_ ( _xi_ ) = [ _f_ ( _xi_ ) _− λ, f_ ( _xi_ ) + _λ_ ], where _f_ ( _xi_ ) corresponds to the predicted values for transfer. We use the _λ_ **-insensitive absolute loss** , a loss function commonly used in support vector regression (Sch¨olkopf et al., 1998; Vapnik, 1999): 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0007-05.png)


We experiment using _λ ∈_ [0 _,_ 1] with a step of 0 _._ 01. Since we are using the normalized ELEC2 dataset, transfer takes values in [0 _,_ 1], thus _L_ ( _λ_ ; ( _f_ ( _xi_ ) _, yi_ )) is bounded by _B_ = 1. By definition _L_ ( _λ_ ; ( _f_ ( _xi_ ) _, yi_ )) is nonincreasing with respect to _λ_ . 

Fig. 2 shows results for the aforementioned setup. We can observe that in the original setting, both non-exchangeable methods approximate well the desired loss threshold even during the timesteps at which the data suffers from distribution drift. Specifically, as observed by Barber et al. (2023), the electricity _transfer_ values are more noisy during the middle of the time range and we can see that the standard CRC + LS method underestimates the _λ_[ˆ] for these data points resulting in increased loss, above the desired one. With respect to the CRC + WLS setup, we can see that it manages to reach the desired loss with a smaller interval width on average, indicating that fitting the weighted leastsquares model performs better when the data distribution changes, allowing for smaller _λ_ during calibration. For the permuted data that simulates the exchangeable data scenario, we can see that all methods perform similarly, reaching the desired loss, as expected. 

7 

Published as a conference paper at ICLR 2024 

Figure 2: Results on ELEC2 data for _α_ = 0 _._ 05 and _λ_ defined by the prediction interval width. Presented curves are smoothed by taking a rolling average with a window of 300 data points per timestep. 

Figure 3: _F_ 1-score control on the Natural Questions dataset. Average set size (left) and risk (right) over 1000 independent random data splits. 

## 4.3 OPEN-DOMAIN QUESTION ANSWERING 

We now shift to open-domain QA, a task that consists in answering factoid questions using a large collection of documents. This is done in two stages, following Angelopoulos et al. (2023a): _(i)_ a retriever model (Karpukhin et al., 2020, DPR) selects passages from Wikipedia that might contain the answer to the question, and _(ii)_ a reader model examines the retrieved contexts and extract text sub-spans that serve as candidate answers.[3] 

Given a vocabulary _V_ , each _Xi ∈Z_ is a question and _Yi ∈Z[k]_ a set of _k_ correct answers, where _Z_ := _V[m]_ (we assume that _Xi_ and _Yi_ are sequences composed of up to _m_ tokens). We calibrate the **best token-based** _F_ 1 **-score** of the prediction set[4] , taken over all pairs of predictions and answers, 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0008-06.png)


which is nonincreasing and upper-bounded by _B_ = 1. We consider a CRC baseline that predicts _λ_[ˆ] following Eq. (6). For non-X CRC, we choose weights _{wi}[n] i_ =1[by computing the dot product be-] tween the embedding representations of _{Xi}[n] i_ =1[and] _[ X][n]_[+1][, obtained using a sentence-transformer] model (Reimers & Gurevych, 2019) designed for semantic search,[5] and predict _λ_[ˆ] following Eq. (10). While in standard CRC _λ_[ˆ] is the same for each test example, this is not the case for non-X CRC. 

> 3Enumerating all possible answers is intractable, and thus we retrieve the top several hundred candidate answers, extracted from the top 100 passages (which is sufficient to control all risks). 

> 4This is the same loss used by Angelopoulos et al. (2023a). 

> 5 We use the multi-qa-mpnet-base-dot-v1 model available at https://huggingface.co/ sentence-transformers/multi-qa-mpnet-base-dot-v1. 

8 

Published as a conference paper at ICLR 2024 

While Theorem 1 requires the weights to be independent of the test example, we relax this assumption by setting higher weights for questions in a “neighborhood” of _Xn_ +1 (see §3). Intuitively, we could think of a situation where the questions are posed by multiple users, each of which may have a tendency to ask semantically similar questions or from the same domain. In this case, we could choose _a priori_ higher weights for closer domains/users without violating this assumption. 

We use the Natural Questions dataset (Kwiatkowski et al., 2019; Karpukhin et al., 2020), considering _n_ = 2500 points for calibration and 1110 for evaluation. Following Angelopoulos et al. (2023a), we use _α_ = 0 _._ 3 and report results over 1000 trials in Fig. 3. While the test risk is similar in both cases (0 _._ 30 _±_ 0 _._ 015), the prediction sets of our method are considerably smaller than those of standard CRC (23 _._ 0 _±_ 1 _._ 47 vs. 24 _._ 6 _±_ 1 _._ 83, respectively). By choosing appropriate weights we can better estimate the set size needed to obtain the desired risk level, while standard CRC tends to overestimate the set size to reach the same value. We thus obtain better estimates of confidence over the predictions. 

## 5 RELATED WORK 

Conformal prediction (Gammerman et al., 1998; Vovk et al., 1999; Saunders et al., 1999) has proven to be a useful tool for obtaining uncertainty sets/intervals for the predictions of machine learning models, having found a variety of extensions and applications over the years. Among these are _split conformal prediction_ (Papadopoulos et al., 2002), which does not require retraining the predictor and instead uses a held-out dataset and _cross-conformal prediction_ (Vovk, 2015), which is a hybrid between split conformal prediction and cross-validation. Some of these methods have recently been applied in tasks such as language modeling (Schuster et al., 2022), molecular design (Fannjiang et al., 2022), pose estimation (Yang & Pavone, 2023), and image denoising (Teneggi et al., 2023). 

In addition to the works discussed in §2, several extensions to non-exchangeable data have been proposed for time series (Chernozhukov et al., 2018; 2021b; Xu & Xie, 2021; Stankeviciute et al., 2021; Lin et al., 2022; Zaffran et al., 2022; Sun & Yu, 2022; Schlembach et al., 2022; Angelopoulos et al., 2023b), covariate shift (Tibshirani et al., 2019), label shift (Podkopaev & Ramdas, 2021), and others (Cauchois et al., 2020; Gibbs & Candes, 2021; Chernozhukov et al., 2021a; Gibbs & Cand`es, 2022; Oliveira et al., 2022; Guan, 2022). Moreover, there is recent work aiming at controlling arbitrary risks in an online setting (Feldman et al., 2022). The ideas, assumptions, or formal guarantees in these works are different to ours—we refer the reader to the specific papers for further information. 

Angelopoulos et al. (2023a) touch the case of conformal risk control under _covariate shift_ (Proposition 3; without providing any empirical validation), explaining how to generalize the work of Tibshirani et al. (2019) to any monotone risk under the strong assumption that the distribution of _Y |X_ is the same for both the training and test data and that the likelihood ratio between _X_ test and _X_ train is known or can be accurately estimated using a large set of test data. This result is orthogonal to ours. Besides, they quantify how unweighted conformal risk control degrades when there is an arbitrary distribution shift. Our work is more general and differs in several significant ways: we allow for an arbitrary design of weights, the bounds can be tighter, and the losses are bounded in [ _A, B_ ], not necessarily in [0 _, B_ ]. Specifically, their Proposition 4 is a particular case of our main result (choosing _A_ = 0 and unitary weights), which we use as a baseline in our experiments. 

## 6 CONCLUSIONS 

We have proposed a new method for conformal risk control, which is still valid when the data is not exchangeable ( _e.g._ , due to an arbitrary distribution shift) and provides a tighter bound on the expected loss than that of previous work. Our simulated experiments illustrate how non-exchangeable conformal risk control effectively provides prediction sets satisfying the risk requirements in the presence of non-exchangeable data (in particular, in the presence of change points and distribution drift), without sacrificing performance if the data is in fact exchangeable. Additional experiments with real data validate the usefulness of our approach. 

Our work opens up exciting possibilities for research on risk control in challenging settings. For instance, it is an attractive framework for providing guarantees on the predictions of large language models, being of particular interest in tasks involving language generation, medical data (Jalali et al., 2020), or reinforcement learning (Wang et al., 2023), where the i.i.d. assumption does not hold. 

9 

Published as a conference paper at ICLR 2024 

## ACKNOWLEDGMENTS 

We would like to thank M´ario Figueiredo, the SARDINE lab team, and the anonymous reviewers for helpful discussions. This work was built on open-source software; we acknowledge Van Rossum & Drake (2009); Oliphant (2006); Virtanen et al. (2020); Walt et al. (2011); Pedregosa et al. (2011), and Paszke et al. (2019). This work was supported by EU’s Horizon Europe Research and Innovation Actions (UTTER, contract 101070631), by the project DECOLLAGE (ERC-2022-CoG 101088763), by the Portuguese Recovery and Resilience Plan through project C645008882-00000055 (Center for Responsible AI), and by Fundac¸˜ao para a Ciˆencia e Tecnologia through contract UIDB/50008/2020. 

## REFERENCES 

- Anastasios N Angelopoulos and Stephen Bates. A gentle introduction to conformal prediction and distribution-free uncertainty quantification. _arXiv preprint arXiv:2107.07511_ , 2021. 

- Anastasios N. Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, and Tal Schuster. Conformal risk control, 2023a. 

- Anastasios N. Angelopoulos, Emmanuel J. Candes, and Ryan J. Tibshirani. Conformal pid control for time series prediction, 2023b. 

- Rina Foygel Barber, Emmanuel J. Cand`es, Aaditya Ramdas, and Ryan J. Tibshirani. Conformal prediction beyond exchangeability. _The Annals of Statistics_ , 51(2):816 – 845, 2023. doi: 10. 1214/23-AOS2276. URL https://doi.org/10.1214/23-AOS2276. 

- Stephen Bates, Anastasios Angelopoulos, Lihua Lei, Jitendra Malik, and Michael Jordan. Distribution-free, risk-controlling prediction sets. _J. ACM_ , 68(6), sep 2021. ISSN 0004-5411. doi: 10.1145/3478535. URL https://doi.org/10.1145/3478535. 

- Jean Bretagnolle and Catherine Huber. Estimation des densit´es: risque minimax. _Zeitschrift f¨ur Wahrscheinlichkeitstheorie und verwandte Gebiete_ , 47:119–137, 1979. 

- Maxime Cauchois, Suyash Gupta, Alnur Ali, and John C Duchi. Robust validation: Confident predictions even when distributions shift. _arXiv preprint arXiv:2008.04267_ , 2020. 

- Victor Chernozhukov, Kaspar W¨uthrich, and Zhu Yinchu. Exact and robust conformal inference methods for predictive machine learning with dependent data. In S´ebastien Bubeck, Vianney Perchet, and Philippe Rigollet (eds.), _Proceedings of the 31st Conference On Learning Theory_ , volume 75 of _Proceedings of Machine Learning Research_ , pp. 732–749. PMLR, 06–09 Jul 2018. URL https://proceedings.mlr.press/v75/chernozhukov18a.html. 

- Victor Chernozhukov, Kaspar W¨uthrich, and Yinchu Zhu. Distributional conformal prediction. _Proceedings of the National Academy of Sciences_ , 118(48):e2107794118, 2021a. doi: 10.1073/pnas.2107794118. URL https://www.pnas.org/doi/abs/10.1073/pnas. 2107794118. 

- Victor Chernozhukov, Kaspar W¨uthrich, and Yinchu Zhu. An exact and robust conformal inference method for counterfactual and synthetic controls. _Journal of the American Statistical Association_ , 116(536):1849–1864, Jun 2021b. ISSN 1537-274X. doi: 10.1080/01621459.2021.1920957. URL http://dx.doi.org/10.1080/01621459.2021.1920957. 

Imre Csisz´ar and J´anos K¨orner. _Information theory: coding theorems for discrete memoryless systems_ . Cambridge University Press, 2011. 

- Clara Fannjiang, Stephen Bates, Anastasios N. Angelopoulos, Jennifer Listgarten, and Michael I. Jordan. Conformal prediction under feedback covariate shift for biomolecular design. _Proceedings of the National Academy of Sciences_ , 119(43):e2204569119, 2022. doi: 10. 1073/pnas.2204569119. URL https://www.pnas.org/doi/abs/10.1073/pnas. 2204569119. 

- Shai Feldman, Liran Ringel, Stephen Bates, and Yaniv Romano. Achieving risk control in online learning settings, 2022. 

10 

Published as a conference paper at ICLR 2024 

- Alexander Gammerman, Volodya Vovk, and Vladimir Vapnik. Learning by transduction. In Gregory F. Cooper and Seraf´ın Moral (eds.), _UAI ’98: Proceedings of the Fourteenth Conference on Uncertainty in Artificial Intelligence, University of Wisconsin Business School, Madison, Wisconsin, USA, July 24-26, 1998_ , pp. 148–155. Morgan Kaufmann, 1998. 

- Isaac Gibbs and Emmanuel Candes. Adaptive conformal inference under distribution shift. In M. Ranzato, A. Beygelzimer, Y. Dauphin, P.S. Liang, and J. Wortman Vaughan (eds.), _Advances in Neural Information Processing Systems_ , volume 34, pp. 1660–1672. Curran Associates, Inc., 2021. URL https://proceedings.neurips.cc/paper_files/ paper/2021/file/0d441de75945e5acbc865406fc9a2559-Paper.pdf. 

- Isaac Gibbs and Emmanuel Cand`es. Conformal inference for online prediction with arbitrary distribution shifts, 2022. 

- Leying Guan. Localized conformal prediction: a generalized inference framework for conformal prediction. _Biometrika_ , 110(1):33–50, Jul 2022. ISSN 1464-3510. doi: 10.1093/biomet/asac040. URL http://dx.doi.org/10.1093/biomet/asac040. 

- Michael Harries. Splice-2 comparative evaluation: Electricity pricing. In _Technical report, University of New South Wales_ , 1999. 

- Ali Jalali, Hannah Lonsdale, Nhue Do, Jacquelin Peck, Monesha Gupta, Shelby Kutty, Sharon R. Ghazarian, Jeffrey P. Jacobs, Mohamed Rehman, and Luis M. Ahumada. Deep learning for improved risk prediction in surgical outcomes. _Scientific Reports_ , 10(1):9289, 2020. doi: 10.1038/ s41598-020-62971-3. URL https://doi.org/10.1038/s41598-020-62971-3. 

Edwin T Jaynes. Information theory and statistical mechanics. _Physical review_ , 106(4):620, 1957. 

- Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih. Dense passage retrieval for open-domain question answering. In _Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pp. 6769–6781, Online, November 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.550. URL https://aclanthology.org/2020. emnlp-main.550. 

- Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, Kristina Toutanova, Llion Jones, Matthew Kelcey, Ming-Wei Chang, Andrew M. Dai, Jakob Uszkoreit, Quoc Le, and Slav Petrov. Natural questions: A benchmark for question answering research. _Transactions of the Association for Computational Linguistics_ , 7:452–466, 2019. doi: 10.1162/tacl ~~a 0~~ 0276. URL https://aclanthology.org/Q19-1026. 

- Zhen Lin, Shubhendu Trivedi, and Jimeng Sun. Conformal prediction intervals with temporal dependence. _Transactions on Machine Learning Research_ , 2022. ISSN 2835-8856. URL https://openreview.net/forum?id=8QoxXTDcsH. 

- Alfred M¨uller. Integral probability metrics and their generating classes of functions. _Advances in Applied Probability_ , 29(2):429–443, 1997. ISSN 00018678. URL http://www.jstor. org/stable/1428011. 

Travis E Oliphant. _A guide to NumPy_ , volume 1. Trelgol Publishing USA, 2006. 

- Roberto I. Oliveira, Paulo Orenstein, Thiago Ramos, and Jo˜ao Vitor Romano. Split conformal prediction for dependent data, 2022. 

- Harris Papadopoulos, Kostas Proedrou, Volodya Vovk, and Alex Gammerman. Inductive confidence machines for regression. In Tapio Elomaa, Heikki Mannila, and Hannu Toivonen (eds.), _Machine Learning: ECML 2002_ , pp. 345–356, Berlin, Heidelberg, 2002. Springer Berlin Heidelberg. ISBN 978-3-540-36755-0. 

11 

Published as a conference paper at ICLR 2024 

- Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison, Andreas Kopf, Edward Yang, Zachary DeVito, Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang, Junjie Bai, and Soumith Chintala. Pytorch: An imperative style, high-performance deep learning library. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alch´e-Buc, E. Fox, and R. Garnett (eds.), _Advances in Neural Information Processing Systems 32_ , pp. 8024–8035. Curran Associates, Inc., 2019. 

- F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay. Scikit-learn: Machine learning in Python. _Journal of Machine Learning Research_ , 12:2825–2830, 2011. 

- Aleksandr Podkopaev and Aaditya Ramdas. Distribution-free uncertainty quantification for classification under label shift. In Cassio de Campos and Marloes H. Maathuis (eds.), _Proceedings of the Thirty-Seventh Conference on Uncertainty in Artificial Intelligence_ , volume 161 of _Proceedings of Machine Learning Research_ , pp. 844–853. PMLR, 27–30 Jul 2021. URL https://proceedings.mlr.press/v161/podkopaev21a.html. 

- Nils Reimers and Iryna Gurevych. Sentence-BERT: Sentence embeddings using Siamese BERTnetworks. In _Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)_ , pp. 3982–3992, Hong Kong, China, November 2019. Association for Computational Linguistics. doi: 10.18653/v1/D19-1410. URL https://aclanthology.org/ D19-1410. 

- Craig Saunders, Alexander Gammerman, and Volodya Vovk. Transduction with confidence and credibility. In _Proceedings of the Sixteenth International Joint Conference on Artificial Intelligence_ , IJCAI ’99, pp. 722–726, San Francisco, CA, USA, 1999. Morgan Kaufmann Publishers Inc. ISBN 1558606130. 

- Filip Schlembach, Evgueni Smirnov, and Irena Koprinska. Conformal multistep-ahead multivariate time-series forecasting. In Ulf Johansson, Henrik Bostr¨om, Khuong An Nguyen, Zhiyuan Luo, and Lars Carlsson (eds.), _Proceedings of the Eleventh Symposium on Conformal and Probabilistic Prediction with Applications_ , volume 179 of _Proceedings of Machine Learning Research_ , pp. 316–318. PMLR, 24–26 Aug 2022. URL https://proceedings.mlr.press/v179/ schlembach22a.html. 

- Bernhard Sch¨olkopf, Peter Bartlett, Alex Smola, and Robert C Williamson. Shrinking the tube: a new support vector regression algorithm. _Advances in neural information processing systems_ , 11, 1998. 

- Tal Schuster, Adam Fisch, Jai Gupta, Mostafa Dehghani, Dara Bahri, Vinh Q. Tran, Yi Tay, and Donald Metzler. Confident adaptive language modeling. In Alice H. Oh, Alekh Agarwal, Danielle Belgrave, and Kyunghyun Cho (eds.), _Advances in Neural Information Processing Systems_ , 2022. URL https://openreview.net/forum?id=uLYc4L3C81A. 

- Kamile Stankeviciute, Ahmed M Alaa, and Mihaela van der Schaar. Conformal time-series forecasting. _Advances in neural information processing systems_ , 34:6216–6228, 2021. 

- Sophia Sun and Rose Yu. Copula conformal prediction for multi-step time series forecasting, 2022. 

- Jacopo Teneggi, Matthew Tivnan, Web Stayman, and Jeremias Sulam. How to trust your diffusion model: A convex optimization approach to conformal risk control. In Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara Engelhardt, Sivan Sabato, and Jonathan Scarlett (eds.), _Proceedings of the 40th International Conference on Machine Learning_ , volume 202 of _Proceedings of Machine Learning Research_ , pp. 33940–33960. PMLR, 23–29 Jul 2023. URL https://proceedings.mlr.press/v202/teneggi23a.html. 

- Ryan J Tibshirani, Rina Foygel Barber, Emmanuel Candes, and Aaditya Ramdas. Conformal prediction under covariate shift. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alch´e-Buc, E. Fox, 

12 

Published as a conference paper at ICLR 2024 

and R. Garnett (eds.), _Advances in Neural Information Processing Systems_ , volume 32. Curran Associates, Inc., 2019. URL https://proceedings.neurips.cc/paper_files/ paper/2019/file/8fb21ee7a2207526da55a679f0332de2-Paper.pdf. 

- Guido Van Rossum and Fred L. Drake. _Python 3 Reference Manual_ . CreateSpace, Scotts Valley, CA, 2009. ISBN 1441412697. 

- Vladimir Vapnik. _The nature of statistical learning theory_ . Springer science & business media, 1999. 

- Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, St´efan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, CJ Carey,[˙] Ilhan Polat, Yu Feng, Eric W. Moore, Jake Vand erPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E. A. Quintero, Charles R Harris, Anne M. Archibald, Antˆonio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1. 0 Contributors. SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. _Nature Methods_ , 2020. doi: https://doi.org/10.1038/s41592-019-0686-2. 

- Vladimir Vovk. Cross-conformal predictors. _Annals of Mathematics and Artificial Intelligence_ , 74(1):9–28, 2015. doi: 10.1007/s10472-013-9368-4. URL https://doi.org/10.1007/ s10472-013-9368-4. 

- Vladimir Vovk, Alex Gammerman, and Glenn Shafer. _Algorithmic Learning in a Random World_ . Springer-Verlag, Berlin, Heidelberg, 2005. ISBN 0387001522. 

- Volodya Vovk, Alexander Gammerman, and Craig Saunders. Machine-learning applications of algorithmic randomness. In _Proceedings of the Sixteenth International Conference on Machine Learning_ , ICML ’99, pp. 444–453, San Francisco, CA, USA, 1999. Morgan Kaufmann Publishers Inc. ISBN 1558606122. 

- St´efan van der Walt, S Chris Colbert, and Gael Varoquaux. The NumPy array: a structure for efficient numerical computation. _Computing in Science & Engineering_ , 13(2):22–30, 2011. 

- Jun Wang, Jiaming Tong, Kaiyuan Tan, Yevgeniy Vorobeychik, and Yiannis Kantaros. Conformal temporal logic planning using large language models: Knowing when to do what and when to ask for help, 2023. 

- Chen Xu and Yao Xie. Conformal prediction interval for dynamic time-series. In Marina Meila and Tong Zhang (eds.), _Proceedings of the 38th International Conference on Machine Learning_ , volume 139 of _Proceedings of Machine Learning Research_ , pp. 11559–11569. PMLR, 18–24 Jul 2021. URL https://proceedings.mlr.press/v139/xu21h.html. 

- Heng Yang and Marco Pavone. Object pose estimation with statistical guarantees: Conformal keypoint detection and geometric uncertainty propagation. _2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ , Jun 2023. doi: 10.1109/cvpr52729.2023.00864. URL http://dx.doi.org/10.1109/CVPR52729.2023.00864. 

- Margaux Zaffran, Olivier Feron, Yannig Goude, Julie Josse, and Aymeric Dieuleveut. Adaptive conformal predictions for time series. In Kamalika Chaudhuri, Stefanie Jegelka, Le Song, Csaba Szepesvari, Gang Niu, and Sivan Sabato (eds.), _Proceedings of the 39th International Conference on Machine Learning_ , volume 162 of _Proceedings of Machine Learning Research_ , pp. 25834–25866. PMLR, 17–23 Jul 2022. URL https://proceedings.mlr.press/ v162/zaffran22a.html. 

## A PROOF OF LEMMA 1 

The TV distance can be written as an integral probability metric (M¨uller, 1997): 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0013-15.png)


13 

Published as a conference paper at ICLR 2024 

Now, we define _m_ = ( _A_ + _B_ ) _/_ 2, _v_ = ( _B − A_ ) _/_ 2, and _f_[¯] = ( _f − m_ ) _/v_ : _S →_ [ _−_ 1 _,_ 1]. Noticing that for any _c ∈_ R, we have E _P_ [ _f_ ] _−_ E _Q_ [ _f_ ] = E _P_ [ _f_ + _c_ ] _−_ E _Q_ [ _f_ + _c_ ], we can evaluate the difference in expectations as 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0014-02.png)


Repeating with _f_[¯] = ( _m − f_ ) _/v_ (which is also in [ _−_ 1 _,_ 1]), yields a similar upper-bound for E _Q_ [ _f_ ] _−_ E _P_ [ _f_ ], from which the result for _|_ E _P_ [ _f_ ] _−_ E _Q_ [ _f_ ] _|_ follows. 

## B PROOF OF THEOREM 1 

The proof adapts elements of the proofs from Barber et al. (2023) and Angelopoulos et al. (2023a). variable whereLet _Z[K]_ be obtained P _{K_ =from _i}_ = _Zw_ ˜by _i_ (note thatswapping _Z[n]_ ( _X_[+1] _K_ = _, Y ZK_ ).) Letand ( _Xn_ +1 _, Yn_ +1), where _K_ is a random 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0014-06.png)


be the weighted empirical risk in the calibration set plus the additional test example. Let us define 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0014-08.png)


Given the random variable _Z_ , we can think of _λ[∗]_ ( _Z_ ) as another random variable which is a transformation of _Z_ . Moreover, we define the random variable _Fi_ ( _Z_ ) = _L_ ( _λ[∗]_ ( _Z_ ); ( _Xi, Yi_ )) for _i ∈_ [ _n_ +1], as well as the vector of random variables _F_ ( _Z_ ) = [ _F_ 1( _Z_ ) _, . . . , Fn_ +1( _Z_ )]. From Lemma 1, we have 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0014-10.png)


a bound that we will use later. Writing _Li_ ( _λ_ ) _≡ L_ ( _λ_ ; ( _Xi, Yi_ )) for convenience, we also have, for any _λ_ and for any _k ∈_ [ _n_ + 1], 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0014-12.png)


14 

Published as a conference paper at ICLR 2024 

Figure 4: Average loss (top) and _λ_[ˆ] (bottom) over 10 independent trials for settings (1), (2), and (3). In this case, _λ_ represents the number of predicted labels. We smooth the curves by taking a rolling average with a window of 30 time points. 

Therefore, setting _λ_ = _λ_[ˆ] and using Eq. (10), we obtain _R_[ˆ] _n_ +1( _λ_[ˆ] ; _Z[k]_ ) _≤ NNww_ +1 _[R]_[ˆ] _[n]_[(ˆ] _[λ]_[;] _[ Z]_[)+] _NwB_ +1 _[≤] α_ , which, from Eq. (22), implies _λ[∗]_ ( _Z[k]_ ) _≤ λ_[ˆ] ( _Z_ ). Since the loss _L_ is nonincreasing with _λ_ , we get 

E[ _Ln_ +1( _λ_[ˆ] ( _Z_ ); _Z_ )] _≤_ E[ _Ln_ +1( _λ[∗]_ ( _Z[K]_ ); _Z_ )] = E[ _LK_ ( _λ[∗]_ ( _Z[K]_ ); _Z[K]_ ] 


![](markdown_output/non-exchangeable-conformal-2023_images/non-exchangeable-conformal-2023.pdf-0015-04.png)


The result follows by noting that _d_ TV( _F_ ( _Z_ ) _, F_ ( _Z[i]_ )) _≤ d_ TV( _Z, Z[i]_ ). Eq. (25) is actually a tighter bound, similarly to what has been noted by Barber et al., 2023. 

## C MULTILABEL CLASSIFICATION IN A TIME SERIES 

Fig. 4 shows results averaged across 10 independent trials for _α_ = 0 _._ 2 and setting _λ_ in a slightly different way than that of §4.1. In this case, _λ_ represents the number of active labels and we use _Cλ_ ( _Xi_ ) = top- _λ_ ( _**f**_ ( _Xi_ )). The main takeaways remain the same: both methods perform similarly when the data is exchangeable, in setting (1). Accounting for the non-exchangeability introduced by changepoints and distribution drift using our method enables lowering the risk to the desired level in settings (2) and (3). 

15 

