Proceedings of Machine Learning Research 266:1–21, 2025 Conformal and Probabilistic Prediction with Applications 

## **Conformal Anomaly Detection for Functional Data with Elastic Distance Metrics** 

## **Jason Adams** 

**Jason Adams** jradams@sandia.gov _Sandia National Laboratories, Albuquerque, NM, USA_ **Brandon Berman** bjberma@gmail.com _Sandia National Laboratories, Albuquerque, NM, USA_ **Joshua Michalenko** jjmich@sandia.gov _Sandia National Laboratories, Albuquerque, NM, USA_ **J. Derek Tucker** jdtuck@sandia.gov _Sandia National Laboratories, Albuquerque, NM, USA_ 

**Editor:** Khuong An Nguyen, Zhiyuan Luo, Harris Papadopoulos, Tuwe L¨ofstr¨om, Lars Carlsson and Henrik Bostr¨om 

## **Abstract** 

This paper considers the problem of outlier detection in functional data analysis with a particular focus on the more difficult case of shape outliers. We present an inductive conformal anomaly detection method based on elastic functional distance metrics. This method is evaluated and compared to similar conformal anomaly detection methods for functional data using simulation experiments. The method is also used in the analysis of a real exemplar data set that shows its utility in a practical application. The results demonstrate the efficacy of the proposed method for detecting both magnitude and shape outliers. 

**Keywords:** Anomaly detection, conformal prediction, elastic functional data analysis 

## **1. Introduction** 

Functional data are prevalent in many applications across a wide range of scientific domains (Ullah and Finch, 2013). As such, methods enabling the principled statistical analysis of functional data are important. The development and application of such methods have been rich areas of research for many years, and functional data analysis (FDA) is now a well-established branch of statistics (Ramsay and Silverman, 2005). This paper introduces a novel approach to detecting anomalous functional data. Our method leverages both the conformal prediction (CP) framework (Vovk et al., 2005) and the elastic functional data analysis (EFDA) framework (Srivastava and Klassen, 2016). Technical details regarding these frameworks are provided in Section 2. 

Functional data vary continuously over some independent variable or variables. In this work, we only consider the case where all functional data are observed over a single independent variable. Within a given set of _n_ observed functions, we assume that each function is observed over the same values of the independent variable. While this assumption is often not satisfied in practice, smoothing and interpolation methods can be used to adjust the observed data for this purpose. Although this is far from a trivial process, such methods for preprocessing functional data are outside the scope of this paper. We refer readers to Ramsay and Silverman (2005) as a starting point for smoothing and interpolation methods. 

© 2025 J. Adams, B. Berman, J. Michalenko & J.D. Tucker. 

Adams Berman Michalenko Tucker 

Throughout this paper, the terms _anomaly_ and _outlier_ are used interchangeably to describe an observation that does not fit well within a distribution. This is in line with the definition used by Aggarwal (2016) which says that “[a]n outlier is a data point that is significantly different from the remaining data.” Within this definition, there are two distinct scenarios to consider. In the first scenario, one has access to an outlier-free dataset and seeks to compare a potentially contaminated data set with the pristine one. In the second only a single data set is available and it is desired to identify the most outlying observations. The method we introduce is most appropriately used in the first scenario, so that is the focus of this paper. Consideration of the second case is reserved for future work. 

## **1.1. Related Work** 

Much previous work has been done in both functional outlier detection and conformal anomaly detection. This section reviews some of the most relevant methods and compares them to the present work. 

## 1.1.1. Functional Outlier Detection 

Numerous methods for functional outlier detection have been proposed in the literature. Many papers distinguish between _magnitude_ and _shape_ outliers. As described by Hyndman and Shang (2010), magnitude outliers “lie outside the range of the vast majority of the data” while shape outliers “may be within the range of the rest of the data but have a very different shape from other curves.” Visualization methods are often sufficient to identify magnitude outliers, but shape outliers are typically much more difficult to identify. 

Several approaches to functional outlier detection depend on visualization, aiming to extend standard univariate and multivariate techniques (e.g., boxplots) to the functional case. The primary challenge with such an extension is to determine a reasonable method for ordering functional data. A robust principal component (PC) analysis is used by Hyndman and Shang (2010) to reduce the dimensionality of the functional data. Using the first two PCs, depth and density measures are used to order the PC scores. From these orderings, three functional visualization tools — the rainbow plot, the bagplot, and the boxplot - are constructed and used to detect both magnitude and shape outliers. Similarly, Sun and Genton (2011) use the concept of band depth from L´opez-Pintado and Romo (2009) to construct functional boxplots, and Huang and Sun (2019) introduce the notion of total variation depth to order functional data and construct visualizations for detecting both magnitude and shape outliers. Arribas-Gil and Romo (2014) propose visualization tools called outliergrams, which are constructed based on metrics from L´opez-Pintado and Romo (2011). Noting that magnitude outliers are much easier to detect than shape outliers, Dai et al. (2020) apply several transformations to functional data so that shape outliers can be detected as magnitude outliers. 

Other methods of functional outlier detection do not rely on visualization. Sawant et al. (2012) develop a robust principal component method and apply a multivariate outlier detection method from Hubert et al. (2005) to the PC scores. Similarly, Yu et al. (2017) represent functional data with a B-spline basis (Ramsay and Silverman, 2005) and use the minimum covariance determinant method (Rousseeuw and Driessen, 1999) on the basis coefficients to detect outliers. Both of these methods can be viewed as using standard 

2 

Functional Conformal Anomaly Detection 

outlier detection methods on a reduced number of features extracted algorithmically from a set of functional data. In a different approach by Azcorra et al. (2018), three features are selected to measure the degree of outlyingness in terms of magnitude, shape, and amplitude respectively (note that this paper further divides what other papers call shape outliers into both shape and amplitude outliers). Thresholds are then set on these features to identify outliers. 

Additionally, several methods for functional outlier detection within the EFDA framework have also been proposed. In the method proposed by Xie et al. (2017), elastic distance metrics (discussed in more detail in Section 2 in the present work) are used to construct functional boxplots. Measures of elastic depths are introduced by Harris et al. (2021) and used to identify shape outliers. While not explicitly presented as an outlier detection method, Tucker et al. (2020) introduced functional tolerance bounds that are constructed by bootstrapping and using the EFDA boxplots of Xie et al. (2017), and these tolerance bounds can be used to identify outliers. 

While the present work does make use of the EFDA framework and can be used for detecting both magnitude and shape outliers, it differs from the above-mentioned methods in its reliance on the conformal prediction framework, which none of the others use. It also does not rely on either visualization or dimension reduction/featuriziation techniques. 

## 1.1.2. Conformal Anomaly Detection 

Within the conformal prediction literature, a number of papers have focused on the problem of detecting outliers. The method of conformal anomaly detection (CAD) was introduced by Laxhammar (2014). In a follow up work (Laxhammar and Falkman, 2015), the method of inductive conformal anomaly detection (ICAD) was proposed, and both of these focused on trajectory data. Since we will frame our proposed method as ICAD for functional data, more details on ICAD are given in Section 2. In the work of Cai and Koutsoukos (2022), ICAD is used to detect outliers in cyber-physical systems, such as autonomous vehicles, for the purpose of improving the control mechanisms of such systems. An adaptation of ICAD for univariate time series is proposed by Ishimtsev et al. (2017). A method for adjusting the outputs of ICAD algorithms to reduce the number of false positives (i.e., incorrectly labeling an observation as an outlier) is presented by Bates et al. (2023). The clearest distinction between these papers and the present work is that none of them are concerned with functional data. 

## 1.1.3. Functional Conformal Anomaly Detection 

To date, there have only been a small number of papers that use conformal prediction within a functional data context. In the work of Wang et al. (2025), EFDA methods are used with CP to provide bounds for partially observed functional data. Both Diana et al. (2023) and De Magistris et al. (2024) use CP for spatial functional data. CP has been applied to multivariate functional data and functional time series data by Diquigiovanni et al. (2022) and Ajroldi et al. (2023), respectively. However, two previous works focus on the functional outlier detection problem. First, Lei et al. (2015) introduce a CP approach to visualize classes of functional data. While the main focus of the paper is on visualization and data exploration, the method is also useful for outlier detection. In the work of Diquigiovanni 

3 

Adams Berman Michalenko Tucker 

et al. (2021), a CP method is proposed specifically for the purpose of detecting outliers in functional data. 

Given the close relationship between the methods presented by Lei et al. (2015) and Diquigiovanni et al. (2021) and the one we are proposing, we give a detailed explanation of them in Section 3 and employ them as benchmark methods in Section 4. We note that these methods were not originally presented as ICAD methods, but it is natural to frame them as such. Throughout, we will refer to the ICAD version of the method from Lei et al. (2015) as GMD (for Gaussian Mixture Density) and the ICAD version of the method from Diquigiovanni et al. (2021) as SNCM (for Supremum Non-conformity Measure). The primary difference between our proposed method and GMD and SNCM is that our method is based on the EFDA framework. 

## **1.2. Contribution and Outline** 

Our primary contribution in this work is to introduce a novel ICAD method, based on the EFDA framework, for detecting functional data outliers. We conduct empirical evaluations of this method using simulated data and compare it to both GMD and SNCM. Our results demonstrate the efficacy of our method for functional anomaly detection. 

The outline of the paper is as follows: Section 2 provides necessary details regarding EFDA, CP, and ICAD to understand our method. In Section 3, we introduce our proposed method. Section 4 describes our empirical method comparison. Our method is demonstrated on a real data exemplar in Section 5, and we conclude in Section 6. 

## **2. Preliminaries** 

## **2.1. Elastic Functional Data Analysis** 

In the analysis of functional data, there are two aspects of variability that must be considered. These are _phase_ (or _x_ -axis) variability and _amplitude_ (or _y_ -axis) variability. Figure 1 shows a sample of nine functional data observations that display both phase and amplitude variability. For instance, the two highlighted functions in Figure 1(a) vary considerably in phase but only very little in amplitude. Traditional functional data analysis often utilizes dimension reductions which can lead to a loss of fidelity and inability to detect outliers. The advantage of the EFDA framework is that it utilizes the entire function to create distance metrics that quantify the degree of separation between two functions with regard to both amplitude and phase. It also allows for estimating a Karcher mean, which is a better measure of center than a standard cross-sectional mean (Ramsay and Silverman, 2005) when functional data contain phase variability. In Figure 1(b), the grey curves are the same functional data as in panel (a), the red function is the Karcher mean, and the blue function is the cross-sectional mean. Note that in panel (b), the cross sectional mean, CSM bears little resemblance to the functional data whereas the Karcher mean is much more representative. Thus, the Karcher mean provides a better foundation for inference than the CSM. 

The math underpinning the EFDA framework is quite involved, therefore we provide only the essential details for computing amplitude and phase distances as well as the Karcher mean for a set of functional data. We refer readers who are interested in more detail on the EFDA framework to Srivastava and Klassen (2016). 

4 

Functional Conformal Anomaly Detection 


![](markdown_output/adams25b_images/adams25b.pdf-0005-01.png)


**----- Start of picture text -----**<br>
(a) (b)<br>**----- End of picture text -----**<br>


Figure 1: (a) A small sample of example functional data. (b) The same functional data observations (OBS) with the Karcher mean (KM) and cross-sectional mean (CSM) overlaid. 

Let _f_ be a real-valued and absolutely continuous function over the domain [0 _,_ 1] and _F_ be the set of all such functions[1] . As mentioned elsewhere (Tucker et al., 2013), the absolutely continuous assumption is not a restriction in practice because the observed data are always observed discretely. Let _γ_ : [0 _,_ 1] _→_ [0 _,_ 1] be a boundary preserving diffeomorphism with _γ_ (0) = 0 and _γ_ (1) = 1, and let Γ be the set of all such diffeomorphisms. We call _γ_ a _warping function_ as the composition of _f_ and _γ_ , _f ◦ γ_ , effectively warps the function _f_ but maintains the original domain over which _f_ is defined. Also, we denote the _square root slope function_ 

(SRSF) of a function _f_ by _q_ : [0 _,_ 1] _→_ R such that _q_ ( _t_ ) = sign( _f_[˙] ( _t_ )) _|f_[˙] ( _t_ ) _|_ where the dot over a function indicates its derivative with respect to _t_ . Similarly, we denote the SRSF of ˙ the warping function to be _ψ_ . However, since _γ >_ 0 and _γ >_ 0 for all _t ∈_ [0 _,_ 1], then the ˙ SRSF of _γ_ is simplified to _ψ_ = _[√] γ_ . 

## 2.1.1. Elastic Distance Metrics 

Let _f_ 1, _f_ 2 _∈F_ and _q_ 1, _q_ 2 be their corresponding SRSFs. The amplitude distance between _f_ 1 and _f_ 2 is defined as 


![](markdown_output/adams25b_images/adams25b.pdf-0005-07.png)


where _|| · ||_ represents the functional L[2] metric[2] . The warping function, _γ_ , which optimizes the distance in Equation 1 is typically identified in practice through the Dynamic Programming algorithm (Bertsekas, 2012). Intuitively, the optimal warping function, _γ_ , not only minimizes the distance from _q_ 2 to _q_ 1, but also effectively aligns _f_ 2 to _f_ 1 as ( _q_ 2 _◦ γ_ ) _[√] γ_ ˙ is the 

> 1. In practice, the function _f_ can be defined over any closed interval of the form [ _a, b_ ] _⊂_ R. This is typically done by simply rescaling the interval [0 _,_ 1] to [ _a, b_ ]. 

> 2. Note that this is the Fisher-Rao metric and a proper distance. If we compute this distance using _f_ directly, then it is not a proper distance and hence the reason that the SRSF transformation is used. 

5 

Adams Berman Michalenko Tucker 

SRSF of _f_ 2 _◦ γ_ . For all EFDA computations herein, we use the `fdasrvf` package (version 2.3.4) (Tucker, 2017) within the `R` programming language (R Core Team, 2023). For two warping functions, _γ_ 1, _γ_ 2 _∈_ Γ, the distance between them is computed as 


![](markdown_output/adams25b_images/adams25b.pdf-0006-02.png)


where _ψ_ 1 and _ψ_ 2 are the SRSFs of _γ_ 1 and _γ_ 2, respectively. In order to find the phase distance between two functions, _f_ 1 _, f_ 2 _∈F_ , we first find the optimal warping function from _f_ 2 to _f_ 1. Again, denote this function as _γ_ . Next the warping function from _f_ 1 to itself is simply the identity function ( _γI_ ( _t_ ) = _t_ ), and the SRSF of the identity function is the ˙ constant function equal to one (� _γI_ ( _t_ ) = 1). Thus, the phase distance between _f_ 2 and _f_ 1 simplifies to 


![](markdown_output/adams25b_images/adams25b.pdf-0006-04.png)


where _ψ_ is the SRSF of the optimal warping function _γ_ that aligns _f_ 2 to _f_ 1. This simplification occurs because the space of all _ψ_ s forms a Hilbert Sphere (see Tucker et al., 2013). 

## 2.1.2. Karcher Mean 

Let _f_ 1 _, . . . , fn_ represent a set of functions from the function space _F_ and _q_ 1 _, . . . , qn_ be their respective SRSFs. The Karcher mean of _f_ 1 _, . . . , fn_ is given by 


![](markdown_output/adams25b_images/adams25b.pdf-0006-08.png)


Equivalently, we can define the Karcher mean of the SRSFs, _q_ 1 _, . . . , qn_ , as 


![](markdown_output/adams25b_images/adams25b.pdf-0006-10.png)


Note that _µq_ is the SRSF of _µf_ . The algorithm used in the `fdasrvf R` package finds _µq_ and then transforms it to _µf_ . 

The transformation from SRSF space back to the original function space, assuming a generic function _f_ and its SRSF _q_ , is 


![](markdown_output/adams25b_images/adams25b.pdf-0006-13.png)


where _f_ ( _t_ 0) is the function value at the initial time point, _t_ 0. When obtaining _µf_ from _µq_ , the initial value is computed as _n[−]_[1][ �] _[n] i_ =1 _[f][i]_[(] _[t]_[0][).] 

6 

Functional Conformal Anomaly Detection 

## **2.2. Conformal Prediction and ICAD** 

Conformal prediction was first introduced by Vovk et al. (2005) as a distribution-free approach to obtaining valid uncertainty quantification (UQ). It has recently been gaining popularity in the machine learning literature as a computationally efficient means to obtain high quality UQ with many data types and different classes of models (Angelopoulos and Bates, 2021; Zhou et al., 2024). Let ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _∼PX×Y_ be an _i.i.d_ random sample and _Xn_ +1 be a test point with _Yn_ +1 the unobserved label associated with the test point _Xn_ +1. For simplicity, we use the notation _Zi_ = ( _Xi, Yi_ ). CP methods produce a _prediction set_ , _C_ ( _Xn_ +1), for the test point _Xn_ +1, such that _P_ ( _Yn_ +1 _∈ C_ ( _Xn_ +1)) _≥_ 1 _− α_ for any level of significance, _α ∈_ (0 _,_ 1). This property is known as the marginal coverage guarantee, and we note that it also holds under the weaker assumption of exchangeability of _Z_ 1 _, . . . , Zn,_ ( _Xn_ +1 _, Yn_ +1). 

To produce a prediction set, a _non-conformity measure_ (NCM) must first be defined. The NCM is a function that measures how well _Zi_ conforms with the other observations. In the original formulation of CP, NCM values are computed for all _Zi_ , _i ∈{_ 1 _, . . . , n, n_ + 1 _}_ , relative to the set _Z_ ( _−i_ ) = _{Zj,_ : _j_ = 1 _, . . . , i −_ 1 _, i_ + 1 _, . . . , n, n_ + 1 _}_ . For NCMs that incorporate information from the entire set _Z_ ( _−i_ ), this process can become computationally expensive. 

_Inductive_ CP (ICP) is an alternative approach that has a lower computational burden at the cost of less efficient use of available data. ICP randomly splits all available observations for training into two sets: a _training data set_ and a _calibration data set_ . The purpose of the training data set is to fit a base model which relates the object _X_ to the label _Y_ . Meanwhile, the purpose of the calibration data set is to evaluate the NCM. For clarity, we use the term _full training data set_ to refer to all observations available for training and denote this set as _D[full]_ = _{Z_ (1) _, . . . , Z_ ( _n_ ) _}_ . Similarly, we denote the training and calibration sets, respectively, as _D[tr]_ = _{Z_ 1 _, . . . , Zn_ 1 _}_ , and _D[cal]_ = _{Zn_ 1+1 _, . . . , Zn_ 1+ _n_ 2 _}_ (note the parentheses in subscripts of _D[full]_ are intended to emphasize that the observations in _D[full]_ are indexed differently than those in _D[tr]_ and _D[cal]_ , due to random splitting). Let _I[tr]_ = _{_ 1 _, . . . , n_ 1 _}_ and _I[cal]_ = _{n_ 1 + 1 _, . . . , n_ 1 + _n_ 2 _}_ represent the indices of the observations in _D[tr]_ and _D[cal]_ , respectively. Throughout this work, we take _n_ 1 = � 32 _[n]_ � and _n_ 2 = _n − n_ 1 where _⌈·⌉_ is the ceiling function. To construct a prediction set for a test observation, _Zn_ +1, the NCM is computed and compared to the NCM values obtained by evaluating the NCM on the calibration data set. 

In this work, we use the p-value approach to constructing prediction sets. Let _sn_ 1+ _i_ = _s_ ( _Zn_ 1+ _i_ ; _D[tr]_ ) represent the NCM value of the _i[th]_ calibration observation and _s[y] n_ +1[=] _s_ (( _Xn_ +1 _, y_ ); _D[tr]_ ) be the NCM value of the test point where _y_ is the assumed value of _Yn_ +1, the label associated with _Xn_ +1. The p-value corresponding to _Xn_ +1 is then computed as 


![](markdown_output/adams25b_images/adams25b.pdf-0007-06.png)


In traditional CP, when _p[y] n_ +1 _[≥][α]_[,][the][assumed][value,] _[y]_[,][of][the][label] _[Y][n]_[+1][,][is][one][element] that defines the prediction set, _C_ ( _Xn_ +1). In the case of ICAD, there is no reliance upon the label, and to simplify the notation we drop the superscript _y_ and denote the p-value as _pn_ +1. If exchangeability assumptions hold and _pn_ +1 _≥ α_ , then _Zn_ +1 is labeled as an 

7 

Adams Berman Michalenko Tucker 

inlier with (1 _− α_ ) _·_ 100% confidence. Otherwise, _Zn_ +1 is labeled an outlier. Note that the marginal coverage guarantee is only applicable to inliers and not to outliers. Also, we must use _α ≥ n_ 21+1[or][all][test][points][will][automatically][be][labeled][as][inliers.] 

## **3. Elastic Functional Distance Metrics ICAD** 

Our proposed method is ICAD where the NCM is based on elastic functional distances and the Karcher mean. We call this method _elastic functional distance metrics_ ICAD, or EFDM. Let _D[full]_ = _{f_ (1) _, . . . , f_ ( _n_ ) _}_ be the full training data set of functional data observations. Further assume _f_ (1) _, . . . , f_ ( _n_ ) _∼PF_ are exchangeable, where _PF_ is a probability distribution over the function space _F_ . Using random assignment we create _D[tr]_ = _{f_ 1 _, . . . , fn_ 1 _}_ and _D[cal]_ = _{fn_ 1+1 _, . . . , fn_ 1+ _n_ 2 _}_ . As described in Section 1, we also assume that all functional observations are measured at the same points in the domain. We denote these domain points as _T_ = _{t_ 0 _, t_ 1 _, . . . , tM }_ . 

To label a new function _fn_ +1 as an inlier or outlier using a level of significance _α_ , EFDM proceeds as follows: 

1. Compute the Karcher mean of the training data set _D[tr]_ , denoted as _µtr_ . 

2. Compute the sets _d[tr] a_[=] _[{][d][a]_[(] _[µ][tr][, f][i]_[):] _[i][∈I][tr][}]_[and] _[d][tr] p_[=] _[{][d][p]_[(] _[µ][tr][, f][i]_[):] _[i][∈I][tr][}]_[.][Let] _mina_ = min _d[tr] a_[,] _[max][a]_[= max] _[ d][tr] a_[,] _[min][p]_[= min] _[ d][tr] p_[,][and] _[max][p]_[= max] _[ d][tr] p_[.] 

3. Compute _d[cal] a i_[=] _[d][a]_[(] _[µ][tr][, f][n]_ 1[+] _[i]_[)][and] _[d][cal] p i_[=] _[d][p]_[(] _[µ][tr][, f][n]_ 1[+] _[i]_[),][the][amplitude][and][phase] distances from the Karcher mean to each function in the calibration data. 

4. Compute the NCM for each calibration observation as 


![](markdown_output/adams25b_images/adams25b.pdf-0008-09.png)


5. Compute _d[ts] a_[=] _[d][a]_[(] _[µ][tr][, f][n]_[+1][)][and] _[d][ts] p_[=] _[d][p]_[(] _[µ][tr][, f][n]_[+1][),][the][amplitude][and][phase][dis-] tances from the Karcher mean to the test function. 

6. Compute the NCM for the test function as 


![](markdown_output/adams25b_images/adams25b.pdf-0008-12.png)


7. Compute the p-value, _pn_ +1, as in equation (7). If _pn_ +1 _< α_ , _fn_ +1 is labeled as an outlier; else it is labeled as an inlier. 

As seen in steps 4 and 6, the NCM used for EFDM is the average of the standardized amplitude and phase distances from an observation to the Karcher mean of the training data. This standardization is important so that both the amplitude and phase components are unitless and can contribute equally to the NCM. We now describe several potential adjustments to this NCM. 

8 

Functional Conformal Anomaly Detection 

The basic NCM given above is primarily intended to detect shape outliers. This approach will also detect magnitude outliers if they are outlying _on the x-axis_ (phase distance will properly account for these). However, magnitude outliers that are outlying predominately in the _y_ direction may not be accounted for by amplitude distance, due to the differentiation when transforming a function to SRSF space. Thus, magnitude outliers that are essentially vertical shifts of observations in the data will not be detected. To enable the detection of such magnitude outliers, _translation distance_ can be incorporated into the NCM. To do this we compute _|µtr_ ( _tk_ ) _− fi_ ( _tk_ ) _|_ where _tk_ is a point in the domain where the vertical shift is prominent. Once the translation distance is standardized it can be included alongside the standardized phase and amplitude distances as well. The final NCM is then the average of the three standardized distances. 

Another possible adjustment is to allow for different weightings of the amplitude and phase (and potentially translation) distance components so that the NCM is a weighted average rather than a simple arithmetic mean. While a functional data set that displays more amplitude than phase variability, or vice versa, is not a problem because we standardize the distances, there may still be cases when it is desirable to weight one component higher than the other. Taking this to an extreme, it is also possible to use only one of the components if, for instance, we know _a prioi_ that there is only one type of variability in a data set. We caution against this, however. Suppose a functional data set that contains only amplitude variability is used in the EFDM algorithm with only amplitude distance in the NCM. If a new observation looks similar to the training data in amplitude but varies in phase, it will not be marked as an outlier. 

Finally, smoothed conformal prediction (Vovk et al., 2005) is often used to guarantee exact asymptotic validity. This is carried out by adjusting the p-value computation to 


![](markdown_output/adams25b_images/adams25b.pdf-0009-04.png)


where _τ_ is a random draw from the _U_ (0 _,_ 1) distribution. In all of our computations, we use these smoothed conformal p-values. Other p-value adjustments are possible and may be desirable, depending on the use case (see, e.g., Bates et al., 2023). 

## **3.1. Other Functional ICAD Methods** 

In this section, we frame the methods of Lei et al. (2015) and Diquigiovanni et al. (2021) as functional ICAD methods for comparison to EFDM. 

## 3.1.1. GMD 

The GMD ICAD method begins by projecting the functional data to a lower-dimensional space. In our case, we use functional principal component analysis (FPCA) (Ramsay and Silverman, 2005) to achieve the projection, but other projection methods could be used. Let _ξij_ = _⟨fi, θj⟩_ be the _j[th]_ component of the projected functional observation, _fi_ for _i_ = 1 _, . . . , n_ and _j_ = 1 _, . . . , p_ . Here, _θj_ represents the _j[th]_ functional principal component and _⟨·, ·⟩_ is the functional inner product (Ramsay and Silverman, 2005). The projection of _fi_ can then be written as _ξi_ = ( _ξi_ 1 _, . . . , ξip_ ). Note that the FPCs are estimated using only the training data, and all training, calibration, and test data use the same FPCs for projection to _ξi_ . 

9 

Adams Berman Michalenko Tucker 

The projected data are modeled with a Gaussian mixture model (GMM) (Hastie et al., 2009) with _K_ components. From the projected version of the training data, _Dξ[tr]_[=] _[ {][ξ]_[1] _[, . . . , ξ][n]_ 1 _[}]_[,] the mean, covariance and mixture proportions are learned. We denote the fitted GMM as 


![](markdown_output/adams25b_images/adams25b.pdf-0010-02.png)


where _ϕ_ ( _·_ ; _µ,_ Σ) represents the multivariate normal density with mean vector _µ_ and covariance matrix Σ, and the _π_ ˆ _k_ are the estimated mixing proportions. The NCM is then computed as _si_ ( _ξi_ ) = _−_ 1 _· G_ ( _ξi_ ), hence the name Gaussian mixture density (GMD) for this approach[3] . We also implement a refinement that was introduced by Lei et al. (2015) to provide a narrower prediction band. With the GMD maximum (GMDM) refinement, the NCM is instead computed as 


![](markdown_output/adams25b_images/adams25b.pdf-0010-04.png)


We wrote our own implementations of GMD and GMDM in `R` that can be found on Github. Our code uses the `mclust` package (version 6.1.1) (Scrucca et al., 2023) and the `mvtnorm` package (version 1.3.1) (Genz et al., 2021). 

## 3.1.2. SNCM 

In the work of Diquigiovanni et al. (2021), the proposed NCM is computed as 


![](markdown_output/adams25b_images/adams25b.pdf-0010-08.png)


where _m_ ( _t_ ) is a mean function and _r_ ( _t_ ) is a modulation function, and both of these are estimated from only the training data. Because this NCM uses the supremum, we refer to this method as supremum non-conformity measure (SNCM) ICAD. For the mean function, only the cross-sectional mean function is used by Diquigiovanni et al. (2021). For the modulation function, the authors compare three options: _r_ ( _t_ ) = 1; the cross-sectional standard deviation function; and what is referred to as the optimal modulation function. The optimal modulation function is defined as 


![](markdown_output/adams25b_images/adams25b.pdf-0010-10.png)


where 


![](markdown_output/adams25b_images/adams25b.pdf-0010-12.png)


where _ν_ is the _⌈_ ( _n_ 1 + 1)(1 _− α_ ) _⌉[th]_ smallest value of the set _{_ sup _t∈T |fi_ ( _t_ ) _− m_ ( _t_ ) _|_ : _i ∈ D[tr] }_ . 

We wrote our own implementation of SNCM in `R` that can be found on Github. Our code made use of the `fdasrvf` package (version 2.3.4) and the `caTools` package (version 1.18.3) (Tuszynski and Dietze, 2024). 

> 3. Note that Lei et al. (2015) use a _conformity_ measure rather than a non-conformity measure, so they simply compute the density rather than the negative density. The two approaches are equivalent. 

10 

Functional Conformal Anomaly Detection 

## **4. Simulation Experiments** 

In this section, we empirically evaluate the performance of the methods described in Section 3. Magnitude outliers, as mentioned in Section 1.1.1, are the easier case, so these experiments focus instead on detecting shape outliers. 

## **4.1. Experiment Data** 

These experiments use functional data generated from three different templates. These are the _standard_ , _narrow_ , and _double peaked_ templates. Respectively, they are given as: 


![](markdown_output/adams25b_images/adams25b.pdf-0011-05.png)


To generate functional data from these templates, we randomly generate values for the _a_ and _p_ parameters. Figure 2 shows randomly generated data from each of these templates. Panel (a) contains 500 standard functions, panel (b) contains 50 narrow functions, and panel (c) contains 50 double peaked functions. The standard and narrow data sets were generated using _a ∼ N_ ( _µ_ = 1 _, σ_ = 0 _._ 15) and _p ∼ N_ (0 _,_ 1 _._ 75). The double peaked functions were generated with _a ∼ N_ (1 _,_ 0 _._ 10) and _p ∼ N_ (0 _,_ 0 _._ 15). The domain points for all generated functions are 250 equally spaced points over the interval [ _−_ 8 _,_ 8]. Treating the standard data as inliers, the key thing to note about both the narrow and double peaked data is that these are _shape-only_ outliers. In terms of magnitude, they fit well within the distribution of the standard data. 


![](markdown_output/adams25b_images/adams25b.pdf-0011-07.png)


**----- Start of picture text -----**<br>
(a) (b) (c)<br>**----- End of picture text -----**<br>


Figure 2: Randomly generated data sets. (a) 500 standard functions, (b) 50 narrow functions, and (c) 50 double peaked functions. These are also the test sets for the first experiment. 

## **4.2. Experiment 1** 

The goal of the first experiment is two-fold: first, we investigate the coverage of the ICAD methods over inlier and outlier functions separately. Second, we consider the effect of 

11 

Adams Berman Michalenko Tucker 

sample size on the coverage. Using full training data set sizes of _n_ = 50, 100, and 250, we randomly generate 500 data sets using the standard template. That is, there are 1500 total simulated full training data sets for this experiment. Each of the 1500 data sets are run through the ICAD methods, and inlier/outlier labels are assigned to each function in three different test sets. The first test set consists of 500 standard functions generated with the same parameters as the full training sets (these are the inlier functions). The second test set contains 50 narrow functions, and the third contains 50 double peaked functions. Both the second and third test sets are outliers relative to the training data. These test sets are shown in Figure 2. 

|Method Name|Details|
|---|---|
|EFDM<br>SNCM1<br>SNCM2<br>GMD1<br>GMD2<br>GMD3<br>GMDM|NCM uses amplitude and phase distances only<br>Uses the cross-sectional mean function and the optimal modulation function<br>Uses the Karcher mean and the optimal modulation function<br>Uses _p_= 2, _K_ = 1<br>Uses _p_= 3, _K_ = 2<br>Uses _p_= 5, _K_ = 2<br>Uses _p_= 5, _K_ = 2|



Table 1: Description of methods used for experiment 1. 

Table 1 details each method used for this experiment. For each simulated data set, inlier/outlier labels were obtained for every functional observation in the three test sets using a significance level of _α_ = 0 _._ 10. The coverage for a single simulated data set is simply the proportion of test functions marked as inliers (this can be viewed as the coverage averaged over the test functions). These proportions are then averaged over all 500 simulated data sets that have the same sample size to provide the final mean coverage estimate for a method. These values, along with the standard deviation over the simulated data sets, are given in Tables 2 and 3. Table 2 contains results from the standard test set where the mean coverage values should be close to 1 _− α_ = 0 _._ 90. Table 3 contains results from the narrow and double peaked test sets where mean coverage values close to 0 are desirable. Note that the values for GMD3 and GMDM are missing because, with some of the full training sets of size _n_ = 50 and _n_ = 100, the GMMs could not be fit. In all tables, bolded values represent the best value(s) in each column. 

||Standard Test Data|Standard Test Data|Standard Test Data|
|---|---|---|---|
|Method|_n_= 50|_n_= 100|_n_= 250|
|EFDM|0_._893(0_._07)|0_._895(0_._05)|**0.901 (0.03)**|
|SNCM1|**0.900 (0.06)**|**0.899 (0.05)**|**0.899 (0.03)**|
|SNCM2|0_._901(0_._06)|**0.899 (0.05)**|0_._903(0_._03)|
|GMD1|0_._901(0_._07)|**0.899 (0.05)**|0_._905(0_._04)|
|GMD2|**0.900 (0.06)**|**0.899 (0.05)**|**0.901 (0.03)**|
|GMD3|_−_|_−_|**0.901 (0.03)**|
|GMDM|_−_|_−_|0_._884(0_._03)|



Table 2: Mean(SD) coverage results from experiment 1 for the standard test data. 

12 

Functional Conformal Anomaly Detection 

||Narrow Test Data|Narrow Test Data|Narrow Test Data|Double Peaked Test Data|Double Peaked Test Data|Double Peaked Test Data|
|---|---|---|---|---|---|---|
|Method|_n_= 50|_n_= 100|_n_= 250|_n_= 50|_n_= 100|_n_= 250|
|EFDM|**0.052(0.13)**|**0.001(0.02)**|**0(0)**|**0.001(0.01)**|**0(0)**|**0(0)**|
|SNCM1|0_._927(0_._08)|0_._911(0_._06)|0_._888(0_._04)|0_._972(0_._08)|0_._982(0_._04)|0_._991(0_._03)|
|SNCM2|0_._927(0_._09)|0_._908(0_._07)|0_._882(0_._08)|0_._966(0_._08)|0_._978(0_._05)|0_._992(0_._03)|
|GMD1|0_._992(0_._02)|0_._997(0_._01)|0_._999(0_._002)|0_._999(0_._002)|1(0)|1(0)|
|GMD2|0_._889(0_._13)|0_._900(0_._09)|0_._912(0_._04)|0_._389(0_._34)|0_._241(0_._26)|0_._131(0_._17)|
|GMD3|_−_|_−_|0_._542(0_._19)|_−_|_−_|0_._170(0_._21)|
|GMDM|_−_|_−_|0_._487(0_._19)|_−_|_−_|0_._104(0_._15)|



Table 3: Mean(SD) coverage results from experiment 1 for the narrow and double peaked test data and standard functions as training/calibration data. 

The results of Table 2 utilize full training and testing data sets that are comprised of standard functions. Thus, the mean coverage values, as seen in Table 2, are all very close to 0 _._ 90 for all methods. The only effect of sample size seems to be to reduce the variability in the coverage estimates for each data set, as would also be expected. From this table, no methods stand out as outperforming the others. In the online supplementary material, we include plots that show that different methods achieve the correct average coverage in distinct ways. 

The performance of the methods is much more variable in Table 3. Here, EFDM has the best performance in every case. With enough training data ( _n_ = 250 for the narrow data and _n_ = 100 for the double peaked), it never labels outliers as inliers in any of the 500 runs. Both SNCM methods perform poorly, but the coverage does decrease somewhat as sample size increases for the narrow test data. This pattern, however, does not hold for the double peaked data. GMD1 has the worst performance of any method in every case. GMD2 performs poorly on the narrow test data but much better on the double peaked data. GMD3 and GMDM perform better on the narrow test data than the other GMD and SNCM methods, and they even outperform GMD2 on the double peaked data. 

## **4.3. Experiment 2** 

In experiment 2, our goal is to simulate the first outlier detection scenario where the training and calibration data contain no outliers and external data, which may contain outliers, are labeled using the ICAD methods. In this experiment, we reuse the same 1500 full training data sets from experiment 1 (so there are 500 data sets for each sample size, _n_ = 50, _n_ = 100, and _n_ = 250). Each full training set has two corresponding test sets containing 100 functional observations each. One test set contains 95% inliers (i.e., they are simulated using the standard template function and the same normal distribution parameters as the full training data) and 5% double peaked outliers, simulated with the same parameters as the double peaked test data in experiment 1. The other test set contains 90% inliers and 10% double peaked outliers. 

Each full training data set is randomly split into training and calibration data, and each of the methods from Table 1 are used to assign inlier/outlier status to all functions in both test data sets. For each test data set, we examine the effects of using two different levels of significance, _α_ = 0 _._ 05 and _α_ = 0 _._ 10. Method performance is assessed using the Matthew’s 

13 

Adams Berman Michalenko Tucker 

correlation coefficient (MCC) (Matthews, 1975), which has been shown to perform well in cases of extreme class imbalance (Chicco et al., 2021). MCC values close to 1 indicate better performance (or higher positive correlation between predictions and ground truth labels) while values close to 0 indicate poor performance (little correlation between predictions and ground turth labels). Since it is a correlation, MCC can also be negative (indicating negative correlation between predictions and ground truth labels). For this experiment, the double peaked outliers are treated as the positive class. MCC is computed for each test set, and the mean and standard deviation over the 500 full training sets (per sample size) are given in Tables 4 and 5. As in experiment 1, values are missing for GMD3 and GMDM when _n_ = 50 and _n_ = 100. Additional metrics from this experiment are given in the online supplementary material. 

||5% Outliers in Test Data|5% Outliers in Test Data|5% Outliers in Test Data|10% Outliers in Test Data|10% Outliers in Test Data|10% Outliers in Test Data|
|---|---|---|---|---|---|---|
|Method|_n_= 50|_n_= 100|_n_= 250|_n_= 50|_n_= 100|_n_= 250|
|EFDM|**0.668(0.19)**|**0.734(0.14)**|**0.728(0.12)**|**0.735(0.15)**|**0.818(0.11)**|**0.817(0.10)**|
|SNCM1|_−_0_._033(0_._05)|_−_0_._037(0_._04)|_−_0_._044(0_._03)|_−_0_._049(0_._06)|_−_0_._058(0_._04)|_−_0_._063(0_._04)|
|SNCM2|_−_0_._027(0_._06)|_−_0_._034(0_._05)|_−_0_._044(0_._03)|_−_0_._042(0_._07)|_−_0_._053(0_._05)|_−_0_._062(0_._04)|
|GMD1|_−_0_._043(0_._03)|_−_0_._048(0_._03)|_−_0_._049(0_._02)|_−_0_._062(0_._04)|_−_0_._067(0_._03)|_−_0_._068(0_._03)|
|GMD2|0_._276(0_._27)|0_._353(0_._24)|0_._426(0_._22)|0_._342(0_._28)|0_._428(0_._25)|0_._508(0_._21)|
|GMD3|_−_|_−_|0_._403(0_._27)|_−_|_−_|0_._464(0_._28)|
|GMDM|_−_|_−_|0_._435(0_._24)|_−_|_−_|0_._522(0_._24)|



Table 4: Mean(SD) MCC values for experiment 2 using _α_ = 0 _._ 05. 

||5% Outliers in Test Data|5% Outliers in Test Data|5% Outliers in Test Data|10% Outliers in Test Data|10% Outliers in Test Data|10% Outliers in Test Data|
|---|---|---|---|---|---|---|
|Method|_n_= 50|_n_= 100|_n_= 250|_n_= 50|_n_= 100|_n_= 250|
|EFDM|0**.601(0.16)**|**0.589(0.14)**|**0.578(0.10)**|**0.710(0.14)**|**0.702(0.11)**|**0.697(0.09)**|
|SNCM1|_−_0_._046(0_._07)|_−_0_._051(0_._06)|_−_0_._059(0_._05)|_−_0_._066(0_._08)|_−_0_._081(0_._06)|_−_0_._085(0_._05)|
|SNCM2|_−_0_._042(0_._07)|_−_0_._048(0_._07)|_−_0_._059(0_._05)|_−_0_._059(0_._08)|_−_0_._070(0_._06)|_−_0_._085(0_._05)|
|GMD1|_−_0_._070(0_._03)|_−_0_._073(0_._02)|_−_0_._072(0_._02)|_−_0_._098(0_._04)|_−_0_._103(0_._04)|_−_0_._102(0_._03)|
|GMD2|0_._359(0_._23)|0_._444(0_._17)|0_._495(0_._12)|0_._440(0_._26)|0_._546(0_._17)|0_._609(0_._13)|
|GMD3|_−_|_−_|0_._479(0_._16)|_−_|_−_|0_._588(0_._15)|
|GMDM|_−_|_−_|0_._473(0_._11)|_−_|_−_|0_._596(0_._11)|



Table 5: Mean(SD) MCC values for experiment 2 using _α_ = 0 _._ 10. 

Both Tables 4 and 5 exhibit similar patterns to those seen in Table 3. As in the previous experiment, EFDM outperforms all other methods in each case. The performance gap between EFDM and the other methods is larger when _α_ = 0 _._ 05 than when _α_ = 0 _._ 10. In fact, when _α_ = 0 _._ 10 the mean MCC for EFDM is within one standard deviation of the mean MCC for GMD2 (and GMD3 and GMDM when applicable). In both tables, SNCM1, SNCM2, and GMD1 consistently perform poorly, registering negative MCC values in every case. 

14 

Functional Conformal Anomaly Detection 

## **4.4. Experiment Conclusions** 

There are several conclusions to be drawn from these results. As discussed, shape outliers are harder to detect than magnitude outliers, and we intended the narrow and double peaked outliers to be a particularly difficult case of shape outliers relative to our standard simulated data. When plotted, both narrow and double peaked outliers fit well within the standard data. The narrow data are also only very slightly different in shape than the standard data. We note that Lei et al. (2015) is primarily focused on visualization of functional data, and the method of Diquigiovanni et al. (2021) is best suited for identifying magnitude outliers. Thus, it should be emphasized that we are considering a case not explicitly mentioned by either of the other two works. 

Regarding SNCM, there does not seem to be any benefit of using the Karcher mean rather than a cross-sectional mean function as SNCM1 and SNCM2 performed similarly in all experiments. SNCM does not appear to be well-suited for detecting the kind of shape outliers that we used in these experiments. 

There did not seem to be much of a difference in performance between GMD and GMDM methods when they used the same parameters. In both experiments, some of the GMD/GMDM methods perform reasonably well detecting these difficult shape outliers. We believe that the poor performance of GMD1 is due to its rigidity. That is, the projected functional data are being represented by a single bivariate Gaussian distribution. It is likely not flexible enough to provide a good representation of the functional data we used. As flexibility increases with larger values of _p_ and _K_ , these methods do much better, even coming fairly close to EFDM performance on experiment 2. With even greater flexibility, it is possible that GMD/GMDM methods could perform even better. One downside of this method is that more data are needed to enable more flexible implementations. On the other hand, GMD/GMDM methods are trained and produce labels with relatively low computational expense, so they may be a good choice with large functional data sets. 

We have already noted that EFDM performs well in each experiment. We also emphasize here that EFDM can perform well on relatively small sample sizes. When _n_ = 50, _n_ 1 = 34 and _n_ 2 = 16. Providing the correct coverage and being useful as an outlier detector with such a small amount of data is an important feature of EFDM. 

Finally, experiment 2 clearly demonstrates that results depend heavily on the selection of the significance level, _α_ . To select an appropriate value, the user needs to understand and compare the costs of false positives and false negatives. This decision is further influenced by the fact that we must choose _α ≥ n_ 21+1[.][Because][selecting] _[α]_[forces][a][determination] about outlier status, it may be wise to analyze p-values rather than settling on a single value of _α_ for a given application. 

## **5. Analysis of Exemplar Data** 

In this section, we analyze a real data set using EFDM. Our purpose is to demonstrate a use case of EFDM and not to provide thorough analysis of the data. 

15 

Adams Berman Michalenko Tucker 

## **5.1. Temperature Data** 

For our exemplar, we use data downloaded from the National Centers for Environmental Information at the National Oceanic and Atmospheric Administration (NOAA). We downloaded daily high and low temperatures and calculated the daily mean temperature from the years 1981-2024 at five different airports in the United States: Atlanta (Hartsfield-Jackson), Dallas-Love Field, Dallas-Fort Worth International, Miami International, and San Francisco International. In this case, each year is taken as a single functional observation. Thus, we train on the data from each site and then label the years at all other sites as inliers or outliers. With this analysis, we hope to see most years labeled as inliers for similar sites (e.g., the two sites in Dallas) and most years labeled as outliers when the sites are dissimilar (e.g., Miami and San Francisco). To account for potential magnitude outliers, we included translation distance in two runs of EFDM. The first run used the initial point for computing translation distance while the second run used the midpoint, where the Atlanta data seems to differ most from the Dallas data sets. 

EFDA methods work best on smooth data, and since our goal is to demonstrate EFDM capabilities on real data rather than provide thorough analysis, the temperature data went through overly simplistic preprocessing before training. We stress that the analysis here should not be used to make general conclusions about the temperature data themselves but only to shed light on EFDM as a method. To produce the data used for analysis, we first computed a daily mean temperature, _dmean_ = 0 _._ 5( _dmax_ + _dmin_ ) for every day over the 44 years at each site, where _dmax_ and _dmin_ are the daily high and daily low temperatures, respectively. We then averaged all _dmean_ temperatures in a given month to produce _mmean_ . At this point, each functional observation (year) was observed over 12 time points (months). We then smoothed the data using a Fourier basis, as described by Ramsay and Silverman (2005), and interpolated the smoothed functions so that we again had daily mean temperatures. 

Figure 3: The monthly averaged daily mean temperature data for five sites in the United States. 

Because each site has _n_ = 44 years of temperature data, we have _n_ 1 = 30 training functions and _n_ 2 = 14 calibration functions. Since we need _α ≥ n_ 21+1[,][we][use] _[α]_[=][0] _[.]_[10.] Table 6 shows the percentage of years at the site in the column that are labeled as outliers when training on the site in the row. All years at all other sites are labeled as outliers when 

16 

Functional Conformal Anomaly Detection 

training on either Miami or San Francisco. When training and testing on Atlanta and the two Dallas sites, the proportion of outliers is very different depending on which point is used for computing translation distance. This highlights the impact the point selection can have when detecting magnitude outliers. Similar tables are presented for GMD and SNCM in the supplementary material. 

||EFDM with Initial Point|EFDM with Initial Point|EFDM with Initial Point|EFDM with Initial Point|EFDM with Initial Point|EFDM with Midpoint|EFDM with Midpoint|EFDM with Midpoint|EFDM with Midpoint|EFDM with Midpoint|
|---|---|---|---|---|---|---|---|---|---|---|
||Testing Site|||||Testing Site|||||
|Training Site|ATL|DFW|DAL|MIA|SFO|ATL|DFW|DAL|MIA|SFO|
|ATL|_−_|0_._114|0_._091|1|1|_−_|0_._841|0_._682|1|1|
|DFW|0_._5|_−_|0_._205|1|1|0_._864|_−_|0_._25|1|1|
|DAL|0_._318|0_._182|_−_|1|1|0_._5|0_._091|_−_|1|1|
|MIA|1|1|1|_−_|1|1|1|1|_−_|1|
|SFO|1|1|1|1|_−_|1|1|1|1|_−_|



Table 6: Percentage of outliers when training on the site in the row and labeling the site in the column for all five sites: Atlanta (ATL), Dallas-Forth Worth (DFW), Dallas-Love Field (DAL), Miami (MIA), and San Francisco (SFO). The first five columns show results of using EFDM with translation distance computed at the initial point; the last five columns are obtained using the midpoint instead. 

## **6. Conclusion** 

In this paper, we have introduced the elastic functional distance metrics ICAD method, evaluated it alongside two competing ICAD methods for functional data, and demonstrated its effectiveness on a real data set. We argue that our results show EFDM to be effective at detecting both shape and magnitude outliers. 

As argued by Bates et al. (2023), users of conformal prediction methods, including ICAD, need to be aware of potential multiple testing pitfalls. In particular, the coverage guarantee of CP methods holds for a single test point, _P_ ( _Yn_ +1 _∈ C_ ( _Xn_ +1)) _≥_ 1 _− α_ . However, the probability that a large number of test points will all belong to their respective prediction sets can become much smaller than 1 _− α_ as the number of test points increases. We did not implement any corrections for this, and this could be potentially increasing the number of false positives for some of our results. In future work, we will implement corrections and compare the outcomes with our current results. 

## **Code, Data, and Supplementary Materials** 

The R code for implementing the methods and analyses in this work is available at `https: //github.com/sandialabs/conformal-functional-outliers` . This repository also contains data sets used in both the exemplar analysis and the simulation experiments. Additional results from our analyses can also be found in the supplementary material document within the respository. 

17 

Adams Berman Michalenko Tucker 

## **Acknowledgments** 

The authors express gratitude to Dr. Jing Lei who graciously shared `R` code implementing his functional conformal prediction methods. 

This work was supported by the Laboratory Directed Research and Development program at Sandia National Laboratories, a multimission laboratory managed and operated by National Technology and Engineering Solutions of Sandia LLC, a wholly owned subsidiary of Honeywell International Inc. for the U.S. Department of Energy’s National Nuclear Security Administration under contract DE-NA0003525. This paper describes objective technical results and analysis. Any subjective views or opinions that might be expressed in the paper do not necessarily represent the views of the U.S. Department of Energy or the United States Government. 

## **References** 

- Charu C. Aggarwal. _Outlier Analysis_ . Springer Publishing Company, Incorporated, 2nd edition, 2016. ISBN 3319475770. 

- Niccol`o Ajroldi, Jacopo Diquigiovanni, Matteo Fontana, and Simone Vantini. Conformal prediction bands for two-dimensional functional time series. _Computational Statistics & Data Analysis_ , 187:107821, 2023. 

- Anastasios N Angelopoulos and Stephen Bates. A gentle introduction to conformal prediction and distribution-free uncertainty quantification. _arXiv preprint arXiv:2107.07511_ , 2021. 

- Ana Arribas-Gil and Juan Romo. Shape outlier detection and visualization for functional data: the outliergram. _Biostatistics_ , 15(4):603–619, 2014. 

- Arturo Azcorra, Luis F Chiroque, Rub´en Cuevas, Antonio Fern´andez Anta, Henry Laniado, Rosa Elvira Lillo, Juan Romo, and Carlo Sguera. Unsupervised scalable statistical method for identifying influential users in online social networks. _Scientific reports_ , 8(1):6955, 2018. 

- Stephen Bates, Emmanuel Cand`es, Lihua Lei, Yaniv Romano, and Matteo Sesia. Testing for outliers with conformal p-values. _The Annals of Statistics_ , 51(1):149–178, 2023. 

- Dimitri Bertsekas. _Dynamic programming and optimal control: Volume I_ , volume 4. Athena scientific, 2012. 

- Feiyang Cai and Xenofon Koutsoukos. Real-time out-of-distribution detection in cyberphysical systems with learning-enabled components. _IET Cyber-Physical Systems: Theory & Applications_ , 7(4):212–234, 2022. 

- Davide Chicco, Matthijs J Warrens, and Giuseppe Jurman. The matthews correlation coefficient (mcc) is more informative than cohen’s kappa and brier score in binary classification assessment. _Ieee Access_ , 9:78368–78381, 2021. 

18 

Functional Conformal Anomaly Detection 

- Wenlin Dai, Tom´aˇs Mrkviˇcka, Ying Sun, and Marc G Genton. Functional outlier detection and taxonomy by sequential transformations. _Computational Statistics & Data Analysis_ , 149:106960, 2020. 

- Anna De Magistris, Andrea Diana, and Elvira Romano. Conformal prediction for functional ordinary kriging. _arXiv preprint arXiv:2409.20084_ , 2024. 

- Andrea Diana, Elvira Romano, and Antonio Irpino. Distribution free prediction for geographically weighted functional regression models. _Spatial Statistics_ , 57:100765, 2023. 

- Jacopo Diquigiovanni, Matteo Fontana, and Simone Vantini. The importance of being a band: Finite-sample exact distribution-free prediction sets for functional data. _arXiv preprint arXiv:2102.06746_ , 2021. 

- Jacopo Diquigiovanni, Matteo Fontana, and Simone Vantini. Conformal prediction bands for multivariate functional data. _Journal of Multivariate Analysis_ , 189:104879, 2022. 

- Alan Genz, Frank Bretz, Tetsuhisa Miwa, Xuefei Mi, Friedrich Leisch, Fabian Scheipl, Bjoern Bornkamp, Martin Maechler, Torsten Hothorn, and Maintainer Torsten Hothorn. Package ‘mvtnorm’. _Journal of Computational and Graphical Statistics_ , 11(950-971):155, 2021. 

- Trevor Harris, J Derek Tucker, Bo Li, and Lyndsay Shand. Elastic depths for detecting shape anomalies in functional data. _Technometrics_ , 63(4):466–476, 2021. 

- Trevor Hastie, Robert Tibshirani, Jerome H Friedman, and Jerome H Friedman. _The elements of statistical learning: data mining, inference, and prediction_ , volume 2. Springer, 2009. 

- Huang Huang and Ying Sun. A decomposition of total variation depth for understanding functional outliers. _Technometrics_ , 61(4):445–458, 2019. 

- Mia Hubert, Peter J Rousseeuw, and Karlien Vanden Branden. Robpca: a new approach to robust principal component analysis. _Technometrics_ , 47(1):64–79, 2005. 

- Rob J Hyndman and Han Lin Shang. Rainbow plots, bagplots, and boxplots for functional data. _Journal of Computational and Graphical Statistics_ , 19(1):29–45, 2010. 

- Vladislav Ishimtsev, Alexander Bernstein, Evgeny Burnaev, and Ivan Nazarov. Conformal _k_ -nn anomaly detector for univariate data streams. In _Conformal and Probabilistic Prediction and Applications_ , pages 213–227. PMLR, 2017. 

- Rikard Laxhammar. _Conformal anomaly detection: Detecting abnormal trajectories in surveillance applications_ . PhD thesis, University of Sk¨ovde, 2014. 

- Rikard Laxhammar and G¨oran Falkman. Inductive conformal anomaly detection for sequential detection of anomalous sub-trajectories. _Annals of Mathematics and Artificial Intelligence_ , 74:67–94, 2015. 

19 

Adams Berman Michalenko Tucker 

- Jing Lei, Alessandro Rinaldo, and Larry Wasserman. A conformal prediction approach to explore functional data. _Annals of Mathematics and Artificial Intelligence_ , 74:29–43, 2015. 

- Sara L´opez-Pintado and Juan Romo. On the concept of depth for functional data. _Journal of the American statistical Association_ , 104(486):718–734, 2009. 

- Sara L´opez-Pintado and Juan Romo. A half-region depth for functional data. _Computational Statistics & Data Analysis_ , 55(4):1679–1695, 2011. 

- Brian W Matthews. Comparison of the predicted and observed secondary structure of t4 phage lysozyme. _Biochimica et Biophysica Acta (BBA)-Protein Structure_ , 405(2):442– 451, 1975. 

- R Core Team. _R: A Language and Environment for Statistical Computing_ . R Foundation for Statistical Computing, Vienna, Austria, 2023. URL `https://www.R-project.org/` . 

- J.O. Ramsay and B.W. Silverman. _Functional Data Analysis, 2nd_ . Springer, New York, 2005. doi: 10.1002/0471667196.ess3138. 

- Peter J Rousseeuw and Katrien Van Driessen. A fast algorithm for the minimum covariance determinant estimator. _Technometrics_ , 41(3):212–223, 1999. 

- Pallavi Sawant, Nedret Billor, and Hyejin Shin. Functional outlier detection with robust functional principal component analysis. _Computational Statistics_ , 27:83–102, 2012. 

- Luca Scrucca, Chris Fraley, T Brendan Murphy, and Adrian E Raftery. _Model-based clustering, classification, and density estimation using mclust in R_ . Chapman and Hall/CRC, 2023. 

- Anuj Srivastava and Eric P Klassen. _Functional and shape data analysis_ , volume 1. Springer, 2016. 

- Ying Sun and Marc G Genton. Functional boxplots. _Journal of computational and graphical statistics_ , 20(2):316–334, 2011. 

- J. D. Tucker, W. Wu, and A. Srivastava. Generative models for functional data using phase and amplitude separation. _Computational Statistics and Data Analysis_ , 61:50–66, 2013. 

J Derek Tucker. Package ‘fdasrvf’, 2017. 

- J Derek Tucker, John R Lewis, Caleb King, and Sebastian Kurtek. A geometric approach for computing tolerance bounds for elastic functional data. _Journal of applied statistics_ , 47(3):481–505, 2020. 

Jarek Tuszynski and Michael Dietze. Package ‘catools’, 2024. 

- Shahid Ullah and Caroline F Finch. Applications of functional data analysis: A systematic review. _BMC medical research methodology_ , 13:1–12, 2013. 

20 

Functional Conformal Anomaly Detection 

- Vladimir Vovk, Alexander Gammerman, and Glenn Shafer. _Algorithmic learning in a random world_ , volume 29. Springer, 2005. 

- Fangyi Wang, Sebastian Kurtek, and Yuan Zhang. Joint registration and conformal prediction for partially observed functional data. _arXiv preprint arXiv:2502.15000_ , 2025. 

- Weiyi Xie, Sebastian Kurtek, Karthik Bharath, and Ying Sun. A geometric approach to visualization of variability in functional data. _Journal of the American Statistical Association_ , 112(519):979–993, 2017. 

- Fengmin Yu, Liming Liu, Liying Jin, Nanxiang Yu, and Hua Shang. A method for detecting outliers in functional data. In _IECON 2017-43rd Annual Conference of the IEEE Industrial Electronics Society_ , pages 7405–7410. IEEE, 2017. 

- Xiaofan Zhou, Baiting Chen, Yu Gui, and Lu Cheng. Conformal prediction: A data perspective. _arXiv preprint arXiv:2410.06494_ , 2024. 

21 

