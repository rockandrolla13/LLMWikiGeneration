Proceedings of Machine Learning Research 266:1–48, 2025 Conformal and Probabilistic Prediction with Applications 

## **Dynamic Conformal Prediction for Multi-Target Regression: Optimising Informational Efficiency under Joint Validity** 

**Filip Schlembach** filip.schlembach@maastrichtuniversity.nl **Evgueni Smirnov** smirnov@maastrichtuniversity.nl **Mark H. M. Winands** m.winands@maastrichtuniversity.nl _Department of Advanced Computing Sciences, Maastricht University, Maastricht, The Netherlands_ 

**Editor:** Khuong An Nguyen, Zhiyuan Luo, Harris Papadopoulos, Tuwe L¨ofstr¨om, Lars Carlsson and Henrik Bostr¨om 

## **Abstract** 

Inductive conformal prediction equips point regressors with finite-sample prediction sets that provably contain the unknown label with prescribed probability. For multi-target regression, joint coverage across all output dimensions can be guaranteed by combining one-dimensional conformal predictors, one for each output dimension, resulting in an axisaligned hyperrectangular prediction region. The validity and informational efficiency of these hyperrectangular prediction regions depend on the choice of the targeted error rate for the individual one-dimensional conformal predictors. We cast this choice as an errorbudget allocation problem and introduce Dynamic Conformal Prediction for Multi-Target Regression (DCP-MT), a method that finds the budget allocation which minimises the hyperrectangles’ volumes while retaining joint coverage under exchangeability. Experiments on synthetic and real-world data sets demonstrate that DCP-MT reduces hyperrectangle volumes compared to state-of-the-art methods when nonconformity scores’ correlations across target dimensions are weak or heterogeneous, while maintaining the nominal coverage. The proposed method thus offers a simple, drop-in solution for existing multi-target regression pipelines. 

**Keywords:** Inductive conformal prediction, multi-target regression, hyperrectangular prediction regions, multiple hypothesis testing, uncertainty quantification. 

## **1. Introduction** 

The reliability of machine-learning methods increasingly hinges on their ability not only to predict accurately but also to quantify the uncertainty associated with every prediction. _Conformal prediction_ (CP) has emerged as a distribution-free, model agnostic framework that provides prediction regions for point forecasts with finite-sample validity guarantees (Vovk et al., 2005). While applying CP to single-target regression is straightforward, many real-world tasks require multi-target regression (Neeven and Smirnov, 2018). In this setting, practitioners need a joint prediction region that covers all label dimensions simultaneously with a prescribed error rate. Maintaining this joint validity while minimising the prediction region’s volume is a challenging problem. 

Various methods have been proposed to apply CP to multi-target regression problems (Vovk, 2013; Stankeviˇci¯ut˙e et al., 2021; Messoudi et al., 2021, 2022; Schlembach et al., 2022, 2025; Feldman et al., 2023; Ajroldi et al., 2023; Diquigiovanni et al., 2024), producing prediction regions of different shapes. In this article, we focus on CP variants that generate axis-aligned hyperrectangular prediction regions because (i) they retain the intuitive pertarget interpretation of classic one-dimensional intervals making them explainable and easily 

© 2025 F. Schlembach, E. Smirnov & M.H.M. Winands. 

Schlembach Smirnov Winands 

interpretable in human-in-the-loop workflows, (ii) they provide individual guarantees on each dimension, and (iii) they integrate seamlessly into tabular decision rules or rule-based post-processing pipelines. 

Current methods that produce hyperrectangular prediction regions do this by combining multiple conformal predictors, one for each dimension of the label space, and assign all of them the same targeted error rate. Two approaches exist to determine the common targeted error rate. The first splits the global targeted error rate evenly, applying Bonferroni (Vovk, 2013) or Sid´ak corrections ([ˇ] Messoudi et al., 2021), which are often overly conservative. The second exploits the correlation between the output’s dimensions (Messoudi et al., 2021; Timans et al., 2025), which is efficient when there is a strong positive correlation across targets. To improve the prediction region’s informational efficiency[1] when there is no or weak correlation across the output’s dimensions, we investigate how to set the targeted error rate for the individual single-target conformal predictors to minimise the hyperrectangular prediction region’s volume. 

Our contributions are fourfold: 

- We formulate the choice of the local targeted error rates for the individual single-target conformal predictors as a global error-budget allocation problem and prove that joint validity is guaranteed whenever the sum of the local targeted error rates does not exceed the global targeted error rate. 

- Building on this insight, we introduce _Dynamic Conformal Prediction for Multi-Target Regression_ (DCP-MT), an approach that finds the budget allocation, which minimises the hyperrectangle’s volume without distributional assumptions using integer linear programming. 

- We provide a theoretical analysis comparing DCP-MT to related state-of-the-art methods producing hyperrectangular prediction regions. 

- Extensive experiments on synthetic and public real-world data sets demonstrate that DCP-MT improves hyperrectangle volume compared to state-of-the-art methods when nonconformity scores’ correlations across target dimensions are weak and have different marginal distributions, while maintaining the nominal coverage. 

The remainder of this article is structured as follows. Section 2 discusses inductive CP for multi-target regression and highlights the difficulties of extending single-target CP to multi-target regression. Section 3 surveys existing work on applying CP in the multitarget regression setting, focussing on methods that produce axis-aligned hyperrectangular prediction regions. Our method DCP-MT is proposed in Section 4, where we prove its validity and discuss implementation details. Section 6 reports experimental results, and Section 7 discusses the findings and compares DCP-MT to related methods. Section 8 provides the conclusions and future research directions. Additional experimental details are given in the Appendix. 

> 1. We use the term _informational efficiency_ as a synonym for the _efficiency_ of prediction sets, referring to their size, as introduced by Vovk et al. (2005, p.9). This is done to clearly distinguish informational efficiency from computational efficiency. 

2 

Dynamic Conformal Prediction for Multi-Target Regression 

## **2. Inductive Conformal Prediction for Multi-Target Regression** 

In this section, we introduce the general concepts and associated notation used in this article in two parts. First, Subsection 2.1 recapitulates multi-target regression. Second, Subsection 2.2 describes inductive conformal prediction (ICP) in generic terms, how it is applied to single-target regression problems and then shows how and why extending ICP to the multi-target setting is non-trivial. 

## **2.1. Multi-Target Regression** 

Let **X** _⊆_ R _[L]_ be the object space and **Y** _⊆_ R _[M]_ the _M_ -dimensional label space. We are given a sample of _N_ pairs _{_ ( **x**[(] _[n]_[)] _,_ **y**[(] _[n]_[)] ) _}[N] n_ =1 _[∼P]_ **[X]** _[,]_ **[Y]**[,][drawn][from][an][arbitrary][probability] distribution _P_ **X** _,_ **Y** , where each label **y**[(] _[n]_[)] = ( _y_ 1[(] _[n]_[)] _[, . . . , y] M_[(] _[n]_[)][)] _[⊤]_[contains] _[M]_[real-valued][targets] observed simultaneously with the object **x**[(] _[n]_[)] _∈_ **X** . A _multi-target regressor_ is any learning ˆalgorithm **f** ( **x** ) = **ˆy** . The fitted model ˆthat, after training **f** is a point estimator which produces an estimate of the labelon the sample, returns a fitted model[ˆ] **f** : **X** _−→_ **Y** _,_ **x** _�→_ **ˆy** for a given object **x** . We drop the superscript ( _n_ ) whenever the context is clear and denote generic observations simply by ( **x** _,_ **y** ). 

## **2.2. Inductive Conformal Prediction** 

In the regression setting, inductive conformal prediction (ICP) turns any point estimator into a _set-valued_ predictor that satisfies a finite-sample coverage guarantee under two assumptions. First, the examples are exchangeable, and second, the learning algorithm treats them symmetrically, i.e. the model fitting algorithm produces the same model[2] independently of the order of the examples in the training set (Barber et al., 2022). We summarise the generic construction in a way that is agnostic to the output dimension _M_ . The mechanism is the same whether **Y** _⊆_ R or **Y** _⊆_ R _[M]_ . 

Given a sample _D_ = �( **x**[(] _[n]_[)] _,_ **y**[(] _[n]_[)] )� _[N] n_ =1[of] _[N]_[examples,][randomly][split][it][into][a] _[proper] training set D_ tr = �( **x**[(] _[n]_[)] _,_ **y**[(] _[n]_[)] )� _[N] n_ =1[tr][of size] _[ N]_[tr][ and a] _[ calibration set][D]_[cal][=][ �][(] **[x]**[(] _[n]_[)] _[,]_ **[ y]**[(] _[n]_[)][)][�] _[N] n_ = _N_ tr+1 of size _N_ cal = _N − N_ tr. Next, fit a model on _D_ tr and obtain a point predictor[ˆ] **f** : **X** _→_ **Y** _,_ **x** _�→_[ˆ] **f** ( **x** ) = **y** ˆ. 

A _nonconformity measure_ (NCM) is a measurable function 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0003-09.png)


that assigns a _single scalar_ to the example ( **x** _,_ **y** ). The NCM estimates how different any joint observation ( **x** _,_ **y** ) is from the examples in _D_ tr (Vovk et al., 2005). 

Use an NCM to compute the nonconformity scores _α_[(] _[n]_[)] = _A_ �( **x**[(] _[n]_[)] _,_ **y**[(] _[n]_[)] ) _,_[ˆ] **f** � for each joint observation in the calibration set _D_ cal. Now let _α_ (1 _−ϵ_ ) = Q1 _−ϵ_ ( _{α_[(] _[n]_[)] _}[N] n_ = _N_ tr+1[)][be][the] empirical (1 _−ϵ_ ) quantile of _{α_[(] _[n]_[)] _}[N] n_ = _N_ tr+1[.][Q][1] _[−][ϵ]_[ denotes the quantile function which returns] the _⌈_ (1 _− ϵ_ )( _N_ cal + 1) _⌉_ th smallest value of the computed nonconformity scores. 

Finally, for a new object **x**[(] _[N]_[+1)] _∈_ **X** , define the prediction region 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0003-13.png)


> 2. The model fitting algorithm needs to produce models with the same distribution for randomized algorithms. 

3 

Schlembach Smirnov Winands 

Any Γ _[ϵ]_ constructed in such a way is called an _inductive conformal predictor_ . Inductive conformal predictors are conservatively valid meaning that 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0004-02.png)


regardless of the distribution of ( **X** _,_ **Y** ) and of the form of _A_ (Vovk et al., 2005). We call _ϵ_ the targeted error rate and say that an error occurs when **y**[(] _[N]_[+1)] _∈/_ Γ _[ϵ]_ ( **x**[(] _[N]_[+1)] ). 

For a more in-depth overview of conformal prediction, please refer to (Vovk et al., 2005; Toccaceli, 2022; Fontana et al., 2023). Angelopoulos and Bates (2022) provide an excellent hands-on introduction to conformal prediction. 

For single-target regression problems, a classic NCM is the absolute residual _α_[(] _[n]_[)] = ˆ _|y_[(] _[n]_[)] _− y_[(] _[n]_[)] _|_ . Using absolute residuals as the NCM produces the prediction region 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0004-06.png)


ˆ which takes the form of an interval centred around _y_ . When using absolute residuals as the NCM, the inductive conformal predictor Γ _[ϵ]_ assigns all test points intervals of the same size equal to 2 _α_ (1 _−ϵ_ ) (Papadopoulos et al., 2002). There exist more complex nonconformity measures for single-target regression, an example of which are normalized nonconformity measures (Papadopoulos et al., 2002; Papadopoulos and Haralambous, 2011). 

We classify approaches applying conformal prediction to multi-target regression into two main groups:[3] _single-test_ methods and _multi-tests_ methods. This classification stems from observing conformal prediction through a hypothesis testing lens (Vovk et al., 2005; Timans et al., 2025). Given a candidate label **y** ¯ for an object **x** , a conformal predictor as defined in (2) tests whether it should be included in the prediction region. 

Single-test methods employ an NCM _A_ : **X** _×_ **Y** _→_ R, with **Y** _⊆_ R _[M]_ , which assigns a single nonconformity score to any pair ( **x** _,_ **y** ). The single test for inclusion can then be performed by comparing the nonconformity score to the threshold _α_ 1 _−ϵ_ provided by the quantile function. A simple examples of such an NCM is the Euclidean norm _α_ = _∥_ **y** ˆ _−_ **y** _∥_ which leads to a hyperspherical prediction region. Johnstone and Cox (2021); Messoudi et al. (2022); Dheur et al. (2025) present examples of NCMs producing prediction regions with more complex shapes. These methods can exploit rich dependence structures but the prediction regions’ complex shapes make them difficult to interpret and therefore less attractive in human-in-the-loop scenarios. We mention them here for completeness but focus on multi-tests methods for the remainder of this article. 

Multi-tests methods, on which we focus for the remainder of this article, combine _M_ single-target conformal predictors _{_ Γ _[ϵ] m[m][}][M] m_ =1[,][one][for][each][dimension] _[m]_[of][the][label][space,] into a single Γ _[ϵ]_ . These conformal predictors employ an NCM _A_ : **X** _×_ R _→_ R which provides nonconformity scores for the associated dimension. The test for inclusion of a candidate label **y** ¯ is therefore performed _M_ times in parallel. Timans et al. (2025) provide a rigorous theoretical analysis relating the combination of multiple conformal predictors for multi-target regression to multiple hypothesis testing. 

> 3. Ajroldi et al. (2023); Diquigiovanni et al. (2024) present a related third approach, building upon functional data analysis which is not directly applicable to point forecasts. 

4 

Dynamic Conformal Prediction for Multi-Target Regression 

The prediction region of multi-tests methods is the Cartesian product of the _M_ onedimensional intervals constructed by the Γ _[ϵ] m[m]_[and][therefore][of][hyperrectangular][shape.][4] Prediction regions constructed in this way have the benefit that the sides of the hyperrectangle are parallel to the axes of the label space. They also provide individual coverage guarantees for each dimension of the label space. For any label **y** to be considered inside the prediction region, all of its components _{ym}[M] m_ =1[need to be contained within the prediction] interval associated with their dimension _m_ . Hence, we can write validity, as defined in (3), for multi-tests methods as 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0005-02.png)


where Γ _[ϵ]_ ( **x**[(] _[N]_[+1)] ) is the hyperrectangular prediction region with a global targeted error rate _ϵh_ and Γ _[ϵ] m[m]_[(] **[x]**[(] _[N]_[+1)][)][is][the][prediction][interval][for][dimension] _[m]_[with][a][local][targeted][error] rate _ϵm_ (Timans et al., 2025). To avoid confusion _ϵh_ = _ϵ_ denotes the global error rate moving forward. 

The challenge in the design of multi-tests methods lies in the choice of the local targeted error rates _ϵm_ . They need to be chosen in such a way, that the method is valid as described in (5). Next to validity, _informational efficiency_ is a desired property for conformal predictors, meaning that the generated prediction region should be non-empty and as small as possible (Vovk et al., 2005). Exhaustively searching for a valid prediction region of minimal size is computationally inefficient because the quantile function each Γ _[ϵ] m[m]_[uses][can][return] _N_ + 1 different values, leading to ( _N_ + 1) _[M]_ combinations that need to be tested (Vovk, 2013). The following section describes a number of methods that have been devised to reduce this computational cost. 

## **3. Related Work** 

Vovk (2013) propose the first computationally efficient multi-tests method called _Bonferroni predictors_ . A Bonferroni predictor assigns the same value _ϵm_ = _ϵh/M_ to all local significance levels. Its name and the choice for _ϵm_ stem from the Bonferroni family-wise error rate (FWER) correction method. The validity of Bonferroni predictors is directly derived from Boole’s inequality. While Vovk (2013) introduces the method initially for transductive conformal predictors, which do not rely on a separate calibration set, it has subsequently been applied to ICP (Stankeviˇci¯ut˙e et al., 2021; Schlembach et al., 2022, 2025; Vovk et al., 2022). These applications show that Bonferroni predictors are generally too conservative, producing prediction regions that are larger than necessary for the targeted global error rate _ϵh_ . 

To improve the informational efficiency of the prediction regions, Messoudi et al. (2021) try to capture the dependencies across the nonconformity scores’ dimensions by fitting copulas (Sklar, 1959) to them. Messoudi et al. (2021) test three copulas. The independent 

> 4. It is possible to envision NCMs for single-target conformal predictors that do not lead to prediction regions that take the form of a single continuous interval. In our experience, they are uncommon in practice and their discussion is omitted in this article. 

5 

Schlembach Smirnov Winands 

copula is equivalent to the Sid´ak FWER correction and sets[ˇ] _ϵm_ = 1 _−_ (1 _− ϵh_ )[1] _[/M]_ , assuming independence between the nonconformity scores. It is less conservative than the Bonferroni predictors but makes independence assumptions about the nonconformity scores’ distributions that are not always met. The use of the Gumbel copula results in setting _ϵm_ = 1 _−_ (1 _− ϵh_ )[1] _[/][√][θ] M_ , where _θ_ is a parameter in the copula’s generator function that Messoudi et al. (2021) estimate using the matrix of nonconformity scores and the Maximum Pseudo-Likelihood Estimator. For _θ_ = 1 the Gumbel copula is equivalent to the independent copula. For larger values of _θ_ , it results in an even less conservative FWER correction that is justified if there is positive correlation between the nonconformity scores of the dimensions of the label space. The empirical copula estimates the cumulative distribution function (CDF) [0 _,_ 1] _[M] →_ [0 _,_ 1] which, given the _M_ local targeted error rates _ϵm_ , can be used to compute the global targeted error rate _ϵh_ . Because there is no analytical expression for the inverse of this CDF, searching for an optimal solution leads to the same computational cost as described at the end of Subsection 2.2. For this reason Messoudi et al. (2021) only search the subspace where all _ϵm_ have the same value, allowing for a simple dichotomic search. 

Timans et al. (2025) propose `Max-Rank` , a method that is informationally efficient when the nonconformity scores in the dimensions of the label space are positively correlated. `Max-Rank` first computes the rank for all nonconformity scores _{_ rank( _αm_[(] _[n]_[)][)] _[}][N] n_ = _N_ tr+1[for each] dimension _m_ in the label space. It then computes the max( _{_ rank( _αm_[(] _[n]_[)][)] _[M] m_ =1 _[}]_[) over all dimen-] sions for each element in the calibration set. Finally, applying the quantile function Q1 _−ϵh_ to the list of max ranks returns the rank _r_ 1 _−ϵh_ which is used to compute the local targeted error rates _ϵm_ = _r_ 1 _−ϵh/_ ( _N_ cal + 1). In practice, the _ϵm_ do not need to be computed, as _r_ 1 _−ϵh_ can directly be used to determine the empirical (1 _− ϵm_ ) quantile for each dimension.[5] 

The copula conformal predictors and Max-Rank are computationally and informationally efficient, performing as well as Bonferroni predictors in the worst case scenarios. All methods presented in this section assign the same local targeted error _ϵm_ to all dimensions. In situations where the nonconformity scores are weakly correlated across the nonconformity scores’ dimensions and when their marginal distributions differ, identical _ϵm_ s will not produce optimal solutions. To solve this, we propose a new method in the following section. 

## **4. Dynamic Conformal Prediction for Multi-Target Regression (DCP-MT)** 

We now present _Dynamic Conformal Prediction for Multi-Target Regression_ (DCP-MT), a method that can assign different local targeted error rates to different dimensions in order to minimise the prediction region’s volume. A sufficient condition for the validity of any such method is presented in Theorem 1. 

**Theorem 1** _Let ϵh be the global targeted error rate for a multi-tests conformal predictor and let {ϵm}[M] m_ =1 _[be][the][local][error][rates][associated][with][each][dimension][of][the][label][space.]_ 

> 5. For `Max-Rank` the distinction between single-test methods and multi-tests methods becomes ambiguous, as the computed max rank for each element in the calibration set could be interpreted as the nonconformity scores, collapsing the method to a single test. 

6 

Dynamic Conformal Prediction for Multi-Target Regression 

_A multi-tests conformal predictor is valid, if_ 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0007-02.png)


**Proof** The result is derived by applying Boole’s inequality to (5) 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0007-04.png)


which can be rewritten as (6). 

Equation (6) shows that for a multi-tests method to be valid, it is sufficient that the sum of the local targeted error rates _ϵm_ does not exceed the global targeted error rate _ϵh_ . We can therefore interpret the global targeted error rate as a global error budget. DCP-MT solves the problem of optimally allocating the global error budget _ϵh_ between the _M_ dimensions of the label space to minimise the volume of the resulting hyperrectangular prediction region. The volume of the prediction region is given by[�] _[M] m_ =1[2][Q][1] _[−][ϵ] m_[(] _[{][α]_[(] _[m,n]_[)] _[}][N] n_ = _N_ tr+1[) where] _{α_[(] _[m,n]_[)] _}[N] n_ = _N_ tr+1[are all nonconformity scores associated with dimension] _[ m]_[.][Minimising this] product with respect to the _ϵm_ is equivalent to minimising the sum 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0007-07.png)


To find the minimum, DCP-MT first sorts the nonconformity scores for each dimension, such that _αm[′]_[(1)] _≤ αm[′]_[(2)] _≤· · · ≤ αm[′]_[(] _[N]_[cal][)] _, ∀n ∈{_ 1 _, . . . , N }_ , where _αm[′]_[(] _[n]_[)] is a sorted nonconformity score with the associated local targeted error rate _ϵ_[(] _m[n]_[)][= 1] _[ −][n/]_[(] _[N]_ cal[+ 1).][Let] _[ I] m_[(] _[n]_[)] _[∈{]_[0] _[,]_[1] _[}]_ be a binary variable indicating the choice of _ϵ_[(] _m[n]_[)][as the local targeted error rate for dimension] _m_ . Finding the optimal allocation of the error budget is then equivalent to minimising the cost function 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0007-09.png)


under the constraints 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0007-11.png)


and 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0007-13.png)


7 

Schlembach Smirnov Winands 

Minimising the cost function (9) directly minimises the volume of the hyperrectangular prediction region as shown in (8). The transformation of the volume from a product into a sum is necessary to solve the problem via a standard mixed-integer linear programming (MILP) solver. Constraint (10) ensures validity while the constraints in (11) ensure that only one targeted error rate is chosen per dimension. 

An MILP formulation fits this optimization problem because the choice of local significance levels _em_ is equivalent to selecting one quantile from the discrete, finite set of nonconformity scores for each dimension _m_ . These choices are represented by binary indicator variables _Im_[(] _[n]_[)][,][which][introduce][integer][constraints][into][the][optimization.][At][the] same time, the objective, which consists in minimizing the volume of the hyperrectangular prediction region, can be expressed as a sum of logarithms of the selected quantiles, and hence, as a linear function over the indicator variables. The MILP formulation enables us to efficiently explore this combinatorial space and find a globally optimal allocation of the error budget that respects the validity constraint in Equation (10). 

In practice, DCP-MT is used by following the ICP procedure laid out in Section 2.2. First, a training algorithm fits the underlying model to the proper training set. Next, the individual inductive conformal predictors are calibrated on the calibration set, each on the nonconformity scores of their associated dimension. Finally, during inference, the hyperrectangular prediction region is built for each new object by solving the MILP optimisation problem presented in this section. 

## **5. Comparison** 

This section discusses the theoretical results, comparing DCP-MT to Bonferroni predictors, copula conformal predictors, and Max-Rank. 

In multi-target conformal prediction, guaranteeing joint coverage across all outputs is essential, but doing so efficiently is challenging. Among multi-tests methods, Bonferroni prdictors (Vovk, 2013) provide FWER control by allocating the total significance level equally among targets, but they are highly conservative, resulting in unnecessarily wide prediction intervals. More sophisticated methods like copula conformal predictors (Messoudi et al., 2021; Sun and Yu, 2024) and Max-Rank (Timans et al., 2025) attempt to exploit dependencies between the dimensions’ nonconformity scores. Copula-based methods explicitly model joint distributions, while Max-Rank leverages positive dependence using ranks. These methods are most efficient when outputs are strongly positively dependent and assign the same local significance levels _ϵm_ to all targets. In the presence of positive dependencies between the dimensions’ nonconformity scores copula conformal predictors and Max-Rank can violate the constraint (10) imposed by Boole’s inequality while still maintaining theoretical validity guarantees. 

DCP-MT offers a different approach. While it does not model output dependencies explicitly, it dynamically adjusts the local significance levels _ϵm_ subject to constraint (10) imposed by Boole’s inequality to decrease the volume of the predicted region. Therefore, DCP-MT achieves smaller prediction regions when the dimensions’ nonconformity scores are weakly correlated and have different marginal distributions. 

Once the local targeted error rates _ϵm_ have been determined, all methods select the associated nonconformity score from the calibration set for each dimension using the quantile 

8 

Dynamic Conformal Prediction for Multi-Target Regression 

function or the rank in the case of Max-Rank. Therefore, the difference in computational complexity between the methods stems from the way the local targeted error rates _ϵm_ are determined. Bonferroni is the simplest method computationally, requiring only a simple division operation to compute the _ϵm_ . Max-Rank is a little more complex. First Max-Rank requires a pass through the calibration set’s nonconformity scores to compute the max rank. Then it applies the quantile function to the results and a single division operation to compute the _ϵm_ . Finding the optimal solution for copula conformal predictors using the empirical copula would be computationally prohibitive due to the lack of an analytical expression for the CDF’s inverse. Therefore, Messoudi et al. (2021) opted to assign all _ϵm_ the same value, restricting the search space. Because the empirical copula is monotonically increasing when the _ϵm_ are decreasing simultaneously, the largest value for the _ϵm_ that satisfies the global targeted error rate can then be determined through a simple search operation. DCP-MT requires solving a single convex optimization problem to distribute the global error budget efficiently and set the _ϵm_ . This is more efficient than finding a globally optimal hyperrectangle but remains computationally more complex than Bonferroni predictors, copula conformal predictors, and Max-Rank. 

## **6. Experiments** 

In this section, we examine the empirical performance of the DCP-MT method presented in Section 4 on simulated and real-world data sets and compare it to other multi-tests methods. For the comparison we chose Bonferroni predictors as a baseline and copula conformal predictors using the empirical copula as well as Max-Rank as they are the best performing methods in (Messoudi et al., 2021) and (Timans et al., 2025). The code to reproduce the experiments is available at `https://github.com/filipschlembach/dcp_mt` . 

Subsection 6.1 introduces the data sets. This is followed by the description of how the experiments are conducted and which underlying models we used in Subsection 6.2. We report the experimental results in Subsection 6.3. 

## **6.1. Data Sets** 

This section presents the synthetic and real-world data sets used to evaluate DCP-MT and to compare it to other multi-tests methods. 

**Synthetic data sets.** Inspired by Barber et al. (2022), the synthetic data sets used in this article have the structure 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0009-08.png)


where _A_ is a _M × L_ shaped matrix of randomly generated coefficients and _e_ is an added noise term. The data sets differ in the way the noise is generated. 

For the first data set _L_ = 5, _N_ = 2, and the noise term _e ∼_ [ _U_ ( _−_ 1 _,_ 1) _, χ_[2] 2[]] _[⊤]_[is made up of] two components that are sampled independently from a uniform and a Chi-squared distribution. This simulates a situation where the nonconformity scores are not correlated across the nonconformity scores’ dimensions and when their marginal distributions differ. For the second, third, and fourth data set, _L_ = 5, _N_ = 2, and the noise term _e ∼N_ ([0 _,_ 0] _[⊤] ,_ **σ** ) is sampled from a two-dimensional multivariate normal distribution, where **σ** is a 2 _×_ 2 matrix with values equalling 1 on the main diagonal and _σ_ otherwise. Setting _σ_ to 0, 0 _._ 5, and 1 for 

9 

Schlembach Smirnov Winands 

Table 1: Overview over the used real-world data sets. _N_ is the number of examples in the data set, _L_ = dim( **X** ), and _M_ = dim( **Y** ). 

|**Name**|_N_ **examples**|_L_|_M_|
|---|---|---|---|
|diabetes (Efron et al., 2004)|442|9|2|
|music origin (Zhou et al., 2014)|1059|68|2|
|rf1 (Tsoumakas et al., 2011)|9125|64|8|
|rf2 (Tsoumakas et al., 2011)|9125|576|8|
|scm1d (Tsoumakas et al., 2011)|9803|280|16|
|scm20d (Tsoumakas et al., 2011)|8966|61|16|



the data sets respectively controls the correlation between the noise term’s dimensions. We chose varying correlation to highlight the difference between DCP-MT, copula conformal predictors and Max-Rank, as copula conformal predictors and Max-Rank are expected to perform well for higher values of _σ_ . For each data set, we generate a sample containing 1000 examples. 

**Real-world data sets.** In addition to the experiments on synthetic data sets, we also apply DCP-MT and the methods presented in Section 3 to six real-world data sets shown in Table 1. For the diabetes data set we have chosen to predict features 3 and 4 as they are weakly correlated. Music origin (Zhou et al., 2014), rf1, rf2, scm1d, and scm20d (Tsoumakas et al., 2011) are taken from Messoudi et al. (2021) and Timans et al. (2025) tested Max-Rank on rf1, and scm1d. 

## **6.2. Experimental Setup** 

The experiments use a 5-fold cross validation scheme. The proper training set _D_ tr and calibration set _D_ cal contain 67% and 33% of the examples in the training folds, respectively. As described in Subsection 2.2 we fit an underlying model to the proper training set and calibrate the conformal predictors on the calibration set. The test fold serves to evaluate the model and the conformal prediction methods. Matching the data generating process, we use scikit-learn’s (Pedregosa et al., 2011) linear regressor as the underlying model for the synthetic data sets. For the diabetes (Efron et al., 2004) data set we employ XGBoost regressors as the underlying model which offer good performance at low computational cost. To maintain comparability, we preprocess the music origin (Zhou et al., 2014), rf1, rf2, scm1d, and scm20d (Tsoumakas et al., 2011) data sets following Messoudi et al. (2021). We also follow the lead of Messoudi et al. (2020) for the underlying model, using a neural network and replicating their architecture. All experiments are repeated 20 times. 

## **6.3. Experimental Results** 

In this section, we first present the results for the synthetic data set with _e ∼_ [ _U_ ( _−_ 1 _,_ 1) _, χ_[2] 2[]] _[⊤]_ in detail, as it highlights the situation for which DCP-MT was designed. We then provide a summary of the results for all synthetic and real-world data sets. Appendix A contains the 

10 

Dynamic Conformal Prediction for Multi-Target Regression 

Table 2: Multi-tests method’s mean error rates and standard deviations for the synthetic data set with _e ∼_ [ _U_ ( _−_ 1 _,_ 1) _, χ_[2] 2[]] _[⊤]_[.][Underlined][values][indicate][instances][for][which] the measured error rate exceeds the targeted error rate while bold values indicate that the method produced the smallest prediction region. 

|_ϵh_<br>**Bonferroni**|**DMT-CP**<br>**Empirical Copula**|**DMT-CP**<br>**Empirical Copula**||**Max-Rank**|
|---|---|---|---|---|
|0.05<br>0.049 ± 0.006<br>0.10<br>0.098 ± 0.008<br>0.15<br>0.140 ± 0.007<br>0.20<br>0.188 ± 0.009<br>0.25<br>0.235 ± 0.013<br>0.30<br>0.276 ± 0.010<br>0.35<br>0.322 ± 0.013<br>0.40<br>0.365 ± 0.013<br>0.45<br>0.401 ± 0.015<br>0.50<br>0.445 ± 0.014<br>0.55<br>0.478 ± 0.015<br>0.60<br>0.515 ± 0.011<br>0.65<br>0.551 ± 0.013<br>0.70<br>0.580 ± 0.013<br>0.75<br>0.612 ± 0.011<br>0.80<br>0.643 ± 0.009<br>0.85<br>0.671 ± 0.011<br>0.90<br>0.701 ± 0.010<br>0.95<br>0.722 ± 0.009|**0.052 ± 0.005**<br>**0.104 ± 0.008**<br>**0.154 ± 0.010**<br>**0.207 ± 0.011**<br>**0.253 ± 0.014**<br>**0.304 ± 0.013**<br>**0.349 ± 0.014**<br>**0.404 ± 0.014**<br>**0.455 ± 0.014**<br>**0.502 ± 0.012**<br>**0.550 ± 0.011**<br>**0.602 ± 0.011**<br>**0.649 ± 0.011**<br>**0.700 ± 0.009**<br>**0.750 ± 0.011**<br>**0.803 ± 0.009**<br>0.847 ± 0.009<br>0.895 ± 0.009<br>0.942 ± 0.009|0.051 ± 0.006<br>0.101 ± 0.009<br>0.148 ± 0.009<br>0.197 ± 0.010<br>0.250 ± 0.012<br>0.301 ± 0.013<br>0.351 ± 0.012<br>0.399 ± 0.015<br>0.448 ± 0.016<br>0.500 ± 0.016<br>0.552 ± 0.014<br>0.602 ± 0.014<br>0.652 ± 0.013<br>0.702 ± 0.013<br>0.751 ± 0.010<br>0.799 ± 0.010<br>0.849 ± 0.009<br>0.898 ± 0.010<br>0.949 ± 0.009|**0**|0.057 ± 0.007<br>0.104 ± 0.007<br>0.151 ± 0.010<br>0.203 ± 0.011<br>0.253 ± 0.012<br>0.303 ± 0.013<br>0.353 ± 0.012<br>0.404 ± 0.016<br>0.453 ± 0.016<br>0.502 ± 0.015<br>0.554 ± 0.014<br>0.607 ± 0.015<br>0.656 ± 0.013<br>0.706 ± 0.012<br>0.750 ± 0.010<br>0.802 ± 0.010<br>**.852 ± 0.010**<br>**.902 ± 0.009**<br>**.950 ± 0.008**|
||||**0**||
||||**0**||



Table 3: Multi-tests method’s mean hyperrectangle volumes for the synthetic data set with _e ∼_ [ _U_ ( _−_ 1 _,_ 1) _, χ_[2] 2[]] _[⊤]_[.][Bold][values][indicate][that][the][method][produced][the][smallest] prediction region while underlined values highlight instances for which the measured error rate exceeds the targeted error rate. 

|_ϵh_<br>**Bonferroni**|**DMT-CP**<br>**Empirical Copula**|**DMT-CP**<br>**Empirical Copula**||**Max-Rank**|
|---|---|---|---|---|
|0.05<br>0.374 ± 0.013<br>0.10<br>0.283 ± 0.010<br>0.15<br>0.233 ± 0.007<br>0.20<br>0.199 ± 0.006<br>0.25<br>0.175 ± 0.005<br>0.30<br>0.159 ± 0.004<br>0.35<br>0.141 ± 0.004<br>0.40<br>0.126 ± 0.004<br>0.45<br>0.114 ± 0.004<br>0.50<br>0.103 ± 0.003<br>0.55<br>0.094 ± 0.003<br>0.60<br>0.085 ± 0.003<br>0.65<br>0.077 ± 0.003<br>0.70<br>0.070 ± 0.003<br>0.75<br>0.063 ± 0.003<br>0.80<br>0.056 ± 0.002<br>0.85<br>0.050 ± 0.002<br>0.90<br>0.044 ± 0.002<br>0.95<br>0.040 ± 0.002|**0.323 ± 0.011**<br>**0.234 ± 0.007**<br>**0.194 ± 0.005**<br>**0.163 ± 0.005**<br>**0.142 ± 0.004**<br>**0.124 ± 0.004**<br>**0.109 ± 0.004**<br>**0.094 ± 0.004**<br>**0.080 ± 0.003**<br>**0.069 ± 0.003**<br>**0.060 ± 0.002**<br>**0.051 ± 0.002**<br>**0.043 ± 0.002**<br>**0.036 ± 0.001**<br>**0.030 ± 0.001**<br>**0.024 ± 0.001**<br>0.018 ± 0.001<br>0.013 ± 0.001<br>0.007 ± 0.001|0.369 ± 0.013<br>0.280 ± 0.011<br>0.226 ± 0.007<br>0.194 ± 0.006<br>0.169 ± 0.004<br>0.149 ± 0.004<br>0.131 ± 0.004<br>0.115 ± 0.004<br>0.102 ± 0.004<br>0.089 ± 0.003<br>0.077 ± 0.003<br>0.065 ± 0.003<br>0.054 ± 0.003<br>0.044 ± 0.002<br>0.034 ± 0.002<br>0.025 ± 0.002<br>0.017 ± 0.001<br>0.011 ± 0.001<br>0.006 ± 0.001|**0**|0.354 ± 0.011<br>0.276 ± 0.011<br>0.223 ± 0.007<br>0.190 ± 0.006<br>0.167 ± 0.004<br>0.148 ± 0.004<br>0.130 ± 0.004<br>0.114 ± 0.004<br>0.101 ± 0.004<br>0.088 ± 0.003<br>0.076 ± 0.003<br>0.064 ± 0.003<br>0.053 ± 0.003<br>0.043 ± 0.002<br>0.034 ± 0.002<br>0.025 ± 0.002<br>**.017 ± 0.001**<br>**.011 ± 0.001**<br>**.005 ± 0.001**|
||||**0**||
||||**0**||



11 

Schlembach Smirnov Winands 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0012-01.png)


**----- Start of picture text -----**<br>
( a ) Error rates ( b ) Volumes<br>**----- End of picture text -----**<br>


Figure 1: Multi-tests method’s mean error rates and volumes for the synthetic data set with _e ∼_ [ _U_ ( _−_ 1 _,_ 1) _, χ_[2] 2[]] _[⊤]_[over][20][repetitions.] 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0012-03.png)


**----- Start of picture text -----**<br>
( a ) Residuals ( b ) Residual correlation matrix<br>**----- End of picture text -----**<br>


Figure 2: Underlying model’s absolute residuals and their correlation for the synthetic data set with _e ∼_ [ _U_ ( _−_ 1 _,_ 1) _, χ_[2] 2[]] _[⊤]_[.] 

12 

Dynamic Conformal Prediction for Multi-Target Regression 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0013-01.png)


**----- Start of picture text -----**<br>
( a ) Bonferroni ( b ) DCP-MT<br>1.0<br>Test Residuals o. 0.4 Test<br>0. 80<br>c)><br>2 0.3<br>0.6 Q<br>YoO xN<br>= 0.2<br>0.45,<br>a<br>@ 0.1<br>0. 26<br>U)<br>0.0<br>o2 O38 o4 05 °° 00 Ol oO2 O38 04<br>n nh<br>( c ) Empirical Copula ( d ) Max-Rank<br>**----- End of picture text -----**<br>


Figure 3: Multi-tests method’s partition of the residual space for the synthetic data set with _e ∼_ [ _U_ ( _−_ 1 _,_ 1) _, χ_[2] 2[]] _[⊤]_[averaged][over][20][repetitions.] 

13 

Schlembach Smirnov Winands 

Table 4: Error rates acoss all experiments for _ϵh_ = 0 _._ 05. Bold values indicate that the method produced the smallest prediction region while underlined values highlight instances for which the measured error rate _≥_ 0 _._ 05. 

|**Data Set**<br>**Bonferroni**|**DMT-CP**<br>**Empirical Copula**|**DMT-CP**<br>**Empirical Copula**||**Max-Rank**|
|---|---|---|---|---|
|synt, _e ∼_[_U_(_−_1_,_1)_, χ_2<br>2]_⊤_<br>0.049 ± 0.006<br>synt, _e ∼N_(**0**_,_**σ**), _σ_ = 0<br>0.045 ± 0.006<br>synt, _e ∼N_(**0**_,_**σ**), _σ_ = 0_._5<br>0.043 ± 0.004<br>synt, _e ∼N_(**0**_,_**σ**), _σ_ = 1<br>0.023 ± 0.005<br>synt, _e ∼N_(**0**_,_**σ**), _σ_ = _−_0_._5<br>0.043 ± 0.004<br>diabetes<br>0.035 ± 0.011<br>music origin<br>0.042 ± 0.007<br>rf1<br>0.037 ± 0.002<br>rf2<br>0.037 ± 0.002<br>scm1d<br>0.021 ± 0.001<br>scm20d<br>0.021 ± 0.002|**0.052 ± 0.005**<br>**0.054 ± 0.008**<br>**0.052 ± 0.005**<br>0.035 ± 0.005<br>**0**<br>**0.054 ± 0.006**<br>0.049 ± 0.013<br>**0.047 ± 0.008**<br>0.037 ± 0.002<br>**0.036 ± 0.002**<br>0.026 ± 0.001<br>0.027 ± 0.002|0.051 ± 0.006<br>0.045 ± 0.006<br>0.048 ± 0.004<br>**.049 ± 0.006**<br>0.045 ± 0.005<br>0.038 ± 0.012<br>0.048 ± 0.006<br>0.049 ± 0.003<br>0.048 ± 0.002<br>0.050 ± 0.002<br>0.049 ± 0.002|**0**<br>**0**<br>**0**|0.057 ± 0.007<br>0.051 ± 0.008<br>0.051 ± 0.005<br>**.049 ± 0.006**<br>0.051 ± 0.006<br>**.050 ± 0.013**<br>0.051 ± 0.007<br>**.051 ± 0.002**<br>0.050 ± 0.002<br>**.052 ± 0.002**<br>**.051 ± 0.002**|
||||**0**||
||||**0**||



full suite of experimental results. We evaluate the tested methods by measuring the error rate and the volume of the prediction region for different global targeted error rates _ϵh_ . 

Table 2 and Figure 1( _a_ ) show the measured error rate while Table 3 and Figure 1( _b_ ) present the prediction region’s volume for the synthetic data set with _e ∼_ [ _U_ ( _−_ 1 _,_ 1) _, χ_[2] 2[]] _[⊤]_[.] For this data set, DMT-CP produces the smallest prediction regions for _ϵh ≤_ 0 _._ 8 while MaxRank narrowly takes the lead for _ϵh ≥_ 0 _._ 85. Figure 2( _a_ ) shows that the underlying model’s residuals follow the distribution of the noise term _e_ and their lack of correlation is displayed in Figure 2( _b_ ). Finally, Figure 3 shows how the various methods partition the residual space. Because _y ∈_ R[2] , the rectangular prediction region is the Cartesian product of two prediction intervals. These intervals are produced by two conformal predictors Γ _[ϵ] m[m]_[,][one][for][each] dimension of _y_ . As shown in Equation (4), these Γ _[ϵ] m[m]_[utilise] _[ α] m,_ (1 _−ϵm_ )[, the 1] _[−][ϵ][m]_[quantile of] the residuals of dimension _m_ . For each tested global significance level _ϵh_ , Figure 3 contains a rectangle with vertices (0 _,_ 0) _,_ ( _α_ 1 _,_ (1 _−ϵ_ 1) _,_ 0) _,_ (0 _, α_ 2 _,_ (1 _−ϵ_ 2)) and ( _α_ 1 _,_ (1 _−ϵ_ 1) _, α_ 2 _,_ (1 _−ϵ_ 2)). Unfolding such a rectangle along one axis and unfolding the result along the second axis gives the shape of the prediction region for a chosen global targeted error rate _ϵh_ . This representation visualizes the different behaviours of the tested methods. Bonferroni predictors produce prediction regions that progressively grow in both dimensions when the global targeted error rate _ϵh_ decreases, assigning equal and decreasing local targeted error rates _ϵm_ to each dimension. Copula Conformal Predictors and Max-Rank display a similar behaviour but assign larger local targeted error rates than Bonferroni predictors, leading to smaller prediction regions. DCP-MT follows a different strategy, assigning a small portion of its total error budget to the first dimension, leading to a large interval which only changes minimally, while increasing the interval in the second dimension when the global targeted error rate _ϵh_ decreases. 

Tables 4 and 5 compare the tested method’s measured error rates and prediction region volumes for all synthetic and real-world data sets at _ϵh_ = 0 _._ 05, providing a broader overview over tested methods’ performance. DCP-MT produces the smallest prediction regions when the residuals’ dimensions are weakly correlated. This is especially true for small values of _ϵh_ on the as can be seen in Tables 7, 13, 15, and 17, where Max-Rank is generally more informationally efficient for larger _ϵh_ . Max-Rank also produces smaller hyperrectangles when the residuals’ dimensions are strongly correlated such as for the synthetic data set with _e ∼N_ ([0 _,_ 0] _[⊤]_ ] _,_ **σ** ) and _σ_ = 1. 

14 

Dynamic Conformal Prediction for Multi-Target Regression 

Table 5: Hyperrectangle volumes acoss all experiments for _ϵh_ = 0 _._ 05. Bold values indicate that the method produced the smallest prediction region while underlined values highlight instances for which the measured error rate _≥_ 0 _._ 05. 

|**Data Set**<br>**Bonferroni**|**DMT-CP**<br>**Empirical Copula**|**DMT-CP**<br>**Empirical Copula**|||**Max-Rank**|
|---|---|---|---|---|---|
|synt, _e ∼_[_U_(_−_1_,_1)_, χ_2<br>2]_⊤_<br>0.374 ± 0.013<br>synt, _e ∼N_(**0**_,_**σ**), _σ_ = 0<br>6.644 ± 0.246<br>synt, _e ∼N_(**0**_,_**σ**), _σ_ = 0_._5<br>4.390 ± 0.126<br>synt, _e ∼N_(**0**_,_**σ**), _σ_ = 1<br>5.928 ± 0.305<br>synt, _e ∼N_(**0**_,_**σ**), _σ_ = _−_0_._5<br>6.068 ± 0.230<br>diabetes<br>7.919 ± 0.943<br>music origin<br>24.417 ± 2.147<br><br>rf1<br>172.734 ± 81.099<br>rf2<br>87.792 ± 46.649<br><br>scm1d<br>11.387E9 ± 5.455E9<br>3.7<br>scm20d<br>108.772E9 ± 36.307E9<br>35.95|**0.323 ± 0.011**<br>**6.312 ± 0.205**<br>**4.124 ± 0.114**<br>5.682 ± 0.281<br>**4**<br>**5.621 ± 0.150**<br>6.604 ± 0.752<br>**22.860 ± 1.602**<br><br>32.901 ± 14.016<br>3<br>**14.946 ± 8.429**<br>1<br>53E9 ± 1.420E9<br>41.820<br>5E9 ± 11.015E9<br>1.172|0.369 ± 0.013<br>6.628 ± 0.232<br>4.263 ± 0.122<br>**.552 ± 0.221**<br>5.962 ± 0.239<br>7.627 ± 0.923<br>23.433 ± 1.969<br>8.125 ± 18.702<br>9.484 ± 12.388<br>E6 ± 11.540E6<br>E9 ± 0.345E9|**32.7**|**32**|0.354 ± 0.011<br>6.347 ± 0.201<br>4.159 ± 0.105<br>**4.552 ± 0.221**<br>5.720 ± 0.230<br>**6.498 ± 0.784**<br>23.237 ± 2.002<br>**.341 ± 15.305**<br>16.539 ± 10.866<br>**E6 ± 8.828E6**<br>**E9 ± 0.301E9**|
|||||**74**||
||||**0.9**|**42**||



Appendix A contains the detailed experimental results for all data sets. This includes the measured error rates and prediction region volumes for different _ϵh_ and the residual correlation matrix. For data sets with a two-dimensional label space it also provides a plot of the residuals and plots of the methods’ partition of the residual space for different _ϵh_ . 

## **7. Discussion** 

This section discusses the empirical results, comparing DCP-MT to Bonferroni predictors, copula conformal predictors, and Max-Rank. 

The theoretical differences discussed in Section 5 are confirmed by the experimental results shown in Section 6.3. DCP-MT produces smaller prediction regions than copula conformal predictors and Max-Rank for data sets whose nonconformity scores are weakly correlated across their dimensions and/or have differing marginal distributions. In the case of strong positive correlation between the dimensions’ nonconformity scores Max-Rank excels as expected given the method’s design. These results agree with the experimental results of Timans et al. (2025), reporting that Max-Rank is most efficient in the presence of strong positive correlation and will behave similarly to Bonferroni predictors in the absence of correlation. The behaviour of copula conformal predictors using the empirical copula generally resembles the one of Max-Rank while producing hyperrectangles that are slightly larger. Bonferroni conformal predictors are not competitive, producing the largest prediction regions. In some instances DCP-MT, Copula conformal predictors, and Max-Rank produce errors with a frequency slightly above the targeted error rate which is consistent with the results in Messoudi et al. (2021). This can not be observed for Bonferroni conformal predictors, which also produce the largest prediction regions. 

Because of the different approaches the discussed methods take, we recommend to choose a method based on the characteristics of the nonconformity scores a user encounters. Depending on the data set’s size and the number of dimension of the label space, the computational complexity might be another factor the user should consider. Appendix B contains a preliminary theoretical analysis of the discussed methods’ computational complexity as well as the wall time measured for the experiments presented in Section 6.3. 

15 

Schlembach Smirnov Winands 

## **8. Conclusion and Future Research** 

In this article, we present DCP-MT, a novel approach to determine the local targeted error rates of multiple single-target inductive conformal predictors when combining them to form a hyperrectangular prediction regions. DCP-MT minimises the hyperrectangle’s volume by dynamically allocating a global error budget between the local targeted error rates using integer linear programming. The theoretical analysis of DCP-MT proves its validity under exchangeability of the examples in the data set and a symmetric training algorithm for the underlying model. 

The experimental results on four synthetic and six public real-world data sets serve to validate DCP-MT’s theoretical properties and provide insights into the method’s behaviour. We compare DCP-MT to Bonferroni predictors, copula conformal predictors and Max-Rank. The results show that DCP-MT excels when the nonconformity scores are weakly correlated across the dimensions of the label space and when the distributions of the nonconformity scores differ between dimensions. In these situations, assigning the same local targeted error rate to all their single-target inductive conformal predictors limits the informational efficiency of the related methods. Plots that show the partition of the residual space for different global targeted error rates visualise the differences in the tested method’s behaviours. 

For future research, we would like to investigate the interactions of DCP-MT with input dependent nonconformity metrics such as utilised by Messoudi et al. (2021) and compare it to the method proposed by Cleaveland et al. (2024). It would also be interesting to extend the approach of optimising the prediction region’s volume to other methods like copula conformal predictors. Finally, we believe that for multi-target regression applications with high-dimensional label spaces and very large calibration sets, DCP-MT might benefit from additional computational optimisation, such as using a minibatch approach. 

## **References** 

- Niccol`o Ajroldi, Jacopo Diquigiovanni, Matteo Fontana, and Simone Vantini. Conformal prediction bands for two-dimensional functional time series. _Computational Statistics & Data Analysis_ , 187:107821, July 2023. ISSN 01679473. doi: 10.1016/j.csda.2023.107821. URL `https://linkinghub.elsevier.com/retrieve/pii/S0167947323001329` . 

- Anastasios N. Angelopoulos and Stephen Bates. A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification, December 2022. URL `http://arxiv.org/abs/2107.07511` . arXiv:2107.07511 [cs, math, stat]. 

- Rina Foygel Barber, Emmanuel J. Candes, Aaditya Ramdas, and Ryan J. Tibshirani. Conformal prediction beyond exchangeability. _arXiv:2202.13415 [stat]_ , March 2022. URL `http://arxiv.org/abs/2202.13415` . arXiv: 2202.13415. 

- Matthew Cleaveland, Insup Lee, George J. Pappas, and Lars Lindemann. Conformal Prediction Regions for Time Series Using Linear Complementarity Programming. _Proceedings of the AAAI Conference on Artificial Intelligence_ , 38(19):20984–20992, March 2024. ISSN 2374-3468, 2159-5399. doi: 10.1609/aaai.v38i19.30089. URL `https: //ojs.aaai.org/index.php/AAAI/article/view/30089` . 

16 

Dynamic Conformal Prediction for Multi-Target Regression 

- Victor Dheur, Matteo Fontana, Yorick Estievenart, Naomi Desobry, and Souhaib Ben Taieb. A Unified Comparative Study with Generalized Conformity Scores for Multi-Output Conformal Regression, February 2025. URL `https://arxiv.org/abs/2501.10533` . ~~e~~ print: 2501.10533. 

- Jacopo Diquigiovanni, Matteo Fontana, and Simone Vantini. Distribution-Free Prediction Bands for Multivariate Functional Time Series: an Application to the Italian Gas Market, January 2024. URL `http://arxiv.org/abs/2107.00527` . arXiv:2107.00527 [stat]. 

- Bradley Efron, Trevor Hastie, Iain Johnstone, and Robert Tibshirani. Least angle regression. _The Annals of Statistics_ , 32(2):407–499, April 2004. doi: 10.1214/009053604000000067. 

- Shai Feldman, Liran Ringel, Stephen Bates, and Yaniv Romano. Achieving Risk Control in Online Learning Settings, January 2023. URL `http://arxiv.org/abs/2205.09095` . arXiv:2205.09095 [cs, stat]. 

- Matteo Fontana, Gianluca Zeni, and Simone Vantini. Conformal prediction: A unified review of theory and new challenges. _Bernoulli_ , 29 (1), February 2023. ISSN 1350-7265. doi: 10.3150/21-BEJ1447. URL `https://projecteuclid.org/journals/bernoulli/volume-29/issue-1/ Conformal-prediction--A-unified-review-of-theory-and-new/10.3150/ 21-BEJ1447.full` . 

- Chancellor Johnstone and Bruce Cox. Conformal uncertainty sets for robust optimization. In Lars Carlsson, Zhiyuan Luo, Giovanni Cherubin, and Khuong An Nguyen, editors, _Proceedings of the Tenth Symposium on Conformal and Probabilistic Prediction and Applications_ , volume 152 of _Proceedings of Machine Learning Research_ , pages 72–90. PMLR, September 2021. URL `https://proceedings.mlr.press/v152/johnstone21a.html` . 

- Soundouss Messoudi, S´ebastien Destercke, and Sylvain Rousseau. Conformal multi-target regression using neural networks. In Alexander Gammerman, Vladimir Vovk, Zhiyuan Luo, Evgueni Smirnov, and Giovanni Cherubin, editors, _Proceedings of the Ninth Symposium on Conformal and Probabilistic Prediction and Applications_ , volume 128 of _Proceedings of Machine Learning Research_ , pages 65–83. PMLR, September 2020. URL `https://proceedings.mlr.press/v128/messoudi20a.html` . 

- Soundouss Messoudi, S´ebastien Destercke, and Sylvain Rousseau. Copula-based conformal prediction for multi-target regression. _Pattern Recognition_ , 120:108101, June 2021. ISSN 00313203. doi: 10.1016/j.patcog.2021.108101. URL `https://linkinghub.elsevier. com/retrieve/pii/S0031320321002880` . 

- Soundouss Messoudi, S´ebastien Destercke, and Sylvain Rousseau. Ellipsoidal conformal inference for Multi-Target Regression. In Ulf Johansson, Henrik Bostr¨om, Khuong An Nguyen, Zhiyuan Luo, and Lars Carlsson, editors, _Proceedings of the Eleventh Symposium on Conformal and Probabilistic Prediction with Applications_ , volume 179 of _Proceedings of Machine Learning Research_ , pages 294–306. PMLR, August 2022. URL `https://proceedings.mlr.press/v179/messoudi22a.html` . 

17 

Schlembach Smirnov Winands 

- Jelmer Neeven and Evgueni Smirnov. Conformal stacked weather forecasting. In Alex Gammerman, Vladimir Vovk, Zhiyuan Luo, Evgueni Smirnov, and Ralf Peeters, editors, _Proceedings of the Seventh Workshop on Conformal and Probabilistic Prediction and Applications_ , volume 91 of _Proceedings of Machine Learning Research_ , pages 220– 233. PMLR, June 2018. URL `https://proceedings.mlr.press/v91/neeven18a.html` . 

- Harris Papadopoulos and Haris Haralambous. Reliable prediction intervals with regression neural networks. _Neural Networks_ , 24(8):842–851, October 2011. ISSN 08936080. doi: 10. 1016/j.neunet.2011.05.008. URL `https://linkinghub.elsevier.com/retrieve/pii/ S089360801100150X` . 

- Harris Papadopoulos, Kostas Proedrou, Volodya Vovk, and Alex Gammerman. Inductive Confidence Machines for Regression. In Tapio Elomaa, Heikki Mannila, and Hannu Toivonen, editors, _Machine Learning: ECML 2002_ , pages 345–356, Berlin, Heidelberg, 2002. Springer Berlin Heidelberg. ISBN 978-3-540-36755-0. 

- Fabian Pedregosa, Ga¨el Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand Thirion, Olivier Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss, Vincent Dubourg, Jake Vanderplas, Alexandre Passos, David Cournapeau, Matthieu Brucher, Matthieu Perrot, and Edouard[´] Duchesnay. Scikit-learn: Machine Learning in Python. _J. Mach. Learn. Res._ , 12:2825–2830, November 2011. ISSN 1532-4435. Publisher: JMLR.org. 

- Filip Schlembach, Evgueni Smirnov, and Irena Koprinska. Conformal Multistep-Ahead Multivariate Time-Series Forecasting. In Ulf Johansson, Henrik Bostr¨om, Khuong An Nguyen, Zhiyuan Luo, and Lars Carlsson, editors, _Proceedings of the Eleventh Symposium on Conformal and Probabilistic Prediction with Applications_ , volume 179 of _Proceedings of Machine Learning Research_ , pages 316–318. PMLR, August 2022. URL `https://proceedings.mlr.press/v179/schlembach22a.html` . 

- Filip Schlembach, Evgueni Smirnov, Irena Koprinska, and Mark H. M. Winands. Conformal multistep-ahead multivariate time-series forecasting. _Machine Learning_ , 114(7):165, June 2025. ISSN 1573-0565. doi: 10.1007/s10994-024-06722-9. URL `https://doi.org/10. 1007/s10994-024-06722-9` . 

- M. Sklar. Fonctions de r´epartition `a N dimensions et leurs marges. _Annales de l’ISUP_ , VIII (3):229–231, 1959. URL `https://hal.science/hal-04094463` . Publisher: Publications de l’Institut de Statistique de l’Universit´e de Paris. 

- Kamil˙e Stankeviˇci¯ut˙e, Ahmed M. Alaa, and Mihaela van der Schaar. Conformal Time-Series Forecasting. In _Advances in Neural Information Processing Systems 34 (NeurIPS 2021)_ , 2021. URL `https://proceedings.neurips.cc/paper/2021/hash/ 312f1ba2a72318edaaa995a67835fad5-Abstract.html` . 

- Sophia Sun and Rose Yu. Copula Conformal Prediction for Multi-step Time Series Forecasting, March 2024. URL `https://arxiv.org/abs/2212.03281` . ~~e~~ print: 2212.03281. 

18 

Dynamic Conformal Prediction for Multi-Target Regression 

- Alexander Timans, Christoph-Nikolas Straehle, Kaspar Sakmann, Christian A. Naesseth, and Eric Nalisnick. Max-Rank: Efficient Multiple Testing for Conformal Prediction, March 2025. URL `https://arxiv.org/abs/2311.10900` . ~~e~~ print: 2311.10900. 

- Paolo Toccaceli. Introduction to conformal predictors. _Pattern Recognition_ , 124:108507, April 2022. ISSN 00313203. doi: 10.1016/j.patcog.2021.108507. URL `https:// linkinghub.elsevier.com/retrieve/pii/S003132032100683X` . 

- Grigorios Tsoumakas, Eleftherios Spyromitros-Xioufis, Jozef Vilcek, and Ioannis Vlahavas. MULAN: A Java Library for Multi-Label Learning. _Journal of Machine Learning Research_ , 12(71):2411–2414, 2011. URL `http://jmlr.org/papers/v12/tsoumakas11a. html` . 

- Vladimir Vovk. Transductive conformal predictors. In Harris Papadopoulos, Andreas S. Andreou, Lazaros Iliadis, and Ilias Maglogiannis, editors, _Artificial Intelligence Applications and Innovations_ , pages 348–360, Berlin, Heidelberg, 2013. Springer Berlin Heidelberg. ISBN 978-3-642-41142-7. doi: 10.1007/978-3-642-41142-7 ~~3~~ 6. 

- Vladimir Vovk, A. Gammerman, and Glenn Shafer. _Algorithmic learning in a random world_ . Springer, New York, 2005. ISBN 978-0-387-00152-4 978-0-387-25061-8. 

- Vladimir Vovk, Bin Wang, and Ruodu Wang. Admissible ways of merging p-values under arbitrary dependence. _The Annals of Statistics_ , 50(1), February 2022. ISSN 0090-5364. doi: 10.1214/21-AOS2109. URL `https: //projecteuclid.org/journals/annals-of-statistics/volume-50/issue-1/ Admissible-ways-of-merging-p-values-under-arbitrary-dependence/10.1214/ 21-AOS2109.full` . 

- Fang Zhou, Q. Claire, and Ross D. King. Predicting the Geographical Origin of Music. In _2014 IEEE International Conference on Data Mining_ , pages 1115–1120, 2014. doi: 10.1109/ICDM.2014.73. 

19 

Schlembach Smirnov Winands 

## **Appendix A. Additional Experimental Results** 

This Section contains the additional experimental results. Each subsection corresponds to one of the data sets from Section 6.1. In the tables, underlined values indicate instances for which the measured error rate exceeds the targeted error rate while bold values indicate that the method produced the smallest prediction region. 

## **A.1. Synthetic, Multivariate Normal Error,** _σ_ = 0 

Additional results for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), _σ_ = 0 

Table 6: Multi-tests method’s mean error rates and standard deviations for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 0. 

|_ϵh_<br>Bonferroni||DCP-MT<br>Empirical Copula|DCP-MT<br>Empirical Copula|DCP-MT<br>Empirical Copula|Max-Rank|
|---|---|---|---|---|---|
|0.05<br>0.045 ± 0.006<br>0.10<br>0.093 ± 0.006<br>0.15<br>0.136 ± 0.007<br>0.20<br>0.181 ± 0.008<br>0.25<br>0.230 ± 0.009<br>0.30<br>0.272 ± 0.013<br>0.35<br>0.320 ± 0.012<br>0.40<br>0.367 ± 0.012<br>0.45<br>0.402 ± 0.011<br>0.50<br>0.444 ± 0.012<br>0.55<br>0.477 ± 0.014<br>0.60<br>0.516 ± 0.014<br>0.65<br>0.552 ± 0.012<br>0.70<br>0.582 ± 0.014<br>0.75<br>0.613 ± 0.013<br>0.80<br>0.648 ± 0.013<br>0.85<br>0.673 ± 0.011<br>0.90<br>0.703 ± 0.011<br>0.95<br>0.728 ± 0.010|**0**|**.054 ± 0.008**<br>**.109 ± 0.007**<br>**.159 ± 0.010**<br>**.208 ± 0.011**<br>0.251 ± 0.012<br>0.297 ± 0.014<br>0.339 ± 0.009<br>0.387 ± 0.011<br>0.426 ± 0.014<br>0.463 ± 0.015<br>0.503 ± 0.013<br>0.549 ± 0.016<br>0.588 ± 0.018<br>0.633 ± 0.017<br>0.692 ± 0.018<br>0.761 ± 0.026<br>0.835 ± 0.016<br>0.897 ± 0.013<br>0.950 ± 0.007|**0**|0.045 ± 0.006<br>0.094 ± 0.006<br>0.144 ± 0.009<br>0.191 ± 0.010<br>0.244 ± 0.012<br>0.295 ± 0.013<br>0.348 ± 0.012<br>0.396 ± 0.013<br>0.444 ± 0.014<br>0.498 ± 0.017<br>0.551 ± 0.015<br>0.599 ± 0.015<br>0.647 ± 0.014<br>0.697 ± 0.009<br>**.753 ± 0.012**<br>0.802 ± 0.010<br>0.851 ± 0.009<br>0.900 ± 0.008<br>0.948 ± 0.008|0.051 ± 0.008<br>0.096 ± 0.008<br>0.147 ± 0.009<br>0.197 ± 0.010<br>**0.248 ± 0.012**<br>**0.298 ± 0.013**<br>**0.350 ± 0.011**<br>**0.401 ± 0.013**<br>**0.450 ± 0.013**<br>**0.499 ± 0.017**<br>**0.552 ± 0.014**<br>**0.604 ± 0.015**<br>**0.653 ± 0.014**<br>**0.701 ± 0.010**<br>0.753 ± 0.011<br>**0.805 ± 0.009**<br>**0.854 ± 0.010**<br>**0.903 ± 0.007**<br>**0.950 ± 0.008**|
||**0**|||||
||**0**|||||
||**0**|||||
|||||||
|||||||



Table 7: Multi-tests method’s mean hyperrectangle volumes for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 0. 

|_ϵh_<br>Bonferroni|DCP-MT|Empirical Copula|Max-Rank|
|---|---|---|---|
|0.05<br>6.644 ± 0.246<br>0.10<br>5.182 ± 0.115<br>0.15<br>4.364 ± 0.107<br>0.20<br>3.623 ± 0.085<br>0.25<br>3.005 ± 0.079<br>0.30<br>2.636 ± 0.077<br>0.35<br>2.310 ± 0.063<br>0.40<br>2.023 ± 0.058<br>0.45<br>1.818 ± 0.053<br>0.50<br>1.616 ± 0.052<br>0.55<br>1.466 ± 0.049<br>0.60<br>1.308 ± 0.045<br>0.65<br>1.173 ± 0.041<br>0.70<br>1.077 ± 0.036<br>0.75<br>0.980 ± 0.031<br>0.80<br>0.885 ± 0.029<br>0.85<br>0.816 ± 0.028<br>0.90<br>0.736 ± 0.026<br>0.95<br>0.674 ± 0.023|**6.312 ± 0.205**<br>**4.966 ± 0.115**<br>**4.073 ± 0.102**<br>**3.378 ± 0.078**<br>2.897 ± 0.075<br>2.520 ± 0.057<br>2.216 ± 0.056<br>1.942 ± 0.055<br>1.733 ± 0.051<br>1.551 ± 0.048<br>1.396 ± 0.042<br>1.241 ± 0.043<br>1.121 ± 0.037<br>1.010 ± 0.034<br>0.897 ± 0.030<br>0.763 ± 0.027<br>0.618 ± 0.027<br>0.451 ± 0.024<br>0.249 ± 0.023|6.628 ± 0.232<br>5.171 ± 0.114<br>4.238 ± 0.130<br>3.482 ± 0.121<br>2.872 ± 0.083<br>2.478 ± 0.072<br>2.138 ± 0.063<br>1.853 ± 0.066<br>1.610 ± 0.067<br>1.381 ± 0.060<br>1.180 ± 0.051<br>1.024 ± 0.046<br>0.883 ± 0.035<br>0.751 ± 0.026<br>**0.610 ± 0.026**<br>0.484 ± 0.020<br>0.354 ± 0.016<br>0.228 ± 0.011<br>0.116 ± 0.013|6.347 ± 0.201<br>5.127 ± 0.138<br>4.174 ± 0.117<br>3.391 ± 0.113<br>**2.837 ± 0.084**<br>**2.457 ± 0.073**<br>**2.125 ± 0.061**<br>**1.824 ± 0.064**<br>**1.583 ± 0.063**<br>**1.377 ± 0.059**<br>**1.176 ± 0.051**<br>**1.010 ± 0.045**<br>**0.869 ± 0.036**<br>**0.741 ± 0.026**<br>0.610 ± 0.024<br>**0.475 ± 0.019**<br>**0.348 ± 0.017**<br>**0.222 ± 0.011**<br>**0.112 ± 0.013**|



20 

Dynamic Conformal Prediction for Multi-Target Regression 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0021-01.png)


**----- Start of picture text -----**<br>
( a ) Error Rate ( b ) Volume<br>**----- End of picture text -----**<br>


Figure 4: Multi-tests method’s mean error rates and volumes for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 0. 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0021-03.png)


**----- Start of picture text -----**<br>
( a ) Residuals ( b ) Residual correlation matrix<br>**----- End of picture text -----**<br>


Figure 5: Underlying model’s absolute residuals and their correlation for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 0. 

21 

Schlembach Smirnov Winands 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0022-01.png)


**----- Start of picture text -----**<br>
( a ) Bonferroni ( b ) DCP-MT<br>1.0<br>Test Residuals cc)< 2.0 Test<br>0. 80<br>><br>g 1.5<br>vo<br>0.6¥<br>i} 2<br>= 1.0<br>0.45,<br>a<br>o 0.5<br>0.22<br>O)<br>0.0<br>0.0<br>0.5 1.0 1.5 2.0 . 0.0 0.5 1.0 1.5 2.0<br>rn rY<br>( c ) Empirical Copula ( d ) Max-Rank<br>**----- End of picture text -----**<br>


Figure 6: Multi-tests method’s partition of the residual space for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 0 averaged over 20 repetitions. 

22 

Dynamic Conformal Prediction for Multi-Target Regression 

## **A.2. Synthetic, Multivariate Normal Error,** _σ_ = 0 _._ 5 

Additional results for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), _σ_ = 0 _._ 5 

Table 8: Multi-tests method’s mean error rates and standard deviations for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 0 _._ 5. 

|_ϵh_<br>Bonferroni||DCP-MT<br>Empirical Copula|DCP-MT<br>Empirical Copula|Max-Rank|
|---|---|---|---|---|
|0.05<br>0.043 ± 0.004<br>0.10<br>0.091 ± 0.007<br>0.15<br>0.130 ± 0.007<br>0.20<br>0.178 ± 0.007<br>0.25<br>0.218 ± 0.007<br>0.30<br>0.257 ± 0.008<br>0.35<br>0.298 ± 0.008<br>0.40<br>0.342 ± 0.010<br>0.45<br>0.378 ± 0.011<br>0.50<br>0.418 ± 0.010<br>0.55<br>0.454 ± 0.008<br>0.60<br>0.490 ± 0.009<br>0.65<br>0.525 ± 0.010<br>0.70<br>0.552 ± 0.013<br>0.75<br>0.585 ± 0.013<br>0.80<br>0.617 ± 0.010<br>0.85<br>0.647 ± 0.010<br>0.90<br>0.678 ± 0.009<br>0.95<br>0.703 ± 0.010|**0**|**.052 ± 0.005**<br>0.099 ± 0.007<br>0.150 ± 0.009<br>0.197 ± 0.010<br>0.240 ± 0.008<br>0.278 ± 0.009<br>0.325 ± 0.015<br>0.368 ± 0.012<br>0.409 ± 0.012<br>0.443 ± 0.011<br>0.481 ± 0.015<br>0.525 ± 0.016<br>0.568 ± 0.015<br>0.630 ± 0.017<br>0.715 ± 0.022<br>0.784 ± 0.017<br>0.845 ± 0.016<br>0.896 ± 0.012<br>0.944 ± 0.008|0.048 ± 0.004<br>0.097 ± 0.007<br>0.145 ± 0.006<br>0.194 ± 0.009<br>0.250 ± 0.008<br>0.298 ± 0.009<br>0.348 ± 0.011<br>0.397 ± 0.011<br>0.449 ± 0.010<br>0.501 ± 0.012<br>0.548 ± 0.011<br>0.593 ± 0.014<br>0.645 ± 0.012<br>0.694 ± 0.012<br>0.747 ± 0.013<br>0.796 ± 0.010<br>0.844 ± 0.009<br>0.895 ± 0.008<br>0.944 ± 0.006|0.051 ± 0.005<br>**0.100 ± 0.008**<br>**0.148 ± 0.007**<br>**0.199 ± 0.008**<br>**0.252 ± 0.008**<br>**0.300 ± 0.009**<br>**0.349 ± 0.011**<br>**0.403 ± 0.011**<br>**0.453 ± 0.011**<br>**0.502 ± 0.011**<br>**0.549 ± 0.012**<br>**0.598 ± 0.014**<br>**0.650 ± 0.012**<br>**0.699 ± 0.012**<br>**0.746 ± 0.013**<br>**0.799 ± 0.010**<br>**0.848 ± 0.007**<br>**0.897 ± 0.008**<br>**0.946 ± 0.005**|
||||||



Table 9: Multi-tests method’s mean hyperrectangle volumes for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 0 _._ 5. 

|_ϵh_<br>Bonferroni||DCP-MT<br>Empirical Copula|DCP-MT<br>Empirical Copula|Max-Rank|
|---|---|---|---|---|
|0.05<br>4.390 ± 0.126<br>0.10<br>3.419 ± 0.088<br>0.15<br>2.919 ± 0.073<br>0.20<br>2.468 ± 0.062<br>0.25<br>2.134 ± 0.045<br>0.30<br>1.905 ± 0.039<br>0.35<br>1.687 ± 0.031<br>0.40<br>1.501 ± 0.032<br>0.45<br>1.368 ± 0.031<br>0.50<br>1.228 ± 0.028<br>0.55<br>1.113 ± 0.028<br>0.60<br>0.990 ± 0.026<br>0.65<br>0.879 ± 0.025<br>0.70<br>0.801 ± 0.024<br>0.75<br>0.721 ± 0.020<br>0.80<br>0.651 ± 0.017<br>0.85<br>0.594 ± 0.020<br>0.90<br>0.534 ± 0.018<br>0.95<br>0.488 ± 0.017|**4**|**.124 ± 0.114**<br>3.313 ± 0.080<br>2.770 ± 0.071<br>2.353 ± 0.048<br>2.053 ± 0.036<br>1.818 ± 0.033<br>1.619 ± 0.034<br>1.434 ± 0.032<br>1.279 ± 0.031<br>1.143 ± 0.029<br>1.030 ± 0.027<br>0.915 ± 0.023<br>0.824 ± 0.021<br>0.731 ± 0.016<br>0.626 ± 0.015<br>0.495 ± 0.017<br>0.377 ± 0.014<br>0.256 ± 0.015<br>0.137 ± 0.013|4.263 ± 0.122<br>3.338 ± 0.082<br>2.763 ± 0.058<br>2.323 ± 0.057<br>1.946 ± 0.044<br>1.690 ± 0.037<br>1.477 ± 0.040<br>1.302 ± 0.034<br>1.127 ± 0.035<br>0.954 ± 0.036<br>0.813 ± 0.026<br>0.703 ± 0.022<br>0.597 ± 0.022<br>0.505 ± 0.022<br>0.413 ± 0.021<br>0.325 ± 0.017<br>0.241 ± 0.016<br>0.156 ± 0.010<br>0.074 ± 0.006|4.159 ± 0.105<br>**3.296 ± 0.079**<br>**2.729 ± 0.066**<br>**2.280 ± 0.053**<br>**1.933 ± 0.040**<br>**1.681 ± 0.038**<br>**1.471 ± 0.036**<br>**1.281 ± 0.033**<br>**1.110 ± 0.037**<br>**0.950 ± 0.034**<br>**0.810 ± 0.027**<br>**0.693 ± 0.021**<br>**0.588 ± 0.022**<br>**0.497 ± 0.023**<br>**0.413 ± 0.021**<br>**0.319 ± 0.017**<br>**0.235 ± 0.015**<br>**0.152 ± 0.010**<br>**0.071 ± 0.006**|
||||||



23 

Schlembach Smirnov Winands 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0024-01.png)


**----- Start of picture text -----**<br>
( a ) Error Rate ( b ) Volume<br>**----- End of picture text -----**<br>


Figure 7: Multi-tests method’s mean error rates and volumes for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 0 _._ 5. 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0024-03.png)


**----- Start of picture text -----**<br>
( a ) Residuals ( b ) Residual correlation matrix<br>**----- End of picture text -----**<br>


Figure 8: Underlying model’s absolute residuals and their correlation for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 0 _._ 5. 

24 

Dynamic Conformal Prediction for Multi-Target Regression 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0025-01.png)


**----- Start of picture text -----**<br>
( a ) Bonferroni ( b ) DCP-MT<br>1.0<br>Test Residuals oO. 1.2 Test<br>0. 80 1.0<br>ov><br>° 0.8<br>062VY 20.6<br>€<br>0.45,tial 0.4<br>o<br>0.22 0.2<br>0)<br>0.0<br>0.0<br>1.0 1.5 2.0 2.5 . 0.0 0.5 1.0 1.5 2.0<br>rn rY<br>( c ) Empirical Copula ( d ) Max-Rank<br>**----- End of picture text -----**<br>


Figure 9: Multi-tests method’s partition of the residual space for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 0 _._ 5 averaged over 20 repetitions. 

25 

Schlembach Smirnov Winands 

## **A.3. Synthetic, Multivariate Normal Error,** _σ_ = 1 

Additional results for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), _σ_ = 1. 

Table 10: Multi-tests method’s mean error rates and standard deviations for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 1. 

|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|Max-Rank|
|---|---|---|---|
|0.05<br>0.023 ± 0.005<br>0.035 ± 0.005<br>0.10<br>0.049 ± 0.006<br>0.063 ± 0.007<br>0.15<br>0.071 ± 0.006<br>0.098 ± 0.010<br>0.20<br>0.097 ± 0.008<br>0.131 ± 0.010<br>0.25<br>0.125 ± 0.008<br>0.154 ± 0.011<br>0.30<br>0.148 ± 0.009<br>0.189 ± 0.015<br>0.35<br>0.174 ± 0.009<br>0.225 ± 0.021<br>0.40<br>0.203 ± 0.009<br>0.259 ± 0.020<br>0.45<br>0.225 ± 0.009<br>0.287 ± 0.013<br>0.50<br>0.254 ± 0.009<br>0.311 ± 0.018<br>0.55<br>0.276 ± 0.010<br>0.331 ± 0.019<br>0.60<br>0.303 ± 0.010<br>0.376 ± 0.035<br>0.65<br>0.330 ± 0.011<br>0.428 ± 0.046<br>0.70<br>0.354 ± 0.011<br>0.496 ± 0.044<br>0.75<br>0.380 ± 0.011<br>0.603 ± 0.048<br>0.80<br>0.404 ± 0.013<br>0.748 ± 0.042<br>0.85<br>0.426 ± 0.014<br>0.829 ± 0.021<br>0.90<br>0.453 ± 0.014<br>0.891 ± 0.009<br>0.95<br>0.478 ± 0.013<br>0.944 ± 0.009|**0**<br>**0**<br>**0**<br>**0**|**.049 ± 0.006**<br>**.097 ± 0.008**<br>**.148 ± 0.009**<br>0.200 ± 0.008<br>**.254 ± 0.009**<br>**.303 ± 0.010**<br>**.354 ± 0.011**<br>0.401 ± 0.013<br>0.448 ± 0.014<br>**.504 ± 0.009**<br>**.552 ± 0.011**<br>0.599 ± 0.016<br>0.648 ± 0.015<br>0.695 ± 0.014<br>**.750 ± 0.013**<br>0.801 ± 0.011<br>0.849 ± 0.010<br>0.900 ± 0.009<br>0.947 ± 0.008|0.049 ± 0.006<br>0.097 ± 0.008<br>0.148 ± 0.009<br>**0.203 ± 0.009**<br>0.254 ± 0.009<br>0.303 ± 0.010<br>0.354 ± 0.011<br>**0.404 ± 0.013**<br>**0.453 ± 0.014**<br>0.504 ± 0.009<br>0.552 ± 0.011<br>**0.603 ± 0.016**<br>**0.652 ± 0.015**<br>**0.698 ± 0.014**<br>0.750 ± 0.013<br>**0.805 ± 0.011**<br>**0.853 ± 0.009**<br>**0.905 ± 0.009**<br>**0.950 ± 0.008**|
||**0**|||
||**0**|||
||**0**|||
||**0**|||
||**0**|||



Table 11: Multi-tests method’s mean hyperrectangle volumes for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 1. 

|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|Max-Rank|
|---|---|---|---|
|0.05<br>5.928 ± 0.305<br>5.682 ± 0.281<br>0.10<br>4.552 ± 0.221<br>4.445 ± 0.189<br>0.15<br>3.852 ± 0.146<br>3.703 ± 0.152<br>0.20<br>3.245 ± 0.149<br>3.100 ± 0.131<br>0.25<br>2.741 ± 0.118<br>2.678 ± 0.108<br>0.30<br>2.430 ± 0.100<br>2.342 ± 0.093<br>0.35<br>2.136 ± 0.084<br>2.068 ± 0.077<br>0.40<br>1.886 ± 0.064<br>1.814 ± 0.068<br>0.45<br>1.706 ± 0.067<br>1.609 ± 0.057<br>0.50<br>1.494 ± 0.066<br>1.433 ± 0.052<br>0.55<br>1.332 ± 0.059<br>1.284 ± 0.048<br>0.60<br>1.188 ± 0.045<br>1.143 ± 0.043<br>0.65<br>1.069 ± 0.039<br>1.031 ± 0.038<br>0.70<br>0.983 ± 0.039<br>0.926 ± 0.037<br>0.75<br>0.890 ± 0.036<br>0.814 ± 0.036<br>0.80<br>0.805 ± 0.034<br>0.666 ± 0.036<br>0.85<br>0.739 ± 0.033<br>0.500 ± 0.031<br>0.90<br>0.655 ± 0.032<br>0.343 ± 0.024<br>0.95<br>0.585 ± 0.028<br>0.186 ± 0.020|**4**<br>**3**<br>**2**<br>**1**|**.552 ± 0.221**<br>**.245 ± 0.149**<br>**.430 ± 0.100**<br>1.913 ± 0.065<br>**.494 ± 0.066**<br>**.188 ± 0.045**<br>**.983 ± 0.039**<br>0.817 ± 0.037<br>0.669 ± 0.032<br>**.522 ± 0.023**<br>**.410 ± 0.019**<br>0.324 ± 0.022<br>0.247 ± 0.018<br>0.182 ± 0.015<br>**.118 ± 0.013**<br>0.071 ± 0.009<br>0.037 ± 0.005<br>0.017 ± 0.002<br>0.005 ± 0.001|4.552 ± 0.221<br>3.245 ± 0.149<br>2.430 ± 0.100<br>**1.886 ± 0.064**<br>1.494 ± 0.066<br>1.188 ± 0.045<br>0.983 ± 0.039<br>**0.805 ± 0.034**<br>**0.655 ± 0.032**<br>0.522 ± 0.023<br>0.410 ± 0.019<br>**0.318 ± 0.022**<br>**0.241 ± 0.018**<br>**0.178 ± 0.015**<br>0.118 ± 0.013<br>**0.068 ± 0.009**<br>**0.035 ± 0.004**<br>**0.015 ± 0.002**<br>**0.004 ± 0.001**|
||**1**|||
||**0**|||
||**0**|||
||**0**|||
||**0**|||



26 

Dynamic Conformal Prediction for Multi-Target Regression 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0027-01.png)


**----- Start of picture text -----**<br>
( a ) Error Rate ( b ) Volume<br>**----- End of picture text -----**<br>


Figure 10: Multi-tests method’s mean error rates and volumes for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 1. 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0027-03.png)


**----- Start of picture text -----**<br>
( a ) Residuals ( b ) Residual correlation matrix<br>**----- End of picture text -----**<br>


Figure 11: Underlying model’s absolute residuals and their correlation for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 1. 

27 

Schlembach Smirnov Winands 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0028-01.png)


**----- Start of picture text -----**<br>
( a ) Bonferroni ( b ) DCP-MT<br>1.0<br>Residuals é 2.0 Test Residuals<br>0. 80<br>‘ 4 Ss2 1.5 ‘ 4<br>0.6¥o<br>fi) N<br>= “1.0<br>0.45<br>it)<br>3 0.5<br>0.2 56<br>(0)<br>0.0<br>0.0<br>0.5 1.0 1.5 . 0.0 0.5 1.0<br>rn rY<br>( c ) Empirical Copula ( d ) Max-Rank<br>**----- End of picture text -----**<br>


Figure 12: Multi-tests method’s partition of the residual space for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = 1 averaged over 20 repetitions. 

28 

Dynamic Conformal Prediction for Multi-Target Regression 

## **A.4. Synthetic, Multivariate Normal Error,** _σ_ = _−_ 0 _._ 5 

Additional results for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), _σ_ = _−_ 0 _._ 5 

Table 12: Multi-tests method’s mean error rates and standard deviations for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = _−_ 0 _._ 5. 

|_ϵh_<br>Bonferroni|DCP-MT<br>Empirical Copula|DCP-MT<br>Empirical Copula|Max-Rank|
|---|---|---|---|
|0.05<br>0.043 ± 0.004<br>0.10<br>0.090 ± 0.007<br>0.15<br>0.131 ± 0.007<br>0.20<br>0.178 ± 0.010<br>0.25<br>0.224 ± 0.009<br>0.30<br>0.262 ± 0.011<br>0.35<br>0.301 ± 0.013<br>0.40<br>0.343 ± 0.014<br>0.45<br>0.378 ± 0.015<br>0.50<br>0.418 ± 0.015<br>0.55<br>0.453 ± 0.013<br>0.60<br>0.487 ± 0.016<br>0.65<br>0.521 ± 0.013<br>0.70<br>0.550 ± 0.014<br>0.75<br>0.583 ± 0.013<br>0.80<br>0.613 ± 0.013<br>0.85<br>0.640 ± 0.012<br>0.90<br>0.669 ± 0.010<br>0.95<br>0.693 ± 0.010|**0.054 ± 0.006**<br>**0.103 ± 0.011**<br>0.150 ± 0.011<br>0.198 ± 0.010<br>0.241 ± 0.010<br>0.282 ± 0.015<br>0.328 ± 0.018<br>0.371 ± 0.018<br>0.408 ± 0.017<br>0.448 ± 0.014<br>0.490 ± 0.020<br>0.535 ± 0.024<br>0.581 ± 0.026<br>0.638 ± 0.021<br>0.699 ± 0.016<br>**0**<br>0.771 ± 0.017<br>0.832 ± 0.015<br>0.894 ± 0.013<br>0.945 ± 0.007|0.045 ± 0.005<br>0.093 ± 0.008<br>0.145 ± 0.010<br>0.195 ± 0.011<br>0.250 ± 0.010<br>0.301 ± 0.012<br>0.350 ± 0.013<br>0.402 ± 0.014<br>0.453 ± 0.013<br>0.502 ± 0.015<br>0.549 ± 0.016<br>0.598 ± 0.017<br>0.651 ± 0.013<br>0.698 ± 0.014<br>**.749 ± 0.012**<br>0.796 ± 0.009<br>0.847 ± 0.011<br>0.896 ± 0.007<br>0.944 ± 0.006|0.051 ± 0.006<br>0.097 ± 0.008<br>**0.148 ± 0.009**<br>**0.201 ± 0.011**<br>**0.253 ± 0.011**<br>**0.303 ± 0.012**<br>**0.353 ± 0.014**<br>**0.407 ± 0.014**<br>**0.457 ± 0.013**<br>**0.502 ± 0.015**<br>**0.550 ± 0.016**<br>**0.603 ± 0.016**<br>**0.655 ± 0.013**<br>**0.702 ± 0.014**<br>0.747 ± 0.011<br>**0.800 ± 0.009**<br>**0.851 ± 0.011**<br>**0.900 ± 0.007**<br>**0.946 ± 0.005**|



Table 13: Multi-tests method’s mean hyperrectangle volumes for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = _−_ 0 _._ 5. 

|_ϵh_<br>Bonferroni|DCP-MT<br>Empirical Copula|DCP-MT<br>Empirical Copula|Max-Rank|
|---|---|---|---|
|0.05<br>6.068 ± 0.230<br>0.10<br>4.519 ± 0.109<br>0.15<br>3.721 ± 0.105<br>0.20<br>3.105 ± 0.078<br>0.25<br>2.674 ± 0.063<br>0.30<br>2.374 ± 0.070<br>0.35<br>2.092 ± 0.057<br>0.40<br>1.858 ± 0.056<br>0.45<br>1.695 ± 0.059<br>0.50<br>1.506 ± 0.049<br>0.55<br>1.364 ± 0.049<br>0.60<br>1.221 ± 0.051<br>0.65<br>1.097 ± 0.039<br>0.70<br>1.002 ± 0.035<br>0.75<br>0.904 ± 0.035<br>0.80<br>0.818 ± 0.033<br>0.85<br>0.747 ± 0.030<br>0.90<br>0.669 ± 0.022<br>0.95<br>0.609 ± 0.022|**5.621 ± 0.150**<br>**4.319 ± 0.123**<br>3.532 ± 0.095<br>2.958 ± 0.069<br>2.573 ± 0.063<br>2.269 ± 0.070<br>2.005 ± 0.065<br>1.772 ± 0.057<br>1.590 ± 0.051<br>1.428 ± 0.042<br>1.289 ± 0.039<br>1.144 ± 0.038<br>1.020 ± 0.034<br>0.898 ± 0.032<br>0.779 ± 0.026<br>**0**<br>0.641 ± 0.022<br>0.500 ± 0.021<br>0.347 ± 0.020<br>0.190 ± 0.015|5.962 ± 0.239<br>4.446 ± 0.130<br>3.520 ± 0.102<br>2.950 ± 0.071<br>2.463 ± 0.068<br>2.104 ± 0.064<br>1.825 ± 0.056<br>1.583 ± 0.050<br>1.366 ± 0.047<br>1.167 ± 0.048<br>1.006 ± 0.039<br>0.862 ± 0.042<br>0.719 ± 0.036<br>0.595 ± 0.028<br>**.453 ± 0.029**<br>0.335 ± 0.026<br>0.231 ± 0.018<br>0.153 ± 0.011<br>0.079 ± 0.009|5.720 ± 0.230<br>4.384 ± 0.129<br>**3.484 ± 0.087**<br>**2.884 ± 0.069**<br>**2.443 ± 0.076**<br>**2.091 ± 0.059**<br>**1.812 ± 0.059**<br>**1.556 ± 0.048**<br>**1.347 ± 0.045**<br>**1.165 ± 0.048**<br>**1.003 ± 0.038**<br>**0.850 ± 0.041**<br>**0.710 ± 0.035**<br>**0.586 ± 0.028**<br>0.455 ± 0.028<br>**0.327 ± 0.025**<br>**0.226 ± 0.018**<br>**0.149 ± 0.011**<br>**0.076 ± 0.008**|



29 

Schlembach Smirnov Winands 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0030-01.png)


**----- Start of picture text -----**<br>
( a ) Error Rate ( b ) Volume<br>**----- End of picture text -----**<br>


Figure 13: Multi-tests method’s mean error rates and volumes for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = _−_ 0 _._ 5. 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0030-03.png)


**----- Start of picture text -----**<br>
( a ) Residuals ( b ) Residual correlation matrix<br>**----- End of picture text -----**<br>


Figure 14: Underlying model’s absolute residuals and their correlation for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = _−_ 0 _._ 5. 

30 

Dynamic Conformal Prediction for Multi-Target Regression 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0031-01.png)


**----- Start of picture text -----**<br>
( a ) Bonferroni ( b ) DCP-MT<br>1.0<br>Test Residuals oO< 175 Test<br>0. 85 1.50<br>><br>4 1.25<br>oO<br>0.62 1.00<br>Yfi) xN<br>0.45,= 0.75<br>n 0.50<br>8<br>0. 26 0.25<br>oO<br>0.00<br>0.0<br>0.5 1.0 15 2.0 . 0.0 0.5 1.0 15<br>nN lan<br>( c ) Empirical Copula ( d ) Max-Rank<br>**----- End of picture text -----**<br>


Figure 15: Multi-tests method’s partition of the residual space for the synthetic data set with _e ∼N_ ( **0** _,_ **σ** ), and _σ_ = _−_ 0 _._ 5 averaged over 20 repetitions. 

31 

Schlembach Smirnov Winands 

## **A.5. Diabetes** 

Table 14: Multi-tests method’s mean error rates and standard deviations for the diabetes (Efron et al., 2004) data set. 

|_ϵh_<br>Bonferroni|DCP-MT<br>Empirical Copula|Max-Rank|
|---|---|---|
|0.05<br>0.035 ± 0.011<br>0.10<br>0.084 ± 0.017<br>0.15<br>0.129 ± 0.021<br>0.20<br>0.171 ± 0.024<br>0.25<br>0.219 ± 0.025<br>0.30<br>0.263 ± 0.025<br>0.35<br>0.303 ± 0.024<br>0.40<br>0.349 ± 0.020<br>0.45<br>0.382 ± 0.021<br>0.50<br>0.420 ± 0.025<br>0.55<br>0.459 ± 0.027<br>0.60<br>0.495 ± 0.029<br>0.65<br>0.527 ± 0.025<br>0.70<br>0.564 ± 0.023<br>0.75<br>0.599 ± 0.021<br>0.80<br>0.629 ± 0.022<br>0.85<br>0.660 ± 0.023<br>0.90<br>0.691 ± 0.022<br>0.95<br>0.718 ± 0.023|0.049 ± 0.013<br>0.038 ± 0.012<br>**0.101 ± 0.020**<br>0.091 ± 0.018<br>**0.156 ± 0.025**<br>0.140 ± 0.024<br>**0.203 ± 0.024**<br>0.187 ± 0.024<br>**0.251 ± 0.023**<br>0.241 ± 0.026<br>**0.296 ± 0.025**<br>0.288 ± 0.025<br>0.347 ± 0.028<br>0.335 ± 0.024<br>0.396 ± 0.023<br>0.381 ± 0.024<br>0.439 ± 0.025<br>0.439 ± 0.028<br>0.481 ± 0.025<br>0.490 ± 0.027<br>0.518 ± 0.027<br>0.542 ± 0.026<br>0.566 ± 0.030<br>0.592 ± 0.029<br>0.612 ± 0.024<br>0.641 ± 0.022<br>0.663 ± 0.028<br>0.684 ± 0.023<br>0.708 ± 0.027<br>0.736 ± 0.022<br>0.762 ± 0.027<br>0.786 ± 0.020<br>0.810 ± 0.028<br>0.841 ± 0.017<br>0.879 ± 0.019<br>0.894 ± 0.018<br>0.943 ± 0.016<br>0.946 ± 0.013|**0.050 ± 0.013**<br>0.101 ± 0.017<br>0.147 ± 0.023<br>0.197 ± 0.024<br>0.247 ± 0.024<br>0.293 ± 0.026<br>**0.347 ± 0.024**<br>**0.394 ± 0.025**<br>**0.450 ± 0.028**<br>**0.501 ± 0.027**<br>**0.545 ± 0.027**<br>**0.595 ± 0.026**<br>**0.644 ± 0.023**<br>**0.694 ± 0.022**<br>**0.745 ± 0.022**<br>**0.794 ± 0.020**<br>**0.848 ± 0.016**<br>**0.899 ± 0.017**<br>**0.949 ± 0.013**|



Table 15: Multi-tests method’s mean hyperrectangle volumes for the diabetes (Efron et al., 2004) data set. 

|_ϵh_<br>Bonferroni|DCP-MT<br>Empirical Copula|Max-Rank|
|---|---|---|
|0.05<br>7.919 ± 0.943<br>0.10<br>4.795 ± 0.446<br>0.15<br>3.526 ± 0.295<br>0.20<br>2.795 ± 0.255<br>0.25<br>2.252 ± 0.159<br>0.30<br>1.895 ± 0.134<br>0.35<br>1.617 ± 0.119<br>0.40<br>1.389 ± 0.081<br>0.45<br>1.230 ± 0.074<br>0.50<br>1.078 ± 0.069<br>0.55<br>0.945 ± 0.064<br>0.60<br>0.838 ± 0.054<br>0.65<br>0.747 ± 0.046<br>0.70<br>0.658 ± 0.041<br>0.75<br>0.580 ± 0.035<br>0.80<br>0.514 ± 0.028<br>0.85<br>0.458 ± 0.030<br>0.90<br>0.405 ± 0.028<br>0.95<br>0.357 ± 0.026|6.604 ± 0.752<br>7.627 ± 0.923<br>**4.076 ± 0.369**<br>4.584 ± 0.405<br>**2.979 ± 0.226**<br>3.346 ± 0.283<br>**2.349 ± 0.170**<br>2.593 ± 0.217<br>**1.951 ± 0.129**<br>2.053 ± 0.155<br>**1.653 ± 0.107**<br>1.702 ± 0.130<br>1.414 ± 0.089<br>1.458 ± 0.103<br>1.212 ± 0.073<br>1.234 ± 0.079<br>1.051 ± 0.062<br>1.013 ± 0.073<br>0.919 ± 0.056<br>0.858 ± 0.055<br>0.820 ± 0.053<br>0.714 ± 0.046<br>0.711 ± 0.048<br>0.594 ± 0.039<br>0.618 ± 0.039<br>0.489 ± 0.025<br>0.531 ± 0.037<br>0.415 ± 0.027<br>0.453 ± 0.034<br>0.328 ± 0.027<br>0.374 ± 0.034<br>0.254 ± 0.021<br>0.302 ± 0.032<br>0.185 ± 0.020<br>0.213 ± 0.029<br>0.119 ± 0.016<br>0.118 ± 0.018<br>0.056 ± 0.011|**6.498 ± 0.784**<br>4.279 ± 0.362<br>3.191 ± 0.274<br>2.483 ± 0.200<br>2.005 ± 0.138<br>1.665 ± 0.135<br>**1.392 ± 0.093**<br>**1.181 ± 0.077**<br>**0.973 ± 0.072**<br>**0.824 ± 0.052**<br>**0.706 ± 0.048**<br>**0.586 ± 0.034**<br>**0.487 ± 0.029**<br>**0.397 ± 0.025**<br>**0.314 ± 0.027**<br>**0.242 ± 0.020**<br>**0.176 ± 0.018**<br>**0.112 ± 0.015**<br>**0.052 ± 0.010**|



32 

Dynamic Conformal Prediction for Multi-Target Regression 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0033-01.png)


**----- Start of picture text -----**<br>
( a ) Error Rate ( b ) Volume<br>**----- End of picture text -----**<br>


Figure 16: Multi-tests method’s mean error rates and volumes for the diabetes (Efron et al., 2004) data set. 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0033-03.png)


**----- Start of picture text -----**<br>
( a ) Residuals ( b ) Residual correlation matrix<br>**----- End of picture text -----**<br>


Figure 17: Underlying model’s absolute residuals and their correlation for the diabetes (Efron et al., 2004) data set. 

33 

Schlembach Smirnov Winands 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0034-01.png)


**----- Start of picture text -----**<br>
( a ) Bonferroni ( b ) DCP-MT<br>1.0 1.75<br>Test Residuals o< 1.50 Test<br>0. 80<br>3 1.25<br>0.62oO 1.00<br>YZoO gNn<br>= 0.75<br>0.45<br>a 0.50<br>0.228 0 0.25<br>oO<br>0.00<br>0.0<br>1 2 3 . 0 1 2 3<br>Mm len<br>( c ) Empirical Copula ( d ) Max-Rank<br>**----- End of picture text -----**<br>


Figure 18: Multi-tests method’s partition of the residual space for the diabetes (Efron et al., 2004) data set. 

34 

Dynamic Conformal Prediction for Multi-Target Regression 

## **A.6. Music Origin** 

Table 16: Multi-tests method’s mean error rates and standard deviations for the music origin (Zhou et al., 2014) data set. 

|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula||Max-Rank|
|---|---|---|---|---|
|0.05<br>0.042 ± 0.007<br>**0.047 ± 0.008**<br>0.10<br>0.085 ± 0.009<br>0.096 ± 0.011<br>0.15<br>0.125 ± 0.010<br>**0.140 ± 0.011**<br>0.20<br>0.164 ± 0.012<br>**0.187 ± 0.011**<br>0.25<br>0.211 ± 0.013<br>0.230 ± 0.017<br>0.30<br>0.252 ± 0.012<br>0.272 ± 0.015<br>0.35<br>0.292 ± 0.012<br>0.316 ± 0.017<br>0.40<br>0.332 ± 0.015<br>0.350 ± 0.018<br>0.45<br>0.372 ± 0.014<br>0.399 ± 0.019<br>0.50<br>0.411 ± 0.016<br>0.444 ± 0.020<br>0.55<br>0.447 ± 0.019<br>0.488 ± 0.016<br>0.60<br>0.483 ± 0.019<br>0.523 ± 0.017<br>0.65<br>0.515 ± 0.020<br>0.564 ± 0.017<br>0.70<br>0.544 ± 0.024<br>0.593 ± 0.023<br>0.75<br>0.571 ± 0.027<br>0.642 ± 0.033<br>0.80<br>0.602 ± 0.028<br>0.704 ± 0.042<br>0.85<br>0.631 ± 0.026<br>0.795 ± 0.026<br>0.90<br>0.660 ± 0.027<br>0.864 ± 0.026<br>0.95<br>0.691 ± 0.026<br>0.934 ± 0.014|**0**<br>**0**|0.048 ± 0.006<br>0.097 ± 0.010<br>0.147 ± 0.011<br>0.198 ± 0.011<br>0.246 ± 0.009<br>**.295 ± 0.013**<br>0.343 ± 0.015<br>0.396 ± 0.016<br>0.447 ± 0.016<br>**.500 ± 0.016**<br>0.551 ± 0.016<br>0.603 ± 0.016<br>0.650 ± 0.017<br>**.700 ± 0.016**<br>0.750 ± 0.015<br>0.801 ± 0.013<br>0.847 ± 0.013<br>**.896 ± 0.012**<br>**.946 ± 0.008**|**0**|0.051 ± 0.007<br>**.100 ± 0.010**<br>0.149 ± 0.011<br>0.201 ± 0.010<br>**.248 ± 0.008**<br>0.294 ± 0.013<br>**.346 ± 0.016**<br>**.398 ± 0.015**<br>**.450 ± 0.016**<br>0.501 ± 0.016<br>**.552 ± 0.016**<br>**.604 ± 0.017**<br>**.651 ± 0.018**<br>0.700 ± 0.016<br>**.751 ± 0.015**<br>**.801 ± 0.013**<br>**.848 ± 0.013**<br>0.893 ± 0.013<br>0.945 ± 0.008|
||||**0**<br>**0**<br>**0**<br>**0**<br>**0**||
||**0**||||
||||**0**||
||||**0**||
||||**0**||
||**0**<br>**0**||||
||||**0**||
||||**0**||



Table 17: Multi-tests method’s mean hyperrectangle volumes for the music origin (Zhou et al., 2014) data set. 

|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula||Max-Rank|
|---|---|---|---|---|
|0.05<br>24.417 ± 2.147<br>**22.860 ± 1.602**<br>0.10<br>18.667 ± 1.229<br>16.928 ± 1.251<br>0.15<br>14.569 ± 1.012<br>**12.774 ± 0.900**<br>0.20<br>12.321 ± 0.962<br>**10.161 ± 0.586**<br>0.25<br>9.866 ± 0.731<br>8.460 ± 0.575<br>0.30<br>8.105 ± 0.517<br>7.317 ± 0.471<br>0.35<br>7.019 ± 0.448<br>6.456 ± 0.441<br>0.40<br>6.195 ± 0.418<br>5.692 ± 0.348<br>0.45<br>5.476 ± 0.401<br>4.900 ± 0.338<br>0.50<br>4.863 ± 0.394<br>4.183 ± 0.282<br>0.55<br>4.409 ± 0.386<br>3.610 ± 0.227<br>0.60<br>4.011 ± 0.368<br>3.168 ± 0.166<br>0.65<br>3.648 ± 0.346<br>2.799 ± 0.135<br>0.70<br>3.336 ± 0.280<br>2.463 ± 0.131<br>0.75<br>3.002 ± 0.231<br>2.157 ± 0.149<br>0.80<br>2.631 ± 0.198<br>1.849 ± 0.150<br>0.85<br>2.296 ± 0.192<br>1.483 ± 0.134<br>0.90<br>1.987 ± 0.167<br>1.083 ± 0.145<br>0.95<br>1.763 ± 0.160<br>0.639 ± 0.104|**6**<br>**3**<br>**1**<br>**0**<br>**0**|23.433 ± 1.969<br>16.994 ± 1.215<br>13.190 ± 0.951<br>10.635 ± 0.868<br>8.271 ± 0.642<br>**.954 ± 0.482**<br>5.992 ± 0.481<br>5.025 ± 0.383<br>4.323 ± 0.366<br>**.642 ± 0.355**<br>3.067 ± 0.345<br>2.553 ± 0.330<br>2.086 ± 0.286<br>**.728 ± 0.250**<br>1.449 ± 0.214<br>1.223 ± 0.209<br>1.008 ± 0.186<br>**.757 ± 0.169**<br>**.447 ± 0.131**|**1**|23.237 ± 2.002<br>**6.677 ± 1.155**<br>13.074 ± 0.909<br>10.499 ± 0.849<br>**8.217 ± 0.646**<br>6.977 ± 0.482<br>**5.951 ± 0.487**<br>**4.995 ± 0.386**<br>**4.309 ± 0.363**<br>3.644 ± 0.356<br>**3.061 ± 0.346**<br>**2.544 ± 0.333**<br>**2.085 ± 0.284**<br>1.730 ± 0.248<br>**1.446 ± 0.211**<br>**1.221 ± 0.206**<br>**1.008 ± 0.188**<br>0.779 ± 0.171<br>0.462 ± 0.133|



35 

Schlembach Smirnov Winands 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0036-01.png)


**----- Start of picture text -----**<br>
( a ) Error Rate ( b ) Volume<br>**----- End of picture text -----**<br>


Figure 19: Multi-tests method’s mean error rates and volumes for the music origin (Zhou et al., 2014) data set. 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0036-03.png)


**----- Start of picture text -----**<br>
( a ) Residuals ( b ) Residual correlation matrix<br>**----- End of picture text -----**<br>


Figure 20: Underlying model’s absolute residuals and their correlation for the music origin (Zhou et al., 2014) data set. 

36 

Dynamic Conformal Prediction for Multi-Target Regression 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0037-01.png)


**----- Start of picture text -----**<br>
( a ) Bonferroni ( b ) DCP-MT<br>1.0<br>Test Residuals cc)< 3.0 Test Residuals<br>ova<br>o 2.0<br>062<br>2 S15<br>0.45a 1.0<br>o<br>0. 26 0.5<br>(0)<br>0.0<br>0.0<br>1 2 3 4 , 0 1 2 3 4<br>MN MN<br>( c ) Empirical Copula ( d ) Max-Rank<br>**----- End of picture text -----**<br>


Figure 21: Multi-tests method’s partition of the residual space for the music origin (Zhou et al., 2014) data set. 

37 

Schlembach Smirnov Winands 

## **A.7. rf1** 

Table 18: Multi-tests method’s mean error rates and standard deviations for the rf1 (Tsoumakas et al., 2011) data set. 

|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula||Max-Rank|
|---|---|---|---|---|
|0.05<br>0.037 ± 0.002<br>0.037 ± 0.002<br>0.10<br>0.071 ± 0.004<br>0.076 ± 0.005<br>0.15<br>0.105 ± 0.004<br>0.112 ± 0.005<br>0.20<br>0.138 ± 0.005<br>0.145 ± 0.004<br>0.25<br>0.171 ± 0.005<br>0.178 ± 0.005<br>0.30<br>0.201 ± 0.006<br>0.212 ± 0.007<br>0.35<br>0.231 ± 0.006<br>0.245 ± 0.006<br>0.40<br>0.261 ± 0.006<br>0.278 ± 0.007<br>0.45<br>0.290 ± 0.006<br>0.308 ± 0.007<br>0.50<br>0.319 ± 0.007<br>0.338 ± 0.007<br>0.55<br>0.345 ± 0.007<br>0.366 ± 0.008<br>0.60<br>0.372 ± 0.008<br>0.393 ± 0.008<br>0.65<br>0.398 ± 0.009<br>0.419 ± 0.009<br>0.70<br>0.422 ± 0.009<br>0.444 ± 0.009<br>0.75<br>0.447 ± 0.009<br>0.469 ± 0.009<br>0.80<br>0.471 ± 0.009<br>0.492 ± 0.009<br>0.85<br>0.494 ± 0.009<br>0.514 ± 0.010<br>0.90<br>0.516 ± 0.009<br>0.535 ± 0.010<br>0.95<br>0.537 ± 0.008<br>0.556 ± 0.009|**0**<br>**0**|0.049 ± 0.003<br>0.099 ± 0.003<br>0.149 ± 0.004<br>0.200 ± 0.005<br>0.249 ± 0.005<br>0.299 ± 0.006<br>0.350 ± 0.006<br>0.399 ± 0.006<br>**.449 ± 0.005**<br>**.500 ± 0.005**<br>**.550 ± 0.004**<br>**.600 ± 0.003**<br>**.650 ± 0.005**<br>**.700 ± 0.005**<br>**.751 ± 0.005**<br>**.800 ± 0.004**<br>**.850 ± 0.004**<br>**.901 ± 0.003**<br>**.951 ± 0.003**|**0**|**.051 ± 0.002**<br>**.102 ± 0.004**<br>**.151 ± 0.004**<br>**.202 ± 0.005**<br>**.251 ± 0.005**<br>**.301 ± 0.006**<br>**.352 ± 0.006**<br>**.401 ± 0.006**<br>0.451 ± 0.005<br>0.502 ± 0.005<br>0.551 ± 0.004<br>0.601 ± 0.003<br>0.651 ± 0.005<br>0.701 ± 0.005<br>0.751 ± 0.005<br>0.801 ± 0.004<br>0.851 ± 0.004<br>0.901 ± 0.003<br>0.951 ± 0.003|
||||**0**||
||||**0**||
||||**0**||
||||**0**||
||||**0**||
||||**0**||
||||**0**||
||||||
||**0**<br>**0**<br>**0**<br>**0**||||
||**0**||||
||**0**||||
||**0**||||
||**0**||||
||**0**||||



Table 19: Multi-tests method’s mean hyperrectangle volumes for the rf1 (Tsoumakas et al., 2011) data set. 

|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|||Max-Rank|
|---|---|---|---|---|---|
|0.05<br>172.734 ± 81.099<br>32.901 ± 14.016<br>0.10<br>7.227 ± 3.014<br>3.135 ± 1.077<br>0.15<br>1.378 ± 0.529<br>0.750 ± 0.265<br>0.20<br>0.441 ± 0.158<br>0.264 ± 0.098<br>0.25<br>0.187 ± 0.067<br>0.120 ± 0.044<br>0.30<br>0.094 ± 0.032<br>0.062 ± 0.023<br>0.35<br>0.053 ± 0.018<br>0.035 ± 0.013<br>0.40<br>0.032 ± 0.011<br>0.021 ± 0.007<br>0.45<br>0.020 ± 0.007<br>0.013 ± 0.005<br>0.50<br>0.013 ± 0.004<br>0.009 ± 0.003<br>0.55<br>0.009 ± 0.003<br>0.006 ± 0.002<br>0.60<br>0.006 ± 0.002<br>0.004 ± 0.001<br>0.65<br>0.004 ± 0.002<br>0.003 ± 0.001<br>0.70<br>0.003 ± 0.001<br>0.002 ± 0.001<br>0.75<br>0.002 ± 0.001<br>0.002 ± 0.001<br>0.80<br>0.002 ± 0.001<br>0.001 ± 0.000<br>0.85<br>0.001 ± 0.000<br>0.001 ± 0.000<br>0.90<br>0.001 ± 0.000<br>0.001 ± 0.000<br>0.95<br>0.001 ± 0.000<br>0.001 ± 0.000|3<br>**0**<br>**0**|8.125 ± 18.702<br>1.595 ± 0.617<br>0.296 ± 0.105<br>0.090 ± 0.027<br>0.036 ± 0.011<br>0.016 ± 0.005<br>0.008 ± 0.002<br>0.004 ± 0.001<br>**.002 ± 0.001**<br>**.001 ± 0.000**<br>**.001 ± 0.000**<br>**.000 ± 0.000**<br>**.000 ± 0.000**<br>**.000 ± 0.000**<br>**.000 ± 0.000**<br>**.000 ± 0.000**<br>**.000 ± 0.000**<br>**.000 ± 0.000**<br>**.000 ± 0.000**|**3**|**2.**|**341 ± 15.305**<br>**.446 ± 0.548**<br>**.282 ± 0.099**<br>**.086 ± 0.026**<br>**.035 ± 0.011**<br>**.015 ± 0.004**<br>**.007 ± 0.002**<br>**.004 ± 0.001**<br>0.002 ± 0.001<br>0.001 ± 0.000<br>0.001 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000|
|||||**1**||
|||||**0**||
|||||**0**||
|||||**0**||
|||||**0**||
|||||**0**||
|||||**0**||
|||||||
||**0**<br>**0**<br>**0**<br>**0**|||||
||**0**|||||
||**0**|||||
||**0**|||||
||**0**|||||
||**0**|||||



38 

Dynamic Conformal Prediction for Multi-Target Regression 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0039-01.png)


**----- Start of picture text -----**<br>
( a ) Error Rate ( b ) Volume<br>**----- End of picture text -----**<br>


Figure 22: Multi-tests method’s mean error rates and volumes for the rf1 (Tsoumakas et al., 2011) data set. 

Figure 23: Underlying model’s residual correlation matrix for the rf1 (Tsoumakas et al., 2011) data set. 

39 

Schlembach Smirnov Winands 

## **A.8. rf2** 

Table 20: Multi-tests method’s mean error rates and standard deviations for the rf2 (Tsoumakas et al., 2011) data set. 

|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula||Max-Rank|
|---|---|---|---|
|0.05<br>0.037 ± 0.002<br>**0.036 ± 0.002**<br>0.10<br>0.072 ± 0.003<br>0.077 ± 0.004<br>0.15<br>0.110 ± 0.004<br>0.117 ± 0.005<br>0.20<br>0.143 ± 0.004<br>0.153 ± 0.006<br>0.25<br>0.176 ± 0.005<br>0.189 ± 0.006<br>0.30<br>0.208 ± 0.005<br>0.224 ± 0.006<br>0.35<br>0.238 ± 0.006<br>0.256 ± 0.005<br>0.40<br>0.268 ± 0.005<br>0.287 ± 0.006<br>0.45<br>0.296 ± 0.005<br>0.318 ± 0.006<br>0.50<br>0.325 ± 0.006<br>0.346 ± 0.006<br>0.55<br>0.352 ± 0.006<br>0.374 ± 0.006<br>0.60<br>0.380 ± 0.006<br>0.400 ± 0.006<br>0.65<br>0.406 ± 0.007<br>0.426 ± 0.007<br>0.70<br>0.431 ± 0.007<br>0.451 ± 0.008<br>0.75<br>0.456 ± 0.007<br>0.474 ± 0.008<br>0.80<br>0.480 ± 0.008<br>0.497 ± 0.009<br>0.85<br>0.502 ± 0.009<br>0.520 ± 0.009<br>0.90<br>0.523 ± 0.008<br>0.541 ± 0.009<br>0.95<br>0.544 ± 0.008<br>0.562 ± 0.009|0.048 ± 0.002<br>0.099 ± 0.002<br>0.150 ± 0.003<br>0.199 ± 0.004<br>0.250 ± 0.004<br>0.298 ± 0.004<br>0.348 ± 0.003<br>**0.399 ± 0.004**<br>**0.449 ± 0.004**<br>**0.498 ± 0.005**<br>**0.548 ± 0.005**<br>**0.598 ± 0.005**<br>**0.648 ± 0.005**<br>**0.700 ± 0.005**<br>**0.750 ± 0.005**<br>**0.800 ± 0.004**<br>**0.851 ± 0.004**<br>**0.900 ± 0.003**<br>**0.950 ± 0.002**|**0**|0.050 ± 0.002<br>**.101 ± 0.002**<br>**.152 ± 0.003**<br>**.201 ± 0.004**<br>**.251 ± 0.004**<br>**.300 ± 0.004**<br>**.349 ± 0.003**<br>0.400 ± 0.004<br>0.450 ± 0.004<br>0.499 ± 0.005<br>0.549 ± 0.005<br>0.600 ± 0.005<br>0.649 ± 0.005<br>0.701 ± 0.005<br>0.750 ± 0.005<br>0.801 ± 0.004<br>0.851 ± 0.004<br>0.901 ± 0.003<br>0.950 ± 0.002|
|||**0**||
|||**0**||
|||**0**||
|||**0**||
|||**0**||



Table 21: Multi-tests method’s mean hyperrectangle volumes for the rf2 (Tsoumakas et al., 2011) data set. 

|_ϵ_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|_ϵ_<br>Bonferroni<br>DCP-MT<br>Empirical Copula||Max-Rank|
|---|---|---|---|
|0.05<br>87.792 ± 46.649<br>**14.946 ± 8.429**<br>0.10<br>3.260 ± 2.041<br>1.404 ± 0.725<br>0.15<br>0.651 ± 0.343<br>0.361 ± 0.172<br>0.20<br>0.229 ± 0.108<br>0.137 ± 0.065<br>0.25<br>0.103 ± 0.049<br>0.065 ± 0.030<br>0.30<br>0.054 ± 0.027<br>0.035 ± 0.016<br>0.35<br>0.031 ± 0.015<br>0.020 ± 0.009<br>0.40<br>0.019 ± 0.009<br>0.013 ± 0.005<br>0.45<br>0.012 ± 0.005<br>0.008 ± 0.004<br>0.50<br>0.008 ± 0.004<br>0.005 ± 0.002<br>0.55<br>0.005 ± 0.002<br>0.004 ± 0.002<br>0.60<br>0.004 ± 0.002<br>0.003 ± 0.001<br>0.65<br>0.003 ± 0.001<br>0.002 ± 0.001<br>0.70<br>0.002 ± 0.001<br>0.001 ± 0.001<br>0.75<br>0.002 ± 0.001<br>0.001 ± 0.000<br>0.80<br>0.001 ± 0.000<br>0.001 ± 0.000<br>0.85<br>0.001 ± 0.000<br>0.001 ± 0.000<br>0.90<br>0.001 ± 0.000<br>0.001 ± 0.000<br>0.95<br>0.001 ± 0.000<br>0.000 ± 0.000|19.484 ± 12.388<br>0.859 ± 0.398<br>0.178 ± 0.073<br>0.059 ± 0.024<br>0.023 ± 0.009<br>0.011 ± 0.004<br>0.005 ± 0.002<br>**0.003 ± 0.001**<br>**0.002 ± 0.000**<br>**0.001 ± 0.000**<br>**0.001 ± 0.000**<br>**0.000 ± 0.000**<br>**0.000 ± 0.000**<br>**0.000 ± 0.000**<br>**0.000 ± 0.000**<br>**0.000 ± 0.000**<br>**0.000 ± 0.000**<br>**0.000 ± 0.000**<br>**0.000 ± 0.000**|1<br>**0**|6.539 ± 10.866<br>**.793 ± 0.369**<br>**.171 ± 0.069**<br>**.057 ± 0.023**<br>**.023 ± 0.008**<br>**.010 ± 0.004**<br>**.005 ± 0.002**<br>0.003 ± 0.001<br>0.002 ± 0.000<br>0.001 ± 0.000<br>0.001 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000|
|||**0**||
|||**0**||
|||**0**||
|||**0**||
|||**0**||



40 

Dynamic Conformal Prediction for Multi-Target Regression 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0041-01.png)


**----- Start of picture text -----**<br>
( a ) Error Rate ( b ) Volume<br>**----- End of picture text -----**<br>


Figure 24: Multi-tests method’s mean error rates and volumes for the rf2 (Tsoumakas et al., 2011) data set. 

Figure 25: Underlying model’s residual correlation matrix for the rf2 (Tsoumakas et al., 2011) data set. 

41 

Schlembach Smirnov Winands 

## **A.9. scm1d** 

Table 22: Multi-tests method’s mean error rates and standard deviations for the scm1d (Tsoumakas et al., 2011) data set. 

|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|Max-Rank|
|---|---|
|0.05<br>0.021 ± 0.001<br>0.026 ± 0.001<br>0.050 ± 0.002<br>0.10<br>0.040 ± 0.002<br>0.047 ± 0.003<br>0.099 ± 0.003<br>0.15<br>0.061 ± 0.003<br>0.070 ± 0.004<br>0.150 ± 0.003<br>0.20<br>0.082 ± 0.003<br>0.093 ± 0.003<br>0.200 ± 0.004<br>0.25<br>0.102 ± 0.004<br>0.113 ± 0.004<br>0.249 ± 0.003<br>0.30<br>0.121 ± 0.003<br>0.134 ± 0.004<br>0.299 ± 0.003<br>0.35<br>0.141 ± 0.004<br>0.154 ± 0.004<br>0.349 ± 0.004<br>0.40<br>0.160 ± 0.004<br>0.174 ± 0.005<br>0.400 ± 0.004<br>0.45<br>0.179 ± 0.004<br>0.193 ± 0.004<br>0.449 ± 0.004<br>0.50<br>0.198 ± 0.004<br>0.212 ± 0.004<br>0.498 ± 0.004<br>0.55<br>0.216 ± 0.004<br>0.231 ± 0.004<br>0.548 ± 0.004<br>0.60<br>0.234 ± 0.004<br>0.248 ± 0.003<br>0.598 ± 0.003<br>0.65<br>0.251 ± 0.004<br>0.265 ± 0.004<br>0.649 ± 0.003<br>0.70<br>0.268 ± 0.003<br>0.282 ± 0.004<br>0.698 ± 0.004<br>0.75<br>0.283 ± 0.004<br>0.298 ± 0.004<br>0.748 ± 0.004<br>0.80<br>0.298 ± 0.003<br>0.313 ± 0.004<br>**0.799 ± 0.004**<br>0.85<br>0.313 ± 0.003<br>0.328 ± 0.004<br>**0.849 ± 0.003**<br>0.90<br>0.327 ± 0.003<br>0.342 ± 0.004<br>**0.899 ± 0.003**<br>0.95<br>0.341 ± 0.003<br>0.356 ± 0.004<br>**0.949 ± 0.003**|**0.052 ± 0.002**<br>**0.101 ± 0.002**<br>**0.152 ± 0.003**<br>**0.202 ± 0.004**<br>**0.251 ± 0.003**<br>**0.300 ± 0.003**<br>**0.350 ± 0.004**<br>**0.401 ± 0.004**<br>**0.450 ± 0.004**<br>**0.499 ± 0.004**<br>**0.549 ± 0.004**<br>**0.599 ± 0.003**<br>**0.650 ± 0.003**<br>**0.698 ± 0.004**<br>**0.749 ± 0.004**<br>0.799 ± 0.004<br>0.850 ± 0.003<br>0.900 ± 0.003<br>0.950 ± 0.003|



Table 23: Multi-tests method’s mean hyperrectangle volumes for the scm1d (Tsoumakas et al., 2011) data set. 

|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula||||Max-Rank|
|---|---|---|---|---|
|0.05<br>11387195021 ± 5455494297<br>3753203987 ± 1420280347<br>41820923 ± 11540509<br>0.10<br>161280296 ± 54689221<br>74214589 ± 23661934<br>643216 ± 117978<br>0.15<br>13872041 ± 4321745<br>7001601 ± 1918128<br>38361 ± 5326<br>0.20<br>2268132 ± 548707<br>1253055 ± 312528<br>5553 ± 838<br>0.25<br>544677 ± 126477<br>321505 ± 73152<br>1084 ± 144<br>0.30<br>167680 ± 36681<br>103735 ± 22282<br>251 ± 31<br>0.35<br>61579 ± 12268<br>39680 ± 8105<br>64.915 ± 9.348<br>0.40<br>25642 ± 4441<br>17172 ± 3199<br>17.357 ± 2.438<br>0.45<br>12098 ± 2042<br>8198 ± 1427<br>4.803 ± 0.642<br>0.50<br>6127 ± 1008<br>4216 ± 686<br>1.360 ± 0.194<br>0.55<br>3238 ± 530<br>2311 ± 360<br>0.380 ± 0.052<br>0.60<br>1777 ± 283<br>1327 ± 204<br>0.108 ± 0.015<br>0.65<br>1052 ± 162<br>794 ± 119<br>0.029 ± 0.004<br>0.70<br>650.046 ± 98.984<br>489.282 ± 71.034<br>0.008 ± 0.001<br>0.75<br>410.726 ± 59.717<br>311.254 ± 44.093<br>0.002 ± 0.000<br>0.80<br>265.403 ± 37.348<br>202.153 ± 28.171<br>**0.000 ± 0.000**<br>0.85<br>174.552 ± 23.357<br>134.516 ± 18.488<br>**0.000 ± 0.000**<br>0.90<br>118.474 ± 15.136<br>90.933 ± 12.394<br>**0.000 ± 0.000**<br>0.95<br>81.466 ± 10.949<br>62.658 ± 8.493<br>**0.000 ± 0.000**|**32**|**774**|**81**|**6 ± 8828963**<br>**65 ± 109330**<br>**5158 ± 4657**<br>**5195 ± 786**<br>**1029 ± 138**<br>**243 ± 31**<br>**322 ± 8.743**<br>**811 ± 2.355**<br>**664 ± 0.619**<br>**327 ± 0.187**<br>**371 ± 0.050**<br>**105 ± 0.015**<br>**029 ± 0.004**<br>**008 ± 0.001**<br>**002 ± 0.000**<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000<br>0.000 ± 0.000|
|||**55**|**72**|**65 **|
||||**3**<br>**62.**|**51**|
|||||**5**|
|||||**1**|
|||||**32**|
||||**16.**|**81**|
||||**4.**<br>**1.**<br>**0.**<br>**0.**<br>**0.**<br>**0.**<br>**0.**<br><br><br><br>|**66**|
|||||**32**<br>**37**<br>**10**<br>**02**<br>**00**<br>**00**<br>0.0<br>0.0<br>0.0<br>0.0|



42 

Dynamic Conformal Prediction for Multi-Target Regression 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0043-01.png)


**----- Start of picture text -----**<br>
( a ) Error Rate ( b ) Volume<br>**----- End of picture text -----**<br>


Figure 26: Multi-tests method’s mean error rates and volumes for the scm1d (Tsoumakas et al., 2011) data set. 

Figure 27: Underlying model’s residual correlation matrix for the scm1d (Tsoumakas et al., 2011) data set. 

43 

Schlembach Smirnov Winands 

## **A.10. scm20d** 

Table 24: Multi-tests method’s mean error rates and standard deviations for the scm20d (Tsoumakas et al., 2011) data set. 

|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|Max-Rank|
|---|---|
|0.05<br>0.021 ± 0.002<br>0.027 ± 0.002<br>0.049 ± 0.002<br>0.10<br>0.039 ± 0.003<br>0.049 ± 0.003<br>0.098 ± 0.004<br>0.15<br>0.062 ± 0.004<br>0.072 ± 0.004<br>0.148 ± 0.004<br>0.20<br>0.082 ± 0.004<br>0.094 ± 0.005<br>0.198 ± 0.004<br>0.25<br>0.103 ± 0.005<br>0.115 ± 0.006<br>0.248 ± 0.004<br>0.30<br>0.123 ± 0.006<br>0.134 ± 0.005<br>0.297 ± 0.004<br>0.35<br>0.141 ± 0.005<br>0.154 ± 0.006<br>0.347 ± 0.004<br>0.40<br>0.161 ± 0.005<br>0.173 ± 0.006<br>0.397 ± 0.005<br>0.45<br>0.177 ± 0.005<br>0.191 ± 0.006<br>0.448 ± 0.004<br>0.50<br>0.197 ± 0.005<br>0.209 ± 0.005<br>0.499 ± 0.005<br>0.55<br>0.213 ± 0.005<br>0.227 ± 0.005<br>0.549 ± 0.005<br>0.60<br>0.229 ± 0.006<br>0.244 ± 0.005<br>0.599 ± 0.005<br>0.65<br>0.246 ± 0.006<br>0.260 ± 0.005<br>0.649 ± 0.006<br>0.70<br>0.260 ± 0.005<br>0.276 ± 0.006<br>0.698 ± 0.005<br>0.75<br>0.277 ± 0.005<br>0.292 ± 0.006<br>0.749 ± 0.004<br>0.80<br>0.291 ± 0.006<br>0.307 ± 0.005<br>0.799 ± 0.003<br>0.85<br>0.305 ± 0.006<br>0.322 ± 0.005<br>0.849 ± 0.003<br>0.90<br>0.321 ± 0.006<br>0.336 ± 0.005<br>0.899 ± 0.004<br>0.95<br>0.334 ± 0.006<br>0.349 ± 0.006<br>**0.950 ± 0.003**|**0.051 ± 0.002**<br>**0.100 ± 0.004**<br>**0.150 ± 0.005**<br>**0.200 ± 0.004**<br>**0.250 ± 0.004**<br>**0.298 ± 0.004**<br>**0.349 ± 0.004**<br>**0.399 ± 0.005**<br>**0.449 ± 0.005**<br>**0.500 ± 0.005**<br>**0.550 ± 0.005**<br>**0.600 ± 0.005**<br>**0.650 ± 0.006**<br>**0.699 ± 0.005**<br>**0.750 ± 0.004**<br>**0.799 ± 0.003**<br>**0.850 ± 0.003**<br>**0.900 ± 0.004**<br>0.950 ± 0.003|



Table 25: Multi-tests method’s mean hyperrectangle volumes for the music scm20d (Tsoumakas et al., 2011) data set. 

|_ϵh_<br>Bonferroni<br>DCP-MT<br>Empirical Copula|||Max-Rank|
|---|---|---|---|
|0.05<br>108772471099 ± 36307263659<br>35955379066 ± 11015273007<br>1172582220 ± 345982686<br>0.10<br>3891399957 ± 1418997924<br>1592281229 ± 546138137<br>40943128 ± 14226060<br>0.15<br>399793160 ± 145477607<br>238981538 ± 83581288<br>4674176 ± 1819219<br>0.20<br>103537820 ± 36730140<br>63341800 ± 23666577<br>829646 ± 337978<br>0.25<br>31089891 ± 11904414<br>21814753 ± 8697915<br>195841 ± 80515<br>0.30<br>13073237 ± 5395580<br>9026934 ± 3807150<br>55315 ± 24220<br>0.35<br>6206213 ± 2708349<br>4190937 ± 1817270<br>17306 ± 7919<br>0.40<br>2943052 ± 1311661<br>2131334 ± 930811<br>5734 ± 2745<br>0.45<br>1625242 ± 719661<br>1158625 ± 504736<br>1884 ± 911<br>0.50<br>889071 ± 385238<br>668919 ± 293430<br>630 ± 326<br>0.55<br>549855 ± 240086<br>405368 ± 179573<br>213 ± 113<br>0.60<br>349811 ± 157026<br>254117 ± 113466<br>70.085 ± 37.083<br>0.65<br>215962 ± 94763<br>164406 ± 73801<br>22.013 ± 11.712<br>0.70<br>144915 ± 63992<br>109267 ± 49440<br>6.669 ± 3.705<br>0.75<br>94756 ± 42453<br>74518 ± 34104<br>1.778 ± 1.068<br>0.80<br>66412 ± 29466<br>51747 ± 23860<br>0.419 ± 0.265<br>0.85<br>47633 ± 21547<br>36683 ± 17061<br>0.077 ± 0.052<br>0.90<br>33008 ± 15138<br>26339 ± 12375<br>0.009 ± 0.006<br>0.95<br>24367 ± 11492<br>19200 ± 9078<br>**0.000 ± 0.000**|**9**|**42**|**799215 ± 301176043**<br>**6005596 ± 12547808**<br>**4284514 ± 1678530**<br>**784011 ± 313692**<br>**187253 ± 76667**<br>**53257 ± 23192**<br>**16618 ± 7623**<br>**5587 ± 2678**<br>**1838 ± 893**<br>**616 ± 318**<br>**208 ± 110**<br>**68.639 ± 36.429**<br>**21.671 ± 11.500**<br>**6.531 ± 3.626**<br>**1.756 ± 1.047**<br>**0.412 ± 0.261**<br>**0.075 ± 0.051**<br>**0.009 ± 0.006**<br>0.000 ± 0.000|
|||**3**||
||||**4284514 **|
||||**78401**<br>**1872**<br>**532**<br>**16**<br>**5**<br><br>**68.63**<br>**21.67**<br>**6.5**<br>**1.7**<br>**0.4**<br>**0.0**<br>**0.0**<br>0.|



44 

Dynamic Conformal Prediction for Multi-Target Regression 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0045-01.png)


**----- Start of picture text -----**<br>
( a ) Error Rate ( b ) Volume<br>**----- End of picture text -----**<br>


Figure 28: Multi-tests method’s mean error rates and volumes for the scm20d (Tsoumakas et al., 2011) data set. 

Figure 29: Underlying model’s residual correlation matrix for the scm20d (Tsoumakas et al., 2011) data set. 

45 

Schlembach Smirnov Winands 

## **Appendix B. Computational Complexity** 

This Section presents a preliminary analysis of the computational complexity of the multitests methods DCP-MT, Bonferroni predictors (Vovk, 2013), Copula CP (Messoudi et al., 2021) using the empirical copula, and Max-Rank (Timans et al., 2025). These are the methods used for the experiments in this article. 

## **B.1. Theoretical Analysis** 

We deduce the computational complexity of the compared methods when computing the prediction region for a new object **x** and a single global significance level _ϵh_ . Further work is necessary to describe computational efficiency gains that can be achieved for each method when prediction regions for multiple global significance levels _ϵh_ are computed simultaneously. 

Table 26: Multi-tests methods’ computational complexity. 

||**Bonferroni**|**DMT-CP**|**Empirical Copula**|**Max-Rank**|
|---|---|---|---|---|
|Complexity|_O_(_MN_callog(_N_cal))|_O_(2_MN_cal)|_O_(_MN_callog(_N_cal))|_O_(_MN_callog(_N_cal))|



**Bonferroni.** Computing the local significance levels _ϵm_ can be done in a single step and has a complexity _O_ (1). Next, the method determines the associated quantile for each dimension. This can be achieved through sorting and using the index _⌈_ (1 _− ϵm_ )( _N_ cal + 1) _⌉_ to get the right element, costing _O_ ( _N_ cal log( _N_ cal)) and _O_ (1), respectively. Therefore the total computational of Bonferroni CP complexity is _O_ (1) + _M_ ( _O_ ( _N_ cal log( _N_ cal)) + _O_ (1)) = _O_ ( _MN_ cal log( _N_ cal)). 

**DCP-MT.** The MILP problem has _MN_ cal binary variables and therefore a worst-case complexity of _O_ (2 _[MN]_[cal] ). 

**Copula CP.** Using the empirical copula, Copula CP first computes the _p_ -values for the residuals in each dimension in _O_ ( _MN_ cal log( _N_ cal)). Next, binary search is used to find the largest local significance _ϵm_ such that the global targeted error rate of _ϵh_ is not exceeded, requiring _O_ (log( _N_ cal)) steps, which each takes _O_ ( _MN_ cal) operations to evaluate. Finally, because the residuals are already sorted from the computation of the _p_ -values, computing the 1 _− ϵm_ quantile in each dimension can be done in _O_ ( _M_ ) time. Therefore, the total computational complexity of Copula CP is _O_ ( _MN_ cal log( _N_ cal)) + _O_ ( _N_ cal) _· O_ ( _MN_ cal) + _O_ ( _M_ ) = _O_ ( _MN_ cal log( _N_ cal)). 

**Max-Rank.** Getting the ranks of the residuals for each dimension costs _O_ ( _MN_ cal log( _N_ cal)). Computing the maximum rank for each example in the calibration set adds _O_ ( _MN_ cal) operations. The 1 _− ϵh_ quantile of the maximum ranks is computed in _O_ ( _N_ cal log( _N_ cal)). 

46 

Dynamic Conformal Prediction for Multi-Target Regression 

Finally, because the residuals are already sorted, computing the 1 _− ϵm_ quantile in each dimension can be done in _O_ ( _M_ ). Therefore, the total computational complexity of Max-Rank is _O_ ( _MN_ cal log( _N_ cal)) + _O_ ( _MN_ cal) + _O_ ( _N_ cal log( _N_ cal)) + _O_ ( _M_ ) = _O_ ( _MN_ cal log( _N_ cal)). 

## **B.2. Experimental Wall Time** 

Table 27: Total wall time across all experiments for multi-tests methods. The column _M_ = dim( **Y** ) indicates the number of dimensions in the labels space. Bold values indicate the fastest method. 


![](markdown_output/schlembach25a_images/schlembach25a.pdf-0047-04.png)


**----- Start of picture text -----**<br>
|||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Data|Set|Bonferroni|DMT-CP|Empirical|Copula|Max-Rank|M|
|synt,|e|∼|[|U|(|−|1|,|1)|, χ|[2]|2|[]]|[⊤]|0.009|31.618|1.292|0.013|2|
|synt,|e|∼N|(|0|,|σ|),|σ|=|0|0.010|31.684|1.295|0.013|2|
|synt,|e|∼N|(|0|,|σ|),|σ|=|0|.|5|0.010|32.026|1.295|0.013|2|
|synt,|e|∼N|(|0|,|σ|),|σ|=|1|0.011|35.666|1.410|0.016|2|
|synt,|e|∼N|(|0|,|σ|),|σ|=|−|0|.|5|0.010|30.828|1.272|0.013|2|
|diabetes|0.337|63.747|2.763|0.035|2|
|music|origin|0.063|146.643|8.242|0.048|2|
|rf1|0.050|696.357|50.787|0.192|8|
|rf2|0.048|698.977|50.939|0.196|8|
|scm1d|0.090|1472.797|59.414|0.400|16|
|scm20d|0.076|1326.763|50.244|0.359|16|
|Bonferroni|
|1400|DMT-CP|
|Empirical Copula|
|1200|Max-Rank|
|1000|
|800|
|600|
|400|
|200|
|0|
|2|4|6|8|10|12|14|16|
|Number of output dimensions M = dim(Y)|

**----- End of picture text -----**<br>


Figure 30: Total wall time in seconds across all experiments for multi-tests methods as a function of the number of dimensions in the labels space _M_ = dim( **Y** ). 

Table 27 and Figure 30 show the wall time for each tested method. They do not include any compute time related to training or the computation of the nonconformity scores and 

47 

Schlembach Smirnov Winands 

measure exclusively the time it took the methods to compute the forecasting regions. The conclusions that can be drawn from comparing methods based on these results are limited as these methods are not all optimised to the same degree. Furthermore, we conducted these experiments on a virtual server whose performance depends on the load on the host system which may vary over time. 

48 

