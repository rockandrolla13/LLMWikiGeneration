Conformal Prediction Advanced Topics in Statistical Learning, Spring 2023 Ryan Tibshirani 

## **1 Introduction** 

Conformal prediction is a relatively new framework for quantifying uncertainty in the predictions made by arbitrary prediction algorithms. Fundamentally, it does so by converting an algorithm’s predictions into prediction sets, which have strong finite-sample coverage properties. 

The idea behind conformal prediction was born out of conversations between Vladimir Vovk and his colleagues, including Alexander Gammerman and Vladimir Vapnik (who was visiting the university), in the mid 1990s at Royal Holloway, University of College London. The definitive reference is Vovk et al. (2005). This remained a topic of intense interest for Vovk and collaborators for many years, up through current day. It is Larry Wasserman who brought about the interest in the statistics community, and inspired Carnegie Mellon University colleagues including Jing Lei (and the author of these lecture notes), to collaborate on conformal prediction in the mid 2010s. This lecture will draw mostly from the language for conformal prediction developed in Lei et al. (2018); Tibshirani et al. (2019). 

The community working on conformal prediction remained fairly small for most of its short history, until fairly recently—just the last few years, really—when it exploded in popularity in the machine learning community. As such, there will be a lot of interesting work about conformal prediction that we will not be covering. A nice recent overview is Angelopoulos and Bates (2023). The last section of that monograph provides some sense of the current trends in the field. 

## **1.1 A lofty goal?** 

The basic goal of conformal prediction is as follows. Let ( _Xi, Yi_ ) _∼ P_ , _i_ = 1 _, . . . , n_ be i.i.d. feature and response pairs, from a distribution _P_ on _X × Y_ . For concreteness, we can think of the feature space as say, _X_ = R _[d]_ , and the response space as _Y_ = R, though this need not be the case in general. Let _α ∈_ (0 _,_ 1) be and a nominal error level. Then we want to find a _prediction band_ , 

**==> picture [112 x 13] intentionally omitted <==**

with the property that for a new i.i.d. pair ( _Xn_ +1 _, Yn_ +1) _∼ P_ , 

**==> picture [302 x 14] intentionally omitted <==**

where the probability is over all of our data ( _Xi, Yi_ ), _i_ = 1 _, . . . , n_ + 1. 

On the one hand, without placing any assumptions on _P_ , and without appealing to asymptotics of any kind, this might seem like a really hard goal in general. On the other hand, we can do something trivial to obtain it: for example, 

**==> picture [181 x 31] intentionally omitted <==**

will always have exactly 1 _− α_ coverage, that is, it will achieve (1) with an equality. 

So the real question is this (albeit still somewhat vaguely-phrased): can we achieve (1), in finite samples, without any assumptions on _P_ , by doing something “nontrivial”? In particular, we would like our strategy to adapt to the hardness of the problem, in the following sense: the more easily we can predict _Yn_ +1 from _Xn_ +1, the smaller we would like our set _C_[ˆ] _n_ ( _Xn_ +1) to be. 

1 

## **1.2 This is achieveable!** 

Perhaps remarkably, this last goal is actually achieveable, in a very general way. As we will see in the coming sections, we can start with any algorithm that produces a “point predictor” _f_[ˆ] _n_ that predicts _Yn_ +1 from _Xn_ +1, and turn this into a “set predictor” _C_[ˆ] _n_ that satisfies (1). 

The basic idea behind conformal prediction is two-fold. The first key idea can actually be explained in a simpler context, _where there are no features at all_ , and we just have a sequence _Yi ∈_ R, _i_ = 1 _, . . . , n_ of real-valued response values. Suppose our goal is to find a one-sided prediction interval _C_[ˆ] _n_ = ( _−∞,_ ˆ _qn_ ] with 

**==> picture [285 x 12] intentionally omitted <==**

Given this goal (2), a natural place to start would be to set _q_ ˆ _n_ to be the level (1 _− α_ ) sample quantile of _Y_ 1 _, . . . , Yn_ , which we denote by 

**==> picture [148 x 29] intentionally omitted <==**

with _δa_ denoting a point mass at _a_ , and hence _n_[1] � _ni_ =1 _[δ][Y][i]_[denoting][the][empirical][distribution][of] _[Y]_[1] _[, . . . , Y][n]_[.] But this would only give use the approximate result 

**==> picture [98 x 11] intentionally omitted <==**

This becomes exact as _n →∞_ , under standard conditions (that ensure convergence of the sample quantile to the population quantile). So can we instead get something that satisfies (2) in finite-sample? 

**First key idea: use ranks to form adjusted quantiles.** This is where the first key idea behind conformal prediction comes in (which in a sense traces back to work on rank-based statistics and permutations by Fisher and Pitman in the 1930s). As _Yn_ +1 is i.i.d. with _Y_ 1 _, . . . , Yn_ , then 

**==> picture [389 x 11] intentionally omitted <==**

This means that 

**==> picture [395 x 19] intentionally omitted <==**

which is in turn equivalent to[1] 

**==> picture [390 x 19] intentionally omitted <==**

The last step is critical: note that we have moved from a comparison between _Yn_ +1 and a an order statistic of _Y_ 1 _, . . . , Yn_ +1 in (4) to a comparison between _Yn_ +1 and an order statistic of _Y_ 1 _, . . . , Yn_ in (5). This is key, because what is on the right-hand side of the _≤_ sign in (5) is _computable from just the first n points_ . Accordingly, by defining 

**==> picture [332 x 11] intentionally omitted <==**

we have precisely achieved (2). 

The formulation in (6) is arguably the most intuitive way to remember how to achieve coverage. There are other equivalent formulations. One such equivalent formulation (we will see more later on) is 

**==> picture [334 x 29] intentionally omitted <==**

> 1To see this, consider the complement of the events (inside the probabilities) in (4), (5). Abbreviate _k_ = _⌈_ (1 _− α_ )( _n_ + 1) _⌉_ . Then _Yn_ +1 _>_ the _k_ smallest of _Y_ 1 _, . . . , Yn_ +1 is clearly an equivalent statement to _Yn_ +1 _>_ the _k_ smallest of _Y_ 1 _, . . . , Yn_ , since _Yn_ +1 can never be strictly larger than itself. That said, this argument really only makes sense for _k ≤ n_ , and for _k_ = _n_ + 1, which occurs if _α <_ 1 _/_ ( _n_ + 1), then _⌈_ (1 _− α_ )( _n_ + 1) _⌉_ = _n_ + 1, then we have to interpret the ( _n_ + 1) smallest of _Y_ 1 _, . . . , Yn_ as being + _∞_ to equate (4), (5). This is the consistent with interpreting the quantile function in (7) to return + _∞_ when the input level is _≥_ 1. 

2 

In this way, we can also see the solution here as simply to taking the sample quantile at an adjusted level: we use _⌈_ (1 _− α_ )( _n_ + 1) _⌉/n_ , instead of 1 _− α_ , which is a sort of finite-sample correction. But in our opinion, the fact that (7) achieves the coverage guarantee is less obvious; only through its equivalence to (6)—and then the equivalence to the precedings displays in (5), (4), (3)—does this become transparent. A very simple illustration of the key idea here is given in Figure 1. 

**==> picture [328 x 110] intentionally omitted <==**

**----- Start of picture text -----**<br>
Y       is equally likely to occupy  n +1<br>≥1 − α fraction<br>any of the values<br>… …<br>Y (1) Y (2) Y (3) Y (4) Y ⌈(1− α )( n +1)⌉ Y ( n +1)<br>**----- End of picture text -----**<br>


Figure 1: _Illustration of the first key idea in conformal prediction, as stated in_ (3) _,_ (4) _. Note also that we have the sharpened version_ (8) _when there are almost surely no ties._ 

~~**Love**~~ **Exchangeability is all you need.** Looking back at (3), all that we need for this to hold is that _Y_ 1 _, . . . , Yn_ +1 are _exchangeable_ , which is a weaker than the i.i.d. assumption. Recall that exchangeability of _Y_ 1 _, . . . , Yn_ +1 means that their joint distribution is unchanged under permutations: 

**==> picture [272 x 15] intentionally omitted <==**

**Coverage upper bound when there are no ties.** If there are almost surely no ties between _Y_ 1 _, . . . , Yn_ +1 (or we use a suitably random tie-breaking rule) then the statement in (4) can be sharpened to an equality, 

**==> picture [420 x 23] intentionally omitted <==**

Simply upper bounding the right-hand side above gives 

**==> picture [418 x 22] intentionally omitted <==**

Carrying on from by the same logic as before leads to the sharpened conclusion, 

**==> picture [324 x 22] intentionally omitted <==**

with _q_ ˆ _n_ still defined as in (6). To be clear, the lower bound on coverage in (10) always holds, and the upper bound holds under the assumption that there are almost surely no ties. 

**Naive attempt to lift this idea to regression problems.** Now let’s try to lift the first key idea to a regression setting, where we observe both _Xi ∈X_ and _Yi ∈_ R, _i_ = 1 _, . . . , n_ , and want a prediction set for _Yn_ +1 based on _Xn_ +1. Suppose that _f_[ˆ] _n_ is any point predictor, trained on ( _Xi, Yi_ ), _i_ = 1 _, . . . , n_ , such that (to put it informally) 

ˆ _fn_ ( _x_ ) predicts the value of _y_ that we expect to see at _x_ . 

Then we could proceed naively as follows. We define (absolute) residuals made on the training set, 

**==> picture [148 x 13] intentionally omitted <==**

ˆ and just as in (6), let _qn_ = _⌈_ (1 _− α_ )( _n_ + 1) _⌉_ smallest of _R_ 1 _, . . . , Rn_ . We could then define the prediction set to be _C_[ˆ] _n_ ( _x_ ) = _{y_ : _|y − f_[ˆ] _n_ ( _x_ ) _| ≤ q_ ˆ _n}_ , or in other words 

**==> picture [150 x 14] intentionally omitted <==**

3 

in the hope that _Yn_ +1 _∈ C_[ˆ] _n_ ( _Xn_ +1) with probability at least 1 _− α_ . However, 

**==> picture [394 x 13] intentionally omitted <==**

and the latter event does _not_ hold with probability 1 _− α_ , because _Rn_ +1 = _|Yn_ +1 _− f_[ˆ] _n_ ( _Xn_ +1) _|_ is _not_ exchangeable with _R_ 1 _, . . . , Rn_ . 

The problem is that _f_[ˆ] _n_ has already "seen" ( _Xi, Yi_ ), _i_ = 1 _, . . . , n_ (since it was trained on them), but it has not yet seen ( _Xn_ +1 _, Yn_ +1). Accordingly, the test residual _Rn_ +1 will be generally stochastically larger than the training residuals _R_ 1 _, . . . , Rn_ , and so the naive prediction set defined above will generally undercover. 

## **2 Split conformal prediction** 

Enter the second key idea behind conformal prediction, and _split conformal prediction_ , which is the simplest and most computationally efficient way to carry out this idea. Split conformal prediction is the focus of this section, and we stick to regression where responses are real-valued, so _Y_ = R. The next section describes a (much more complicated) method that avoids splitting the data. At the end of this lecture, we will consider classification, where _Y_ is discrete. 

**Second key idea: construct scores symmetrically.** In a nutshell, the second key idea in conformal prediction is to build residuals in way that treats all of the data (that goes into determining their distribution), including the test data, in a _symmetric_ fashion. This will ensure that the residuals obey the exchangeability condition we require in order to get coverage. 

Concretely, in split conformal prediction (split CP) we do the following. We first divide the training set into two sets: 

- _D_ 1, called the _proper training set_ ; and 

- _D_ 2, called the _calibration set_ . 

We can think of these as sets of indices, so that _D_ 1 _, D_ 2 are such that _D_ 1 _∩ D_ 2 = _∅_ and _D_ 1 _∪ D_ 2 = _{_ 1 _, . . . , n}_ . Let _n_ 1 = _|D_ 1 _|_ and _n_ 2 = _|D_ 2 _|_ . The next step is to fit our point predictor on proper training points ( _Xi, Yi_ ), _i ∈ D_ 1, call it _f_[ˆ] _n_ 1. Then we define calibration set residuals 

**==> picture [130 x 13] intentionally omitted <==**

a conformal quantile 

**==> picture [204 x 11] intentionally omitted <==**

and a conformal set 

**==> picture [317 x 14] intentionally omitted <==**

The main guarantee we can get is that 

**==> picture [381 x 23] intentionally omitted <==**

where the lower bound on coverage always holds, and the upper bound holds under the assumption that the residuals are almost surely distinct. Why? If we condition on the proper training set ( _Xi, Yi_ ), _i ∈ D_ 1, then _the calibration residuals Ri, i ∈ D_ 2 _and the test residual Rn_ +1 = _|Yn_ +1 _− f_[ˆ] _n_ 1( _Xn_ +1) _| are all i.i.d._ , and therefore 

**==> picture [397 x 13] intentionally omitted <==**

occurs (by our previous arguments) with probability at least 1 _− α_ , and at most 1 _− α_ + 1 _/_ ( _n_ 2 + 1) if the residuals are almost surely distinct. 

4 

**Any score function will work.** Above, we used absolute residuals as a negatively-oriented score function (negatively-oriented meaning that lower values are better). But really, any negatively-oriented score function will do, and the argument goes through just as before. That is, suppose _V_ ( _x, y_ ) = _V_ (( _x, y_ ); _f_[ˆ] _n_ 1) assigns a conformity score to the point ( _x, y_ ) based on _f_[ˆ] _n_ 1 (for simplicity, we will generally drop the notational dependence on _f_[ˆ] _n_ 1). Define, generalizing the construction leading up to (11), calibration set scores 

**==> picture [112 x 11] intentionally omitted <==**

## and a conformal set 

**==> picture [288 x 19] intentionally omitted <==**

Then we get the exact same guarantee as in (12), since _Ri_ , _i ∈ D_ 2 and _Rn_ +1 = _V_ ( _Xn_ +1 _, Yn_ +1) are all still i.i.d., conditional on _f_[ˆ] _n_ 1). This will be important later, as we’ll see how to move beyond the residual score to obtain better local adaptivity in our prediction bands. 

Positively-oriented scores will work too, we can just negate them (to make the negatively-oriented) before passing them through this construction. This would result in a conformal set of the form 

**==> picture [264 x 19] intentionally omitted <==**

An example of a naturally occurring positively-oriented scores will arise in the classification setting. 

**Quantile and CDF formulations.** Keeping the conformity score generic (and negatively-oriented) for now, we note that there are multiple equivalent formulations for the split conformal prediction set: 

**==> picture [384 x 83] intentionally omitted <==**

The original formulation in (13) is (we think) the most intuitive. 

The second formulation in (14) is of the form “test score _≤_ adjusted quantile”. This form will be useful for generalizing conformal prediction to use weights, which we will cover in the next lecture, when we consider certain settings where the scores are no longer exchangeable. 

The third formulation (15) is expressed in terms the empirical cumulative distribution function (CDF) of _Ri_ , _i ∈ D_ 2, precisely, its left-continuous version. It is of the form “CDF evaluated at test score _≤_ adjusted level”. This is a useful form when considering auxiliary randomization schemes, covered next. 

**Auxiliary randomization to get exact coverage.*** It is worth noting that we can always use auxiliary randomization to get exact coverage in our prediction sets, that is, to achieve 1 _− α_ coverage in (12). You can skip this without interrupting the flow of understanding the ideas in the rest of this lecture, hence the asterisk. First, rewrite the conformal set in its CDF form (15) as 

**==> picture [424 x 28] intentionally omitted <==**

This now compares the left-continuous empirical CDF of the _n_ 2 + 1 points _Ri_ , _i ∈ D_ 2 and _V_ ( _x, y_ ), evaluated at the test score _V_ ( _x, y_ ), to an adjusted level. To explain the auxiliary randomization mechanism, it helps to look at what happens at the (unknown) test point ( _Xn_ +1 _, Yn_ +1): let _Rn_ +1 = _V_ ( _Xn_ +1 _, Yn_ +1) denote its score, and let _F_[ˆ] _n[−]_ 2+1[denote][the][left-continuous][CDF][of] _[R][i]_[,] _[i][ ∈][D]_[2][and] _[R][n]_[+1][.][Then] 

**==> picture [258 x 23] intentionally omitted <==**

5 

which we know occurs with probability at least 1 _− α_ . 

In general, for any random variable _Z_ whose CDF is _F_ ( _x_ ) = P( _Z ≤ z_ ) and whose left-continuous CDF is _F[−]_ ( _z_ ) = P( _Z < z_ ) = lim _y→z− F_ ( _y_ ), we can construct a randomized version by defining, for _U ∼_ Unif(0 _,_ 1), 

**==> picture [166 x 13] intentionally omitted <==**

This has the property that P( _F[∗]_ ( _Z_ ) _≤ t_ ) = _t_ , for any _t_ . 

Returning to our conformal setting, we see that if we define a randomized conformal prediction set based on auxiliary randomization of the empirical CDF, such that 

**==> picture [204 x 14] intentionally omitted <==**

then we will get coverage with probability exactly 1 _− α_ . Spelling it out in more detail, this is the same as defining the randomized conformal set 

**==> picture [396 x 28] intentionally omitted <==**

where _U ∼_ Unif(0 _,_ 1) is independent of everything else. To record its guarantee, this set always satisfies 

**==> picture [210 x 19] intentionally omitted <==**

## **2.1 Remarks** 

Here we make some brief remarks about split conformal prediction. First, recall that the naive prediction band—as covered at the end of Section 1.2—is generally going to undercover, drastically so when _f_[ˆ] _n_ overfits the training data. In a sense, we can think of the split conformal band (11) as being _protected against overfitting_ , since it based on comparing a test score to calibration set scores, and in the overfitting regime, these will all be equally large (in distribution). 

Second, note that the split conformal band (11) constructed using absolute residual scores has width that is _exactly constant in x_ . This is not generally a good thing: it means that the band does not adapt to the local hardness of the problem (how hard it is to predict at any given _x_ ), as we will clearly see in an example to follow. However, this can be addressed by changing the conformity score, as we will do in Section 4. 

Third and last, we note the following key fact: _the better the point predictor f_[ˆ] _n_ 1 (from the proper training set), _the tighter the prediction band will be_ . Both experiments and theory corroborate this claim; see, e.g., Lei et al. (2018), and Figure 2, which is taken from that paper. (Do not confuse this point with the last point about local width at a particular _x_ ; here we are talking about the of the prediction band width in an _average_ sense over _x_ .) Therefore, any prediction algorithm leads to valid coverage, but better algorithms (for the prediction problem at hand) lead to smaller prediction sets. 

An interesting way to interpret this last observation is as follows. Let us condition on the proper training set implicitly so we do not have to express it notationally. Then, average length is: 

**==> picture [182 x 27] intentionally omitted <==**

where _µ_ is Lebesgue measure and _PX_ is the distribution of _X_ , the feature vector. Meanwhile, coverage is: 

**==> picture [200 x 26] intentionally omitted <==**

where _PY |X_ is the distribution of _Y |X_ . Therefore, an inefficient prediction algorithm must somehow put mas in _low density regions_ of _PY |X_ , which does not hurt its coverage, but inflates its length. 

6 

**==> picture [449 x 491] intentionally omitted <==**

**----- Start of picture text -----**<br>
Coverage, Setting A Coverage, Setting A Coverage, Setting C<br>GGGG [G] GGGG GG G GGGG GGGGG G [G] G G G G GGGG GGGG GGGGG G GGG G G G G GGGGG GGGGGGGG G [G] GGGGGGGGG [G] G G G [G] G [G] GG [G] GGGG GG [G] G [GG] GGGG G G GGGGG GGGG G GGGGG GGGG [G] GGGG GG G GGGG GGGGG G [G] G G G G GGGG GGGG GGGGG G GGG G G G G GGGGG GGGGGGGG G [G] GGGGGGGGG [G] G G G [G] G [G] GG [G] GGGG GG [G] G [GG] GGGG G G GGGGG GGGG G GGGGG G G GGGG G GG [G] GGG G GGG GGG G GGG GG G [G] G [G] GGG GGGG G GGGG G GGG G G G G [G] GGGG GGGGG G G GG GG GG GG [G] G [G] G GGGGG [GG] GGGG [G] G GGGG G [GGGG] GGGG [G] G [G] [G] G [G] [GGGGGG]<br>Lasso Lasso Lasso<br>Elastic net Elastic net Elastic net<br>Stepwise Stepwise Stepwise<br>Spam Spam Spam<br>Random forest Random forest Random forest<br>0 0.1 0.1 0.2 0.2 0.3 0.3 0.4 0.4 0.5 0 0.1 0.1 0.2 0.2 0.3 0.3 0.4 0.4 0.5 −1.6 −1.2 −1 −0.8 −0.3 0.1 0.3<br>Relative optimism Relative optimism Relative optimism<br>Test Error, Setting A Test Error, Setting B Test Error, Setting C<br>GG [G] GGGG [GG] G [GGG] GG [GG] G G [G] G [G] G [GG][G] G GGG GG [G] GGGG [GGGGGG] G [G] [GGG] G G [G] [G][G] G [GG] G [G] G [GGG] G [GGG] G [GGGGGGGGG] [G] G [G] [G]<br>GG GGG G GGGGGGG GGGG G G G G G G GGGGG [G] GG [GG]<br>GGGG G GG [G] G G [GG] G [GG] GG GGGGG G G G G G G GG [G] G GGGG GGGGG G GGG G G GG [G] GGG GG [G] G G [G] G [GG] [G] G [G][G] [G][G][GGGGGGGG] [G][G] [G][G] [G] [G] [G][G] [G][G] [GGGG][G] [G] [GGGG][GGGG] G GGG GGGGGG GG G GG GGG GG G GG G [G] GG G G G [G] G GG [G] G GG GG [G] G GGG [G] G G GGGG G [G][G] G [G] [GGGG] G [G] [GGG][G] [G][G] [G] [G] [GGG] [GGGGG][G] [GGG] [G] [G] [G] [G] [G] [G] [G] [GG] [G] [G] [G] G G GGGG G GGGGGG G GG [G] GGG G G [G] G [G] G GG [G][G] G GGG [G] [G] GG [G][G] [GG] G [G] [G] [G] [G] G [G] [G] [G] [GGGG] GGGG [G] G G G [G] [GG] G [G] [G] G [G] [G] [G] G [GG] [G][GGGGGGG] [GGG] G [GGGG] G<br>0 0.1 0.1 0.2 0.2 0.3 0.3 0.4 0.4 0.5 0 0 0.1 0.1 0.2 0.3 0.3 0.4 0.4 0.5 −1.6 −1.2 −1 −0.8 −0.3 0.1 0.3<br>Relative optimism Relative optimism Relative optimism<br>Length, Setting A Length, Setting B Length, Setting C<br>GGGG GGGG [G] G GGGGG [G] GG GG G G G G G G GGGGGGG GGGG GGGGG G GGG GGGG [G] G GGGGG GGG [G] G GGGGGGGGG [GG] G [G] G [GG] GG [G] G [G] GGGGGGG [GGGG] G G [G] GGGGG [G] G GG GGG [G] GG G [G] G [G] G G G [G] GG G [GG] [GG][GGGG][GGGG] [GGGG][GGGGG] G GGGGGGGGGGGG G GGGG GGGGGG GG G GG GGG GG G GG G GGG G G GGG GG [G] G GG GG [G] G GGGGG GGGGGGGGGG GGG [G] G [G] [GGGG][G] GGGG [GGG] GG [GGGGG] GG [GG] [G] G [G][GG][G] [G] [G] G [GG] [G][GGGG] [G] GG [GGG][G] GGGG G G [G] GG [G] G [G][G] [G] [G] [G] [G] [G] [GG] [G] [G] GGG GGGG [G] GG [G] GGG G GGG GG [G] G GGG G [G] GGGG [GG][G] G GGG [G] [G] G [GG][G] [G] G [G] G [G] [G] [GGG] G [G] [GGG] GGGG [G] GGGG [G] GG [G] GG [G][G] [G] [G][G] [GGG] G [G][GGGGGGGGG] [GGG] G [GGGG] GGGGG [GG] GGG [GG] G [GGGG] GG G [G] [GGGG] [GGG] G [G] [G]<br>0 0.1 0.1 0.2 0.2 0.3 0.3 0.4 0.4 0.5 0 0 0.1 0.1 0.2 0.3 0.3 0.4 0.4 0.5 −1.6 −1.2 −1 −0.8 −0.3 0.1 0.3<br>Relative optimism Relative optimism Relative optimism<br>1.0 1.0 1.0<br>0.8 0.8 0.8<br>0.6 0.6 0.6<br>Coverage Coverage Coverage<br>0.4 0.4 0.4<br>0.2 0.2 0.2<br>0.0 0.0 0.0<br>45<br>3.0 40 250<br>35<br>200<br>2.5 30<br>Test error Test error Test error<br>150<br>25<br>2.0<br>20 100<br>15<br>6.0 22 50<br>45<br>20<br>5.5 40<br>18<br>35<br>Length 5.0 Length 16 Length 30<br>25<br>14<br>4.5 20<br>12<br>15<br>**----- End of picture text -----**<br>


Figure 2: _Experiments demonstrating the coverage (top row), test error (middle row), and average length (bottom row) of split conformal prediction in three different simulation settings, and with several different prediction algorithms. The x-axis in each plot sweeps over internal hyperparameters of the algorithms (they are simply put on a common scale using a notion called relative optimism). Settings A, B, and C are increasingly challenging, in terms of the tractability of prediction. Takeaways: any algorithm, using any hyperparameter value, leads to essentially exactly 90% coverage in all settings (this was the nominal level), as seen in the top row; moreover, test error of the algorithm-hyperparameter pair and average length (or width, these are used synonymously) of the prediction set correlate quite strongly. Credit: Lei et al. (2018)._ 

7 

**==> picture [206 x 206] intentionally omitted <==**

**----- Start of picture text -----**<br>
0 1 2 3 4 5 6<br>X<br>1.0<br>0.5<br>0.0<br>Y −0.5<br>−1.0<br>−1.5<br>−2.0<br>**----- End of picture text -----**<br>


Figure 3: _Example of split conformal prediction, based on a smoothing spline with 5 degrees of freedom._ 

## **2.2 Example** 

Now we give an example of split conformal in action, in Figure 3. In this simple univariate example (realvalued features), we split the data randomly and equally into a proper training set (points drawn in black) and a calibration set (drawn in blue). We use a smoothing spline with 5 degrees of freedom to fit _f_[ˆ] _n_ 1 on the proper training set. The split conformal prediction band, which is simply computed from an adjusted level 90% quantile of the calibration residuals, and is drawn in orange. 

This is guaranteed to have at least 90% test coverage, when we draw test points from the same distribution as that used to generate the training data. We can see that the band is constant-width, by design. This is a function of using the absolute residual as our conformity score. It is not desirable in the current example because it will tend to overcover on the left side of the domain, and undercover on the right side (note that the variance of _Y |X_ is not constant in this example). We will revisit (and remedy) this later in Section 4. 

## **2.3 Conditional coverage properties?** 

We have seen that split conformal prediction comes with the strong, distribution-free coverage guarantee in (12). Of course, simply by marginalizing over the proper training set, it also has the unconditional coverage property, 

**==> picture [218 x 23] intentionally omitted <==**

Going the other direction, we could ask if it has coverage properties after we condition on _more_ than just the proper training set. If we condition on both the proper training set and the calibration set, that is, we condition on the _entire training set_ , then when the conformity scores are almost surely distinct (or we use a suitably random tie-breaking rule): 

**==> picture [386 x 19] intentionally omitted <==**

where _kα_ = _⌈_ (1 _− α_ )( _n_ 2 + 1) _⌉_ . The result in (16) is a consequence of standard facts about order statistics and you’ll prove it on the homework. How do we interpret it? Note, the only thing random in this probability the test point ( _Xn_ +1 _, Yn_ +1) (everything else has been conditioned on). Therefore, we can think about it as follows: _as we draw random calibration sets_ , each one being of size _n_ 2 (containing i.i.d. draws 

8 

from a fixed distribution _P_ ), the coverage integrated over a single test point is distributed as Beta( _kα, n_ 2 + 1 _− kα_ ). This distribution has mean 

**==> picture [123 x 24] intentionally omitted <==**

exactly as expected. It has variance 

**==> picture [133 x 24] intentionally omitted <==**

Thus when _n_ 2 is small, this distribution has considerable variability, and for any given calibration set in hand, we might see the test coverage looking far from 1 _− α_ . To give you a more precise sense, Figure 4 plots the density of this beta distribution for _α_ = 0 _._ 1 and a few values of _n_ 2. 

**==> picture [342 x 249] intentionally omitted <==**

**----- Start of picture text -----**<br>
n = 100<br>n = 1000<br>n = 5000<br>0.80 0.85 0.90 0.95 1.00<br>Coverage<br>80<br>60<br>Density<br>40<br>20<br>0<br>**----- End of picture text -----**<br>


Figure 4: _Density of the beta distribution in_ (16) _that describes the calibration set conditional coverage of split conformal prediction, for alpha_ = 0 _._ 1 _and a few values of n_ 2 _._ 

How about instead conditioning on _Xn_ +1? This kind of coverage, which we will call _X-conditional coverage_ , would be highly desirable: it would say that 

**==> picture [310 x 19] intentionally omitted <==**

which means that we would cover the response at test feature value _x_ . Alas, this is asking for too much, and in a sense that we will make precise later, in Section 3.3, this is effectively impossible to do without making assumptions about the distribution _P_ governing the data. 

## **3 Full conformal prediction** 

Is there some way to get guaranteed coverage without splitting the data? Enter _full conformal prediction_ (often just called conformal prediction). This method is generally much more expensive and much more complicated than its split counterpart, but it is nonetheless a beautiful and important idea—and in some cases, it can indeed be computed efficiently. 

9 

In full conformal prediction, we still abide by the second key idea described previously, in which we construct residuals in a way that treats all data symmetrically. We just do it in a more subtle way. Fix any _x ∈X_ , and suppose that we want to figure out whether any given response value _y ∈_ R should be in our prediction set _C_[ˆ] _n_ ( _x_ ). We call _y_ in the _trial_ or _query_ value. Now we do something unlike anything we have seen thus far: we train our prediction algorithm on ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _,_ ( _x, y_ )—note this is an _augmented_ training set, with _n_ + 1 points—to produce a point predictor _f_[ˆ] _n,_ ( _x,y_ ). We define residuals 

**==> picture [183 x 33] intentionally omitted <==**

Then we a conformal set 

**==> picture [388 x 19] intentionally omitted <==**

The guarantee we get is that 

**==> picture [342 x 22] intentionally omitted <==**

where the lower bound on coverage always holds, and the upper bound holds under the assumption that the residuals are almost surely distinct once we plug in for the random test point ( _x, y_ ) = ( _Xn_ +1 _, Yn_ +1). Why? After we plug in for the random test point, and abbreviate 

**==> picture [164 x 14] intentionally omitted <==**

we can see that _these residuals are all exchangeable_ . (To be precise, this is only true if the algorithm that we use to fit the point predictor _f_[ˆ] _n,_ ( _x,y_ ) is a symmetric function of the training data that it takes as input, i.e., does not use knowledge of the order in which the training points were passed.) Therefore 

**==> picture [336 x 13] intentionally omitted <==**

occurs (by our previous arguments) with probability at least 1 _− α_ , and at most 1 _− α_ + 1 _/_ ( _n_ + 1) if the residuals are almost surely distinct. 

All of the extensions mentioned in the split conformal section, after defining the basic method based on residual scores, carry over to full conformal. We summarize these below. 

- Any negatively-oriented and suitably symmetric score function can be used in place of the absolute residual score and the guarantee is unchanged. That is, define 

**==> picture [283 x 41] intentionally omitted <==**

for any function _V_ that is symmetric in its last _n_ + 1 arguments. This function can, for example, train a point predictor on the last _n_ + 1 arguments—as long as it treats them symmetrically—and then use it to return some score for the first argument. Then the conformal prediction set in (17) still has the same guarantee in (18), by the same exchangeability arguments. 

- We can rewrite the conformal set (17) in equivalent quantile and CDF forms: 

**==> picture [369 x 62] intentionally omitted <==**

- We can always inject auxiliary randomness in order to obtain coverage exactly 1 _− α_ in (18). 

10 

## **3.1 Remarks** 

The remarks discussed for split conformal previously also carry over more or less to full conformal prediction. To summarize briefly: the full conformal band is protected against overfitting, because now computation of _f_[ˆ] _n,_ ( _x,y_ ) involves the query point ( _x, y_ ); the band produced by full conformal under the residual score is often roughly (though not exactly) constant-width, which is not generally a good property, but can be addressed by changing the score function (more later); and lastly, in general, the better the prediction algorithm, the tighter the band will be overall. 

Next we give two further remarks. The first one is on computation: full conformal is in general _extremely computationally expensive_ : for every _x_ at which we want to compute the prediction set _C_[ˆ] _n_ ( _x_ ) in (17), we need to refit the point predictor _f_[ˆ] _n,_ ( _x,y_ ) (kernel regression, random forest, neural net, etc.) at in principle every _y ∈_ R in order to compute and compare the residuals _Ri_[(] _[x,y]_[)] , _i_ = 1 _, . . . , n_ + 1. This would actually be infinitely expensive, but in practice of course we would do it over a finite grid of _y_ values, which could still be tremendously expensive. Relatively speaking, split conformal is computationally trivial: it is typically dominated by the cost of fitting the point predictor _f_[ˆ] _n_ 1 once. Due to its extreme computational cost, full conformal prediction is rarely used in practice, except for small problem sizes, or with special prediction algorithms that have something like a “shortcut” formula for refitting the point predictor. Also, it is worth mentioning that in between split and full conformal prediction are methods that look like cross-validation, and cycle through using different parts of the data for training and. See Barber et al. (2021) for details. 

The second remark is about interpreting the conformal set via p-values. Observe that we can rewrite (20) once more as 

**==> picture [242 x 44] intentionally omitted <==**

Informally, we can interpret the fraction of residuals larger than the test residual, which we denote by _p_ ( _y_ ), as a p-value for the null hypothesis _H_ 0 : _Yn_ +1 = _y_ . Thus we can think of conformal prediction as using _y_ as a pivotal value, and _keeping all of values y for which we do not reject_ the null hypothesis, which it does by comparing _p_ ( _y_ ) to an adjusted significance level of _⌊α_ ( _n_ + 1) _⌋/n_ . 

## **3.2 Example** 

Figure 5 gives an example of full conformal in action. The underlying data is the same as in Figure 3, but for the prediction algorithm we now use a smoothing spline with 15 degrees of freedom (this allows the influence of the query point ( _x, y_ ) on the spline fit to be more visible). We demonstrate how to calculate the prediction set at a single value _x_ = 4 _._ 75, marked in blue. Figure 5 is actually an animation, but it might not render as one in many PDF viewers; if you can, try using Adobe Acrobat Reader to see the animation. We run the query response value _y_ over a grid, and for each _y_ , compute the smoothing spline fit using _n_ + 1 points, the original data set and ( _x, y_ ). Look carefully and you’ll see the gray smoothing spline curve get pulled upwards as _y_ moves upwards. For each value of _y_ , we record the fraction _p_ ( _y_ ) of residuals larger than the test residual, and in the end, the 90% prediction set keeps _y_ for which _p_ ( _y_ ) _≥⌊α_ ( _n_ + 1) _⌋/n ≈_ 0 _._ 1, visualized by thresholding the p-value histogram drawn along the right axis. 

## **3.3 Impossibility of X-conditional coverage** 

Returning to the issue of X-conditional coverage raised previously, here we drop some disappointing news: conformal prediction methods do not achieve this in general. The story is actually more grim: no method does, in a meaningful way, in the distribution-free setting. If _C_[ˆ] _n_ is any prediction band such that 

**==> picture [330 x 19] intentionally omitted <==**

then Lei and Wasserman (2014) show that 

**==> picture [376 x 30] intentionally omitted <==**

11 

**==> picture [288 x 206] intentionally omitted <==**

**----- Start of picture text -----**<br>
0 1 2 3 4 5 6 0.0 0.2 0.4 0.6 0.8 1.0<br>X<br>1.0<br>0.5<br>0.0<br>Y −0.5<br>−1.0<br>−1.5<br>−2.0<br>**----- End of picture text -----**<br>


Figure 5: _Example of full conformal prediction, where the prediction algorithm is a smoothing spline with 15 degrees of freedom. (This figure is actually an animation, but it might not render as one in most PDF viewers; if you can, try using Adobe Acrobat Reader to see the animation.)_ 

As before, _µ_ denotes Lebesgue measure and _PX_ is the feature distribution associated with _P_ . A non-atom point _x_ 0 of _PX_ is one for which _PX_ ( _Bδ_ ( _x_ 0)) _→_ 0 as _δ →_ 0, where _Bδ_ ( _x_ 0) is the _ℓ_ 2 ball of radius _δ_ centered at _x_ 0. Thus, in effect, the above says that any prediction band which claims to cover at almost every _x_ , for every joint distribution _P_ , must be infinite in size at any point _x_ 0 at which we do not have a positive probability of seeing duplicate observations. You’ll explore more of the details on your homework. 

## **4 Improving local adaptivity** 

Even though X-conditional coverage is effectively impossible in the distribution-free setting, in the sense made precise previously, this _does not_ mean that different methods cannot have widely different behaviors in practice, when it comes to their ability to deliver approximate X-conditional coverage. We will broaden our terminology and perspective and use _local adaptivity_ of a prediction band as a term that refers to its ability to shrink the band at values of _x_ at which prediction is easy, and inflate it at values of _x_ at which prediction is hard. This is admittedly somewhat vague, but because X-conditional coverage isn’t really our precise goal, local adaptivity is a better notion to keep in mind. 

There are different methods for obtaining better local adaptivity. The ones covered in this lecture all have to do with simply changing the conformity score. Below we cover two options in regression. 

## **4.1 Studentized residuals** 

A simple variant on the residual score is what we call a _studentized residual_ . We describe the idea for split conformal prediction (the full conformal extension is similar). On _D_ 1, we fit both a point predictor _f_[ˆ] _n_ 1 ˆ and a “spread predictor” _σn_ 1, which is designed to predict (say) the standard deviation of _|Y − f_[ˆ] _n_ 1( _X_ ) _|_ at _X_ = _x_ . Then on _D_ 2, we compute “studentized” or normalized residuals 

**==> picture [134 x 26] intentionally omitted <==**

**==> picture [381 x 11] intentionally omitted <==**

**==> picture [346 x 18] intentionally omitted <==**

12 

ˆ whose width we can see adapts according to _σn_ 1. The guarantee is just as before, in (12). Figure 6 gives an example. 

**==> picture [444 x 219] intentionally omitted <==**

**----- Start of picture text -----**<br>
G G GGG G G G GGGG G GG GG [G] G G G GG G GG GGGG G GGGGG GGGGG GGGGG G G G GG [G] GGGGGGGGGGGG G GG G GGGGGGG G GGG G G G G G GGGGG G GGGGGGG G GGGGGGG G GGG G GGGGG G GGGGG G GGGGGGGGGG G G GG GGGGGGGGGGGGGGGGGGGGGGGGG G G G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G G G GGGGG G GGGGGGG G GGGGGGGGGGGGGGGGGGG G GGGGGGG G GGGGGGGGGGGGG G GGGGGGG G GGGGGGGGGG G GGGGGGGGG G GGGGGGGGGGGGG G GGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGG G GGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGG G GGGGGGGGG G GGGGGGGG G G G GGGGGGGGGGGG G GGGGGGGGGGGGG G GGGGGGGGGGGGGGGG G GG G GGGGGGGGGGGGGGGGGGGGGGGGG GG GGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGG [G] GGGGG G GGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG [G] GGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G G GGG G G G GGGG G GG GG [G] G G G GG G GG GGGG G GGGGG GGGGG GGGGG G G G GG [G] GGGGGGGGGGGG G GG G GGGGGGG G GGG G G G G G GGGGG G GGGGGGG G GGGGGGG G GGG G GGGGG G GGGGG G GGGGGGGGGG G G GG GGGGGGGGGGGGGGGGGGGGGGGGG G G G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G G G GGGGG G GGGGGGG G GGGGGGGGGGGGGGGGGGG G GGGGGGG G GGGGGGGGGGGGG G GGGGGGG G GGGGGGGGGG G GGGGGGGGG G GGGGGGGGGGGGG G GGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGG G GGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGG G GGGGGGGGG G GGGGGGGG G G G GGGGGGGGGGGG G GGGGGGGGGGGGG G GGGGGGGGGGGGGGGG G GG G GGGGGGGGGGGGGGGGGGGGGGGGG GG GGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGG [G] GGGGG G GGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG [G] GGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG<br>G G G G<br>G G<br>0 1 2 3 4 5 6 0 1 2 3 4 5 6<br>X X<br>2 2<br>1 1<br>0 0<br>Y Y<br>−1 −1<br>−2 −2<br>**----- End of picture text -----**<br>


Figure 6: _Examples of split conformal prediction with the usual residual score (left panel) and the studentized residual score (right panel). The data comes from the same generative model as in Figures 3 and 5. We can see that the studentized residual adapts to the local hardness of prediction (and delivers something closer to conditional coverage). Credit: Lei et al. (2018)._ 

## **4.2 Quantile regression** 

There are two issues that can make studentized residuals fall short in practice. 

1. If _f_[ˆ] _n_ 1 is complex, then little information is left on the proper training set in order to fit _σ_ ˆ _n_ 1 (because the proper training residuals will be close to zero). This can be addressed with further data splitting, but that comes at a cost of statistical efficiency. 

2. More broadly, it does not need to be true that the variance of _Y |X_ = _x_ and the level 1 _− α_ quantile of this distribution are always tied together; in some problem settings they can even have opposing behaviors. Note that the former is being targeted by studentized residuals, but the latter is what should really be targeting in prediction bands. 

Romano et al. (2019) show that both of these can be addressed by changing our perspective on the point predictor itself: why not have it predict the level 1 _− α_ quantile of the response at _X_ = _x_ directly? (As opposed to predicting the mean of the response at _X_ = _x_ , which is what generic regression methods do.) 

Their proposal, called _conformalized quantile regression_ (CQR), works as follows, in the split setting (the full version is similar). We first fit two point predictors, denoted _f_[ˆ] _n[α/]_ 1[2] and _f_[ˆ] _n_[1] 1 _[−][α/]_[2] , on the proper training data ( _Xi, Yi_ ), _i ∈ D_ 1. Here each _f_[ˆ] _n[τ]_ 1[(] _[x]_[)][is][estimates][the][level] _[τ]_[quantile][of] _[Y][ |][X]_[=] _[ x]_[.][This][can][be][obtained] from a variety of quantile regression methods, which often only require a change of the loss function from a generic regression method. Then we form calibration set scores 

**==> picture [240 x 14] intentionally omitted <==**

**==> picture [356 x 11] intentionally omitted <==**

**==> picture [328 x 14] intentionally omitted <==**

13 

which enjoys the same guarantee as in (12). 

In the example from Figure 6, the data set is large enough and the point predictor stable enough that CQR (not shown) provides little gain over studentized residuals. However, in other examples, it can provide a clear gain. See Romano et al. (2019). Still, studentized residuals (or variants thereof) remain in fairly common use because we can use “out-of-the-box” regression methods to fit each of _f_[ˆ] _n_ 1 _,_ ˆ _σn_ 1 in sequence. 

## **5 Conformal** 

In this last section, we briefly cover conformal prediction for classification problems. The story is much the same, but we need different conformity score functions, since residual or quantile regression scores are not generally appropriate in classification. Below we cover a standard choice, based on predicted probabilities. Then we cover a choice that is designed to have better local adaptivity, based on cumulative probabilities. Throughout, we take _Y_ = _{_ 1 _, . . . , K}_ . 

## **5.1 Likelihood scores** 

We describe the idea for split conformal formulation (full conformal being similar). We first fit a probabilistic classifier _f_[ˆ] _n_ 1 to the proper training data ( _Xi, Yi_ ), _i ∈ D_ 1. That is, to be clear, 

**==> picture [262 x 14] intentionally omitted <==**

We then form calibration set scores, 

**==> picture [112 x 13] intentionally omitted <==**

In words, each _Ri_ is the probability or likelihood assigned to the correct class (on the unseen observation ( _Xi, Yi_ ) from the calibration set). Thus note that this is a positively-oriented score. We let 

**==> picture [180 x 11] intentionally omitted <==**

and the conformal set 

**==> picture [134 x 19] intentionally omitted <==**

This has precisely the same guarantee as in (12). 

## **5.2 Cumulative likelihood** 

To make the conformal prediction sets more adaptive (still in the context of having fit a probabilistic classifier _f_[ˆ] _n_ 1 on _D_ 1), Romano et al. (2020) propose a conformity score based on cumulative likelihood, defined as _f_ ˆ _n_ 1follows.( _Xi_ ; _k_ ), _k_ For= 1each _, . . . , Ki ∈_ in _D_ 2decreasing, let _πi_ be order,the permutationso that of 1 _, . . . , K_ that sorts the predicted probabilities 

**==> picture [238 x 13] intentionally omitted <==**

The the conformity scores are 

**==> picture [266 x 32] intentionally omitted <==**

In words, each _Ri_ is the cumulative probability of all classes considered “at least as likely” as the true one, by our probabilistic classifier. Note that this is negatively-oriented (if the true class is assigned a very low probability, then the cumulative probability of all classes “at least as likely” as it will be very high). Hence we let 

**==> picture [204 x 11] intentionally omitted <==**

14 

and the conformal set 

**==> picture [340 x 31] intentionally omitted <==**

This has precisely the same guarantee as in (12). 

Angelopoulos et al. (2021) refer to this method as _adaptive prediction sets_ (APS) and define a regularized version called RAPS that often delivers much smaller sets in practice. Figure 7 gives a few examples of RAPS from their paper. 

Figure 7: _Examples of RAPS, which is conformal prediction with a regularized version of the cumulative likelihood score. The true label in each case is “fox squirrel”, and we can see that the prediction sets adapt appropriately in size to the hardness of the classification task. Credit: Angelopoulos et al. (2021)._ 

## **References** 

- Anastasios N. Angelopoulos and Stephen Bates. A gentle introduction to conformal prediction and distribution-free uncertainty quantification. _Foundations and Trends in Machine Learning_ , 16(4):494–591, 2023. 

- Anastasios N. Angelopoulos, Stephen Bates, Jitendra Malik, and Michael I. Jordan. Uncertainty sets for image classifiers using conformal prediction. In _Proceedings of the International Conference on Learning Representations_ , 2021. 

- Rina Foygel Barber, Emmanuel J. Candès, Aaditya Ramdas, and Ryan J. Tibshirani. Predictive inference with the jackknife+. _Annals of Statistics_ , 49(1):486–507, 2021. 

- Jing Lei and Larry Wasserman. Distribution-free prediction bands for non-parametric regression. _Journal of the Royal Statistical Society: Series B_ , 76(1):71–96, 2014. 

- Jing Lei, Max G’Sell, Alessandro Rinaldo, Ryan J. Tibshirani, and Larry Wasserman. Distribution-free predictive inference for regression. _Journal of the American Statistical Association_ , 113(523):1094–1111, 2018. 

- Yaniv Romano, Evan Patterson, and Emmanuel J. Candès. Conformalized quantile regression. In _Advances in Neural Information Processing Systems_ , 2019. 

- Yaniv Romano, Matteo Sesia, and Emmanuel J. Candès. Classification with valid and adaptive coverage. In _Advances in Neural Information Processing Systems_ , 2020. 

- Ryan J. Tibshirani, Rina Foygel Barber, Emmanuel J. Candès, and Aaditya Ramdas. Conformal prediction under covariate shift. In _Advances in Neural Information Processing Systems_ , 2019. 

- Vladimir Vovk, Alex Gammerman, and Glenn Shafer. _Algorithmic Learning in a Random World_ . Springer, 2005. 

15 

