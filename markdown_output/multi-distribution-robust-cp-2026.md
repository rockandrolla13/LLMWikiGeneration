# Multi-Distribution Robust Conformal Prediction Yuqi Yang and Ying Jin[∗] 

## **Abstract** 

In many fairness and distribution robustness problems, one has access to labeled data from multiple source distributions yet the test data may come from an arbitrary member or a mixture of them. We study the problem of constructing a conformal prediction set that is uniformly valid across multiple, heterogeneous distributions, in the sense that no matter which distribution the test point is from, the coverage of the prediction set is guaranteed to exceed a pre-specified level. We first propose a max-p aggregation scheme that delivers finite-sample, multi-distribution coverage given any conformity scores associated with each distribution. Upon studying several efficiency optimization programs subject to uniform coverage, we prove the optimality and tightness of our aggregation scheme, and propose a general algorithm to learn conformity scores that lead to efficient prediction sets after the aggregation under standard conditions. We discuss how our framework relates to group-wise distributionally robust optimization, sub-population shift, fairness, and multi-source learning. In synthetic and real-data experiments, our method delivers valid worst-case coverage across multiple distributions while greatly reducing the set size compared with naively applying max-p aggregation to single-source conformity scores, and can be comparable in size to single-source prediction sets with popular, standard conformity scores. 

## **1 Introduction** 

Reliable uncertainty quantification is critical for deploying machine learning systems in high-stakes domains [Platt et al., 1999, Gal et al., 2016, Guo et al., 2017, Lakshminarayanan et al., 2017, Kuleshov et al., 2018, Jiang et al., 2012, Kompa et al., 2021]. Conformal prediction is a powerful distribution-free framework for this purpose. Given any prediction model, it offers prediction sets whose coverage guarantees hold without strong parametric assumptions on the data generating process [Vovk et al., 2005, Lei et al., 2018]. 

This paper studies how to maintain such reliability when models are deployed across multiple heterogeneous environments [Crammer et al., 2008, Mansour et al., 2008, Hashimoto et al., 2018, Romano et al., 2019a]. For example, a clinical risk prediction model trained on data from several hospitals must remain reliable when a new patient’s record comes from one of these sites. Our goal in this work is to construct prediction sets with valid coverage even when it is impossible to reveal where that patient came from. 

Formally, we assume access to labeled data _D_ = _∪[K] k_ =1 _[D]_[(] _[k]_[)][from] _[K][∈]_[N][+][heterogeneous][sources,][where] each _D_[(] _[k]_[)] = _{_ ( _Xi_[(] _[k]_[)] _, Yi_[(] _[k]_[)] ) _}i∈Ik_ consists of i.i.d. samples from an unknown distribution _P_[(] _[k]_[)] . Here _Xi_[(] _[k]_[)] _∈X_ is the features, and _Yi_[(] _[k]_[)] _∈Y_ is the response. Write _n_ = _|D|_ . For a new test point ( _Xn_ +1 _, Yn_ +1) drawn from one of these sources, we aim to build a prediction set _C_[ˆ] ( _Xn_ +1) _⊆Y_ with _uniform coverage_ : 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0001-08.png)


where P _D×P_ ( _k_ ) denotes the joint distribution of the labeled data and a new test point ( _Xn_ +1 _, Yn_ +1) _∼ P_[(] _[k]_[)] . In words, _C_[ˆ] ( _·_ ) should achieve the nominal coverage level simultaneously for all possible sources. Several practically important scenarios motivate such a guarantee: 

> ∗ Department of Statistics and Data Science, University of Pennsylvania. Email: `yjinstat@wharton.upenn.edu` . Reproduction code for experimental results in the paper can be found in `https://github.com/AragornBFRer/MDCP` . 

1 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0002-00.png)


**----- Start of picture text -----**<br>
Joint training<br>h *( x ,  y )<br>Distribution 1<br>C ˆ2( X ) ˆ C ˆ2( X ) ˆ C ˆ2( X ) Distribution 2<br>C ˆ1( X ) C 1( X ) C 1( X )<br>C ˆ( X ) C ˆ( X ) C ˆ( X )<br>(a) Full domination (b) Partial overlap (c) MDCP idea<br>**----- End of picture text -----**<br>


Figure 1: Prediction sets with uniform coverage need to balance the coverage across multiple distributions. (a) When one distribution has heavier tails, a valid prediction set _C_[ˆ] ( _X_ ) may coincide with the larger one _C_[ˆ] 1( _X_ ). (b) When two distributions _partially overlap_ , a uniformly valid prediction set _C_[ˆ] ( _X_ ) sits in between two distributions and is longer than single-source sets _C_[ˆ] 1( _X_ ) and _C_[ˆ] 2( _X_ ). (c) MDCP achieves uniform coverage by jointly training a conformity score and aggregating multiple prediction sets from the trained score. 

- **Fairness without protected attributes.** Fair prediction across protected attributes such as race, gender, or socioeconomic status is a central goal of equitable machine learning [Madras et al., 2018, Hashimoto et al., 2018]. In this context, group-conditional coverage demands the coverage of the prediction sets to hold for all groups [Romano et al., 2019a, Jung et al., 2022, Gibbs et al., 2025]. However, existing methods rely on the test group information (i.e., which distribution the test point is from). In sensitive scenarios, the group labels may be unavailable or protected [Gupta et al., 2018, Martinez et al., 2021, Lahoti et al., 2020], necessitating a single prediction set with coverage over all groups. When _P_[(] _[k]_[)] denotes a sensitive group, uniform coverage (1) provides such a guarantee without group information. 

- **Subpopulation shift.** When each distribution represents a subpopulation, a prediction set with uniform coverage (1) protects against arbitrary subpopulation shift [Sagawa et al., 2019, Santurkar et al., 2020, Subbaswamy et al., 2021, Yang et al., 2023]. Formally, subpopulation shift assumes the labeled data come from _P_ train =[�] _[K] k_ =1 _[π][k][P]_[ (] _[k]_[)][,][with][non-negative][mixture][weights] _[{][π][k][}][K] k_ =1[that][sum][to][1,][and][each] _[P]_[ (] _[k]_[)] is a subpopulation (e.g., hospitals, demographic groups). The test distribution is _P_ test =[�] _[K] k_ =1 _[π] k[′][P]_[ (] _[k]_[)][,] with distinct weights _{πk[′][}][K] k_ =1[.][Any][prediction][set][obeying][(][1][)][guarantees][valid][coverage][under][any][such] shift, since E _P_ test( _Yn_ +1 _∈ C_[ˆ] ( _Xn_ +1)) =[�] _[K] k_ =1 _[π] k[′]_[P] _P_[ (] _[k]_[)][(] _[Y][n]_[+1] _[∈][C]_[ˆ][(] _[X][n]_[+1][))] _[ ≥]_[1] _[ −][α]_[once][�] _[K] k_ =1 _[π] k[′]_[= 1.] 

- **Multi-source data.** Many scientific and engineering applications naturally aggregate heterogeneous datasets collected under different protocols or environments [Crammer et al., 2008, Mansour et al., 2008], which has attracted interests in conformal prediction as well [Lu et al., 2023, Spjuth et al., 2019, Liu et al., 2024]. Examples include hospitals with varying patient demographics, or satellite sensors operating under distinct conditions. Standard conformal prediction (calibrated on pooled data from all sites) is valid only for the mixture distribution induced by the training sample. In contrast, (1) offers guarantees to all individual sources, ensuring reliability even when the test data align with only one of them. 

To achieve uniform coverage (1) with a single prediction set _C_[ˆ] ( _Xn_ +1), the key challenge is to balance the heterogeneous sources for reasonable efficiency (prediction set size). We demonstrate the efficiencyvalidity tension via two examples in Figure 1(a-b). In panel (a), the label in one source has a more dispersed distribution and therefore requires larger source-wise prediction sets; any single set that attains 1 _−α_ coverage for that source will typically be conservative for the more concentrated source. In panel (b), different sources place probability mass in different regions of the response, so a uniformly valid set may need to cover multiple regions and can be substantially larger than a single-source set. 

2 

## **1.1 Preview of results** 

In this paper, we propose Multi-Distribution Conformal Prediction (MDCP), a general framework for constructing efficient prediction sets that achieve the uniform coverage guarantee (1) given per-source datasets. Our starting point is a simple, distribution-free _max-p aggregation_ mechanism for achieving uniform validity. For each source, we compute a conformal p-value using any conformity score, and then aggregate these p-values by taking their maximum. Inverting the aggregated p-value yields a prediction set that is exactly the union of the single-source conformal sets, and therefore delivers _finite-sample_ uniform coverage. 

While always valid, this naive aggregation can be inefficient when sources are heterogeneous. In nested cases like Fig. 1(a), it is essentially unavoidable to over-cover one source for the validity in the other more dispersed distribution. In cases like Fig. 1(b), however, a strict subset of the naive union can still satisfy uniform coverage: the slack in coverage in some sources allows the final set to be trimmed while maintaining the worst-case coverage. Importantly, such improvements can still be obtained with max-p aggregation, but only if the per-source sets are re-designed by using appropriate per-source conformity scores (Fig. 1(c)). 

To formalize this principle, we analyze population-level optimization programs to theoretically characterize the optimal prediction sets with the minimal size/length subject to uniform coverage, which yield concrete guidance for score design. In specific, there exists one single conformity score function _h[∗]_ : _X ×Y →_ R, which depends on a dual problem involving all the source distributions, such that the max-p aggregation based on this score converges to the optimally efficient prediction set. Moreover, max-p aggregation is _tight_ : the optimal set achieves (nearly) exact 1 _− α_ coverage for at least one source distribution. 

Building on these insights, we develop an end-to-end MDCP procedure that learns the optimal score and combines it with max-p aggregation to produce a final prediction set. We prove that MDCP achieves finitesample uniform coverage (1), and it asymptotically matches the oracle optimal set under mild consistency conditions. We instantiate MDCP for both classification and regression using general learning algorithms and practical training strategies. Finally, in extensive simulations and real-data applications to satellite imagery and medical service datasets, MDCP achieves tight worst-case coverage while substantially improving efficiency over naive aggregation baselines, often approaching the size of single-source prediction sets. 

We summarize our contributions as follows: 

- We introduce a general max-p aggregation scheme that achieves uniform coverage based on singlesource conformal p-values. 

- We characterize the population-optimal prediction sets subject to uniform coverage, and show that the max-p aggregation is optimal and tight when paired with properly chosen conformity scores. 

- We propose an end-to-end pipeline to learn the conformity scores and construct efficient MDCP sets for both classification and regression. 

- We demonstrate the effectiveness of MDCP in extensive simulations and real data applications. 

## **1.2 Related work** 

**Multi-source/distribution conformal prediction.** Our setting is connected to several recent work on conformal prediction from multiple data sources, where the goals vary, including learning with limited communications across sources [Lu et al., 2023], using other sources to improve efficiency in one source [Liu et al., 2024], aggregating individual prediction sets without data sharing [Spjuth et al., 2019] for i.i.d. data [Humbert et al., 2023], and leveraging density ratio for coverage over one single test distribution [Plassier et al., 2024]. In contrast, our goal is to leverage all data sources during training to construct a uniformly valid prediction set for a new test point from any source, leading to distinct techniques and guarantees. 

**Distributionally-robust conformal prediction.** This work falls broadly into the strand in conformal prediction regarding distribution robustness, which studies the construction of prediction sets with valid 

3 

coverage when the test distribution differs from that of the labeled data. Earlier works assume the test distribution is unidentified but is under various types of perturbations around the labeled data distribution, and seeks to protect against the worst-case among these perturbations, such as a divergence ball [Cauchois et al., 2024] or conditional shift within a divergence ball [Jin et al., 2023, Yin et al., 2024, Ai and Ren, 2024], and adversarial attacks [Gendler et al., 2021, Ghosh et al., 2023]. This work can be viewed as distributionallyrobust conformal prediction when the test distribution is an unknown member of the source distributions or an arbitrary mixture of them, which necessitates entirely different techniques than these works. 

**Group-conditional conformal prediction.** Within conformal prediction, our setting is close to the group-conditional conformal prediction, sometimes framed for fairness [Romano et al., 2019a] and extended to multi-validity [Jung et al., 2022, Gibbs et al., 2025]. MDCP can be viewed as addressing a similar problem when a distribution represents a group-conditional distribution. In contrast, however, our method achieves so without observing the group label at test time, which can be particularly useful in sensitive scenarios with protected labels. As such, the techniques we develop are in sharp contrast to those methods. 

**Distribution robustness and multi-source/group learning.** This work is connected to a rich line of work on the robustness to distribution shift and heterogeneity across data sources. Classical domain adaptation and multi-source learning frameworks aim to generalize models across environments with distinct data-generating mechanisms [Crammer et al., 2008, Mansour et al., 2008, Ben-David et al., 2010]. In the modern ML setting, robust optimization and distributionally robust optimization (DRO) offer a complementary worst-case perspective [Ben-Tal et al., 2009, Rahimian and Mehrotra, 2019], and group-robust variants (e.g., group-DRO or relatedly, agnostic federated learning) seek worst-case performance over groups or mixtures of source distributions [Hashimoto et al., 2018, Sagawa et al., 2019, Mohri et al., 2019, Santurkar et al., 2020, Lahoti et al., 2020, Martinez et al., 2020, Subbaswamy et al., 2021, Yang et al., 2023]. Our approach parallels this perspective but operates in the space of coverage guarantees rather than loss minimization: MDCP ensures valid coverage holds for all source distributions, serving as a analogue of group-DRO in uncertainty quantification with exact finite-sample validity. 

## **2 Max-p conformal prediction** 

In this section, we introduce the general max-p aggregation scheme and establish its finite-sample uniform validity. Following split conformal prediction [Vovk et al., 2005, Lei et al., 2018], we assume each data source _D_[(] _[k]_[)] is randomly split to a training fold _D_ train[(] _[k]_[)][and a calibration fold] _[ D]_ calib[(] _[k]_[)][.][We assume] _[ {D]_ train[(] _[k]_[)] _[}] k[K]_ =1[are used] to obtain any conformity score function _sk_ : _X × Y →_ R associated with each distribution _k ∈_ [ _K_ ], which can be viewed as independent of the calibration folds and the test data. 

Our method begins by calibrating single-source conformal p-values 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0004-06.png)


By conformal prediction theory, inverting _p_[(] _[k]_[)] leads to a valid prediction set for the _k_ -th distribution: 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0004-08.png)


Our max-p aggregation scheme simply takes the maximum over the _K_ p-values, which is then inverted to yield the prediction set: 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0004-10.png)


It is straightforward to show that this prediction set is the union of single-source prediction sets in (2), and it enjoys finite-sample uniform validity. The proof of Theorem 1 is included in Appendix B.1. 

4 

**Theorem 1** (Finite-sample uniform validity) **.** _Let {p_[(] _[k]_[)] ( _y_ ) _}[K] k_ =1 _[and][p]_[(] _[y]_[)] _[be][defined][above.][Then,][the][aggre-] gated set equals the union of the per-source conformal sets:_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0005-01.png)


_For an independent test point_ ( _Xn_ +1 _, Yn_ +1) _∼ P with any mixture distribution P_ =[�] _k[π][k][P]_[ (] _[k]_[)] _[and][arbitrary] weights_[�] _[K] k_ =1 _[π][k]_[= 1] _[,][π][k][≥]_[0] _[,][the][prediction][set][achieves][valid][coverage]_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0005-03.png)


_which implies the uniform coverage_ (1) _for any individual source as a special case._ 

Despite the generality and validity of this approach, several questions remain. The first is _tightness_ . A natural concern is that the aggregated set is larger than any single-source prediction set that is valid in its respective distribution; it is therefore unclear whether the worst-case per-source coverage of (3) may be way above 1 _− α_ . The second is _efficiency_ , that is, how to design the individual scores _{sk}[K] k_ =1[so][that][the] aggregated set is of a reasonable size/length. If the individual sets _C_[ˆ][(] _[k]_[)] ( _Xn_ +1) do not overlap enough, their union may be overly large. These are the main questions addressed in the rest of the paper. 

## **3 Optimality of max-p aggregation** 

In this part, we address the questions above by studying the optimality of our max-p aggregation. First, we solve several population-level optimization programs to derive the optimal prediction sets with the smallest size/length subject to uniform coverage. Then, we show that our max-p aggregation is asymptotically equivalent to such optimal sets when the conformity scores converge to an optimal score. 

## **3.1 Size optimization under uniform validity** 

We begin with minimizing prediction set size/length subject to uniform validity when the distributions are known. Our final prediction sets are calibrated to satisfy the marginal uniform coverage (1). One could therefore study a marginal size-minimization program (we include this in Appendix A.1 for completeness). However, in the multi-source deployment setting, the test covariate distribution can be any mixture of _{PX_[(] _[k]_[)] _[}] k[K]_ =1[,][so][there][is][no][canonical][choice][of][how][to][average] _[|][C]_[(] _[X]_[)] _[|]_[over] _[X]_[when][defining][the][“optimal] size.” Instead, to obtain a canonical target for score design, we analyze a pointwise program: for each fixed _x ∈X_ , minimize _|C_ ( _x_ ) _|_ subject to uniform conditional coverage across sources. Importantly, we do not claim conditional validity, which is in principle impossible to achieve in finite sample [Foygel Barber et al., 2021]. Rather, we use the optimal form of prediction sets to guide the learning of suitable conformity scores. 

Let ( _X , A, ν_ ) and ( _Y, B, µ_ ) be finite measure spaces with _ν_ ( _X_ ) _< ∞_ and _µ_ ( _Y_ ) _< ∞_ , and write _ρ_ := _ν ⊗ µ_ , where _µ_ is the count measure for classification and the Lebesgue measure for regression. Throughout the paper, we assume that for each _k_ = 1 _, . . . , K_ , the covariate distribution _PX_[(] _[k]_[)] admits a density _rk_ ( _x_ ) with respect to _ν_ , and that _Y | X_ = _x_ has density _fk_ ( _· | x_ ) with respect to _µ_ . For a measurable subset _C_ ( _X_ ) _⊆Y_ , we define _|C_ ( _X_ ) _|_ as the cardinality in classification problems when _|Y| < ∞_ , and the Lebesgue measure in regression problems when _Y_ = R.[1] 

**Optimal prediction set under conditional validity.** Consider the following problem for any _x ∈X_ : 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0005-12.png)


> 1For clarity, we assume sufficient regularity of the underlying distributions so the prediction sets considered are measurable. 

5 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0006-00.png)


Any set that satisfies the constraints in (4) for every _x ∈X_ also satisfies uniform marginal coverage, so the conditional feasible set is (strictly) smaller than the marginal one. Therefore, integrating _|C[∗]_ ( _x_ ) _|_ over any distribution over _X_ is no smaller than the corresponding marginal optimum (Appendix A.1). 

Solving (4) amounts to a change-of-variable via the indicator function _Ix_ ( _y_ ) := 1 _{y ∈ C_ ( _x_ ) _}_ . For a clear presentation, we relax the range of _Ix_ ( _y_ ) to [0 _,_ 1], so that _Ix_ ( _y_ ) can be viewed as the probability of _y ∈ C_ ( _x_ ) for a randomized prediction set. This relaxation is without loss for our characterization: the objective and constraints are linear in _Ix_ ( _y_ ), so an optimum is attained by an indicator except possibly on the boundary where randomization can be used to achieve exact coverage. Theorem 2 offers the form of optimal prediction sets, whose proof relies on solving the dual problem of (4), and is included in Appendix B.3. 

**Theorem 2** ( _X_ -conditional optimality) **.** _For a fixed x ∈X , there exists non-negative multipliers λ[∗]_ ( _x_ ) = ( _λ[∗]_ 1[(] _[x]_[)] _[, . . . , λ][∗] K_[(] _[x]_[))] _[∈]_[R] _[K]_ + _[such][that,][with][h][λ]_[(] _[x, y]_[)][:=][�] _[K] k_ =1 _[λ][k]_[(] _[x]_[)] _[ f][k]_[(] _[y][ |][ x]_[)] _[,][an][optimal][solution][to]_[(][4][)] _[takes] the form_ 

_C[∗]_ ( _x_ ) = � _y ∈Y_ : _hλ∗_ ( _x, y_ ) _>_ 1� _∪ S_ ( _x_ ) _, S_ ( _x_ ) _⊆{y ∈Y_ : _hλ∗_ ( _x, y_ ) = 1 _}. In particular, λ[∗]_ ( _x_ ) = ( _λ[∗]_ 1[(] _[x]_[)] _[, . . . , λ][∗] K_[(] _[x]_[))] _[ ∈]_[R] _[K]_ + _[is][the][optimal][solution][to][the][dual][problem]_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0006-05.png)


_where_ ( _hλ_ ( _x, y_ ) _−_ 1)+ = max _{hλ_ ( _x, y_ ) _−_ 1 _,_ 0 _}. Moreover, complementary slackness holds for each k:_ 

_(i) If λ[∗] k_[(] _[x]_[)] _[ >]_[ 0] _[,][then][P]_[ (] _[k]_[)][(] _[Y][n]_[+1] _[∈][C][∗]_[(] _[x]_[)] _[ |][ X][n]_[+1][=] _[ x]_[) = 1] _[ −][α][;] (ii) If λ[∗] k_[(] _[x]_[) = 0] _[,][then][P]_[ (] _[k]_[)][(] _[Y][n]_[+1] _[∈][C][∗]_[(] _[x]_[)] _[ |][ X][n]_[+1][=] _[ x]_[)] _[ ≥]_[1] _[ −][α][.] (iii) There exists some k[∗] ∈_ [ _K_ ] _such that λ[∗] k[∗]_[(] _[x]_[)] _[ >]_[ 0] _[and][P]_[ (] _[k][∗]_[)][(] _[Y][n]_[+1] _[∈][C][∗]_[(] _[x]_[)] _[ |][ X][n]_[+1][=] _[ x]_[) = 1] _[ −][α][.] If additionally µ_ � _{y_ : _hλ[∗]_ ( _x, y_ ) = 1 _}_ � = 0 _, then C[∗]_ ( _x_ ) _is unique up to µ-null sets._ 

Here, in the complementary slackness results, one should understand the coverage probability _P_[(] _[k]_[)] ( _Yn_ +1 _∈ C[∗]_ ( _x_ ) _| Xn_ +1 = _x_ ) as randomizing the set with some probability _I[∗]_ ( _x, y_ ) _∈_ [0 _,_ 1] 

Theorem 2 reveals that for each _x_ , the optimal set keeps the smallest _µ_ -measure subset of _Y_ that contains at least 1 _− α_ conditional probability mass under every source. The dual weights _λ[∗] k_[(] _[x]_[)][quantify] which sources are locally hardest to cover: _λ[∗] k_[(] _[x]_[)] _[>]_[0][iff][the] _[k]_[-th][constraint][is][active][at] _[x]_[.][The][resulting] score _hλ[∗]_ ( _x, y_ ) =[�] _[K] k_ =1 _[λ] k[∗]_[(] _[x]_[)] _[f][k]_[(] _[y][ |][ x]_[)][acts][as][a][“shared][score,”][and][the][optimal][set][is][its][superlevel][set][at] threshold 1 (plus optional boundary randomization). 

## **3.2 Asymptotic optimality of max-p aggregation** 

Having studied the population-level optimal solutions, we proceed to show that our max-p aggregation is indeed _optimal_ and _tight_ . Connecting Section 3.1 with max-p aggregation, our result states that, when using individual conformity scores that converge to an optimal score, the resulting prediction set converges to the optimal (while retaining finite-sample coverage due to Theorem 1). 

As discussed, we focus on the (conceptually natural) conditional problem (4), and analogous results for the marginal problem follow from similar ideas. Let _λ[∗]_ ( _x_ ) _∈_ R _[K]_ +[be][a][dual][maximizer][for][the][program][(][4][),] and let _h[∗]_ ( _x, y_ ) :=[�] _[K] k_ =1 _[λ] k[∗]_[(] _[x]_[)] _[f][k]_[(] _[y][|][x]_[).][Recall][that][the][oracle-optimal][set] _[C][∗]_[(] _[x]_[)][is][of][the][form] 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0006-13.png)


6 

The boundary set _T_ ( _x_ ) is in general challenging to pinpoint: one may either randomize its inclusion to achieve exact 1 _− α_ coverage, or include _T_ ( _x_ ) with slightly inflated coverage. In classification problems, such choices would affect the prediction set size since the size of _T_ ( _x_ ) is non-negligible under the count measure. To avoid over-complication, we stick to the generic form of _C[∗]_ ( _x_ ) in (6) and isolate _S[∗]_ ( _x_ ) in our results. 

To describe the practical prediction set under max-p aggregation, we follow the procedure in Section 2. Splitting each source into training and calibration folds, we let _nk_ = _|D_ calib[(] _[k]_[)] _[|]_[.][Assuming][access][to][estimators] ˆ _fk_[(] _[n]_[)] ( _· | ·_ ) and _λ_[ˆ][(] _[n]_[)] ( _·_ ) obtained from _∪[K] k_ =1 _[D]_ train[(] _[k]_[)][,][we define] _[h]_[ˆ][(] _[x, y]_[) :=][ �] _[K] k_ =1 _[λ]_[ˆ] _[k]_[(] _[x]_[) ˆ] _[f][k]_[(] _[y][ |][ x]_[),][and use the confor-] mity score _sk_ ( _x, y_ ) := _−h_[ˆ] ( _x, y_ ) to construct the prediction set (3). To simplify boundary conditions, we adopt the randomized version of our general max-p aggregation which remains finite-sample valid. Specifically, for source _k ∈_ [ _K_ ] and a candidate label value _y ∈Y_ at a feature value _x ∈X_ , we define the randomized p-value 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0007-02.png)


where _Uk ∼_ Unif([0 _,_ 1]) are i.i.d. and independent of everything else, and we write _Sk,i_ = _−h_[ˆ] ( _Xi_[(] _[k]_[)] _, Yi_[(] _[k]_[)] ), and _sk_ ( _x, y_ ) = _−h_[ˆ] ( _x, y_ ). Finally, we construct our prediction set at level _α ∈_ (0 _,_ 1) via 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0007-04.png)


The superscript emphasizes the dependence on the sample size. 

Theorem 3 provides a size gap guarantee between our aggregated set and the oracle set as _nk →∞_ , controlled by the tie-region size. The proof is in Appendix B.4. 

**Theorem 3.** _Assume for each k, there exists constants Bk >_ 0 _such that_ sup _x,y fk_ ( _y|x_ ) _≤ Bk < ∞, and p p_ ˆ sup _x ∥λ_[ˆ] ( _x_ ) _− λ[∗]_ ( _x_ ) _∥∞ →_ 0 _, and_ sup _x,y |f_ ˆ _k_ ( _y|x_ ) _− fk_ ( _y|x_ ) _| →_ 0 _as nk, n →∞, where_ sup _x ∥λ_ ( _x_ ) _∥∞ ≤ M (tight in probability) for a constant M >_ 0 _. Then we have_ sup _x,y |h_[ˆ] ( _x, y_ ) _− h[∗]_ ( _x, y_ ) _| →p_ 0 _. Furthermore, let T_ := _{_ ( _x, y_ ) : _h[∗]_ ( _x, y_ ) = 1 _} and write its measure as ρ_ ( _T_ ) = � _T[dµ]_[(] _[y]_[)] _[dν]_[(] _[x]_[)] _[.][Then]_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0007-08.png)


_Here, with slight abuse of notation, we identify a set C_ ( _x_ ) _with its graph {_ ( _x, y_ ): _y ∈ C_ ( _x_ ) _} ⊆X × Y. Further, let |C|_ := � _X[µ]_[(] _[C]_[(] _[x]_[))] _[dν]_[(] _[x]_[)] _[,][then][for][any][optimal][C][∗]_[=] _[{]_[(] _[x, y]_[)][:] _[h][∗]_[(] _[x, y]_[)] _[>]_[1] _[} ∪][S][∗]_[(] _[x]_[)] _[,][we][have]_ lim sup _n→∞_ �� _|C_ ˆ( _n_ ) _| −|C ∗|_ �� _≤ ρ_ ( _T_ ) _. Moreover, for ν-almost all fixed values of x, there exists a measurable subset S∞_ ( _x_ ) _⊆ T_ ( _x_ ) _⊆Y such that there exists a subsequence {n_[(] _[j]_[)] _}, along which_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0007-10.png)



![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0007-11.png)


In words, Theorem 3 shows that, as long as our procedure in Section 2 is instantiated with individual score functions that are consistent for _−h[∗]_ ( _x, y_ ), our prediction set under max-p aggregation is asymptotically equivalent to the oracle set _C[∗]_ ( _x_ ) up to the boundary set _T_ ( _x_ ) (whose inclusion may depend on practitioners’ choice). This result has two key takeaways: 

- First, the max-p aggregation is _optimal_ up to the unavoidable ambiguity set _T_ , since it attains the oracle-optimal prediction set size. 

- Second, the max-p aggregation is (pointwise) _tight_ : the oracle set _C[∗]_ is shown in Theorem 2 to achieve exact 1 _− α_ (conditional) coverage for at least one distribution, which implies that max-p aggregation provides (asymptotically) exact coverage for at least one source. 

While we focus on the conditional problem throughout, we shall see that aiming for the conditionallyoptimal prediction set typically leads to tight _marginal_ worst-case coverage when evaluated over a specific test distribution in both simulations and real data experiments. 

7 

## **4 Practical algorithms** 

The above results establish the conceptual foundations of implementing MDCP. In this section, we develop concrete algorithms in classification and regression problems. At a high level, they proceed in three steps: 

- (i) First, we estimate per-source conditional models _f_[ˆ] _k_ ( _y | x_ ) by a black-box model. 

- (ii) Then, we learn a covariate-dependent nonnegative weight vector _λ_[ˆ] ( _x_ ) _∈_ R _[K]_ +[based][on][a][dual][problem.] 

- (iii) Finally, we apply the max-p aggregation with the same per-source scores _sk_ ( _x, y_ ) := _−_[�] _[K] ℓ_ =1 _[λ]_[ˆ] _[ℓ]_[(] _[x]_[) ˆ] _[f][ℓ]_[(] _[y][ |][ x]_[)] to build the MDCP sets. 

We focus on approximating the conditionally optimal score in Theorem 2, which relies on the conditional models _fk_ ( _y | x_ ) and the unknown dual functions _{λ[∗] k_[(] _[x]_[)] _[}][K] k_ =1[.][A][natural][idea][is][then][to][approximate][the] optimal scores _sk_ ( _x, y_ ) := _−hλ∗_ ( _x, y_ ), and couple them with the max-p aggregation. 

In Section 4.1, we introduce the general dual objective that allows the estimation of _{λ[∗] k_[(] _[x]_[)] _[}][K] k_ =1[,][and] demonstrate the consistency of this approach under suitable conditions. We then present the concrete implementations for classification in Section 4.2 and for regression in Section 4.3, respectively. 

## **4.1 Optimizing scores via an empirical dual objective** 

Section 3.2 motivates us to approximate the optimal solution _λ_ ( _·_ ) to the (integrated) dual problem 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0008-08.png)


˜ for a properly chosen distribution _ν_ ( _·_ ), and recall that _µ_ ( _·_ ) is the counting measure in classification and Lebesgue measure in regression. Theorem 4 is a simplified statement of a formal result in Appendix B.5. 

˜ **Theorem 4** (Informal) **.** _For any ν_ ( _·_ ) _that covers the support of X in the data, the optimal solution λ[∗]_ : _X →_ R _[K]_ + _[that][maximizes]_[Φ(] _[λ]_[)] _[in]_[(][8][)] _[coincides][with][the][dual][solution][λ][∗]_[(] _[x]_[)] _[given][in][Theorem][2][.]_ 

˜ A convenient option is to take _ν_ ( _·_ ) as the covariate distribution for the pooled dataset. This leads to the empirical dual objective (replacing expectation by empirical average, and unknown quantities by estimates) 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0008-12.png)


where we recall that _D_ = _{_ ( _Xi, Yi_ ) _}[n] i_ =1[=] _[∪][K] k_ =1 _[{]_[(] _[X] i_[(] _[k]_[)] _, Yi_[(] _[k]_[)] ) _}i∈Ik_ is the pooled dataset, and _n_ = _|D|_ . In ˆ addition, _p_ pool( _y | x_ ) estimates _p_ pool( _y | x_ ) =[�] _[K] k_ =1 _[w][k][f][k]_[(] _[x, y]_[)] _[ /]_[ �] _[K] k_ =1 _[w][k][f][k]_[(] _[x]_[),][the][conditional][density][for] the pooled data, and _wk_ is the fraction of the _k_ -th source data among the pooled dataset. A natural idea is then to parameterize the function _λ_ ( _·_ ) and solve the empirical risk minimization (ERM) problem (9). **Example: sieve estimation.** In the following, we present and theoretically justify such a procedure using the method of sieves [Geman and Hwang, 1982]. The sieve analysis below is one concrete way to verify the high-level consistency assumptions in Theorem 3. Practically, we implement _λ_ ( _·_ ) using splines or neural networks (see both Sections 4.2, 4.3 and experiments in Sections 5 and 6). 

Consider an increasing sequence Θ1 _⊂_ Θ2 _⊂· · ·_ of spaces of smooth functions. To be consistent with the language of ERM, we write the loss function and our estimator via 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0008-15.png)


8 

Here, ( _Xi, Yi_ ) are from the distribution of the pooled data _p_ pool( _x, y_ ), and _p_ ˆpool is a pre-trained estimator. We consider two examples of sieves inspired by Yadlowsky et al. [2022], Jin et al. [2022]. 

**Example 5** (Polynomials) **.** _Let Pol_ ( _J, ϵ_ ) _be the space of J-th order polynomials on_ [0 _,_ 1] _truncated at ϵ >_ 0 _:_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0009-02.png)



![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0009-03.png)


_Then we define_ Θ _n_ = Θ _[K] n,_ 0 _[,][where]_[Θ] _[n,]_[0][=] _[ {][x][ �→]_[�] _[d] j_ =1 _[f][j]_[(] _[x][j]_[):] _[f][j][∈]_[Spl(] _[J][n][,]_[ 0)] _[, j]_[= 1] _[, . . . , d][}][for][J][n][→∞][.]_ 

In both examples, we consider coordinate-wise function _{fj_ ( _xj_ ) _}[d] j_ =1[for] _[X][⊆]_[R] _[d]_[in][a][sieve][series,][so] that[�] _[d] j_ =1 _[f][j]_[(] _[x][j]_[)] _[∈]_[Θ] _[n,]_[0][,][and][the][optimal][dual][variables] _[λ][∗]_[(] _[·]_[):] _[X][→]_[R] _[K]_[is][approximated][by][elements] in Θ _n_ = Θ _[K] n,_ 0[.][Here,][we][truncate][the][functions][away][from][zero][for][simplicity.][Note][that][if] _[λ][∗] k_[(] _[x]_[)][is][always] positive and continuous and _X_ is a compact set, then there exists a positive _ϵ >_ 0 such that inf _x∈X λ[∗] k_[(] _[x]_[)] _[ ≥][ϵ]_[.] In practice, we can set _ϵ_ to be small enough, or let _ϵ_ = _ϵn_ decays slowly to zero. 

Next, we show the convergence of _λ_[ˆ] ( _·_ ) _∈_ Θ _n λ[∗]_ ( _·_ ). For _p_ 1 = _⌈p⌉−_ 1 and _p_ 2 = _p − p_ 1, we define 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0009-07.png)


To ensure non-negativeness, we define the truncated function class Λ _[p] c,_ +[:=] � _x �→_ max _{f_ ( _x_ ) _,_ 0 _}_ : _f ∈_ Λ _[p] c_ �. We denote the oracle minimizer and loss function as 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0009-09.png)


Throughout, Epool[ _·_ ] denotes the expectation under the pooled distribution, and _ℓ_[ˆ] ( _·_ ) is viewed as fixed. Assuming the optimal dual functions in Theorem 2 obeys _λ[∗] ∈_ Θ = (Λ _[p] c,_ +[)] _[K]_[,][Theorem][4][ensures][the] minimizer _λ[∗]_ ( _·_ ) in (11) coincides with the optimal _λ[∗]_ ( _·_ ) in Theorem 2; we thus use the same notation. 

Similar to Jin et al. [2022, Theorem 1], we can show that the solution (10) is close to _λ[∗]_ once _p_ ˆpool is accurate. Our formal results build on the following two assumptions. Assumption 7 is a natural condition that the estimation error in _p_ ˆpool translates to errors in population risk minimizer of the same order. Assumption 8 collects regularity conditions that are standard in the literature and hold for convex and smooth functions; it is needed to derive rates, but consistency holds under even weaker conditions. 

ˆ ˆ **Assumption 7.** _Assume ∥λ[∗] − λ_[¯] _[∗] ∥L_ 2 = _OP_ ( _∥p_ pool _− p_ pool _∥L_ 2) _and ∥λ[∗] − λ_[¯] _[∗] ∥∞_ = _OP_ ( _∥p_ pool _− p_ pool _∥∞_ ) _._ 

**Assumption 8.** _Suppose X_ =[�] _[d] j_ =1 _[X][j][is][the][Cartesian][product][of][compact][intervals,][and][θ][∗][∈]_[Θ = (Λ] _[p] c_[)] _[K] for some c >_ 0 _. Suppose Ppool has positive density on X . We assume the function_ E _pool_ [ _ℓ_[ˆ] ( _λ, x, Y_ ) _| X_ = _x_ ] _is ηλ_ ¯ _-strongly[∗]_ ( _x_ ) _∥_ 2 _< ϵconvexfor sufficientlyat λ_[¯] _[∗]_ ( _x_ ) _forsmallall ϵ >x ∈X_ 0 _, .whereAlso,∥· ∥|ℓ_[ˆ] ( _θ, x, y_ 2 _is the_ ) _−Euclideanℓ_[ˆ] ( _λ_[¯] _[∗] , x, y_ ) _norm,| ≤ ℓ_[¯] ( _x, yand_ ) _∥_ sup _θ_ ( _xx_ ) _∈X − λ_[¯] E _[∗] pool_ ( _x_ )[¯ _∥ℓ_ 2( _x, Yfor_ ) _∥_[2] _θ_ ] _< M_ ( _x_ ) _− for some constant M >_ 0 _. Furthermore, there exists a constant C_ 1 _such that_ E _pool_ [ _ℓ_[ˆ] ( _θ, X, Y_ ) _− ℓ_[ˆ] ( _λ_[¯] _[∗] , X, Y_ )] _≤ C_ 1 _∥θ − λ_[¯] _[∗] ∥_[2] _L_ 2 _[when][θ][∈]_[(Λ] _[p] c_[)] _[K][and][∥][θ][ −][λ]_[¯] _[∗][∥][L]_ 2 _[is][sufficiently][small.]_ 

9 

Theorem 9 justifies using sieve approximation and ERM to learn the functions _λ[∗]_ ( _·_ ). Its proof largely follows Jin et al. [2022], and is included in Appendix B.6 for completeness. 

**Theorem 9.** _Under Assumptions 7 and 8, We set Jn_ ˆ _≍_ ( _n/_ log _n_ )[1] _[/]_[(2] _[p]_[+] _[d]_[)] _for the sieve estimators in Examples 5 and 6, and suppose λ_[ˆ] = argmin _θ∈_ Θ E[ˆ] pool� _ℓ_ ( _θ, X, Y_ )� _. Then employing the function classes in_ ˆ _the two examples, we have ∥λ_[ˆ] _− λ[∗] ∥L_ 2 = _OP_ �([lo] _n_[g] _[ n]_[)] _[p/]_[(2] _[p]_[+] _[d]_[)][�] + _OP_ ( _∥p_ pool _− p_ pool _∥L_ 2) _and ∥λ_[ˆ] _− λ[∗] ∥∞_ = _OP_ �([lo] _n_[g] _[ n]_[)][2] _[p]_[2] _[/]_[(2] _[p]_[+] _[d]_[)][2][�] + _OP_ ( _∥p_ ˆpool _− p_ pool _∥∞_ ) _._ 

Our results so far justify an ERM approach to learn the unknown _λ[∗] k_[(] _[x]_[)][and][approximate][the][optimal] MDCP set. Suppose that the true optimal dual functions _λ[∗] k_[(] _[x]_[)][in][Theorem][2][is][sufficiently][smooth][in] _x_ , and that we solve the ERM (10) with a suitable sieve class based on a consistent _p_ ˆpool( _y | x_ ). Theorem 9 then ensures _λ_[ˆ] ( _·_ ) converges to _λ[∗]_ ( _·_ ). Thus, as long as the _f_[ˆ] _k_ ( _· | ·_ )’s are consistent, taking _sk_ ( _x, y_ ) = _−_[�] _[K] k_ =1 _[λ]_[ˆ] _[k]_[(] _[x]_[) ˆ] _[f][k]_[(] _[y][ |][ x]_[)][yields][an][MDCP][set][that][is][asymptotically][optimal.] 

## **4.2 Algorithm for classification** 

We now state the concrete MDCP algorithm for the classification setting. Recall that we split the labeled data into the training fold _D_ train = _∪[K] k_ =1 _[D]_ train[(] _[k]_[)][and][the][calibration][fold] _[D]_[calib][=] _[ ∪][K] k_ =1 _[D]_ calib[(] _[k]_[)][.][For][each][source] _k_ , we fit a classifier _p_ ˆ _k_ ( _y | x_ ) on the training fold _D_ train[(] _[k]_[)][by any off-the-shelf algorithm.][Next, we learn] _[ λ][∗]_[(] _[x]_[) via] solving an empirical optimization objective. We approximate the covariate-dependent, nonnegative weights _λk_ ( _x_ ) via basis functions such as splines or hidden representations from neural networks. Let Λ( _x_ ) _∈_ R _[m]_ denote the vector of basis functions evaluated at a covariate value _x_ . For _K_ sources, we collect the basis coefficients into a matrix Θ _∈_ R _[K][×][m] ,_ with row _θj[⊤]_[parameterizing][the] _[j]_[-th][weight][function.][We][then][define] 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0010-05.png)


where softplus( _t_ ) = log(1 + _e[t]_ ) is applied elementwise. Accordingly, the score function with parameter Θ is _h_ ( _x, y_ ; Θ) :=[�] _[K] k_ =1 _[λ][k]_[(] _[x]_[; Θ)] _[ ·][p]_[ˆ] _[k]_[(] _[y][ |][ x]_[)] _[.]_ 

We fit the parameters Θ[ˆ] by maximizing the Lagrangian-inspired empirical objective in Section 4.1. For a miscoverage level _α_ , the objective as a function of Θ is given by 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0010-08.png)


where E[ˆ] _D_ train[ _·_ ] denotes the empirical average across the pooled training fold, ( _t_ ) _−_ = min _{t,_ 0 _}_ denotes the negative part, and _p_ ˆpool( _y | x_ ) is an estimator for _p_ pool( _y | x_ ). It can be obtained by simply fitting a classifier ˆ over the pooled data, or assembling the single-source models via _p_ pool( _y | x_ ) =[�] _k[w]_[ˆ] _[k]_[ ˆ] _[p][k]_[(] _[y][ |][ x]_[)][with][the] ˆ marginal weights _wk_ = _|D_ train[(] _[k]_[)] _[|][/]_[ �] _ℓ[|D]_ train[(] _[ℓ]_[)] _[|]_[,][avoiding][another][model][fit][for][fast][implementation.] 

Finally, given the fitted parameters Θ,[ˆ] we define the (source-invariant) score function 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0010-11.png)


and use them to calibrate the final prediction sets following (3) or the procedure outlined in Section 3.2. The entire procedure is summarized in Algorithm 1, which also covers regression problems below. 

## **4.3 Algorithm for regression** 

For regression problems, the data splitting, parameterization and estimation of _λ_ ( _x_ ) are similar. The key difference is in fitting the conditional density function _fk_ ( _y | x_ ). While one can use any estimator, here we model _Y_ = _µ_ ( _X_ ) + _σ_ ( _X_ ) _· ϵ_ for some _ϵ ∼ N_ (0 _,_ 1). Then, we use nonparameteric methods, such as gradient boosting, to estimate _µ_ ( _x_ ) and _σ_ ( _x_ ) using each _D_ train[(] _[k]_[)][;][see Appendix][ C.2][ for a detailed estimation procedure.] 

10 

**Algorithm 1** Multi-Distribution Conformal Prediction (MDCP) 

**Input:** Data _D_ = _∪[K] k_ =1 _[D]_[(] _[k]_[)][from] _[K]_[sources,][test][input] _[X][n]_[+1][,][significance][level] _[α]_[,][problem] `[mode]`[.] 1: Split the data _D_ into _D_ train = _∪[K] k_ =1 _[D]_ train[(] _[k]_[)][and] _[D]_[calib][=] _[ ∪][K] k_ =1 _[D]_ calib[(] _[k]_[)][.] 

- 2: `// Train per-source models` 

- 3: **if** `mode` = classification **then** 

4: Fit any classifier _p_ ˆ _k_ ( _y | x_ ) on _D_ train[(] _[k]_[)][for] _[k][∈]_[[] _[K]_[]][and] _[p]_[ˆ][pool][(] _[y][ |][ x]_[)][on] _[D]_[train][.] 

- 5: **else if** `mode` = regression **then** 

6: Fit conditional density estimator _f_[ˆ] _k_ ( _y | x_ ) on _D_ train[(] _[k]_[)][via,][e.g.,][conditional][gaussian][model][for] _[k][∈]_[[] _[K]_[]] and a pooled estimator _f_[ˆ] pool( _y | x_ ) on _D_ train. 

- 7: **end if** 

- 8: `// Fit Lagrange multiplier` _λ_ ( _·_ ) 

- 9: Solve the empirical objective (13) on _D_ train to obtain spline parameters Θ.[ˆ] 

- 10: `// MDCP set on test point` _x_ 

- 11: **if** `mode` = classification **then** 12: Set _sk_ ( _x, y_ ) = _−_[�] _[K] ℓ_ =1 _[λ][ℓ]_[(] _[x]_[;][ˆΘ)ˆ] _[p][ℓ]_[(] _[y][ |][ x]_[)][via][(][12][)][for][all] _[k][∈]_[[] _[K]_[].] 13: Compute _sk_ ( _Xn_ +1 _, y_ ) for all _y ∈Y_ , and _p_[(] _[k]_[)] ( _y_ ) with _D_ calib[(] _[k]_[)][using][(][7][)][for] _[k][∈]_[[] _[K]_[].] 14: Compute _C_[ˆ] ( _x_ ) = _{y_ : _p_ ( _y_ ) _≥ α}_ with _p_ ( _y_ ) = max _k p_[(] _[k]_[)] ( _y_ ). 

- 15: **else if** `mode` = regression **then** 

16: Set _sk_ ( _x, y_ ) = _−_[�] _[K] ℓ_ =1 _[λ][ℓ]_[(] _[x]_[;][ˆΘ) ˆ] _[f][ℓ]_[(] _[y][ |][ x]_[)][via][(][12][)][for][all] _[k][∈]_[[] _[K]_[].] 17: Generate _y_ -grid and use a grid search to construct prediction set _C_[ˆ] ( _Xn_ +1) (Appendix C.3). 

- 18: **end if** 

**Output:** Prediction set _C_[ˆ] ( _Xn_ +1). 

Given the estimators _µ_ ˆ( _x_ ) and _σ_ ˆ( _x_ ), our working model is _f_[ˆ] _k_ ( _y | x_ ) _∝_ exp _{−_ ( _y − µ_ ˆ( _x_ ))[2] _/_ (2ˆ _σ_ ( _x_ )[2] ) _}_ . In the single-source case, this reduces to the prediction set proposed by Lei et al. [2018]. We follow the same parameterization and ERM objective as in the classification case to obtain the estimated basis parameters Θ[ˆ] and scores _sk_ ( _x, y_ ) = _−_[�] _[K] ℓ_ =1 _[λ][ℓ]_[(] _[x]_[;][ˆΘ) ˆ] _[f][ℓ]_[(] _[y][ |][ x]_[), which are then used to calibrate the single-source p-values (][7][)] and the corresponding MDCP set in the same way as in Section 4.2. 

Finally, we note that thresholding the learned score function _sk_ ( _x, y_ ) = _−_[�] _[K] ℓ_ =1 _[λ][ℓ]_[(] _[x]_[;][ˆΘ) ˆ] _[f][ℓ]_[(] _[y][ |][ x]_[)][does] not necessarily lead to an interval MDCP set. However, as we model _f_[ˆ] _k_ ( _y | x_ ) as a normal distribution, the MDCP set must be the union of at most _K_ intervals. This structure allows us to compute a super-set of our MDCP set via an efficient grid search. For brevity, we defer the details and justifications to Appendix C.3. 

## **5 Simulation studies** 

In this section, we assess the validity and efficiency of our algorithms in diverse classification and regression settings, and investigate how the heterogeneity and separation among sources impact the performance. 

## **5.1 Simulation settings** 

We begin by outlining the common setup in both classification and regression settings. We consider _K_ = 3 sources, a feature dimension of _d_ = 10, and a nominal level at _α_ = 0 _._ 1. Across all settings, the features are generated by _Xi_[(] _[k]_[)] _∼N_ �0 _,_ Σ� with Σ _ij_ = 0 _._ 2 + 0 _._ 8 1 _{i_ = _j}_ , and the heterogeneity across sources is in the conditional label distribution. In each run, we randomly draw a set _I ⊂{_ 1 _, . . . , d}_ of size _|I|_ = 4 uniformly at random, so the labels depend on _X_ only through _XI_ . We examine three suites of experiments: 

- (1). `Linear` : In this suite, the labels are generated from a linear model involving _XI_ . 

11 

- (2). `Nonlinear` : The labels are from a nonlinear model of _XI_ ; otherwise the same as `Linear` . 

- (3). `Temperature` : This final suite focuses on the linear setting where a “temperature” parameter _τ_ controls the degree of heterogeneity or separation across sources. 

The specific data generating processes (DGPs) are given in Section 5.2 and Section 5.3 for classification and regression settings, respectively. Across all experiments, we generate _nk_ = 2000 labeled samples from each source, and randomly split the pooled data into training (37.5%), calibration (12.5%), and test (50%) folds. We compare our MDCP method in Algorithm 1 with two competing methods: 

- (i). `Baseline-src-` _k_ : The standard conformal prediction set _C_[ˆ] src- _k_ with calibration data from source _k_ . 

- (ii). `Baseline-agg` : A simple max- _p_ aggregation of per-source prediction sets _C_[ˆ] max-p := _∪[K] k_ =1 _[C]_[ˆ][src-] _[k]_[.][This] is the baseline without efficiency-oriented score learning. 

For each configuration, we repeat the experiments for _N_ = 100 times and report the mean results. For fair comparison, all the methods build on the same conditional mean and standard deviation estimators to be specified later. With these choices, the single-source baseline is standard conformal prediction sets with the widely-used TPS score [Sadinle et al., 2019] which tends to produce efficient prediction sets in classification and the variance-adaptive score of Lei et al. [2018] in regression problems. 

## **5.2 Simulations in classification settings** 

**Data generating processes.** We simulate _C_ = 6 classes. For source _k ∈_ [ _K_ ] and class _c ∈_ [ _C_ ], the conditional class probability is given by a multinomial model _fk_ ( _y_ = _c | x_ ) _∝_ exp _{ηkc_ ( _x_ ) _}_ with _ηkc_ ( _x_ ) = _ξk_ ( _bkc_ + _βkc[⊤][x]_[)][+][1] _[{][c][>]_[1] _[}][ g]_[(] _[x]_[).] Here, with a temperature parameter _τ ∈_ R, the linear signal is _ξk_ = i.i.d. 2 _._ 5(1 + 0 _._ 25 _τ · uk_ ) with _uk ∼_ Unif([ _−_ 1 _,_ 1]), and the heterogeneous intercept is independently sampled as _bkc ∼N_ (0 _,_ (0 _._ 4 _τ_ )[2] ). The source-specific linear coefficients are _βkc_ = _β_[¯] _c_ + _τ ·_ ∆ _kc_ where, after a random sample of _I ⊆_ [ _d_ ] with _|I|_ = 4, we independently sample ( _β_[¯] _c_ ) _j ∼N_ (0 _,_ 1) and (∆ _kc_ ) _j ∼N_ (0 _,_ 0 _._ 15[2] ) for each _j ∈I_ and set ( _β_[¯] _c_ ) _j_ = (∆ _kc_ ) _j_ = 0 for _j ∈I/_ . Finally, the nonlinear component _g_ ( _x_ ) is set as zero in the `Linear` experiments, and we vary its definition in three DGPs in the `Nonlinear` experiments: (a) interaction: _g_ ( _x_ ) = 2[�] ( _u,v_ ) _[w][uv][ x][u][x][v]_[;][(b)][sinusoid:] _[g]_[(] _[x]_[)][=][2][�][3] _r_ =1 _[a][r]_[ sin(] _[u] r[⊤][x]_[+] _[b][r]_[),][(c)][softplus:] _g_ ( _x_ ) = 2[�][3] _r_ =1 _[a][r]_[ log] �1 + exp( _u[⊤] r[x]_[ +] _[ b][r]_[)] �. At the beginning of each experiment, we sample the weights _wuv_ , the linear coefficients _ar_ , _ur_ , and _br_ (the detailed processes are in Appendix C.1); afterwards, we draw the labeled and unlabeled data conditional on them. In the `Linear` and `Nonlinear` experiments, the temperature parameter is fixed at _τ_ = 2 _._ 5. In the evaluation of `Temperature` experiments, we focus only on the linear model with _g_ ( _x_ ) _≡_ 0 and vary the temperature _τ ∈{_ 0 _._ 5 _,_ 1 _._ 5 _,_ 2 _._ 5 _,_ 3 _._ 5 _,_ 4 _._ 5 _}_ . 

**Method implementations.** We implement the three competing methods based on the same estimators (built from the training folds) for fair comparison. We train a gradient boosting classifier _p_ ˆ _k_ ( _y | x_ ) to estimate _P_[(] _[k]_[)] ( _Y_ = _y | X_ = _x_ ) for each source _k_ , and a separate gradient boosting classifier on the pooled training data to estimate _p_ pool( _y | x_ ). Following Section 4.2, we specify the per-source scores 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0012-09.png)


where, following the procedure in Section 4.2, we parameterize the nonnegative weight functions _λk_ ( _x_ ) as spline functions, and learn _λ_[ˆ] _k_ ( _x_ ) by minimizing the empirical objective (9). Specifically, we use a cubic B- spline basis with 3 polynomial degree and 5 knots placed uniformly over the range of the observed covariates, constructed using the `SplineTransformer` in the `scikit-learn` Python package. The multipliers _λ_[ˆ] _k_ ( _x_ ) are trained on the same training fold based on the fitted classifiers _p_ ˆ _k_ ( _y | x_ ) and _p_ ˆpool( _y | x_ ), i.e., we reuse the training data. In both `Baseline-src-` _k_ and `Baseline-agg` , we use the widely-used TPS score [Sadinle et al., 2019] with the same fitted probabilities _p_ ˆ _k_ ( _y | x_ ) to build single-source and aggregated prediction sets, thereby serving as baselines with the same fitted models without optimizing for multi-distribution efficiency. 

12 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0013-00.png)


**----- Start of picture text -----**<br>
Baseline agg Baseline src 0 Baseline src 1 Baseline src 2 MDCP<br>1.00 1.00 6<br>0.90<br>0.90<br>4<br>0.70 2<br>0.70<br>0.49 0.15 0<br>Method Method Method<br>Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCP Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCP Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCP<br>Avg set size<br>Overall coverage<br>Worst-case coverage<br>**----- End of picture text -----**<br>


Figure 2: Performance of MDCP and baselines in the classification `Linear` experiments, where the bars represent the result of each method averaged over _N_ = 100 runs, and the dots represent the result in each run. Left: coverage over all test data. Middle: worst-case coverage over single-source test data. Right: average set size over all test data. 

**Simulation results.** Figure 2 presents the comparison between MDCP and two baselines in the `Linear` setting, in terms of average coverage (evaluated over all the test data), worst-case coverage (over each source of test data), and average set size (over all the test data). The single-source sets lead to severe under-coverage. Due to max-p aggregation, both `Baseline-agg` and MDCP achieve valid worst-case coverage, yet MDCP delivers (i) significant efficiency improvement, and (ii) tight worst-case coverage. MDCP yields prediction sets that are on average a 34.39% smaller than max- _p_ aggregation. MDCP is also more stable: the standard deviation of set size is 47.10% lower then the max- _p_ baseline. The tight worst-case coverage shows that although we focused on the conditional optimal formulation, the complementary slackness is quite strong when evaluated marginally (Theorem 2). 

Figure 3 presents the results in the `Nonlinear` settings. While single-source calibration severely undercovers, MDCP maintains tight worst-case coverage across all settings. MDCP again produces much smaller prediction sets relative to `Baseline-agg` . Notably, in the softplus setting, MDCP achieves even smaller set sizes than single-source sets, showing the benefits of both max-p aggregation and efficiency optimization: MDCP adaptively concentrates coverage on regions with strong overlap across sources. 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0013-04.png)


**----- Start of picture text -----**<br>
Max-agg baseline Source 0 Source 1 Source 2 MDCP<br>Overall coverage Worst-case coverage Avg set size<br>1.00 1.00<br>6<br>0.90 0.90 5<br>4<br>0.70 3<br>0.70<br>2<br>0.42 0.13 1<br>Nonlinear term Nonlinear term Nonlinear term<br>linear interaction sinusoid softplus linear interaction sinusoid softplus linear interaction sinusoid softplus<br>**----- End of picture text -----**<br>


Figure 3: Performance of MDCP and baselines in the classification `Nonlinear` experiments. The _x_ -axis is the setting of the nonlinear term _g_ ( _x_ ), with the linear setting presented for comparison. The connected dots are average results colored by method, with the colored, dimmed dots being the results in each of the _N_ = 100 runs. Left: coverage over all test data. Middle: worst-case coverage over single-source test data. Right: average set size over all test data. 

We further investigate the effect of the separation of sources in Figure 4. As the temperature parameter _τ_ increases and the per-source distributions move farther apart, the coverage of single-source baseline declines. 

13 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0014-00.png)


**----- Start of picture text -----**<br>
Baseline (max agg) Baseline src 0 Baseline src 1 Baseline src 2 MDCP<br>Overall coverage Worst-case coverage Avg set size<br>6<br>0.9<br>0.9<br>0.8<br>4<br>0.8 0.7<br>0.6 2<br>0.7<br>0.5<br>0.5 1.5 2.5 3.5 4.5 0.5 1.5 2.5 3.5 4.5 0.5 1.5 2.5 3.5 4.5<br>Temperature Temperature Temperature<br>**----- End of picture text -----**<br>


Figure 4: Performance of MDCP and baselines in the classification `Temperature` experiments. The _x_ -axis is the temperature parameter _τ_ . Each line shows the results of a method averaged over _N_ = 100 runs, with shaded _±_ 1 standard deviation across runs. Left: coverage over all test data. Middle: worst-case coverage over single-source test data. Right: average set size over all test data. 

Nevertheless, MDCP maintains tight worst-case coverage and substantial efficiency gain over `Baseline-agg` . 

**Additional results: optimization stability.** To study the stability of training the multipliers, in Appendix D.1, we extend the objective (13) with a penalty on certain norms of Θ to encourage stability, and evaluate a variant of Algorithm 1 that optimizes the penalty parameter in the training process. Across all the settings, the improvement of this approach is negligible, showing that MDCP is stable enough. 

**Additional results: covariate shift settings.** Our current settings introduce concept shift in the conditional distribution of the labels. We conduct additional experiments in settings where heteroegeneity across sources are due to (i) covariate shift and (ii) both covariate and concept shifts. These experiments lead to largely similar messages; see Appendix D.2.1 for details. 

## **5.3 Simulations in regression problems** 

**Data generating processes.** In all regression settings, for source _k ∈_ [ _K_ ], we sample the labels via _Y_ = _µk_ ( _X_ )+ _εk_ , with independent noise _εk ∼N_ (0 _, σk_[2][).][Following similar design ideas as in the classification] settings, given a temperature parameter _τ ∈_ R, the regression function is _µk_ ( _x_ ) = _βk[⊤][x]_[+] _[b][k]_[ +] _[g]_[(] _[x]_[), where the] source-specific coefficient is given by _βk_ = _β_[¯] +0 _._ 2 _τ · δk_ , with _β_[¯] _j ∼N_ (0 _,_ 1) and ( _δk_ ) _j ∼N_ (0 _,_ 1) independently drawn for _j ∈I_ and _β_[¯] _j ≡_ 0 and ( _δk_ ) _j ≡_ 0 for _j ∈I/_ , and _I_ is the randomly drawn set of signals. The sourcespecific intercept is given by _bk_ = _b_ + _τ · vk_ with independently drawn _b ∼N_ (0 _,_ 0 _._ 5[2] ) and _vk ∼N_ (0 _,_ 0 _._ 5[2] ). In each run, we randomly sample a signal-to-noise ratio from Unif([5 _,_ 10]), and achieve it by adjusting the noise variance _σk_[2][.][Finally,][the][nonlinear][component] _[g]_[(] _[x]_[)][is][set][to][be][zero][in][the] `[Linear]`[experiments,][and] we consider the same three choices of _g_ ( _x_ ) in the `Nonlinear` experiments as in the classification settings (Section 5.2), with the same sampling process of the hyper-parameters. 

We fix _τ_ = 2 _._ 5 in `Linear` and `Nonlinear` experiments. In `Temperature` setting, we focus only on the linear model and vary _τ ∈{_ 0 _._ 5 _,_ 1 _._ 5 _,_ 2 _._ 5 _,_ 3 _._ 5 _,_ 4 _._ 5 _}_ ; in addition, we sample _u ∼_ Unif([ _{_ 1 _− τ/_ 4 _}_ + _,_ 1 + _τ/_ 4]) and multiply the SNR-calibrated _σk_ by _u_ , so that the temperature also affect the noise level. In each run, we sample all the hyper-parameters once, and generate the data conditional on them. 

**Method implementations.** In the regression procedure, the optimal score function relies on the condition density _fk_ ( _y | x_ ) in each source _k_ . As mentioned in Section 4.3, to avoid the challenging conditional density estimation, we model the data as _PY_[(] _[k] |_[)] _X_ = _x[∼N]_[(] _[µ][k]_[(] _[x]_[)] _[, σ][k]_[(] _[x]_[))][for][some][functions] _[µ][k]_[(] _[x]_[)][=][E][(] _[k]_[)][[] _[Y][|][ X]_[=] _[x]_[]] and _σk_[2][(] _[x]_[) = Var][(] _[k]_[)][(] _[Y][|][ X]_[=] _[ x]_[),][and][obtain][their][estimates] _[µ]_[ˆ] _[k]_[(] _[·]_[)][and] _[σ]_[ˆ] _[k]_[(] _[·]_[)][on][the][training][fold][via][gradient] boosting decision trees. Plugging in the two estimates leads to the estimated per-source conditional densities 

14 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0015-00.png)


**----- Start of picture text -----**<br>
Baseline agg Baseline src 0 Baseline src 1 Baseline src 2 MDCP<br>0.99 0.99<br>0.90 15<br>0.90<br>10<br>0.70<br>0.70 5<br>0.30 0.00 0<br>Method Method Method<br>Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCP Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCP Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCP<br>Overall coverage Avg interval width<br>Worst-case coverage<br>**----- End of picture text -----**<br>


Figure 5: Evaluation with regression `Linear` suites; details are otherwise the same as Figure 2. 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0015-02.png)


**----- Start of picture text -----**<br>
Max-agg baseline Source 0 Source 1 Source 2 MDCP<br>Overall coverage Worst-case coverage Avg interval width<br>1.00 1.00<br>35<br>0.90 0.90 30<br>25<br>20<br>0.70<br>15<br>0.70<br>10<br>5<br>0.31 0.00 0<br>Nonlinear term Nonlinear term Nonlinear term<br>linear interaction sinusoid softplus linear interaction sinusoid softplus linear interaction sinusoid softplus<br>**----- End of picture text -----**<br>


Figure 6: Evaluation with regression `Nonlinear` suites; details are otherwise the same as in Figure 3. 

_f_ ˆ _k_ ( _y | x_ ) using gradient boosting decision trees. In the same way, we fit a pooled Gaussian working model on pooled training data to obtain (ˆ _µ_ pool( _x_ ) _,_ ˆ _σ_ pool( _x_ )) for the conditional density estimate _p_ ˆpool( _y | x_ ). The conformity score for MDCP is then given by _sk_ ( _Xi, Yi_ ) := _−_[�] _[K] k_ =1 _[λ]_[ˆ] _[k]_[(] _[X][i]_[) ˆ] _[f][k]_[(] _[Y][i][|][X][i]_[)] _[,]_[where][we][parameterize] _λ_ ( _x_ ) _∈_ R _[K]_ +[as][the][spline][function][as][in][Section][ 5.2][ and learn] _[λ]_[ˆ] _[k]_[(] _[x]_[) by][minimizing][the empirical objective (][9][)] ˆ ˆ on the same training fold. Both baselines use the conformity score _Vk_ ( _x, y_ ) = ( _y − µk_ ( _x_ )) _/σk_ ( _x_ ) with the same estimated functions as in MDCP, paralleling the method in [Lei et al., 2018]. 

**Simulation results.** Figure 5 shows the performance of the competing methods in the `Linear` settings. MDCP achieves a tight 90.25% worst-case coverage showing the (approximate) complementary slackness, while the single-source baseline severely under-covers. On average, MDCP attains a 22.44% smaller set compared to the `Baseline-agg` method, with notably smaller variance of interval width. The naive method is conservative, yielding 97.32% average and 95.94% worst-case coverage in the test data. In the `Nonlinear` setting presented in Figure 6, MDCP maintains valid average and worst-case coverage while achieving consistently shorter prediction sets across all settings compared to the max-p baseline. In contrast, the single-source baseline fails to achieve validity, and the `Baseline-agg` method is overly conservative even in the worst-case sense. MDCP strikes a balance between coverage and efficiency: it achieves much higher coverage with just slightly longer prediction sets than the single-source counterparts, and avoids the unnecessary overlap with tight coverage compared with `Baseline-agg` . 

In the `Temperature` experiments where the parameter _τ_ governs the separation of multiple sources, as shown in Figure 7, we observe similar messages as in the classification case. The performance of `Baseline-src-` _k_ degrades as _τ_ increases, with lower average and worst-case coverage and larger standard 

15 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0016-00.png)


**----- Start of picture text -----**<br>
Baseline (max agg) Baseline src 0 Baseline src 1 Baseline src 2 MDCP<br>Overall coverage Worst-case coverage Avg interval width<br>1.0<br>15<br>0.9<br>0.8<br>0.8 10<br>0.6<br>0.7 5<br>0.6 0.4<br>0.5 1.5 2.5 3.5 4.5 0.5 1.5 2.5 3.5 4.5 0.5 1.5 2.5 3.5 4.5<br>Temperature Temperature Temperature<br>**----- End of picture text -----**<br>


Figure 7: Evaluation with regression `Temperature` suites; details are otherwise the same as in Figure 4. 

deviation. By contrast, MDCP stands right at the point of tight coverage, while achieving uniformly smaller set widths than the `Baseline-agg` method by adaptively trading off the coverage across sources. 

**Additional results: optimization stability.** We conduct the same suite of experiments on the optimization process as in the classification settings; see Appendix D.1 for details. Again, our results across all the simulation settings demonstrate the stability of the current optimization process. 

**Additional results: covariate shift settings.** Similar to Section 5.2, we additionally evaluate settings with covariate shifts. We observe similar messages summarized in Appendix D.2.2. 

## **6 Real-data applications** 

Finally, we demonstrate the broad application of MDCP through three real datasets. Section 6.1 focuses on a classification task where MDCP protects against subpopulation shift. Section 6.2 addresses uniform coverage across urban and rural areas when inferring economic information from satellite image. Section 6.3 uses a medical service dataset to ensure fairness across sensitive groups without observing the group label. 

## **6.1 Functional category of satellite image under subpopulation shift** 

Satellite ML has been widely used to detect functional land uses, allocate resources, and inform risk analyses. A key challenge here is the geographic heterogeneity and acquisition variability. Here, we use MDCP to protect subpopulation shift between data-rich locations to data-poor regions due to different materials, urban morphologies, and imaging conditions. 

We leverage the 2016 time slice in the Functional Map of the World (FMoW) dataset [Christie et al., 2018] with over one million images from 249 countries/regions, and the label is one of 62 functional classes. We focus on uniform coverage across regions in Africa, the Americas, Asia, Europe, Oceania and _Other_ . We treat each geographic region as a source. Let _X_ denote the image input and _Y_ the functional class label. In this context, uniform coverage ensures reliability under arbitrary changes in the composition of regions. 

The data contains 140,459 samples in total. We allocate 37.5% as the model training fold _|D_ pre-train _|_ = 52 _,_ 531. The training distribution is highly imbalanced, with 30.27% from Europe and 38.72% from the Americas, yet only 2.23% from Oceania and 0.05% from Other. Using the `DenseNet-121` backbone [Huang et al., 2018] initialized with `ImageNet` weights [Deng et al., 2009], we compute the penultimate representation _e_ ( _x_ ) and fit a pooled probabilistic classifier _p_ ˆpool( _y | x_ ) together with region-specific classifiers _{p_ ˆ _k_ ( _y | x_ ) _}[K] k_ =1 on top of _e_ ( _x_ ). The models are trained on _D_ pre-train and these probability estimates are used by both the TPS baselines and MDCP; further modeling details are deferred to Appendix C.4.1. 

Next, we perform _N_ = 100 random partitions of the remaining data into auxiliary train (12.5%), calibration (37.5%), and test (50%) splits. Before fitting _λ_ ( _x_ ), we apply PCA to the feature vectors _e_ ( _x_ ) on 

16 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0017-00.png)


**----- Start of picture text -----**<br>
Baseline agg Africa Americas Asia Europe Oceania Other MDCP<br>0.98 0.97<br>12.5<br>0.90<br>10.0<br>0.90<br>7.5<br>0.80 5.0<br>0.80 0.61 2.5<br>Method Method Method<br>Baseline aggAfricaAmericas AsiaEuropeOceaniaOtherMDCP Baseline aggAfricaAmericas AsiaEuropeOceaniaOtherMDCP Baseline aggAfricaAmericas AsiaEuropeOceaniaOtherMDCP<br>Avg set size<br>Overall coverage<br>Worst-case coverage<br>**----- End of picture text -----**<br>


Figure 8: Performance of MDCP, `Baseline-agg` , and `Baseline-src-` _k_ with each source region on the FMoW dataset across six sources: Africa, Americas, Asia, Europe, Oceania, and _Other_ . The bars show the average results over _N_ = 100 runs, and the dots show the result in each run. Left: overall coverage evaluated over the entire test set. Middle: worst-coverage over all test sources. Right: average set size over the entire test set. 

the auxiliary training split and retain the first 16 components. We parameterize _λ_ ( _x_ ) _∈_ R _[K]_ +[by][a][feedfor-] ward neural network containing two hidden layers of width 4 with ReLU activations and a _K_ -dimensional output. We fit _λ_ ( _x_ ) by optimizing the empirical dual objective in Section 4.2 on the auxiliary training split, then calibrate MDCP on the calibration split and evaluate on the test split. Baselines use the same fitted conditional models with TPS scores, calibrated on the 37.5% calibration split and evaluated on the 50% test split. The nominal coverage is set at 1 _− α_ = 0 _._ 9, and the results are reported in Figure 8. 

Due to nontrivial heterogeneity across regions, we observe unequal coverage for single-source baselines. Standard conformal prediction sets calibrated using data from the _Other_ region achieve overall coverage above 0 _._ 9, yet still suffer from undercoverage in the worst-case. Notably, the baseline calibrated on data-rich regions (e.g., Europe and the Americas) exhibits worse worst-case coverage (despite the lower variability in coverage across runs). A possible explanation is that the abundant data allow the model to be well trained, producing prediction sets that are tightly tuned to those specific source distributions but perform poorly in others. In contrast, for data-scarce regions such as _Other_ , the model performs poorly even in the original source, and thus must output wide sets. Consequently, models calibrated on scarce-data regions can yield better worst-case coverage than those calibrated on rich-data regions, albeit at the cost of larger prediction sets. In comparison, MDCP remains valid across all sources, with near-tight worst-case coverage. Moreover, `Baseline-agg` admits any signal deemed useful by any source and is conservative. MDCP mitigates this issue by joint training across sources. Indeed, its set size is even smaller than single-source prediction sets, showing the significant benefit of efficiency optimization. 

In Appendix D.1.2, we further examine the penalty-tuning approach similar to the simulations. In this task, we again observe negligible difference from standard MDCP, showing the stability of our procedure. 

## **6.2 Poverty prediction under urban-rural shift** 

Household surveys for mapping economic well-being are infrequent or missing especially in regions where nationally representative surveys are limited by local resources [Blumenstock et al., 2015]. In these scenarios, satellite imagery offers a scalable proxy: a practical strategy is to learn from countries with the desired economic label then transfer to countries with images only [Abelson et al., 2014]. In this part, we visit the subset of a modified release of the Yeh et al. [2020] poverty-mapping dataset from 2014 to 2016 to show the application of MDCP to provide reliable uncertainty quantification across rural and urban areas. In this data, the features are the satellite image, and the label is a continuously-valued wealth index. Figure 9a visualizes the label density in the urban and rural areas which exhibits strong heterogeneity. 

17 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0018-00.png)


**----- Start of picture text -----**<br>
Urban KDE Rural KDE Overall Baseline agg Rural Urban MDCP<br>0.98 0.98<br>1.00 0.90 0.90 2.00<br>0.75 1.75<br>0.50 1.50<br>0.25 1.25<br>0.65<br>0.65 0.56 1.00<br>0.00<br>1 0 1 2 3<br>Wealth index (target)<br>Method Method Method<br>(a) Per-source and pooled distribu- (b) Performance of MDCP and baselines averaged over N = 100 splits. Left:<br>tion of the label. The curves come coverage evaluated over the entire test set. Middle: worst-case coverage for two<br>from a kernel density estimation. sources. Right: prediction set width over the entire test set.<br>Baseline agg Rural Urban MDCP Baseline agg Rural Urban MDCP Baseline agg Rural Urban MDCP<br>Density<br>Overall coverage Avg interval width<br>Worst-case coverage<br>**----- End of picture text -----**<br>


Figure 9: Results of MDCP and baselines in the PovertyMap dataset. 

The dataset contains _n_ = 7 _,_ 535 samples, with 2,664 from urban areas and 4,871 from rural, each treated as a source. We reserve 37.5% of the data for training and fit a shared 8-channel `ResNet-18` backbone [He et al., 2015] with random initialization. On top of the shared `ResNet-18` representation _e_ ( _x_ ), we fit both pooled and source-specific working models that output (ˆ _µ_ ( _x_ ) _,_ ˆ _σ_ ( _x_ )) as in Section 5.3 and hence a conditional density _f_[ˆ] ( _y | x_ ) = _N_ ( _y_ ; ˆ _µ_ ( _x_ ) _,_ ˆ _σ_[2] ( _x_ )). The training details of these density models are in Appendix C.4.2. This yields two source models _f_[ˆ][Rural] ( _y | x_ ) and _f_[ˆ][Urban] ( _y | x_ ), as well as a pooled model _p_ ˆpool( _y | x_ ). Next, we perform _N_ = 100 random splits of the remaining data into auxiliary train (12.5%), calibration (37.5%), and test (50%) folds. As in FMoW, before fitting _λ_ ( _x_ ) we apply PCA to _e_ ( _x_ ) and keep the first 16 components. We use the same neural-network parameterization for _λ_ ( _x_ ) as in FMoW, fit it on the auxiliary training fold, calibrate the MDCP set on the calibration fold, and evaluate on the test fold. 

As shown in Figure 9b, single-source models calibrated with single-source data fail to achieve valid coverage on the other domain. We see from Figure 9a that the rural distribution is more skewed; under strong heterogeneity, despite the larger sample size from the rural source, single-source calibration still produces short intervals and low coverage. On the other hand, `Baseline-agg` , which naively combines single-source prediction sets, is overly conservative. MDCP maintains tight worst-case coverage with significant efficiency gains, striking a good balance in coverage allocation across sources. 

Finally, we find that the penalty-tuning extension of MDCP still offers no clear advantage over MDCP. See Appendix D.1.2 for further discussion. 

## **6.3 Medical services utilization across sensitive groups** 

Our last application revisits the Medical Expenditure Panel Survey (MEPS) dataset used in Romano et al. [2019a], including Panels 19-21 [MEPS19, MEPS20, MEPS21], to address equalized coverage even without observing the sensitive group label. The dataset contains detailed individual-level information on demographics and health care utilization. The features include age, marital status, race, poverty level, and health status and insurance related covariates. The label is a continuously-valued medical service utilization score. 

We follow the same pre-processing steps as Romano et al. [2019a] with one-hot encoding of categorical variables. The feature dimension for _X_ is 139, consistent across panels. We apply a log transformation to the label due to its skewedness; without this step, the estimated variance would be excessively inflated which drastically degrades the efficiency of single-source baselines. As reported by the Romano et al. [2019b], predictive distributions vary across the sensitive attribute _race_ : a neural-network predictor tends to predict higher utilization for non-White than for White individuals. Motivated by this finding, we treat _race_ as the source label, assigning _k_ = 0 to non-White and _k_ = 1 to White, with sample sizes _n_ 0 = 9640 and _n_ 1 = 6016. 

We split the data into training (60%), calibration (20%), and test (20%) folds. For both MDCP and the baselines, we follow the same modeling procedure as in Section 5.3: conditional densities are modeled as 

18 

_PY_[(] _[k] |X_[)] = _x[∼N]_[(] _[µ][k]_[(] _[x]_[)] _[, σ][k]_[(] _[x]_[)][2][),][with] _[µ]_[ˆ] _[k]_[(] _[x]_[) and] _[σ]_[ˆ] _[k]_[(] _[x]_[) estimated via gradient-boosting decision trees trained on] the source-specific training fold; in addition, we fit a pooled model on the union of the training data using the same approach as in Section 5.3. MDCP further fits _λ_ ( _x_ ) using the same training data and calibrates prediction sets on the entire calibration fold. In contrast, the single-source baselines ( `Non-White` only and `White` only) calibrate solely on their respective source-specific calibration fold. The `Baseline-agg` combines the two single-source calibrated sets. Finally, the three methods are all evaluated on the same test fold. The above protocol is applied independently to each panel, with results reported separately. 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0019-01.png)


**----- Start of picture text -----**<br>
Baseline agg Non-white White MDCP<br>Overall coverage Worst-case coverage Avg interval width<br>0.97 0.97 4.0<br>3.5<br>0.90 0.90<br>3.0<br>0.86<br>2.5<br>0.82<br>0.80 0.80 2.0<br>4.0<br>0.97 0.97<br>3.5<br>0.90 0.90 3.0<br>0.87<br>0.83 2.5<br>0.80 0.80 2.0<br>0.98 0.97<br>4<br>0.90 0.90<br>3<br>0.86<br>0.82<br>0.80 0.80 2<br>Method<br>Baseline aggNon-white White MDCP Baseline aggNon-white White MDCP Baseline aggNon-white White MDCP<br>Baseline aggNon-white White MDCP Baseline aggNon-white White MDCP Baseline aggNon-white White MDCP<br>Baseline aggNon-white White MDCP Baseline aggNon-white White MDCP Baseline aggNon-white White MDCP<br>Panel 19 Panel 19 Panel 19<br>Panel 20 Panel 20 Panel 20<br>Panel 21 Panel 21 Panel 21<br>**----- End of picture text -----**<br>


Figure 10: Results of MDCP and baselines in the MEPS dataset evaluation across three panels and two sensitive groups (sources), white and non-white. The bars show results averaged over _N_ = 100 runs, and the dots show single-run results. Each row corresponds to one panel, and each column corresponds to one metric: average coverage over all test data, worst-case coverage across two sources, and average length of prediction set over all test data. 

Figure 10 reports the performance of the competing methods. The single-source baseline trained and calibrated exclusively on the non-white group exhibits systematic undercoverage (both on average and worstcase) across panels. This is because the white group is more right-skewed and the single-source baseline from the non-white group fails to cover its heavy tail. On the other hand, single-source sets trained and calibrated exclusively on the White group approximately attains worst-case coverage, yet the width of the prediction sets is exceedingly high. We conjecture that this may be due to the unreliable estimation of the working models with the skewed data, since the models are not trained to optimize efficiency in the downstream conformal prediction set. Similarly, `Baseline-agg` is overly conservative and has wide prediction sets. Finally, MDCP achieves tight worst-case coverage, showing the role of approximate complementary slackness. Efficiency optimization lets MDCP achieve even shorter sets than the single-source baselines. 

Finally, in Appendix D.1.2, we find that in this dataset, the penalty-tuning extension of MDCP again yields similar performance as MDCP, showing the robustness of the current implementation. 

19 

## **7 Discussion** 

In this work, we propose the MDCP framework for constructing one single prediction set that offers valid coverage over multiple heterogeneous distributions. The key component is the max-p aggregation, which takes the union of single-source conformal prediction sets and therefore offers the desired coverage. While this scheme simply constructs a prediction set that is larger than needed for valid coverage in any single source, we show that, once coupled with a suitable conformity score, the MDCP set under max-p aggregation is both optimal and tight. We then propose concrete algorithms that learn the optimal conformity score through an empirical dual objective to approach optimality while maintaining finite-sample uniform validity. Our algorithms only need standard single-source classifiers or conditional mean/variance regression models, and connect to commonly-used conformity scores. Extensive simulations and real-world applications demonstrate the validity, efficiency, and tightness of MDCP, and its utility in protecting against sub-population shift, maintaining robustness across heterogeneous regions, and ensuring equalized coverage across sensitive groups. 

Several follow-up questions remain open. The first is a general formulation of multi-distribution extension with any base conformity score. Inspired by a population-level analysis, our conformity score is constructed by finding high-density regions across populations. In classification problems, it coincides with the natural idea of admitting labels into the prediction set based on predicted probability. In regression, however, it might not always be desirable to threshold a density function since it may lead to non-interval sets, and conformity scores that lead to intervals by construction, such as those based on quantile functions [Romano et al., 2019b], are proven effective. Therefore, it may be meaningful to develop a general framework that learns a multi-distribution combination of pre-specified single-source conformity scores by directly optimizing efficiency-based objectives [Stutz et al., 2021, Huang et al., 2023, Xie et al., 2024]. 

Second, instead of max-p aggregation, another natural idea to form a uniformly valid prediction set is to predict which group/population the test point is from, and adjust the coverage based on this prediction. However, it remains unclear how to manage the membership estimation error and its finite-sample guarantee. 

Finally, when it comes to subpopulation shift, we still require the knowledge of the subpopulation the labeled data are from. In practice, the distribution may change from one unknown mixture of subpopulations to another. How to develop robust prediction sets under such shifts may be a valuable problem. 

## **Acknowledgements** 

The authors thank the Wharton Research Computing team for the computational resources provided and the great support from the staff members. 

## **References** 

- Brian Abelson, Kush R. Varshney, and Joy Sun. Targeting direct cash transfers to the extremely poor. In _Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , KDD ’14, page 1563–1572, New York, NY, USA, 2014. Association for Computing Machinery. ISBN 9781450329569. doi: 10.1145/2623330.2623335. URL `https://doi.org/10.1145/2623330.2623335` . 

- Jiahao Ai and Zhimei Ren. Not all distributional shifts are equal: Fine-grained robust conformal inference. _arXiv preprint arXiv:2402.13042_ , 2024. 

- Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer Wortman Vaughan. A theory of learning from different domains. _Machine learning_ , 79(1):151–175, 2010. 

- Aharon Ben-Tal, Laurent El Ghaoui, and Arkadi Nemirovski. _Robust Optimization_ . Princeton University Press, 2009. 

20 

- Joshua Blumenstock, Gabriel Cadamuro, and Robert On. Predicting poverty and wealth from mobile phone metadata. _Science_ , 350(6264):1073–1076, 2015. doi: 10.1126/science.aac4420. URL `https: //www.science.org/doi/abs/10.1126/science.aac4420` . 

- Maxime Cauchois, Suyash Gupta, Alnur Ali, and John C Duchi. Robust validation: Confident predictions even when distributions shift. _Journal of the American Statistical Association_ , 119(548):3033–3044, 2024. 

- Gordon Christie, Neil Fendley, James Wilson, and Ryan Mukherjee. Functional map of the world, 2018. URL `https://arxiv.org/abs/1711.07846` . 

- Koby Crammer, Michael Kearns, and Jennifer Wortman. Learning from multiple sources. _Journal of Machine Learning Research_ , 9(57):1757–1774, 2008. URL `http://jmlr.org/papers/v9/crammer08a.html` . 

- Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hierarchical image database. In _2009 IEEE Conference on Computer Vision and Pattern Recognition_ , pages 248–255, 2009. doi: 10.1109/CVPR.2009.5206848. 

- Rina Foygel Barber, Emmanuel J Candes, Aaditya Ramdas, and Ryan J Tibshirani. The limits of distribution-free conditional predictive inference. _Information and Inference: A Journal of the IMA_ , 10(2):455–482, 2021. 

- Yarin Gal et al. Uncertainty in deep learning. 2016. 

- Stuart Geman and Chii-Ruey Hwang. Nonparametric maximum likelihood estimation by the method of sieves. _The annals of Statistics_ , pages 401–414, 1982. 

- Asaf Gendler, Tsui-Wei Weng, Luca Daniel, and Yaniv Romano. Adversarially robust conformal prediction. In _International Conference on Learning Representations_ , 2021. 

- Subhankar Ghosh, Yuanjie Shi, Taha Belkhouja, Yan Yan, Jana Doppa, and Brian Jones. Probabilistically robust conformal prediction. In _Uncertainty in Artificial Intelligence_ , pages 681–690. PMLR, 2023. 

- Isaac Gibbs, John J Cherian, and Emmanuel J Cand`es. Conformal prediction with conditional guarantees. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , page qkaf008, 2025. 

- Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q Weinberger. On calibration of modern neural networks. In _International conference on machine learning_ , pages 1321–1330. PMLR, 2017. 

- Maya Gupta, Andrew Cotter, Mahdi Milani Fard, and Serena Wang. Proxy fairness. _arXiv preprint arXiv:1806.11212_ , 2018. 

- Tatsunori Hashimoto, Megha Srivastava, Hongseok Namkoong, and Percy Liang. Fairness without demographics in repeated loss minimization. In _International Conference on Machine Learning_ , pages 1929– 1938. PMLR, 2018. 

- Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition, 2015. URL `https://arxiv.org/abs/1512.03385` . 

- Gao Huang, Zhuang Liu, Laurens van der Maaten, and Kilian Q. Weinberger. Densely connected convolutional networks, 2018. URL `https://arxiv.org/abs/1608.06993` . 

- Kexin Huang, Ying Jin, Emmanuel Candes, and Jure Leskovec. Uncertainty quantification over graph with conformalized graph neural networks. _Advances in Neural Information Processing Systems_ , 36:26699– 26721, 2023. 

21 

- Pierre Humbert, Batiste Le Bars, Aur´elien Bellet, and Sylvain Arlot. One-shot federated conformal prediction. In _International Conference on Machine Learning_ , pages 14153–14177. PMLR, 2023. 

- Xiaoqian Jiang, Melanie Osl, Jihoon Kim, and Lucila Ohno-Machado. Calibrating predictive model estimates to support personalized medicine. _Journal of the American Medical Informatics Association_ , 19(2):263– 274, 2012. 

- Ying Jin, Zhimei Ren, and Zhengyuan Zhou. Sensitivity analysis under the _f_ -sensitivity models: a distributional robustness perspective. _arXiv preprint arXiv:2203.04373_ , 2022. 

- Ying Jin, Zhimei Ren, and Emmanuel J Cand`es. Sensitivity analysis of individual treatment effects: A robust conformal inference approach. _Proceedings of the National Academy of Sciences_ , 120(6):e2214889120, 2023. 

- Christopher Jung, Georgy Noarov, Ramya Ramalingam, and Aaron Roth. Batch multivalid conformal prediction. _arXiv preprint arXiv:2209.15145_ , 2022. 

- Benjamin Kompa, Jasper Snoek, and Andrew L Beam. Second opinion needed: communicating uncertainty in medical machine learning. _NPJ Digital Medicine_ , 4(1):4, 2021. 

- Volodymyr Kuleshov, Nathan Fenner, and Stefano Ermon. Accurate uncertainties for deep learning using calibrated regression. In _International conference on machine learning_ , pages 2796–2804. PMLR, 2018. 

- Preethi Lahoti, Alex Beutel, Jilin Chen, Kang Lee, Flavien Prost, Nithum Thain, Xuezhi Wang, and Ed Chi. Fairness without demographics through adversarially reweighted learning. _Advances in neural information processing systems_ , 33:728–740, 2020. 

- Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell. Simple and scalable predictive uncertainty estimation using deep ensembles. _Advances in neural information processing systems_ , 30, 2017. 

- Jing Lei, Max G’Sell, Alessandro Rinaldo, Ryan J Tibshirani, and Larry Wasserman. Distribution-free predictive inference for regression. _Journal of the American Statistical Association_ , 113(523):1094–1111, 2018. 

- Yi Liu, Alexander W Levis, Sharon-Lise Normand, and Larry Han. Multi-source conformal inference under distribution shift. _Proceedings of machine learning research_ , 235:31344, 2024. 

- Charles Lu, Yaodong Yu, Sai Praneeth Karimireddy, Michael Jordan, and Ramesh Raskar. Federated conformal predictors for distributed uncertainty quantification. In _International Conference on Machine Learning_ , pages 22942–22964. PMLR, 2023. 

- David G Luenberger. _Optimization by vector space methods_ . John Wiley & Sons, 1997. 

- David Madras, Elliot Creager, Toniann Pitassi, and Richard Zemel. Learning adversarially fair and transferable representations. In _International Conference on Machine Learning_ , pages 3384–3393. PMLR, 2018. 

- Yishay Mansour, Mehryar Mohri, and Afshin Rostamizadeh. Domain adaptation with multiple sources. In D. Koller, D. Schuurmans, Y. Bengio, and L. Bottou, editors, _Advances in Neural Information Processing Systems_ , volume 21. Curran Associates, Inc., 2008. URL `https://proceedings.neurips.cc/paper_ files/paper/2008/file/0e65972dce68dad4d52d063967f0a705-Paper.pdf` . 

- Natalia Martinez, Martin Bertran, and Guillermo Sapiro. Minimax pareto fairness: A multi objective perspective. In _International conference on machine learning_ , pages 6755–6764. PMLR, 2020. 

- Natalia L Martinez, Martin A Bertran, Afroditi Papadaki, Miguel Rodrigues, and Guillermo Sapiro. Blind pareto fairness and subgroup robustness. In _International Conference on Machine Learning_ , pages 7492– 7501. PMLR, 2021. 

22 

- MEPS19. Medical expenditure panel survey, panel 19. `https://meps.ahrq.gov/mepsweb/data_stats/ download_data_files_detail.jsp?cboPufNumber=HC-181` . Accessed: Oct, 2025. 

- MEPS20. Medical expenditure panel survey, panel 20. `https://meps.ahrq.gov/mepsweb/data_stats/ download_data_files_detail.jsp?cboPufNumber=HC-181` . Accessed: Oct, 2025. 

- MEPS21. Medical expenditure panel survey, panel 21. `https://meps.ahrq.gov/mepsweb/data_stats/ download_data_files_detail.jsp?cboPufNumber=HC-192` . Accessed: Oct, 2025. 

- Mehryar Mohri, Gary Sivek, and Ananda Theertha Suresh. Agnostic federated learning. In _International conference on machine learning_ , pages 4615–4625. PMLR, 2019. 

- Vincent Plassier, Nikita Kotelevskii, Aleksandr Rubashevskii, Fedor Noskov, Maksim Velikanov, Alexander Fishkov, Samuel Horvath, Martin Takac, Eric Moulines, and Maxim Panov. Efficient conformal prediction under data heterogeneity. In _International Conference on Artificial Intelligence and Statistics_ , pages 4879–4887. PMLR, 2024. 

- John Platt et al. Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods. _Advances in large margin classifiers_ , 10(3):61–74, 1999. 

- Hamed Rahimian and Sanjay Mehrotra. Distributionally robust optimization: A review. 2019. Optimization Online. 

- Yaniv Romano, Rina Foygel Barber, Chiara Sabatti, and Emmanuel J. Cand`es. With malice towards none: Assessing uncertainty via equalized coverage, 2019a. URL `https://arxiv.org/abs/1908.05428` . 

- Yaniv Romano, Evan Patterson, and Emmanuel Candes. Conformalized quantile regression. _Advances in Neural Information Processing Systems_ , 32:3543–3553, 2019b. 

- Yaniv Romano, Matteo Sesia, and Emmanuel J Cand`es. Classification with valid and adaptive coverage. _arXiv preprint arXiv:2006.02544_ , 2020. 

- Mauricio Sadinle, Jing Lei, and Larry Wasserman. Least ambiguous set-valued classifiers with bounded error levels. _Journal of the American Statistical Association_ , 114(525):223–234, 2019. 

- Shiori Sagawa, Pang Wei Koh, Tatsunori B Hashimoto, and Percy Liang. Distributionally robust neural networks for group shifts: On the importance of regularization for worst-case generalization. _arXiv preprint arXiv:1911.08731_ , 2019. 

- Shibani Santurkar, Dimitris Tsipras, and Aleksander Madry. Breeds: Benchmarks for subpopulation shift. _arXiv preprint arXiv:2008.04859_ , 2020. 

- Ola Spjuth, Robin Carri´on Br¨annstr¨om, Lars Carlsson, and Niharika Gauraha. Combining prediction intervals on multi-source non-disclosed regression datasets. In _Conformal and Probabilistic Prediction and Applications_ , pages 53–65. PMLR, 2019. 

- David Stutz, Ali Taylan Cemgil, Arnaud Doucet, et al. Learning optimal conformal classifiers. _arXiv preprint arXiv:2110.09192_ , 2021. 

- Adarsh Subbaswamy, Roy Adams, and Suchi Saria. Evaluating model robustness and stability to dataset shift. In _International conference on artificial intelligence and statistics_ , pages 2611–2619. PMLR, 2021. 

- Vladimir Vovk, Alexander Gammerman, and Glenn Shafer. _Algorithmic learning in a random world_ . Springer Science & Business Media, 2005. 

23 

- Ran Xie, Rina Barber, and Emmanuel Candes. Boosted conformal prediction intervals. _Advances in Neural Information Processing Systems_ , 37:71868–71899, 2024. 

- Steve Yadlowsky, Hongseok Namkoong, Sanjay Basu, John Duchi, and Lu Tian. Bounds on the conditional and average treatment effect with unobserved confounding factors. _Annals of statistics_ , 50(5):2587, 2022. 

- Yuzhe Yang, Haoran Zhang, Dina Katabi, and Marzyeh Ghassemi. Change is hard: A closer look at subpopulation shift. _arXiv preprint arXiv:2302.12254_ , 2023. 

- Christopher Yeh, Anthony Perez, Anne Driscoll, George Azzari, Zhongyi Tang, David Lobell, Stefano Ermon, and Marshall Burke. Using publicly available satellite imagery and deep learning to understand economic well-being in africa. _Nature Communications_ , 2020. 

- Mingzhang Yin, Claudia Shi, Yixin Wang, and David M Blei. Conformal sensitivity analysis for individual treatment effects. _Journal of the American Statistical Association_ , 119(545):122–135, 2024. 

24 

## **A Deferred discussion** 

## **A.1 Optimality under marginal coverage** 

In this part, we study the optimal prediction set under marginal validity. We consider the following optimization problem: 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0025-03.png)


We integrate _|C_ ( _x_ ) _|_ over _ν_ ( _·_ ) to ensure a scalar objective. By definition, (14) seeks the measurable prediction set with the smallest size that achieves uniform coverage. Rigorously speaking, by “measurable”, we mean 1 _{y ∈ C_ ( _x_ ) _}_ is a measurable function on _X × Y_ , or _C_ ( _x_ ) is a measurable subset of _Y_ for _ν_ -a.s. all _x ∈X_ . 

Solving (14) amounts to a change-of-variable via the indicator function _I_ ( _x, y_ ) := 1 _{y ∈ C_ ( _x_ ) _}_ . For a clear presentation, we relax the range of _I_ ( _x, y_ ) to [0 _,_ 1], so that _I_ ( _x, y_ ) can be viewed as the probability of _y ∈ C_ ( _x_ ) for a randomized prediction set. The optimization problem becomes 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0025-06.png)


Theorem 10 characterizes the globally optimal prediction set with smallest size subject to uniform validity, whose proof is in Appendix B.2. Here, the coverage probability should be understood as that of a randomized prediction set with probability _I_ ( _x, y_ ) _∈_ [0 _,_ 1]. 

**Theorem 10** (Marginal optimality) **.** _Consider the marginal size-minimization problem_ (15) _. There exists a vector of nonnegative constants λ[∗]_ = ( _λ[∗]_ 1 _[, . . . , λ][∗] K_[)] _[ ∈]_[R] _[K]_ + _[such][that][with][h][λ]_[(] _[x, y]_[) =][ �] _[K] k_ =1 _[λ][k][ r][k]_[(] _[x]_[)] _[ f][k]_[(] _[y][ |][ x]_[)] _[,] one optimal solution C[∗] to_ (15) _takes the following form:_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0025-09.png)


_In particular, λ[∗]_ = ( _λ[∗]_ 1 _[, . . . , λ][∗] K_[)] _[ ∈]_[R] _[K]_ + _[is][the][optimal][solution][to][the][dual][problem]_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0025-11.png)


_where_ ( _hλ_ ( _x, y_ ) _−_ 1)+ = max _{hλ_ ( _x, y_ ) _−_ 1 _,_ 0 _}. Moreover, the complementary slackness holds:_ 

_(i) If λ[∗] k[>]_[ 0] _[then][the][k][-th][constraint][is][active,][with][P]_[ (] _[k]_[)][(] _[Y][∈][C][∗]_[(] _[X]_[)) = 1] _[ −][α][;] (ii) If λ[∗] k_[= 0] _[then][the][k][-th][constraint][is][(weakly)][inactive,][with][P]_[ (] _[k]_[)][(] _[Y][∈][C][∗]_[(] _[X]_[))] _[ ≥]_[1] _[ −][α][;] (iii) There exists at least one k[∗] ∈_ [ _K_ ] _such that λ[∗] k[∗][>]_[ 0] _[and][P]_[ (] _[k][∗]_[)][(] _[Y][∈][C][∗]_[(] _[X]_[)) = 1] _[ −][α][.] If additionally µ_ ( _{y_ : _hλ_ ( _x, y_ ) = 1 _}_ ) = 0 _for ν-a.e. x, then C[∗] is unique up to_ ( _ν ⊗ µ_ ) _-null sets._ 

Theorem 10 reveals the central role of a single score function _hλ∗_ ( _x, y_ ): the optimal solution _C[∗]_ ( _x_ ) is determined by thresholding this score value. Whether to include the boundary set _{y_ : _hλ∗_ ( _x, y_ ) = 1 _}_ in the prediction set is often subject to users’ preference. If _hλ∗_ ( _x, y_ ) does not have point mass over _ν ⊗ µ_ , the inclusion of the boundary set does not affect the average size or coverage probability. Otherwise, one need to randomize the inclusion to achieve exact 1 _− α_ coverage, or include it with slight over-coverage. 

25 

The complementary slackness in statement (iii) of Theorem 10 is worth noting: there always exists one source distribution under which _C[∗]_ ( _X_ ) achieves exact 1 _− α_ coverage. (In the presence of point mass, such coverage should be understood as that of a randomized prediction set with P( _y ∈ C[∗]_ ( _x_ )) = _I[∗]_ ( _x, y_ ) _∈_ [0 _,_ 1]). 

Finally, we remark that since the objective of (14) integrates over the base measure _ν_ ( _·_ ), the solution does not necessarily aim for the smallest average size for _the_ test distribution in a specific problem. Arguably, it would be more natural to study the conditional problem in the main paper for a fixed _x ∈X_ subject to conditional uniform coverage, in which case the objective is inherently a scalar. 

## **B Technical proofs** 

## **B.1 Proof of Theorem 1** 

_Proof of Theorem 1._ Since sup _j∈_ [ _K_ ] _p_[(] _[j]_[)] ( _y_ ) _≤ α_ implies _p_[(] _[k]_[)] ( _y_ ) _≤ α_ , we have 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0026-05.png)


under _P_[(] _[k]_[)] and _D_ . The coverage statement follows by complement. The equality _C_[ˆ] =[�] _k[C]_[ˆ][(] _[k]_[)][is][immediate] from the definition of the supremum and the threshold rule: 

• If _y ∈_ � _y ∈Y_ : sup _j∈_ [ _K_ ] _p_[(] _[j]_[)] ( _y_ ) _> α_ �, then _y ∈_[�] _[K] j_ =1 � _y ∈Y_ : _p_[(] _[j]_[)] ( _y_ ) _> α_ �, since _∃j_ s.t. _p_[(] _[j]_[)] ( _y_ ) _> α_ . • If _y ∈_[�] _[K] j_ =1 � _y ∈Y_ : _p_[(] _[j]_[)] ( _y_ ) _> α_ �, then _∃k_ s.t. _p_[(] _[j]_[)] ( _y_ ) _> α_ , then _y ∈_ � _y ∈Y_ : sup _j∈_ [ _K_ ] _p_[(] _[j]_[)] ( _y_ ) _> α_ �. This concludes the proof of Theorem 1. 

## **B.2 Proof of Theorem 10** 

_Proof of Theorem 10._ Write the joint density function _wk_ ( _x, y_ ) := _rk_ ( _x_ ) _fk_ ( _y | x_ ). The primal problem can be expressed as 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0026-10.png)


Relax _I ∈{_ 0 _,_ 1 _}_ to _I ∈_ [0 _,_ 1]. Since functions _I ∈_ [0 _,_ 1] form a vector space [Luenberger, 1997], we consider the Lagrangian with constant multipliers _λk ≥_ 0: 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0026-12.png)


Let _hλ_ ( _x, y_ ) :=[�] _[K] k_ =1 _[λ][k][w][k]_[(] _[x, y]_[).][Then][we][have] 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0026-14.png)


For a fixed value of _λ_ , minimizing over _I_ ( _x, y_ ) _∈_ [0 _,_ 1] pointwise in ( _x, y_ ) yields the minimizer 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0026-16.png)


which yields the threshold form 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0026-18.png)


26 

After minimizing over _I_ , the dual objective is 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0027-01.png)


this gives the marginal dual objective (16) mentioned in the theorem, and the dual problem is to maximize Φ( _λ_ ) over _λ ∈_ R _[K]_ +[.] 

Note that Slater’s condition holds (e.g., _C_ ( _x_ ) _≡Y_ strictly satisfies each constraint for _α ∈_ (0 _,_ 1)), so strong duality applies and a dual maximizer _λ[∗]_ exists [Luenberger, 1997]. Let _λ[∗]_ be a dual maximizer and define _h[∗]_ ( _x, y_ ) =[�] _k[λ] k[∗][r][k]_[(] _[x]_[)] _[f][k]_[(] _[y][|][x]_[)][and][the][tie][set] _[T]_[(] _[x]_[)][=] _[{][y]_[:] _[h][∗]_[(] _[x, y]_[)][=][1] _[}][.]_[There][exists][a][primal] optimizer 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0027-04.png)


with _Z[∗]_ : _X × Y →_ [0 _,_ 1] measurable, chosen so that 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0027-06.png)


where the covariate distribution _PX_[(] _[k]_[)] admits a density _rk_ ( _x_ ) with respect to _ν_ . Equivalently, writing 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0027-08.png)


_Z[∗]_ must satisfy _ak_ + _bk_ = 1 _− α_ , for all _k_ with _λk >_ 0 and _ak_ + _bk ≥_ 1 _− α_ for all _k_ with _λk >_ 0. When multiple constraints with their Lagrangian multiplier _λk >_ 0, achieving all equalities generally requires a non-constant _Z[∗]_ (for example, using randomized inclusion on the boundary). In cases where the boundary has measure zero ( _ν ⊗ µ_ )( _T_ ) = 0, one can implement _Z[∗]_ deterministically as an indicator of a measurable subset of the tie set; in cases where the boundary has non-zero measure ( _ν ⊗ µ_ )( _T_ ) _>_ 0, this corresponds to randomized tie-breaking. 

Accordingly, complementary slackness yields, with _gk_ ( _C_ ) := �� _X×Y[Iw][k][ dµ dν][ −]_[(1] _[−][α]_[)] _[ ≥]_[0,][it must hold] that 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0027-11.png)


Thus: (i) if _λ[∗] k[>]_[ 0][then] _[P]_[ (] _[k]_[)][(] _[Y][∈][C][∗]_[(] _[X]_[)) = 1] _[ −][α]_[,][and][(ii)][if] _[λ][∗] k_[= 0][then] _[P]_[ (] _[k]_[)][(] _[Y][∈][C][∗]_[(] _[X]_[))] _[ ≥]_[1] _[ −][α]_[.] 

We show next that at least one coordinate of _λ[∗]_ is strictly positive, i.e., statement (iii). Let _ρ_ := _ν ⊗ µ_ and recall that for each _k_ , 

_wk_ ( _x, y_ ) := _rk_ ( _x_ ) _fk_ ( _y | x_ ) _≥_ 0 

is integrable with respect to _ρ_ and satisfies �� _wk dρ_ = 1 since it is the joint density of ( _X, Y_ ) under _P_[(] _[k]_[)] with respect to _ρ_ . 

Notice that for the dual objective (16) with _hλ_ ( _x, y_ ) =[�] _k[λ][k][w][k]_[(] _[x, y]_[),][we][have][Φ(0)][=][0.] Fix any _j ∈{_ 1 _, . . . , K}_ and consider _λ_ = _tej_ with _t >_ 0, where _ej_ is the _j_ -th unit vector. Then _hλ_ = _twj_ and 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0027-17.png)


For any _a ≥_ 0 and _t >_ 0, ( _ta −_ 1)+ _≤ ta_ 1 _{a ≥_ 1 _/t}_ . Applying this pointwise with _a_ = _wj_ ( _x, y_ ) and integrating, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0027-19.png)


27 

Define _Tj_ ( _t_ ) := �� _wj_ 1 _{wj ≥_ 1 _/t} dρ_ . Since _wj_ is integrable, _Tj_ ( _t_ ) _→_ 0 as _t ↓_ 0 (the tail of an integrable function vanishes). Therefore, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0028-01.png)


and hence 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0028-03.png)


Because _Tj_ ( _t_ ) _→_ 0 and 1 _− α >_ 0, there exists _t_ 0 _>_ 0 such that for all _t ∈_ (0 _, t_ 0), 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0028-05.png)


Thus sup _λ≥_ 0 Φ( _λ_ ) _>_ 0, so a dual maximizer cannot be _λ[∗]_ = 0. Consequently,[�] _k[λ] k[∗][>]_[ 0][and][there][exists][at] least one _k[∗]_ with _λ[∗] k[∗][>]_[ 0.][By][complementary][slackness][(][18][),] 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0028-07.png)


This proves item (iii). 

Finally, if _µ_ ( _{y_ : _hλ∗_ ( _x, y_ ) = 1 _}_ ) = 0 for _ν_ -almost every _x_ , then the boundary set is _µ_ -null almost surely, making the optimizer unique up to ( _ν ⊗ µ_ )-null sets. 

## **B.3 Proof of Theorem 2** 

_Proof of Theorem 2._ Fix _x ∈ X_ and write _I_ ( _y_ ) := 1 _{y ∈ C_ ( _x_ ) _}_ . The conditional program is 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0028-12.png)


Relax _I ∈{_ 0 _,_ 1 _}_ to _I ∈_ [0 _,_ 1]. Similar to the marginal problem, we can form the Lagrangian with multipliers _λ_ ( _x_ ) = ( _λ_ 1( _x_ ) _, . . . , λK_ ( _x_ )) _∈_ R _[K]_ +[(here] _[x]_[is][treated][as][fixed,][yet][we][write][the][argument][in] _[x]_[for][clarity):] 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0028-14.png)


Let _hλ_ ( _x_ )( _y_ ) :=[�] _k[λ][k]_[(] _[x]_[)] _[f][k]_[(] _[y][|][ x]_[).][Then] 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0028-16.png)


For fixed _λ_ ( _x_ ), minimization over _I ∈_ [0 _,_ 1] is pointwise in _y_ . Any minimizer has the threshold form 

_Cλ_ ( _x_ )( _x_ ) = � _y_ : _hλ_ ( _x_ )( _y_ ) _>_ 1� _∪ S_ ( _x_ ) _,_ with _S_ ( _x_ ) _⊆{y_ : _hλ_ ( _x_ )( _y_ ) = 1 _}._ (19) 

The dual function is 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0028-20.png)


this gives the conditional dual objective (5) mentioned in the theorem, and the dual problem is to maximize Φ _x_ over _λ_ ( _x_ ) _∈_ R _[K]_ +[.] 

Slater’s condition holds (e.g., _C_ ( _x_ ) _≡Y_ yields strict feasibility since _α ∈_ (0 _,_ 1)), so strong duality applies and a dual maximizer _λ[∗]_ ( _x_ ) exists. Thresholding _hλ∗_ ( _x_ ) yields a primal optimum _C[∗]_ ( _x_ ). Complementary slackness gives, for each _k_ , 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0028-23.png)


Hence: 

28 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0029-00.png)


We now show that at least one coordinate of _λ[∗]_ ( _x_ ) is strictly positive. Note that Φ _x_ (0) = 0. Fix any _j ∈{_ 1 _, . . . , K}_ and consider _λ_ ( _x_ ) = _tej_ with _t >_ 0, where _ej_ is the _j_ -th unit vector. Then _hλ_ ( _x_ )( _y_ ) = _tfj_ ( _y | x_ ) and 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0029-02.png)


For any _a ≥_ 0 and _t >_ 0, ( _ta −_ 1)+ _≤ ta ·_ 1 _{ta −_ 1 _≥_ 0 _}_ = _ta ·_ 1 _{a ≥_ 1 _/t}_ . Applying this pointwise with _a_ = _fj_ ( _y | x_ ) and integrating, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0029-04.png)


Because _fj_ ( _· | x_ ) is a density (or probability mass function), � _fjdµ_ = 1. The set _{fj ≥_ 1 _/t}_ shrinks to the empty set as _t ↓_ 0, and 0 _≤ fj_ 1 _{fj ≥_ 1 _/t} ≤ fj_ . By dominated convergence, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0029-06.png)


Therefore, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0029-08.png)


Since _Tj_ ( _t_ ) _→_ 0 and 1 _− α >_ 0, there exists _t_ 0 _>_ 0 such that for all _t ∈_ (0 _, t_ 0), 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0029-10.png)


Thus sup _λ_ ( _x_ ) _≥_ 0 Φ _x_ ( _λ_ ( _x_ )) _>_ 0, so a dual maximizer cannot be _λ[∗]_ ( _x_ ) = 0. Consequently,[�] _k[λ] k[∗]_[(] _[x]_[)] _[>]_[0][and] there exists some _k[∗]_ with _λ[∗] k[∗]_[(] _[x]_[)] _[ >]_[ 0.][By][complementary][slackness][(][20][),] 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0029-12.png)


Additionally, if _µ_ ( _{y_ : _hλ∗_ ( _x_ )( _y_ ) = 1 _}_ ) = 0, then the boundary set is _µ_ -null, making the optimizer unique up to _µ_ -null sets. 

## **B.4 Proof of Theorem 3** 

We begin by introducing the notation employed throughout the proofs, as well as several auxiliary lemmas that will be relied upon in the main results. Proofs of the lemmas are deferred to the Appendix B.4.2. We begin with some useful definitions. 

**Definition 11** (L´evy distance) **.** _For CDFs F and G on_ R _, we denote the L´evy distance as_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0029-17.png)


**Definition 12** (Generalized quantile) **.** _For α ∈_ (0 _,_ 1) _, define the generalized α-quantile set of a CDF G as_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0029-19.png)


_We term each q ∈ Qα_ ( _G_ ) _as a generalized α-quantile._ 

**Definition 13** (Randomized quantile) **.** _Given scores W_ 1 _, . . . , Wn ∈_ R _and an auxiliary U ∼_ Unif(0 _,_ 1) _independent of the data, define the randomized empirical CDF_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0029-22.png)


_We define the randomized empirical α-quantile of {W_ 1 _, . . . , Wn} as_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0029-24.png)


29 

**Lemma 14** (Quantile stability under uniform CDF convergence) **.** _Let G be a CDF on_ R _and let Gn be CDFs with_ sup _t |Gn_ ( _t_ ) _− G_ ( _t_ ) _| →_ 0 _as n →∞. Fix α ∈_ (0 _,_ 1) _, and let Qα_ ( _G_ ) _denote the generalized α-quantile set defined in Equation_ (22) _. Suppose qn ∈_ R _satisfies Gn_ ( _qn−_ ) _≤ α ≤ Gn_ ( _qn_ ) _, then_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0030-01.png)


_In particular, if Qα_ ( _G_ ) = _{q[∗] } (i.e., G is continuous at the α-quantile and there is no flat segment at level α), then qn → q[∗] ._ 

**Lemma 15** (L´evy-to-quantile-set continuity) **.** _Let dL denote the L´evy distance as defined in Equation_ (21) _. If dL_ ( _Gn, G_ ) _≤ ε and Qα_ ( _G_ ) = [ _a, b_ ] _, then every q ∈ Qα_ ( _Gn_ ) _satisfies q ∈_ [ _a − ε, b_ + _ε_ ] _. In particular,_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0030-04.png)


## **B.4.1 Proof of Theorem 3** 

_Proof of Theorem 3._ To clearly denote the asymptotic regime as _n →∞_ , throughout this proof, we add the superscript ( _n_ ) to the estimated quantities _λ_[ˆ] , _f_[ˆ] _k_ , and _h_[ˆ] . 

Since both _fk_ and _λ_[ˆ][(] _[n]_[)] are bounded, and by assumption, sup _x ∥λ_[ˆ][(] _[n]_[)] ( _x_ ) _−λ[∗]_ ( _x_ ) _∥∞ →p_ 0, sup _x,y |f_ ˆ _k_ ( _n_ )( _y|x_ ) _− p fk_ ( _y|x_ ) _| →_ 0, decompose 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0030-08.png)


Each term tends to 0 in probability, hence 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0030-10.png)


Fix _k_ and condition on _h_[ˆ][(] _[n]_[)] . Let _Wk,i_ := _h_[ˆ][(] _[n]_[)] ( _Xi_[(] _[k]_[)] _, Yi_[(] _[k]_[)] ) and _Wk,_ test := _h_[ˆ][(] _[n]_[)] ( _x, y_ ). Since _V_ = _−h_[ˆ] , the randomized _p_ -value from the Equation (7) is the randomized empirical CDF of _W_ at the test point: 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0030-12.png)


Thus, the single-source prediction set is based on thresholding _h_[ˆ][(] _[n]_[)] : 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0030-14.png)


where _q_ ˆ _k,α_[(] _[n]_[)][is][the][randomized][empirical] _[α]_[-quantile][of] _[W][k,i]_[:] 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0030-16.png)


Aggregating _K_ sources yields 

_C_ ˆ[(] _[n]_[)] ( _x_ ) = _{y_ : ˆ _h_[(] _[n]_[)] ( _x, y_ ) _≥ q_ ˆmin[(] _[n]_[)] _,α[}][,]_ 

where _q_ ˆmin[(] _[n]_[)] _,α_[:= min] _[k][q]_[ˆ] _k,α_[(] _[n]_[)][.] 

Let _Fk_ ( _t_ ) be the CDF of _h[∗]_ ( _X, Y_ ) under _P_[(] _[k]_[)] and _Fk_[(] _[n]_[)] ( _t_ ) the CDF of _h_[ˆ][(] _[n]_[)] ( _X, Y_ ). Conditional on the training data, the calibration scores are i.i.d. from a distribution with CDF _Fk_[(] _[n]_[)] . By the DKW inequality, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0030-21.png)


30 

Moreover, since sup _|h_[ˆ][(] _[n]_[)] _− h[∗] | →p_ 0, we can show that 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-01.png)


_p n_ ) with _εn →_ 0, hence _dL_ ( _Fk_ ( _, Fk_ ) _→_ 0 in probability (equivalently, _Fk_[(] _[n]_[)] ( _t_ ) _→ Fk_ ( _t_ ) at continuity points). Therefore, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-03.png)


in probability, and in particular _F_[ˆ] _k_[(] _[n]_[)] ( _t_ ) _→ Fk_ ( _t_ ) at all continuity points _t_ (uniformly in probability). Since our randomized p-value inversion selects an empirical generalized _α_ -quantile _q_ ˆ _k,α_[(] _[n]_[)] _[∈][Q][α]_[( ˆ] _[F]_[ (] _k[n]_[)] ), apply Lemma 14 yields 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-05.png)



![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-06.png)



![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-07.png)


By triangle inequality, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-09.png)


That is, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-11.png)


In particular, if 1 is the unique generalized _α_ -quantile of _Fk_ , then _q_ ˆ _k,α_[(] _[n]_[)] _→p_ 1. 

By KKT conditions and strong duality, we know the optimal rule thresholds at 1; that is, it includes all ( _x, y_ ) with _h[∗]_ ( _x, y_ ) _>_ 1 and, at most, a randomized fraction of those with _h[∗]_ ( _x, y_ ) = 1. Under _P_[(] _[k]_[)] , the maximal coverage achievable without lowering the threshold is 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-14.png)


The coverage constraint P[(] _[k]_[)] ( _y ∈ C[∗]_ ) _≥_ 1 _− α_ therefore forces 1 _− Fk_ (1 _[−]_ ) _≥_ 1 _− α_ , i.e., _Fk_ (1 _[−]_ ) _≤ α_ for every _k_ ; otherwise the threshold-1 solution would be infeasible, contradicting strong duality. 

By conclusion (iii) of Theorem 2, there exists at least one _k_ with _λk >_ 0, such that _α_ lies in the jump [ _Fk_ (1 _[−]_ ) _, Fk_ (1)], hence the generalized _α_ -quantile is unique and equals 1. Consequently, for each _k_ , any _α_ -quantile of _Fk_ is no smaller than 1, and for at least one _k_ , it is exactly equal to 1. Therefore, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-17.png)


Let 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-19.png)


Then _δn →p_ 0 by Equations (25) and (24). Also note that, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-21.png)


Hence, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0031-23.png)


31 

where 

_B_ ˆ _n ⊆{_ ( _x, y_ ) : _|h_ ˆ[(] _[n]_[)] ( _x, y_ ) _− q_ ˆmin[(] _[n]_[)] _,α[|]_[ = 0] _[} ⊆{]_[(] _[x, y]_[) :] _[ |][h][∗]_[(] _[x, y]_[)] _[ −]_[1] _[| ≤][δ][n][}][,]_ which follows from the Equation (24) derived earlier. Taking symmetric differences with _{_ ( _x, y_ ) : _h[∗]_ ( _x, y_ ) _≥_ 1 _}_ and letting _n →∞_ , 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0032-02.png)


since _T_ = _{_ ( _x, y_ ) : _h[∗]_ ( _x, y_ ) = 1 _}_ and _|T |_ = _ρ_ ( _T_ ) = � _X[µ]_[(] _[T]_[(] _[x]_[))] _[dν]_[(] _[x]_[),][and][the][measure][of][shrinking][neighbor-] hoods of _T_ tends to _|T |_ . 

Finally, write 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0032-05.png)


The first bracket is bounded in absolute value by _ρ_ ( _C_[ˆ][(] _[n]_[)] _△{h[∗] ≥_ 1 _}_ ) _≤|T |_ from Inequality (26). The second bracket equals _|T | −|S[∗] |_ + _|{h[∗] >_ 1 _}| −|{h[∗] >_ 1 _}|_ = _|T | −|S[∗] |_ , whose absolute value is _≤|T |_ . Therefore, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0032-07.png)


Moreover, Inequality (26) shows there exists a subsequence _{nj}_ and a measurable set _S∞ ⊆ T_ := _{_ ( _x, y_ ) : _h[∗]_ ( _x, y_ ) = 1 _}_ such that 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0032-09.png)


Consequently, choosing the oracle set _C[∗]_ ( _x_ ) = _{y_ : _h[∗]_ ( _x, y_ ) _>_ 1 _} ∪ S∞_ ( _x_ ) yields _|C_[ˆ][(] _[n][j]_[)] _| →|C[∗] |_ . 

## **B.4.2 Proof of Lemma 14** 

_Proof of Lemma 14._ For a monotone right-continuous _H_ , denote the left limit by _H_ ( _x−_ ) := sup _t<x H_ ( _t_ ). If sup _t |Hn_ ( _t_ ) _− H_ ( _t_ ) _| ≤ ε_ , then also sup _x |Hn_ ( _x−_ ) _− H_ ( _x−_ ) _| ≤ ε_ , because 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0032-13.png)


Let _a_ := inf _{t_ : _G_ ( _t_ ) _≥ α}_ and _b_ := sup _{t_ : _G_ ( _t_ ) _≤ α}_ ; then _a ≤ b_ and _Qα_ ( _G_ ) = [ _a, b_ ]. Then 

- For any _δ >_ 0, _G_ ( _a − δ_ ) _< α_ . Define _γL_ ( _δ_ ) := _α − G_ ( _a − δ_ ) _>_ 0. 

- For any _δ >_ 0, for all _x ≥ b_ + _δ_ we have _G_ ( _x−_ ) _> α_ . Indeed, for any such _x_ pick _s_ with _b < s < x_ ; then _G_ ( _s_ ) _> α_ by definition of _b_ , so _G_ ( _x−_ ) _≥ G_ ( _s_ ) _> α_ . Hence define _γR_ ( _δ_ ) := _G_ ( _b_ + _δ/_ 2) _− α >_ 0. 

**Left bound.** Fix _δ >_ 0 and choose _n_ large so that sup _t |Gn_ ( _t_ ) _− G_ ( _t_ ) _| ≤ εn_ with _εn < γL_ ( _δ_ ) _/_ 2. If _q ≤ a − δ_ then 

_Gn_ ( _q_ ) _≤ G_ ( _q_ ) + _εn ≤ G_ ( _a − δ_ ) + _εn_ = _α − γL_ ( _δ_ ) + _εn < α,_ 

contradicting the requirement _α ≤ Gn_ ( _q_ ) for _q ∈ Qα_ ( _Gn_ ). Therefore any _q ∈ Qα_ ( _Gn_ ) must satisfy _q > a − δ_ . **Right bound.** With the same _n_ and _εn_ and the _γR_ ( _δ_ ) defined above, if _q ≥ b_ + _δ_ then 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0032-20.png)


contradicting the requirement _Gn_ ( _q−_ ) _≤ α_ for _q ∈ Qα_ ( _Gn_ ). Therefore any _q ∈ Qα_ ( _Gn_ ) must satisfy _q < b_ + _δ_ . 

32 

Therefore, for any fixed _δ >_ 0 and all sufficiently large _n_ we have 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0033-01.png)


In particular, our selected _qn ∈ Qα_ ( _Gn_ ) lies within _δ_ of the closed set [ _a, b_ ] = _Qα_ ( _G_ ), so dist( _qn, Qα_ ( _G_ )) _≤ δ_ . Because _δ >_ 0 was arbitrary, dist( _qn, Qα_ ( _G_ )) _→_ 0. 

For the unique-quantile case _Qα_ ( _G_ ) = _{q[∗] }_ , the distance convergence implies _qn → q[∗]_ . 

## **B.4.3 Proof of Lemma 15** 

_Proof of Lemma 15. dL ≤ ε_ means _F_ ( _x − ε_ ) _− ε ≤ Gn_ ( _x_ ) _≤ F_ ( _x_ + _ε_ ) + _ε_ for all _x_ . If _q ∈ Qα_ ( _Gn_ ) then _Gn_ ( _q−_ ) _≤ α ≤ Gn_ ( _q_ ), hence 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0033-06.png)


If _q < a − ε_ , then _q_ + _ε < a_ and _F_ ( _q_ + _ε_ ) _≤ α_ , contradicting the right inequality. If _q > b_ + _ε_ , then _q − ε > b_ and _F_ ( _q − ε_ ) _≥ α_ , contradicting the left inequality. So _q ∈_ [ _a − ε, b_ + _ε_ ]. 

## **B.5 Optimality of the integrated dual problem** 

In this part, we formalize the discussion at the beginning of Section 4.1 on the optimal _λ[∗]_ ( _x_ ) as the solution to an integrated dual objective. 

**Proposition 16** (Equivalence of integrated dual and conditional dual) **.** _For k_ = 1 _, . . . , K, let fk_ ( _· | x_ ) _be the conditional density/pmf of Y | X_ = _x with respect to µ. Fix α ∈_ (0 _,_ 1) _. For λ ∈_ R _[K]_ + _[and][x][∈X][,][define] hλ_ ( _x, y_ ) :=[�] _[K] k_ =1 _[λ][k][f][k]_[(] _[y][|][ x]_[)] _[,][and]_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0033-11.png)


_Let ν_ ˜ _be a σ-finite measure on_ ( _X , A_ ) _with Radon–Nikodym density w_ ( _x_ ) := _[d] dν[ν]_[˜] _[satisfying]_[0] _[ < w]_[(] _[x]_[)] _[ <][ ∞][for] ν-a.e. x. Consider the integrated dual objective_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0033-13.png)


_Then_ Φ _ν_ ˜( _λ_ ( _·_ )) = � _X[w]_[(] _[x]_[)] _[ φ][x]_[(] _[λ]_[(] _[x]_[))] _[ dν]_[(] _[x]_[)] _[,][and]_ 

_(i) A measurable λ[∗]_ ( _·_ ) _maximizes_ Φ _ν_ ˜ _if and only if_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0033-16.png)


_Hence the set of maximizers is independent of the particular choice of ν_ ˜ _, as long as dν/dν_ ˜ _>_ 0 _ν-a.e._ 

- _(ii) For ν-a.e. x, any maximizer λ[∗]_ ( _x_ ) _is a dual maximizer of the x-conditional problem_ (4) _. Thresholding hλ∗ at level 1 gives the conditionally optimal set_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0033-19.png)


˜ _as in Theorem 2. Thus the optimal score and set do not depend on ν._ 

_Proof of Proposition 16._ By the Radon–Nikodym theorem, _dν_ ˜ = _w dν_ with _w >_ 0 _ν_ -a.e. Substituting, 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0033-22.png)


33 

For any measurable _λ_ ( _·_ ), 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0034-01.png)


with equality iff _φx_ ( _λ_ ( _x_ )) = sup _λ≥_ 0 _φx_ ( _λ_ ) for _ν_ -a.e. _x_ . Note that _λ_[ˆ] ( _·_ ) with _λ_[ˆ] ( _x_ ) _∈_ argmax _φx_ ( _·_ ) exists and attains the upper bound, for this _λ_[ˆ] , 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0034-03.png)


which matches the upper bound in Equation (27) and is therefore optimal. Moreover, if a candidate _λ_ ( _·_ ) fails to maximize _φx_ at a set of _x_ with positive _ν_ ˜-measure, replacing it by a pointwise maximizer on that set always strictly increases Φ _ν_ ˜, proving the necessity. Because _w_ ( _x_ ) _>_ 0, multiplying by _w_ ( _x_ ) does not change the pointwise argmax sets, so the maximizers are independent of _ν_ ˜. 

By definition, _φx_ ( _·_ ) is the dual objective of the _x_ -conditional problem (4). Therefore, a pointwise maximizer _λ[∗]_ ( _x_ ) is a dual maximizer for (4). By KKT conditions for (4), thresholding _hλ∗_ ( _x, ·_ ) at 1 yields the conditionally optimal set stated above. Independence from _ν_ ˜ follows from (i). 

## **B.6 Proof of Theorem 9** 

_Proof of Theorem 9._ First, following exactly the same conditions and proof in Jin et al. [2022, Theorem 1] applied to the loss function _ℓ_[ˆ] ( _·_ ), we can show that _∥λ_[ˆ] _− λ_[¯] _[∗] ∥L_ 2 = _OP_ �([lo] _n_[g] _[ n]_[)] _[p/]_[(2] _[p]_[+] _[d]_[)][�] and _∥λ_[ˆ] _− λ_[¯] _[∗] ∥∞_ = _OP_ �([lo] _n_[g] _[ n]_[)][2] _[p]_[2] _[/]_[(2] _[p]_[+] _[d]_[)][2][�] . Then, by triangle inequality and Assumption 7, we obtain the desired results. 

## **C Experimental details** 

## **C.1 Hyperparameter sampling** 

We detail the sampling process of the hyperparameters in the simulations in Section 5.3. 

For the interaction family, we draw the weights i.i.d. from _wuv ∼N_ (0 _,_ 1 _._ 1[2] ) for ( _u, v_ ) _∈I × I_ . For both the sinusoidal and softplus families, each unit _r_ = 1 _,_ 2 _,_ 3 uses a projection vector _ur ∈_ R _[d]_ constructed as follows: we first sample a support _Sr ⊂I_ of size 3 uniformly at random and draw a magnitude _Mr ∼_ Unif(0 _._ 375 _,_ 0 _._ 875), sample a random unit vector _dr ∈_ R[3] and define _ur_ [ _Sr_ ] = _Mrdr_ with _ur_ [ _I \ Sr_ ] = 0. The sinusoidal component samples _br ∼_ Unif( _−π/_ 3 _, π/_ 3) and _ar ∼_ Unif(0 _._ 5 _,_ 1 _._ 5), independently across _r_ . The softplus component utilizes the same construction for _ur_ as above, but with _br ∼_ Unif( _−_ 0 _._ 5 _,_ 0 _._ 5) and _ar ∼_ Unif(0 _._ 75 _,_ 2 _._ 0), again independently across _r_ . 

## **C.2 Algorithm instantiation** 

This subsection includes omitted implementation details in the classification and regression algorithms in our experiments. 

**Classification algorithm** In Section 5.2, we use nonparametric methods for probability estimations (in our case, we use gradient-boosted trees), and calibrate their probabilistic outputs with stratified crossvalidation and an isotonic mapping. We solve for the optimizer _λ_ using minibatch updates. The optimization is implemented in PyTorch with automatic differentiation, where precomputed spline features, data densities, source weights, and related terms are used to form an objective on the minibatch, with a trainable spline parameter matrix. Gradients are then computed via autodifferentiation, and parameters are updated with Adam. After each epoch update, we do full-data evaluations to allow early stopping, improving efficiency and mitigating overfitting. 

34 

**Regression algorithm** In Section 5.3, for each source _k_ we fit a heteroskedastic Gaussian plug-in model for the conditional density. We first learn a regression function _µ_ ˆ _k_ ( _x_ ) using flexible nonparametric estimators (in our case, we use gradient-boosted trees). To model dispersion, we obtain out-of-fold predictions _µ_ ˜ for the mean model via _K_ -fold: we partition the data into _K_ folds, for each of the _K_ folds, fit the model on _K −_ 1 ˆ ˜ folds and predict on the held-out fold and compute the squared residuals _r_[2] = ( _Y − µ_ )[2] . we then fit a second regressor on residual variance to the logarithm of the residual squares using all _K_ folds. At prediction time we evaluate _σ_ ˆ _k_ ( _x_ ) from this variance model, and form 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0035-01.png)


As in classification, we treat the marginal density of _X_ as constant and use _f_[ˆ] _k_ ( _x, y_ ) := _f_[ˆ] _k_ ( _y | x_ ) throughout. And we also use minibatch optimizer, softplus nonnegativity, and early stopping. 

## **C.3 Grid search algorithm and guarantee** 

Let _D_ train and _D_ calib be the training and calibration data pooled across all _K_ sources. Define: 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0035-05.png)


Fix an integer _M ≥_ 2 (e.g., _M_ = 100). Define a uniform grid on [ _yL, yU_ ] with ∆:= _[y] M[U][−] −[y]_ 1 _[L]_[:] 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0035-07.png)


We call _y_[(] _[j]_[)] and _y_[(] _[j]_[+1)] are adjacent grid points. A subset _B_ of indices is called _consecutive_ if it contains no gaps; equivalently, _B_ can be written as _{a, a_ + 1 _, . . . , b}_ for some integers _a ≤ b_ . For example, _{_ 3 _,_ 4 _,_ 5 _}_ is consecutive, while _{_ 3 _,_ 5 _}_ is not. For a test covariate _x_ , we include a candidate _y_ -grid point _y_ if the aggregated MDCP _p_ -value _p_ ( _y_ ) := max _k p_[(] _[k]_[)] ( _x, y_ ) _>_ = _α_ , where each _p_[(] _[k]_[)] is derived using formula (7). Let 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0035-09.png)


be the set of included grid indices. We decompose _J_ into consecutive blocks _Br_ = _{jr,L, . . . , jr,R}_ for _r_ = 1 _, . . . , R_ . We say a decomposition is _maximal_ , if the decomposed blocks are consecutive, disjoint and cannot be enlarged by adding adjacent indices from _J_ . 

35 

**Algorithm 2** Grid-Search Algorithm (Regression) 

**Input:** Number of sources _K_ , pooled calibration data _D_ = _∪[K] k_ =1 _[D]_[(] _[k]_[)][,][test][input] _[x]_[,][grid][endpoints] _[y][L][, y][U]_[,] grid size _M_ , grid spacing ∆, significance level _α_ 

- 1: `// Grid construction` 

- 2: Construct grid points _y_[(] _[j]_[)] , _j_ = 0 _, . . . , M −_ 1 over [ _yL, yU_ ] as in (28). 

- 3: `// Evaluate aggregated` _p_ `-values on the grid` 

- 4: **for** _j_ = 0 **to** _M −_ 1 **do** 

- 5: Compute _p_ ( _y_[(] _[j]_[)] ) = max _k p_[(] _[k]_[)] ( _x, y_[(] _[j]_[)] ) 

- 6: **end for** 

- 7: Collect included grid points, form _J_ following (29). 

- 8: `// Merge included grid points into blocks` 

- 9: Decompose _J_ into maximal consecutive blocks _Br_ = _{jr,L, . . . , jr,R}_ for _r_ = 1 _, . . . , R_ . 

- 10: `// Extend each block by one grid spacing` 

- 11: **for** each block _Br_ **do** 

12: Create interval _Ir_ := [ _y_[(] _[j][r,L]_[)] _−_ ∆ _, y_[(] _[j][r,R]_[)] + ∆] 

- 13: **end for** 

14: Taking unions of all intervals _C_ grid( _x_ ) :=[�] _r[I][r]_ **Output:** Regression prediction set _C_ grid( _x_ ) for test input _x_ 

Let _C_ MDCP denote the MDCP set we want to construct with score _sk_ ( _x, y_ ) = _−_[�] _[K] k_ =1 _[λ][k]_[(] _[x]_[;][ˆΘ) ˆ] _[f][k]_[(] _[y][ |][ x]_[)] and _p_ -value (7). Let _C_ grid denote the conformal set constructed from the grid search Algorithm 2. 

**Proposition 17** (Superset on the grid range) **.** _Let C_ := _C_ MDCP( _x_ ) _∩_ [ _yL, yU_ ] _. Suppose each connected component of C is a closed interval_ [ _ℓ, r_ ] _that intersects the grid, i.e.,_ [ _ℓ, r_ ] _∩{y_[(] _[j]_[)] _} ̸_ = ∅ _. Then_ 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0036-18.png)


_Proof of Proposition 17._ Fix a connected component [ _ℓ, r_ ] _⊆ C_ with [ _ℓ, r_ ] _∩{y_[(] _[j]_[)] _} ̸_ = ∅. Let 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0036-20.png)


Since _y_[(] _[j]_[1][)] _, y_[(] _[j]_[2][)] _∈_ [ _ℓ, r_ ] _⊆ C_ , we have _p_ ( _y_[(] _[j]_[1][)] ) _≥ α_ and _p_ ( _y_[(] _[j]_[2][)] ) _≥ α_ , so _j_ 1 _, j_ 2 _∈ J_ and all indices _j ∈_ [ _j_ 1 _, j_ 2] belong to the same consecutive block _Br_ . 

By grid spacing, _y_[(] _[j]_[1] _[−]_[1)] = _y_[(] _[j]_[1][)] _−_ ∆(if _j_ 1 _>_ 0), and _y_[(] _[j]_[2][+1)] = _y_[(] _[j]_[2][)] + ∆(if _j_ 2 _< M −_ 1). 

(i). Because _j_ 1 is the first grid index inside [ _ℓ, r_ ], we have _y_[(] _[j]_[1] _[−]_[1)] _< ℓ ≤ y_[(] _[j]_[1][)] , hence _ℓ ≥ y_[(] _[j]_[1][)] _−_ ∆. 

(ii). Because _j_ 2 is the last grid index inside [ _ℓ, r_ ], we have _y_[(] _[j]_[2][)] _≤ r < y_[(] _[j]_[2][+1)] , hence _r ≤ y_[(] _[j]_[2][)] + ∆. 

Therefore [ _ℓ, r_ ] _⊆_ [ _y_[(] _[j]_[1][)] _−_ ∆ _, y_[(] _[j]_[2][)] +∆] = _Ir_ , where _Ir_ is an interval produced from the Algorithm 2. Taking the union over all components yields _C ⊆_[�] _r[I][r]_[=] _[ C]_[grid][(] _[x]_[).][Finally,][by][construction] _[I][r][⊆]_[[] _[y][L][ −]_[∆] _[,][y][U]_[+ ∆],] so 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0036-26.png)


That is, within the observed _y_ -range, the grid merge-and-extend procedure never excludes any MDCPaccepted value and may only enlarge the set. 

## **C.4 Real-data modeling details** 

## **C.4.1 FMoW model setup** 

After training the `DenseNet-121` backbone on the pre-training split, we use its penultimate feature representation _e_ ( _x_ ) for all subsequent conformal procedures. During the training, we fit a pooled multiclass 

36 

probabilistic classifier on the model training fold _D_ pre-train and, in parallel, one classifier per geographic region on the corresponding region-specific model training fold. Each classifier is trained via cross-entropy and yields estimated class probabilities, denoted by _p_ ˆdata( _y | x_ ) for the pooled model and _p_ ˆ _k_ ( _y | x_ ) for the _k_ -th region. These estimates are used to compute APS scores for the baselines and to form the MDCP score (Section 4.2) through _h_[ˆ] ( _x, y_ ) =[�] _[K] k_ =1 _[λ]_[ˆ] _[k]_[(] _[x]_[)ˆ] _[p][k]_[(] _[y][|][ x]_[),][where] _[λ]_[ˆ][(] _[·]_[)][is][learned][from][the] _[auxiliary]_[training][data.] When fitting _λ_[ˆ] ( _·_ ), we apply PCA to _e_ ( _x_ ) on the _auxiliary_ training data and use the leading components as the input features, following Section 6.1. 

## **C.4.2 PovertyMap model setup** 

We train an 8-channel `ResNet-18` backbone on the designated training split and denote its penultimate feature representation by _e_ ( _x_ ). During the training, we fit (i) a pooled heteroskedastic Gaussian model on the auxiliary training split and (ii) two source-specific Gaussian models for Urban and Rural on their corresponding auxiliary training subsets. Each model outputs functions _µ_ ˆ( _x_ ) _∈_ R and _σ_ ˆ( _x_ ) _>_ 0 (we use softplus as a monotone link to enforce positivity) and defines the conditional density _f_[ˆ] ( _y | x_ ) = _N_ ( _y_ ; ˆ _µ_ ( _x_ ) _,_ ˆ _σ_[2] ( _x_ )). The models are trained by minimizing the Gaussian negative log-likelihood: for an observation ( _xi, yi_ ), 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0037-03.png)


The fitted source-specific densities _{f_[ˆ] _k}_ and the pooled density _f_[ˆ] data are then used in both the regression baselines and MDCP via the score _h_[ˆ] ( _x, y_ ) =[�] _[K] k_ =1 _[λ]_[ˆ] _[k]_[(] _[x]_[) ˆ] _[f][k]_[(] _[y][|][ x]_[)][and][the][max-] _[p]_[aggregation][(Sections][4.3][).] As in Section 6.2, we apply PCA to _e_ ( _x_ ) on the auxiliary training split before fitting _λ_[ˆ] ( _·_ ). 

## **D Additional experiments** 

## **D.1 Ablation study on optimization stability** 

For the ablation study, we examine the difficulty of optimizing the dual objective (8) and assess the stability and reliability of the optimization procedure. The motivating idea is to test whether off-the-shelf optimization via `PyTorch` may lead to large fitted coefficients due to instability. To this end, we introduce the following penalty terms to encourage stability, recall in (12), _λj_ ( _x_ ) = softplus �Λ( _x_ ) _[⊤] θj_ � for _j ∈_ [ _K_ ], where Λ( _x_ ) _∈_ R _[m]_ is a vector of spline basis functions and _θj ∈_ R _[m]_ are trainable coefficients: 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0037-08.png)


where _D_ is the second order difference operator: 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0037-10.png)


which serves as a discrete analogue of penalizing the curvature of the underlying function _λk_ ( _·_ ), and _θk,i_ is the _i_ -th parameter in the spline feature space. 

We select the hyperparameter _γ_ over the grid [0 _._ 0 _,_ 0 _._ 001 _,_ 0 _._ 01 _,_ 0 _._ 1 _,_ 1 _._ 0 _,_ 10 _._ 0 _,_ 100 _._ 0 _,_ 1000 _._ 0]. To use the data efficiently, we split the training data into a _mimic calibration set_ and a _mimic test set_ . For each individual run, we calibrate the method on the mimic calibration set for every candidate _γ_ , evaluate performance on the mimic test set, and choose the _γ_ that yields the smallest average set size on this mimic test set. Denote this selected value by _γ[∗]_ . We then fix _γ[∗]_ and run MDCP with the original calibration and test data. Since the calibration and test data are not involved in this optimization process, the uniform coverage guarantee of MDCP still follows. Moreover, we expect the selected hyperparameter to perform at least as well as, and 

37 

potentially better than, the non-penalized version (i.e., _γ_ = 0) in terms of the chosen efficiency criterion. We compare the results from the penalized MDCP with data-driven _γ[∗]_ side by side with the non-penalized version ( _γ_ = 0). We evaluate this approach across all the simulation studies and real data applications. 

## **D.1.1 Simulation results** 

For the classification simulations, using the setup in Section 5.2, we evaluate performance on the three suites from Section 5.1: `Linear` (Figure 11), `Nonlinear` (Figure 12), and `Temperature` (Figure 13). After the initial training step, we split the training data into equal-sized mimic calibration and mimic test sets (50%/50%) and apply the parameter-selection procedure described above. Across all three suites, tuning the penalty parameter _γ_ produces at most negligible gains in set efficiency. This suggests that the MDCP optimization step is already stable and no additional penalty is required in most of the simulation settings. 

In the regression simulations, under the same setup as Section 5.3, we examine performance on the three suites defined in Section 5.1: `Linear` (Figure 14), `Nonlinear` (Figure 15), and `Temperature` (Figure 16). Analogous to the classification experiments, once the model has been trained, we divide the training data evenly into a mimic calibration set and a mimic test set, and subsequently perform the parameter selection procedure described above. Across all three suites, data-driven tuning of the penalty parameter _γ_ produces, at best, marginal improvements in set efficiency. This finding indicates that the baseline MDCP optimization procedure is already sufficiently robust, and that, in most simulated scenarios, the dual optimization problem can be solved reliably without introducing an additional penalty term. 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0038-04.png)


**----- Start of picture text -----**<br>
Baseline agg Baseline src 0 Baseline src 1 Baseline src 2 MDCP MDCP tuned<br>1.00 1.00 6<br>0.90<br>0.90<br>4<br>0.70 2<br>0.70<br>0.49 0.15 0<br>Method Method Method<br>Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCPMDCP tuned Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCPMDCP tuned Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCPMDCP tuned<br>Avg set size<br>Overall coverage<br>Worst-case coverage<br>**----- End of picture text -----**<br>


Figure 11: Evaluation on the classification `Linear` suites, where MDCP with data-driven _γ[∗]_ is labeled as “MDCP tuned”. All other experimental settings are identical to those in Figure 2. 

38 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0039-00.png)


**----- Start of picture text -----**<br>
Max-agg baseline Source 0 Source 1 Source 2 MDCP MDCP tuned<br>Overall coverage Worst-case coverage Avg set size<br>1.00 1.00<br>6<br>0.90<br>0.90 5<br>4<br>0.70 3<br>0.70<br>2<br>0.42 0.13 1<br>Nonlinear term Nonlinear term Nonlinear term<br>linear interaction sinusoid softplus linear interaction sinusoid softplus linear interaction sinusoid softplus<br>**----- End of picture text -----**<br>


Figure 12: Evaluation on the classification `Nonlinear` suites. Experimental settings are identical to Figure 3. The differences between vanilla MDCP and tuned MDCP are small across all nonlinear term settings. 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0039-02.png)


**----- Start of picture text -----**<br>
Baseline (max agg) Baseline src 0 Baseline src 1 Baseline src 2 MDCP MDCP tuned<br>Overall coverage Worst-case coverage Avg set size<br>6<br>0.9<br>0.9<br>0.8<br>4<br>0.8 0.7<br>0.6 2<br>0.7<br>0.5<br>0.5 1.5 2.5 3.5 4.5 0.5 1.5 2.5 3.5 4.5 0.5 1.5 2.5 3.5 4.5<br>Temperature Temperature Temperature<br>**----- End of picture text -----**<br>


Figure 13: Evaluation on the classification `Temperature` suites. Experimental settings are identical to Figure 4. Vanilla MDCP and tuned MDCP exhibit only minor differences across all temperature parameter settings. 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0039-04.png)


**----- Start of picture text -----**<br>
Baseline agg Baseline src 0 Baseline src 1 Baseline src 2 MDCP MDCP tuned<br>0.99 0.99<br>0.90 15<br>0.90<br>10<br>0.70<br>0.70 5<br>0.30 0.00 0<br>Method Method Method<br>Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCPMDCP tuned Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCPMDCP tuned Baseline aggBaseline src 0Baseline src 1Baseline src 2 MDCPMDCP tuned<br>Overall coverage Avg interval width<br>Worst-case coverage<br>**----- End of picture text -----**<br>


Figure 14: Results on the regression `Linear` suites, where MDCP with the selected penalty strength parameter _γ[∗]_ appears as “MDCP tuned”. All other experimental settings match those in Figure 5. 

39 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0040-00.png)


**----- Start of picture text -----**<br>
Max-agg baseline Source 0 Source 1 Source 2 MDCP MDCP tuned<br>Overall coverage Worst-case coverage Avg interval width<br>1.00 1.00<br>35<br>0.90 0.90 30<br>25<br>20<br>0.70<br>15<br>0.70<br>10<br>5<br>0.31 0.00 0<br>Nonlinear term Nonlinear term Nonlinear term<br>Figure 15: Results on the regression Nonlinear suites Experimental settings match those in Figure 6. Across all<br>choices of the nonlinear term, MDCP and tuned MDCP behave very similarly.<br>Baseline (max agg) Baseline src 0 Baseline src 1 Baseline src 2 MDCP MDCP tuned<br>Overall coverage Worst-case coverage Avg interval width<br>1.0<br>15<br>0.9<br>0.8<br>0.8 10<br>0.6<br>0.7 5<br>0.6 0.4<br>0.5 1.5 2.5 3.5 4.5 0.5 1.5 2.5 3.5 4.5 0.5 1.5 2.5 3.5 4.5<br>Temperature Temperature Temperature<br>linear interaction sinusoid softplus linear interaction sinusoid softplus linear interaction sinusoid softplus<br>**----- End of picture text -----**<br>


Figure 16: Results on the regression `Temperature` suites. Experimental settings match those in Figure 7. For all temperature parameter values, the gap between MDCP and tuned MDCP is negligible. 

## **D.1.2 Real data results** 

We also assess the impact of _γ_ on the real-world datasets. Following Section 6, we repeat the procedures for the FMoW, PovertyMap, and MEPS datasets, now including _γ_ as an additional tuning parameter. The candidate values match those used above, ranging from 0 _._ 001 to 1000, with _γ_ = 0 corresponding to the non-penalized version. For all three datasets, the training set is split 50%/50% into mimic calibration and mimic test subsets. For the FMoW and PovertyMap experiments, we use _γ_ to control an _ℓ_ 2 penalty on the magnitude of the learned weight functions, of the form _γ_ E[ˆ] train[[�] _k[λ][k]_[(] _[X]_[)][2][].][In][particular,][this][tuning] affects only the estimation of _λ_ ( _x_ ); all subsequent calibration and evaluation steps remain unchanged. For the FMoW dataset (Figure 17), the original MDCP procedure is already stable, and introducing the penalty term yields little to no improvement. For the PovertyMap dataset (Figure 18), introducing _γ_ does not improve overall efficiency but does increase variability in the results. We attribute this to the _γ_ -selection procedure: the chosen value is optimal for the _mimic calibration_ and _mimic test_ sets (Appendix D.1), but not necessarily for the true calibration and test sets. For the MEPS dataset (Figure 19), the low-density regions of the highly skewed target distribution are particularly challenging for baseline methods using score functions similar to Lei et al. [2018]. In this setting, the penalty term still influences the behavior of the _λk_ , helping prevent them from growing excessively large in low-density areas, but the resulting performance gains are modest. MDCP nonetheless maintains stable behavior while focusing more effectively on the higher-density and more practically relevant regions. 

These results show that the mimic-split strategy can yield performance gains in cases where density 

40 

estimation or optimization is particularly difficult, while remaining simple to implement with a 50%/50% calibration–test split. However, in most settings the vanilla MDCP procedure is already sufficiently robust, and the tuned MDCP variant offers little to no additional benefit. 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0041-01.png)


**----- Start of picture text -----**<br>
Baseline agg Africa Americas Asia Europe Oceania Other MDCP MDCP tuned<br>0.98 0.97<br>12.5<br>0.90<br>10.0<br>0.90<br>7.5<br>0.80 5.0<br>0.80 0.61 2.5<br>Method Method Method<br>Figure 17: Results on the FMoW data, using the algorithmic procedure described in Section 6.1. MDCP and tuned<br>MDCP produce closely aligned performance in this case.<br>Baseline agg Rural Urban MDCP MDCP tuned<br>0.98 0.98<br>2.00<br>0.90 0.90<br>1.75<br>1.50<br>1.25<br>0.65<br>0.65 0.56 1.00<br>Method Method Method<br>Baseline agg RuralUrbanMDCPMDCP tuned Baseline agg RuralUrbanMDCPMDCP tuned Baseline agg RuralUrbanMDCPMDCP tuned<br>Baseline aggAfricaAmericas AsiaEuropeOceaniaOtherMDCP tunedMDCP Baseline aggAfricaAmericas AsiaEuropeOceaniaOtherMDCP tunedMDCP Baseline aggAfricaAmericas AsiaEuropeOceaniaOtherMDCP tunedMDCP<br>Avg set size<br>Overall coverage<br>Worst-case coverage<br>Overall coverage Avg interval width<br>Worst-case coverage<br>**----- End of picture text -----**<br>


Figure 18: Results on the PovertyMap data, using the algorithmic procedure described in Section 6.2. Introducing the parameter _γ_ increases the variability of efficiency. 

## **D.2 Additional simulations in covariate shift settings** 

To evaluate MDCP in regimes where covariate shift contributes to the source heterogeneity, we introduce two additional suites of simulation settings: 

(1). `Covariate-shift` : In this suite, _PX_[(] _[k]_[)] differs across sources but _P_ ( _Y | X_ ) is shared. 

(2). `Covariate-and-concept-shift` : In this suite, both _PX_[(] _[k]_[)] and _P_ ( _Y | X_ ) vary across sources. 

These experiments follow the common protocol of Section 5.1: we consider _K_ = 3 sources, feature dimension _d_ = 10, and nominal miscoverage level _α_ = 0 _._ 1. For each source _k ∈{_ 1 _,_ 2 _,_ 3 _}_ , we generate _nk_ = 2000 labeled samples. The pooled data are then randomly split into training (37.5%), calibration (12.5%), and test (50%) folds. For each suite, to focus on the effect of covariate shift, we fix the temperature parameter at _τ_ = 2 _._ 5, exclude nonlinear terms in both classification and regression settings, and sweep the covariate-shift magnitude parameter _δX_ over _δX ∈{_ 0 _,_ 0 _._ 5 _,_ 1 _._ 5 _,_ 2 _._ 5 _,_ 3 _._ 5 _,_ 4 _._ 5 _}_ . For each configuration, we repeat the experiments for _N_ = 100 independent trials. In each setting, we evaluate thye following competing methods: 

41 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0042-00.png)


**----- Start of picture text -----**<br>
Baseline agg Non-white White MDCP MDCP tuned<br>Overall coverage Worst-case coverage Avg interval width<br>0.97 0.97 4.0<br>3.5<br>0.90 0.90<br>3.0<br>0.86<br>2.5<br>0.82<br>0.80 0.80 2.0<br>4.0<br>0.97 0.97<br>3.5<br>0.90 0.90 3.0<br>0.87<br>0.83 2.5<br>0.80 0.80 2.0<br>0.98 0.97<br>4<br>0.90 0.90<br>3<br>0.86<br>0.82<br>0.80 0.80 2<br>Method<br>Baseline aggNon-white WhiteMDCPMDCP tuned Baseline aggNon-white WhiteMDCPMDCP tuned Baseline aggNon-white WhiteMDCPMDCP tuned<br>Baseline aggNon-white WhiteMDCPMDCP tuned Baseline aggNon-white WhiteMDCPMDCP tuned Baseline aggNon-white WhiteMDCPMDCP tuned<br>Baseline aggNon-white WhiteMDCPMDCP tuned Baseline aggNon-white WhiteMDCPMDCP tuned Baseline aggNon-white WhiteMDCPMDCP tuned<br>Panel 19 Panel 19 Panel 19<br>Panel 20 Panel 20 Panel 20<br>Panel 21 Panel 21 Panel 21<br>**----- End of picture text -----**<br>


Figure 19: Results on the MEPS data, using the algorithmic procedure described in Section 6.3. Introducing _γ_ provides a modest improvement to tuned MDCP, offering slightly better efficiency on this highly skewed dataset. 

- (i). `Baseline-src-` _k_ : The standard conformal prediction set _C_[ˆ] src- _k_ with calibration data from source _k_ . 

- (ii). `Baseline-agg` : A simple max- _p_ aggregation of per-source prediction sets _C_[ˆ] max-p := _∪[K] k_ =1 _[C]_[ˆ][src-] _[k]_[.][This] is the baseline without efficiency-oriented score learning. 

- (iii). `MDCP` : Our method in Algorithm 1. 

- (iv). `MDCP-tuned` : The tuned variant of our method in Algorithm 1, employing a spline approximation for _λ_ and tuned penalty-term parameters, as detailed in Appendix D.1. 

As in Section 5.1, the single-source baseline is standard conformal prediction sets with the widely-used APS score [Romano et al., 2020] in classification and the variance-adaptive score of Lei et al. [2018] in regression problems. 

During each randomized individual run, we first sample an informative index set _I ⊂{_ 1 _, . . . , d}_ uniformly at random with _|I|_ = 4. We then construct a shared covariance matrix Σ _∈_ R _[d][×][d]_ for all sources using the equicorrelated form Σ _ij_ = 0 _._ 2 + 0 _._ 8 1 _{i_ = _j}_ . Next, we sample a shift direction _v ∈_ R _[d]_ supported on the informative coordinates: we draw _vI ∼N_ (0 _, I|I|_ ), set _vI c_ = 0, and normalize _v_ . For a given shift magnitude _δX_ , we define the source-specific Gaussian means _µ_ 1 = 0, _µ_ 2 = + _δX v_ , _µ_ 3 = _−δX v_ , and generate covariates i.i.d. as 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0042-08.png)


Importantly, compared to the setup in Section 5.1, we do not standardize _X_ after sampling, so the mean shifts remain present in the observed covariates. 

42 

## **D.2.1 Additional simulations in classification settings** 

**Data generating processes.** For classification, the label space is _Y_ = _{_ 1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _,_ 6 _}_ , with a total of _C_ = 6 classes. We first draw class-specific base slopes _{β_[¯] _c}[C] c_ =1 _[⊂]_[R] _[d]_[supported][on] _[I]_[,][with][(¯] _[β][c]_[)] _[j][∼N]_[(0] _[,]_[ 1)] for _j ∈ I_ and ( _β_[¯] _c_ ) _j_ = 0 for _j ∈/ I_ . We then generate _Y | X_ using a multinomial logit model with a fixed temperature _τ_ = 2 _._ 5. 

In the `Covariate-shift` suite, the conditional distribution _P_ ( _Y | X_ ) is shared across sources. We draw shared intercepts[¯] _bc ∼N_ (0 _,_ (0 _._ 4 _τ_ )[2] ) and set _ξk ≡ τ_ , _βkc ≡ β_[¯] _c_ , and _bkc ≡_[¯] _bc_ for all sources _k_ . Given a covariate value _x_ , we compute logits _ηc_ ( _x_ ) = _τ_ ([¯] _bc_ + _β_[¯] _c[⊤][x]_[),][and][sample] _[Y]_[from][P][(] _[Y]_[=] _[c][|][X]_[=] _[x]_[)][=] � _Cc[′]_ ex=1p[exp] _{ηc[{]_ ( _x[η][c]_ ) _[′] }_[(] _[x]_[)] _[}]_[,] where _c ∈_ [ _C_ ]. In the `Covariate-and-concept-shift` suite, we follow the linear concept-shift mechanism with fixed _τ_ = 2 _._ 5, while retaining the mean-shifted covariates described above. Specifically, for each source iid _k_ , we draw _uk ∼_ Unif([ _−_ 1 _,_ 1]) and set _ξk_ = _τ_ (1 + 0 _._ 25 _τuk_ ). We also draw source-specific intercepts _bkc ∼N_ (0 _,_ (0 _._ 4 _τ_ )[2] ) and perturb the slopes via _βkc_ = _β_[¯] _c_ + _τ_ ∆ _kc_ , where (∆ _kc_ ) _j ∼N_ (0 _,_ 0 _._ 15[2] ) for _j ∈ I_ and (∆ _kc_ ) _j_ = 0 otherwise. Given _x_ from source _k_ , we compute _ηkc_ ( _x_ ) = _ξk_ ( _bkc_ + _βkc[⊤][x]_[)][and][sample] _[Y]_[according] to the multinomial probabilities P ( _Y_ = _c | X_ = _x,_ source = _k_ ) = _C_ exp _{ηkc_ ( _x_ ) _}_[where] _[c][ ∈]_[[] _[C]_[].] � _c[′]_ =1[exp] _[{][η][kc][′]_[(] _[x]_[)] _[}]_[,] 

**Method implementations.** The first three methods are implemented as in Section 5.2, while the `MDCP-tuned` variant additionally uses the hyperparameter _γ_ for the penalty in the _λ_ -optimization objective and follows the definitions and tuning procedures in Appendix D.1. 

**Simulation results.** Figure 20 presents the results of the covariate-shift simulation in the classification setting. As the heterogeneity induced by the covariates across sources increases with the parameter _δX_ , MDCP maintains tight worst-case coverage, whereas the `Baseline-agg` method conservatively drives both the overall and worst-case coverage metrics to 1.0. MDCP also exhibits a more stable trajectory for the average set size (i.e., a smaller slope) compared with the baseline methods, while `Baseline-agg` shows a more rapid increase in average set size and a larger standard deviation at the same time. 

Figure 21 presents the simulation results under the classification setting when both covariate shift and concept shift are present. MDCP remains robust, achieving tight worst-case coverage on average. It also maintains stability across different values of _δX_ , yielding a relatively flat average set size curve, whereas `Baseline-agg` degrades gradually as _δX_ increases. 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0043-06.png)


**----- Start of picture text -----**<br>
Baseline agg Baseline src 0 Baseline src 1 Baseline src 2 MDCP MDCP tuned<br>Overall coverage Worst-case coverage Avg set size<br>1.0 1.0<br>6<br>0.9 0.8<br>4<br>0.8 0.6<br>0.7 0.4 2<br>0.6 0.2<br>0 0.5 1.5 2.5 3.5 4.5 0 0.5 1.5 2.5 3.5 4.5 0 0.5 1.5 2.5 3.5 4.5<br>Shift magnitude Shift magnitude Shift magnitude<br>**----- End of picture text -----**<br>


Figure 20: Performance of MDCP and baselines in the classification `Covariate-shift` experiments. The x-axis is the covariate-shift magnitude _δX_ , which determines _PX_[(] _[k]_[)] separation while keeping _P_ ( _Y | X_ ) fixed. Each line reports the mean over _N_ = 100 runs, and the shaded region indicates _±_ 1 standard deviation across runs. Left: coverage over all test data. Middle: worst-case coverage over single-source test data. Right: average set size over all test data. 

## **D.2.2 Additional simulations in regression settings** 

**Data generating processes.** For regression, we use a linear Gaussian model _Y_ = _β[⊤] X_ + _b_ + _ε, ε ∼ N_ (0 _, σ_[2] ). In each run, we randomly sample a signal-to-noise ratio from Unif([5 _,_ 10]), and achieve it by 

43 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0044-00.png)


**----- Start of picture text -----**<br>
Baseline agg Baseline src 0 Baseline src 1 Baseline src 2 MDCP MDCP tuned<br>Overall coverage Worst-case coverage Avg set size<br>1.0 1.0<br>6<br>0.9 0.8<br>0.8 0.6 4<br>0.7 0.4<br>2<br>0.6 0.2<br>0 0.5 1.5 2.5 3.5 4.5 0 0.5 1.5 2.5 3.5 4.5 0 0.5 1.5 2.5 3.5 4.5<br>Shift magnitude Shift magnitude Shift magnitude<br>**----- End of picture text -----**<br>


Figure 21: Performance of MDCP and baselines in the classification `Covariate-and-concept-shift` experiments. The x-axis is the covariate shift magnitude _δX_ , with both _PX_[(] _[k]_[)] and _P_[(] _[k]_[)] ( _Y | X_ ) varying across sources. Each line reports the mean over _N_ = 100 runs, and the shaded region indicates _±_ 1 standard deviation. Left: coverage over all test data. Middle: worst-case coverage over single-source test data. Right: average set size over all test data. 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0044-02.png)


**----- Start of picture text -----**<br>
Baseline agg Baseline src 0 Baseline src 1 Baseline src 2 MDCP MDCP tuned<br>Overall coverage Worst-case coverage Avg interval width<br>1.0 1.0 12.5<br>0.9 0.8 10.0<br>7.5<br>0.8<br>0.6<br>5.0<br>0.7<br>0.4<br>2.5<br>0.6<br>0 0.5 1.5 2.5 3.5 4.5 0 0.5 1.5 2.5 3.5 4.5 0 0.5 1.5 2.5 3.5 4.5<br>Shift magnitude Shift magnitude Shift magnitude<br>**----- End of picture text -----**<br>


Figure 22: Evaluation with regression `Covariate-shift` suites; details are otherwise the same as in Figure 20. 


![](markdown_output/multi-distribution-robust-cp-2026_images/multi-distribution-robust-cp-2026.pdf-0044-04.png)


**----- Start of picture text -----**<br>
Baseline agg Baseline src 0 Baseline src 1 Baseline src 2 MDCP MDCP tuned<br>Overall coverage Worst-case coverage Avg interval width<br>12.5<br>0.9 0.8<br>10.0<br>0.8<br>0.6 7.5<br>0.7<br>5.0<br>0.4<br>0.6<br>2.5<br>0 0.5 1.5 2.5 3.5 4.5 0 0.5 1.5 2.5 3.5 4.5 0 0.5 1.5 2.5 3.5 4.5<br>Shift magnitude Shift magnitude Shift magnitude<br>**----- End of picture text -----**<br>


Figure 23: Evaluation with regression `Covariate-and-concept-shift` suites; details are otherwise the same as in Figure 21. 

44 

adjusting the noise variance _σk_[2][.] 

In the `Covariate-shift` suite, _P_ ( _Y | X_ ) is shared across sources and the noise level is also shared. We draw a shared slope vector _β_[¯] _∈_ R _[d]_ with _β_[¯] _j ∼N_ (0 _,_ 1) for _j ∈ I_ and _β_[¯] _j_ = 0 otherwise, and a shared intercept[¯] _b ∼N_ (0 _,_ 0 _._ 5[2] ). To enforce common noise, we compute _σ_[2] once using the realized covariates from source 1, and reuse this _σ_[2] for all sources. We then generate, for each source _k_ , _Yi_[(] _[k]_[)] = _β_[¯] _[⊤] Xi_[(] _[k]_[)] +[¯] _b_ + _ε_[(] _i[k]_[)] , iid where _ε_[(] _i[k]_[)] _∼N_ (0 _, σ_[2] ). In the `Covariate-and-concept-shift` suite, we introduce source-specific regression functions and calibrate noise per source. We draw a base slope _β_[¯] _∈_ R _[d]_ supported on _I_ same as the `Covariate-shift` suite, and a base intercept _b ∼N_ (0 _,_ 0 _._ 5[2] ). For each source _k_ , we sample _δk ∈_ R _[d]_ supported on _I_ with ( _δk_ ) _j ∼N_ (0 _,_ 1) for _j ∈ I_ and 0 otherwise, and set _βk_ = _β_[¯] + 0 _._ 2 _τ δk_ , _bk_ = _b_ + _τvk_ , iid _vk ∼N_ (0 _,_ 0 _._ 5[2] ). We then compute _σk_[2][,][and][sample] _[Y] i_[(] _[k]_[)] = _βk[⊤][X] i_[(] _[k]_[)] + _bk_ + _ε_[(] _i[k]_[)] , where _ε_[(] _i[k]_[)] _∼N_ (0 _, σk_[2][).] 

**Method implementations.** The first three methods are implemented exactly as in Section 5.3. The `MDCP-tuned` variant further introduces a hyperparameter _γ_ to control the penalty in the _λ_ -optimization objective and adheres to the definitions and tuning procedures specified in Appendix D.1. 

**Simulation results.** The evaluation results for the `Covariate-shift` suite under the regression setting are shown in Figure 22. MDCP achieves tight worst-case coverage, while the performance of individual sources steadily degrades as _δX_ increases, as expected. The average interval width of MDCP consistently stays below that of `Baseline-agg` , although the MDCP curve gradually increases and tends to be get closer with `Baseline-agg` . This behavior is also expected: as _δX_ , which approximately controls the separation among sources, continues to grow, in the extreme case where sources become perfectly separated, the optimal strategy is to optimize the per-source interval widths, and the efficiency gains from leveraging information across multiple sources become minimal. 

The evaluation results for the `Covariate-and-concept-shift` suite under the regression setting are shown in Figure 23. Again, MDCP achieves tight worst-case coverage, while both the overall and worst-case coverage of the per-source-calibrated methods `Baseline-src-` _k_ continually degrade. As explained earlier, the MDCP curve also tends to approach that of `Baseline-agg` as the shift magnitude increases. 

45 

