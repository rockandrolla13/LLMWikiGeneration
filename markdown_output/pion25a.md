Proceedings of Machine Learning Research 266:1–3, 2025 Conformal and Probabilistic Prediction with Applications 

## **A Bayesian framework for calibrating Gaussian process predictive distributions** 

**Aur´elien Pion** aurelien.pion@centralesupelec.fr _Transvalor S.A., Biot, France Universit´e Paris-Saclay, CNRS, CentraleSup´elec, L2S, Gif-sur-Yvette, France_ **Emmanuel Vazquez** emmanuel.vazquez@centralesupelec.fr 

aurelien.pion@centralesupelec.fr 

_Universit´e Paris-Saclay, CNRS, CentraleSup´elec, L2S, Gif-sur-Yvette, France_ 

**Editor:** Khuong An Nguyen, Zhiyuan Luo, Harris Papadopoulos, Tuwe L¨ofstr¨om, Lars Carlsson and Henrik Bostr¨om 

Gaussian processes (GPs) are Bayesian models widely used for interpolating an unknown deterministic function _f_ : _X ⊂_ R _[d] →_ R from observed data. A GP model places a Gaussianprocess prior on _f_ , written as _ξ ∼_ GP( _m, k_ ), where _m_ : _X →_ R is the mean function and _k_ : _X × X →_ R is a positive definite covariance kernel. Given noiseless observations _Dn_ = _{_ ( _xi, f_ ( _xi_ )) _}[n] i_ =1[, the GP posterior defines a predictive distribution at any] _[ x][ ∈X]_[, which] is Gaussian with posterior mean _mn_ ( _x_ ) and posterior variance _σn_[2][(] _[x]_[),][both][computable][in] closed form. 

In the noiseless setting, GPs are prominent tools for sequential prediction, as their posterior distributions provide both predictions and uncertainty quantification. Two common examples of sequential predictions are Bayesian optimization (see, e.g., Jones et al., 1998) and estimation of excursion probabilities (see, e.g., Bect et al., 2012). 

In practice, however, GP predictive distributions are frequently miscalibrated: the actual frequency with which _f_ ( _x_ ) falls within nominal confidence intervals (with respect to a distribution over _X_ ) may substantially deviate from the intended level, as shown by Pion and Vazquez (2025). This can lead to overconfident predictions that underestimate uncertainty, or overly conservative ones that overstate it. In practice, it is generally preferable to have conservative predictive distributions. 

Among available approaches to improve calibration, conformal prediction (CP) is particularly attractive because it is model-agnostic and provides distribution-free guarantees on marginal coverage. It has been adapted to GPs through full conformal prediction (FCP) method by Papadopoulos (2024), or via J+GP, a variant of Jackknife+ (Barber et al., 2021) proposed by Jaber et al. (2024), providing post-hoc correction at user-specified coverage levels. In another line of work, Vovk et al. (2017b) introduce the Conformal Predictive Systems (CPS), based on CP to build a cumulative distribution function (CDF) at each test point for an unknown label. CPS have been adapted to kernel methods by Vovk et al. (2017a) and thus naturally apply to GP. However, when few points are available, CP methods may produce prediction intervals of infinite length. Moreover, CP methods guarantee only marginal coverage, not coverage for a given dataset. 

For these reasons, we propose a Bayesian approach to constructing predictive distributions for GPs and introduce a novel method named _calGP_ . The method retains the GP posterior mean as regression estimates, but models normalized prediction errors using a 

© 2025 A. Pion & E. Vazquez. 

Pion Vazquez 

generalized normal distribution. The shape and scale parameters of this distribution are selected using a Bayesian strategy inspired by tolerance intervals (Meeker et al., 2017). The resulting predictive distribution remains centered on the GP posterior mean, while allowing for improved calibration—particularly in the tails—and supports continuous inference at arbitrary confidence levels. By adjusting the variance of the predictive distribution independently of its mean, calGP makes it possible to control the level of conservativeness in uncertainty quantification. 

Figure 1 presents a comparison of three calibration methods: the proposed calGP, along with J+GP and FCP. Predictive intervals from the predictive distributions of the GP are also presented. Intervals from J+GP and FCP can become infinite when the confidence level exceeds 1 _/_ ( _n_ + 1), failing to capture local variations in uncertainty. calGP captures regions of high deviation (”excursions”), demonstrating improved calibration performance. 

In this study, we focus on comparing empirical coverages of prediction intervals provided by calGP, FCP, and J+GP, evaluated on multiple functions using a test grid. 


![](markdown_output/pion25a_images/pion25a.pdf-0002-04.png)


**----- Start of picture text -----**<br>
Prediction interval with J+GP Prediction interval with calPIT Prediction interval with FCP<br>1.6<br>1.4<br>1.2<br>1.0<br>0.8<br>0.6<br>0.4<br>1 0 1 2 1 0 1 2 1 0 1 2<br>calibrated interval posterior mean f evaluations GP interval<br>z z z<br>**----- End of picture text -----**<br>


Figure 1: Prediction intervals constructed by J+GP (left) and calGP (middle) and FCP (right) at confidence level 1 _− α_ = 0 _._ 75. The parameter _δ_ for calGP is set to 0 _._ 03. J+GP and FCP intervals may become unbounded when _α >_ 1 _/_ ( _n_ +1), and fail to adapt to excursions. calGP yields more informative, location-sensitive intervals. 

## **Acknowledgments** 

This work was funded by Transvalor S.A. 

## **References** 

- R. F. Barber, E. J. Cand`es, A. Ramdas, and R. J. Tibshirani. Predictive inference with the jackknife+. _Ann. Stat._ , 49(1), 2021. 

- J. Bect, D. Ginsbourger, L. Li, V. Picheny, and E. Vazquez. Sequential design of computer experiments for the estimation of a probability of failure. _Stat. Comput._ , 22:773–793, 2012. 

2 

Bayesian calibration for GPs 

- E. Jaber, V. Blot, N. Brunel, V. Chabridon, E. Remy, B. Iooss, D. Lucor, M. Mougeot, and A. Leite. Conformal approach to gaussian process surrogate evaluation with coverage guarantees, 2024. hal-04389163 (preprint submitted on 11 January 2024). 

- Donald Jones, Matthias Schonlau, and William Welch. Efficient global optimization of expensive black-box functions. _Journal of Global Optimization_ , 13:455–492, 12 1998. doi: 10.1023/A:1008306431147. 

- W. Q. Meeker, G. J. Hahn, and L. A. Escobar. _Statistical Intervals: A Guide for Practitioners and Researchers_ . John Wiley & Sons, Hoboken, New Jersey, second edition, 2017. ISBN 978-0-471-68717-7. 

- H. Papadopoulos. Guaranteed coverage prediction intervals with gaussian process regression. _IEEE Trans. Pattern Anal. Mach. Intell._ , 46(12):9072–9083, dec 2024. 

- A. Pion and E. Vazquez. Gaussian process interpolation with conformal prediction: Methods and comparative analysis. In G. Nicosia, V. Ojha, S. Giesselbach, M. P. Pardalos, and R. Umeton, editors, _Mach. Learn. Optim. Data Sci._ , pages 218–228, Cham, 2025. Springer Nature Switzerland. ISBN 978-3-031-82484-5. 

- Vladimir Vovk, Ilia Nouretdinov, Valery Manokhin, and Alex Gammerman. Conformal predictive distributions with kernels, 2017a. URL `https://arxiv.org/abs/1710.08894` . 

- Vladimir Vovk, Jieli Shen, Valery Manokhin, and Min-ge Xie. Nonparametric predictive distributions based on conformal prediction. In Alex Gammerman, Vladimir Vovk, Zhiyuan Luo, and Harris Papadopoulos, editors, _Proceedings of the Sixth Workshop on Conformal and Probabilistic Prediction and Applications_ , volume 60 of _Proceedings of Machine Learning Research_ , pages 82–102. PMLR, 13–16 Jun 2017b. 

3 

