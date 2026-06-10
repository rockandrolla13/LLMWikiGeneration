_**risks**_ 

_Article_ 

## **Three Essays on Stopping** 

## **Eberhard Mayerhofer** 

Department of Mathematics and Statistics, University of Limerick, Limerick V94TP9X, Ireland; eberhard.mayerhofer@ul.ie 

Received: 27 September 2019; Accepted: 16 October 2019; Published: 18 October 2019 

**Abstract:** First, we give a closed-form formula for first passage time of a reflected Brownian motion with drift. This corrects a formula by Perry et al. (2004). Second, we show that the maximum before a fixed drawdown is exponentially distributed for any drawdown, if and only if the diffusion characteristic _µ_ / _σ_[2] is constant. This complements the sufficient condition formulated by Lehoczky (1977). Third, we give an alternative proof for the fact that the maximum before a fixed drawdown is exponentially distributed for any spectrally negative Lévy process, a result due to Mijatovi´c and Pistorius (2012). Our proof is similar, but simpler than Lehoczky (1977) or Landriault et al. (2017). 

**Keywords:** reflected Brownian motion; linear diffusions; spectrally negative Lévy processes; drawdown 

**MSC (2010):** 60J65; 60J75 

## **1. Introduction** 

This paper comprises three essays on stopping. 

In Section 2, we compute the Laplace transform of the first hitting time of a fixed upper barrier for a reflected Brownian motion with drift. This expands on and corrects a result by Perry et al. (2004). 

In Section 3, we show, by using an intrinsic delay differential equation, that for a diffusion process, the maximum before a fixed drawdown threshold is generically exponentially distributed, only if the diffusion characteristic _µ_ / _σ_[2] is constant. This complements the sufficient condition formulated by Lehoczky (1977). By solving discrete delay differential equations, we further construct diffusions, where the exponential law only holds for specific drawdown sizes. 

Section 4 uses Lehoczky (1977)’s argument to show that the maximum before a fixed drawdown threshold is exponentially distributed for any spectrally negative Lévy process, the parameter being the right-sided logarithmic derivative of the scale function. This yields an alternative proof to the original one in Mijatovi´c and Pistorius (2012) and is also similar to the one in Landriault et al. (2017). 

## **2. The First Hitting Time for a Reflected Brownian Motion With Drift** 

Let _X_ be a reflected Brownian motion on [0, ∞), with drift _µ_ and volatility _σ_ . Then _X_ can be written as 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0001-16.png)


where _W_ = ( _Wt_ ) _t≥_ 0 is a standard Brownian motion, and _L_ = ( _Lt_ ) _t≥_ 0 is an inon-decreasing process, such that the induced random measure _dL_ is supported on _{X_ = 0 _}_ . Itô’s formula implies that for any _f ∈ Cb_[2][([][0,][ ∞][))][ satisfying] _[f][ ′]_[(][0][+) =][ 0, the process] 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0001-18.png)


_Risks_ **2019** , _7_ , 105; doi:10.3390/risks7040105 

www.mdpi.com/journal/risks 

_Risks_ **2019** , _7_ , 105 

2 of 10 

is a martingale, where _Ay_ is the differential operator, defined by _Ay f_ ( _y_ ) = _[σ]_ 2[2] _[f][ ′′]_[(] _[y]_[) +] _[ µ][ f][ ′]_[(] _[y]_[)][.][1] For _δ ≥−x_ , we define the first hitting time: 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0002-03.png)


Since, before reaching the boundary 0, the process cannot be distinguished from a Brownian motion with drift, we may confine ourselves to computing _τδ_ for barriers _δ_ + _x_ , where _δ >_ 0. Our aim is to compute the Laplace transform: 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0002-05.png)


**Theorem 1.** _For δ ≥_ 0 _, the Laplace transform of the first hitting time of a reflected Brownian motion with drift µ and volatility σ is given by_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0002-07.png)


**Proof.** Pick Φ _∈ Cc_[∞][(][R][)][, such that][ Φ][(] _[ξ]_[) =][ 1 for] _[ |][ξ][| ≤][x]_[ +] _[ δ]_[.][Furthermore, let] _[ κ][∈]_[R][; then for any] _[ θ][≥]_[0] and _t ≥_ 0, the function 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0002-09.png)


satisfies _f_ := _F_ ( _t_ , _·_ ) _∈ Cb_[2][and] _[f][ ′]_[(][0][)][=][0.][According][to][the][introductory][notes][of][this][section,] the process _F_ ( _t_ , _Xt_ ) _−_[�] 0 _[t][∂][s][F]_[(] _[s]_[,] _[ X][s]_[)] _[ds][ −]_[�] 0 _[t][A][y][F]_[(] _[s]_[,] _[ X][s]_[)] _[ds]_[ is a uniformly bounded martingale; therefore,] the stopped process 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0002-11.png)


is also a true martingale, which starts at zero, P _[x]_ - almost surely. Using the fact that Φ( _Xt∧τδ_ ) = 1, we find that the stopped process satisfies for any _t ≥_ 0, 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0002-13.png)


Letting _t →_ ∞, we thus get by optional sampling, 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0002-15.png)


> 1 In the language of linear diffusions Borodin and Salminen (2012), _X_ has infinitesimal generator _Ay_ acting on the domain _D_ ( _Ay_ ) = _{ f ∈ Cb_[2][([][0,][ ∞][))] _[ |][f][ ′]_[(][0][+) =][ 0] _[}]_[.] 

_Risks_ **2019** , _7_ , 105 

3 of 10 

For the two choices _κ ∈{κ−_ , _κ_ + _}_ , where 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0003-03.png)


we thus obtain two equations, for two unknown moments, 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0003-05.png)


Solving this linear system for the involved moments yields the Laplace transform of _τδ_ , Equation (1). 

**Remark 1.** _This result can also be obtained from a more general result for spectrally negative Lévy processes, reflected at an upper barrier (Avram et al. 2017, Proposition 4.B and Section 10.1). In fact, the distribution of τ[δ] is equal in distribution to the first hitting time_ 0 _of the Brownian motion Xt_ = _δ_ + _σBt − µt, starting at δ ≥_ 0 _, reflected at x_ + _δ >_ 0 _. Its Laplace transform is therefore given by_ 

_where_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0003-09.png)


_(see Avram et al. (2017), Section 10.1)._ 

_Remarks On Perry et al. (2004)_ 

For another “sanity check” of Theorem 4, we compute the Laplace transform Equation (1) independently when _µ_ = 0 and _x_ = 0. In this case, the reflected Brownian motion is equal to _|σB|_ in law, where _B_ is a standard Brownian motion. But then _τδ_ is equal in distribution to 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0003-13.png)


Now, it is well known that the Laplace transform of � _τδ_ is given by 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0003-15.png)


which indeed coincides with Equation (1) for _µ →_ 0 and _x_ = 0. 

Perry et al. (2004), Formula (5.2), state a different Laplace transforms than our Theorem 4. Letting _µ →_ 0 in Perry et al. (2004), Formula (5.2) indeed yields for _σ_[2] = 1 and _x_ = 0, 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0003-18.png)


which contradicts Equation (2). The proof of Perry et al. (2004), Lemma 5.1, cannot be rectified, however, by merely fixing the (obviously) missing factor of 1/2 for _α_[2] in the second line of their proof. Indeed, in the same line, they forget a factor _e[−][κ][W]_[(] _[s]_[)] in the second integrand; thus, by inserting special values of _κ_ into the process in line 2, one does not get rid of the local-time term, as claimed. 

_Risks_ **2019** , _7_ , 105 

4 of 10 

## **3. Diffusions with Exponentially Distributed Gains Before Fixed Drawdowns** 

Let _X_ be a diffusion process on the interval [ _−a_ , ∞), satisfying the SDE 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0004-04.png)


where _µ_ ( _x_ ) and _σ_ ( _x_ ) are locally Lipschitz continuous functions of linear growth on [ _−a_ , ∞), and _σ_ ( _x_ ) _>_ 0 thereon. 

For a threshold 0 _< δ ≤ a_ , we define _M[δ]_ as the maximum of _X_ , prior to a drawdown of size _δ_ , that is 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0004-07.png)


We use the abbreviation Φ( _x_ ) := _e[−]_[2][ �] 0 _[x][γ]_[(] _[u]_[)] _[du]_ , where _γ_ ( _x_ ) = _µ_ ( _x_ )/ _σ_[2] ( _x_ ). The following is due to Lehoczky (1977): 

## **Proposition 1.** 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0004-10.png)


Caution is needed when interpreting the original paper Lehoczky (1977): Lehoczky uses the letter “a” for three different objects: The drift _µ_ ( _x_ ) is denoted as _a_ ( _x_ ), while _−a_ is the left endpoint of the interval of the support of _X_ ; third, the threshold _δ_ in his paper is also called _a_ . An inspection of Lehozky’s proof reveals that our more general version with _δ ≤ a_ holds. 

In terms of diffusion characteristics, Lehoczky’s result holds in a more general context. First, the assumption of locally Lipschitz coefficients are too strong, and can be relaxed. For example, we can relax to Hölder regularity of _σ_ ( _x_ ) of order no worse than 1/2, due to Yamada et al. (1971). In addition, we can allow reflecting or absorbing boundary conditions, thus include reflected diffusions. For instance, Proposition 1 holds for a Brownian motion with drift, starting at 0 and being reflected at _−a_ , because the process _X_ cannot hit _−a_ before it reaches a strictly positive maximum, due to strict positive volatility _σ_ (0) _>_ 0. 

From Equation (4), it can be seen that when _µ_ / _σ_[2] is constant, _M[δ]_ is exponentially distributed (the special case for for a Brownian motion with drift is due to Taylor (1975), and independently discovered by Golub et al. (2016)). Mijatovi´c and Pistorius (2012) extended this result to spectrally negative Lévy processes: For those, _M[δ]_ is also exponentially distributed, with the parameter being the right-sided logarithmic derivative of the scale function, evaluated at the drawdown threshold. 

This section characterizes the exponential law for diffusions: 

## **Theorem 2.** _The following are equivalent:_ 

_1. µ_ ( _x_ )/ _σ_[2] ( _x_ ) _is a constant on_ [ _−a_ , ∞) _._ 

_2. For each δ >_ 0 _, M[δ] is exponentially distributed._ 

**Proof of the Theorem.** Sufficiency of the first condition for the second one follows directly from Proposition 1. Suppose, therefore, that for each 0 _< δ ≤ a_ , there exists Λ( _δ_ ) _>_ 0 such that _M[δ]_ is exponentially distributed with parameter Λ( _δ_ ). Then, due to Equation (4), 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0004-19.png)


_Risks_ **2019** , _7_ , 105 

5 of 10 

By this particular functional form, and, since _µ_ / _σ_[2] is continuous, it follows that the functions Λ( _δ_ ) and Φ( _x_ ) are continuously differentiable. By differentiating Equation (5) with respect to _ξ_ , we have 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0005-03.png)


and differentiating with respect to _δ_ yields, in conjunction with the previous identity, 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0005-05.png)


Therefore, also 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0005-07.png)


and dividing the last two equations yields Lobacevsky’s functional equation[2] 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0005-09.png)


Note, Φ is continuously differentiable, and strictly positive. Hence, by taking derivatives with respect to _δ_ , we get 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0005-11.png)


and by setting _ξ_ = _δ_ , we thus have 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0005-13.png)


where _α_ = Φ _[′]_ (0)/Φ(0) _∈_ R. We conclude that for some _β ∈_ R, 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0005-15.png)


By Equation (7), we can extend the exponential solution to _−a ≤ ξ <_ 0: By setting _ξ_ = 0, we indeed have 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0005-17.png)


Similarly, we can successively extend the validity of Equation (8) to the right, using the functional Equation (7). Now that Φ( _ξ_ ) = _e[βξ]_ for all _ξ ∈_ [ _−a_ , ∞) we have, by taking the logarithmic derivative of Φ, that _µ_ ( _x_ )/ _σ_[2] ( _x_ ) is indeed a constant on [ _−a_ , ∞). 

Examples of processes for which the running maximum at drawdown is exponentially distributed are the following: 

1. ( _a_ = _−_ ∞): Brownian motion with drift _σBt_ + _µt_ . 

2. ( _a <_ ∞): Reflected Brownian motion with drift, reflected at _−a_ . 

3. Similar examples as in 1 and 2 can be constructed, where _µ_ ( _x_ )/ _σ_[2] ( _x_ ) is constant. These include 

However, there are processes that do not satisfy Theorem 2, even though they may exhibit exponentially distributed gains before _δ_ drawdowns for specific choices of _δ_ . One can, for instance, let _µ_ / _σ_[2] be constant only on [ _−_ 1, ∞), and modify _µ_ , _σ_[2] on [ _−_ 2, _−_ 1) in such a way, that the SDE Equation (3) has unique global strong solution. Then, by Proposition 1, for any _δ <_ 1 the maximum at 

> 2 See (Aczél (1966) p. 82, Chapter 2 Equation (16)) and the references therein. 

_Risks_ **2019** , _7_ , 105 

6 of 10 

drawdown of size _δ_ is exponentially distributed. It goes without saying, that there must exist _δ >_ 1, for which this is not the case. 

Similar, but more sophisticated, examples can be constructed by solving delay differential equations for Φ( _·_ ) = _e[−]_[2][ �] 0 _[·][µ]_[(] _[u]_[)][/] _[σ]_[2][(] _[u]_[)] _[du]_ , such that only for a specific threshold _δ_ , _M[δ]_ is exponentially distributed. Equation (6) reads in differential form: 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0006-04.png)


which is the simplest non-trivial (discrete) delay differential equation. To construct a diffusion process for which the maximum before a drawdown of size 1 is exponentially distributed with parameter one, we set Λ( _δ_ ) = _δ_ = 1, and we choose a strictly positive continuous function _g_ ( _x_ ) on [ _−_ 1, 0] satisfying _g_ (0) = 1. To obtain Φ on [0, ∞), we solve 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0006-06.png)


subject to Φ( _ξ_ ) = _g_ ( _ξ_ ) for _ξ ∈_ [ _−_ 1, 0]. This problem has a unique solution with exponential growth. However, if _g_ is not an exponentially linear function (that is, of the form _e[λ][x]_ for some _λ >_ 0), then Φ is not, and therefore _µ_ / _σ_[2] is not constant. An underlying diffusion process _X_ with _M_[1] being exponentially distributed with parameter one can for instance be constructed, by solving SDE Equation (3), where _σ_ = 1 and _µ_ = _−_ 2[Φ] Φ _[′]_[(] ( _[x] x_[)] )[on][[] _[−]_[1,][ ∞][)][.][Due][to][Theorem][2][,] _[M][δ]_[is,][in][general,] not exponentially distributed. 

## **4. Lehoczky’s Proof for Spectrally Negative Lévy Martingales** 

We study in this section the distribution of maximal gains[3] of processes, prior to the occurrence of a fixed loss _δ >_ 0. Golub et al. (2016, 2018) claim that for a Brownian motion (the toy model of a fair game), this gain is exponentially distributed, with parameter _δ_ ; thus, on average, one gains _δ_ before experiencing a loss of size _δ_ . This result is independent of the volatility of the Brownian motion. In private communication, Golub (2014) raised the question of whether similar scaling laws hold for other processes, e.g., other diffusion models, or processes with jumps. Such models are useful as benchmark models in the context of certain event-based high-frequency trading algorithms, where the Brownian motion is used as a proxy for an asset, and the location of the maximum suggests the beginning of a trend reversal.[4] 

The conjecture that a fair game on average experiences the exact same gain as is lost later on may appear intuitive. And this is indeed the case for many continuous-time martingales, those who are time-changed Brownian motions, with a quadratic variation tending to infinity, along almost every path (because the timing is not relevant here). But it is not true for Lévy martingales, as can be seen from Theorem 4. Nevertheless, the (exponential) distribution of gains, not its parameter, is universal within the class of spectrally negative Lévy processes. Besides, the martingale property is not needed to arrive at this result. 

After Theorem 4 was proved in the summer of 2019, F. Hubalek kindly pointed out that the result is, in identical form, preceded by Mijatovi´c and Pistorius (2012). Our proof is, however, similar to the one of Lehoczky (1977), and is therefore an alternative, and simpler one. Finally, we also found a replication of Lehoczky’s proof in Landriault et al. (2017), Lemma 3.1, however, this proof is also more difficult than ours due the more general discretization used therein. 

> 3 This random gain is called “overshoot” in Golub et al. (2016). In this section, we refrain from using this terminology due to its established meaning in the field of Lévy processes—it is the discrepancy between a certain threshold, and a jump processes’ value, passing beyond that threshold. 

> 4 It goes without saying that the first time this maximum is attained is not a stopping time; otherwise, one could devise arbitrage strategies that short-sell the asset at the maximum. 

_Risks_ **2019** , _7_ , 105 

7 of 10 

We assume, that a Lévy process _X_ is given with downward jumps only but not equal to the negative of a Lévy subordinator and not being a deterministic drift[5] . Such a process is defined by its Lévy exponent 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0007-03.png)


which is of the form 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0007-05.png)


with Lévy-Khintchine triplet _µ ∈_ R, _σ ∈_ R and a measure _ν_ ( _dξ_ ) supported on ( _−_ ∞, 0), integrating min( _ξ_[2] , 1). 

The scale function _W_ is the unique absolutely continuous function [0, ∞) _→_ [0, ∞) with Laplace transform 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0007-08.png)


Since the processes lack positive jumps, they can only creep up. This assumption is essential to obtain exit probabilities from compact intervals and also for the main Theorem 4. 

**Theorem 3.** _(Bertoin 1996, Theorem VII.8) Let x_ , _y >_ 0 _, the probability that X makes its first exit from_ [ _−x_ , _y_ ] _at y is_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0007-11.png)


For a threshold _δ >_ 0, we define _M[δ]_ as the supremum of _X_ , prior to a drawdown of size _δ_ , that is 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0007-13.png)


We are ready to state and proof the main theorem: 

**Theorem 4.** _For a spectrally negative Lévy process, the maximal gain M[δ] before a δ-loss is exponentially distributed with parameter equal to the logarithmic derivative of the scale function, that is,_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0007-16.png)


**Proof of Theorem 4.** The proof is inspired by Golub et al. (2016), however, the exact same idea can be traced back to Lehoczky (1977) in the general context of univariate diffusions processes. Let _Ak_ , _n_ be the event that _X_ reaches _kξ_ /2 _[n]_ before _−δ_ + ( _k −_ 1)/2 _[n] ξ_ ( _k_ = 1, . . . , 2 _[n]_ ). The set _{M[δ] ≥ ξ}_ can be approximated by[�] _[n] k_ =1 _[A][k]_[,] _[n]_[, which are decreasing for increasing] _[ n]_[.][In other words,] 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0007-18.png)


Therefore, 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0007-20.png)


> 5 This is the natural non-degeneracy condition of Bertoin (1996), Chapter VII to ensure that the process creeps up to any level. 

_Risks_ **2019** , _7_ , 105 

8 of 10 

Due to state-independence of the process (translation invariance) and the Markov property 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0008-03.png)


where the last identity follows from Theorem 3. Since _W_ is differentiable from the right at _δ_ , applying L’Hospital’s rule yields 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0008-05.png)


**Remark 2.** _Theorem 4 implicitly requires right-differentiability of the scale functions, which is for free, because it can be rewritten as an integral of the tail of some finite measure, see (Bertoin (1996), Chapter VII). However, in many models, full C_[1] _-regularity is guaranteed (cf. the characterization given by (Kuznetsov et al. (2012), Lemma 2.4))._ 

_Examples_ 

The scale functions for the below processes are taken from review article of Hubalek and Kyprianou (2011). Throughout this section, _E_ ( _λ_ ) denotes the exponential distribution with parameter _λ >_ 0. 

**Example 1** (Compound Poisson Process) **.** _Assume we have a compound Poisson process with negative exponentially distributed jumps,_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0008-10.png)


_We get_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0008-12.png)


_Clearly, W ∈ C_[1] (0, ∞) _,_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0008-14.png)


_Therefore, by Theorem 4_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0008-16.png)


Unlike the previous example, the following two examples exhibit the same qualitative dependence on the threshold _δ_ , as the standard Brownian motion, where _M[δ] ∼E_ (1/ _δ_ ): when _δ →_ 0, the average maximum at drawdown of size _δ_ tends to 0, and when _δ →_ ∞, this average goes to infinity. 

**Example 2** (Brownian motion with drift) **.** _A Brownian motion with drift µ >_ 0 _and volatility σ,_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0008-19.png)


_has scale function_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0008-21.png)


_Risks_ **2019** , _7_ , 105 

9 of 10 

_Hence,_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0009-03.png)


_Therefore, by Theorem 4 (see, e.g., Golub et al. (2016)),_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0009-05.png)


**Example 3** (Caballero and Chaumont (2006)) **.** _This is a Lévy process without diffusion component, defined by its Lévy measure_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0009-07.png)


_where β ∈_ (1, 2) _, and its Laplace exponent,_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0009-09.png)


_The process exhibits Infinite variation jumps, and drifts to −_ ∞ _, because_ Ψ _[′]_ (0) _<_ 0 _. The scale function is_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0009-11.png)


_Using Theorem 4, we thus get_ 


![](markdown_output/Three_Essays_on_Stopping_images/Three_Essays_on_Stopping.pdf-0009-13.png)


The asymptotic behaviour of the logarithmic derivative of the scale function of a spectrally negative Lévy process can be characterized using the asymptotic behaviour of _W_ and _W[′]_ , cf. (Kuznetsov et al. 2012, Chapter 3). For instance, _W_ (0) = _W_ (0+) = 0, if and only if the process is of infinite variation. In the case of finite variation, we can write the process as _δt − Jt_ , where _J_ is a subordinator; and then _W_ (0) = 1/ _δ >_ 0. Furthermore, _W[′]_ (0+) = ∞, if a diffusion component is present, or if the Lévy measure is infinite. These general findings are consistent with the three examples. 

**Funding:** This research received no external funding. 

**Acknowledgments:** I thank John Appleby, Florin Avram, Huayuan Dong, Friedrich Hubalek, Andreas Kyprianou and two anonymous referees for useful comments. 

## **References** 

Aczél, János. 1966. _Lectures on Functional Equations and Their Applications_ . Waltham: Academic Press, vol. 19. Avram, Florin, Danijel Grahovac, and Ceren Vardar-Acar. 2017. The _W_ , _Z_ scale functions kit for first passage 

problems of spectrally negative Lévy processes, and applications to the optimization of dividends. _arXiv_ . arXiv:1706.06841. 

Bertoin, Jean. 1996. _Lévy Processes_ . Cambridge: Cambridge University Press, vol. 121. 

Borodin, Andrei. N., and Paavo Salminen. 2012. _Handbook of Brownian Motion-Facts and Formulae_ . Basel: Birkhäuser. Caballero, Maria Emilia, and Loïc Chaumont. 2006. Conditioned stable Lévy processes and the Lamperti representation. _Journal of Applied Probability_ 43: 967–83. [CrossRef] 

Golub, Anton. 2014. Flov Technologies, Zürich, Switzerland. Private communication. Golub, Anton, Gregor Chliamovitch, Alexandre Dupuis, and Bastien Chopard. 2016. Multi-scale representation of high frequency market liquidity. _Algorithmic Finance_ 5: 3–19. [CrossRef] 

Golub, Anton, James B. Glattfelder, and Richard B. Olsen. 2018. The alpha engine: Designing an automated trading algorithm. In _High-Performance Computing in Finance_ . London: Chapman and Hall/CRC, pp. 49–76. 

_Risks_ **2019** , _7_ , 105 

10 of 10 

Hubalek, Friedrich, and Andreas E. Kyprianou. 2011. Old and new examples of scale functions for spectrally negative Lévy processes. In _Seminar on Stochastic Analysis, Random Fields and Applications VI_ . Basel: Springer, pp. 119–45. 

Kuznetsov, Alexey., Andreas E. Kyprianou, and Victor Rivero. 2012. The theory of scale functions for spectrally negative Lévy processes. In _Lévy Matters II_ . New York: Springer, pp. 97–186. 

Landriault, David, Bin Li, and Hongzhong Zhang. 2017. On magnitude, asymptotics and duration of drawdowns for Lévy models. _Bernoulli_ 23: 432–58. [CrossRef] 

Lehoczky, John P. 1977. Formulas for stopped diffusion processes with stopping times based on the maximum. _The Annals of Probability_ 5: 601–7. [CrossRef] 

Mijatovi´c, Aleksandar, and Martijn R. Pistorius. 2012. On the drawdown of completely asymmetric Lévy processes. _Stochastic Processes and their Applications_ 122: 3812–36. [CrossRef] 

Perry, David, Wolfgang Stadje, and Shelemyahu Zacks. 2004. The first rendezvous time of Brownian motion and compound Poisson-type processes. _Journal of Applied Probability_ 41: 1059–70. [CrossRef] 

Taylor, Howard M. 1975. A stopped Brownian motion formula. _The Annals of Probability_ 3: 234–46. [CrossRef] 

Yamada, Toshio, and Shinzo Watanabe. 1971. On the uniqueness of solutions of stochastic differential equations. _Journal of Mathematics of Kyoto University_ 11: 155–67. [CrossRef] 

_⃝_ c 2019 by the author. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/). 

