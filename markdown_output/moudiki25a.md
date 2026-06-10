Proceedings of Machine Learning Research 266:1–2, 2025 Conformal and Probabilistic Prediction with Applications 

## **Conformal Predictive Simulations for Univariate Time Series** 

## **T. Moudiki** 

thierry.moudiki@gmail.com 

_Techtonique LLC, USA_ 

**Editor:** Khuong An Nguyen, Zhiyuan Luo, Harris Papadopoulos, Tuwe L¨ofstr¨om, Lars Carlsson and Henrik Bostr¨om 

## **Abstract** 

Uncertainty quantification is useful because it allows, among other things, for the assessment of impact of alternative, hypothetical scenarios on business metrics of interest. For example, in the context of electricity load forecasting, uncertainty quantification can help in assessing the impact of a drop in temperature on electricity demand, and taking appropriate measures to avoid blackouts. In financial forecasting, uncertainty quantification can help in assessing the impact of an increase in stock market on a portfolio, and taking appropriate measures to avoid large losses. Another application, in insurance, is the calculation of capital requirements in extremely adverse situations. 

In this context, despite having been available for decades (see Vovk et al. (2005)), Conformal Prediction (CP) is becoming more and more popular, and a gold standard technique. The interested reader can find an accessible introduction to CP applied to regression and classification tasks in Angelopoulos and Bates (2023). 

This study proposes a revisited approach to uncertainty quantification for univariate time series forecasting, that can be adapted to multivariate time series forecasting. The approach adapts split conformal prediction (SCP, see Vovk et al. (2005)), usually applied to tabular data but never to sequential data, to sequential data. Time series data indeed possess some peculiarities, because they are not exchangeable but rather often, auto-correlated. Loosely speaking, not being exchangeable means that the sequential order in the data matters crucially, and randomly splitting as done in the standard SCP setting for tabular data doesn’t work anymore in this context. In addition to the non-exchangeability of the original data, time series residuals can also, in turn, be non-exchangeable. This hasn’t prevented time series forecasting from being impacted by the CP trend, and many different approaches have been proposed to circumvent the non-exchangeability, and take into account their sequential structure of input data. The contribution of this paper is twofold: 

1. I propose a new and different approach to CP for time series, based on SCP, but with a twist: instead of splitting the data randomly or by stratifying a variable of interest, I split the data in a way that **preserves its temporal order** . 

2. The **conformity score** , a score computed on calibrated residuals for obtaining quantiles of the predictive distribution, is chosen to be the standardized residuals (instead of absolute residuals in classical SCP). 

Although this relatively straightforward (just as SCP) approach may sound simplistic, it’s quite robust and can be applied to a wide range of time series data, both real-world and synthetic. This makes it suitable for industrial applications. **Empirical results for predictive coverage rates and Winkler scores are available for more than 30,000 time series** . 

Code and results are available with more details at: 

© 2025 T. Moudiki. 

Moudiki 

- `https://gitlab.com/conf3180013/conformalkde/` . 

- `https://tr.ee/f0VfXz` . 

- `https://tr.ee/pQSH1J` . 

- `https://www.researchgate.net/publication/382589729_Probabilistic_Forecasting_with_ nnetsauce_using_Density_Estimation_Bayesian_inference_Conformal_prediction_and_ Vine_copulas` 

These extensive experiments evaluate various forecasting methods, conformalized and non-conformalized, across multiple time series datasets (the famous M3, Makridakis and Hibon (2000), M5, Makridakis et al. (2022), and Tourism, Athanasopoulos et al. (2011) forecasting competitions data, plus multiple real-world and synthetic series). The metrics employed are the coverage rate and Winkler score. Results demonstrate that SCPcalibration provides more reliable prediction intervals than alternatives. Key strengths include its consistent achievement of nominal coverage rates (e.g., 92-95% vs. target 95%) compared to uncalibrated Gaussian methods (which typically undercover) and adaptive conformal approaches (showing unstable coverage). SCP works effectively across different base models without requiring strict distributional assumptions. And even when SCP intervals are wider than theoretically minimum widths, the Winkler score settles the debate with the other methods envisaged in the experiments. All this evidence establishes SCP as a current gold standard for rigorous uncertainty quantification in time series forecasting. **Keywords:** conformal prediction, time series forecasting, uncertainty quantification, predictive simulation, coverage guarantees 

## **References** 

- Anastasios N. Angelopoulos and Stephen Bates. Conformal prediction: A gentle introduction. _Foundations and Trends® in Machine Learning_ , 16(4), 2023. URL `http: //dx.doi.org/10.1561/2200000101` . 

- George Athanasopoulos, Rob J Hyndman, Haiyan Song, and Doris C Wu. The tourism forecasting competition. _International Journal of Forecasting_ , 27(3):822–844, 2011. 

- Spyros Makridakis and Michele Hibon. The m3-competition: results, conclusions and implications. _International journal of forecasting_ , 16(4):451–476, 2000. 

- Spyros Makridakis, Fotios Petropoulos, and Evangelos Spiliotis. Introduction to the m5 forecasting competition special issue. _International Journal of Forecasting_ , 38(4):1279, 2022. 

- Vladimir Vovk, Alexander Gammerman, and Glenn Shafer. _Algorithmic learning in a random world_ , volume 29. Springer, 2005. 

2 

