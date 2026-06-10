## **Bayesian Reconstruction and Regression with Multivariate Graph Signals** 

_Author:_ Edward Antonian 

_Supervisors:_ Prof. Mike Chantler & Prof. Gareth W. Peters 

_Submitted for the degree of Doctor of Philosophy_ 

## Heriot-Watt University 

School of Mathematical and Computer Sciences 

March 2024 

The copyright in this thesis is owned by the author. Any quotation from the thesis or use of any of the information contained in it must acknowledge this thesis as the source of the quotation or information. 

## _Abstract_ 

Graph Signal Processing (GSP) is a rapidly evolving field that combines ideas from spectral graph theory and classical signal processing to analyse and manipulate data residing on an irregular domain. In this thesis, we contribute several advancements to GSP theory, in particular, with regard to Bayesian reconstruction and regression techniques for multivariate graph signals. The first topic we consider is the reconstruction of signals existing on two-dimensional Cartesian product graphs, in the presence of noise and arbitrary missing data. Using numerical methods and the properties of the Kronecker product, we derive two efficient algorithms for computing the posterior mean and show how the optimal choice of technique depends on the model hyperparameters and sparsity of the input data. We then build on this by applying similar algorithms to solve several multivariate graph signal regression models. In particular, we generalise prior work on Kernel Graph Regression (KGR) and Regression with Network Cohesion (RNC), which are relevant when the explanatory variables are exogenous and endogenous respectively, by allowing for arbitrary patterns of missing data in the input signal. Following this, we adapt the reconstruction and regression methods developed prior in the thesis to the Multiway Graph Signal Processing (MWGSP) paradigm. MWGSP is an emerging sub-field that focuses on tensor-valued graph signals, where each axis is described by a unique graph topology. In order to help write effective and efficient MWGSP algorithms, we also present the PyKronecker library which creates an abstracted API for manipulating high-dimensional Kronecker-structured matrices. The next topic we consider is techniques for computing the posterior covariance of our models. First, we propose several algorithms for estimating the marginal posterior variance and compare them to other alternative standard techniques. Combined with an active learning strategy, we demonstrate that our procedure can generate superior estimates, with _R_[2] _>_ 0 _._ 95. We also derive an efficient algorithm for sampling directly from the posterior whilst avoiding computationally expensive MCMC-based approaches, using a technique known as perturbation optimisation. Finally, we develop new models that generalise our previous reconstruction and regression models to accommodate binary and categorical tensor graph signals. Each topic in this thesis is also accompanied by a real-world case study to corroborate the utility of the methods or demonstrate their theoretical properties. 

## _Acknowledgements_ 

First and foremost, I want to thank my supervisors Professors Mike Chantler and Gareth Peters. I am very grateful for their steadfast support and guidance throughout this process and consider myself truly fortunate to have worked with and learned from such insightful and dedicated individuals. In addition to their invaluable academic guidance, they also taught me the value of patience, perseverance and kindness. 

I would also like to thank our partners at NatWest, in particular Stuart Wray, Sebastien Geroult, and Beverley O’Neill. Their consistent support both professionally and personally was deeply appreciated and is a testament to the culture within the company. This process would also not have been possible without the generous financial support of the company at large, for which I am immensely grateful. 

Thank you also to my friends, who keep me sane. Special mention must go to my fellow student Cole van Jaarsveldt, with whom it’s been a pleasure to work and learn alongside. Finally, I would like to thank my family. Their love is what keeps me going and, to them, I owe more than words can express. 

ii 

_“The more I read, the more I acquire, the more certain I am that I know nothing.”_ 

Voltaire 

## **Contents** 

|**Abstract**|**Abstract**|**Abstract**||**i**|
|---|---|---|---|---|
|**Acknowledgements**||||**ii**|
|**Contents**||||**iv**|
|**List of **||**Figures**||**viii**|
|**List of **||**Tables**||**x**|
|**Abbreviations**||||**xi**|
|**Symbols**||||**xii**|
|**Identities**||||**xv**|
|**Publications**||||**xvi**|
|**1**|**Introduction**|||**1**|
||1.1|Research goals<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||2|
||1.2|GSP fundamentals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||4|
||1.3|Example applications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||8|
|||1.3.1|Biology<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|8|
|||1.3.2|Transportation and infrastructure<br>. . . . . . . . . . . . . . . . . .|8|
|||1.3.3|Finance and economics. . . . . . . . . . . . . . . . . . . . . . . . .|9|
|||1.3.4|Sensor networks<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|9|
||1.4|Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||10|
||1.5|Thesis|organisation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|10|
|**2**|**Literature **||**Review, Contributions and Scope**|**12**|
||2.1|A historical perspective on GSP. . . . . . . . . . . . . . . . . . . . . . . .||12|
||2.2|Graph|kernels and graph flters . . . . . . . . . . . . . . . . . . . . . . . .|14|
|||2.2.1|Bayesian approaches to GSP<br>. . . . . . . . . . . . . . . . . . . . .|16|
|||2.2.2|Approximating graph flters with Chebyshev polynomials<br>. . . . .|18|
||2.3|Graph|Signal Reconstruction<br>. . . . . . . . . . . . . . . . . . . . . . . . .|21|
||2.4|Graph|Signal Regression . . . . . . . . . . . . . . . . . . . . . . . . . . . .|22|



iv 

_Contents_ 

v 

|||2.4.1<br>Exogenous case: Kernel Graph Regression and Gaussian Processes|2.4.1<br>Exogenous case: Kernel Graph Regression and Gaussian Processes|||
|---|---|---|---|---|---|
|||on Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .|.|23|
|||2.4.2<br>Endogenous case: Regression with Network Cohesion. . . . .|. .|.|25|
||2.5|Multiway Graph Signal Processing . . . . . . . . . . . . . . . . . . .|. .|.|27|
||2.6|Node classifcation . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .|.|28|
||2.7|Related topics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .|.|30|
|||2.7.1<br>Graph learning . . . . . . . . . . . . . . . . . . . . . . . . . .|. .|.|30|
|||2.7.2<br>GSP on directed graphs . . . . . . . . . . . . . . . . . . . . .|. .|.|32|
||2.8|Opportunities for extension . . . . . . . . . . . . . . . . . . . . . . .|. .|.|35|
|**3**|**Signal Reconstruction on Cartesian Product Graphs**||||**36**|
||3.1|Graph Products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .|.|37|
|||3.1.1<br>Basic defnitions<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. .|.|37|
|||3.1.2<br>The spectral properties of products graphs<br>. . . . . . . . . .|. .|.|39|
|||3.1.3<br>Signals and flters on Cartesian product graphs . . . . . . . .|. .|.|40|
||3.2|Graph Signal Reconstruction on Cartesian Product Graphs . . . . .|. .|.|43|
|||3.2.1<br>Problem statement . . . . . . . . . . . . . . . . . . . . . . . .|. .|.|46|
|||3.2.2<br>A stationary iterative method . . . . . . . . . . . . . . . . . .|. .|.|50|
|||3.2.2.1<br>An eigendecomposition-free distributed implementation||.|52|
|||3.2.3<br>A conjugate gradient method . . . . . . . . . . . . . . . . . .|. .|.|55|
|||3.2.4<br>Real data experiments . . . . . . . . . . . . . . . . . . . . . .|. .|.|58|
||3.3|Convergence properties. . . . . . . . . . . . . . . . . . . . . . . . . .|. .|.|62|
|||3.3.1<br>Upper bound on convergence: the weak flter limit . . . . . .|. .|.|64|
|||3.3.2<br>Lower bound on convergence: the strong flter limit<br>. . . . .|. .|.|65|
|||3.3.3<br>Practical implications and method selection . . . . . . . . . .|. .|.|67|
|||3.3.4<br>Experimental validation . . . . . . . . . . . . . . . . . . . . .|. .|.|69|
|||3.3.4.1<br>Experiment 1: testing the strong and weak flter limits||.|69|
|||3.3.4.2<br>Experiment 2: Testing intermediate values of _β_ . . .|. .|.|70|
||3.4|Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .|.|72|
|**4**|**Multivariate Regression Models for Time-Varying Graph Signals**||||**74**|
||4.1|Kernel Graph Regression with Unrestricted Patterns of Missing Data|. .|.|76|
|||4.1.1<br>Model description<br>. . . . . . . . . . . . . . . . . . . . . . . .|. .|.|76|
|||4.1.2<br>Relation to graph signal reconstruction<br>. . . . . . . . . . . .|. .|.|79|
|||4.1.3<br>Solving for the posterior mean<br>. . . . . . . . . . . . . . . . .|. .|.|81|
||4.2|Regression with Network Cohesion . . . . . . . . . . . . . . . . . . .|. .|.|83|
|||4.2.1<br>Model description<br>. . . . . . . . . . . . . . . . . . . . . . . .|. .|.|83|
|||4.2.2<br>Solving for the posterior mean<br>. . . . . . . . . . . . . . . . .|. .|.|86|
||4.3|Network regression with both global and local explanatory variables|. .|.|87|
||4.4|Network regression for pollutant monitoring . . . . . . . . . . . . . .|. .|.|90|
||4.5|Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .|.|97|
|**5**|**Regression and Reconstruction with Tensor-Valued Multiway Graph**|||||
||**Signals**||||**99**|
||5.1|Multiway Graph Signal Processing . . . . . . . . . . . . . . . . . . .|. .|.|100|
|||5.1.1<br>The Cartesian product of more than two graphs<br>. . . . . . .|. .|.|100|
|||5.1.2<br>Representing _d_-dimensional graph signals . . . . . . . . . . .|. .|.|103|
|||5.1.3<br>The _d_-dimensional GFT and IGFT . . . . . . . . . . . . . . .|. .|.|105|



|_Contents_|_Contents_|_Contents_|||||vi|
|---|---|---|---|---|---|---|---|
|||5.1.4|Multiway spectral operators and fltering||||. . . . . . . . . . . . . . 109|
||5.2|Multiway Graph Signal reconstruction . . .||.|.|.|. . . . . . . . . . . . . . 111|
|||5.2.1|Tensor SIM . . . . . . . . . . . . . .|.|.|.|. . . . . . . . . . . . . . 113|
|||5.2.2|Tensor CGM . . . . . . . . . . . . .|.|.|.|. . . . . . . . . . . . . . 115|
||5.3|Multiway Kernel Graph Regression . . . . .||.|.|.|. . . . . . . . . . . . . . 116|
|||5.3.1|Computation of the posterior mean.|.|.|.|. . . . . . . . . . . . . . 118|
||5.4|Multiway Regression with Network Cohesion|||.|.|. . . . . . . . . . . . . . 120|
||5.5|GSR and KGR for green bond yield prediction||||.|. . . . . . . . . . . . . . 122|
||5.6|Conclusions . . . . . . . . . . . . . . . . . .||.|.|.|. . . . . . . . . . . . . . 128|
|**6**|**Signal Uncertainty: Estimation and Sampling**||||||**130**|
||6.1|Estimating the posterior marginal variance||.|.|.|. . . . . . . . . . . . . . 132|
|||6.1.1|A baseline approach . . . . . . . . .|.|.|.|. . . . . . . . . . . . . . 132|
|||6.1.2|Matrix diagonal estimation . . . . .|.|.|.|. . . . . . . . . . . . . . 133|
|||6.1.3|A supervised learning approach . . .|.|.|.|. . . . . . . . . . . . . . 133|
||||6.1.3.1<br>Solving with Ridge Regression|||.|. . . . . . . . . . . . . . 135|
||||6.1.3.2<br>Solving with RNC . . . . .|.|.|.|. . . . . . . . . . . . . . 136|
||||6.1.3.3<br>Ridge regression with learned||flter parameters . . . . . . 136|||
|||6.1.4|Query strategies<br>. . . . . . . . . . .|.|.|.|. . . . . . . . . . . . . . 137|
|||6.1.5|Comparison and analysis<br>. . . . . .|.|.|.|. . . . . . . . . . . . . . 137|
||6.2|Posterior Sampling . . . . . . . . . . . . . .||.|.|.|. . . . . . . . . . . . . . 139|
|||6.2.1|Perturbation optimization (PO)<br>. .|.|.|.|. . . . . . . . . . . . . . 141|
|||6.2.2|PO for Graph Signal Reconstruction|.|.|.|. . . . . . . . . . . . . . 142|
|||6.2.3|Drawing samples for KGR, RNC and|KG-RNC . . . . . . . . . . . 145||||
||||6.2.3.1<br>PO with KGR . . . . . . .|.|.|.|. . . . . . . . . . . . . . 145|
||||6.2.3.2<br>PO with RNC . . . . . . .|.|.|.|. . . . . . . . . . . . . . 146|
||||6.2.3.3<br>PO with KG-RNC . . . . .|.|.|.|. . . . . . . . . . . . . . 150|
||6.3|Variance Estimation: Prediction vs Sampling|||.|.|. . . . . . . . . . . . . . 151|
|||6.3.1|Experiments<br>. . . . . . . . . . . . .|.|.|.|. . . . . . . . . . . . . . 152|
||6.4|Conclusions . . . . . . . . . . . . . . . . . .||.|.|.|. . . . . . . . . . . . . . 153|
|**7**|**Reconstruction and Regression with Binary-Valued Graph Signals**<br>**155**|||||||
||7.1|Logistic Graph Signal Reconstruction (L-GSR)||||.|. . . . . . . . . . . . . . 157|
|||7.1.1|Solving for the MAP estimator with the IRLS algorithm . . . . . . 160|||||
|||7.1.2|Completing IRLS iterations with the|CGM|||. . . . . . . . . . . . . 162|
||7.2|Multiclass Logistic Graph Signal Reconstruction|||||. . . . . . . . . . . . . . 164|
||7.3|Logistic Graph Signal Regression . . . . . .||.|.|.|. . . . . . . . . . . . . . 171|
|||7.3.1|Logistic Kernel Graph Regression (L-KGR) . . . . . . . . . . . . . 171|||||
||||7.3.1.1<br>Binary L-KGR . . . . . . .|.|.|.|. . . . . . . . . . . . . . 172|
||||7.3.1.2<br>Multiclass L-KGR . . . . .|.|.|.|. . . . . . . . . . . . . . 174|
|||7.3.2|Logistic Regression with Network Cohesion (L-RNC) . . . . . . . . 175|||||
||||7.3.2.1<br>Binary L-RNC . . . . . . .|.|.|.|. . . . . . . . . . . . . . 175|
||||7.3.2.2<br>Multiclass L-RNC . . . . .|.|.|.|. . . . . . . . . . . . . . 180|
||7.4|Image segmentation experiments . . . . . .||.|.|.|. . . . . . . . . . . . . . 185|
|||7.4.1|Background/foreground separation .|.|.|.|. . . . . . . . . . . . . . 185|
||||7.4.1.1<br>Assessing accuracy as a function of label percentage . . . 186|||||
||||7.4.1.2<br>Qualitative efects of varying _γ_ and _β_ . . . . . . . . . . . 187|||||



_Contents_ 

vii 

|||7.4.2|Multiclass segmentation with hyper-spectral images<br>. . . . . . . . 189|
|---|---|---|---|
||7.5|Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190||
|||7.5.1|Convergence of the IRLS algorithm . . . . . . . . . . . . . . . . . . 190|
|||7.5.2|Efcient computation in the multiclass L-RNC algorithm<br>. . . . . 191|
||7.6|Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193||
|**8**|**Conclusions**<br>**194**|||
||8.1|Thesis|summary<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194|
||8.2|Future|Work<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196|
|||8.2.1|Scalability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196|
|||8.2.2|Multiway Filter Design<br>. . . . . . . . . . . . . . . . . . . . . . . . 197|
|||8.2.3|Graph and parameter learning<br>. . . . . . . . . . . . . . . . . . . . 198|
|||8.2.4|Generalised Linear Models (GLMs) . . . . . . . . . . . . . . . . . . 198|



**A Proofs** 

**199** 

## **List of Figures** 

|1.1|A visual representation of a simple graph<br>. . . . . . . . . . . . . . . . .|.|1|
|---|---|---|---|
|1.2|A graphical depiction of a graph signal . . . . . . . . . . . . . . . . . . .|.|2|
|1.3|A visualisation of the Laplacian eigenvectors for a network of regions in|||
||the UK<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.|6|
|1.4|A visualisation of the Laplacian eigenvectors of the cycle graph . . . . .|.|7|
|2.1|An example of a random smooth graph signal . . . . . . . . . . . . . . .|.|17|
|2.2|Successive approximations of a flter function using Chebyshev polynomials.||19|
|2.3|Graphical depiction of an order-3 tensor . . . . . . . . . . . . . . . . . .|.|27|
|3.1|Graphical depiction of the standard graph products. . . . . . . . . . . .|.|39|
|3.2|A visual representation of applying an isotropic and anisotropic graph flter||44|
|3.3|Chebyshev approximation accuracy visualisation<br>. . . . . . . . . . . . .|.|56|
|3.4|Snapshot of the Covid-19 case rate in the UK . . . . . . . . . . . . . . .|.|60|
|3.5|A visual depiction of the four ways we removed data. Black lines/dots indicate|||
||data that was removed.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|.|61|
|3.6|The number of iterations required for convergence in the weak flter limit for the|||
||SIM and CGM both theoretically and empirically, as a function of _γ_. . . . . .|.|70|
|3.7|Strong Filter Limit convergence experiments. . . . . . . . . . . . . . . .|.|71|
|3.8|Convergence experiments<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|.|72|
|4.1|Graph signal regression with exogenous variables . . . . . . . . . . . . .|.|75|
|4.2|Graph signal regression with local variables . . . . . . . . . . . . . . . .|.|75|
|4.3|Tensor indexing notation. . . . . . . . . . . . . . . . . . . . . . . . . . .|.|84|
|4.4|The network of monitoring stations created via Voronoi tessellation . . .|.|91|
|4.5|The structure of the missing data for the pollutant prediction problem .|.|94|
|4.6|Model predictions vs ground truth at a particular node. . . . . . . . . .|.|96|
|4.7|Model predictions vs ground truth at a particular time . . . . . . . . . .|.|97|
|5.1|Graphical depiction of an order-3 tensor . . . . . . . . . . . . . . . . . .|.|99|
|5.2|Graphical depiction of a 3D Cartesian product graph . . . . . . . . . . .|.|101|
|5.3|Conversion between a multidimensional array and a vector. . . . . . . .|.|104|
|5.4|3D plot of the yield on US treasuries of various maturities over time . .|.|122|
|5.5|Graph categorising green bonds based on sector . . . . . . . . . . . . . .|.|124|
|5.6|Graph categorising green bonds based on tax status<br>. . . . . . . . . . .|.|125|
|5.7|A visualisation of the tensor coordinates used in the greed bond application126|||
|5.8|The output of the GSR model on several green bonds from the test set .|.|128|
|5.9|The output of the KGR model on several green bonds from the test set|.|129|



viii 

_List of Figures_ 

ix 

|6.1|Performance of various algorithms for predicting the posterior log-variance140|
|---|---|
|6.2|Performance of the sampling strategy for predicting posterior marginal|
||variance compared with the supervised learning strategies as a function|
||of graph size<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153|
|7.1|Visualisation of a binary classifcation task over a network . . . . . . . . . 156|
|7.2|Visualisation of a multiclass classifcation task over a network . . . . . . . 156|
|7.3|Visualisation of binary classifcation on a 2D lattice<br>. . . . . . . . . . . . 160|
|7.4|Visualisation of multiclass classifcation on a 2D lattice. . . . . . . . . . . 167|
|7.5|Foreground/background separation with L-GSR and L-RNC . . . . . . . . 186|
|7.6|Image segmentation output as a function of labelled pixel fraction<br>. . . . 187|
|7.7|Accuracy of binary L-GSR and L-RNC models as a function of label fraction188|
|7.8|Qualitative efects of varying _β_ on the output of the L-GSR and L-RNC|
||algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188|
|7.9|Qualitative efects of varying _γ_ on the output of the L-GSR and L-RNC|
||algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189|
|7.10|A visual overview of the Indian Pines hyperspectral image dataset<br>. . . . 189|
|7.11|The predicted class labels from the multiclass L-GSR and L-RNC algo-|
||rithms as applied to the Indian pines dataset<br>. . . . . . . . . . . . . . . . 190|



## **List of Tables** 

|2.1|Example graph flter functions<br>. . . . . . . . . . . . . . . . . . . . . . .|.|15|
|---|---|---|---|
|3.1|The adjacency and Laplacian matrices for the standard graph products|.|38|
|3.2|Spectral decomposition of product graphs . . . . . . . . . . . . . . . . .|.|40|
|3.3|Anisotropic graph flter functions in two dimensions<br>. . . . . . . . . . .|.|43|
|3.4|Graph signal reconstruction real data results<br>. . . . . . . . . . . . . . .|.|62|
|3.5|The scaling behaviour of the number of steps required for convergence as|||
||a function of _γ_ and _m_. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.|68|
|4.1|Global explanatory variables used in the environmental modelling appli-|||
||cation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.|92|
|4.2|Local explanatory variables used in environmental modelling application|.|93|
|4.3|The Root Mean Square Error and _R_2 statistic are shown for the fve|||
||models on the train, validation and test sets.<br>. . . . . . . . . . . . . . .|.|95|
|5.1|Anisotropic graph flter functions in an arbitrary number of dimensions|.|111|
|5.2|Information on the tax status of green bonds<br>. . . . . . . . . . . . . . .|.|125|
|5.3|Results for bond yield experiments . . . . . . . . . . . . . . . . . . . . .|.|127|
|6.1|The posterior covariance matrix appearing in the tensor GSR, KGR, RNC|||
||and KR-RNC models.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|.|131|
|6.2|The explanatory variables used to predict the posterior log-variance<br>. .|.|135|



x 

## **Abbreviations** 

|ASP|Algebraic Signal Processing|
|---|---|
|CGM|Conjugate Gradient Method|
|CNN|Convolutional Neural Network|
|DFT/DCT/DST|Discrete Fourier/Cosine/Sine Transform|
|DSP|Digital Signal Processing|
|FFT/FCT/FST|Fast Fourier/Cosine/Sine Transform|
|GFT|Graph Fourier Transform|
|GLS|Generalised Least Squares|
|GNN|Graph Neural Network|
|GSP|Graph Signal Processing|
|GSR|Graph Signal Reconstruction|
|IGFT|Inverse Graph Fourier Transform|
|IRLS|Iteratively Reweighted Least Squares|
|JIT|Just in Time|
|KGR|Kernel Graph Regression|
|MAP|Maximum A Posteriori|
|MWGSP|Multiway Graph Signal Processing|
|PCA|Principal Component Analysis|
|PSD|Positive Semi-Defnite|
|RKHS|Reproducing Kernel Hilbert Space|
|RMSE|Root Mean Square Error|
|RNC|Regression with Network Cohesion|
|SGT|Spectral Graph Theory|
|SIM|Stationary Iterative Method|
|SNR|Signal to Noise Ratio|
|WFL/SFL|Weak/Strong Filter Limit|



xi 

## **Symbols** 

Unless otherwise specified, the following naming conventions apply. 

|**Integer constants**||
|---|---|
|_N_|The number of nodes in a graph|
|_T_|The number of time points considered|
|_M_|The number of explanatory variables|
|_Q_|The number of queries|
|**Integer variables**||
|_n_|The index of a specifc node in a graph|
|_t_|The index of a specifc time point|
|_m_|The index of a specifc explanatory variable|
|_q_|The index of a specifc query|
|_i, j, k_|Generic indexing variables|
|**Scalar variables**||
|_α_|An autocorrelation regularisation parameter|
|_β_|A hyperparameter characterising a graph flter|
|_γ_|A precision parameter|
|_λ_|An eigenvalue _or_ ridge regression penalty parameter|
|_µ_|The mean of a random variable|
|_σ_2|The variance of a random variable|



xii 

_Symbols_ 

xiii 

|**Matrix Operators**||
|---|---|
|**A**|The graph adjacency matrix|
|**D**|A diagonal matrix|
|**H**|A graph flter _or_ Hessian matrix|
|**I**_N_|The (_N × N_) identity matrix|
|**O**_N_|An (_N × N_) matrix of ones|
|**K**|A kernel (Gram) matrix|
|**L**|The graph Laplacian|
|**M**|SIM update matrix|
|**U**|Laplacian eigenvector matrix|
|**V**|Kernel eigenvector matrix|
|**Λ**|A diagonal eigenvalue matrix|
|**Σ**|A covariance matrix|
|**Ψ**|A preconditioning matrix|
|**Φ**|A matrix of basis functions|
|**Vectors/matrices/tensors**||
|**e**_,_**E**_,_**_E_**|The prediction residuals|
|**f**_,_**F**_,_**_F_**|A predicted graph signal|
|**g**_,_**G**_,_**_G_**|A spectral scaling vector/matrix/tensor|
|**j**_,_**J**_,_**_J_**|Alternative spectral scaling vector/matrix/tensor|
|**_M_**|Latent probability tensor|
|**s**_,_**S**_,_**_S_**|A binary selection vector/matrix/tensor|
|**q**_,_**Q**_,_**_Q_**|Alternative binary selection vector/matrix/tensor|
|**x**_,_**X**_,_**_X_**|Vector/matrix/tensor of explanatory variables|
|**y**_,_**Y**_,_**_Y_**|(Partially) observed graph signal|
|**z**_,_**Z**_,_**_Z_**|Signal of spectral components|
|_ω,_**Ω**_,_**_Ω_**|Log marginal variance signal|
|**1**_N_|A length-_N_ vector of ones|
|**e**_i_|The _i_-th unit basis vector|
|**w**_,_**W**|A vector/matrix of regression coefcients|
|**_α_**|A fexible intercept vector/tensor|
|**_β_**|A graph flter parameter vector|
|**_θ_**|A aggregated coefcient vector [**_α_**_⊤,_ **_β_**_⊤_]_⊤_|



_Symbols_ 

xiv 

|**Functions**||
|---|---|
|_g_(_·_)|A graph flter function|
|_p_(statement)|The probability that a statement is true|
|_π_(_·_)|A probability density function|
|_ξ_(_·_)|Optimisation target function|
|_κ_(_·, ·_)|A kernel function|
|**Operations**||
|(_·_)_⊤_|Transpose of a matrix/vector|
|_|| · ||_F|The Frobenius norm|
|tr (_·_)|The trace of a square matrix|
|vec (_·_)|Convert a matrix to a vector in column-major order|
|vecRM(_·_)|Convert a matrix to a vector in row-major order|
|mat (_·_)|Convert a vector to a matrix in column-major order|
|matRM(_·_)|Convert a vector to a matrix in row-major order|
|diag (_·_)|Convert a vector to a diagonal matrix|
|diag_−_1 (_·_)|Convert the diagonal of a matrix into a vector|
|_⊗_|The Kronecker product|
|_⊕_|The Kronecker sum|
|_◦_|The Hadamard product|
|**Graphs**||
|_G_|A graph|
|_V_|A vertex/node set|
|_E_|An edge set|
|**Miscellaneous**||
|ˆ(_·_)|The estimator of a matrix/vector/tensor|
|_O_(_·_)|The runtime complexity|
|_xi_|A vector element|
|**X**_i_|A matrix column|
|**X**_ij_|A matrix element|



## **Identities** 

vec ( **AXB** ) ( **B** _[⊤] ⊗_ **A** ) vec ( **X** ) tr � **A** _[⊤]_ **B** � vec ( **A** ) _[⊤]_ vec ( **B** ) **AC** _⊗_ **BD** ( **A** _⊗_ **B** )( **C** _⊗_ **D** ) ( **A** _⊗_ **B** ) _[−]_[1] **A** _[−]_[1] _⊗_ **B** _[−]_[1] tr � **X** _[⊤]_ **AYB** � vec ( **X** ) _[⊤]_ ( **B** _[⊤] ⊗_ **A** ) vec ( **Y** ) vec ( **J** _◦_ **Y** ) diag�vec ( **J** ) �vec ( **Y** ) diag _[−]_[1][�] **A** diag( **x** ) **B** � ( **B** _[⊤] ◦_ **A** ) **x** 

xv 

## **Publications** 

Below is a list of related academic publications submitted during this PhD. Some of the work presented in these papers contains material also presented in this thesis. 

1. Antonian, E. B., Peters, G. W., Chantler, M. J. (2023). PyKronecker: A Python Library for the Efficient Manipulation of Kronecker Products and Related Structures. In _The Journal of Open Source Software, 8(81)._ 

2. Antonian, E. B., Peters, G. W., Chantler, M. J. (2024). Kernel Generalized Least Squares Regression for Network-Structured Data. Submitted to _Plos One_ (In Review). 

3. Antonian, E. B., Peters, G. W., Chantler, M. J. (2024). Bayesian Reconstruction of Cartesian Product Graph Signals with General Patterns of Missing Data. Submitted to _Journal of the Franklin Institute_ (In Review). 

xvi 

## **Chapter 1** 

## **Introduction** 

In the field of discrete mathematics, the term “graph” denotes a collection of distinct objects that may possess some form of pairwise connection or association. The discrete objects that make up the graph are referred to as nodes (or vertices), and their connections are known as edges (or arcs). This abstract structure can be employed to represent numerous real-world phenomena. For example, in an airline route map, nodes could symbolise airports, and edges could indicate the presence of a direct flight. 

Graphs and network models are utilised in many actively researched areas of mathematics, including network processes such as epidemic modelling [Pare et al., 2020], Graph Neural Networks (GNNs) [Zhou et al., 2020], graphical models [Holmes and Jain, 2008], and semi-supervised learning [Chong et al., 2020]. 

In this thesis, the subject of focus is Graph Signal Processing (GSP), a rapidly evolving field that sits at the intersection of spectral graph theory, statistics, and data science [Ortega et al., 2018]. GSP is an actively researched area devoted to the mathematical analysis of signals that are defined over the nodes of a graph, simply referred to as _graph signals_ . 

**==> picture [159 x 186] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>2 3<br>4<br>5 6<br>7 8<br>9<br>10<br>**----- End of picture text -----**<br>


Figure 1.1: A visual representation of a simple graph with 10 nodes and 20 edges. 

1 

Chapter 1. _Introduction_ 

2 

**==> picture [159 x 148] intentionally omitted <==**

Figure 1.2: A graphical depiction of a smooth graph signal. Here, the value of the signal at each node is represented by its colour. 

A graph signal represents a value that is measured simultaneously at every node in a graph. For example, consider a social media network, where each node represents an individual, and the presence of an edge indicates that the two individuals have connected. An example of a graph signal in this context could be the age of each person in the network, or a score indicating their propensity to engage with certain content. In either case, this is a value that could theoretically be measured or estimated across the network, though it may be subject to missing data or noise. 

GSP typically uses tools that stem from classical signal processing, where the goal is to manipulate data that resides on a regular domain such as audio, images or radio. GSP utilises spectral graph theory to generalise these classical techniques, leading to graph-based counterparts of algorithms such as filtering, sampling, and reconstruction [Shuman et al., 2013]. Applications of such methods are numerous, ranging from social networks [Dong et al., 2015] and brain connectivity modelling [Huang et al., 2018] to sensor networks [Zhu and Rabbat, 2012], and protein structures [Srivastava et al., 2023]. GSP today remains rapidly evolving, with advancements in both theory and practical applications occurring constantly [Leus et al., 2023]. As such, there are numerous opportunities for contribution, making it an exciting and dynamic area of research. 

## **1.1 Research goals** 

The goal of this thesis is to provide contributions to the areas of multivariate graph signal reconstruction and regression. A single signal, measured over a network comprising _N_ nodes, is an example of a univariate structure and can be described by a vector **y** _∈_ R _[N]_ . Our methods, by contrast, are designed to be applicable to higher-dimensional objects. For example, _T_ samples of a graph signal measured across time can be described by a matrix **Y** _∈_ R _[N][×][T]_ . This kind of two-dimensional data can also be viewed as a single graph signal measured on the nodes of a Cartesian product graph [Imrich and Klavˇzar, 2000]. More generally, a tensor-valued signal _**Y** ∈_ R _[N]_[1] _[×][N]_[2] _[×][...][×][N][d]_ can be understood as a signal on a _d_ -dimensional Cartesian product graph [Stanley et al., 2020]. 

Our aim is to expand the existing literature on multivariate GSP by presenting several novel Bayesian models for reconstructing partially observed graph signals, with and without additional 

Chapter 1. _Introduction_ 

3 

explanatory variables. Graph signal reconstruction is a well-studied topic in GSP, however, the majority of published literature to date has focused on univariate, or time-varying signal models that provide point estimates for the missing values. We aim to generalise this in two ways. First, we present a rich Bayesian formulation, that outputs not only a point estimate but a full probability distribution quantifying prediction uncertainty. Furthermore, our goal is to produce models applicable to graph signals defined on arbitrary Cartesian product graphs, which naturally extend univariate and time-varying models. While the input to a graph signal reconstruction problem is typically only the partially observed graph signal and the topology of the underlying graph, we also consider the situation in which additional explanatory variables are available to aid in the estimation process. Therefore another key objective of ours is to produce graph signal regression models, applicable to a range of different data scenarios, that are robust to missing data. 

As mentioned, a key aspect of our models is the Bayesian formulation, which produces a full posterior probability distribution over the unknown reconstructed signal, rather than a single point estimate. Given the high-dimensional nature of the data, the posterior covariance, which contains information regarding the correlation between every element in the multivariate signal _**Y**_ , is often too large to process with consumer-grade computer hardware. Therefore, another objective of ours is to develop efficient methods for extracting information regarding the prediction uncertainty. In particular, we consider two related but separate tasks: estimating the marginal posterior variance (node-level uncertainty) and drawing samples directly from the posterior. 

The majority of GSP models tend to focus on real-valued graph signals, leaving signals with binary or categorical entries relatively unexplored. It is therefore an additional goal of ours to develop new statistical reconstruction and regression algorithms for such graph signals. Although related tasks have been examined within semi-supervised learning in machine learning and GNNs in deep learning, we aim to introduce and showcase novel Bayesian models that are grounded firmly in the theoretical framework of GSP. 

The high-dimensional nature of the models explored in this thesis comes with a unique set of challenges concerning computational robustness and efficiency. As such, a core objective is to reduce the computational cost of our algorithms wherever possible and to provide a detailed and transparent analysis of their time and memory complexity. The models we present are designed to be applicable to a wide range of application areas, and as such, throughout this thesis, we also provide illustrative examples and case studies to demonstrate their applicability. 

Chapter 1. _Introduction_ 

4 

## **1.2 GSP fundamentals** 

A graph, _G_ , with _N_ vertices is described by a node-set _V_ , and an edge set _E_ . In this thesis, we will be primarily concerned with undirected graphs without self-loops, meaning the edges have no preferential direction and nodes do not connect to themselves. By imposing some arbitrary but consistent ordering on the nodes, this graph can also be described by an _N × N_ adjacency matrix **A** , where the entry **A** _ij_ = **A** _ji ≥_ 0 holds the strength of connection between nodes _i_ and _j_ . In the basic case of a non-weighted graph, **A** _ij_ is simply one if the corresponding edge exists and zero otherwise. Using the same ordering, a graph signal can be represented by a vector, **y** , of length _N_ , where **y** _i_ holds the value of the graph signal at node _i_ . 

One key property of a graph signal is its _smoothness_ . Intuitively speaking, a smooth graph signal should exhibit gentle variation between closely connected nodes, as illustrated in fig. 1.2. Conversely, a rough graph signal might see large jumps in signal value between neighbouring nodes. Mathematically, the smoothness of a signal, **y** , defined over the nodes of an undirected graph, can be measured in several ways. One simple option is the total square variation (TV2), which is defined as follows. 

**==> picture [282 x 31] intentionally omitted <==**

This metric, also known as Dirichlet energy, sums up the square difference in signal value at each neighbouring node, weighted by the corresponding entry in the adjacency matrix, with the factor of a half adjusting for the double counting of nodes. It can also be written in terms of a single quadratic form, by introducing a new matrix **L** - the so-called graph _Laplacian_ . 

**==> picture [245 x 13] intentionally omitted <==**

The Laplacian, like the adjacency matrix **A** , is another symmetric _N × N_ matrix and is defined as **L** = **D** _−_ **A** , where **D** is the degree matrix. **D** is a diagonal operator, where entry **D** _ii_ holds the sum of all the edge weights linked to node _i_ , or in other words, the vector along the diagonal of **D** is the column (or row) sum of **A** . The Laplacian, which can be interpreted as a generalisation of the discrete second-order derivative operator for an irregular topology, is of central importance to many aspects of GSP [Shuman et al., 2013]. 

Chapter 1. _Introduction_ 

5 

It is straightforward to show that the two expressions for the total square variation given in eqs. (1.1) and (1.2) are equivalent; see for example chapter 3 of Ortega [2022]. A few basic facts stand out about the Laplacian quadratic form. 

1. **y** _[⊤]_ **Ly** _≥_ 0 for any **y** . Since TV2( **y** ) sums the square difference between the signal at each pair of nodes, weighted by the non-negative entries of the adjacency matrix, the Laplacian quadratic form must be strictly non-negative. By definition, this implies that the matrix **L** is positive semi-definite (PSD). 

2. **1** _[⊤]_ **L1** = 0, where **1** is a length- _N_ vector of ones. If the signal of interest is constant over the whole graph, the total square variation must be zero. Moreover, if the graph contains two or more isolated sub-graphs, with edges connecting nodes within each clique but not between cliques, then any signal that is constant over each sub-graph will have a total square variation of zero. 

Since **L** is positive semi-definite, its eigenvalues are all real and non-negative, and its eigenvectors can be chosen to be real and orthonormal. Thus, **L** can be decomposed as follows. 

**==> picture [235 x 12] intentionally omitted <==**

Here, **U** is the orthogonal, _N × N_ matrix of eigenvectors _{_ **u** _i}_ , and **Λ** is the diagonal matrix of corresponding eigenvalues _{λi}_ , typically arranged in ascending order. As **U** is orthonormal, it holds that **u** _[⊤] i_ **[u]** _[j]_[=] _[δ][ij]_[,][and][that] _[{]_ **[u]** _[i][}]_[form][a][set][spanning][R] _[N]_[.] Given the definition of the Laplacian quadratic form, the eigenvectors are the unique set of orthonormal vectors that sequentially minimise the total square variation, subject to perpendicularity to all those preceding [Spielman, 2019]. 

**==> picture [144 x 123] intentionally omitted <==**

Chapter 1. _Introduction_ 

6 

**==> picture [354 x 192] intentionally omitted <==**

**----- Start of picture text -----**<br>
λ 1 = 0 λ 2 = 0 . 018 λ 3 = 0 . 046 λ 4 = 0 . 069<br>λ 5 = 0 . 074 λ 6 = 0 . 102 λ 7 = 0 . 118 λ 8 = 0 . 174<br>**----- End of picture text -----**<br>


**==> picture [354 x 120] intentionally omitted <==**

Figure 1.3: A visualisation of the first eight Laplacian eigenvectors, alongside their associated eigenvalues, for a network of local authority regions in the UK. Each node represents a region, and each pair of regions share an edge if they border one another (or have a direct ferry crossing). Colour is used to represent the value of the graph signal at each node. 

In this way, the eigenvectors of the graph Laplacian can be understood as sequentially less smooth with respect to the topology of the graph. The corresponding eigenvalue, referred to as the frequency, gives a value specifying how “rough” each eigenvector is relative to the others, as measured by TV2. Note that, for any undirected graph, the first Laplacian eigenvector will always be constant with an eigenvalue of zero. Figure 1.3 gives a visual depiction of the first eight Laplacian eigenvectors and eigenvalues for a network representing local authority regions in the UK.[1] 

Since _{_ **u** _i}_ span the total space of R _[N]_ , any graph signal, **y** , can be decomposed into a weighted sum of the Laplacian eigenvectors. This parallels the classical Fourier transform, which expands signals into the basis of complex exponentials [Sneddon, 1995]. As such, any graph signal, **y** , has a dual representation, **z** , in the frequency domain. Transformations between these two representations can be achieved by applying the Graph Fourier Transform (GFT) and Inverse 

> 1Using boundary data published by the Office for National Statistics [ONS, 2019] 

Chapter 1. _Introduction_ 

7 

**==> picture [272 x 197] intentionally omitted <==**

**----- Start of picture text -----**<br>
λ 1 = 0 λ 2 = 0 . 004 λ 3 = 0 . 004<br>λ 4 = 0 . 016 λ 5 = 0 . 016 λ 6 = 0 . 035<br>λ 7 = 0 . 035 λ 8 = 0 . 063 λ 9 = 0 . 063<br>**----- End of picture text -----**<br>


**==> picture [272 x 67] intentionally omitted <==**

Figure 1.4: A visualisation of the first nine Laplacian eigenvectors of a cycle graph with 50 nodes, along with their associated eigenvalue. 

Graph Fourier Transform (IGFT), which amount to multiplying by the matrices **U** _[⊤]_ and **U** , respectively. 

**==> picture [254 x 12] intentionally omitted <==**

**==> picture [255 x 11] intentionally omitted <==**

For some simple graphs, the GFT is equivalent to a well-known transform in classical signal processing. For example, the Laplacian of the cycle graph (i.e. a set of nodes connected in a loop) has eigenvectors that can be expressed as sines and cosines (or, in full generality, complex exponentials) as visualised in fig. 1.4. This concept has been used to establish a rigorous connection between GSP and classical signal processing, through the study of Algebraic Signal Processing (ASP) [Puschel and Moura, 2003, Sandryhaila and Moura, 2013b]. With the GFT and IGFT defined, a wide range of potential models is opened up, many of which can be understood as direct generalisations of methods from conventional signal processing. Classical tasks such as filtering, denoising, reconstruction, sampling, compression etc. can all be translated into the GSP paradigm, setting the stage for a new era of signal processing that leverages graph structures for more complex and rich data analysis, and opening the door to a wealth of novel applications. 

Chapter 1. _Introduction_ 

8 

## **1.3 Example applications** 

Graph signal processing methods have proven effective in numerous real-world applications. In this brief section, we highlight several use cases from the literature to serve as motivation for the content of this thesis. Many of these areas are used as illustrative examples for the methods developed in this work. 

## **1.3.1 Biology** 

The world of biology provides numerous interesting use cases for graph signal processing methods [Li et al., 2023]. One area which has garnered significant interest is in analysing protein-protein interactions. Here, the concept is to model a set of proteins as nodes in an “interactome”, which is the network of physical molecular interactions in a particular cell. Recent work such as Colonnese et al. [2021] used GSP methods to predict new interactions between proteins, while work such as Jha et al. [2022] used graph neural networks for the same task. These models aim to automate the prediction of protein interactions, reducing the time and cost associated with experimental methods. Other work has modelled an individual protein molecule as a network of residues connected based on their physical distance in 3D space, to predict its biophysical properties [Srivastava et al., 2023]. 

Another domain in biology that has benefited from GSP methods is brain connectivity modelling. Studies such as Atasoy et al. [2016], Goldsberry et al. [2017], Itani and Thanou [2021], Menoret et al. [2017] have found that the graph-spectral frequency profile of signals derived from fMRI imaging can provide valuable insight into brain activity. Specifically, these and related works have identified specific Laplacian spectral profiles associated with different emotional states, task familiarity, and neurological diseases. 

## **1.3.2 Transportation and infrastructure** 

Another domain in which GSP methods have been extensively applied is transportation and infrastructure. In Hasanzadeh et al. [2017], the authors propose an adaptive ARMA model in the graph frequency domain for real-time traffic prediction, achieving a substantial performance increase over non-graph-aware alternatives. Traffic prediction was also addressed using GSP methods in Chakraborty [2017] with a technique known as trend filtering [Wang et al., 2016]. Automatic incident detection using spatiotemporally denoised thresholds was applied in Chakraborty et al. [2019]. In Xiu et al. [2022], the authors used a spatial-temporal multi-graph convolutional wavelet network to predict passenger numbers on a metro system. 

Chapter 1. _Introduction_ 

9 

GSP has also been employed to analyse patterns of power consumption in electricity grids [Ramakrishna and Scaglione, 2021], pressure in hydraulic networks [Zhou et al., 2022b] and leak detection in water networks [Orn et al., 2022]. In He et al. [2018] and Zheng et al. [2022], the authors utilised GSP to address non-intrusive load disaggregation—an active area of research in the field of smart grids and energy conservation where the goal is to estimate each appliance’s contribution to total consumption. In Ying et al. [2022], the authors tackle the recovery of harmonic data lost during power transmission, based on spectral graph theory, and in Wang et al. [2022c], the authors use GSP to identify abnormal batteries from cell-level voltage signals in a network of electric bicycle charging stations. 

## **1.3.3 Finance and economics** 

Networks have been used in financial and economic models for many years [Marti et al., 2021], yet recently GSP has found some interesting use cases. In Vinicius et al. [2020], the authors employ a spectral model to learn an underlying graph structure from financial time-series data, showing that meaningful physical interpretations related to the market index factor can be extracted from this representation. In Zhang et al. [2023b], the authors consider how GSP can be incorporated into momentum-based financial forecasting models, demonstrating that the additional topological information can enhance the accuracy of such models. 

GSP has also been used recently in the context of asset allocation and portfolio theory. The portfolio cut paradigm, introduced in Dees et al. [2020], is a graph-theoretic portfolio partitioning technique that enables investors to group economically meaningful clusters of assets. In Arroyo et al. [2022], this concept is extended to include a dynamic portfolio, with time-evolving clusters. 

Graph Neural Networks have also been used extensively in financial applications [Wang et al., 2022a]. 

## **1.3.4 Sensor networks** 

Sensor networks are a classic application for GSP methods, as a graph is typically straightforward to construct from the physical positioning of the devices [Jablonski, 2017]. Many applications in this domain focus on distributed algorithms, as sensors and IoT devices are naturally suited to local communication. The aims of such applications are varied, encompassing tasks like compression [Zhu and Rabbat, 2012], denoising [Tay, 2021], reconstruction [Wang et al., 2015b], and distributed data processing [Chi et al., 2022]. 

Chapter 1. _Introduction_ 

10 

Some of the earliest work classified as GSP involved applications with sensor data, for example, Guestrin et al. [2004]. Here, the authors used local basis functions to design a regression algorithm capable of fast convergence with only local communication. In Wagner et al. [2005], the authors develop a distributed wavelet transform and applied it to a signal compression task over a network of sensors. 

## **1.4 Contributions** 

In this thesis, we present several contributions to the theory and practice of graph signal processing, the most prominent of which are summarised below. 

-  We propose a parametrised family of low-pass filters for signals on Cartesian product graphs composed of two or more factor graphs. 

-  Using these filters to construct graph-spectral priors, we propose a holistic Bayesian framework for reconstruction and regression tasks with partially observed, real-valued signals on Cartesian product graphs. 

-  We give practical advice for implementing such models by providing a detailed analysis of their runtime complexity as a function of the model hyperparameters and input data composition. 

-  We present PyKronecker, a Python library for the efficient and scalable manipulation of Kronecker-structured operators and tensor-valued signals. 

-  We propose and evaluate several methods for characterising the posterior covariance of our models that are scalable to large graphs with multiple tensor dimensions. 

-  We extend and generalise our reconstruction and regression algorithms to graph signals that contain binary or categorical observations. 

## **1.5 Thesis organisation** 

The core content of this thesis begins in chapter 3, with the reconstruction of signals on general two-dimensional Cartesian product graphs. Here, we introduce our Bayesian model formulation and present two iterative algorithms for computing the posterior mean. In chapter 4, we consider how the reconstruction problem can be modified by introducing additional explanatory variables, leading to three novel multivariate regression models applicable to different modelling scenarios. In chapter 5, we generalise the reconstruction and regression techniques developed in the preceding two chapters to _d_ -dimensional tensor-valued data, under the “Multiway” GSP 

Chapter 1. _Introduction_ 

11 

(MWGSP) framework. This is followed, in chapter 6, by an investigation into the posterior covariance of the models, where we develop scalable techniques for estimating the marginal variance and direct sampling. Finally, in chapter 7, we modify the reconstruction and regression algorithms to handle binary and categorical graph signals. Along the way, there are several methodological contributions as well as some detailed case studies. We begin, in chapter 2, by defining the precise scope of this thesis, reviewing the relevant literature, and presenting a more detailed breakdown of our core contributions. 

## **Chapter 2** 

## **Literature Review, Contributions and Scope** 

This literature review aims to provide an overview of the field of Graph Signal Processing (GSP) with a particular emphasis on multivariate reconstruction and regression models. First, we will give some historical context for the subject, highlighting the key theoretical advancements and canonical examples, before moving towards the contemporary developments relevant to this thesis. This begins with a basic review of graph filters and kernels, which are foundational building blocks of the methods presented in this thesis. Next, we discuss the topic of graph signal reconstruction, before covering different approaches to regression with graph signals. This is followed by a survey of the emerging field of multiway graph signal processing, and finally, we discuss node classification methods. For each of these topics, we explain how the methods presented in this thesis contribute to the field. 

By presenting a holistic view of the existing literature, this review aims to set a firm foundation upon which we can build the discussion for our ensuing research questions. In addition, this chapter will also hone in on the specific scope of this thesis and define the boundaries of our research. In particular, we aim to identify the areas of interest that remain under-explored or incomplete in the current state of research, as well as demarcate the topics which are not directly relevant to our research focus. 

## **2.1 A historical perspective on GSP** 

Though GSP as a field in its own right is generally understood to have been established in the early 2000s, its underlying conceptual framework draws upon the well-established fields of 

12 

Chapter 2. _Literature Review, Contributions and Scope_ 

13 

Spectral Graph Theory (SGT), and Digital Signal Processing (DSP), which both date back several decades. SGT is a branch of mathematics that studies the eigenvalues and eigenvectors associated with a graph’s adjacency or Laplacian matrix to gain insight into its structural properties [Chung, 1997]. Early work on SGT can be traced back to the 1950s and ’60s [Collatz and Sinogowitz, 1957, Hoffman, 1969], although many of the concepts had already been studied in parallel within quantum chemistry [Huckel, 1931]. One of the foundational results in SGT is the multiplicity of the Laplacian’s zero eigenvalue gives the number of connected components in the graph [Cvetkovic et al., 1980]. Another key result is Cheeger’s inequality, which relates the second smallest eigenvalue of the Laplacian (also known as the algebraic connectivity) to the isoperimetric number of the graph (a measure of a graph’s bottleneck) [Cheeger, 1971]. 

Digital Signal Processing (DSP), sometimes considered a branch of electrical engineering, utilises digital computation to analyse, transform, or filter signals, which can be in forms such as sound, images, and sensor data [Rabiner and Gold, 1975]. The core principles of DSP are grounded in linear algebra, calculus, differential equations, and statistics. This theoretical underpinning has led to a plethora of practical applications across varied fields, such as telecommunications, audio processing, image and video processing, astronomy, and seismology, to name a few. Within DSP, the Discrete Fourier Transform (DFT) and its fast algorithmic implementation, the Fast Fourier Transform (FFT), play a central role, with many tasks such as reconstruction, denoising, compression, and filtering requiring analysis and manipulation of the frequency content of signals [Duhamel and Vetterli, 1990]. 

GSP began to take shape as a separate discipline around the start of the 21st century, as the proliferation of data and advancements in computer technology gave rise to more complex, irregular, and high-dimensional data structures. The theoretical framework underpinning GSP emerged from work on Algebraic Signal Processing (ASP), with several papers published by Puschel and Moura from 2003 to 2008 establishing an axiomatic approach to discrete time signal processing [Puschel and Moura, 2003, 2006, 2008]. This mathematical formalism, based on the concept of shift operators, established a unifying framework for several concepts from classical signal processing. For example, under the ASP paradigm, the Discrete Cosine Transform (DCT) and DFT are understood as generated from different discrete shift operators (a chain and cycle respectively) [Isufi et al., 2024]. 

Meanwhile, in the data science and machine learning community, concepts from SGT were being applied to nonlinear dimensionality reduction using the Laplacian eigenbasis [Belkin and Niyogi, 2003, Donoho and Grimes, 2003, Roweis and Saul, 2000]. This was followed by work such as Kondor and Lafferty [2002] and Smola and Kondor [2003], who studied the topic of graph kernels. This work was subsequently applied in semi-supervised learning, where the goal is to maximise the utility of unlabelled data using its topology in feature space [Belkin et al., 2004a, Zhou and 

Chapter 2. _Literature Review, Contributions and Scope_ 

14 

Sch¨olkopf, 2004, Zhu et al., 2003]. We return to the topic of graph kernels in greater detail in section 2.2. 

Around the same time, in the signal processing community, authors were working on both distributed and global algorithms for denoising and regression on sensor networks Guestrin et al. [2004], Wagner et al. [2006, 2005]. 

In the early 2010s, two distinct yet complementary approaches to GSP emerged, as discussed in Leus et al. [2023]. The first approach, often credited to Sandryhaila and Moura [2013b,c], adopted an algebraic perspective, building upon existing work in Algebraic Signal Processing. This methodology primarily focused on defining the Graph Fourier Transform and related concepts using the foundational operation of graph shifts. Conversely, the second approach, as proposed by Hammond et al. [2011], Shuman et al. [2013], endorsed the use of the graph Laplacian as the central operator for GSP algorithms. This second paradigm, which aligns closely with the concepts presented in section 1.2, is also the primary approach utilised in this thesis. 

## **2.2 Graph kernels and graph filters** 

In GSP, two distinct but closely related concepts are graph filters and graph kernels. In the Laplacian-based GSP paradigm, both can be understood as spectral operators which modify the frequency profile of a graph signal, providing a direct generalisation of conventional filters in classical signal processing. (It is worth noting that, in this context, ‘graph kernel’ should not be confused with another concept, bearing the same name, which refers to distance measures between pairs of graphs [Kriege et al., 2020].) Graph filters/kernels play a fundamental role in GSP, and are at the heart of numerous algorithms including reconstruction [Romero et al., 2017b], anomaly detection [Xiao et al., 2021b], GNNs [Gama et al., 2020] and graph learning [Mateos et al., 2019]. 

A graph filter or kernel is characterised by a function _g_ ( _λ_ ), which can be applied to scale the frequency profile of a signal **y** . This is performed by initially transforming **y** into the frequency domain via the GFT, then subsequently scaling the _i_ -th frequency component by _g_ ( _λi_ ) independently, and finally transforming back to the node domain via the IGFT. Consequently, it can be represented by a matrix operator **H** _∈_ R _[N][×][N]_ as follows. 

**==> picture [242 x 12] intentionally omitted <==**

Equivalently, **H** can be understood as originating from the direct application of the function _g_ ( _·_ ) to the Laplacian, represented as **H** = _g_ ( **L** ). Here, this operation should be interpreted as 

Chapter 2. _Literature Review, Contributions and Scope_ 

15 

|**Filter**||_g_(_λ_; _β_)|
|---|---|---|
|1-hop random walk||(1 +_βλ_)_−_1|
|Difusion||exp(_−βλ_)|
|ReLu|max(1_−βλ,_0)||
|Sigmoid|2<br>�|1 + exp(_βλ_)<br>�_−_1|
|Gaussian|exp<br>�<br>_−_(_βλ_)2�||
|Bandlimited|1_,_|if_βλ ≤_1 else 0|



Table 2.1: Some example low-pass graph filter functions 

an analytic function of a matrix, that is, a series sum of matrix powers [Bhatia, 1997]. The function _g_ ( _·_ ) can be set such that it promotes certain properties in the output signal. For example, a low-pass filter (such as those specified in table 2.1) is a monotonically decreasing function, attenuating the high-frequency content of a signal. In table 2.1, we describe each filter by a positive parameter _β_ which controls the filter strength, with higher values resulting in more aggressive attenuation of high-frequency content. The choice of filter will depend on the application of interest and may rely on expert domain knowledge about the spectral profile of the graph signals. 

In the GSP community, the term ‘filter’ is typically preferred when referring to this class of operator [Shuman et al., 2013], although some favour the term ‘kernel’ [Ioannidis et al., 2016, Romero et al., 2017a]. Often, the primary practical distinction is that a kernel is an increasing function, used to construct penalty terms in regularised problems, whereas a filter is a decreasing one, interpreted as providing spectral transformations on graph signals. In Romero et al. [2017b], the authors advocate for the preferential use of the term kernel, arguing that many GSP methods have an elegant interpretation in terms of Reproducing Kernel Hilbert Spaces (RKHSs). Within the machine learning community, where kernel methods and RKHSs are common, the kernel interpretation is typically favoured [Kondor and Lafferty, 2002, Smola and Kondor, 2003]. Regardless, either convention can be used, and in this thesis, we predominantly describe our methods in terms of filters since they provide a more direct correlation with conventional signal processing techniques, offering an intuitive way to manipulate and reason about the spectral content of graph signals. 

Chapter 2. _Literature Review, Contributions and Scope_ 

16 

## **2.2.1 Bayesian approaches to GSP** 

Spectral operators can be used to define probability distributions over smooth graph signals. An early example of this approach can be found in Gadde and Ortega [2015], where the authors propose a Gaussian Random Field (GRF) model for generating graph signals. In particular, they propose a method for vertex sampling that treats signals as random variables drawn from the following underlying multivariate Gaussian distribution. 

**==> picture [261 x 13] intentionally omitted <==**

This probabilistic interpretation offers a principled way of reasoning about graph signals, making the connection between GSP and specific methods from semi-supervised learning more apparent [Zhu et al., 2003]. A more general probabilistic framework for graph signal processing is proposed in Zhang et al. [2015], where distributions are parametrised by graph filters, offering increased flexibility. Once again, graph signals are interpreted as Gaussian Random Fields, however, the covariance structure is expanded to encompass a greater variety of spectral profiles. In particular, the distribution is given by 

**==> picture [252 x 13] intentionally omitted <==**

where **H** is a generic graph filter. Since **H**[2] = **U** _g_[2] ( **Λ** ) **U** _[⊤]_ , this distribution can be interpreted as an independent multivariate Gaussian in the Laplacian eigenbasis, where the covariance of the _i_ -th basis vector is given by _g_[2] ( _λi_ ). Since, for a low pass filter, _g_ ( _·_ ) is monotonically decreasing, this naturally results in higher probability density placed on smoothly varying graph signals. 

Further insight into this model can be gained from the following considerations. First, start with an independent multivariate normally distributed random variable, denoted as **y** _∼N_ ( **0** _,_ **I** _N_ ) . Applying a graph filter yields a new signal, **Hy** , which has its high-frequency content attenuated in accordance with the properties of the filter. This filtered signal will also be normally distributed, according to **Hy** _∼N_ � **0** _,_ **H**[2][�] . Therefore the process of filtering white Gaussian noise is equivalent to drawing from a distribution with mean zero and covariance **H**[2] , meaning **H**[2] can be interpreted as a covariance matrix for generating smooth, normally distributed graph signals. This flexible approach permits the encoding of various beliefs regarding the frequency profile of graph signals. Figure 2.1 displays an example of a random signal drawn from the distribution of eq. (2.3) using a bandlimited filter. 

This approach is also embraced in Venkitaraman et al. [2020], where the authors use graph filters to construct a Gaussian process regression model over graphs. In particular, they use a GRF to 

Chapter 2. _Literature Review, Contributions and Scope_ 

17 

**==> picture [168 x 247] intentionally omitted <==**

Figure 2.1: An example of a random smooth signal on the UK district graph, sampled from _N_ � **0** _,_ **H**[2][�] using a bandlimited filter. 

specify the prior distribution over their weight matrix, resulting in predictions that are smooth with respect to the graph topology. The filter-based GRF model also provides interpretation for the work of Gadde and Ortega [2015], which can be seen as a special case of this more general formulation. In particular, their chosen covariance matrix can be written in the form ( **L** + _δ_ **I** ) _[−]_[1] = **U** _g_[2] ( **Λ** ) **U** _[⊤]_ , where the filter function is given by _g_ ( _λ_ ) = 1 _/√λ_ + _δ_ . Similarly, [Perraudin and Vandergheynst, 2017] suggest a flexible class of Laplacian-based covariance matrices, however, their focus is on stationary signals with potentially non-Gaussian distributions. In other work such as Dong et al. [2016], the authors take a Bayesian approach to the problem of graph learning, using similar graph-spectral priors. 

In general, many GSP models utilising some form of quadratic Laplacian-based regularisation can be interpreted in Bayesian terms, although this connection often goes undiscussed [Gribonval, 2011]. We believe that taking a transparently Bayesian approach to graph signal reconstruction and regression problems has several benefits. Chiefly among them is the ability to characterise the posterior covariance of the predicted signal, which gives a quantitative measure of the uncertainty associated with the prediction at each node. While most GSP models provide only point estimates, Bayesian methods give a richer output which is useful for understanding the prediction veracity and model limitations. Additionally, Bayesian methods offer a principled way of setting model hyperparameters. For example, regularisation terms acquire a more rigorous statistical interpretation, aiding in their practical application. However, Bayesian models also 

Chapter 2. _Literature Review, Contributions and Scope_ 

18 

introduce computational challenges and typically require specific domain knowledge from the outset. In the context of GSP, presumptions about the signal’s underlying properties must be established beforehand. While this requirement might pose difficulties in certain scenarios, in others, it presents an opportunity. For instance, if the signal of interest is generated through a graph-based diffusion process, employing a diffusion filter is likely to be most effective. 

## **2.2.2 Approximating graph filters with Chebyshev polynomials** 

So far, we have presented graph filters as spectral operators which are constructed by applying a function to the eigenvalues of the graph Laplacian. However, this formulation is predicated on the notion that it is practical to compute and store the eigendecomposition of **L** . Since the time complexity of this operation scales as _O_ ( _N_[3] ), this can quickly become infeasible for large-scale graphs with a high number of nodes. In addition, applying the matrix **H** to a graph signal has complexity _O_ ( _N_[2] ), in general requiring information from all nodes to compute the filtered signal value at each node. 

On the other hand, a typical feature of graphs is sparsity, since the degree of each node is often independent of the size of the graph. This means that multiplication of a graph signal **y** by the Laplacian can often be achieved with complexity _O_ ( _|E|_ ) _≪ O_ ( _N_[2] ). Furthermore, in the context of a physically realised graph such as a sensor network, computation of **Ly** can be executed ‘locally’, in the sense that the result at any particular node depends only on the signal value at the direct neighbours of that node. 

One popular and longstanding technique that takes advantage of both these ideas involves approximating a graph filter using Chebyshev polynomials [Shuman et al., 2018]. In general, if a graph filter can be approximated as a polynomial of the graph Laplacian, then we can take advantage of the sparsity of **L** to efficiently filter signals without performing eigendecomposition. Consider the following standard polynomial approximation to a graph filter. 

**==> picture [292 x 31] intentionally omitted <==**

The Chebyshev polynomial approximation is analogous, but rather than summing powers of **L** directly, we sum order- _K_ polynomials, _T_[¯] _k_ ( **L** ). 

**==> picture [306 x 30] intentionally omitted <==**

Standard Chebyshev polynomials form an orthonormal basis with respect to the product 

Chapter 2. _Literature Review, Contributions and Scope_ 

19 

**==> picture [230 x 218] intentionally omitted <==**

**----- Start of picture text -----**<br>
K = 1 K = 2<br>1.0<br>g( )<br>Approximation<br>0.5<br>0.0<br>K = 3 K = 4<br>1.0<br>0.5<br>0.0<br>0.0 0.5 1.0 1.5 2.0 0.0 0.5 1.0 1.5 2.0<br>**----- End of picture text -----**<br>


Figure 2.2: Successive approximations of the filter function _g_ ( _λ_ ) = exp( _−_ 3 _λ_ ) using Chebyshev polynomials. 

**==> picture [273 x 26] intentionally omitted <==**

and can be used to approximate arbitrary functions within this domain. They also have several well-documented advantages in terms of computational robustness and error over standard polynomial approximations that arise from a Taylor series expansion [Rivlin, 2020]. While the standard Chebyshev polynomials _{Tk}_ are valid on the domain [ _−_ 1 _,_ 1], in the context of graph filters, they must be applicable over the range [0 _, λ_ max], leading to the transformed variant _{T_[¯] _k}_ appearing in eq. (2.5). These can be defined recursively as follows. 

**==> picture [304 x 25] intentionally omitted <==**

subject to the initial conditions 

**==> picture [287 x 23] intentionally omitted <==**

Note that this definition ensures only repeated multiplications by **L** when applying _T_[¯] _k_ ( **L** ) to a graph signal. To approximate an arbitrary filter function _g_ ( _λ_ ), the coefficients _ck_ are given by 

Chapter 2. _Literature Review, Contributions and Scope_ 

20 

**==> picture [345 x 69] intentionally omitted <==**

and can be quickly evaluated numerically. 

Chebyshev polynomials appeared in early papers on GSP, such as [Hammond et al., 2011], in which the authors were concerned with defining wavelet transforms on graphs, also defined in terms of Laplacian-based spectral operators _g_ ( **L** ). Since then, they have been widely used in distributed applications [Shuman et al., 2018], and have also been extensively employed in Graph Neural Networks [Gama et al., 2020]. In Defferrard et al. [2017], Chebyshev polynomials form the basis of convolutional filters with learned parameters, in direct analogy with traditional Convolutional Neural Networks (CNNs). This approach was further developed in Kipf and Welling [2017] by reducing the number of terms in the polynomial to mitigate overfitting. 

In Rimleanscaia and Isufi [2020], Tseng [2020], the authors propose an extension to polynomial filters, which considers a more general class of rational filters, i.e. the ratio between two polynomials. As they describe, in certain circumstances, rational designs can approximate a given frequency response using lower-order polynomials. Notably, when the response is band-limited, rational filters were found to have significantly lower error than standard Chebyshev polynomials, which tend to struggle when approximating the sharp cut-off. In general, rational filtering requires solving a linear system **y** _[′]_ = _P_ ( **L** ) _[−]_[1] _Q_ ( **L** ) **y** , where _P_ and _Q_ are the polynomials occurring in the numerator and denominator, respectively. This incurs an additional computational cost. Furthermore, solving for the coefficients of each polynomial no longer has a closed-form solution and requires addressing a more challenging non-convex, constrained optimisation problem. 

As noted, polynomial approximations are primarily useful because multiplications of a graph signal by the Laplacian can be executed efficiently. In all the papers discussed so far, efficiency has been achieved through distributed execution and/or leveraging Laplacian sparsity. However, another way to exploit the Laplacian structure is if it has a representation in terms of a tensor factorisation. In this thesis, we leverage this fact extensively, focusing on how tensor factorisation can further optimise the computation time and resource usage, especially in cases with highdimensional data or large-scale product graphs. 

Chapter 2. _Literature Review, Contributions and Scope_ 

21 

## **2.3 Graph Signal Reconstruction** 

Graph Signal Reconstruction (GSR), sometimes also known as graph signal interpolation, is a classic problem in GSP [Ortega et al., 2018]. The task can be stated as, given a partially observed graph signal, estimate the signal value at the unobserved vertices using only the topology of the graph. Closely related, is the topic of signal sampling, which seeks to find an informative set of vertices to measure a graph signal, in order to perform an accurate reconstruction [Tanaka et al., 2020]. GSR is often posed as an optimisation problem where one seeks to identify a smooth underlying graph signal, **f** , that simultaneously minimises the square error across the observed nodes, as well as a penalty term _P_ , that enforces some kind of signal smoothness or bandlimited assumption. 

**==> picture [281 x 23] intentionally omitted <==**

Early work on GSR, such as Anis et al. [2016], Narang et al. [2013a], Wang et al. [2015a], mainly focused on the reconstruction of bandlimited graph signals. Here, the goal is to find the optimal reconstruction of a signal using only the first _K_ eigenvectors of the graph Laplacian, with a frequency less than _ω_ (the so-called Paley-Wiener space). In Narang et al. [2013a], for example, this is achieved using an Iteratively Reweighted Least Squares (IRLS) algorithm, with a Chebyshev polynomial approximation to the bandlimited filter. While most work assumes that the cut-off frequency is known, some authors have proposed simultaneously learning it [Marques et al., 2016, Varma et al., 2015]. In other work, such as [Belkin et al., 2004b, Chen et al., 2015, Narang et al., 2013b], a simpler Laplacian-based regularisation term is used to penalise the total square variation. 

In Romero et al. [2017b], the authors propose using a flexible parametrisation of the reconstructed signal profile based on graph kernels. This can be understood as a generalisation of previous works where, rather than specifying a particular form of the penalty term, arbitrary kernel functions of the graph Laplacian are utilised to draw functions from an RKHS. 

Several methods have also been proposed for the reconstruction of time-varying graph signals, in so termed Time-Vertex (T-V) problems. In Qiu et al. [2017], the penalty term in the optimisation objective promotes both smoothness across the graph using a Laplacian penalty, and consistency across time, by introducing a temporal difference operator **D** . Despite being presented in a slightly different way, this also amounts to a Laplacian penalty, since **DD** _[⊤]_ , which appears in the regularisation term, is precisely the Laplacian of a path graph. The problem is then solved for both the noiseless and noisy cases using a gradient projection algorithm with a 

Chapter 2. _Literature Review, Contributions and Scope_ 

22 

backtracking line search. A similar method is adopted in Giraldo et al. [2022], but with a regularised version of the Laplacian for improved computational robustness. In Ioannidis et al. [2016], this approach is modified to incorporate a more dynamic penalty that can adjust the strength of regularisation across the graph and across time independently, using so-termed “space-time kernels”. Furthermore, in this paper, as well as Ioannidis et al. [2018], Romero et al. [2017a], the authors propose an online algorithm that can accommodate dynamic graphs (i.e. graphs for which the edge weights can change over time), although this is only possible for a special class of kernel which have a tri-diagonal inverse. 

Recently, some methods have also been proposed for distributed reconstruction of time-varying graph signals. In Chi et al. [2022], as well as [Zhou et al., 2022a], the authors propose distributed algorithms that draw upon the work of Qiu et al. [2017] using the temporal difference operator. In these two papers, which have similar goals but were developed separately, the authors use a modified Newton method to solve the optimisation problem, by making use of an approximation to the Hessian. 

In general, there is certainly scope for extensions to the literature on graph signal reconstruction. For example, there are open questions on the best way to address GSR for directed graphs, multilayer graphs and signals where the graph must be learned simultaneously. In particular, we would like to highlight that multidimensional graph signals have only been addressed in the context of time-varying signals. To the best of our knowledge, reconstruction on general Cartesian product and multiway graphs has not been addressed. 

## **2.4 Graph Signal Regression** 

Another key topic that runs through this thesis is graph signal regression. One of the earliest papers to reference regression in the context of GSP is Guestrin et al. [2004]. Here, the authors propose a distributed algorithm for computing a function that approximates a time-varying graph signal, with applications aimed specifically at sensor networks. This paper, which predates much of the work on Laplacian-based GSP, is primarily focused on efficient algorithms for communication between sensors, and in modern parlance is more akin to graph signal compression, as the authors seek a low-dimensional representation of the original signal. It can also be considered a particular class of distributed spatial regression, as they consider the _x_ - _y_ coordinates of each sensor, rather than modelling the network in terms of nodes and edges. 

In this thesis, the definition of graph signal regression we use differs somewhat from this formulation. For our purposes, we consider graph signal regression to be the task of estimating a graph signal as a function of additional explanatory variables. In particular, we highlight two different scenarios which we term exogenous (global) and endogenous (local) regression. For 

Chapter 2. _Literature Review, Contributions and Scope_ 

23 

the exogenous case, we examine work on Kernel Graph Regression (KGR) [Venkitaraman et al., 2019] and related variants such as Gaussian Process on Graphs (GPoG) Venkitaraman et al. [2020]. For the endogenous case, we examine work on Regression with Network Cohesion (RNC) [Li et al., 2019]. 

## **2.4.1 Exogenous case: Kernel Graph Regression and Gaussian Processes on Graphs** 

The task of graph regression with endogenous explanatory variables can be stated as follows. Consider a series of _T_ real-valued graph signals, each measured on a graph comprising _N_ nodes, _{_ **y** _t ∈_ R _[N] }[T] t_ =1[.][Each of these signals has a corresponding associated length-] _[M]_[vector of explana-] tory variables _{_ **x** _t ∈_ R _[M] }[T] t_ =1[.][The goal is to learn a function that maps the explanatory variables] to the graph signals, such that if a new explanatory vector **x** _[′]_ is supplied, we should be able to estimate the corresponding graph signal **y** _[′]_ . By penalising predictions that are not smooth with respect to the topology of the graph, the intention is to produce an estimator that outperforms non-graph-aware alternatives. Note that, while we use the index _t_ to denote each sample, the set _{_ **x** _t,_ **y** _t}_ can simply be regarded as training pairs and need not represent time-series data (although they often may). 

In this context, the variables are ‘exogenous’ or global in the sense that they are not associated with any node in particular, and the signal at each node in the graph can learn a unique functional response. For example, consider a time-varying graph signal consisting of net profits for a network of businesses connected based on industry or supply chain. In this case, the explanatory variables could be factors in the broader economy such as GDP growth, inflation or unemployment which may affect each company differently. 

In Venkitaraman et al. [2019], the authors propose Kernel Graph Regression (KGR) for this purpose. Here, each node in the observed graph signal **y** _t_ is modelled as a unique linear combination of a basis function representation of the explanatory variables _**ϕ**_ ( **x** _t_ ) _∈_ R _[P]_ , such that **y** _t_ = **W** _[⊤]_ _**ϕ**_ ( **x** _t_ ), where **W** _∈_ R _[P][ ×][N]_ is a matrix of coefficients. To find the optimal value of **W** , they propose the following cost function. 

**==> picture [365 x 30] intentionally omitted <==**

The first term in this objective seeks to minimise the square prediction error, the second provides regularisation for the coefficient matrix, and the third utilises the total square variation, of eq. (1.2), to promote signal smoothness. Next, the authors leverage the so-called ‘kernel trick’ to transform this into a non-parametric regression problem. This is achieved by introducing a 

Chapter 2. _Literature Review, Contributions and Scope_ 

24 

_T × T_ kernel matrix **K** , where **K** _ij_ = _κ_ ( **x** _i,_ **x** _j_ ) [Rasmussen and Williams, 2005], which results in the following in-sample prediction. 

**==> picture [329 x 19] intentionally omitted <==**

where **Y** _∈_ R _[T][ ×][N]_ is the matrix formed by stacking each observed signals _{_ **y** _t}_ , vec ( _·_ ) represents column-major vectorisation mapping R _[T][ ×][N] �→_ R _[T N]_ , and mat ( _·_ ) is the reverse operation R _[T N] �→_ R _[T][ ×][N]_ . The result is the prediction made over the training samples _{_ **x** _t}[T] t_ =1[.][This][can][also][be] adjusted to make a prediction for an unseen explanatory variable **x** _[′]_ . Some recent extensions have been proposed to KGR such as Elias et al. [2022], where the authors use an algorithm based on random Fourier features to improve computational robustness. 

In Venkitaraman et al. [2020], the same authors propose a new model which takes a Bayesian perspective to define Gaussian Processes over Graphs (GPG). Here, a modified approach is used, where a graph-spectral prior is placed over the coefficient matrix to induce smoothness in the output signal. This results in not only a point estimate for the signal but a multivariate Gaussian probability distribution with a mean and covariance. In particular, the authors define an online algorithm where the distribution over a signal at time _T_ + 1, given **x** _T_ +1 is given by 

**==> picture [310 x 14] intentionally omitted <==**

with 

**==> picture [335 x 37] intentionally omitted <==**

**==> picture [327 x 13] intentionally omitted <==**

Several papers have also proposed extensions to this model. For example, in Miao et al. [2022], the authors present a modified algorithm that simultaneously learns the underlying graph structure. In Zhi et al. [2023], the authors propose parametrising the filter function as a finite polynomial of the graph Laplacian, and simultaneously learn the polynomial coefficients, extending their earlier work in Pu et al. [2021]. 

In chapter 4, we present a hybrid model that incorporates aspects of graph signal reconstruction, as well as Gaussian processes over graphs. In particular, we are interested in reconstructing timevarying partially observed graph signals when additional exogenous explanatory variables exist. 

Chapter 2. _Literature Review, Contributions and Scope_ 

25 

Notably, all the models discussed in this subsection assume that readings across all vertices are available as inputs into the model. However, in many real-world applications, node-level data may be corrupted by equipment failure or difficult/expensive to reliably collect. Whilst one option may be to simply remove problematic nodes from the problem entirely, this can waste valuable data that may help in the estimation problem. In chapter 5, we take this further by developing a model that is capable of reconstructing _d_ -dimensional multiway graph signals with exogenous variables. To the best of our knowledge, none of these issues have been addressed in the available literature. 

## **2.4.2 Endogenous case: Regression with Network Cohesion** 

The second graph regression setting we wish to highlight is the case when endogenous variables exist to aid with the estimation process. Consider a single graph signal **y** _∈_ R _[N]_ , with elements existing on the nodes of a known graph. In this scenario, each node, _n_ , has an associated vector of explanatory variables **x** _n ∈_ R _[M]_ . The goal is to build a predictive model which utilises these local explanatory variables, whilst also incorporating the underlying structure of the network. 

In Li et al. [2019], the authors propose Regression with Network Cohesion (RNC). Here, they propose modelling each element of the observed graph signal **y** _n_ as a linear combination of an intercept term and the explanatory variables at node _n_ . This is summarised by the following statistical model. 

**==> picture [244 x 11] intentionally omitted <==**

**X** _∈_ R _[N][×][M]_ is the matrix formed by stacking each vector of explanatory variables, **w** _∈_ R _[M]_ is a coefficient vector, and **c** _∈_ R _[N]_ is a flexible intercept term of individual node effects. The model error _**ε** ∈_ R _[N]_ is assumed to have a zero mean and a variance of _σ_[2] **I** _N_ . The model seeks to learn an optimal value for **c** and **w** by minimising the following objective function. 

**==> picture [291 x 12] intentionally omitted <==**

The addition of the total square variation term, which the authors name the cohesion penalty, is intended to promote smoothness over the flexible intercept with respect to the topology of the graph. The justification for this is that closely connected nodes are likely to have similar baseline effects, meaning the model simultaneously learns a shared coefficient vector **w** , and a unique but smooth intercept. The optimal values can be computed by introducing a combined parameter vector _**θ**_ =  , with an estimator given by **w**  **[c]**  

Chapter 2. _Literature Review, Contributions and Scope_ 

26 

**==> picture [285 x 39] intentionally omitted <==**

It is worth highlighting that the RNC model places the graph-cohesion penalty on the intercept term **c** only, and not the overall prediction **Xw** + **c** . This separation into a smooth term **c** and a potentially non-smooth term **Xw** is an interesting choice, which does not necessarily guarantee a smooth prediction. One could instead propose a model of the form 

**==> picture [306 x 12] intentionally omitted <==**

in which case the optimal value of the parameter vector _**θ**_ would be given by 

**==> picture [321 x 39] intentionally omitted <==**

This topic was not addressed in the original paper; however, it presents an interesting direction for future research. Comparing the predictive performance of these two models using real-world datasets could be particularly valuable. 

To make a prediction on the test set, where the new explanatory variables **X** _[′] ∈_ R _[N][ ′][×][M]_ are available, the authors use the following. 

**==> picture [240 x 11] intentionally omitted <==**

where **w** ˆ is the optimal value found by minimising eq. (2.18), and **c** ˆ _[′]_ is found by minimising the following objective. 

**==> picture [323 x 39] intentionally omitted <==**

where the new Laplacian characterising the full graph containing all train and test nodes has been broken into blocks as shown. Note that as long as the two parts of the graph are mutually connected, the inverse of **L** 22 will exist. As noted by the authors, there may be some issues surrounding computational robustness within this model. In particular, the system matrix found in eq. (2.21) may in general be singular. To overcome this the authors propose adding a small term _γ_ **I** _N_ to the graph Laplacian, which fixes this issue. 

Chapter 2. _Literature Review, Contributions and Scope_ 

27 

**==> picture [78 x 184] intentionally omitted <==**

**----- Start of picture text -----**<br>
G 3<br>G 1<br>G 2<br>**----- End of picture text -----**<br>


Figure 2.3: Graphical depiction of an order-3 tensor signal with graphs underlying each axis. 

One limitation of the RNC model is that the total square variation penalty, while simple and easy to interpret, lacks the flexibility to specify more generic expectations about the spectral profile of the observed graph signal. Furthermore, the authors only consider a single measurement across the graph, without extending this to time-varying or general multivariate graph signals. 

## **2.5 Multiway Graph Signal Processing** 

Multiway Graph Signal Processing (MWGSP) is an emerging subfield that extends Graph Signal Processing to analyse data represented by multidimensional arrays and tensors [Stanley et al., 2020]. In most standard GSP applications, a signal is represented by a vector **y** _∈_ R _[N]_ , which is interpreted as existing on the nodes of a single graph. MWGSP generalises this by considering tensor-valued signals _**Y** ∈_ R _[N]_[1] _[×][N]_[2] _[×][...][×][N][d]_ , where each axis is described by an independent graph, which are combined together via a _d_ -dimensional product. Many multidimensional models and algorithms from GSP and classical signal processing, such as the 2D DFT and Time-Vertex (TV) signals can be reinterpreted under the MWGSP framework, bringing additional insight and new applications. As a relatively new paradigm, there is yet to be a large pool of research on MWGSP. Whilst many authors have noted its potential applications [Li et al., 2023, Marques et al., 2020a], many models from GSP are yet to be discussed in the context of GSP. This leaves many opportunities for the development of theory in this area. 

It should be noted that MWGSP is related by distinct from multi-layer GSP [Zhang et al., 2023a]. This is also an emerging framework that uses the language of tensors to describe higher-order graph structures. However, in multi-layer GSP, the focus is on multiple layers of heterogeneous graphs, each with possibly different structures and physical meanings, that connect to each other 

Chapter 2. _Literature Review, Contributions and Scope_ 

28 

in more general ways. For example, one layer could represent a network of cloud computing servers, and another could represent a power grid. Each layer may have different nodes with _intralayer_ edges, and the two layers may be connected via _interlayer_ edges. This is certainly a promising and interesting framework, but not the focus of this thesis. 

## **2.6 Node classification** 

The majority of models and algorithms discussed in this review thus far have primarily dealt with real-valued graph signals **y** _∈_ R _[N]_ . However, it is natural to generalise this to other forms of data, for example, binary signals **y** _∈{_ 0 _,_ 1 _}[N]_ representing two distinct classes, or signals on the interval **y** _∈_ [0 _,_ 1] _[N]_ which could represent probabilities. Moreover, this can easily be extended to categorical data, where each node belongs to one of _C_ classes, with a corresponding simplex representing their respective probabilities. Signals with these characteristics can be employed to design node classification algorithms. 

The GFT operator is typically defined to act on real-valued graph signals, which has conventionally limited GSP models to this type of data. However, some studies have considered node classification tasks. For instance, in Sandryhaila and Moura [2013a], the authors utilise graph signals of the form **s** _∈{−_ 1 _,_ 0 _,_ +1 _}[N]_ to represent a binary classification task, with zero signifying an unknown label. Their proposed prediction for the true signal is the solution to the optimisation problem outlined as follows: 

**==> picture [311 x 20] intentionally omitted <==**

Here, **C** represents a diagonal matrix with **C** _nn_ = _|_ **s** _n|_ , and TVG( **y** ) is a graph shift total variation measure, imposing a smoothness assumption, given by 

**==> picture [283 x 28] intentionally omitted <==**

for a graph adjacency matrix **A** with maximum eigenvalue _λ_ max. The authors also compare this with a method utilising TV2 Laplacian-based regularisation, with the results favouring the former approach. One potential issue with this model is that the optimisation searches in the space of real-valued signals, which are subsequently interpreted as estimates for class probabilities. Although the _ϵ_ -condition ensures that the predictions do not deviate excessively from the observed classes, confined to the set _{−_ 1 _,_ 0 _,_ +1 _}_ , there is, in theory, nothing preventing the estimates from extending beyond this range, which may make results difficult to interpret. Furthermore, their total variation measure lacks the flexibility to encode more precise assumptions 

Chapter 2. _Literature Review, Contributions and Scope_ 

29 

about the spectral profile of the signal and is applied directly to a class probability vector, which is typically designed for real-valued signals only. This makes some aspects of their model difficult to interpret from a theoretical perspective. 

More recently, Tran et al. [2020] propose a method for binary node classification based on the so-called logistic network lasso. They consider the situation where each node also has an associated vector of explanatory variables **x** _n ∈_ R _[M]_ , and propose that the class probabilities can be estimated using a logistic function as follows. 

**==> picture [276 x 24] intentionally omitted <==**

This is similar in spirit to traditional logistic regression, except each node in the network also has its own unique coefficient vector **w** _n_ specifying the contribution of the local explanatory variables to the respective probability. Evidently, in isolation, the optimal setting for each **w** _n_ is underdetermined. To complete this model, they introduce a cost function that includes a standard logistic loss function accompanied by a total variation penalty, defined as follows: 

**==> picture [268 x 23] intentionally omitted <==**

This objective is then minimised using a primal-dual method with proximal splitting. The outcome is that node clusters are encouraged to share the same coefficient vectors, with the L1 norm promoting exact matches for closely connected nodes, as opposed to the smooth variation that a quadratic penalty would induce. The concept of using a logistic function to map real numbers to the interval [0 _,_ 1] is an interesting suggestion since the real-valued coefficient vectors can then be penalised in the vertex domain, which is more consistent from a GSP perspective. Their application of a Lasso penalty term also exhibits interesting properties and bears some similarity to trend filtering on graphs [Wang et al., 2016]. 

Node classification has also been addressed in the machine learning community, typically under the framework of semi-supervised learning. For example, in Belkin and Niyogi [2002], the authors effectively introduce an early bandlimited model for binary graph signal reconstruction, although it predates many of the modern GSP concepts. Here, they consider reconstructing a binary signal **y** _∈{−_ 1 _,_ 1 _}[N]_ by finding a linear combination of the first _K_ eigenvectors of the graph Laplacian. In particular, denoting **U** _K ∈_ R _[N][×][K]_ as the rectangular matrix containing the first _K_ eigenvectors, they seek a vector **a** that minimises the following objective. 

**==> picture [91 x 13] intentionally omitted <==**

(2.28) 

Chapter 2. _Literature Review, Contributions and Scope_ 

30 

This is simply a standard least squares problem with a solution given by 

**==> picture [255 x 12] intentionally omitted <==**

Their prediction for the unknown class labels is then determined based on whether the corresponding element of **U** _k_ **a** is greater than or less than zero. While the paper shows promising results on a dataset of handwritten digits, it suffers from some of the same difficulties in terms of interpretability as Sandryhaila and Moura [2013a]. In particular, the prediction **U** _k_ **a** is an unbounded, real-valued estimator to a binary input signal. Furthermore, unlike the output of the model proposed in Tran et al. [2020], the predicted signal cannot be interpreted in probabilistic terms. 

## **2.7 Related topics** 

For the sake of clarity, in this section, we give a high-level overview of two important topics within GSP which are adjacent to the work in this thesis, but not directly relevant to the core subject matter. While not addressed directly in this thesis, these topics offer potentially useful avenues for the extension of our work. 

## **2.7.1 Graph learning** 

When GSP was originally formulated, the graph of interest was typically assumed to be known a priori, with the subsequent methods following from the existence of this basic structure. In real-world applications, this can often be the case, for example, in a social, transport or citation network it is clear how objects should be connected given the nature of the problem. In other applications, for example in a protein-protein interactome, domain-specific knowledge can be incorporated in a principled way to construct a graph [Li et al., 2023]. In others, such as a sensor network, _k_ -nearest neighbour, _ε_ -ball, or permuted minimum spanning tree techniques can be used to construct a reasonable graph [Qiao et al., 2018]. 

However, in other circumstances, it may not be so clear how to derive or construct a graph, and instead, one must be learned from the data. An example of this may be the stock price returns of a network of companies. While it may be possible to construct a graph using information such as industry, supply chain, or strategic alliance [Cheng and Li, 2021, Gao et al., 2021], this information may be difficult to gather or otherwise unavailable. Another approach would be simply to learn a graph directly from the returns data. In general, the graph learning problem can be formulated as, given a set of graph signals _{_ **y** _t ∈_ R _[N] }[T] t_ =1[,][find][an][appropriate][sparse] 

Chapter 2. _Literature Review, Contributions and Scope_ 

31 

_N × N_ adjacency matrix [Dong et al., 2019]. From the perspective of GSP, it is assumed that these observations are generated from some network process, operating on a latent underlying graph structure. 

One of the oldest and simplest approaches, predating work on GSP, is so-called correlation networks. Here, a graph can be constructed by considering the pairwise correlation between the signal at nodes _i_ and _j_ . For example, one approach is to set **A** _ij_ = 1 if _ρij >_ 0 and zero otherwise [Mateos et al., 2019]. While such approaches are simple and have an intuitive notion of pairwise interaction, correlations may be due to latent network effects rather than direct pairwise influence. For example, two nodes may be interacting via a third node _k_ , in which case it is more prudent to set **A** _ik_ = **A** _jk_ = 1, and **A** _ij_ = 0. While there are techniques to overcome such confounding variables (see, Kolaczyk [2009], section 7), in general, this can be problematic from the perspective of graph learning. 

An alternative prominent technique is the Graphical Lasso (GL) [Friedman et al., 2007]. The GL is a sparse penalised maximum likelihood estimator for the precision matrix **P** (the inverse of the covariance matrix **Σ** ) of a multivariate Gaussian random variable. The estimated value of **P** is given by 

**==> picture [317 x 37] intentionally omitted <==**

where **Σ**[ˆ] is the sample covariance, with the L1 norm promoting sparsity in **P** . The graph Laplacian is then derived by assuming **P** is a regularised version of **L** [Lake and Tenenbaum, 2010]. 

Other approaches favour more GSP-oriented estimation models by incorporating signal smoothness assumptions. For example, in Hu et al. [2015], the authors propose learning the Laplacian matrix directly by solving the following optimisation problem. 

**==> picture [303 x 34] intentionally omitted <==**

where **Y** _∈_ R _[N][×][T]_ is the matrix obtained by stacking each observed graph signal **y** _t_ . This was modified slightly in Dong et al. [2016] by introducing a new matrix **X** , of the same dimensions as **Y** , meant to be a smooth approximation of **Y** . Their optimisation objective was then given by 

Chapter 2. _Literature Review, Contributions and Scope_ 

32 

**==> picture [327 x 34] intentionally omitted <==**

A more computationally efficient approach was proposed in Kalofolias [2016], but using the adjacency matrix rather than the Laplacian. There has been a substantial amount of additional work on graph learning from a GSP perspective. For a detailed review, see Dong et al. [2019], Mateos et al. [2019]. 

## **2.7.2 GSP on directed graphs** 

The work presented in this thesis, and indeed the majority of published literature on GSP, is focused on undirected graphs. The benefit of this framework is that the undirected graph Laplacian naturally gives rise to a simple definition of signal smoothness. It is also a well-behaved Hermitian operator, with real eigenvalues and orthonormal eigenvectors that serve as a wellmotivated and coherent Fourier basis [Ortega et al., 2018]. However, there is also rich literature regarding GSP for directed graphs (or digraphs) [Marques et al., 2020b]. Directed graphs, while less commonly found in GSP, are more suitable for modelling certain applications such as web links, citation networks, trade flows and follower-model social networks, since they can accommodate both incoming and outgoing edges. However, extending the Graph Fourier Transform framework to signals on digraphs is less straightforward and several alternative proposals exist. 

One originates from some of the earliest work on GSP from Sandryhaila and Moura, where the GFT for a general directed graph is constructed from the total variation of a graph signal **y** defined as follows. 

**==> picture [266 x 11] intentionally omitted <==**

where **A**[norm] is the adjacency matrix (or, more generally, any graph shift operator) divided by its spectral radius to ensure that the transformed signal is appropriately scaled for comparison with the original signal [Sandryhaila and Moura, 2013c]. A Fourier basis _{_ **u** _i}_ is then defined by first taking an eigendecomposition of the adjacency matrix, and then ordering the eigenvectors according to their total variation. Where the adjacency matrix is non-diagonalisable, one can instead resort to the generalised eigenvectors using Jordan decomposition. 

While this definition is attractive from a theoretical standpoint, it suffers from several drawbacks. In general, the eigenvectors are complex-valued and may be more difficult to interpret, for example, constant signals no longer have zero variation. Furthermore, the eigenvectors are 

Chapter 2. _Literature Review, Contributions and Scope_ 

33 

typically non-orthonormal, meaning Parseval’s identity no longer holds and signal power is not preserved when transforming between the vertex and spectral domains. Other work has attempted to overcome these limitations by proposing a new definition of variation on directed graphs. In Sardellitti et al. [2017], the authors define the Graph Directed Variation (GDV) as follows. 

**==> picture [271 x 31] intentionally omitted <==**

where [ **y** _i −_ **y** _j_ ]+ = max( **y** _i −_ **y** _j,_ 0). The search for the GFT basis is then given by the optimisation problem of finding the set of orthonormal vectors that subsequently minimise the GDV subject to perpendicularity with all those preceding. Under this framework, smooth signals on digraphs represent a flow from a smaller value to a larger one over a directed edge. Hence, the signal at two nodes _i_ and _j_ is only penalised if **y** _i >_ **y** _j_ . For example, if there were a set of temperature sensors over a mountain range, a directed graph would connect stations based on elevation since readings at higher altitudes are expected to be lower. 

A similar strategy was used in Shafipour et al. [2019], where the variation was defined as follows. 

**==> picture [274 x 31] intentionally omitted <==**

To generate a Fourier basis that is roughly evenly spread with respect to the variation measure, these authors proposed solving the following optimisation objective. 

**==> picture [323 x 58] intentionally omitted <==**

These approaches, whilst offering a simple and meaningful definition of directed variation are potentially limited in their applicability, since the underlying assumption that a graph signal should flow from lower to higher values over directed edges may not be suitable for all scenarios. It also implies that any signal that monotonically increases over the direction of the network has the same variation, namely zero. Furthermore, there is a significant additional computation cost to solving these optimisation problems that makes scaling to large graphs difficult. 

One other interesting and novel proposal for the GFT of a directed graph is to use the so-called “magnetic Laplacian” [DeResende and Costa, 2020, Zhang et al., 2021]. The magnetic Laplacian 

Chapter 2. _Literature Review, Contributions and Scope_ 

34 

is a complex-valued Hermitian matrix which generalises the standard undirected Laplacian for directed graphs and is defined as follows. 

**==> picture [249 x 11] intentionally omitted <==**

Here, **D** is the diagonal degree matrix defined as **D** _ii_ =[�] _j_ **[A]** _[ij]_[,] **[A]** _[S]_[is][the][symmetric][adjacency] matrix, defined as **A** _S_ =[1] 2[(] **[A]**[ +] **[ A]** _[⊤]_[),][and] **[Γ]**[is][a][Hermitian][matrix][given][by] 

**==> picture [265 x 14] intentionally omitted <==**

Here, i is the imaginary unit and _q_ is a parameter known as the _charge_ . The exponentiation is element-wise. Each element **Γ** _ij_ represents a complex phase, where the angle is proportional to the net outflow between nodes _i_ and _j_ . The effect is that **L** _M_ is a Hermitian matrix that captures both the magnitude and the direction of the edges at each node. This operator arises in quantum mechanics to describe the Hamiltonian of a charged particle on a graph subject to the action of a magnetic field [Shubin, 1994]. Note that, for an undirected graph, the magnetic Laplacian reduces to the standard Laplacian. 

As a complex Hermitian operator, **L** _M_ has eigenvectors given by unitary matrix **U** , and realvalued eigenvalues. 

**==> picture [238 x 12] intentionally omitted <==**

where **U** _[†]_ is the Hermitian adjoint of **U** . Therefore, the GFT of a signal **y** is given by **U** _[†]_ **y** and the IGFT by **Uy** . This elegant formulation maintains many of the desirable properties of the undirected GFT, such as power preservation. Early results indicate that the magnetic Laplacian may be effective in tasks such as community detection and denoising on directed graphs [Fanuel et al., 2017, Furutani et al., 2020]. However, some uncertainty remains on how to interpret the complex-valued signals after transformations via the GFT and IGFT. In Furutani et al. [2020], the authors opt to take the real part of the signal only, however, best practices have not yet been established. 

In general, spectral methods on directed graphs present a number of additional challenges and there is no clear front-runner for how to handle them. For this reason, as well as the additional computational challenges associated with many of the methods, the authors of Marques et al. [2020b] suggest that node-domain algorithms may generally be preferable when it comes to directed graphs. 

Chapter 2. _Literature Review, Contributions and Scope_ 

35 

## **2.8 Opportunities for extension** 

In this thesis, we focus on multivariate graph signals, that is signals that can be described by matrices or, more generally, _d_ -dimensional tensors. Two-dimensional reconstruction and regression models have been primarily considered in the context of Time-Vertex problems [Ioannidis et al., 2016, Qiu et al., 2017, Venkitaraman et al., 2019]. As such, one of our initial objectives is to revisit these problems from the perspective of generic two-dimensional Cartesian product graphs, of which many T-V models can be seen as a subset. We also note that, although T-V graph filters have been analysed in some depth, there has not, to the best of our knowledge, been detailed work on flexible two-dimensional graph filters and GRFs. 

Research on tensor-valued graph signal models on _d_ -dimensional Cartesian product graphs is relatively sparse. While there has been some recent progress in the field of multi-layer graph signal processing [Zhang et al., 2023a], MWGSP seems to have received less attention [Stanley et al., 2020]. We believe there is a significant opportunity for the development of novel models in this area, with numerous potential applications. This is especially relevant in the big data era, with large-scale datasets often characterised by complex multi-way dependencies. 

We also note that there have been relatively few GSP models developed for binary and multiclass graph signals. While node classification tasks have been considered in early work on semisupervised learning [Belkin and Niyogi, 2002], and the realm of graph neural networks [Xiao et al., 2021a], we believe there is an opportunity to develop statistical regression and reconstruction problems for categorical graph signals that harness some of the more recent developments in GSP. 

Many multivariate graph regression and reconstruction problems could also benefit from simultaneous graph, or graph filter parameter, learning. While there is interesting ongoing work in this area, such as [Zhi et al., 2023], in this thesis we do not address questions of this nature. Finally, we also note that there is also significant scope for improvement of GSP models on directed graphs. Again, while interesting work is ongoing, we do not address this topic in this thesis. 

## **Chapter 3** 

## **Signal Reconstruction on Cartesian Product Graphs** 

In this chapter, we address the topic of signal reconstruction over general two-dimensional Cartesian product graphs, where an arbitrary set of signal elements is missing. The first key objective is to present a novel Bayesian model for this purpose, based on our formulation of multivariate graph filters, where a smooth underlying signal must be inferred given a noisy partial observation. The second is to produce two scalable iterative algorithms for computing the posterior mean and investigate their respective convergence properties both theoretically and empirically. 

As discussed in section 2.3, Graph Signal Reconstruction (GSR) is a topic that has received substantial attention in the last decade. Whilst the majority of past models have focused on the reconstruction of a single one-dimensional signal, with some recent models extending this to time-varying signals, our approach can be seen as a natural generalisation that encompasses two-dimensional matrix signals with arbitrary undirected graphs underlying each axis. Furthermore, we believe our Bayesian approach can offer new insight into multivariate correlation structure over irregular topologies. Since efficient computation is a critical factor in real-world applications of GSR, we devote substantial attention to a careful analysis of computational complexity. In doing so, we show how the two iterative algorithms we present possess different convergence behaviour and implementation details, making the optimal choice dependent on the hyperparameters, data composition, and graph sparsity. 

We begin in section 3.1 by reviewing the concept of a graph product, explaining our rationale for focusing on the Cartesian product in particular, and introducing our model for two-dimensional anisotropic filters. In section 3.2, we present our statistical model for graph signal reconstruction on a Cartesian product graph and derive the two algorithms for solving the posterior mean. These 

36 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

37 

encompass a Stationary Iterative Method (SIM) based on matrix splitting and a Conjugate Gradient Method (CGM) using a graph-spectral preconditioner. In addition, we show how the SIM can be implemented using Chebyshev polynomials to avoid Laplacian eigendecomposition. To end this section, we demonstrate the utility of these models using a dataset comprising daily SARS-CoV-19 case rates across the UK. Finally, in section 3.3, we engage in an in-depth analysis of the convergence properties of each method and propose practical guidelines for method selection. 

## **3.1 Graph Products** 

In this chapter, we will be primarily concerned with signal processing on _Cartesian product graphs_ . This special class of graph finds applications in numerous areas, such as video, hyperspectral image processing and network time series problems. However, the Cartesian product is not the only way to consistently define a product between two graphs. In this section, we formally introduce the concept of a graph product, examine several prominent examples, and explain why we choose to look specifically at the Cartesian graph product. 

## **3.1.1 Basic definitions** 

In the general case, consider two undirected graphs _GA_ = ( _VA, EA_ ) and _GB_ = ( _VB, EB_ ) with vertex sets given by _VA_ = _{a ∈_ N _| a ≤ NA}_ and _VB_ = _{b ∈_ N _| b ≤ NB}_ respectively. (In this context we do not regard zero to be an element of the natural numbers, with node indices beginning from zero). A new graph _G_ can be constructed by taking the product between _GA_ and _GB_ . In its most general form, this can be written as follows. 

**==> picture [258 x 11] intentionally omitted <==**

For all common definitions of a graph product _⋄_ , the resultant graph _G_ has a vertex set _V_ given by the Cartesian product of the vertex sets of the corresponding factor graphs, that is 

**==> picture [319 x 12] intentionally omitted <==**

Typically, vertices are arranged in lexicographic order, in the sense that ( _a, b_ ) _≤_ ( _a[′] , b[′]_ ) iff _a < a[′]_ or ( _a_ = _a[′]_ and _b ≤ b[′]_ ) [Harzheim, 2005]. To define a product, one must specify a consistent rule for constructing the new edge set _E_ from the factor edge sets _EA_ and _EB_ . In general, there are 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

38 

eight possible conditions for deciding whether two nodes ( _a, b_ ) and ( _a[′] , b[′]_ ) are to be connected in the new graph. 

|1.|[_a, _|_a′_]_∈EA_|and|_b_=_b′_|
|---|---|---|---|---|
|2.|[_a, _|_a′_] _/∈EA_|and|_b_=_b′_|
|3.|[_a, _|_a′_]_∈EA_|and|[_b, b′_]_∈EB_|
|4.|[_a, _|_a′_] _/∈EA_|and|[_b, b′_]_∈EB_|
|5.|[_a, _|_a′_]_∈EA_|and|[_b, b′_] _/∈EB_|
|6.|[_a, _|_a′_] _/∈EA_|and|[_b, b′_] _/∈EB_|
|7.||_a_=_a′_|and|[_b, b′_]_∈EB_,|
|8.||_a_=_a′_|and|[_b, b′_] _/∈EB_|



Each definition of a graph product corresponds to the union of a specific subset of these conditions, thus, there exist 256 different types of graph product [Barik et al., 2015]. Of these, the Cartesian product (conditions 1 or 7), the direct product (condition 3), the strong product (conditions 1, 3 or 7) and the lexicographic product (conditions 1, 3, 5 or 7) are referred to as the standard products and are well-studied [Imrich and Klavˇzar, 2000]. A graphical depiction of the standard graph products is shown in figure 3.1. In each of these four cases, the adjacency and Laplacian matrices of the product graph can be described in terms of matrices relating to the factor graphs [Barik et al., 2018, Fiedler, 1973]. This is shown in table 3.1. 

Given these definitions, it may seem that all the standard graph products are non-commutative in the sense that **A** _A ⊕_ **A** _B_ = **A** _B ⊕_ **A** _A_ etc. However, the graphs _GA ⋄GB_ and _GB ⋄GA_ are in fact isomorphically identical in the case of the Cartesian, direct and strong products. This is not the case for the Lexicographic product [Imrich and Klavˇzar, 2000]. 

||Adjacency matrix|Laplacian|
|---|---|---|
|Cartesian|**A**_A ⊕_**A**_B_|**L**_A ⊕_**L**_B_|
|Direct|**A**_A ⊗_**A**_B_|**D**_A ⊗_**L**_B_ +**L**_A ⊗_**D**_B −_**L**_A ⊗_**L**_B_|
|Strong|**A**_A ⊗_**A**_B_ +**A**_A ⊕_**A**_B_|**D**_A ⊗_**L**_B_ +**L**_A ⊗_**D**_B −_**L**_A ⊗_**L**_B_ +**L**_A ⊕_**L**_B_|
|Lexicographic|**I**_A ⊗_**A**_B_ +**A**_A ⊗_**O**_A_|**I**_A ⊗_**L**_B_ +**L**_A ⊗_**O**_B_ +**D**_A ⊗_(_NB_**I**_B −_**O**_B_)|



Table 3.1: The adjacency and Laplacian matrices for the standard graph products. Here, **D** _A_ and **D** _B_ are the diagonal degree matrices, i.e **D** _A_ = diag ( **A** _A_ **1** ). **I** _A_ and **O** _A_ are the ( _NA × NA_ ) identity matrix and matrix of ones respectively. 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

39 

**==> picture [359 x 147] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cartesian product Direct product<br>® @ e ee ©<br>@ @<br>> o °® ‘2 *<br>@ GA GB a) .@ @ o rad\<br>@ @ @<br>e e (9) Strong product Lexicographic product<br>**----- End of picture text -----**<br>


Figure 3.1: A graphical depiction of the four standard graph products 

## **3.1.2 The spectral properties of products graphs** 

In the field of graph signal processing, we are often concerned with analysing the properties of graphs via eigendecomposition of the graph Laplacian [Mieghem, 2010]. In the case of product graphs, it is greatly preferable if we can fully describe the spectrum of _GA ⋄GB_ in terms of the spectra of _GA_ and _GB_ alone. This is because the direct decomposition of a dense **L** has time-complexity _O_ ( _NA_[3] _[N] B_[ 3][),][whereas][decomposition][of][the][factor][Laplacians][individually][has] complexity _O_ ( _NA_[3][+] _[ N] B_[ 3][).][As][the][graphs][under][consideration][become][medium][to][large,][this][fact] quickly makes direct decomposition of the product graph Laplacian intractable. However, in the general case, only the spectra of the Cartesian and lexicographic graph products can be described in this way [Barik et al., 2018]. In the case of the direct and strong product, it is possible to estimate the spectra without performing the full decomposition (see [Sayama, 2016]). However, in general, the full eigendecomposition of the product graph Laplacian can only be described in terms of the factor eigendecompositions when both factor graphs are regular. 

Consider the eigendecompositions of **L** _A_ and **L** _B_ . 

**==> picture [301 x 13] intentionally omitted <==**

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

40 

||||Eigenvalues||||Eigenvectors|
|---|---|---|---|---|---|---|---|
|Cartesian|||_λ_(_A_)<br>_a_<br>+_λ_(_B_)<br>_b_||||(**U**_A_)_a ⊗_(**U**_B_)_b_|
|Direct_⋆_||_rAλ_(_B_)<br>_b_|+_rBλ_(_A_)<br>_a_<br>_−λ_(_A_)<br>_a_||_λ_(_B_)<br>_b_||(**U**_A_)_a ⊗_(**U**_B_)_b_|
|Strong_⋆_|(1|+_rA_)_λ_(_B_)<br>_b_|+ (1 +_rB_)_λ_(_A_)<br>_a_|_−λ_(_A_)<br>_a_||_λ_(_B_)<br>_b_|(**U**_A_)_a ⊗_(**U**_B_)_b_|
|Lexicographic_†_|||_NBλ_(_A_)<br>_a_||||(**U**_A_)_a ⊗_**1**_B_|
|||_λ_(_B_)<br>_b_<br>+_NB_deg(_a_)|||||**e**_a ⊗_(**U**_B_)_b_|



Table 3.2: Eigendecomposition of the Laplacian of the standard graph products. Here, _a_ and _b_ are understood to run from 1 to _NA_ and 1 to _NB_ respectively. _⋆_ only for _rA_ and _rB_ -regular factor graphs. _†_ note that the _b_ runs from 2 to _NB_ in the lower row. 

where **U** _A_ and **U** _B_ are the respective orthonormal eigenvector matrices, and **Λ** _A_ and **Λ** _B_ are the diagonal eigenvalue matrices given by 

**==> picture [388 x 19] intentionally omitted <==**

Given these definitions, table 3.2 gives information about the spectral decomposition of the standard graph products. 

## **3.1.3 Signals and filters on Cartesian product graphs** 

While both the direct and strong products do find uses in certain applications (for example, see [Kaveh and Alinejad, 2011]), they are both less common and more challenging to work with in a graph signal processing context due to their spectral properties described in the previous subsection. In practice, being limited to regular factor graphs means the majority of practical GSP applications are ruled out. The lexicographic product does not share this drawback, however, it is also significantly less common than the Cartesian product in real-world applications. For this reason, in the following, we focus primarily on the Cartesian product. 

Given the spectral decomposition of the Cartesian graph product stated in table 3.2, we can write the Laplacian eigendecomposition in matrix form as follows. 

**==> picture [342 x 12] intentionally omitted <==**

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

41 

This motivates the following definitions for the Graph Fourier Transform (GFT) and its inverse (IGFT). Consider a signal defined over the nodes of a Cartesian product graph expressed as a matrix **Y** _∈_ R _[N][B][×][N][A]_ . We can perform the GFT as follows. 

**==> picture [318 x 14] intentionally omitted <==**

Correspondingly, we can define the IGFT acting on a matrix of spectral components **Z** _∈_ R _[N][B][×][N][A]_ as follows. 

**==> picture [317 x 14] intentionally omitted <==**

Product graph signals: representation and vectorisation 

It is natural to assume that signals defined on the nodes of a Cartesian product graph _GA_ □ _GB_ could be represented by matrices (order two tensors) of shape ( _NA × NB_ ). Since product graph operators, such as the Laplacian **L** _A ⊕_ **L** _B_ , act on vectors of length _NANB_ , we must define a consistent function to map matrix graph signals _∈_ R _[N][A][×][N][B]_ to vector graph signals _∈_ R _[N][A][N][B]_ . The standard mathematical operator for this purpose is the vec ( _·_ ) function, along with its reverse operator mat ( _·_ ). However, this is somewhat problematic since vec ( _·_ ) is defined to act in _column-major_ order, that is 

**==> picture [276 x 91] intentionally omitted <==**

**----- Start of picture text -----**<br>
Y<br>(1 , 1)<br>Y (1 , 1) Y (1 , 2) . . . Y (1 ,NB )  <br>  Y<br>  (2 , 1)<br> Y (2 , 1) Y (2 , 2) . . . Y (2 ,NB ) <br>vec   = ...<br> ... ... ... ... <br> <br>Y ( NA− 1 ,NB )<br> Y ( NA, 1) Y ( NA, 2) . . . Y ( NA,NB )<br> Y ( NA,NB ) <br>**----- End of picture text -----**<br>


As is visible, this does not result in a lexicographic ordering of the matrix elements when the graph signal has shape ( _NA × NB_ ). Therefore, to avoid this issue and to be consistent with standard mathematical notation, we will assume that graph signals are represented by matrices of shape ( _NB × NA_ ) when considering the product between two graphs _GA_ □ _GB_ . For graph signals of this shape, the first index represents traversal of the nodes in _GB_ , and the second index represents traversal of the nodes in _GA_ . This ensures that matrix elements are correctly mapped to vector elements when using the column-major vec ( _·_ ) function. 

Given these definitions, we can define a spectral operator (usually a low-pass filter) **H** which acts on graph signals according to a spectral scaling function _g_ ( _λ_ ; _β_ ) such as one of those defined in table 2.1. As with regular non-product graphs, the action of this operator can be understood as 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

42 

first transforming a signal into the Laplacian frequency domain via the GFT, then scaling the spectral components according to some function, and finally transforming back into the vertex domain via the IGFT. 

**==> picture [305 x 74] intentionally omitted <==**

The matrix **G** _∈_ R _[N][B][×][N][A]_ , which we refer to as the spectral scaling matrix, holds the value of the scaling function applied to the sum of pairs of eigenvalues, such that 

**==> picture [263 x 19] intentionally omitted <==**

We observe that defining the filtering operation in this manner implies that the intensity is equal across both _GA_ and _GB_ . We refer to filters of this type as _isotropic_ . This can be further generalised by considering an _anisotropic_ graph filter, which offers independent control over the filter intensity in each of the two dimensions. In this case, we define **G** as follows. 

**==> picture [269 x 19] intentionally omitted <==**

where now _g_ is chosen to be an anisotropic graph filter such as one of those listed in table 3.3. Note that the original parameter _β_ is now replaced by two parameters _βa_ and _βa_ which offer independent control over the filter intensity in each dimension. In order for the definition of a 2D anisotropic filter to remain consistent with the underlying Cartesian product graph, we note that all filters we list are given by a function of a weighted sum of each Laplacian eigenvalue. Other more general functions of _λ_[(] _a[A]_[)] and _λ_[(] _b[B]_[)] will also result in operators that commute with the Laplacian but cannot be consistently considered graph spectral operators on the Cartesian product graph. 

Similarly defined two-dimensional filters have appeared in image processing literature [Aubert and Kornprobst, 2006], however, their use in graph signal processing so far has been limited to time-varying graph signal models. In Romero et al. [2017a], the authors propose ‘space-time kernels’, and in Grassi et al. [2018], Isufi et al. [2017], Jiang et al. [2021], Loukas and Foucard [2016], the authors discuss joint time-vertex filters. These models can essentially be understood 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

43 

|**Filter**||_g_(_λa, λb_; _βa, βb_)|
|---|---|---|
|1-hop random walk||(1 +_βaλa_+_βbλb_)_−_1|
|Difusion||exp(_−βaλa −βbλb_)|
|ReLu|max(1_−βaλa −βbλb,_0)||
|Sigmoid|2<br>�|1 + exp(_βaλa_+_βbλb_)<br>�_−_1|
|Gaussian|exp<br>�<br>_−_(_βaλa_+_βbλb_)2�||
|Bandlimited|1_,_|if_βaλa_+_βbλb ≤_1 else 0|



Table 3.3: Anisotropic graph filter functions in two dimensions 

as operating on a two-dimensional Cartesian product graph when one of the graphs takes the form of a path or a cycle graph, which gives rise to the standard Discrete Fourier Transform (DFT) in the time dimension. However, to the best of our knowledge, no one has addressed filters applicable to general two-dimensional Cartesian product graphs. Figure 3.2 depicts an anisotropic graph filter applied to a Cartesian product graph constructed from a 4-node line graph and a generic 10-node. 

## **3.2 Graph Signal Reconstruction on Cartesian Product Graphs** 

We now turn our attention to the task of signal reconstruction on Cartesian product graphs. In the following, we will replace the factor graph labels _A_ and _B_ with _T_ and _N_ respectively. The reason for this is that one application of particular interest is graph time-series problems, where we seek to model a network of _N_ nodes across a series of _T_ discrete time points. These so-called “time-vertex” (T-V) problems have garnered significant interest recently in the context of GSP [Grassi et al., 2018, Isufi et al., 2017, Loukas and Foucard, 2016]. T-V signals can be understood as existing on the nodes of a Cartesian product graph _GT_ □ _GN_ . In particular, we can conceptualise _T_ repeated measurements of a signal defined across the nodes of a _N_ -node graph as a single measurement of a signal defined on the nodes of _GT_ □ _GN_ , where _GT_ is a simple path graph. In the following subsection, we begin the main contributions of this chapter. 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

44 

**==> picture [326 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br>
βT = 0 . 01 βT = 1<br>βT<br>βN = 0 . 01<br>βN<br>βN = 1<br>**----- End of picture text -----**<br>


Figure 3.2: A visual representation of an anisotropic filter applied to a signal on a Cartesian product graph. In the top left, the filter intensity is low in both dimensions resulting in a signal with no particular correlation. In the top right, the filter intensity is strong in the _T_ dimension, resulting in a longitudinally smoother signal with little cross-sectional correlation. In the lower left, the filter is strong in the _N_ dimension, resulting in smooth cross-sections with little correlation longitudinally. In the lower right, the filter is strong in both dimensions, resulting in a signal that is smooth both cross-sectionally and longitudinally. 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

45 

## On the Laplacian spectrum of the path graph 

When considering time-vertex problems with uniformly spaced time intervals, _GT_ will be described by a path graph with equal weights on each edge. This special case of a graph has vertices given by _VT_ = _{t ∈_ N _| t ≤ T }_ and edges given by _ET_ = _{_ [ _t, t_ + 1] _| t < T }_ . The Laplacian matrix of the path graph is therefore given by 

**==> picture [144 x 91] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 − 1<br> <br>− 1 2 − 1<br>L T = ...<br>− 1 2 − 1<br>− 1 1<br> <br>**----- End of picture text -----**<br>


The eigenvalues and eigenvectors of this Laplacian are well-known and can be expressed in closed-form [Jiang, 2012]. In particular, 

**==> picture [116 x 21] intentionally omitted <==**

and 

**==> picture [136 x 21] intentionally omitted <==**

where the columns of **U** are appropriately normalised such that the magnitude of each eigenvector is one. Furthermore, this implies that the graph Fourier transform of a signal **y** _∈_ R _[T]_ is given by the orthogonal type-II Discrete Cosine Transform (DCT) [Ahmed et al., 1974]. This is of significance, as it means we can leverage Fast Cosine Transform (FCT) algorithms [Makhoul, 1980] which operate in a similar manner to the well-known Fast Fourier Transform (FFT) [Cooley and Tukey, 1965]. See chapter 4 of Rao and Yip [1990] for an overview of FCT algorithms. In general, FFT-type algorithms are challenging to derive for the GFT [LeMagoarou and Gribonval, 2016], however, this is a simple case where it can be achieved. 

In particular, this reduces both of the following procedures 

**==> picture [181 x 13] intentionally omitted <==**

from _O_ ( _T_[2] ) operations to _O_ ( _T_ log _T_ ) operations, which can be significant for large timeseries problems. 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

46 

## **3.2.1 Problem statement** 

The goal of Graph Signal Reconstruction (GSR) is to estimate the value of a partially observed graph signal at nodes where no data was collected. In the context of GSR on a Cartesian product graph, the available data is a partially observed signal **Y** _∈_ R _[N][×][T]_ where only an arbitrary subset _S_ = _{_ ( _n_ 1 _, t_ 1) _,_ ( _n_ 2 _, t_ 2) _, . . . }_ of the signal elements were recorded. By default, all other missing elements of **Y** are set to zero. To track which elements were missing from **Y** , we also define **S** _∈{_ 0 _,_ 1 _}[N][×][T]_ , which is referred to as the binary sensing matrix. It has entries given by 

**==> picture [261 x 43] intentionally omitted <==**

As such, the data available for input into the GSR problem is as follows. 

**==> picture [270 x 19] intentionally omitted <==**

Our model is based on the assumption that **Y** is a noisy partial observation of an underlying signal **F** _∈_ R _[N][×][T]_ , which is assumed to be smooth with respect to the graph topology[1] . Specifically, we assume that the observed matrix **Y** is generated according to the following statistical model. 

**==> picture [246 x 13] intentionally omitted <==**

The matrix **E** represents the model error and is assumed, without loss of generality, to have an independent normal distribution with unit variance which can be achieved by standardising **Y** appropriately. Therefore, the probability distribution of **Y** given the latent signal **F** is 

**==> picture [307 x 19] intentionally omitted <==**

Note that the covariance matrix diag (vec ( **S** )) is semi-positive definite by construction. This naturally reflects the constraint that some elements of **Y** are zero with probability 1. 

In order to estimate the latent signal **F** , we must provide a prior distribution describing our belief about its likely profile ahead of time. In general, we expect **F** to be smooth with respect to the topology of the graph. This can be expressed by setting the covariance matrix in its prior 

> 1See the note on page 48 for a how this assumption can be tested statistically. 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

47 

to be proportional to **H**[2] , where **H** is a graph filter as defined in equation (3.7). Again without loss of generality, we assume that the prior mean for **F** is zero across all elements. 

**==> picture [261 x 13] intentionally omitted <==**

Next, given an observation **Y** , we use Bayes’ rule to find the posterior distribution over **F** . This is given by 

**==> picture [291 x 26] intentionally omitted <==**

where we use the notation _π_ ( _·_ ) to denote a probability density function. 

The posterior distribution for **F** is given by 

**==> picture [288 x 13] intentionally omitted <==**

where **P** is the posterior precision matrix, given by 

**==> picture [267 x 12] intentionally omitted <==**

A proof of this can be found in the appendix, theorem A.1. In this chapter, we are primarily interested in computing the posterior mean, which is the solution to the following linear system. 

**==> picture [305 x 21] intentionally omitted <==**

Note that here, to avoid the introduction of further notation, we have used vec ( **F** ) to represent the posterior mean, whereas previously it represented a random variable. We return to the question of sampling from the posterior and estimating the posterior covariance directly in chapter 6. 

Two significant computational challenges arise when working with non-trivial graph signal reconstruction problems, where the number of vertices in the product graph is large. First, although the posterior mean point estimator given in eq. (3.17) has an exact closed-form solution, its evaluation requires solving an _NT × NT_ system of equations, which is impractical for all but the smallest of problems. Second, since the eigenvalues of **H** can be close to or exactly zero, **H** _[−]_[2] may be severely ill-conditioned and even undefined. This means the condition number of the coefficient matrix may not be finite, making basic iterative methods to numerically solve the 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

48 

linear system, such as steepest descent, slow or impossible. The models proposed in this section aim to overcome these problems. 

Since the coefficient matrix defining the system is of size _NT × NT_ , direct methods such as Gaussian elimination are assumed to be out of the question. In such cases, one often resorts to one of three possible solution approaches: stationary iterative methods; Krylov methods; or multigrid methods. Each is part of the family of iterative methods which are most commonly found in applications of sparse matrices, such as finite element methods [Brenner et al., 2008]. In the following, we propose a stationary iterative method and a Krylov method and compare their relative behaviour. In both cases, we show that each step of the iterative process can be completed in _O_ ( _N_[2] _T_ + _NT_[2] ) operations, making a solution feasible for relatively large graph problems. First, we present each of the methods in isolation. Then, the convergence behaviour of each is derived theoretically and verified numerically. 

## Is GSR appropriate? A statistical test 

Before beginning a graph signal reconstruction task, it is worth asking whether GSR indeed represents an appropriate method for the given data. Rephrasing this, the question boils down to whether the partially observed signal already exhibits smoothness with respect to the available graph. To test this statistically, we can perform the following steps. For simplicity, we will assume a one-dimensional GSR problem, however, the methods discussed can be extended to Cartesian product graphs (although some care must be taken to perform the operations efficiently). 

1. Downsample the partially observed signal **y** _∈_ R _[N]_ into a vector **y** � _∈_ R _N_[�] such that only the observed elements are kept. Do the same to the adjacency matrix to produce **A**[�] _∈_ R _N_[�] _×N_[�] , which represents the connections between the available nodes, and create its corresponding Laplacian **L**[�] _∈_ R _N_[�] _×N_[�] . 

2. Shift and scale the vector of observed data **y** � such that it has a mean of zero and unit variance. 

3. Compute the total square variation of **y** � as 

**==> picture [125 x 73] intentionally omitted <==**

**----- Start of picture text -----**<br>
TV2( y �) = y � [⊤] L [�]  � y<br>= ( U [�] [⊤] y �) [⊤] Λ [�]  ( U [�] [⊤] y �)<br>N �<br>� �<br>= � λn  ( U  � [⊤] y ) [2] n<br>n =1<br>**----- End of picture text -----**<br>


Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

49 

where **L**[�] = **U**[�] **Λ**[�] **U**[�] _[⊤]_ . 

4. Define the following hypothesis test: 

**Null hypothesis** H0: The vector **y** � is spherically distributed in the Fourier domain. **Alternative hypothesis** H1: **y** � is biased towards low-frequency Fourier components. 

� � � If H0 is true, then ( **U**[�] _[⊤]_ **y** ) _n ∼N_ (0 _,_ 1) and Cov ( **U**[�] _[⊤]_ **y** ) _i,_ ( **U**[�] _[⊤]_ **y** ) _j_ = _δij_ . In this case, � � TV2( **y** �) is the sum of _N_[�] independent gamma random variables, where 

**==> picture [142 x 21] intentionally omitted <==**

Therefore, 

**==> picture [209 x 19] intentionally omitted <==**

By the Lyapunov central limit theorem [Feller, 1968], we can therefore say that under the null hypothesis, TV2( **y** �) will be approximately distributed as 

**==> picture [147 x 71] intentionally omitted <==**

assuming that _N_[�] is sufficiently large. To test the hypothesis, we apply the corresponding _·_ Cumulative Distribution Function (CDF) Φ( ), with the above mean and variance, to the computed value of TV2( **y** �) and check whether it is less than some predefined level _p_ , for example, 0.05. 

**==> picture [186 x 42] intentionally omitted <==**

� In other words, if Φ (TV2( **y** )) is greater than _p_ , GSR is unlikely to be an effective tool since the partially observed signal does not exhibit smoothness with respect to the underlying graph at a statistically significant level. On the other hand, if it is less than _p_ then there is good evidence that the signal is smooth and that GSR will likely prove effective. 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

50 

## **3.2.2 A stationary iterative method** 

In this section, we demonstrate a technique for obtaining the posterior mean by adopting a classic approach to solving linear systems, known as _matrix splitting_ , which sits within the family of Stationary Iterative Methods (SIMs) [Saad, 2003]. The general splitting strategy is to break the coefficient matrix into the form **M** _−_ **N** , such that 

**==> picture [272 x 12] intentionally omitted <==**

By noting that 

**==> picture [299 x 11] intentionally omitted <==**

**==> picture [288 x 13] intentionally omitted <==**

we devise an iterative scheme given by 

**==> picture [304 x 12] intentionally omitted <==**

When **M** is a simple matrix that is easy to invert, this update function can be vastly more efficient to compute. Common approaches to finding a suitable value for **M** and **N** include the Jacobi, Gauss-Seidel and successive over-relaxation methods, each of which represents a different strategy for splitting the coefficient matrix [Saad, 2003]. However, whilst these techniques are well-studied, they are not appropriate for use in the case of graph signal reconstruction. This is because, for each of these methods, the coefficient matrix is split according to its diagonal and offdiagonal elements in some way. Consequently, this would require the evaluation of **H** _[−]_[2] directly which, as we have discussed, may be large, severely ill-conditioned and possibly ill-defined. 

Instead, we require a custom splitting that avoids direct evaluation of **H** _[−]_[2] , and allows the righthand side of eq. (3.21) to be computed efficiently. The main contribution of this subsection is the identification of appropriate values for **M** and **N** , and an investigation of the consequences of that choice. 

In the following, we set 

**==> picture [312 x 13] intentionally omitted <==**

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

51 

where **S** _[′]_ is the binary matrix representing the complement of the set of selected nodes, i.e. 

**==> picture [261 x 43] intentionally omitted <==**

In this way, the update equation is given by 

**==> picture [385 x 15] intentionally omitted <==**

_−_ 1 Note that this splitting is valid since � _γ_ **H** _[−]_[2] + **I** � is guaranteed to exist. It can also be readily computed as we already have the eigendecomposition of **H** . Noting the decomposed definition of **H** given in eq. (3.7), this can be written as 

**==> picture [340 x 89] intentionally omitted <==**

where **J** _∈_ R _[N][×][T]_ has elements defined by 

**==> picture [243 x 25] intentionally omitted <==**

Note that the update formula can be computed with _O_ ( _N_[2] _T_ + _NT_[2] ) complexity at each step. 

**==> picture [329 x 35] intentionally omitted <==**

Furthermore, this is reduced to _O_ ( _N_[2] _T_ + _NT_ log _T_ ) in the case of T-V problems, and to _O_ � _NT_ log _NT_ � for data residing on a grid (see section 3.2). 

It is well-known that a given splitting will be convergent if the largest eigenvalue _λ_ max of the matrix **M** _[−]_[1] **N** has an absolute value of less than one. This attribute, _ρ_ = _|λ_ max _|_ , is known as the spectral radius. 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

52 

Whilst the spectral radius of **M** _[−]_[1] **N** cannot be computed directly, we can derive an upper bound based on the properties of **M** and **N** individually. 

Consider the spectral radius of **M** _[−]_[1] . By directly inspecting eq. (3.25), it is clear that _ρ_ ( **M** _[−]_[1] ) will be the maximum entry in the matrix **J** since **M** _[−]_[1] is already diagonalised in the basis **U** _T ⊗_ **U** _N_ . Consider now the definition of **J** given in eq. (3.26). By definition, _g_ ( _·_ ) has a maximum value of one on the non-negative reals, achieved when its argument is zero. Since the graph Laplacian is guaranteed to have at least one zero eigenvalue, the maximum entry in the matrix **J** , and therefore the spectral radius of **M** _[−]_[1] , is surely given by 

**==> picture [245 x 23] intentionally omitted <==**

Next, consider the spectral radius of **N** . This can be extracted directly as one since it is a diagonal binary matrix. Since both **M** _[−]_[1] and **N** are positive semi-definite, we can apply the theorem 

**==> picture [252 x 11] intentionally omitted <==**

[Bhatia, 1997]. Therefore, the spectral radius of **M** _[−]_[1] **N** is guaranteed to be less than or equal to 1 _/_ (1+ _γ_ ). Since _γ_ is strictly positive, this is less than one and, as such, convergence is guaranteed. We return to the question of convergence more thoroughly in section 3.3. 

Finally, the update formulas given in eqs. (3.27) and (3.28) can be written equivalently as 

**==> picture [295 x 14] intentionally omitted <==**

**==> picture [306 x 13] intentionally omitted <==**

In this form, the iterations can be easily terminated when _|_ ∆ **F** _k|_ is sufficiently small. The complete procedure is given in algorithm **1** . 

## **3.2.2.1 An eigendecomposition-free distributed implementation** 

In the previous section, we introduced the SIM algorithm, premised on the assumption that the matrices **L** _T_ and **L** _N_ could be decomposed into **U** _T_ **Λ** _T_ **U** _[⊤] T_[and] **[ U]** _[N]_ **[Λ]** _[N]_ **[U]** _[⊤] N_[respectively.][However,] it is also feasible to implement the SIM in a manner that avoids the eigendecomposition of both Laplacians and instead only requires the repeated multiplication of vectors by **L** _T ⊕_ **L** _N_ in the 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

53 

**Algorithm 1** Stationary iterative method with matrix splitting 

**==> picture [273 x 295] intentionally omitted <==**

node domain. If, as is often the case, the original graphs are sparse, this can be achieved with complexity _O_ ( _T |EN |_ + _N |ET |_ ). This alternative is particularly beneficial when working with large factor graphs since the complexity involved in decomposition generally scales at _O_ ( _N_[3] + _T_[3] ). 

Moreover, in certain contexts like sensor or IoT networks, nodes may possess the capability to communicate and compute locally. In such instances, a distributed approach to the signal reconstruction problem, employing a message-passing algorithm, may be more desirable. In this section, we will discuss how these two objectives can be realised by utilising Chebyshev polynomials [Rivlin, 2020]. 

First, note that each iteration of the SIM algorithm is computed by multiplying some vector, vec ( **Z** ), by the matrix **M** _[−]_[1] , which is given by eq. (3.25). Crucially, since **M** _[−]_[1] has eigenvectors **U** _T ⊗_ **U** _N_ , it can be understood as a function applied to a weighted Kronecker sum of the factor graph Laplacians. In particular, 

**==> picture [266 x 13] intentionally omitted <==**

where 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

54 

**==> picture [77 x 25] intentionally omitted <==**

and _g_ ( _·_ ) represents the original filter function used, with parameters _βT , βN_ . (Here, we interpret the application of _J_ ( _x_ ) to a matrix in terms of a power series rather than element-wise.) Thus, eigendecomposition can be entirely bypassed by approximating the function _J_ ( _x_ ) using shifted Chebyshev polynomials [Isufi et al., 2024]. This requires knowledge of the largest eigenvalues of **L** _T_ and **L** _N_ , _λ_[(max)] _T_ and _λ_[(max)] _N_ respectively, but these can also be computed efficiently using methods that take advantage of sparsity such as Arnoldi iterations. 

Assuming an order _K_ approximation to the function _J_ ( _x_ ) is used, with shifted Chebyshev polynomials _T_[¯] _k_ ( _x_ ) defined over the interval [0 _, λ_[¯] ], where _λ_[¯] = _βT λ_[(max)] _T_ + _βN λ_[(max)] _N_ , the approximation is given by 

**==> picture [250 x 30] intentionally omitted <==**

where the coefficients, _ck_ , are computed numerically via the integral given in eq. (2.9) of section 2.2.2. The action of **M** _[−]_[1] on an arbitrary vector vec ( **Z** ) can then be approximately computed as 

**==> picture [282 x 31] intentionally omitted <==**

where **L**[¯] = _βT_ **L** _T ⊕ βN_ **L** _N_ . The result of _T_[¯] ( **L**[¯] )vec ( **Z** ) is defined recursively as 

**==> picture [341 x 25] intentionally omitted <==**

with the initial conditions 

**==> picture [357 x 22] intentionally omitted <==**

In addition, the action of **L**[¯] on vec ( **Z** ) can be efficiently computed as 

**==> picture [287 x 13] intentionally omitted <==**

with complexity _O_ � _NT_ ( _|ET |_ + _|EN |_ )�. When performed in a distributed manner, this operation can be executed at each node utilising information about the value of vec ( **Z** ) at its direct 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

55 

neighbours only. This implies that to compute an order _K_ polynomial, information will need to be gathered from nodes that are a maximum of _K_ hops away via graph edges. 

In the context of a graph time series problem, this method also lends itself to an online implementation. In particular, since each node requires information from nodes no further than _K_ hops away, the signal at node _n_ at time _t_ can be reconstructed when the observed signal at time _t_ + _K_ becomes available. 

One caveat worth noting is that the accuracy of the Chebyshev approximation depends not only on the order of the polynomial but also on the filter used and its parameter(s). Figure 3.3 demonstrates how an order-3 approximation to _J_ ( _x_ ), with _γ_ = 0 _._ 05, varies across several different filter types and parameter settings. For filter functions that exhibit slow variation, typically corresponding to smaller values of _β_ , the fit is usually quite accurate. However, in certain other contexts, it deviates significantly from the true filter function. Another consideration is that the spectral radius of **M** _[−]_[1] is no longer guaranteed to be less than one. For instance, in the case of the bandlimited filter shown in fig. 3.3, the function clearly reaches higher values. To guarantee convergence, the polynomial coefficients should be adjusted such that the approximation remains within the range of [ _−_ 1 _,_ 1]. 

## **3.2.3 A conjugate gradient method** 

The second approach we consider for computing the posterior mean is to use the Conjugate Gradient Method (CGM). First proposed in 1952, the CGM is part of the Krylov subspace family and is perhaps the most prominent iterative algorithm for solving linear systems [Hestenes and Stiefel, 1952]. In computational terms, the method only requires repeated forward multiplication of vectors by the coefficient matrix which, in the standard CGM, bust be PSD. It is therefore effective in applications where this process can be performed efficiently. 

In brief, the CGM seeks to solve the linear system **Ax** = **b** by minimising, at the _k_ -th iteration, some measure of error in the affine space **x** 0 + _Kk_ where _Kk_ is the _k_ -th Krylov subspace given by 

**==> picture [144 x 13] intentionally omitted <==**

The residual **r** _k_ is given by 

**==> picture [58 x 10] intentionally omitted <==**

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

56 

**==> picture [375 x 398] intentionally omitted <==**

**----- Start of picture text -----**<br>
β = 0 . 2 β = 0 . 5 β = 1 β = 3<br>1<br>Diffusion<br>0<br>1<br>1-Hop<br>0<br>1<br>ReLu<br>0<br>1<br>Sigmoid<br>0<br>1<br>Gaussian<br>0<br>1<br>Bandlimited<br>0<br>**----- End of picture text -----**<br>


Figure 3.3: An order-3 Chebyshev polynomial approximation (orange) is compared to the true output of _J_ ( _x_ ) (dashed blue) for several different filter types across various parameter settings. Note how the accuracy of the fit depends on both the filter function used and the value of _β_ . Furthermore, the approximation can sometimes fall outside of the [0, 1] interval. 

and the _k_ -th iterate of the CGM minimises 

**==> picture [100 x 21] intentionally omitted <==**

over **x** 0 + _Kk_ [Kelley, 1995]. 

The CGM works best when the coefficient matrix **A** has a low condition number _κ_ (that is, the ratio between the largest and smallest eigenvalue is small) and, as such, a preconditioning step is often necessary. The purpose of a preconditioner is to reduce _κ_ by solving an equivalent transformed problem. This can be achieved by right or left multiplying the linear system by a preconditioning matrix **Ψ** . However, this likely means the coefficient matrix is no longer 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

57 

PSD, meaning the CGM cannot be used in its basic form. (Other approaches modified for nonPSD matrices exist, e.g. the CGNE or GIMRES [Elman, 1982, Saad and Schultz, 1986]). A preconditioner can also multiply the coefficient matrix on the right by a preconditioner **Ψ** _[⊤]_ and on the left by **Ψ** . This preserves the symmetry meaning we can continue to use the regular CGM. 

In our case, where the coefficient matrix is given by diag (vec ( **S** )) + _γ_ **H** _[−]_[2][�] , preconditioning � will be essential for convergence. To see why, consider the definition of **H** in equation (3.7). A low-pass filter function _g_ ( _·_ ) may be close to zero when applied to the high-frequency eigenvalues of the graph Laplacian, meaning elements of diag (vec ( **G** )) _[−]_[2] may be very large. In the worst case, for example with a band-limited filter, the matrix **H** will be singular, no matrix **H** _[−]_[2] will exist, and the condition number of the coefficient matrix will be, in effect, infinite. Therefore, the primary purpose of this subsection is to find a preconditioner that maintains efficient forward multiplication and is effective at reducing the condition number of the coefficient matrix. 

References such as Saad [2003] give a broad overview of the known approaches to finding a preconditioner. Standard examples include the Jacobi preconditioner which is given by the inverse of the coefficient matrix diagonal and is effective for diagonally dominant matrices, and the Sparse Approximate Inverse preconditioner [Grote and Huckle, 1997]. However, such preconditioners generally require direct evaluation of parts of the coefficient matrix or are computationally intensive to calculate. 

In the following, we derive an effective symmetric preconditioner that allows forward multiplication of the coefficient matrix to be performed efficiently. First consider the transformed variable **Z** , related to **F** in the following way. 

**==> picture [253 x 13] intentionally omitted <==**

Here, **Z** can be interpreted as a set of Laplacian frequency coefficients, which are subsequently scaled according to the graph filter function, and then reverse Fourier transformed back into the node domain. Matrices **Z** which are distributed according to a spherically symmetric distribution, result in signals **F** which are smooth with respect to the graph topology. Since this transform filters out the problematic high-Laplacian frequency Fourier components, the system defined by this transformed variable **Z** is naturally far better conditioned. 

By substituting this expression for **F** back into the likelihood in equation (3.12), and the prior of equation (3.13), one can derive a new expression for the posterior mean of **Z** . This is done explicitly in theorem A.2. The end result is that the new linear system for the transformed variable **Z** is given by 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

58 

**==> picture [397 x 21] intentionally omitted <==**

where we have abbreviated diag (vec ( **G** )) and diag (vec ( **S** )) as **DG** and **DS** respectively. Note that the conditioning of the coefficient matrix is greatly improved from the untransformed problem, as we will discuss in greater detail in section 3.3. Note also that the multiplication of a vector vec ( **R** ) by the coefficient matrix can be computed efficiently as 

**==> picture [407 x 42] intentionally omitted <==**

This has _O_ ( _N_[2] _T_ + _NT_[2] ) complexity at each step which may be reduced to _O_ ( _N_[2] _T_ + _NT_ log _T_ ) in the case of T-V problems, and to _O_ � _NT_ log _NT_ � for data residing on a grid (see section 3.2). 

The linear system defined eq. (3.40) can be understood as a two-sided symmetrically preconditioned version of the original linear system given in eq. (3.17). In particular, the new expression can be constructed by modifying the original system in the following way. 

**==> picture [324 x 19] intentionally omitted <==**

where 

**==> picture [256 x 12] intentionally omitted <==**

Since preconditioning of the coefficient matrix on the left is achieved with **Ψ** _[⊤]_ and on the right with **Ψ** , symmetry is preserved. This ensures that one can continue to utilise algorithms tailored to work with PSD matrices. In algorithm **2** , we outline a conjugate gradient method based on this new formulation. 

## **3.2.4 Real data experiments** 

In this subsection, we evaluate our GSR method using a dataset consisting of daily new SARSCoV-2 cases reported in 372 lower-tier local authorities across the United Kingdom from February 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

59 

**Algorithm 2** Conjugate gradient method with graph-spectral preconditioner 

**==> picture [331 x 361] intentionally omitted <==**

5, 2020, to March 18, 2023 (1138 days) taken from the UK government website[2] . Specifically, we focused on the “newCasesBySpecimenDateRollingRate” metric, which represents the daily number of cases reported per 100,000 residents in each local reporting authority over a 7-day rolling period. To create a graph, we used boundary data[3] , setting adjacency matrix entries as **A** _ij_ to one if districts _i_ and _j_ share a border, and zero otherwise. Note, this graph construction strategy is fairly crude, with the underlying assumption being that virus spread occurs mainly between neighbouring regions. Perhaps a more sophisticated model could use data such as interregion travel volumes to construct a graph, although such data was not easily available at the time of writing. Figure 3.4 illustrates a snapshot of this dataset on December 1, 2020. 

Before beginning the experiments, we performed two preprocessing steps on the raw signal data. First, we took the logarithm of 10 plus the original case rate. This was to eliminate the long tail in the case rate histogram, transforming it to be closer to a Gaussian. We then normalised by 

> 2See `https://coronavirus.data.gov.uk/details/download` 

> 3Data from the Office for National Statistics [ONS, 2019] 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

60 

**==> picture [16 x 136] intentionally omitted <==**

**----- Start of picture text -----**<br>
225<br>200<br>175<br>150<br>125<br>100<br>75<br>50<br>**----- End of picture text -----**<br>


Figure 3.4: The seven-day rolling rate of new Covid cases reported per 100,000 residents in each lower-tier local reporting authority in the United Kingdom on the 1st of December 2020. Missing data is indicated in grey. 

subtracting the overall mean and dividing by the standard deviation. The resultant signal, of shape 372 _×_ 1138, we refer to as **Y** 0. Note that 4.8% of the entries in **Y** 0 were already missing from the original dataset (mostly occurring in the earlier stages of the pandemic). 

The experiment was conducted as follows. First, we removed data from **Y** 0 such that a total fraction _m_ was no longer present. This created two matrices: **Y** , the partially observed signal with missing values filled with zeros; and **S** , the corresponding binary sensing matrix. Data was removed in four distinct ways. First, individual elements of **Y** were selected uniformly at random for removal (‘uniform’). Second, strings of 100 days, beginning at a random date, were removed for individual randomly selected districts (‘strings’). Third, the entire time series for randomly chosen districts were removed (‘districts’). Finally, the signal across every node at randomly selected dates was removed (‘dates’). These four techniques for data removal are depicted for clarity in fig. 3.5. For each technique, we solved the signal reconstruction problem using the GSR model described in this chapter and compared its performance to other baseline reconstruction strategies. In particular, for uniform and string removal, we compared it to linear interpolation in time and longitudinal averaging across all districts. For date removal, we compared it to interpolation in time only, since longitudinal averaging is not possible in this case. Finally, for 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

61 

**==> picture [247 x 194] intentionally omitted <==**

**----- Start of picture text -----**<br>
T T<br>Uniform String s<br>N N<br>T T<br>Dates Districts<br>N N<br>**----- End of picture text -----**<br>


Figure 3.5: A visual depiction of the four ways we removed data. Black lines/dots indicate data that was removed. 

district removal, we compared it to longitudinal averaging, since linear interpolation in time is not possible in this case. For each model, for each method of data removal, we measured the Root Mean Square Error (RMSE) across the reconstructed entries, over four increasing values of _m_ . 

In addition to the aforementioned reconstruction models, we also implemented the time-varying signal reconstruction models described in Qiu et al. [2017]. In this paper, the authors describe two alternative methods for reconstructing a time-varying graph signal representing a noiseless and a noisy case. The noiseless case seeks the reconstructed signal **F** that minimises their chosen smoothness metric subject to the constraint that it precisely interpolates the observed values of **Y** . The noisy case, which is more similar to the model described in this paper, assumes a certain level of noise in the observed values and does not strictly interpolate. The results are shown in table 3.4. 

The findings indicate that the graph-aware approaches exhibit significantly better performance, particularly for the ‘strings’ and ‘districts’ removal strategies. In particular, they outperform longitudinal averaging, underscoring the substantial benefits derived from integrating topological relationships between districts. Conversely, when individual dates are excluded, thus likely leaving only brief segments of the time series absent in any district, the GSR methods remain competitive, albeit linear interpolation shows marginally superior results. This outcome is anticipated for this dataset, considering the metric is computed using a 7-day rolling average, which naturally results in a smooth signal progression. Nevertheless, GSR stands out for its adaptability, applicable to various patterns of missing data. 

Comparing the Bayesian GSR model presented in this study with the noiseless and noisy GSR 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

62 

|_m_|Uniform<br>0.1<br>0.3<br>0.5<br>0.7|Strings|
|---|---|---|
|||0.1<br>0.3<br>0.5<br>0.7|
|Bayesian GSR<br>Qiu et al noiseless<br>Qiu et al noisy<br>Linear interp<br>Longitudinal avrg|0.037<br>0.040<br>0.048<br>0.081<br>0.040<br>0.043<br>0.054<br>0.092<br>0.037<br>0.041<br>0.048<br>0.080<br>0.034<br>0.039<br>0.049<br>0.070<br>0.350<br>0.348<br>0.347<br>0.348|0.230<br>0.249<br>0.247<br>0.243<br>0.242<br>0.255<br>0.254<br>0.251<br>0.229<br>0.249<br>0.249<br>0.244<br>0.540<br>0.531<br>0.520<br>0.526<br>0.341<br>0.350<br>0.356<br>0.347|
|_m_|Dates<br>0.1<br>0.3<br>0.5<br>0.7|Districts|
|||0.1<br>0.3<br>0.5<br>0.7|
|Bayesian GSR<br>Qiu et al noiseless<br>Qiu et al noisy<br>Linear interp<br>Longitudinal avrg|0.038<br>0.055<br>0.058<br>0.075<br>0.041<br>0.060<br>0.062<br>0.079<br>0.037<br>0.040<br>0.048<br>0.081<br>0.035<br>0.038<br>0.046<br>0.066<br>NA<br>NA<br>NA<br>NA|0.202<br>0.249<br>0.271<br>0.273<br>0.210<br>0.257<br>0.281<br>0.282<br>0.202<br>0.248<br>0.274<br>0.273<br>NA<br>NA<br>NA<br>NA<br>0.318<br>0.333<br>0.347<br>0.345|



Table 3.4: The RMSE for different reconstruction models and data removal techniques on the UK SARS-CoV-2 case rate dataset. For each fraction of missing data _m_ , the best-performing model is highlighted in green. Entries where the model is not applicable are indicated by NA. 

models discussed in Qiu et al. [2017], it emerges that both the noisy model and Bayesian GSR generally surpass the noiseless model. This disparity is likely attributable to the significant noise in the real data, which disproportionately influences the reconstruction predictions. The performances of Bayesian GSR and Qiu’s noisy model are closely matched, with Bayesian GSR slightly outperforming in a small majority of scenarios. 

## **3.3 Convergence properties** 

In this section, we conduct a thorough theoretical analysis of the convergence properties of both the SIM and the CGM. As we will demonstrate, their respective convergence rates are heavily influenced by the values of the hyperparameters _β_ , which describes the strength of the graph filter, _γ_ , which determines the regularization strength, and _m_ = _|S[′] |/NT_ , which represents the fraction of values missing from the original graph signal. This helps explain the empirical convergence 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

63 

behaviour and offers insight into trade-offs when it comes to hyperparameter selection. Furthermore, it allows users to make an informed decision about selecting an appropriate method, considering the inherent characteristics of their specific problem. 

It is well-known that the worst-case number of iterations required to reduce the error below some specific tolerance level for matrix splitting methods is inversely proportional to _−_ log _ρ_ ( **M** _[−]_[1] **N** ), where _ρ_ ( _·_ ) denotes the spectral radius (absolute value of the maximum eigenvalue) of a matrix [Demmel, 1997]. For completeness, we provide a brief proof of this in theorem A.3. In the specific context of our graph signal reconstruction algorithm as outlined in section 3.2.2, **M** and **N** have the following values. 

**==> picture [161 x 15] intentionally omitted <==**

where **U** = **U** _T ⊗_ **U** _N_ , **DJ** = diag (vec ( **J** )), and **DS** _′_ = diag (vec ( **S** _[′]_ )). Therefore, the number of iterations required for convergence of the SIM scales as 

**==> picture [273 x 23] intentionally omitted <==**

Note that the matrix **J** [see eq. (3.26) for its definition] has entries that depend on both the regularisation parameter _γ_ and the spectral scaling matrix **G** , which is itself a function of the graph filter parameter(s) _β_ [see eqs. (3.8) and (3.9)]. The matrix **DS** _′_ has entries that depend on the structure of the missing data in the graph signal. Therefore should we expect that the spectral radius, _ρ_ , and consequently the number of steps required for convergence, _n_ SIM, can be affected by all three. 

Similarly, in the conjugate gradient method, the worst-case number of steps required to achieve a specific termination criterion is well-known to be proportional to _[√] κ_ , where _κ_ represents the condition number of the coefficient matrix, i.e. the ratio between the largest and smallest eigenvalue Kelley [1995]. In our particular scenario, the coefficient matrix is provided in eq. (3.40). Therefore, we should expect that the number of iterations required for convergence of the CGM will scale as 

**==> picture [296 x 19] intentionally omitted <==**

where **DG** = diag (vec ( **G** )). Once again, this expression contains the matrix **G** , which depends on the strength of the graph filter function parameter _β_ , the matrix **DS** , which depends on the structure of this missing data, and the precision parameter _γ_ . Consequently, we should expect that, in general, convergence of the CGM is affected by all three of these variables. 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

64 

Whilst it is not possible in general to obtain an analytic expression for _ρ_ or _κ_ as a function of _γ, β_ and _m_ , we can nonetheless gain useful insight into how each of these variables can be expected to affect convergence. We achieve this by considering two distinct limits: one in which the graph filter is very strong (i.e. _β_ is very large) and one in which the graph filter is very weak (i.e. _β_ is very small). 

## **3.3.1 Upper bound on convergence: the weak filter limit** 

Consider the limiting case of a weak filter, where all spectral components are allowed to pass through unaffected. In this case, a graph filter **H** [see eq. (3.7)], which appears in the prior distribution for **F** [see eq. (3.13)], becomes the identity matrix **I** _NT_ . This means no topological information is included in the prior for **F** at all. Given the definitions of the graph filters in tables 2.1 and 3.3, we can conceptualise this as the limit where the parameter characterising the graph filter _β →_ 0 (or, more generally, the limit as _**β** →_ [0 _,_ 0] for an anisotropic graph filter). Since all spectral components are maintained, every element of the spectral scaling matrix **G** will be equal to one. Given eq. (3.26), this further implies the every entry in the matrix **J** becomes 1 _/_ (1 + _γ_ ). 

**==> picture [202 x 23] intentionally omitted <==**

Now consider the spectral radius _ρ_ of the update matrix in the SIM. Given this limiting value of **DJ** , it can be directly evaluated as 

**==> picture [311 x 23] intentionally omitted <==**

Next, consider the condition number _κ_ of the coefficient matrix in the CGM. Again, since in this limit **DG** = **I** , it can be directly evaluated as 

**==> picture [349 x 23] intentionally omitted <==**

Given eqs. (3.44) and (3.45), we can characterise the number of iterations required to reach some convergence criterion in the weak filter limit for the SIM and CGM respectively as 

**==> picture [342 x 26] intentionally omitted <==**

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

65 

These expressions imply that when _γ_ is large, both methods converge quickly. However, they both see the number of iterations increase to infinity as _γ →_ 0. To characterise this more precisely, consider the Taylor expansion of each expression around _γ_ = 0. 

**==> picture [361 x 21] intentionally omitted <==**

As visible, dominant behaviour for small _γ_ follows _O_ ( _γ[−]_[1] ) for the SIM and _O_ ( _γ[−]_[1] _[/]_[2] ) for the CGM. 

## **3.3.2 Lower bound on convergence: the strong filter limit** 

Consider now the limiting case of a strong filter as applied to a signal on a fully connected Cartesian product graph. In this case, every spectral component is filtered out except the the first Laplacian frequency component **u**[(] 1 _[T]_[ )] _⊗_ **u**[(] 1 _[N]_[)] _∝_ **1** (also known as the bias), with eigenvalue _λ_[(] 1 _[T]_[ )] + _λ_[(] 1 _[N]_[)] = 0, which passes through the filter unaffected. When a filter of this kind is used in the prior for **F** , it effectively forces predictions that are constant across all nodes. Given the definitions of the graph filter functions given in tables 2.1 and 3.3, we can associate this with the limit as _β →∞_ . Here, the effect of applying the graph filter to a generic graph signal vec ( **Y** ) is to extract the mean, that is 

**==> picture [132 x 32] intentionally omitted <==**

In this case, the spectral scaling matrix **G** has entries that are zero for all elements except (1, 1) which has the value one. Similarly, the matrix **J** has the value 1 _/_ (1 + _γ_ ) at element (1, 1) and zeros elsewhere. This implies that 

**==> picture [198 x 23] intentionally omitted <==**

where **∆** is an _NT × NT_ matrix given by 

**==> picture [94 x 55] intentionally omitted <==**

In the case of the SIM, the spectral radius of **M** _[−]_[1] **N** in this limit is therefore given by 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

66 

**==> picture [205 x 23] intentionally omitted <==**

Note that 

**==> picture [124 x 21] intentionally omitted <==**

where **O** _NT_ is an _NT × NT_ matrix of ones. Therefore the spectral radius is given by 

**==> picture [236 x 72] intentionally omitted <==**

Since the matrix in brackets is just the vector vec ( **S** _[′]_ ) _[⊤]_ repeated in every row it is surely of rank one and therefore must have an eigenvalue of 0 with multiplicity _NT −_ 1. This implies that the only non-zero eigenvalue (and therefore the spectral radius _ρ_ ) is given by its trace, which is � _n,t_ **[S]** _nt[′]_[=] _[ |S][′][|]_[.][Denoting] _[m]_[ =] _[ |S][′][|][/NT]_[,][this][can][be][expressed][as] 

**==> picture [306 x 25] intentionally omitted <==**

Now consider the condition number _κ_ of the CGM coefficient matrix. In the strong filter limit, this is given by 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

67 

lim _κ_ � **DGU** _[⊤]_ **DSUDG** + _γ_ **I** � = _κ_ � **∆U** _[⊤]_ **DSU∆** + _γ_ **I** � _β→∞_ 

**==> picture [218 x 175] intentionally omitted <==**

Given eqs. (3.44) and (3.45), we can write the scaling rate for the number of iterations in the SIM and CGM respectively. 

**==> picture [385 x 25] intentionally omitted <==**

A key feature of these expressions is that increasing the fraction of missing data _m_ will increase _n_ SIM, but decrease _n_ CGM. Note also that, in the case of a strong filter, the number of iterations required for convergence of the CGM, _n_ CGM, still goes to infinity as _γ →_ 0. However, this behaviour is no longer present for _n_ SIM, which tends towards a constant value of _−_ 1 _/_ log _m_ . Taking a Taylor series expansion of both expressions about _γ_ = 0 demonstrates the asymptotic behaviour in terms of _γ_ more clearly. 

**==> picture [374 x 28] intentionally omitted <==**

In particular, at small _γ_ , the CGM still runs with complexity proportional to _γ[−]_[1] _[/]_[2] whereas the SIM does not involve _γ_ to a negative power at all. Note that _m_ cannot scale arbitrarily close to zero or one, since it will surely be between 1 _/NT_ and 1 _−_ 1 _/NT_ . 

## **3.3.3 Practical implications and method selection** 

In the preceding two sections, we have derived several formulae that characterise the convergence behaviour of both the CGM and the SIM in the limiting case of a strong and weak filter, where _β →∞_ and _β →_ 0 respectively. For the sake of clarity, we have consolidated the critical 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

68 

||||_n_SIM<br>All _γ_<br>Small _γ_|_n_SIM<br>All _γ_<br>Small _γ_||_n_CGM|_n_CGM|_n_CGM|
|---|---|---|---|---|---|---|---|---|
|||||||All _γ_||Small _γ_|
|_β →_0<br>_β →∞_||||_γ−_1<br><br>1<br>log_m_|~~�~~|~~�~~<br>|1 + _γ_<br>_γ_<br>_−m_+ _γ_<br>_γ_<br>�|_γ−_1_/_2<br><br>_γ_<br>1_−m_<br>�_−_1_/_2|
|||||||1|||
||||||||||



Table 3.5: The scaling behaviour of the number of steps required for convergence is shown as a function of _γ_ and _m_ . The upper row gives the behaviour in the limit of a weak filter, and the lower row gives the behaviour in the limit of a strong filter. We also show the dominant term in the Taylor expansion about _γ_ = 0 (“small _γ_ ” columns) which gives a clearer picture of the asymptotic behaviour as _γ →_ 0. 

expressions in table 3.5. In this section, we take a closer look at these expressions and distil the key features that are relevant for implementing these methods in practice. 

First consider the value of _γ_ , which enters the model via eq. (3.13), and acts as a strictly positive regularisation parameter. For both the SIM and CGM, smaller values of _γ_ will universally increase the total number of iterations. This can be proven by taking the partial derivative of each expression with respect to _γ_ , and demonstrating that the resulting expressions are negative for all valid values of _γ_ and _m_ . For completeness, we perform this explicitly in the proof of theorem A.4. Furthermore, the number of iterations will tend towards infinity as _γ →_ 0 in all cases except an asymptotically strong filter with the SIM. When the filter is weak, we should expect that the number of iterations grows faster for the SIM than the CGM as _γ_ approaches zero. This can be seen from the Taylor series expansion about _γ_ = 0, which has a dominant term of _γ[−]_[1] for the SIM and _γ[−]_[1] _[/]_[2] for the CGM. When _γ_ is large we should expect fast convergence for both the SIM and CGM regardless of the value of the other hyperparameters. 

Consider now the parameter _β_ , which characterises the strength of the graph filter, and also enters the model in the prior for **F** in eq. (3.13). For both the SIM and CGM, higher values of _β_ , which more aggressively filter out high-frequency spectral components, are associated with faster convergence. In other words, like _γ_ , increasing _β_ will decrease the number of iterations required to reach a fixed termination condition. This is evidently true since the expressions for _n_ SIM and _n_ CGM are lower when _β →∞_ than they are when _β →_ 0, for any valid value of 0 _≤ m ≤_ 1. It is also reasonable to expect that the number of iterations will decrease monotonically as _β_ is increased, however, we provide no formal proof of this. In contrast to the behaviour of _γ_ , however, these two bounds are still both finite meaning that, the number of steps required for convergence remains finite as _β →_ 0. 

Whilst the convergence rates of both the SIM and CGM have the same directional response to 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

69 

changes in _γ_ and _β_ , they display the opposite behaviour when _m_ is varied. In particular, a higher proportion of missing value in **Y** , corresponding to an increasing value of _m_ , causes the number of iterations to rise for the SIM but fall for the CGM, at least in the limit of a strong filter as _β →∞_ . This can be shown explicitly by taking the partial derivative of _n_ SIM and _n_ CGM with respect to _m_ and demonstrating that it is universally positive for the former and negative for the latter (which we show in theorem A.5). While _m_ has no effect for either the SIM or CGM in the limit as _β →_ 0, we can reasonably expect that it will have _some_ effect for intermediate values of _β_ . This insight is especially important since, unlike _γ_ and _β_ , _m_ is a feature of the data rather than an adjustable hyperparameter. 

## **3.3.4 Experimental validation** 

In order to verify aspects of this theoretically predicted behaviour, we ran several experiments using synthetic data. In particular, we generated two random fully connected graphs, each with 50 nodes, and take their Cartesian product to create a product graph with 2500 nodes. Next, we generated a random 50 _×_ 50 matrix of i.i.d. Gaussian noise with unit variance and chose a fraction _m_ to be removed uniformly at random to generate an observed graph signal **Y** _∈_ R[50] _[×]_[50] and corresponding binary sensing matrix **S** _∈{_ 0 _,_ 1 _}_[50] _[×]_[50] . Next, we set a prior for the underlying smooth signal **F** with precision _γ_ using an isotropic diffusion filter (see table 2.1) with parameter _β_ . We then solved the graph signal reconstruction problem using both the SIM and CGM and counted the number of iterations required to reach a termination condition. Specifically, for the SIM, we terminate when ∆ **F** has a root mean square value of 10 _[−]_[8] , and, for the CGM, when the residual has a root mean square value of 10 _[−]_[5] , which we empirically determined resulted in similar final precision. In the following experiments, we completed this procedure for various values of _m_ , _β_ and _γ_ , and compared the empirical number of iterations required for convergence against the theoretical predictions determined in section 3.3. 

## **3.3.4.1 Experiment 1: testing the strong and weak filter limits** 

In the first experiment, we fix _β_ at zero and _∞_ , and measure the number of iterations required for convergence over a range of values of _m_ and _γ_ . Since these correspond to the weak and strong filter limits respectively, we expect that the convergence rate should be bounded by a function proportional to those given in table 3.5. First, we set _β_ = 0. Note that, in this case, _m_ does not affect the convergence rate of the SIM or CGM (which we also find empirically to be the case). We therefore varied _γ_ alone in 50 logarithmically spaced increments from 10 _[−]_[4] to 10[2] . The results are shown in fig. 3.6. As is visible, the functions broadly follow the expected convergence rate given by the theoretical prediction, performing slightly better in practice in both cases. Note that this is the expected behaviour since the limits give a _worst case_ scaling rate. In both cases, 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

70 

**==> picture [292 x 219] intentionally omitted <==**

**----- Start of picture text -----**<br>
10 [5] SIM theoretical<br>CGM theoretical<br>SIM empirical<br>CGM empirical<br>10 [4]<br>10 [3]<br>10 [2]<br>10 [1]<br>10 4 10 3 10 2 10 1 10 [0] 10 [1] 10 [2]<br>Iteration count<br>**----- End of picture text -----**<br>


Figure 3.6: The number of iterations required for convergence in the weak filter limit for the SIM and CGM both theoretically and empirically, as a function of _γ_ . 

we also scaled the theoretical prediction (corresponding to a vertical shift in the log-log plot) to fit the experimental data. This is also valid since the theoretical predictions give a function proportional to the number of iterations rather than the number of iterations itself. For the SIM, this factor was approximately 10, and for the CGM this factor was approximately 4.5. 

For the second part of experiment 1, we set _β_ = _∞_ , corresponding to the strong filter limit. In this case, we expect the number of iterations to be a function of both _m_ and _γ_ as specified in table 3.5. Therefore, we varied _γ_ in 50 logarithmically spaced increments from 10 _[−]_[6] to 10[2] and _m_ in 50 linearly spaced increments from 0.01 to 0.99. For each unique pair of _m_ and _γ_ , we then counted the number of iterations required for convergence and compared this to the theoretical predictions. The results are shown in fig. 3.7. Again, the empirical results broadly follow the theoretical functions which, as before, are scaled to fit the data. As with the weak filter limit, we again see that the empirical scaling rate is slightly better than the worst-case theoretical prediction. 

## **3.3.4.2 Experiment 2: Testing intermediate values of** _β_ 

In the second experiment, we test the number of iterations required for convergence for intermediate values of _β_ . Note that the analysis carried out in section 3.3 applies only for extremal values of _β_ , meaning the intermediate behaviour is not clearly defined, and will depend on the filter chosen in practice. This was carried out for three values of _m_ : 0.05, 0.5 and 0.95, representing low, medium and high prevalence of missing data respectively. For each value of _m_ , we compute the solution using both algorithms over a grid of 50 _β_ values and 50 _γ_ values which 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

71 

**==> picture [413 x 317] intentionally omitted <==**

**----- Start of picture text -----**<br>
SIM CGM<br>Theoretical<br>Empirical<br>103 103<br>102 102<br>101 101<br>100 100<br>1.0<br>0.8 m0.6 0.4 0.2 0.0 102 100 10 2 10 4 10 6 1.0 0.8 m0.6 0.4 0.2 0.0 102 100 10 2 10 4 10 6<br>103 103<br>102 102<br>101 101<br>100 100<br>1.0<br>0.8 m0.6 0.4 0.2 0.0 102 100 10 2 10 4 10 6 1.0 0.8 m0.6 0.4 0.2 0.0 102 100 10 2 10 4 10 6<br>Iteration count<br>Iteration count<br>**----- End of picture text -----**<br>


Figure 3.7: The number of iterations required for convergence is shown both theoretically and empirically for the SIM and CGM in the strong filter limit, where _β_ = _∞_ . In this case, each plot is a function of both _m_ and _γ_ . The colourmap corresponds to vertical height and is normalised across each plot to aid comparison. 

were logarithmically spaced between 10 _[−]_[1] -10[2] and 10 _[−]_[4] -10[1] respectively. The results are shown in fig. 3.8. 

This experiment validates several key aspects of the theoretical convergence analysis. Firstly, notice that the basic behaviour that the number of iterations rises in all cases as _β_ and _γ_ get closer to zero. Furthermore, in all cases, regardless of the value of _m_ or _β_ , convergence is very fast when _γ_ is large. We also observe the predicted behaviour that the number of iterations plateaus as a function of decreasing _γ_ when _β_ is large for the SIM while it continues to increase for the CGM. However, for this data, the CGM level seems to remain below that of the SIM in this limit. 

One key result of this experiment that aligns with the theoretical prediction is that convergence is accelerated as _m_ rises for the CGM but convergence slows as _m_ rises for the SIM. In particular, for this dataset, _n_ SIM _≤ n_ CGM for all values of _γ_ and _β_ when _m_ = 0 _._ 05, but _n_ CGM _≤ n_ SIMM for all values of _γ_ and _β_ when _m_ = 0 _._ 95. This is particularly impactful as it strongly indicates the CGM should be preferable when data is sparsely observed and the SIM should be preferable 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

72 

**==> picture [412 x 435] intentionally omitted <==**

**----- Start of picture text -----**<br>
SIM CGM<br>10 [5]<br>10 [4]<br>m  = 0 . 05 10 [3]<br>10 [2]<br>10 [1]<br>10 [0] 10 4<br>10 2<br>10 [1]<br>10 [0]<br>10 [2]<br>10 [5]<br>10 [4]<br>m  = 0 . 5 10 [3]<br>10 [2]<br>10 [1]<br>10 [0] 10 4<br>10 2<br>10 [1]<br>10 [0]<br>10 [2]<br>10 [5]<br>10 [4]<br>m  = 0 . 95 10 [3]<br>10 [2]<br>10 [1]<br>10 [0] 10 4<br>10 2<br>10 [1]<br>10 [0]<br>10 [2]<br>105<br>104<br>103<br>102<br>101<br>100 10<br>101 10<br>102 100<br>105<br>104<br>103<br>102<br>101<br>100 10<br>101 10<br>102 100<br>105<br>104<br>103<br>102<br>101<br>100 10<br>101 10<br>102 100<br>4<br>2<br>4<br>2<br>4<br>2<br>Iteration count<br>Iteration count<br>Iteration count<br>**----- End of picture text -----**<br>


Figure 3.8: Six 3D surfaces are shown representing the number of iterations required for convergence for three values of _m_ for both the SIM and CGM algorithms. In each plot, the _x_ -axis represents the filter parameter _β_ , and the _y_ -axis represents the regularisation parameter _γ_ . The colourmap, which is normalised equally across all plots, tracks the vertical height. 

when the data is densely observed. 

## **3.4 Conclusions** 

In this chapter, we have addressed the problem of Graph Signal Reconstruction (GSR) on twodimensional undirected Cartesian product graphs. We began by reviewing existing literature on product graphs, including eigendecomposition of their respective Laplacians [Imrich and Klavˇzar, 

Chapter 3. _Regression and Reconstruction on Cartesian Product Graphs_ 

73 

2000] and discussed the significance of the Cartesian product in particular, which leads to a natural definition of the two-dimensional GFT. Given this, we proposed a formulation for anisotropic two-dimensional graph filters, which builds on the work of Ioannidis et al. [2016] who define the notion of ‘space-time kernels’ for time-varying graph signals, and the T-V framework of Grassi et al. [2018], Isufi et al. [2017], Loukas and Foucard [2016], where the authors discuss joint time-vertex filters. Our formulation provides a modest generalisation, by considering two generic graphs in the product, rather than one necessarily representing time. 

We then used the concept of anisotropic filters to define a Bayesian model for the reconstruction of signals on Cartesian product graphs. This extends related work on univariate GSR [Narang et al., 2013a, Romero et al., 2017b] and Time-Vertex GSR [Ioannidis et al., 2016, Qiu et al., 2017] by considering arbitrary undirected topologies for each factor graph. Our model assumes that the observed signal, **Y** _∈_ R _[N][×][T]_ is a partial observation of a smooth latent signal **F** , with white Gaussian noise. By specifying the expected frequency profile of **F** with a filter-based prior, the model output is a Gaussian posterior over the latent signal **F** . 

The posterior mean is naturally expressed as a linear system of size ( _NT × NT_ ). In order to solve this efficiently, we proposed specialised versions of the classic matrix splitting and conjugate gradient algorithms that leverage the Kronecker structure of the relevant matrices. This resulted in two alternative algorithms, namely the Stationary Iterative Method (SIM) and Conjugate Gradient Method (CGM) both of which can be solved with a complexity of _O_ ( _N_[2] _T_ + _NT_[2] ) per iterative step. In the case of the SIM, we also demonstrated how Chebyshev polynomials, which are often used in distributed GSP models [Shuman et al., 2018], can be leveraged to perform this in a distributed and/or eigendecomposition-free manner. 

In the latter part of this chapter, we focused on a detailed analysis of the convergence behaviour of the SIM and CGM. In particular, we considered how the number of iterations required for convergence is affected by the hyperparameters _β_ and _γ_ , and the proportion of missing data, _m_ . One key finding is that, while both algorithms experience slower convergence when the regularisation parameter _γ_ is small, the CGM has superior asymptotic performance as _γ →_ 0, with the number of iterations scaling as _γ[−]_[1] _[/]_[2] as compared to _γ[−]_[1] . We also investigated how the proportion of missing data, _m_ , impacts convergence. Interestingly, the SIM and CGM exhibit contrasting directional behaviour. Specifically, the CGM tends to be more suitable when the proportion of missing data is high, whereas SIM is generally preferable when it is low. 

## **Chapter 4** 

## **Multivariate Regression Models for Time-Varying Graph Signals** 

In this chapter, we focus on time-series regression models for graph signals. Specifically, our interest lies in the analysis of repeated measurements of a graph signal, where each sample is associated with a set of explanatory variables. The primary objective is to construct a predictive model capable of estimating these signals as a function of the aforementioned explanatory variables. Although regression has traditionally garnered less attention within the Graph Signal Processing (GSP) community compared to reconstruction, this framework holds significant relevance for numerous real-world applications. Consequently, it warrants further exploration and in-depth examination. 

In the subsequent discussion, we emphasise two distinct data scenarios that may emerge within the context of graph signal regression. In the first scenario, the explanatory variables are exogenous or ‘global’ with respect to the graph signals. In this setting, each graph signal **y** _t_ is accompanied by a feature vector **x** _t_ , which is global in the sense that it is associated with the entire signal rather than a specific node. For example, consider predicting the quarterly earnings growth for a network of firms based on economic factors such as interest rates, inflation, and unemployment. A visual representation of the data present in such a scenario can be found in fig. 4.1. 

In the second scenario under consideration, the explanatory variables are ‘local’ to the nodes of the graph signal. This implies that for each graph signal **y** _t_ , every node possesses an individual vector of explanatory variables **x** _nt_ . For instance, consider a network of air quality monitoring stations with the objective of predicting the concentration of a specific airborne pollutant. Each 

74 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

75 

**==> picture [380 x 64] intentionally omitted <==**

**----- Start of picture text -----**<br>
t  = 1 t  = 2 t  =  T<br>x 1 =  −− 010 . 97 .. 4728 y 1 = , x 2 =  −− 100 . 13 .. 3238 y 2 = , . . . x T =  100 ... 616432  y T =<br> 1 . 44   − 1 . 10  − 1 . 65<br>**----- End of picture text -----**<br>


Figure 4.1: A visual representation of a time-series graph signal regression problem with exogenous variables. Here, there are _T_ graph signals measured over a static graph, each with independent missing data (indicated in white with a red cross). Each signal **y** _t_ is accompanied by a unique vector of global explanatory variables **x** _t_ . 

station may simultaneously track various local factors, including temperature, pressure, precipitation, and so on. Figure 4.2 offers a visual depiction of the data encountered in this particular scenario. 

**==> picture [412 x 113] intentionally omitted <==**

**----- Start of picture text -----**<br>
t  = 1 t  = 2 t  =  T<br>[0 . 1 ,  1 . 1 ,  0 . 1] [0 . 2 ,  0 . 9 ,  0 . 0] [1 . 2 ,  0 . 3 ,  0 . 6]<br>[0 . 8 ,  0 . 4 ,  0 . 5] [0 . 4 ,  0 . 7 ,  0 . 8] [1 . 1 ,  0 . 0 ,  1 . 2]<br>[1 . 4 ,  1 . 2 ,  0 . 9] [1 . 1 ,  2 . 4 ,  0 . 4] [0 . 6 ,  1 . 1 ,  1 . 1] [0 . 9 ,  0 . 5 ,  0 . 9] [0 . 4 ,  0 . 0 ,  1 . 3] [1 . 5 ,  0 . 3 ,  0 . 4]<br>y 1 = [0 . 8 ,  0 . 7 ,  0 . 4] , y 2 = [0 . 3 ,  0 . 5 ,  0 . 7] , . . . y T = [2 . 1 ,  0 . 4 ,  0 . 6]<br>[0 . 3 ,  1 . 4 ,  0 . 1] [0 . 7 ,  0 . 1 ,  0 . 9] [1 . 5 ,  0 . 4 ,  1 . 1]<br>[1 . 4 ,  0 . 2 ,  0 . 1] [1 . 7 ,  0 . 1 ,  0 . 6] [0 . 1 ,  0 . 4 ,  1 . 6]<br>[1 . 0 ,  0 . 1 ,  0 . 2] [0 . 2 ,  1 . 7 ,  0 . 7] [1 . 1 ,  1 . 8 ,  0 . 2]<br>[0 . 5 ,  1 . 1 ,  0 . 6] [0 . 2 ,  0 . 9 ,  0 . 7] [0 . 5 ,  0 . 5 ,  1 . 5]<br>[0 . 8 ,  0 . 2 ,  2 . 2] [0 . 7 ,  0 . 0 ,  1 . 1] [1 . 1 ,  0 . 9 ,  0 . 5]<br>**----- End of picture text -----**<br>


Figure 4.2: A visual representation of a time-series graph signal regression problem with local explanatory variables. As before, there are _T_ graph signals measured over a static graph, each with independent missing data (indicated in white with a red cross). In this case, each signal **y** _t_ has a vector of explanatory variables **x** _nt_ for every node in the signal. 

The core goal of this chapter is to derive some useful extensions to existing methods for graph signal regression in both the local and global variable context. In the case of exogenous explanatory variables, we focus on Kernel Graph Regression (KGR) [Elias et al., 2022, Venkitaraman et al., 2019] and the closely related topic of Gaussian Processes over Graphs (GPoG) [Venkitaraman et al., 2020]. A notable issue in practice with existing KGR-type models is the assumption that the input signals **y** _t_ are always fully observed, meaning there is no missing data. As discussed in chapter 3, a prevalent characteristic of graph signals in real-world applications is the high occurrence of missing data. This situation forces the end user to either eliminate entire rows (i.e., the complete time series for a specific node) if any elements in the series are not recorded, which may result in the loss of valuable topological information or alternatively employ interpolation methods, which could prove inadequate for extended strings of missing data. Our proposed model accommodates fully general patterns of missing data in the input signals, enabling users to optimally utilise all available data. 

For the scenario involving local explanatory variables, we enhance a model known as Regression with Network Cohesion (RNC) [Le and Li, 2022, Li et al., 2019] by incorporating several beneficial 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

76 

extensions. Specifically, the original RNC model was designed for a single one-dimensional graph signal whereas the work presented in this chapter extends this to include multiple repeated samples of a graph signal over time, or a single measurement over a general Cartesian product graph. Moreover, the original specification did not account for the presence of missing data. Consequently, we advance the model in at least two significant directions. 

## **4.1 Kernel Graph Regression with Unrestricted Patterns of Missing Data** 

## **4.1.1 Model description** 

Consider a sequence of _T_ real-valued graph signals **y** _t ∈_ R _[N]_ measured over a static _N_ -node graph, for which an arbitrary subset of the elements of each signal may be missing, including potentially the entire signal at certain time points. At each time _t_ , there also exists a vector of variables **x** _t ∈_ R _[M]_ encompassing _M_ distinct explanatory features. Each graph signal may have unique and arbitrary missing data, as indicated by a binary vector **s** _t ∈{_ 0 _,_ 1 _}[N]_ , where ones represent successfully collected data and zeros signify missing data. Any absent data in **y** _t_ should be filled with zeros. Hence, the input data for this problem can be concisely described as follows. 

**==> picture [328 x 19] intentionally omitted <==**

In the following, we assume that the explanatory variables do not contain missing values. However, if any missing values are present, conventional methods such as those described in Little and Rubin [2019] can be employed to fill them. It should be noted that, with this model specification, there is no rigid distinction between in-sample and out-of-sample prediction. To indicate a particular value of **x** _t_ for which a comprehensive prediction should be generated, one can set the corresponding value of **y** _t_ = **s** _t_ = **0** . 

As in section 3.2.1, the graph signals can be stacked together into a matrix **Y** of shape ( _N × T_ ). Note that this is in contrast to the typical shape found in multivariate regression, which is most commonly ( _T × N_ ) with the index referring to each sample varying first, however, we adopt the opposite convention here for the reasons outlined section 3.1.3. 

Consider now a standard _P_ -dimensional basis function representation of each explanatory vector **x** _t_ , denoted as _**ϕ**_ ( **x** _t_ ) _∈_ R _[P]_ [Murphy, 2012]. 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

77 

**==> picture [299 x 21] intentionally omitted <==**

Let us assume that each element of **y** _t_ can be modelled as a noisy linear combination of these basis functions, which may or may not have been observed. This is summarised in the following statistical model. 

**==> picture [308 x 13] intentionally omitted <==**

Here, **W** _∈_ R _[N][×][P]_ represents the model coefficients defining the linear combination, such that each node _n_ has a unique set of regression weights at each row. In the context of a graph signal regression problem, we might expect that these weights vary smoothly between closely connected nodes. For example, in a geospatial problem, neighboring regions might share similar responses to the exogenous variables at each time **x** _t_ . Here, **e** _t ∈_ R _[N]_ is a vector of i.i.d. Gaussian noise with zero mean and unit variance. The basis function vectors can be horizontally stacked together to form a design matrix **Φ** . 

**==> picture [313 x 73] intentionally omitted <==**

Therefore, the statistical model can be written in matrix form as 

**==> picture [253 x 13] intentionally omitted <==**

where **S** _∈{_ 0 _,_ 1 _}[N][×][T]_ is the binary sensing matrix as defined in section 3.2.1, which is also each **s** _t_ stacked horizontally, and **E** _∈_ R _[N][×][T]_ is a matrix of i.i.d. Gaussian noise with zero mean and unit variance. This implies that the probability distribution for vec ( **Y** ) _|_ **W** is given by 

**==> picture [298 x 13] intentionally omitted <==**

To determine the posterior distribution of the model coefficients **W** , it is necessary to specify a prior that reflects the assumption that predicted signals are expected to be smooth with respect to the graph’s topology. We assert that an appropriate prior for **W** is given by 

**==> picture [278 x 14] intentionally omitted <==**

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

78 

Here, **H** _N ∈_ R _[N]_ represents a graph filter constructed in accordance with one of the univariate filter functions defined in table 2.1, while _γ_ serves as a hyperparameter denoting the prior precision. The rationale for this prior, as explicated in Venkitaraman et al. [2020], is as follows. Consider a random graph signal formulated as **W** _**ϕ**_ , where both **W** and _**ϕ**_ have Gaussian i.i.d. entries with zero mean and unit variance. The probability distribution of their product will also be an i.i.d. multivariate Gaussian with zero mean. By applying a graph filter **H** _N_ to smooth this signal, the resulting signal will exhibit the same probability distribution as **W** _**ϕ**_ , assuming **W** was drawn from the distribution specified in eq. (4.6). Consequently, this prior serves to enhance the likelihood of smooth signals. 

Consider now a transformed variable **F** defined by **F** = **WΦ** . Given that **W** has a prior distribution given in eq. (4.6), we can ask what the implied prior for **F** _|_ **Φ** is. Clearly, since the expected value of **W** is zero for all entries, the expected value of **F** should also be zero for all entries regardless of the value of **Φ** . The covariance of **F** can also be computed easily. 

**==> picture [212 x 114] intentionally omitted <==**

Therefore, we can rewrite the model in terms of the new transformed variable as follows. 

**==> picture [286 x 12] intentionally omitted <==**

**==> picture [286 x 19] intentionally omitted <==**

The final step to convert this into a non-parametric regression model is to apply the ‘kerneltrick’ [Scholkopf and Smola, 2018]. Consider the PSD matrix **Φ** _[⊤]_ **Φ** . Entry ( _i, j_ ) will be the inner product between the basis function expansion of **x** _i_ and **x** _j_ . 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

79 

**==> picture [363 x 73] intentionally omitted <==**

The trick is to characterise each inner product in terms of a predefined function such that _**ϕ**_ ( **x** _i_ ) _[⊤]_ _**ϕ**_ ( **x** _j_ ) = _κ_ ( **x** _i,_ **x** _j_ ). This means that instead of mapping the explanatory variables via _**ϕ**_ and computing the inner product directly, it is done in a single operation, leaving the mapping implicit. This means we can replace the matrix **Φ** _[⊤]_ **Φ** with a so-called kernel (or _Gram_ ) matrix **K** _∈_ R _[T][ ×][T]_ , which has entries defined by 

**==> picture [242 x 11] intentionally omitted <==**

where _κ_ ( _·, ·_ ) is any valid Mercer kernel [Rasmussen and Williams, 2005]. A common example is the Gaussian kernel given below. 

**==> picture [278 x 25] intentionally omitted <==**

Therefore, the prior distribution over **F** is given in terms of **K** by 

**==> picture [275 x 19] intentionally omitted <==**

In a similar manner to section 3.2.1, the posterior distribution for **F** _|_ **Y** is given by 

**==> picture [288 x 13] intentionally omitted <==**

where **P**[¯] is the posterior precision matrix for vec ( **F** ), given by 

**==> picture [261 x 13] intentionally omitted <==**

As before, **DS** = diag (vec ( **S** )). 

## **4.1.2 Relation to graph signal reconstruction** 

Despite arising from a different set of modelling assumptions, Kernel Graph Regression as described in section 4.1.1 bears a stark mathematical resemblance to Graph Signal Reconstruction. 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

80 

The only key difference between the specification of these two models is that in GSR, the prior distribution over vec ( **F** ) has covariance **H**[2] [see eq. (3.13)], and in KGR it has covariance **K** _⊗_ **H**[2] _N_ [see eq. (4.12)]. Intuitively speaking, the prior used in the GSR model encodes the belief that the underlying graph signal should be smooth with respect to the topology of the 2D Cartesian product graph. On the other hand, the prior used in the KGR model encodes the belief that the predicted signal should be smooth with respect to the topology of the 1D graph and the explanatory variables, i.e. graph signals **y** _i_ and **y** _j_ are expected to be similar if the vectors **x** _i_ and **x** _j_ are similar. 

As a result of the differences in their respective priors, the posterior precision matrix for vec ( **F** ) is given by **DS** + _γ_ **H** _[−]_[2] in the case of GSR and **DS** + _γ_ **K** _[−]_[1] _⊗_ **H** _[−] N_[2][in][the][case][of][KGR.][In][both] cases, it is the sum of **DS** and a Hermitian matrix. To make this correspondence clearer, we can expand the second term of each expression in terms of its respective eigendecomposition. For GSR, this is 

**==> picture [280 x 34] intentionally omitted <==**

where **U** = **U** _T ⊗_ **U** _N_ , and **DG** = diag (vec ( **G** )). For KGR this is 

**==> picture [308 x 37] intentionally omitted <==**

where **K** and **H** _N_ have eigendecompositions given by 

**==> picture [308 x 13] intentionally omitted <==**

with **Λ** _K_ = diag �� _λ_[(] 1 _[K]_[)] _, λ_[(] 2 _[K]_[)] _, . . . , λ_[(] _T[K]_[)] ��, **U**[¯] = **V** _⊗_ **U** _N_ and **DG** ¯ = diag �vec � **G** ¯ ��. **G**[¯] _∈_ R _[N][×][T]_ has elements given by 

**==> picture [327 x 21] intentionally omitted <==**

Therefore, KGR is algebraically equivalent to GSR under the following change of variables: 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

81 

**==> picture [108 x 11] intentionally omitted <==**

As such, the iterative algorithms developed in chapter 3 can be largely recycled with only minor modifications. However, it is important to bear in mind that the value of the maximum entry in **G** is one, whereas the maximum value in **G**[¯] is � _ρ_ ( **K** ). This has some implications for the SIM and CGM convergence rate, as explored in the following sections. 

## **4.1.3 Solving for the posterior mean** 

We now briefly restate the SIM and CGM algorithms to highlight the small changes necessary to accommodate KGR with arbitrary missing data. The goal is to solve the following linear system 

**==> picture [300 x 21] intentionally omitted <==**

First, let us revisit the SIM. Recall that the strategy is to split the coefficient matrix into **M** _−_ **N** , where **M** is easy to invert. In this case, we can put 

**==> picture [305 x 13] intentionally omitted <==**

where, as before, **DS** _′_ = diag ( **1** _−_ vec ( **S** )). Consider the matrix **M** _[−]_[1] . 

**==> picture [283 x 132] intentionally omitted <==**

¯ ¯ where **DJ** = diag �vec � **J** ��, and **J**[¯] _∈_ R _[N][×][T]_ has entries given by 

**==> picture [290 x 35] intentionally omitted <==**

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

82 

Note that it is still possible to implement this in an eigendecomposition-free manner, although the procedure is slightly more complex than it was in the case of GSR as discussed in section 3.2.2.1. First, we can approximate the function _g_[2] ( _λ_ ) using Chebyshev polynomials. This makes it possible to multiply **H**[2] _N_[onto vectors/matrices without the need to decompose the graph Laplacian.] Next, approximate the function _J_ ( _x_ ) = _x/_ ( _x_ + _γ_ ) using a separate set of Chebyshev polynomials. This makes it possible to approximate the function of a matrix _J_ ( **A** ) = ( _γ_ **A** _[−]_[1] + **I** ) _[−]_[1] . By setting the matrix **A** = **K** _⊗_ **H**[2] , and computing the relevant action of the **H**[2] portion using the original set of polynomials, we can achieve the application of **M** _[−]_[1] onto a vector whilst avoiding eigendecomposition. 

The SIM algorithm then proceeds in much the same way as described in section 3.2.2. As before, it is clear to see that convergence will be achieved, since the spectral radius of **M** _[−]_[1] **N** will surely be less than one for any positive _γ_ . In this case, the update formula is given by 

**==> picture [287 x 14] intentionally omitted <==**

**==> picture [325 x 14] intentionally omitted <==**

Note that each update step can be performed with _O_ ( _N_[2] _T_ + _NT_[2] ) multiplications. 

Next, let us return to the CGM. Recall that the strategy for solving the linear system in eq. (4.17) is to utilise a symmetric preconditioner **Ψ** such that the new system is given by 

**==> picture [340 x 19] intentionally omitted <==**

**Ψ** ¯ should be chosen such that new coefficient matrix **Ψ** ¯ _[⊤]_[�] **DS** + _γ_ **K** _[−]_[1] _⊗_ **H** _[−] N_[2] � **Ψ** ¯ has a reduced condition number. In the present case, we assert that an effective preconditioner is given by 

**==> picture [296 x 13] intentionally omitted <==**

This preconditioner transforms the coefficient matrix into 

**==> picture [365 x 60] intentionally omitted <==**

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

83 

Note that we can efficiently compute the action of multiplying this preconditioned matrix onto an arbitrary vector vec ( **R** ) _∈_ R _[NT]_ as follows. 

**==> picture [370 x 19] intentionally omitted <==**

As with the SIM, this action can be performed with _O_ ( _N_[2] _T_ + _NT_[2] ) multiplications. 

## **4.2 Regression with Network Cohesion** 

## **4.2.1 Model description** 

In this model, we consider a sequence of _T_ real-valued signals, which are regularly sampled over a static _N_ -node graph and may contain arbitrary missing values. As with KGR and GSR, this is represented using an ( _N × T_ ) matrix **Y** , with missing values set to zero and further clarified with the binary sensing matrix **S** _∈{_ 0 _,_ 1 _}[N][×][T]_ which holds zeros at entries where the corresponding element of _Y_ is missing data and ones elsewhere. In this model each node, _n_ , at each time instant, _t_ , under consideration, has an associated length- _M_ vector of explanatory variables **x** _nt ∈_ R _[M]_ . The objective is to make use of both the node-level explanatory variables and the network topology to estimate the missing values in the graph signal. A visual depiction of the data available in this kind of scenario is given in fig. 4.2. 

**==> picture [341 x 18] intentionally omitted <==**

Here, we have introduced the notation _**X**_ , which is an order-3 tensor, which has three independent axes signifying node number _n_ , time instant _t_ , and covariate number _m_ , respectively. In the following sections, we index/slice this tensor of explanatory variables, _**X**_ , in various ways, therefore, it is beneficial to establish some notational standards for this purpose. In general, we adhere to the conventions outlined in Kolda and Bader [2009], which are also similar to those found in Kiers [2000]. 

To refer to an individual element of an order-3 tensor (i.e. a scalar entry), we use the notation _**X** ntm_ . The object generated by fixing two indices and letting a third vary (resulting in a vector) is referred to in this context as a fibre. Using tensor notation, the vector of covariates **x** _nt ∈_ R _[M]_ , which exists at every node, at every time point, can alternatively be written as _**X** nt_ :. A twodimensional section of a tensor (i.e. a matrix), where two indices can vary and a single index is fixed, is known as a slice. For example, we could consider the slice given by a specific covariate measured across the whole graph, at every time instant, for which we would use the notation 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

84 

**==> picture [189 x 328] intentionally omitted <==**

**----- Start of picture text -----**<br>
T<br>M Atopy<br>N<br>jviaiaiat<br>SF<br>‘imlmimtinl<br>X Xntm<br>Xn :: X : t : X :: m<br>X : tm Xn : m Xnt :<br>**----- End of picture text -----**<br>


Figure 4.3: A visual representation of several different ways of indexing into an order3 tensor, with the corresponding notation indicated. 

_**X**_ :: _m_ . Figure 4.3 gives a visual representation of several ways of indexing/slicing an order-3 tensor. 

For the purposes of this section, we also define the special matrix **X** , which is constructed by horizontally stacking the _M_ vectorized slices _**X**_ :: _m_ , resulting in an object of shape ( _NT × M_ ). 

**==> picture [331 x 13] intentionally omitted <==**

In this section, we consider several extensions to a model known as Regression with Network Cohesion (RNC) [Li et al., 2019]. In our version of the model, we assume that every element of the observed graph signal **Y** can be represented as the sum of an intercept term, a linear combination of the node-level covariates, and some Gaussian noise. However, the intercept term is flexible in the sense that each node/time can have a distinct value. To avoid underspecification, the model postulates that the intercepts are smooth with respect to the graph’s topology. This is represented as follows. 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

85 

**==> picture [308 x 13] intentionally omitted <==**

In this context, **C** _∈_ R _[N][×][T]_ represents the flexible intercept term, **w** _∈_ R _[M]_ the vector of regression coefficients, and **E** _∈_ R _[N][×][T]_ a matrix of independent and identically distributed Gaussian noise with unit variance. The key assumption of the RNC model is that the intercept term **C** is smooth with respect to the topology of the entire _T − V_ Cartesian product graph. Furthermore, the above expression can be restated in terms of a single model coefficient vector _**θ**_ , by making use of the definition of **X** _∈_ R _[NT][ ×][M]_ given in eq. (4.25), as follows. 

**==> picture [302 x 19] intentionally omitted <==**

where � **I** _NT_ **X** � _∈_ R _[NT][ ×]_[(] _[NT]_[ +] _[M]_[)] is a block matrix consisting of the ( _NT × NT_ ) identity matrix alongside **X** , and _**θ**_ is the block vector consisting of vec ( **C** ) stacked on top of **w** , that is, 

**==> picture [264 x 37] intentionally omitted <==**

Given eq. (4.27), we can write the probability distribution for **Y** _|_ _**θ**_ as follows. 

**==> picture [331 x 19] intentionally omitted <==**

In order to complete the specification of the Bayesian model, we need a prior distribution for _**θ**_ . In this case, we can independently combine both a graph-spectral prior for the vec ( **C** ) section and an L2 prior for the **w** section. This can be written as follows. 

**==> picture [280 x 37] intentionally omitted <==**

Here, **H** _∈_ R _[NT][ ×][NT]_ is a graph filter defined to act over the entire T-V product graph. This block matrix including **H** and **I** _M_ both encodes the smoothness assumption for the flexible intercept term and provides regularisation for the regression coefficients **w** . Given this, the posterior distribution over _**θ**_ is given by 

**==> picture [294 x 37] intentionally omitted <==**

where 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

86 

**==> picture [338 x 36] intentionally omitted <==**

A proof of this is given in theorem A.6. As before, **DS** = diag (vec ( **S** )). 

## **4.2.2 Solving for the posterior mean** 

In the case of RNC, there is no simple or convenient way to reuse the SIM method to solve for the posterior mean. To see this, consider splitting the matrix **P**[�] into **M** _−_ **N** where 

**==> picture [294 x 37] intentionally omitted <==**

Recall that each iterative step in the SIM requires the multiplication of a vector by **M** _[−]_[1] **N** . Although **M** remains easy to invert, the spectral radius, _ρ_ ( **M** _[−]_[1] **N** ) is no longer guaranteed to be less than one, resulting in a potential lack of convergence. This issue is not unique to a specific permutation of **M** and **N** , but rather persists across multiple arrangements. 

On the other hand, we can find an effective preconditioner **Ψ**[�] _∈_ R[(] _[NT]_[ +] _[M]_[)] _[×]_[(] _[NT]_[ +] _[M]_[)] for use with the CGM, which transforms the linear system as follows. 

**==> picture [381 x 37] intentionally omitted <==**

To obtain a suitable value for **Ψ**[�] , first let us define the eigendecomposition of **X** _[⊤]_ **DSX** . 

**==> picture [260 x 12] intentionally omitted <==**

Since **X** _[⊤]_ **DSX** is positive semi-definite, **U** _M_ can be chosen to be orthonormal. Next, let us also introduce the diagonal matrix **D** _M_ , which has the following definition 

**==> picture [262 x 16] intentionally omitted <==**

We propose that an effective preconditioner is given by 

**==> picture [261 x 37] intentionally omitted <==**

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

87 

where, as before, **U** = **U** _T ⊗_ **U** _N_ . We chose this preconditioner because it transforms the blockdiagonal elements of the original coefficient matrix **P**[�] into matrices with eigenvalues bounded between 1 + _γ_ and _γ_ . In particular, the new coefficient matrix is given by 

**==> picture [267 x 37] intentionally omitted <==**

Note that the upper left block can be multiplied onto a length _NT_ vector with complexity _O_ ( _N_[2] _T_ + _NT_ log _T_ ), by leveraging the properties of the Kronecker product and making use of the Fast Cosine Transform (FCT). The upper right block of this matrix consists of _M_ length- _NT_ column vectors, which can be computed with complexity _O_ ( _MN_[2] _T_ + _MNT_ log _T_ ) and multiplied onto a length _M_ vector with complexity _O_ ( _NTM_ ). This also applies to the lower left block, which is the transpose of the upper right, and can be multiplied onto a length _M_ vector in the same number of operations. Finally, the lower right block can be multiplied onto a length _M_ vector with _M_ operations. Therefore, the overall complexity of multiplying the entire matrix onto a vector of length _NT_ + _M_ is _O_ ( _N_[2] _T_ + _NT_ log _T_ ). 

## **4.3 Network regression with both global and local explanatory variables** 

In section 4.1, we introduced Kernel Graph Regression (KGR) with arbitrary missing values as a non-parametric regression technique, applicable for modelling scenarios where a series of graph signals need to be predicted based on exogenous or ‘global’ explanatory variables. This concept is visually represented in fig. 4.1. On the other hand, Regression with Network Cohesion (RNC), discussed in section 4.2, is suitable for situations where ‘local’ explanatory variables are associated with individual nodes over time, as depicted in fig. 4.2. 

In certain cases, both global and local explanatory variables may coexist. For example, consider a network of businesses where firms are connected based on industry similarity or supply chain integration. In this scenario, the objective may be to predict quarterly revenue growth using variables affecting all firms, such as inflation and interest rates, while also considering firm-level local variables like employee turnover or debt ratio. 

The input data in such a scenario can be summarised as follows 

**==> picture [386 x 19] intentionally omitted <==**

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

88 

Once again, **Y** is a sequence of partially observed graph signals and **S** is the corresponding binary sensing matrix defining which values are missing. _**X**_ represents the tensor of local explanatory variables, where each node at each time has an associated length- _M_ feature vector. In the example, this would represent the firm-level variables such as employee turnover and debt ratio. **X** _[′]_ is the matrix of global explanatory variables, where the _t_ -th row represents the global length- _M[′]_ feature vector at each time _t_ . In this section we also continue to use the notation **X** (without the prime) to denote the matrix which is constructed by horizontally stacking the _M_ vectorized slices _**X**_ :: _m_ , resulting in an object of shape ( _NT × M_ ), as defined in eq. (4.25). 

Leveraging the methods developed for KGR and RNC in sections 4.1 and 4.2, we can naturally integrate both _**X**_ and **X** _[′]_ into the problem. The RNC model supposes that the observed graph signal is a noisy partial observation of a smooth underlying signal **C** added to a regularised linear combination of node-level covariates. Therefore, RNC combines aspects of graph signal reconstruction and ridge regression. As discussed in section 4.1.2, KGR can be understood as a small modification of the graph signal reconstruction problem, where the underlying signal **F** is instead assumed to be smooth with respect to both the 1D network and the explanatory variables, rather than a 2D Cartesian product graph. This involved altering the prior distribution over **F** to include the kernel matrix **K** which is a function of the global variables **X** _[′]_ , as defined in eq. (4.10). 

Similarly, we can modify the prior over the flexible intercept term **C** in the RNC model. Instead of using a prior covariance of _γ_ **H**[2] , we can employ a covariance matrix _γ_ **K** _⊗_ **H**[2] _N_[,][where] **[K]**[is] the kernel matrix and **H** _N_ is a graph filter acting upon the 1D network, as in the KGR model. Since the RNC model is defined in terms of the aggregate parameter vector _**θ**_ , we can adjust its prior distribution accordingly. 

**==> picture [292 x 37] intentionally omitted <==**

Just as with KGR, this new model, which we refer to as Kernel Graph Regression with Network Cohesion (KG-RNC), is algebraically equivalent to the RNC model under the transformation 

**==> picture [108 x 11] intentionally omitted <==**

where **K** has an eigendecomposition **VΛ** _K_ **V** _[⊤]_ and **U**[¯] and **G**[¯] are defined by 

**==> picture [329 x 22] intentionally omitted <==**

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

89 

Given the prior for _**θ**_[ˆ] in eq. (4.37), and the likelihood which is identical to that of the RNC model given in eq. (4.29), the posterior distribution is given by 

**==> picture [294 x 37] intentionally omitted <==**

where 

**==> picture [354 x 37] intentionally omitted <==**

Once again, we can solve the linear system for the mean using the CGM, with a symmetric preconditioner **Ψ**[ˆ] . 

**==> picture [397 x 37] intentionally omitted <==**

where 

**==> picture [261 x 37] intentionally omitted <==**

The new preconditioned coefficient matrix in this case is given by 

**==> picture [267 x 36] intentionally omitted <==**

which can be efficiently multiplied onto a length _NT_ + _M_ vector by leveraging the properties of the Kronecker product. Note that, in this case, the complexity of this multiplication is no longer _O_ ( _N_[2] _T_ + _NT_ log _T_ ), but is now _O_ ( _N_[2] _T_ + _NT_[2] ), since we cannot make use of the Fast Cosine Transform to multiply the matrix **V** _⊗_ **U** onto a vector. 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

90 

## **4.4 Network regression for pollutant monitoring** 

In this section, we give an illustrative example application for the regression models developed in this chapter by applying them to an environmental modelling task. Here, the aim is to check the models produce sensible output, and to gain some insight into their behaviour. Our focus is on predicting the mean daily concentration of PM2 _._ 5, a common airborne pollutant which consists of particulate matter with a diameter of 2.5 micrometres or less. We apply our models to data taken from a network of monitoring stations located in California, obtained from the U.S. Environmental Protection Agency’s Air Data program. This program is responsible for generating daily readings of several airborne pollutants, including Ozone, Sulfur Dioxide (SO2), Carbon Monoxide (CO), Nitrous Dioxide (NO2), PM2 _._ 5 and PM10 at many locations across the U.S. [EPA, 2023]. 

In total, we consider _N_ = 571 monitoring stations across a period of _T_ = 3957 days from the 1[st] of January 2012 to the 30[th] of September 2022. Our method for graph construction was as follows. First, we took the latitude and longitude coordinates of each station and created a twodimensional Voronoi diagram bounded by the California border [Fortune, 1986]. This tessellated the whole region into 571 distinct sub-regions; one per station. Next, we connected each pair of stations ( _i, j_ ) if their respective Voronoi regions shared a boundary, and weight that connection by 1 _/_ (1 + _dij_ ), where _dij_ is their geodesic separation in kilometres. This creates a sparse graph, which is visually represented in fig. 4.4. 

In our experiments, we predicted log(1 + _c_ ) (to reduce skewness [West, 2022]), where _c_ was the concentration of PM2 _._ 5 in parts per million, across the network using all three regression algorithms outlined in this chapter. In the case of Kernel Graph Regression, we used a set of exogenous environmental variables such as season and active wildfires (see table 4.1). For Regression with Network Cohesion, we used local explanatory variables such as measurements of the other pollutants and land use (see table 4.2). For Kernel Graph Regression with Network Cohesion, we used both sets of variables. All explanatory variables were lagged by one day, such that predictions were being made on data collected 24 hours previously. 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

91 

**==> picture [272 x 429] intentionally omitted <==**

Figure 4.4: The network of monitoring stations, created via Voronoi tessellation. The geographic coordinates of the stations are used to create closed regions, which are connected by a weighted edge to neighbouring regions. The colours are for visual clarity only and do not represent a graph signal colour-map. 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

92 

## **Exogenous explanatory variables** 

|**Variable**|**Description**|
|---|---|
|Time|A simple linear variable.|
|Season|Two additional variables tracking season were created by taking|
||the sin and cosine of 2_πt/_365, where _t_ is the day of the year.|
|Active wildfres|The original dataset comprised a list of wildfre events in Cali-|
||fornia, containing information including the geographical coordi-|
||nates, the start date, the end date and the total number of acres|
||burned. Using the coordinates, we assigned each fre to one of nine|
||regions. Then, by dividing the total acres burned by the incident|
||duration, we calculated the average number of acres burning each|
||day for each fre. By summing this for every region, we had an|
||estimate of the total number of acres burning on each day for each|
||region.|
|Temperature|Using data from the Air Data program, we obtained readings for|
||temperature at 90 locations across California. The readings were|
||selected such that no missing data was present. Then, the frst|
||fve principal components were taken.|
|Pressure|As above, but for pressure. Readings from 48 locations were trans-|
||formed into fve PCA components.|
|Humidity|As above, for humidity. Readings from 51 locations were trans-|
||formed into fve PCA components|



Table 4.1: The exogenous (global) explanatory variables used in this experiment. Each feature is not associated with any node in particular but covaries with the graph signal over time. This resulted in a feature matrix **X** of shape 3957 _×_ 27. All columns were normalised to have a mean of zero and a standard deviation of one. All data was lagged by one day relative to the target variable **Y** . 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

93 

||**Endogenous explanatory variables**|
|---|---|
|**Variable**|**Description**|
|Ozone|Ozone readings, transformed via log(1 +_x_), from the Air Data|
||program were taken at all 571 monitoring stations. Where data|
||was missing, graph signal reconstruction was used to interpo-|
||late the missing values. 72% of the original data was missing.|
|Sulfur Dioxide|As above. 95% of the original data was missing.|
|Carbon Monoxide|As above. 89% of the original data was missing.|
|Nitrous Dioxide|As above. 83% of the original data was missing.|
|PM10|As above. 85% of the original data was missing.|
|Elevation|The elevation of the station in meters. This variable remained|
||constant over time|
|Land use|Each monitoring station had a land use fag, which was one|
||of ‘Commercial’, ‘Residential’, ‘Agricultural’, ‘Forest’, ‘Indus-|
||trial’, ‘Desert’, or ‘Military Reservation’. This was turned into|
||a length-7 vector for each station using one-hot encoding which|
||remained constant over time.|
|Location setting|Each station also had a location fag, which was one of ‘Urban|
||And Center City’, ‘Suburban’ or ‘Rural. In the same fashion as|
||above, we created a one-hot encoding for each station, which|
||remained constant over time.|



Table 4.2: The endogenous (local) explanatory variables used in this experiment. Each variable is associated with a monitoring station and also varies over time. For elevation, land use and location setting which are fixed for each station, the values are simply repeated over time. This created an explanatory tensor _**X**_ of shape 571 _×_ 3957 _×_ 16. All data was lagged by one day relative to the target variable **Y** . Note that the first five variables listed here vary over time, wheras the final three remain static over time. 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

94 

Stations ( _N_ = 571) 

**==> picture [15 x 102] intentionally omitted <==**

**----- Start of picture text -----**<br>
= 3957)<br>T<br>(<br>Time<br>**----- End of picture text -----**<br>


Figure 4.5: The structure of the missing data in **Y** 0 is represented visually. Black indicates data that is present, and white indicates areas of missing data. As visible, many stations have no data recorded at all (inactive). Others have the majority of their data present, and some have data recoded for only short periods of time (active). 

The original graph signal, **Y** 0 _∈_ R _[N][×][T]_ , had 88% of its elements missing. The structure of the mising data is shown visually in fig. 4.5. To create a training set **Y** , we removed the entire time series from 20% of the active stations, assigning 10% to a validation set and 10% to a test set. Next, we solved each model using this reduced training set and tuned all relevant hyperparameters by minimising the validation error using an out-of-the-box Nelder-Mead optimisation algorithm [Gao and Han, 2010]. Finally, we made a prediction for each model, and measured the Root Mean Square Error (RMSE) and _R_[2] statistic across the training, validation and test nodes. 

In addition to the KGR, RNC and KG-RNC algorithms discussed, we also tested univariate and multivariate ridge regression using the endogenous and exogenous explanatory variables respectively. However, since multivariate ridge regression has no standard approach for the situation where values are missing from the multivariate targets, we first filled in these values according to the mean reading at each station. Where no readings were available at all at a particular station, we used the mean reading across time. Note that the univariate ridge regression algorithm is effectively equivalent to RNC, but with an intercept that is fixed for each node rather than flexible. The ridge regularisation parameter for each algorithm was also tuned on the validation set, using a simple line search. The results are shown in table 4.3. 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

95 

||RMSE<br>Train<br>Validation<br>Test|_R_2|
|---|---|---|
|||Train<br>Validation<br>Test|
|KGR<br>RNC<br>KG-RNC<br>Ridge (global)<br>Ridge (local)|0.315<br>0.444<br>0.457<br>0.300<br>0.427<br>0.388<br>0.210<br>0.443<br>0.387<br>0.483<br>0.599<br>0.602<br>0.515<br>0.527<br>0.482|0.782<br>0.494<br>0.504<br>0.803<br>0.532<br>0.643<br>0.903<br>0.497<br>0.643<br>0.487<br>0.079<br>0.139<br>0.418<br>0.288<br>0.448|



Table 4.3: The Root Mean Square Error and _R_[2] statistic are shown for the five models on the train, validation and test sets. 

As visible, RNC and KG-RNC demonstrate similar performance and generally obtain the highest accuracy, whilst KGR outperforms both ridge regression models. Of these, ridge regression with endogenous (local) variables achieves lower error than ridge regression with exogenous (global) variables. Given that 88% of the data in **Y** 0 was missing, it is no surprise that global ridge regression produces poor performance, since the vast majority of its training data was produced via the simple mean-filling heuristic. 

The fact that RNC achieves significantly better performance than the local ridge model is strong evidence that the topological information expressed in the flexible intercept term provides additional predictive ability. Figure 4.6 shows the prediction made by each model over a six-month period, at one of the monitoring stations in the test set. As visible, KGR, RNC and KG-RNC all produce predictions that are broadly in line with the ground truth. On close inspection, it is also clear that the RNC and KG-RNC algorithms make very similar predictions, although there are some small deviations. 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

96 

**==> picture [376 x 397] intentionally omitted <==**

**----- Start of picture text -----**<br>
3<br>2<br>KGR<br>1<br>3<br>2<br>RNC<br>1<br>3<br>2<br>KG-RNC<br>1<br>3<br>2<br>Ridge (global)<br>1<br>3<br>2<br>Ridge (local)<br>1<br>Aug Sep Oct Nov Dec Jan<br>2022<br>**----- End of picture text -----**<br>


Figure 4.6: The predictions made over time by each model (orange) are plotted against the ground truth (dashed blue) at a particular node where no input data was collected. 

**??** shows a colour-map of the prediction made by each algorithm on the 27th of September 20154 (the 1000th day in the dataset). Some notable features are that, while the KGR model produces an output that is clearly smooth with respect to the graph topology, the RNC and KG-RNC algorithms are less visibly smooth. This indicates that, for these models, the contribution of the local explanatory variables is dominating over the flexible intercept term. This is further corroborated by the fact that the predictions from the RNC and KG-RNC models look visibly similar to the local ridge model. This is as expected, since the local ridge model is equivalent to the RNC model but with a fixed intercept and, as established, the flexible intercept seems 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

97 

to be playing a less significant role than the local variables. However, as evidenced by the numerical performance detailed in table 4.3, clearly the additional flexibility afforded by this term is valuable in enhancing the predictive capability. 

**==> picture [334 x 351] intentionally omitted <==**

**----- Start of picture text -----**<br>
Ground truth KGR RNC<br>KG-RNC Ridge (global) Ridge (local)<br>**----- End of picture text -----**<br>


Figure 4.7: A colourmap of the predictions made across all regions by each model on an arbitrary date (27th of September 2014.) 

## **4.5 Conclusions** 

In this chapter, we have addressed the topic of multivariate graph signal regression with arbitrary missing data. We began by distinguishing between two modelling scenarios that have appeared in the literature on graph signal regression. The first involves predicting a series of graph signals _{_ **y** _t}_ , given a series of covariates _{_ **x** _t}_ , which we refer to as _exogenous_ explanatory variables. The second involves predicting a single graph signal **y** , where each node has an associated covariate vector **x** _n_ , which we refer to as _endogenous_ explanatory variables. The models presented in this chapter represent extensions to existing work, most notably Kernel Graph Regression (KGR) 

Chapter 4. _Multivariate Regression Models for Time-Varying Graph Signals_ 

98 

and Gaussian Processes over Graphs (GPoG) for the former [Venkitaraman et al., 2020, 2019], and Regression with Network Cohesion (RNC) for the latter [Li et al., 2019]. 

Our primary contribution to the problem of exogenous graph signal regression is to accommodate the case where arbitrary missing data exists in the input signals _{_ **y** _t}_ , which is a common feature of real-world GSP applications. Whilst in Venkitaraman et al. [2020, 2019] the model admits a closed-form solution that can be directly computed via Gaussian elimination, the introduction of missing data in our model makes it necessary to resort to iterative approaches. By highlighting the algebraic similarities to GSR, we demonstrate how the SIM and CGM algorithms developed in the previous chapter can be reappropriated for this purpose with minor modifications. 

Next, we take the RNC model for endogenous explanatory variables developed in Li et al. [2019], which was originally defined for univariate graph signals, and generalise it to signals on two-dimensional Cartesian product graphs. We also extend RNC by incorporating flexible filter-based priors, whereas the original only included a total square variation Laplacian penalty term. Again, this requires an iterative approach to compute the posterior mean, however, in this case, we find that only the CGM can be utilised. By making use of block-Kronecker-structured preconditioner, we present a modified version of the CGM applicable to RNC. 

Finally, we propose a hybrid model that combines aspects of both KGR and RNC, which we term KG-RNC, where both exogenous and endogenous explanatory variables coexist to aid in the estimation process. This model is also applicable for arbitrary missing data, and we find that it achieves similar performance and produces similar output to the RNC model in our case study using data collected from air monitoring stations. 

## **Chapter 5** 

## **Regression and Reconstruction with Tensor-Valued Multiway** 

## **Graph Signals** 

Multiway Graph Signal Processing (MWGSP) is an emerging framework for analysing signals with multiple distinct axes (or ‘ways’), where the relation between elements within each axis is described by a graph topology [Stanley et al., 2020]. For example, consider an fMRI experiment where cerebral blood flow is measured at a set of 3D voxels across time, for multiple subjects, in response to various stimuli. This dataset could be modelled as a six-way graph signal with the three spatial coordinates and the one time coordinate forming a four-way hypergrid graph, the subjects forming a graph based on characteristics, and the stimuli forming a graph based on similarity [Cichocki et al., 2015]. A visual depiction of this is given in fig. 5.1. 

**==> picture [301 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
Stimulus 3<br>Subject 3<br>Subject 2<br>⊗ time ⊗ N ar ⊗ Stimulus 1 O Stimulus F 2<br>Subject 1<br>**----- End of picture text -----**<br>


Figure 5.1: Graphical depiction of a six-way graph signal originating from a hypothetical fMRI experiment. 

99 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

100 

The goal of this chapter is to extend the methods developed in chapters 3 and 4 such that they can accommodate multiway graph signals. In particular, Graph Signal Reconstruction (GSR), Kernel Graph Regression (KGR) and Regression with Network Cohesion (RNC) can all be understood as a special two-dimensional case of their more general MWGSP counterpart. In this chapter, we translate all three models into their _d_ -dimensional form and demonstrate how to solve efficiently for the posterior mean. 

Multiway signals are described using tensors, which can be represented as _d_ -dimensional arrays. Tensor algebra is well-established in fields such as physics and mechanics [Renteln, 2013], however, it is less widespread in the GSP community. As such, the first section of this chapter sets out some conceptual and notational standards regarding tensors, which are core to the present and proceeding chapters. 

We begin section 5.1 by defining the Cartesian product of more than two graphs, and discuss the algebraic and spectral structure of the resultant objects. Next, we cover the tensor representation of multiway graph signals and give the general definition of graph-spectral operators in _d_ -dimensions. We also discuss issues surrounding computational efficiency and how the so-called ‘vec-trick’, utilised in prior chapters, can be generalised to the tensor setting. In section 5.2, we begin the core contributions of this chapter by generalising Bayesian GSR as defined in chapter 3 to the MWGSP setting. This necessitates an updated version of the SIM and CGM to accommodate tensor-valued data in arbitrary dimensions, which we give in sections 5.2.1 and 5.2.2. Next, in section 5.3, we generalise KGR for the non-parametric prediction of multiway graph signals as a function of exogenous variables. Finally, in section 5.4, we generalise RNC as defined in section 4.2 in much the same way. 

## **5.1 Multiway Graph Signal Processing** 

## **5.1.1 The Cartesian product of more than two graphs** 

In section 3.1.1 we gave the general definition of a product between two graphs and highlighted four standard examples, namely the Cartesian, direct, strong and lexicographic products. Each of these product types can be straightforwardly extended to more than two factor graphs by applying their respective definition recursively. For example, consider the Cartesian product between graphs _GA_ = _{VA, EA}_ , _GB_ = _{VB, EB}_ and _GC_ = _{VC, EC}_ where _|VA|_ = _A_ , _|VB|_ = _B_ and _|VC|_ = _C_ . This can be written as 

**==> picture [276 x 11] intentionally omitted <==**

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

101 

**==> picture [416 x 255] intentionally omitted <==**

**----- Start of picture text -----**<br>
GA GB GC<br>**----- End of picture text -----**<br>


Figure 5.2: Graphical depiction of a 3D Cartesian product graph 

The new vertex set, _V_ , is given by the Cartesian product of the individual vertex sets, arranged in lexicographic order. 

**==> picture [347 x 12] intentionally omitted <==**

The new edge set, _E_ , is given by recursively applying conditions 1 and 7 from, section 3.1.1 to the new node set. In particular, any two nodes ( _a, b, c_ ) and ( _a[′] , b[′] , c[′]_ ) are connected in _E_ if they satisfy any of the following three conditions. 

**==> picture [259 x 53] intentionally omitted <==**

Figure 5.2 gives a visual representation of a Cartesian product graph formed from three simple factor graphs. Notice that the size of the new vertex and edge set both grow very quickly. In particular, 

**==> picture [330 x 11] intentionally omitted <==**

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

102 

Happily, the adjacency matrix of a Cartesian product graph **A** has a straightforward representation in terms of the factor adjacency matrices (here **A** _A_ , **A** _B_ and **A** _C_ ). Specifically, it is given by their Kronecker sum. 

**==> picture [324 x 31] intentionally omitted <==**

In general, we can consider the Cartesian product of _d_ factor graphs with adjacency matrices denoted as **A**[(1)] _∈_ R _[N]_[1] _[×][N]_[2] _,_ **A**[(2)] _∈_ R _[N]_[2] _[×][N]_[2] _, . . ._ **A**[(] _[d]_[)] _∈_ R _[N][d][×][N][d]_ . The full adjacency matrix will have size _N × N_ , where _N_ =[�] _Ni_ , and is given by 

**==> picture [294 x 84] intentionally omitted <==**

This can be written compactly as 

**==> picture [237 x 30] intentionally omitted <==**

Similarly, the Laplacian of the product graph, **L** , can be written as the Kronecker sum of the individual factor graph Laplacians **L**[(] _[i]_[)] . 

**==> picture [235 x 30] intentionally omitted <==**

We can perform eigendecomposition on each of the individual graph Laplacians as follows. 

**==> picture [259 x 12] intentionally omitted <==**

where **U**[(] _[i]_[)] is an orthogonal matrix such that each column is an eigenvector of **L**[(] _[i]_[)] , and **Λ**[(] _[i]_[)] is a diagonal matrix containing the corresponding eigenvalues, which are typically listed in ascending order. 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

103 

**==> picture [136 x 73] intentionally omitted <==**

Given this, the Laplacian of the product graph can be decomposed as follows. 

**==> picture [301 x 99] intentionally omitted <==**

where 

**==> picture [286 x 30] intentionally omitted <==**

As with the Kronecker sum, here we have used the notation[�] _[d] i_ =1 **[U]**[ (] _[i]_[)][to][denote][the][chained] Kronecker product of matrices _{_ **U**[(] _[i]_[)] _}_ . 

## **5.1.2 Representing** _**d**_ **-dimensional graph signals** 

Since each node in a _d_ -dimensional product graph is specified by _d_ independent indices, a signal, _**Y**_ , existing over the nodes has a natural representation as a tensor of order _d_ . One way to conceptualise a _d_ -dimensional tensor signal is as a multi-dimensional array with _d_ independent axes. If the _i_ -th factor graph has _Ni_ vertices, then _**Y**_ will be of shape ( _N_ 1 _, N_ 2 _, ...Nd_ ). An individual element of this tensor signal can be specified via a vector index **n** = [ _n_ 1 _, n_ 2 _, ..., nd_ ], where 1 _≤ ni ≤ Ni_ . 

Alternatively, tensor signals have a dual representation as a vector of length _N_ =[�] _Ni_ . This is essential if we are to interpret the _⊗_ symbol strictly as a Kronecker product, rather than a tensor or outer product. Under the Kronecker interpretation, the chained use of _⊗_ used in expressions such as eq. (5.9) results in matrices of shape _N × N_ , providing a linear map from R _[N] →_ R _[N]_ . Therefore, for an operator to act on a tensor graph signal _**Y** ∈_ R _[N]_[1] _[×][N]_[2] _[×][...][×][N][d]_ , we need a method of mapping tensors with shape ( _N_ 1 _, N_ 2 _, ...Nd_ ) to vectors of length _N_ . In 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

104 

|_n_1<br>_n_2<br>_n_3<br>(1_,_1_,_3)<br>(1_,_2_,_3)<br>(1_,_3_,_3)<br>(1_,_4_,_3)<br>(2_,_1_,_3)<br>(2_,_2_,_3)<br>(2_,_3_,_3)<br>(2_,_4_,_3)<br>(3_,_1_,_3)<br>(3_,_2_,_3)<br>(3_,_3_,_3)<br>(3_,_4_,_3)<br>(4_,_1_,_3)<br>(4_,_2_,_3)<br>(4_,_3_,_3)<br>(4_,_4_,_3)<br>(1_,_1_,_2)<br>(1_,_2_,_2)<br>(1_,_3_,_2)<br>(1_,_4_,_2)<br>(2_,_1_,_2)<br>(2_,_2_,_2)<br>(2_,_3_,_2)<br>(2_,_4_,_2)<br>(3_,_1_,_2)<br>(3_,_2_,_2)<br>(3_,_3_,_2)<br>(3_,_4_,_2)<br>(4_,_1_,_2)<br>(4_,_2_,_2)<br>(4_,_3_,_2)<br>(4_,_4_,_2)<br>(1_,_1_,_1)<br>(1_,_2_,_1)<br>(1_,_3_,_1)<br>(1_,_4_,_1)<br>(2_,_1_,_1)<br>(2_,_2_,_1)<br>(2_,_3_,_1)<br>(2_,_4_,_1)<br>(3_,_1_,_1)<br>(3_,_2_,_1)<br>(3_,_3_,_1)<br>(3_,_4_,_1)<br>(4_,_1_,_1)<br>(4_,_2_,_1)<br>(4_,_3_,_1)<br>(4_,_4_,_1)<br>**_Y_**|_n_1<br>_n_2<br>_n_3<br>(1_,_1_,_3)<br>(1_,_2_,_3)<br>(1_,_3_,_3)<br>(1_,_4_,_3)<br>(2_,_1_,_3)<br>(2_,_2_,_3)<br>(2_,_3_,_3)<br>(2_,_4_,_3)<br>(3_,_1_,_3)<br>(3_,_2_,_3)<br>(3_,_3_,_3)<br>(3_,_4_,_3)<br>(4_,_1_,_3)<br>(4_,_2_,_3)<br>(4_,_3_,_3)<br>(4_,_4_,_3)<br>(1_,_1_,_2)<br>(1_,_2_,_2)<br>(1_,_3_,_2)<br>(1_,_4_,_2)<br>(2_,_1_,_2)<br>(2_,_2_,_2)<br>(2_,_3_,_2)<br>(2_,_4_,_2)<br>(3_,_1_,_2)<br>(3_,_2_,_2)<br>(3_,_3_,_2)<br>(3_,_4_,_2)<br>(4_,_1_,_2)<br>(4_,_2_,_2)<br>(4_,_3_,_2)<br>(4_,_4_,_2)<br>(1_,_1_,_1)<br>(1_,_2_,_1)<br>(1_,_3_,_1)<br>(1_,_4_,_1)<br>(2_,_1_,_1)<br>(2_,_2_,_1)<br>(2_,_3_,_1)<br>(2_,_4_,_1)<br>(3_,_1_,_1)<br>(3_,_2_,_1)<br>(3_,_3_,_1)<br>(3_,_4_,_1)<br>(4_,_1_,_1)<br>(4_,_2_,_1)<br>(4_,_3_,_1)<br>(4_,_4_,_1)<br>**_Y_**|_n_1<br>_n_2<br>_n_3<br>(1_,_1_,_3)<br>(1_,_2_,_3)<br>(1_,_3_,_3)<br>(1_,_4_,_3)<br>(2_,_1_,_3)<br>(2_,_2_,_3)<br>(2_,_3_,_3)<br>(2_,_4_,_3)<br>(3_,_1_,_3)<br>(3_,_2_,_3)<br>(3_,_3_,_3)<br>(3_,_4_,_3)<br>(4_,_1_,_3)<br>(4_,_2_,_3)<br>(4_,_3_,_3)<br>(4_,_4_,_3)<br>(1_,_1_,_2)<br>(1_,_2_,_2)<br>(1_,_3_,_2)<br>(1_,_4_,_2)<br>(2_,_1_,_2)<br>(2_,_2_,_2)<br>(2_,_3_,_2)<br>(2_,_4_,_2)<br>(3_,_1_,_2)<br>(3_,_2_,_2)<br>(3_,_3_,_2)<br>(3_,_4_,_2)<br>(4_,_1_,_2)<br>(4_,_2_,_2)<br>(4_,_3_,_2)<br>(4_,_4_,_2)<br>(1_,_1_,_1)<br>(1_,_2_,_1)<br>(1_,_3_,_1)<br>(1_,_4_,_1)<br>(2_,_1_,_1)<br>(2_,_2_,_1)<br>(2_,_3_,_1)<br>(2_,_4_,_1)<br>(3_,_1_,_1)<br>(3_,_2_,_1)<br>(3_,_3_,_1)<br>(3_,_4_,_1)<br>(4_,_1_,_1)<br>(4_,_2_,_1)<br>(4_,_3_,_1)<br>(4_,_4_,_1)<br>**_Y_**|_n_1<br>_n_2<br>_n_3<br>(1_,_1_,_3)<br>(1_,_2_,_3)<br>(1_,_3_,_3)<br>(1_,_4_,_3)<br>(2_,_1_,_3)<br>(2_,_2_,_3)<br>(2_,_3_,_3)<br>(2_,_4_,_3)<br>(3_,_1_,_3)<br>(3_,_2_,_3)<br>(3_,_3_,_3)<br>(3_,_4_,_3)<br>(4_,_1_,_3)<br>(4_,_2_,_3)<br>(4_,_3_,_3)<br>(4_,_4_,_3)<br>(1_,_1_,_2)<br>(1_,_2_,_2)<br>(1_,_3_,_2)<br>(1_,_4_,_2)<br>(2_,_1_,_2)<br>(2_,_2_,_2)<br>(2_,_3_,_2)<br>(2_,_4_,_2)<br>(3_,_1_,_2)<br>(3_,_2_,_2)<br>(3_,_3_,_2)<br>(3_,_4_,_2)<br>(4_,_1_,_2)<br>(4_,_2_,_2)<br>(4_,_3_,_2)<br>(4_,_4_,_2)<br>(1_,_1_,_1)<br>(1_,_2_,_1)<br>(1_,_3_,_1)<br>(1_,_4_,_1)<br>(2_,_1_,_1)<br>(2_,_2_,_1)<br>(2_,_3_,_1)<br>(2_,_4_,_1)<br>(3_,_1_,_1)<br>(3_,_2_,_1)<br>(3_,_3_,_1)<br>(3_,_4_,_1)<br>(4_,_1_,_1)<br>(4_,_2_,_1)<br>(4_,_3_,_1)<br>(4_,_4_,_1)<br>**_Y_**|_n_1<br>_n_2<br>_n_3<br>(1_,_1_,_3)<br>(1_,_2_,_3)<br>(1_,_3_,_3)<br>(1_,_4_,_3)<br>(2_,_1_,_3)<br>(2_,_2_,_3)<br>(2_,_3_,_3)<br>(2_,_4_,_3)<br>(3_,_1_,_3)<br>(3_,_2_,_3)<br>(3_,_3_,_3)<br>(3_,_4_,_3)<br>(4_,_1_,_3)<br>(4_,_2_,_3)<br>(4_,_3_,_3)<br>(4_,_4_,_3)<br>(1_,_1_,_2)<br>(1_,_2_,_2)<br>(1_,_3_,_2)<br>(1_,_4_,_2)<br>(2_,_1_,_2)<br>(2_,_2_,_2)<br>(2_,_3_,_2)<br>(2_,_4_,_2)<br>(3_,_1_,_2)<br>(3_,_2_,_2)<br>(3_,_3_,_2)<br>(3_,_4_,_2)<br>(4_,_1_,_2)<br>(4_,_2_,_2)<br>(4_,_3_,_2)<br>(4_,_4_,_2)<br>(1_,_1_,_1)<br>(1_,_2_,_1)<br>(1_,_3_,_1)<br>(1_,_4_,_1)<br>(2_,_1_,_1)<br>(2_,_2_,_1)<br>(2_,_3_,_1)<br>(2_,_4_,_1)<br>(3_,_1_,_1)<br>(3_,_2_,_1)<br>(3_,_3_,_1)<br>(3_,_4_,_1)<br>(4_,_1_,_1)<br>(4_,_2_,_1)<br>(4_,_3_,_1)<br>(4_,_4_,_1)<br>**_Y_**|_n_1<br>_n_2<br>_n_3<br>(1_,_1_,_3)<br>(1_,_2_,_3)<br>(1_,_3_,_3)<br>(1_,_4_,_3)<br>(2_,_1_,_3)<br>(2_,_2_,_3)<br>(2_,_3_,_3)<br>(2_,_4_,_3)<br>(3_,_1_,_3)<br>(3_,_2_,_3)<br>(3_,_3_,_3)<br>(3_,_4_,_3)<br>(4_,_1_,_3)<br>(4_,_2_,_3)<br>(4_,_3_,_3)<br>(4_,_4_,_3)<br>(1_,_1_,_2)<br>(1_,_2_,_2)<br>(1_,_3_,_2)<br>(1_,_4_,_2)<br>(2_,_1_,_2)<br>(2_,_2_,_2)<br>(2_,_3_,_2)<br>(2_,_4_,_2)<br>(3_,_1_,_2)<br>(3_,_2_,_2)<br>(3_,_3_,_2)<br>(3_,_4_,_2)<br>(4_,_1_,_2)<br>(4_,_2_,_2)<br>(4_,_3_,_2)<br>(4_,_4_,_2)<br>(1_,_1_,_1)<br>(1_,_2_,_1)<br>(1_,_3_,_1)<br>(1_,_4_,_1)<br>(2_,_1_,_1)<br>(2_,_2_,_1)<br>(2_,_3_,_1)<br>(2_,_4_,_1)<br>(3_,_1_,_1)<br>(3_,_2_,_1)<br>(3_,_3_,_1)<br>(3_,_4_,_1)<br>(4_,_1_,_1)<br>(4_,_2_,_1)<br>(4_,_3_,_1)<br>(4_,_4_,_1)<br>**_Y_**|_n_1<br>_n_2<br>_n_3<br>(1_,_1_,_3)<br>(1_,_2_,_3)<br>(1_,_3_,_3)<br>(1_,_4_,_3)<br>(2_,_1_,_3)<br>(2_,_2_,_3)<br>(2_,_3_,_3)<br>(2_,_4_,_3)<br>(3_,_1_,_3)<br>(3_,_2_,_3)<br>(3_,_3_,_3)<br>(3_,_4_,_3)<br>(4_,_1_,_3)<br>(4_,_2_,_3)<br>(4_,_3_,_3)<br>(4_,_4_,_3)<br>(1_,_1_,_2)<br>(1_,_2_,_2)<br>(1_,_3_,_2)<br>(1_,_4_,_2)<br>(2_,_1_,_2)<br>(2_,_2_,_2)<br>(2_,_3_,_2)<br>(2_,_4_,_2)<br>(3_,_1_,_2)<br>(3_,_2_,_2)<br>(3_,_3_,_2)<br>(3_,_4_,_2)<br>(4_,_1_,_2)<br>(4_,_2_,_2)<br>(4_,_3_,_2)<br>(4_,_4_,_2)<br>(1_,_1_,_1)<br>(1_,_2_,_1)<br>(1_,_3_,_1)<br>(1_,_4_,_1)<br>(2_,_1_,_1)<br>(2_,_2_,_1)<br>(2_,_3_,_1)<br>(2_,_4_,_1)<br>(3_,_1_,_1)<br>(3_,_2_,_1)<br>(3_,_3_,_1)<br>(3_,_4_,_1)<br>(4_,_1_,_1)<br>(4_,_2_,_1)<br>(4_,_3_,_1)<br>(4_,_4_,_1)<br>**_Y_**|_n_1<br>_n_2<br>_n_3<br>(1_,_1_,_3)<br>(1_,_2_,_3)<br>(1_,_3_,_3)<br>(1_,_4_,_3)<br>(2_,_1_,_3)<br>(2_,_2_,_3)<br>(2_,_3_,_3)<br>(2_,_4_,_3)<br>(3_,_1_,_3)<br>(3_,_2_,_3)<br>(3_,_3_,_3)<br>(3_,_4_,_3)<br>(4_,_1_,_3)<br>(4_,_2_,_3)<br>(4_,_3_,_3)<br>(4_,_4_,_3)<br>(1_,_1_,_2)<br>(1_,_2_,_2)<br>(1_,_3_,_2)<br>(1_,_4_,_2)<br>(2_,_1_,_2)<br>(2_,_2_,_2)<br>(2_,_3_,_2)<br>(2_,_4_,_2)<br>(3_,_1_,_2)<br>(3_,_2_,_2)<br>(3_,_3_,_2)<br>(3_,_4_,_2)<br>(4_,_1_,_2)<br>(4_,_2_,_2)<br>(4_,_3_,_2)<br>(4_,_4_,_2)<br>(1_,_1_,_1)<br>(1_,_2_,_1)<br>(1_,_3_,_1)<br>(1_,_4_,_1)<br>(2_,_1_,_1)<br>(2_,_2_,_1)<br>(2_,_3_,_1)<br>(2_,_4_,_1)<br>(3_,_1_,_1)<br>(3_,_2_,_1)<br>(3_,_3_,_1)<br>(3_,_4_,_1)<br>(4_,_1_,_1)<br>(4_,_2_,_1)<br>(4_,_3_,_1)<br>(4_,_4_,_1)<br>**_Y_**||vecRM(_·_)<br>tenRM(_·_)<br>**y**<br>(1_,_1_,_1)<br>(1_,_1_,_2)<br>(1_,_1_,_3)<br>(1_,_2_,_1)<br>...<br>(2_,_1_,_1)<br>...<br>(4_,_4_,_3)|vecRM(_·_)<br>tenRM(_·_)<br>**y**<br>(1_,_1_,_1)<br>(1_,_1_,_2)<br>(1_,_1_,_3)<br>(1_,_2_,_1)<br>...<br>(2_,_1_,_1)<br>...<br>(4_,_4_,_3)|vecRM(_·_)<br>tenRM(_·_)<br>**y**<br>(1_,_1_,_1)<br>(1_,_1_,_2)<br>(1_,_1_,_3)<br>(1_,_2_,_1)<br>...<br>(2_,_1_,_1)<br>...<br>(4_,_4_,_3)|
|---|---|---|---|---|---|---|---|---|---|---|---|
||||(1_,_1_,_2)<br>(1_,_2<br>(2_,_1_,_2)<br>(2_,_2||(1_,_1_,_3)<br>(1_,_2_,_3)<br>(1_,_3_,_3)<br>(1_,_4_,_3)|||||(1_,_1_,_1)||
||||||(2_,_1_,_3)<br>(2_,_2_,_3)<br>(2_,_3_,_3)<br>(2_,_4_,_3)|||||(1_,_1_,_2)||
|||||(1_,_1_,_2)<br>(1_,_2|(3_,_1_,_3)<br>(3_,_2_,_3)<br>(3_,_ <br>_,_2)<br>(1_,_3_,_2)<br>(1_,_4_,_2)||3_,_3)<br>(3_,_4_,_3)|||(1_,_1_,_3)||
|||||||||||||
|||_n_2||(2_,_1_,_2)<br>(2_,_2|(4_,_1_,_3)<br>(4_,_2_,_3)<br>(4_,_ <br>_,_2)<br>(2_,_3_,_2)<br>(2_,_4_,_2)||3_,_3)<br>(4_,_4_,_3)|||(1_,_2_,_1)||
||||(1_,_1_,_1)<br>(1_,_2|(3_,_1_,_2)<br>(3_,_2_,_2)<br>(3_,_ <br>_,_1)<br>(1_,_3_,_1)<br>(1_,_4_,_1)||3_,_2)<br>(3_,_4_,_2)||||...||
|_n_1|||(2_,_1_,_1)<br>(2_,_2|(4_,_1_,_2)<br>(4_,_2_,_2)<br>(4_,_ <br>_,_1)<br>(2_,_3_,_1)<br>(2_,_4_,_1)||3_,_2)<br>(4_,_4_,_2)||||(2_,_1_,_1)||
||||(3_,_1_,_1)<br>(3_,_2_,_1)<br>(3_,_3_,_1)<br>(3_,_4_,_1)|||||||...||
||||(4_,_1_,_1)<br>(4_,_2_,_1)<br>(4_,_3_,_1)<br>(4_,_4_,_1)|||||||(4_,_4_,_3)||



Figure 5.3: A graphical depiction of the process of converting an order-3 tensor between its multidimensional array and vector form in row-major order. Note that the elements in the vectorised signal are lexicographically ordered. 

order for this vectorisation process to be consistent with the operators, it should result in a vector with elements arranged in lexicographic order. In some fields, this is referred to as _row-major_ vectorisation since, in the case of an order-2 tensor, the index representing the row varies before the column index. In the following, we symbolise this operation mathematically as vecRM ( _·_ ) : R _[N]_[1] _[×][N]_[2] _[×][...][×][N][d] →_ R _[N]_ , and its reverse operation as tenRM ( _·_ ) : R _[N] →_ R _[N]_[1] _[×][N]_[2] _[×][...][×][N][d]_ . We use the ‘RM’ subscript to indicate explicitly that this process is occurring in row-major order, since the standard vec ( _·_ ) function defined for matrices is most commonly assumed to act in column-major order. 

In the following, we use bold lower-case symbols (e.g. **y** ) to indicate graph signals existing in their vector form, and bold upper-case calligraphic symbols (e.g. _**Y**_ ) to indicate graph signals in their multi-dimensional array form. That is, 

**==> picture [174 x 11] intentionally omitted <==**

Figure 5.3 shows gives a visual summary of the process of converting between these two representations for an order-3 tensor. 

To calculate the vector index _k_ which a tensor element with index **n** = [ _n_ 1 _, n_ 2 _, ..., nd_ ] is mapped to in row-major order, we can apply the following formula. 

**==> picture [278 x 31] intentionally omitted <==**

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

105 

(Note the _±_ 1 disappears when indexing begins from zero). The reverse operation, i.e. mapping a vector element index _k_ to a tensor index **n** can be achieved by running the algorithm **3** . 

Given these two operations, two arrays of any consistent shape can be mapped between one another by first vectorising according to eq. (5.10), and then converting to a tensor using the given algorithm. 

## **5.1.3 The** _**d**_ **-dimensional GFT and IGFT** 

Consider a tensor graph signal _**Y** ∈_ R _[N]_[1] _[×][N]_[2] _[×][...][×][N][d]_ represented in its multi-dimensional array form. In direct analogy to the two-dimensional case given in eqs. (3.5) and (3.6), we can define the Graph Fourier Transform (GFT) and its corresponding inverse (IGFT) of this signal as follows. 

**==> picture [345 x 37] intentionally omitted <==**

**==> picture [348 x 31] intentionally omitted <==**

Consider the definition of the GFT and IGFT of a _d_ -dimensional graph signal given in eqs. (5.11) and (5.12). In both cases, we are required to compute the result of a chained Kronecker product matrix acting on a length- _N_ vector. Whilst the most straightforward approach to computing this product would have time and memory complexity of _O_ ( _N_[2] ), a much more efficient implementation can be achieved by taking advantage of the Kronecker structure of the matrix. Specifically, the memory and time complexity of this operation can be reduced to _O_ ( _N_ ) and _O_ ( _N_[�] _Ni_ ) respectively. The importance of this fact cannot be understated, as it enables scaling to much larger product graphs than would otherwise be possible. 

**Algorithm 3** Mapping a vector element to a tensor element in row-major order 

**Input:** The target vector element _k_ **Input:** The shape of the output tensor ( _N_ 1 _, N_ 2 _, ..., Nd_ ) 

_k ← k −_ 1 

**for** _i_ **from** _d_ **to** 1 **do** 

**==> picture [77 x 29] intentionally omitted <==**

**end for** 

**Output:** ( _n_ 1 + 1 _, n_ 2 + 1 _, ..., nd_ + 1) 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

106 

This general algorithm for achieving this is well-known and can be summarised as follows. Consider the application of a chained Kronecker product matrix acting on a vector **y** . 

**==> picture [142 x 19] intentionally omitted <==**

This can be factorised as follows 

**==> picture [296 x 19] intentionally omitted <==**

As is visible, the original multiplication has now been broken into _d_ stages. However, the _i_ -th stage can be completed with _N × Ni_ multiplications by appropriately reshaping the vector and leveraging the properties of the Kronecker product. The reshaping operation can be completed using strided permutation matrices which can be applied in practice for virtually zero computational cost [Granata et al., 1992]. This idea is also key to the FFT and related algorithms, which can be understood as finding a recursive Kronecker structure in the Fourier matrix [Tolimieri et al., 2013]. 

Work on efficient computational procedures for this operation can be traced back to Roth [1934] who formulated the original 2-dimensional “vec trick” algorithm. The _d_ -dimensional generalisation was proposed in Pereyra and Scherer [1973] and improved in DeBoor [1979]. More recent work, such as Fackler [2019], has focused on further optimisations such as minimising data transit times and parallel processing. 

Furthermore, if the _i_ -th factor graph in the Cartesian product is a path or ring graph, then the corresponding matrix transformation can be completed with only _N_ log _Ni_ multiplications by making use of the FCT/FST/FFT algorithms. In the extreme case, where every factor graph has this special structure, the computational complexity reaches parity with the multidimensional FFT algorithm, and will have a runtime complexity of _O_ ( _N_ log _N_ ) [Smith and Smith, 1995]. 

In order to execute computations of this nature in a maximally efficient way, we have developed the Python library _PyKronecker_ , which is described in detail in Antonian et al. [2023]. This library offers a high-level API for constructing Kronecker-based operators and applying them to either vectors or tensors, whilst optimising the underlying computation using parallel GPU processing and Just In Time (JIT) compilation using the Jax library [Bradbury et al., 2018]. In the following, it will be assumed that all chained Kronecker product matrices are applied to vectors/tensors using an efficient implementation. This is essential for computing the _d_ - dimensional GFT and IGFT, the basic pseudocode for which is shown in algorithm **4** . Note that the ‘reshape’ operation should always be applied using the row-major convention. This is the 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

107 

standard convention in languages such as C and Python’s NumPy library [Harris et al., 2020], but not in languages such as Matlab and Fortran which use the column major convention. 

With a fast algorithm for computing the action of a _d_ -dimensional Kronecker product on a tensor defined, the corresponding algorithm for a Kronecker sum is also easily obtained. Since the Kronecker sum is defined as a sum of Kronecker products, we need only repeat this algorithm _d_ times, skipping each iteration of the loop when the corresponding product is an identity matrix. This modified form is useful when approximating filters with Chebyshev polynomials, which can be computed via repeated application of the Laplacian onto a tensor. 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

108 

**Algorithm 4** Efficient GFT and IGFT in _d_ -dimensions 

**Input:** List of Laplacian eigenvector matrices � **U**[(] _[i]_[)] _∈_ R _[N][i][×][N][i]_[�] _[d] i_ =1 

**function** GFT( _**Y** ∈_ R _[N]_[1] _[×][N]_[2] _[×][...][×][N][d]_ ) 

**for** _i_ **from** 1 **to** _d_ **do** 

**==> picture [188 x 94] intentionally omitted <==**

## **end function** 

**==> picture [183 x 83] intentionally omitted <==**

**end for return** reshape� _**Z** ,_ � _N_ 1 _, N_ 2 _, ..., Nd_ �[�] 

**end function** 

Tensor notation 

The use of tensor algebra is well established in fields such as physics and mechanics [Abraham et al., 1988, Renteln, 2013], however, it is less widespread in the signal processing community. For this reason, we choose to adopt a notation that leans more on standard linear algebra, however, all the equations and algorithms discussed in the following chapters could be alternatively written in a purer form of tensor notation. For example, consider the IGFT of a tensor signal _**Z**_ . In our notation, this is written as 

**==> picture [277 x 31] intentionally omitted <==**

As is visible, this describes the process in terms of regular matrix-vector multiplication but requires the additional definition of the vecRM ( _·_ ) and tenRM ( _·_ ) operations. Alternatively, this expression could be written using tensor indexing and Einstein summation notation 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

109 

as follows. 

**==> picture [313 x 23] intentionally omitted <==**

Note that here the indices _j_ 1 _, j_ 2 _, ..., jd_ on the right-hand side are implicitly summed over. This eliminates the need to consider vectorisation at all and is perhaps a more elegant way of describing the _d_ -dimensional GFT/IGFT. However, there are multiple indices to keep track of which becomes somewhat unaesthetic in a variable number of dimensions. 

Both forms offer different trade-offs, however, there is no practical difference when it comes to executing the signal processing algorithms themselves. Note that, as described in section 5.1.3, the full _N × N_ matrix implied by eq. (5.13) is never actually instantiated in memory (see algorithm **4** ). 

## **5.1.4 Multiway spectral operators and filtering** 

In this section, we make a case for a specific restricted definition of _d_ -dimensional graph filters. In Stanley et al. [2020], the authors discuss spectral operators on multiway graph signals as functions on the space of product graph eigenvalues. We propose a specific form for such functions, which produces operators **H** which can be understood as analytic functions of a Cartesian product graph Laplacian. This makes _d_ -dimensional filters easier to interpret and reason about in the context of MWGSP models. 

Just as in the one and two-dimensional case, the action of a general spectral operator is computed by first taking the GFT of a signal _**Y**_ , then applying some scaling function to each spectral component, and finally transforming back into the vertex domain via the IGFT. 

**==> picture [265 x 11] intentionally omitted <==**

The matrix operator that generates this transformation can be expressed as follows. 

**==> picture [269 x 13] intentionally omitted <==**

In the most general case, the _N_ elements of _**G**_ can vary freely to produce the total space of possible linear operators in the Laplacian eigenbasis. However, only a subset of these can be 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

110 

consistently interpreted as an analytic function of a Cartesian product graph Laplacian. The most restrictive possible definition of a graph filter would be one of the following form. 

**==> picture [245 x 32] intentionally omitted <==**

where 

**==> picture [221 x 30] intentionally omitted <==**

While this is a natural extension of the one-dimensional filter definition, it is isotropically constrained, since the filter strength is equal in all dimensions. In this case, the spectral scaling tensor _**G**_ has elements **n** = [ _n_ 1 _, n_ 2 _, ..., nd_ ] given by 

**==> picture [252 x 31] intentionally omitted <==**

However, we can naturally expand this to encompass anisotropic filters by introducing a parameter vector _**β** ∈_ R _[d]_ , where _βi_ dictates the filter strength in the _i_ -th dimension. 

**==> picture [266 x 66] intentionally omitted <==**

This introduces a modified graph Laplacian[�] _[d] i_ =1 _[β][i]_ **[L]**[(] _[i]_[)][, which effectively scales the edge weights] in each dimension by a factor of _βi_ . In this case, the spectral scaling tensor is given by 

**==> picture [284 x 31] intentionally omitted <==**

where _**λ**_ ( **n** ) _∈_ R _[d]_ is a vector holding the _ni_ -th eigenvalue of each graph Laplacian in the Cartesian product. 

**==> picture [282 x 22] intentionally omitted <==**

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

111 

|**Filter**||_g_(**_λ_**; **_β_**)|
|---|---|---|
|1-hop random walk||(1 +**_β_**_⊤_**_λ_**)_−_1|
|Difusion||exp(_−_**_β_**_⊤_**_λ_**)|
|ReLu|max(1_−_**_β_**_⊤_**_λ_**_,_0)||
|Sigmoid|2<br>�|1 + exp(**_β_**_⊤_**_λ_**)<br>�_−_1|
|Gaussian|exp<br>�<br>_−_(**_β_**_⊤_**_λ_**)2�||
|Bandlimited|1_,_|if**_β_**_⊤_**_λ_**_≤_1 else 0|



Table 5.1: Anisotropic graph filter functions in an arbitrary number of dimensions 

By requiring that the filter is a function of the dot product between _**β**_ and _**λ**_ , we effectively ensure that the operator remains consistent with the Cartesian product. Some example filters of this type are given in table 5.1. Other more general functions _g_ ( _**λ**_ ), which do not conform to this specification, will be more difficult to strictly interpret as a filter on a Cartesian product graph Laplacian. Moreover, since filters defined in this way are analytic functions of the (axeswise scaled) graph Laplacian, Chebyshev and other polynomial approximations can easily be leveraged to efficiently operate on signals in an eigendecomposition-free manner. However, one important caveat to note is that, while the filter strength can be varied, the functional form of the filter must be the same in each dimension. In general it is not clear how to consistently combine different functional forms for each axis into a single operator. 

## **5.2 Multiway Graph Signal reconstruction** 

In this section we extend the multivariate GSR model developed in chapter 3 to the MWGSP paradigm. Consider a tensor signal _**Y**_ of shape � _N_ 1 _, N_ 2 _, ... Nd_ � with elements interpreted as existing on the nodes of a _d_ -dimensional Cartesian product graph. Only a partial set _S_ = _{_ **n** 1 _,_ **n** 2 _, ...}_ of the vector elements of _**Y**_ are available at observation time, with unobserved values set to zero. The goal is to estimate the signal value at these unobserved entries. 

To aid with the model description, we also introduce a binary sensing tensor _**S**_ , of the same shape as _**Y**_ , which is used to indicate which elements of _**Y**_ were observed. This is defined as follows. 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

112 

**==> picture [254 x 43] intentionally omitted <==**

The input data for signal reconstruction on a _d_ -dimensional Cartesian product graph can therefore be summarised as follows. 

**==> picture [300 x 19] intentionally omitted <==**

In analogy with the two-dimensional case, (see section 3.2.1), we assume that _**Y**_ is a noisy partial observation of an underlying tensor, _**F**_ , which is smooth with respect to the topology of the Cartesian product graph. This is represented by the following statistical model. 

**==> picture [247 x 13] intentionally omitted <==**

where, here, the _◦_ symbol represents the generalised tensor Hadamard product, i.e. elementwise multiplication of two tensors. _**E**_ is a random tensor where each element has an independent normal distribution with unit variance. That is, 

**==> picture [263 x 11] intentionally omitted <==**

Given this distribution over the model noise, the conditional distribution of _**Y** |_ _**F**_ is given by 

**==> picture [350 x 19] intentionally omitted <==**

Or, more concisely, 

**==> picture [255 x 13] intentionally omitted <==**

where **f** = vecRM ( _**F**_ ), **y** = vecRM ( _**Y**_ ) , **s** = vecRM ( _**S**_ ) and **D** _**S**_ = diag ( **s** ). In order to encode the belief that the underlying tensor _**F**_ is smooth with respect to the topology of the graph, we can make use of the following prior distribution. 

**==> picture [250 x 13] intentionally omitted <==**

where **H** is constructed from an anisotropic graph filter function, with parameter _**β**_ . 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

113 

**==> picture [62 x 12] intentionally omitted <==**

where **D** _**G**_ = diag (vecRM ( _**G**_ )), and _**G**_ is the spectral scaling matrix obtained by applying a graph filter to the graph Laplacian eigenvalues. The intuition for this prior can be obtained from a direct generalisation of the one and two-dimensional cases. In essence, tensor signals drawn from this prior will have the same probability density function as iid noise filtered by **H** , so samples will be naturally smooth with respect to the topology of the underlying Cartesian product graph. By applying Bayes’ theorem, we obtain the posterior distribution for **f** conditioned on **y** . 

**==> picture [261 x 13] intentionally omitted <==**

where 

**==> picture [246 x 12] intentionally omitted <==**

Therefore, the mean of this posterior is obtained by solving the following linear system. 

**==> picture [260 x 15] intentionally omitted <==**

Once again, we are faced with a similar set of problems to those outlined in section 3.2.1. Namely, the coefficient matrix is very large and potentially ill-defined. This can be solved by turning to iterative methods such as the SIM and CGM, which are repeated here in their form adapted for the general tensor case. 

## **5.2.1 Tensor SIM** 

Generalising the SIM, which we initially describe for the two-dimensional case in section 3.2.2, to the tensor setting is straightforward. In particular, eq. (5.30) can be solved by splitting the coefficient matrix � **D** _**S**_ + _γ_ **H** _[−]_[2][�] into **M** _−_ **N** , where **M** and **N** take on the following values 

**==> picture [286 x 13] intentionally omitted <==**

where **D** _**S** ′_ = diag ( **1** _−_ **s** ). In this case, the inverse of **M** has the form 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

114 

**==> picture [322 x 59] intentionally omitted <==**

where the tensor _**J**_ has entries with the vector index **n** = [ _n_ 1 _, n_ 2 _, ..., nd_ ] given by 

**==> picture [239 x 25] intentionally omitted <==**

Here, the entries of _**G**_ are given by either eq. (5.18) or eq. (5.20), which correspond to an isotropic or anisotropic filter function respectively. Note that, just as described in section 3.2.2.1, it remains possible to apply the matrix **M** _[−]_[1] onto an arbitrary vector/tensor in such a way that eigendecomposition of the factor graph Laplacians is avoided entirely. This is because **M** _[−]_[1] = _J_ ([�] _βi_ **L**[(] _[i]_[)] ), where _J_ ( _x_ ) = _g_[2] ( _x_ ) _/_ ( _g_[2] ( _x_ ) + _γ_ ), so its action can be approximated using Chebyshev polynomials. 

In a very similar manner to eq. (3.21), the SIM update equation is given by 

**==> picture [264 x 12] intentionally omitted <==**

Note that each step can be achieved with time complexity _O_ ( _N_[�] _Ni_ ) by making use of the fast Kronecker algorithm for computing the _d_ -dimensional GFT/IFGT highlighted in section 5.1.3. To be explicit, this update formula can be computed efficiently as 

**==> picture [206 x 48] intentionally omitted <==**

or, equivalently, 

**==> picture [198 x 48] intentionally omitted <==**

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

115 

**Algorithm 5** The tensor SIM for GSR 

**Input:** Observed tensor graph signal _**Y** ∈_ R _[N]_[1] _[×][N]_[2] _[×][...][×][N][d]_ **Input:** Sensing tensor _**S** ∈{_ 0 _,_ 1 _}[N]_[1] _[×][N]_[2] _[×][...][×][N][d]_ **Input:** Factor graph Laplacians _{_ **L**[(] _[i]_[)] _∈_ R _[N][i][×][N][i] }[d] i_ =1 **Input:** Regularisation parameter _γ ∈_ R[+] **Input:** Graph filter function _g_ ( _·_ ; _**β** ∈_ R _[d]_ ) 

**==> picture [264 x 160] intentionally omitted <==**

**end while** 

**Output:** _**F**_ 

using the fast GFT/IGFT algorithms described in **4** . For clarity, the full SIM algorithm is given in algorithm **5** . 

Once again, the worst-case scaling rate of the number of steps required for convergence, _n_ SIM, is bounded by 

**==> picture [184 x 24] intentionally omitted <==**

where _m_ is the fraction of data that is missing in the input tensor _**Y**_ (see section 3.3). As before, the true scaling rate will depend on the strength of the graph filter. 

## **5.2.2 Tensor CGM** 

The tensor version of the CGM also follows naturally from the two-dimensional case outlined in section 3.2.3. In particular, eq. (5.30) can be transformed into the following equivalent preconditioned linear system. 

**==> picture [292 x 16] intentionally omitted <==**

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

116 

where, in the tensor case, 

**==> picture [302 x 31] intentionally omitted <==**

This means eq. (5.35) can be expressed as 

**==> picture [296 x 15] intentionally omitted <==**

Note that, once again, this preconditioned coefficient matrix can be multiplied onto any appropriate tensor _**Z**_ efficiently by making use of the chained Kronecker multiplication procedure given in algorithm **4** . As with the SIM, this can be performed with _O_ ( _N_[�] _Ni_ ) multiplications. In particular, 

**==> picture [218 x 43] intentionally omitted <==**

Just as with the two-dimensional case, we can bound the condition number of the preconditioned coefficient matrix to find the worst-case scaling rates in the limit of a weak and strong filter. As before, this falls between 

**==> picture [156 x 25] intentionally omitted <==**

## **5.3 Multiway Kernel Graph Regression** 

In this section, we take the Kernel Graph Regression (KGR) algorithm, developed in section 4.1, and generalise it to the multiway/tensor case. Consider a series of _T_ product graph signals, each denoted as _**Y** t_ , with dimensions ( _N_ 1 _× ... × Nd_ ). In this scenario, each signal is associated with an _T_ explanatory vector, **x** _t ∈_ R _[M]_ . Therefore, the available data consist of labelled pairs � **x** _t,_ _**Y** t_ � _t_ =1[.] This data can be consolidated into a a matrix, **X** , of dimensions ( _T × M_ ), and a tensor, _**Y**_ , with shape ( _T × N_ 1 _× ... × Nd_ ). 

The observed tensor _**Y**_ may also contain an arbitrary amount of missing data, which is described by the binary sensing tensor _**S**_ . In accordance with previous sections, _**S**_ shares its shape with 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

117 

**Algorithm 6** The tensor CGM for GSR 

**Input:** Observed tensor graph signal _**Y** ∈_ R _[N]_[1] _[×][N]_[2] _[×][...][×][N][d]_ **Input:** Sensing tensor _**S** ∈{_ 0 _,_ 1 _}[N]_[1] _[×][N]_[2] _[×][...][×][N][d]_ **Input:** Factor graph Laplacians _{_ **L**[(] _[i]_[)] _∈_ R _[N][i][×][N][i] }[d] i_ =1 **Input:** Regularisation parameter _γ ∈_ R[+] **Input:** Graph filter function _g_ ( _·_ ; _**β** ∈_ R _[d]_ ) 

For _i_ from 1 to _d_ , decompose **L**[(] _[i]_[)] into **U**[(] _[i]_[)] **Λ**[(] _[i]_[)][ �] **U**[(] _[i]_[)][�] _[⊤]_ Compute _**G**_ by applying eq. (5.20) 

Initialise _**Z R** ←_ _**G** ◦_ GFT ( _**Y**_ ) _**D** ←_ _**R**_ 

**while** _|_ ∆ **R** _| >_ tol **do** 

**==> picture [197 x 107] intentionally omitted <==**

**end while** 

**Output:** IGFT ( _**G** ◦_ _**Z**_ ) 

_**Y**_ and holds ones at elements where successful observations were made and zeros elsewhere. As a result, the input data for multiway KGR can be summarised as follows. 

**==> picture [382 x 18] intentionally omitted <==**

The goal of KGR is to estimate all the missing values within _**Y**_ , accounting for both the topology of the graph and the explanatory variables. As with the two-dimensional KGR model elaborated in section 4.1, no distinction is necessary between “training” and “testing” data in this context. To make a completely new prediction for some explanatory vector **x** _t_ , we merely assign zero to the corresponding values in _**Y**_ and _**S**_ . 

The fundamental logic underpinning the tensor-valued version of KGR remains consistent with the two-dimensional scenario. We continue to assume that _**Y**_ is a noisy, partial observation of 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

118 

an underlying latent signal _**F**_ , which is captured in the following statistical model. 

**==> picture [257 x 11] intentionally omitted <==**

In this section, we omit a detailed derivation of the prior distribution over **f** from first principles, as the process closely resembles the steps provided in section 4.1. For the purposes of this section, we justify it by stating that the signal _**F**_ should display smooth variations across both the space of explanatory variables and the topology of the Cartesian product graph. This can be encoded in the following prior distribution for **f** . 

**==> picture [257 x 14] intentionally omitted <==**

In this expression, **K** denotes a ( _T × T_ ) kernel matrix, which is created by applying a valid Mercer kernel, _κ_ , to pairs of explanatory variables such that **K** _ij_ = _κ_ ( **x** _i,_ **x** _j_ ). Multiple options for _κ_ are available, including popular choices such as the Gaussian kernel (see eq. (4.11)). By applying Bayes’ rule to eqs. (5.38) and (5.39), the posterior distribution over the latent signal **f** can be established. This is given by 

**==> picture [261 x 13] intentionally omitted <==**

where, in this case, the posterior precision matrix **P**[¯] is an _NT × NT_ matrix given by 

**==> picture [261 x 12] intentionally omitted <==**

## **5.3.1 Computation of the posterior mean** 

In order to find the posterior mean, we must solve the linear system **P**[¯] _[−]_[1] **y** . Again, this can be achieved by utilising the tensor versions of the SIM or CGM. In close analogy with the twodimensional case, the process is the same as that of multiway GSR, under the following change of variables. 

**==> picture [260 x 11] intentionally omitted <==**

To define **U**[¯] and _**G**_[¯] , first we must define the eigendecomposition of the kernel matrix **K** . 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

119 

**==> picture [240 x 12] intentionally omitted <==**

where **V** is the matrix with columns representing the normalised eigenvectors of **K** , and **Λ** _K_ is the diagonal matrix holding its eigenvalues in ascending order, such that 

**==> picture [291 x 19] intentionally omitted <==**

Then, **U**[¯] and _**G**_[¯] are defined as follows. 

**==> picture [260 x 12] intentionally omitted <==**

and 

**==> picture [321 x 19] intentionally omitted <==**

Just as with the to dimensional case in the previous chapter, elements of _**G**_[¯] which are larger are associated with smoother eigenvectors. However now these eigenvectors span the entire product space including the product graph and the space of explanatory variables. 

From here, either the SIM or CGM, as given in line 9 and algorithm 6, can be applied. The only changes necessary are the swap in **U**[¯] for **U** and _**G**_[¯] for _**G**_ . As such, this means that whenever GFT( _·_ ) is used, it instead signifies the following operation. 

**==> picture [362 x 72] intentionally omitted <==**

Note that these no longer technically represent the GFT and IGFT, but a modified Kronecker operation that now includes an additional dimension described by **V** . 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

120 

## **5.4 Multiway Regression with Network Cohesion** 

In this section, we extend the Regression with Network Cohesion (RNC) and Kernel Graph Regression with Network Cohesion (KGRNC) algorithms, initially discussed in section 4.2, to the multiway GSP framework. Our starting point will be multiway RNC. In this context, we are concerned with a graph signal residing on the nodes of a known _d_ -dimensional Cartesian product graph, where an arbitrary subset of the elements could be corrupted or absent. Furthermore, each of the _N_ = _N_ 1 _×...×Nd_ nodes is accompanied by a length- _M_ vector of explanatory variables. Consequently, the available data can be summarised as follows. 

**==> picture [394 x 19] intentionally omitted <==**

As before, the binary sensing tensor _**S**_ describes which elements of _**Y**_ were available at observation time. We also define the matrix **X** which is a reshaping of the tensor of explanatory variables _**X**_ such that 

**==> picture [329 x 18] intentionally omitted <==**

In this model, we assume that the signal _**Y**_ is a noisy partial observation of the sum of a smooth tensor signal _**C**_ and a linear combination of the explanatory variables at each node. This is summarised in the following model. 

**==> picture [256 x 13] intentionally omitted <==**

Here, **c** _∈_ R _[N]_ = vecRM ( _**C**_ ) is the flexible intercept term, which is assumed to vary smoothly across the _d_ -dimensional product graph. **w** _∈_ R _[M]_ is the learned coefficient vector which specifies the contribution of the explanatory variables to the prediction at each node. **e** _∈_ R _[N]_ is a random vector of iid Gaussian noise representing the model error. As in the two dimensional case, we can stack **c** and **w** into a single parameter vector _**θ**_ as 

**==> picture [250 x 37] intentionally omitted <==**

Then, the probability distribution over **y** given _**θ**_ can be expressed as follows. 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

121 

**==> picture [287 x 19] intentionally omitted <==**

To create a prior over _**θ**_ , we can combine the assumption that _**C**_ should vary smoothly over the graph with an L2 prior over the coefficient vector **w** . This is expressed as 

**==> picture [283 x 36] intentionally omitted <==**

The resultant posterior distribution over _**θ**_ is therefore given by 

**==> picture [283 x 37] intentionally omitted <==**

where 

**==> picture [333 x 37] intentionally omitted <==**

As in section 4.2, we can solve the linear system **P**[�] _[−]_[1]   using the CGM. In particular, we **X** _[⊤]_ **y**  **[y]**  first define the symmetric preconditioner **Ψ**[�] as follows. 

**==> picture [302 x 37] intentionally omitted <==**

where **U** _M_ and **D** _M_ are generated form the eigendecomposition of **X** _[⊤]_ **D** _**S**_ **X** as follows. 

**==> picture [334 x 14] intentionally omitted <==**

This allows us to generate a preconditioned coefficient matrix and solve the modified linear system as follows. 

**==> picture [266 x 94] intentionally omitted <==**

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

122 

## **5.5 GSR and KGR for green bond yield prediction** 

In this section, we undertake an analysis of the multiway Graph Signal Reconstruction and Kernel Graph Regression algorithms, developed in sections 5.2 and 5.3, applying them to the problem of predicting the yield of a set of green bonds over time. Green finance has recently emerged as an important asset class for funding the transition to a lower carbon economy [Peters et al., 2022]. Green bonds provide a mechanism for governments and municipalities to raise capital for large projects with specific climate or environmental sustainability objectives. In this case study, we utilise the yield time series for a number of US municipal green bonds, collected from Bloomberg, and attempt to estimate the missing values. This approach presents a novel method for estimating the theoretical price of bonds with various characteristics and for analysing the relationship between external factors, such as the federal funding rate or inflation, and yield. 

The yield (to maturity) of a bond is the single discount rate that, when applied to all cash flows, results in a present value equal to the current market price [Hull, 2009]. Broadly speaking, yields represent return on investment and therefore reflect the perceived risk of a particular security, with higher yields necessary to justify riskier assets. External macroeconomic factors such as inflation, central bank interest rates, and economic uncertainty also play a key role in determining yields. 

One key intrinsic factor that can influence the yield of a bond is its maturity, representing the 

**==> picture [312 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
10%<br>8%<br>6%<br>Yield<br>4%<br>30Y<br>2% 10Y<br>5Y<br>V®@ Z<br>0% 2Y<br>Maturity<br>1990<br>1995 6M<br>2000<br>2005<br>WH 2010<br>2015 1M<br>2020<br>Date 2025<br>**----- End of picture text -----**<br>


Figure 5.4: A 3D plot of the yield on US treasuries of various maturities over time. 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

123 

length of time before the principal must be repaid. Under normal market conditions, longterm fixed-income securities, such as 20-year bonds, typically provide higher returns than their short-term counterparts, such as 2-year bonds. This is primarily due to the greater uncertainty associated with longer-term securities, especially concerning potential fluctuations in future interest rates. For a set of equivalent bonds differing only based on their maturity length, the yield is expected to interpolate smoothly at any given time, forming the so-called yield curve. Figure 5.4 demonstrates how the yield curve for US treasuries has varied over the past 35 years. 

For bonds issued by other entities, such as state authorities, numerous intrinsic factors other than maturity may affect the yield. These include the credit rating of the issuer, the tax exemption status, and, particularly relevant to green bonds, the Environmental, Social and Governance (ESG) impact of the funded project. In this case study, we frame the problem of estimating unknown yields as a multiway graph signal processing task. Specifically, we categorise the bonds based on several factors likely to influence the yield, such that each bond can be associated with a node on a four-dimensional Cartesian product graph. In particular, we take into account the following factors, each of which forms the basis of one of the factor graphs. 

1. _Use of funds_ . Each bond in our dataset was associated with a project category (such as water, pollution or power) and sub-category (such as waste management, habitat conservation, or solar farms). We used this information to construct a tree graph, beginning with a root node, and branching into category and sub-category nodes. The resulting tree, comprising a total of 161 nodes, is visualised in fig. 5.5. Each bond can then be associated with a specific leaf node based on its particular project category. 

2. _Credit rating_ . Each bond also had an assigned credit rating associated with the issuer, designated by a ratings agency. These ratings range from the highest possible, “AAA”, to the lowest in our dataset, “BBB+”, giving a total of eight categories. Since these ratings have a natural order, they can be represented using a simple chain graph. 

3. _Maturity_ . Each bond has a fixed period from its issue date to the date of maturity. Unlike treasury bonds, the green bonds we considered did not necessarily have standard maturity lengths. We thus categorised each bond by the length of this period, sorted into eight different bins, with edges corresponding to 0, 1, 2, 5, 10, 20, 30, 40 and 50 years. As with credit rating, the natural order enables us to represent this with a chain graph. 

4. _Tax status_ . Each bond also has an associated tax status. This includes information about whether the bond was taxed at the federal and state level, as well as certain other provisions such as special exemptions for specific institutions. We represented tax status as a network, where any two codes were connected if they shared at least one property in common. Further information on the possible green bond tax statuses is presented in table 5.2, and the graph we used to connect them is depicted in fig. 5.6. 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

124 

**==> picture [334 x 331] intentionally omitted <==**

**----- Start of picture text -----**<br>
Water<br>General<br>General Obligation<br>Pollution<br>Multifamily Hsg<br>Build America Bonds<br>School District<br>Medical Facilities Airport<br>Power Housing<br>EducationDevelopment Utilities Transportation<br>Bond Bank<br>Higher Education<br>**----- End of picture text -----**<br>


Figure 5.5: A representation of the graph used for categorising municipal green bonds based on the sector of the project. 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

125 

|**Tax Status**|**Description**|
|---|---|
|Fed & St Tax-Exempt|Exempt from tax at both the federal and state level.|
|Fed Taxable/St Tax-Exempt|Taxable at the federal level, exempt at the state level.|
|Fed Tax-Exempt/St Taxable|Exempt at the federal level, taxable at the state level.|
|Fed BQ/St Tax-Exempt|“Bank Qualifed” (special provisions for large banks)|
||at the federal level, exempt at the state level.|
|Fed Tax-Exempt|Exempt at the federal level, no information about the|
||state level.|
|AMT/St Tax-Exempt|“Alternate Minimum Tax” (special provision remov-|
||ing certain tax deductions) at the federal level, exempt|
||at the state level.|
|Fed Taxable/St Taxable|Taxable at both the federal and state level.|



Table 5.2: Further information on the possible tax status of the green bonds used in this case study. 

Given these factors, each bond could be associated with a particular four-dimensional coordinate: use of funds, credit rating, maturity, and tax status. With the inclusion of a time coordinate, encompassing weekly data from June 2018 to March 2023, the resulting input tensor _**Y**_ had five distinct axes, with an overall shape of (429 _,_ 161 _,_ 8 _,_ 8 _,_ 7). For the KGR model, this can be 

**==> picture [276 x 251] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fed Taxable/ St Tax-Exempt AMT/St Ta x-Exempt<br>Fed BQ/St Tax-Exempt<br>Fed Taxable/St Taxable<br>Fed & St Tax-Exempt<br>Fed Tax-Exe mpt/St Taxable Fed Tax- Exempt<br>**----- End of picture text -----**<br>


Figure 5.6: A representation of the graph used for categorising municipal green bonds based on the associated tax status. Two different statuses are linked via an edge if they share at least one property in common. 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

126 

|Time<br>_t_<br>429<br>_⊗_<br>_×_<br>Use of funds<br>161<br>_⊗_<br>_×_<br>Rating<br>AAA<br>AA+<br>...<br>BBB+<br>8<br>_⊗_<br>_×_<br>Maturity<br>30-50y<br>20-30y<br>...<br>0-1y<br>8<br>_⊗_<br>_×_<br>Tax status<br>7|Time<br>_t_<br>429<br>_⊗_<br>_×_<br>Use of funds<br>161<br>_⊗_<br>_×_<br>Rating<br>AAA<br>AA+<br>...<br>BBB+<br>8<br>_⊗_<br>_×_<br>Maturity<br>30-50y<br>20-30y<br>...<br>0-1y<br>8<br>_⊗_<br>_×_<br>Tax status<br>7|Time<br>_t_<br>429<br>_⊗_<br>_×_<br>Use of funds<br>161<br>_⊗_<br>_×_<br>Rating<br>AAA<br>AA+<br>...<br>BBB+<br>8<br>_⊗_<br>_×_<br>Maturity<br>30-50y<br>20-30y<br>...<br>0-1y<br>8<br>_⊗_<br>_×_<br>Tax status<br>7|Time<br>_t_<br>429<br>_⊗_<br>_×_<br>Use of funds<br>161<br>_⊗_<br>_×_<br>Rating<br>AAA<br>AA+<br>...<br>BBB+<br>8<br>_⊗_<br>_×_<br>Maturity<br>30-50y<br>20-30y<br>...<br>0-1y<br>8<br>_⊗_<br>_×_<br>Tax status<br>7|
|---|---|---|---|
|||||
|||||
|||||
|||||
||||7|



Figure 5.7: A visualisation of the tensor coordinates used in this application. Rating, maturity and coupon are all represented by a chain graph, while category is represented by a tree graph as described above. 

interpreted as _T_ = 429 repeated measurements of a 4-dimensional multiway graph signal, and for the GSR model, it can be regarded as a single measurement of a 5-dimensional graph signal, with time also represented by a chain graph. Figure 5.7 provides a visual representation of the tensor signal, _**Y**_ , utilised in this application. 

For many specific tensor coordinates, no bond yield existed, and as such the tensor _**Y**_ was very sparse. This could be because the bond was not trading at this particular time, or because no bond ever existed with these particular characteristics. Moreover, since the parent nodes in the graph representing the use of funds are in a sense “artificial” - serving solely to create the tree structure - no realised yield could exist there. Under the framework developed in this thesis, this does not present a problem, since we can simply allocate these coordinates as containing missing data, as specified by the binary sensing tensor _**S**_ . 

Additionally, certain bonds shared identical characteristics, i.e., the same use of funds, rating, maturity, and tax status. In these instances, we simply selected the bond with the longest available history and randomly broke ties. In total, we used 829 bonds (out of a theoretically possible 161 _×_ 8 _×_ 8 _×_ 7 = 72 _,_ 128). As many bonds did not span the total 429 weeks, this left a total missingness of _m_ = 99 _._ 27%. 

As previously noted, one model we employ in this case study to predict the yields is Kernel Graph Regression. This necessitates, in addition to the input tensor _**Y**_ and the sensing tensor _**S**_ , a matrix of explanatory variables **X** with shape ( _T, M_ ). Here, we use the treasury yields over 11 different maturities, along with core inflation, the Federal Reserve fund rate, and a simple linear variable _t_ ranging from -1 to 1, totalling _M_ = 14 explanatory variables. This data was obtained from the FRED API [Federal Reserve Bank of St. Louis, 2023]. 

Our experiment proceeded as follows. Firstly, we randomly divided the 829 bonds into a training, validation, and test set in an 80:10:10 ratio. We then trained the GSR and KGR models on the training set, using the validation set to select the optimal hyperparameters, identified using an 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

127 

||Training<br>MSE<br>_R_2|Validation<br>MSE<br>_R_2|Test|
|---|---|---|---|
||||MSE<br>_R_2|
|GSR<br>KGR<br>Ridge<br>Lasso|0.263<br>0.846<br>0.266<br>0.845<br>0.387<br>0.775<br>0.424<br>0.753|0.332<br>0.819<br>0.333<br>0.820<br>0.501<br>0.729<br>0.482<br>0.739|0.319<br>0.823<br>0.317<br>0.824<br>0.497<br>0.725<br>0.506<br>0.720|



Table 5.3: The Mean Square Error (MSE) and _R_[2] statistic from the bond yield experiment are shown for both GSR and KGR. Results are reported on the training set, the validation set, and the test set. 

optimisation algorithm based on the Nelder-Mead method [Gao and Han, 2012]. In addition, we evaluated two standard linear regression techniques, namely Ridge and Lasso [Murphy, 2012]. In these scenarios, the yield at each moment in time for each bond was modelled as a linear combination of a constant term, the features comprising the matrix **X** , and a one-hot encoding of each of the bond descriptors (use of funds, rating, etc). This resulted in 1+14+159+8+8+7 = 197 explanatory variables for each yield. The regularisation parameter for the Ridge and Lasso models was also selected on the validation set using a straightforward line search. 

The results from the experiment can be found in table 5.3. As can be observed, the GSR and KGR methods attain similar performance to each other, consistently outperforming the Ridge and Lasso techniques. Both also display a Mean Square Error (MSE) and _R_[2] statistic that remains relatively constant across the training, validation, and test sets, suggesting that overfitting has largely been avoided. Figures 5.8 and 5.9 showcases the output of the GSR and KGR models respectively compared with the ground truth, for nine randomly representative bonds from the test set. The shaded regions represent two standard deviations of uncertainty, which is calculated by taking 20 samples from the posterior. (The method for producing these samples is explained in chapter 6). We can observe that both GSR and KGR make broadly similar predictions, which often correlate closely with the ground truth. However, there are instances where the predictions do systematically under or overestimate the yield, for example in the upper middle, middle right, and lower middle plots. This may indicate there was hidden information about this bond not accounted for in our explanatory variables. Further investigation into the reasons for these deviations would be valuable. 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

128 

**==> picture [417 x 404] intentionally omitted <==**

**----- Start of picture text -----**<br>
Water: Current Refunding AA+ Bond Bank: Current Refunding A+ Water: Transit Imps. AA<br>10-20y, Fed Taxable/St Tax-Exempt 2-5y, Fed & St Tax-Exempt 0-1y, Fed Tax-Exempt/St Taxable<br>8%<br>Ground truth<br>Predicted<br>6%<br>4%<br>2%<br>0%<br>Transportation: Green Purpose A General: Sewer Imps. AA General: Green Purpose A<br>40-50y, Fed Taxable/St Tax-Exempt 0-1y, Fed & St Tax-Exempt 2-5y, Fed & St Tax-Exempt<br>8%<br>6%<br>4%<br>2%<br>0%<br>General Obligation: Sewer Imps. A+ Transportation: Sewer Imps. A+ Power: Repayment Of Bank Loan AA-<br>1-2y, Fed Tax-Exempt/St Taxable 40-50y, Fed & St Tax-Exempt 0-1y, Fed Taxable/St Tax-Exempt<br>8%<br>6%<br>4%<br>2%<br>0%<br>Date<br>20192020202120222023 20192020202120222023 20192020202120222023<br>Yield<br>**----- End of picture text -----**<br>


Figure 5.8: The predicted yield is shown from the GSR model, as compared to the ground truth, on a set of green bonds taken from the test set. 

## **5.6 Conclusions** 

In this chapter, we have been concerned with regression and reconstruction tasks with tensorvalued signals that exist on the nodes of a _d_ -dimensional Cartesian product graph, under the so-called ‘Multiway GSP’ (MWGSP) framework [Stanley et al., 2020]. We began by reviewing the concept of Cartesian product graphs in an arbitrary number of dimensions and discussed how this naturally leads to the definition of the _d_ -dimensional GFT and IGFT. We also discussed the dual vector/tensor representation of multiway graph signals and highlighted the importance of efficient computation with chained Kronecker operators, presenting the PyKronecker software library for this purpose [Antonian et al., 2023]. We then made the case for a restricted definition of _d_ -dimensional anisotropic graph filters _g_ ( _**λ**_ ), which are constructed as a decreasing function of a dot product between _**β**_ and _**λ**_ . This ensures that the resultant spectral operator can be 

Chapter 5. _Regression and Reconstruction with Multiway Graph Signals_ 

129 

**==> picture [417 x 404] intentionally omitted <==**

**----- Start of picture text -----**<br>
Water: Current Refunding AA+ Bond Bank: Current Refunding A+ Water: Transit Imps. AA<br>10-20y, Fed Taxable/St Tax-Exempt 2-5y, Fed & St Tax-Exempt 0-1y, Fed Tax-Exempt/St Taxable<br>8%<br>Ground truth<br>Predicted<br>6%<br>4%<br>2%<br>0%<br>Transportation: Green Purpose A General: Sewer Imps. AA General: Green Purpose A<br>40-50y, Fed Taxable/St Tax-Exempt 0-1y, Fed & St Tax-Exempt 2-5y, Fed & St Tax-Exempt<br>8%<br>6%<br>4%<br>2%<br>0%<br>General Obligation: Sewer Imps. A+ Transportation: Sewer Imps. A+ Power: Repayment Of Bank Loan AA-<br>1-2y, Fed Tax-Exempt/St Taxable 40-50y, Fed & St Tax-Exempt 0-1y, Fed Taxable/St Tax-Exempt<br>8%<br>6%<br>4%<br>2%<br>0%<br>Date<br>20192020202120222023 20192020202120222023 20192020202120222023<br>Yield<br>**----- End of picture text -----**<br>


Figure 5.9: The predicted yield is shown from the KGR model as compared to the ground truth on a set of green bonds taken from the test set. 

consistently interpreted as an analytic function of a Cartesian product graph Laplacian. 

The key theoretical contribution of this chapter was to define models for graph signal reconstruction, as well as regression with exogenous and endogenous explanatory variables, for general tensor valued graph signals on _d_ -dimensional Cartesian product graphs. In section 5.2, we reexamined the GSR model developed in chapter 3, generalising it to _d_ dimensions. This necessitated a fresh look at the SIM and CGM methods previously developed to make them applicable to this setting. Next, in sections 5.3 and 5.4 respectively we took the Kernel Graph Regression and Regression with Network Cohesion techniques, which were developed in chapter 4, and generalised them for the multiway case. Finally, in section 5.5, we showed how the multiway KGR and GSR methods could be applied to the problem of predicting the yield of novel green bonds in a time series application. In particular, we showed that both GSR and KGR could achieve good performance, significantly outperforming the standard techniques of Ridge and Lasso regression. 

## **Chapter 6** 

## **Signal Uncertainty: Estimation and Sampling** 

So far in this thesis we have introduced several Bayesian GSP models and focused on tractable methods for finding the mean of the associated Gaussian posterior. In this chapter, we turn our attention to the posterior _covariance_ , which presents several new interesting challenges. These challenges stem from the dimensionality of the associated covariance matrix which, in each case, is the inverse of a large Kronecker-structured operator. For example, consider the twodimensional graph signal reconstruction problem defined in section 3.2. The posterior mean has shape ( _N × T_ ) and the posterior covariance matrix has shape ( _NT × NT_ ). For a modest-sized problem comprising a 200-node graph measured over 365 time points, the (known) precision matrix will have over 5 _×_ 10[9] elements, corresponding to over 20GB of memory with 32-bit floating-point numbers. Even if this could be held in RAM, inverting a matrix of this size would be intractable on consumer-grade hardware. This problem is only compounded when considering the tensor-valued models introduced in chapter 5, where the covariance matrices have _O_ ( _N_[2] ) elements, where _N_ =[�] _Ni_ . Table 6.1 lists the posterior covariance matrices that appear in these models, along with their associated dimensionality. 

Given these challenges, the goal of this chapter is to gain insight into the uncertainty about the predicted posterior mean, whilst circumventing the need to instantiate, invert or decompose large matrices directly in memory. To this end, we specify two separate but related tasks of interest: 

1. _To estimate the posterior marginal variance_ . Given a large, known precision matrix with a Kronecker structure, the task is to estimate the diagonal of the associated covariance matrix (its inverse). Whilst the most straightforward approach would be simply to invert the precision matrix directly and take the diagonal, this will be too memory-intensive for 

130 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

131 

|**Model**|**Covariance matrix**|||**Element count**|
|---|---|---|---|---|
|GSR|�<br>**D****_S_** +_γ_**H**_−_2�_−_1|||�_N_2<br>_i_|
|KGR|�<br>**D****_S_** +_γ_**K**_−_1 _⊗_**H**_−_2�_−_1|||_T_ 2�_N_2<br>_i_|
|RNC|<br><br>**D****_S_** +_γ_**H**_−_2<br>**D****_S_X**<br>**X**_⊤_**D****_S_**<br>**X**_⊤_**D****_S_X**+_λ_**I**_M_|<br><br>_−_1||��_Ni_+_M_<br>�2|
|KG-RNC|<br><br>**D****_S_** +_γ_**K**_−_1 _⊗_**H**_−_2<br>**D****_S_X**<br>**X**_⊤_**D****_S_**<br>**X**_⊤_**D****_S_X**+_λ_**I**_M_||<br><br>_−_1|�<br>_T_ �_Ni_+_M_<br>�2|



Table 6.1: The posterior covariance matrix appearing in the tensor GSR, KGR, RNC and KR-RNC models. 

most practical applications. Computing the marginal variance alone disregards information about the correlation between elements, but still gives valuable insight into prediction uncertainty whilst remaining tractable to store in memory. Therefore, the first task is to produce a scalable algorithm for estimating the diagonal of the posterior covariance matrix. 

2. _To sample directly from the posterior_ . For many applications, the ability to draw independent samples directly from the posterior is of significant interest. However, due to the size of the relevant matrices, direct Cholesky decomposition approaches will be intractable for most realistic use cases. Therefore, the second task is to produce an algorithm that can efficiently draw independent random samples from the posterior, whilst avoiding the memory and computational difficulties associated with the most straightforward approaches. 

The chapter is structured as follows. First, in section 6.1, we consider different approaches for estimating the posterior marginal variance. In particular, we compare a recent stochastic technique for estimating a matrix diagonal [Bekas et al., 2007, Tang and Saad, 2012] with several custom regression models which leverage intuition about the network structure of the problem. We show that, by including these network effects, it is possible to significantly increase prediction accuracy compared with the aforementioned stochastic technique on a test dataset. Next, in section 6.2, we make use of a recently proposed technique for direct sampling known as Perturbation Optimisation (PO) [Vono et al., 2022]. PO is relevant when the precision matrix can be split into a sum of matrices with a known eigenvalue decomposition which, as we will show, is always the case in our models. This allows us to draw independent samples from the posterior 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

132 

distribution for the same computational cost as is required to calculate the posterior mean which, as established in chapter 5, can be achieved efficiently using iterative methods. 

The methods derived in this chapter are designed to be applicable to tensor-valued GSP problems covered in chapter 5. However, since the two-dimensional methods covered in chapters 3 and 4 can be considered special cases of the more general MWGSP format, these too are included under the same framework. 

## **6.1 Estimating the posterior marginal variance** 

Consider the multiway Graph Signal Reconstruction problem as defined in chapter 5. Here, the goal is to estimate a smooth underlying signal, _**F**_ , with shape ( _N_ 1 _, N_ 2 _, ..., Nd_ ), given a partially observed graph signal, _**Y**_ , and binary sensing tensor, _**S**_ , both of which have the same shape as _**F**_ . In section 5.2, we demonstrate that the posterior distribution over **f** _∈_ R _[N]_ = vecRM ( _**F**_ ), given **y** _∈_ R _[N]_ = vecRM ( _**Y**_ ), is 

**==> picture [261 x 14] intentionally omitted <==**

where 

**==> picture [266 x 12] intentionally omitted <==**

The goal of this section is to estimate the posterior marginal variance, i.e. diagonal of the covariance matrix **P** _[−]_[1] , without directly evaluating the matrix in full. For the sake of brevity, in this section, we concentrate on accomplishing this task for the GSR model only. However, the methods discussed can easily be generalised to KGR, RNC and KG-RNC by making suitable modifications. 

## **6.1.1 A baseline approach** 

As previously established, it is possible to efficiently solve a linear system of the form **P** _[−]_[1] **z** , where **z** is an arbitrary length- _N_ vector, using the SIM or CGM. Therefore, a straightforward approach to computing the marginal variance in full is immediately available: to compute the _n_ -th column of **P** _[−]_[1] , we can solve the linear system **P** _[−]_[1] **e** _n_ , where **e** _n_ is the _n_ -th unit basis vector. Consequently, to compute the entire marginal variance in full, we solve this system _N_ =[�] _Ni_ times, once for each _n ∈_ [1 _,_ 2 _, ..., N_ ], retaining only the _n_ -th element of the resultant solution each time. 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

133 

Whilst this strategy avoids holding any ( _N × N_ ) matrix directly in memory, and has lower time complexity than directly inverting **P** , it still presents significant computational challenges. Since obtaining each element of the marginal variance necessitates solving a linear system, the whole process takes _N_ times longer than the computation of the mean, which itself can be intensive for large problems. A natural question, then, is whether the full marginal variance can be _estimated_ for a lower computational cost. 

## **6.1.2 Matrix diagonal estimation** 

One notable approach for estimating the diagonal of an arbitrary matrix comes from Bekas et al. [2007], which was subsequently updated in Tang and Saad [2012]. Here, the authors propose a stochastic technique, based on the earlier work of Hutchinson [1990], which was designed to estimate the trace of a matrix. The authors define the estimator for diag � **P** _[−]_[1][�] as follows. 

**==> picture [317 x 31] intentionally omitted <==**

Here, _⊘_ denotes element-wise division, and _◦_ is the Hadamard product (element-wise multiplication) as before. In the original specification, the vectors _{_ **v** _r}_ have entries of _±_ 1 which are drawn uniformly at random. This estimator converges to the true diagonal of **P** _[−]_[1] as _R →∞_ [Bekas et al., 2007]. For this technique to be scalable, it is necessary for the system **P** _[−]_[1] **v** to be solved efficiently for an arbitrary vector **v** (which it can in our case, using the SIM or CGM). Furthermore, the algorithm requires **P** _[−]_[1] **v** to be computed for _R_ different values of **v** _r_ . Therefore the overall complexity of this approach is proportional to _R_ . For this estimator to be better than the baseline approach outlined in section 6.1.1, we must reach an acceptable level of accuracy for _R ≪ N_ . 

## **6.1.3 A supervised learning approach** 

In this subsection, we introduce the key contribution of the first half of this chapter. The basic idea is as follows. Using the approach outlined in section 6.1.1, we can compute the ‘true’ variance at a limited number, _Q_ , of the elements by solving the linear system **P** _[−]_[1] **e** _n_ , and retaining only the _n_ -th element of the resultant vector, for a set of elements _Q_ . Next, we _predict_ the marginal variance at all the other elements not in the set _Q_ . If we can construct a set of artificial explanatory variables associated with each element, then this becomes a standard supervised learning problem. 

Since variance is strictly positive, we choose to predict the _log_ -variance rather than the variance itself. This transformation changes the prediction range from the positive values of [0 _, ∞_ ] to the 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

134 

full range of [ _−∞, ∞_ ], which is more suitable for standard regression techniques. We define the target variable, denoted as _**Ω**_ , as follows. 

**==> picture [318 x 14] intentionally omitted <==**

Note that here we have introduced the notation diag _[−]_[1] ( _·_ ), which denotes a function mapping the diagonal of an ( _N × N_ ) matrix into a length- _N_ vector. Therefore, the whole expression can be understood as taking the diagonal of the covariance matrix **P** _[−]_[1] , performing an element-wise logarithm, and transforming this into a tensor, _**Ω**_ , of shape ( _N_ 1 _, N_ 2 _, ..., Nd_ ) in row-major order. The objective of the regression algorithms discussed in this section is to predict the tensor _**Ω**_ . 

To make this prediction, we first compute a subset of the elements of _**Ω**_ . Since _**Ω**_ is an order- _d_ tensor, its elements are indexed by a length- _d_ integer vector, **n** . Therefore we can describe the indices that we choose to compute by the set _Q_ = _{_ **n** 1 _,_ **n** 2 _, ...,_ **n** _Q}_ . Additionally, we define the binary tensor _**Q**_ , which also indicates which elements of _**Ω**_ have been computed. 

**==> picture [256 x 43] intentionally omitted <==**

For each index **n** , the corresponding element of _**Ω**_ can be computed as 

**==> picture [271 x 13] intentionally omitted <==**

For a vector index **n** = [ _n_ 1 _, n_ 2 _, ..., nd_ ], the corresponding unit vector **e** _n_ is 

**==> picture [287 x 30] intentionally omitted <==**

The linear system **P** _[−]_[1] **e** _n_ can then be solved efficiently using either the tensor SIM or CGM as discussed in sections 5.2.1 and 5.2.2. We refer to the process of computing these elements of _**Ω**_ as _querying_ . The result, after _Q_ queries, is a partial observation of the matrix _**Ω**_ , where _Q_ of its entries have been filled in, and the rest are set to zero. We refer to this tensor as _**Ω** Q_ . 

**==> picture [237 x 11] intentionally omitted <==**

As mentioned, we also need a set of explanatory variables to help predict the unknown elements of _**Ω**_ . In particular, every element, **n** , should have an associated feature vector, **xn** , which should 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

135 

||**Description**|**Representation**|
|---|---|---|
|**_X_**:_,_1|Constant|**1**(_N_1_,N_2_,...,Nd_)|
|**_X_**:_,_2|Missing observations|**_S_**_′_|
|**_X_**:_,_3|Missing obs fltered|IGFT<br>~~�~~<br>**_G_**_◦_GFT<br>�<br>**_X_**:_,_2<br>�~~�~~|
|**_X_**:_,_4|Diagonal of **H**|tenRM<br>�<br>diag_−_1 (**H**)<br>�|
|**_X_**:_,_5|Diagonal of **H**2|tenRM<br>�<br>diag_−_1 �<br>**H**2��|
|**_X_**:_,_6|N-neighbours|tenRM(**A1**_N_)|
|**_X_**:_,_7|N-neighbours fltered|IGFT<br>~~�~~<br>**_G_**_◦_GFT<br>�<br>**_X_**:_,_6<br>�~~�~~|



Table 6.2: The explanatory variables used to predict the posterior log-variance. Note that _**X**_ : _,_ 4 and _**X**_ : _,_ 5 have an efficient computation - see theorem A.7 

have some explanatory power over _**Ω**_ **n** . In this way, the problem becomes a regular supervised learning task where the goal is to predict _**Ω**_ given the labelled training pairs _{_ _**Ω**_ **n** _,_ **xn** _}_ **n** _∈Q_ . If each feature vector has length _k_ , the explanatory variables as a whole can be described by the tensor _**X**_ with shape ( _N_ 1 _, ..., Nd, k_ ). The question then becomes how to construct a tensor _**X**_ which is likely to explain the posterior marginal variance well. 

By inspecting eq. (6.2), it is clear that the marginal variance can only depend on _**S**_ , and **H** , since these are the only matrices appearing in the posterior covariance ( _γ_ can be considered a constant for this problem). **H** itself also depends on the graph filter used and the structure of the graph. Therefore, we should choose features which capture different aspects of these objects. 

In the following, we use _k_ = 7 different descriptors which are summarised in table 6.2. For the features that include a filtering operation ( _**X**_ : _,_ 3 and _**X**_ : _,_ 7), we use the same filter parameters that were used in the original GSR specification. As in the RNC model of section 5.4, we can combine these tensor variables together into a single matrix **X** as follows. 

**==> picture [344 x 19] intentionally omitted <==**

## **6.1.3.1 Solving with Ridge Regression** 

The first strategy we use to predict the posterior log-variance is simply ridge regression. Here, we model the posterior log-variance _**Ω**_ as a linear combination of the features given in table 6.2, with the optimal weighting, **w** , learned from the observed data. In particular, the predicted value of _**Ω**_ , which we label _**Ω**[⋆]_ is given simply by 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

136 

**==> picture [86 x 11] intentionally omitted <==**

where 

**==> picture [188 x 16] intentionally omitted <==**

Note that since **D** _**Q**_ = diag (vecRM ( _**Q**_ )) is a sparse diagonal matrix, the product **X** _[⊤]_ **D** _**Q**_ **X** can be computed efficiently with _O_ ( _k_[2] _Q_ ) operations. This model includes a regularisation parameter _λ_ which must be set ahead of time (or potentially learned via cross-validation). 

## **6.1.3.2 Solving with RNC** 

The next strategy we use to predict the marginal variance is tensor Regression with Network Cohesion (RNC), as set out in section 5.4. This extends ridge regression by including a flexible intercept term, _**C**_ , which is assumed to be smooth with respect to the graph topology. Since we expect that posterior uncertainty should propagate via closely connected nodes, it is reasonable to assume that _**Ω**_ varies smoothly over the network. In this case, the predicted value for _**Ω**_ is given by 

**==> picture [263 x 11] intentionally omitted <==**

The optimal values for _**C**[⋆]_ and **w** _[⋆]_ can be computed using the same methodology as described in section 5.4. As such, they are given by 

**==> picture [365 x 39] intentionally omitted <==**

Once again, this linear system can be solved efficiently using the SIM or CGM. 

## **6.1.3.3 Ridge regression with learned filter parameters** 

The final novel method we consider for the prediction of the posterior log-variance is based on the empirical observation that the predictions made by ridge regression can be improved by adjusting the parameters that characterise the graph filter used to construct features _**X**_ : _,_ 3 and _**X**_ : _,_ 7. However, it is difficult to tell ahead of time the direction and magnitude of the optimal adjustment. For this reason, we propose a new estimator for _**Ω**_ that simultaneously learns the 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

137 

coefficients multiplying each feature in table 6.2, as well as the filter parameters characterising _**X**_ : _,_ 3 and _**X**_ : _,_ 7, which can vary independently. This can be expressed as follows. 

**==> picture [261 x 11] intentionally omitted <==**

Note that now **X** is a function of the filter parameters _**β**_ . In order to find the optimal values for both **w** _[⋆]_ and _**β**[⋆]_ , we use the following loss function. 

**==> picture [354 x 14] intentionally omitted <==**

where _**β**_ 0 represents the parameters characterising the original graph filter in the base GSR problem. Minimising the expression in eq. (6.13) is in general a non-convex optimisation problem. However, a reasonable initial estimate for **w** is easily attainable by solving the ridge regression problem. From there, only minor adjustments are necessary for significant improvement in predictive performance. Therefore, off-the-shelf nonlinear optimisation algorithms such as quasiNewton methods like BFGS can be readily applied [Fletcher, 2013]. 

## **6.1.4 Query strategies** 

So far in this discussion, we have not addressed the question of how to select which elements of _**Ω**_ to query. The simplest approach is to uniformly select samples at random. However, although unbiased, this can lead to a high variance estimator, particularly when the query size is very small. A preferable approach is to select elements in a principled way, such that the variance of the estimator is reduced for a small sample size. This is likely to be achieved when the associated features of the samples are representative of the population at large. 

Here we make use of a simple but effective query strategy. First, cluster the elements _{_ **n** _}_ into _K ≤ Q_ groups based on the data matrix **X** . Any clustering algorithm can be used here: a simple and fast option is _K_ -means [Hartigan and Wong, 1979, MacQueen, 1967]. Next, generate a query set _Q_ by randomly choosing a new data point from each cluster in order. This simple approach is made explicit in algorithm 7. 

## **6.1.5 Comparison and analysis** 

In order to compare the performance of the various techniques discussed in this section, we ran the following simple experiment which was set up as follows. First, a product graph was generated 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

138 

**Algorithm 7** Querying based on representative samples 

**Input:** Number of clusters _K_ **Input:** Number of queries _Q_ **Input:** Data matrix **X** _∈_ R _[N][×]_[7] 

Group data into _K_ randomly ordered cluster sets _{Ck}[K] k_ =1[using] _[K]_[-means][algorithm] Create empty query set _Q_ **for** _q_ from 1 to _Q_ **do** 

Select next non-empty cluster set _C_ Choose member _nq_ from cluster set _C_ at random Add member _nq_ to query set _Q_ Remove member _nq_ from cluster set _C_ **end for** 

**Output:** Query set _Q_ 

by taking the Cartesian product of three random connected graphs, with 10, 15 and 20 nodes respectively, resulting in a graph with 10 _×_ 15 _×_ 20 = 3000 total nodes. Next, we generated a random binary sensing tensor _**S**_ of shape (10 _,_ 15 _,_ 20) by setting elements to zero or one uniformly at random. Finally, we chose an anisotropic diffusion graph filter with _**β**_ = [0 _._ 5 _,_ 0 _._ 7 _,_ 0 _._ 6], and set _γ_ to one. The task, then, was to predict the diagonal of ( **D** _**S**_ + _γ_ **H** _[−]_[2] ) _[−]_[1] given the values as specified. Given the relatively small size of the problem, we could compute the true value of _**Ω**_ by running the baseline algorithm as discussed in section 6.1.1 over 3000 elements. 

Next, we compared the performance of each of the algorithms discussed in this section. They were the traditional diagonal estimation algorithm of Bekas et al. [2007] (Bekas) outlined in section 6.1.2, Ridge Regression (RR), as outlined in section 6.1.3.1, Regression with Network Cohesion (RNC) as outlined in section 6.1.3.2, and finally ridge regression with Learned Filter Parameters (LFP), as outlined in section 6.1.3.3. For each strategy, we measured the performance of the estimator by computing the total square error of the predicted variance (not the logvariance), and the _R_[2] statistic of the predicted variance. To be explicit, these were calculated as follows. 

**==> picture [292 x 13] intentionally omitted <==**

**==> picture [282 x 29] intentionally omitted <==**

where the exponential is understood as element-wise, and exp( _**Ω**_ ) means the mean of exp( _**Ω**_ ) across all elements. For the case of the Bekas estimator, there was no need to exponentiate the 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

139 

prediction, since it estimates the posterior variance directly, not the log-variance. 

For each of these different estimators, we measured the performance via these two metrics across a range of values of _Q_ , i.e. for different numbers of queries. In the case of the Bekas estimator, we measured the performance for different values of _R_ [see eq. (6.3)]. Since each query requires solving the linear system **P** _[−]_[1] **e** _n_ , and each iteration of the Bekas algorithm requires solving the linear system **P** _[−]_[1] **v** _r_ , these two measures have a direct correspondence in terms of total compute time. 

For the case of RR, RNC and LFP, we also compared the performance when using a random query strategy, and the representative sampling query strategy as outlined in algorithm 7. The results are shown in fig. 6.1. On the _x_ -axis, we show the number of queries (number of Bekas iterations) as a percentage of the total number of elements, i.e. _Q/N_ (or _R/N_ for Bekas). 

The results show that the three supervised learning-based strategies (RR, RNC and LFP) all significantly outperform Bekas on this synthetic dataset. Moreover, when coupled with the representative sampling strategy of algorithm 7, all three achieve an _R_[2] statistic of around 0.99 when only 1% of the elements of _**Ω**_ are queried. These results clearly demonstrate the value of this sampling strategy, especially when the number of queries is low. On this dataset, algorithm 7 has a significant positive impact on performance up to a query percentage of around 3%, beyond which the difference is less pronounced. 

Of the three supervised learning-based techniques, LFP tends to display the strongest performance at low query percentages, for both random and representative query strategies. RR and RNC have similar performance in this domain, with RNC improving more as the query percentage increases. 

Overall, these results demonstrate that high accuracy predictions ( _R_[2] of roughly 0.99) can be achieved for a very low query number relative to the total number of nodes _N_ , especially when combined with algorithm 7. While limited to our graph signal processing models, the supervised learning strategy is clearly more effective than the more general technique of Bekas et al. [2007] on this dataset. 

## **6.2 Posterior Sampling** 

In this section, we move on to the second aim of this chapter, which is to produce an algorithm capable of drawing independent samples directly from the posterior. Let us again begin with the tensor-valued Graph Signal Reconstruction problem. Recall that the posterior distribution is 

**==> picture [261 x 14] intentionally omitted <==**

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

140 

**==> picture [416 x 426] intentionally omitted <==**

**----- Start of picture text -----**<br>
Random Queries Representative Queries<br>RR<br>10 1 RNC<br>LFP<br>Bekas<br>10 2<br>10 3<br>1.000<br>0.995<br>0.990<br>R [2]<br>0.985<br>0.980<br>0.975<br>1% 3% 10% 30% 100% 1% 3% 10% 30% 100%<br>Percentage queried<br>Square Error<br>**----- End of picture text -----**<br>


Figure 6.1: The performance of the various algorithms for predicting the posterior log-variance is shown as a function of the percentage of _**Ω**_ that has been queried. The top row shows the total square error of the posterior variance, and the bottom row shows the _R_[2] statistic. The left column shows results for random queries and the right column shows the results when using representative queries as outlined in algorithm 7. Since the Bekas technique does make use of the active learning strategy, it is repeated in the left and right columns for reference. 

where 

**==> picture [311 x 14] intentionally omitted <==**

The most straightforward approach would be to perform Cholesky decomposition directly on the covariance matrix **P** _[−]_[1] , such that **P** _[−]_[1] = **LL** _[⊤]_ , where **L** is a lower triangular matrix. Every positive-definite matrix (and thus also every valid covariance matrix) has a unique Cholesky 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

141 

decomposition [Horn and Johnson, 2012]. Independent samples can then be drawn according to 

**==> picture [245 x 13] intentionally omitted <==**

where **z** _i ∈_ R _[N]_ is a random vector with components that are independent standard normal variates which can be generated, for example, by using the Box-Muller transform [Box and Muller, 1958]. Alternatively, if we can perform eigendecomposition on the covariance matrix into **P** _[−]_[1] = **UΛU** _[⊤]_ , then samples can be drawn according to 

**==> picture [256 x 13] intentionally omitted <==**

Both these techniques assume that the covariance matrix **P** _[−]_[1] can be directly decomposed in a reasonable amount of time. However, in the case of the GSR problem, **P** _[−]_[1] is not directly available. We instead have a representation of **P** in terms of a diagonal and Kronecker structured operator, as given in eq. (6.18). For even a modestly-sized GSR problem, this makes these approaches numerically infeasible due to both computational cost and memory footprint. 

## **6.2.1 Perturbation optimization (PO)** 

Perturbation Optimisation (PO) is a technique for sampling from high-dimensional Gaussian distributions when the precision matrix **P** is of the form 

**==> picture [254 x 31] intentionally omitted <==**

where _{_ **R** _k}_ are a set of alternative covariance matrices from which it is easier to draw samples from, and _{_ **M** _k}_ are a set of arbitrary full-rank square matrices [Orieux et al., 2012, Papandreou and Yuille, 2010]. The PO algorithm gives a method for drawing samples from the distribution _N_ � **0** _,_ **P** _[−]_[1][�] , which is achieved by completing the following steps. 

1. Step P (Perturbation): For _k_ from 1 to _K_ , draw samples _**η** k_ from _N_ ( **0** _,_ **R** _k_ ) 

2. Step O (Optimisation): Compute **f** as the minimiser of the criterion 

**==> picture [181 x 31] intentionally omitted <==**

Once the optimisation step has been completed, the resultant vector, **f** , will be distributed according to _N_ � **0** _,_ **P** _[−]_[1][�] . This can be trivially extended to non-centred distributions by 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

142 

adding the mean to each sample. It’s important to note that for PO to be an effective algorithm, it necessitates efficient resolution of the optimisation step. As we will see, in our case, we can exploit the Kronecker structure of the relevant matrices to accomplish this step for the same computational cost as computing the mean. 

## **6.2.2 PO for Graph Signal Reconstruction** 

In the case of graph signal reconstruction, we have that 

**==> picture [99 x 14] intentionally omitted <==**

Comparing this to the form required for PO given in eq. (6.20), we can substitute the following values. Note that, since **D** _**S**_ is diagonal and binary, **D**[2] _**S**_[=] **[ D]** _**[S]**_[.] 

**==> picture [227 x 13] intentionally omitted <==**

The random samples _**η**_ 1 and _**η**_ 2 can be generated by setting _**η**_ 1 = **z** 1 and _**η**_ 2 = **D** _**G**_ **z** 2 where **z** 1 and **z** 2 are independently drawn from a multivariate standard normal distribution. This gives the following optimisation objective _J_ ( **f** ). 

**==> picture [393 x 16] intentionally omitted <==**

Taking the derivative with respect to **f** , setting the result equal to zero, and solving for **f** gives 

**==> picture [277 x 14] intentionally omitted <==**

This generates random vectors **f** distributed according to _N_ � **0** _,_ **P** _[−]_[1][�] . To transform this into a distribution with mean **P** _[−]_[1] **y** , we can simply add this term on. 

**==> picture [287 x 13] intentionally omitted <==**

However, in its current form, the solution presents two issues. Firstly, the multiplication by the matrix **P** _[−]_[1] may result in an ill-conditioned linear system. Secondly, **z** 2 is multiplied by the matrix **D** _[−]_ _**G**_[1][,][which,][for][certain][filters][like][the][bandlimited][filter][that][maps][some][values][to][zero,] may map some values to infinity. Both problems can be addressed by introducing the symmetric preconditioner **Ψ** as discussed in section 5.2.2. As previously stated, this is given by 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

143 

**==> picture [232 x 11] intentionally omitted <==**

This transforms the system into 

**==> picture [317 x 36] intentionally omitted <==**

where 

**==> picture [167 x 12] intentionally omitted <==**

With this preconditioner in place, the linear system **Q** _[−]_[1][ �] **Ψ** _[⊤]_ **y** + **Ψ** _[⊤]_ **D** _**S**_ **z** 1 + _[√] γ_ **z** 2� can then be solved efficiently using the CGM. For the sake of completeness, we now provide a brief proof that the expression given in eq. (6.25) generates samples from the correct distribution. 

**Theorem 6.1.** _Consider the following expression for the vector_ **f** _∈_ R _[N] ._ 

**==> picture [170 x 13] intentionally omitted <==**

_If z_ 1 _, z_ 2 _∼N_ ( **0** _,_ **I** _N_ ) _, then_ **f** _is distributed according to_ 

**==> picture [91 x 13] intentionally omitted <==**

_Proof._ To prove this statement it suffices to show that the expected value of **f** is **P** _[−]_[1] **y** , and that the covariance is **P** _[−]_[1] . Note that the following identities hold. 

**==> picture [284 x 33] intentionally omitted <==**

Let us begin with the expected value. 

**==> picture [200 x 14] intentionally omitted <==**

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

144 

Since E [ **z** 1] = E [ **z** 2] = **0** , these two terms can be dropped from the expression, leaving 

**==> picture [82 x 13] intentionally omitted <==**

Making use of identity (d), this is then 

**==> picture [58 x 12] intentionally omitted <==**

Next, let us compute the covariance. 

**==> picture [222 x 13] intentionally omitted <==**

Consider the three terms within the inner brackets. Since the first has no stochastic component, it does not contribute to the covariance and can therefore be dropped. 

**==> picture [264 x 135] intentionally omitted <==**

We have therefore shown that E [ **f** ] = **P** _[−]_[1] **y** and that Cov [ **f** ] = **P** _[−]_[1] , completing the proof. 

Given the expression for **f** outlined in eq. (6.25), we have a straightforward procedure for sampling from the posterior distribution of the GSR model, as detailed in algorithm 8. It’s important to note that the primary computational load of this algorithm stems from solving the linear system using the CGM. Consequently, the computational complexity of drawing a single sample from the posterior distribution is equivalent to solving one linear system via the CGM. 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

145 

**Algorithm 8** Draw one sample from the GSR posterior distribution 

Sample **z** 1 from _N_ ( **0** _,_ **I** _N_ ) Sample **z** 2 from _N_ ( **0** _,_ **I** _N_ ) **a** _←_ **D** _**G**_ **U** _[⊤]_ **D** _**S**_ **z** 1 **b** _←[√] γ_ **z** 2 **c** _←_ **a** + **b Ψ** _←_ **UD** _**G**_ **Q** _←_ **D** _**G**_ **U** _[⊤]_ **D** _**S**_ **UD** _**G**_ + _γ_ **I** _N_ **f** _←_ **Q** _[−]_[1][ �] **Ψ** _[⊤]_ **y** + **c** � (solve with the CGM) **f** _←_ **Ψf Output: f** 

## **6.2.3 Drawing samples for KGR, RNC and KG-RNC** 

So far in this section, we have shown how perturbation optimisation can be used to draw samples from the posterior distribution of the GSR model. Using the same basic strategy, we can also derive algorithms for the KGR, RNC and KG-RNC models. 

## **6.2.3.1 PO with KGR** 

In the case of Kernel Graph Regression (KGR), there is little change from the GSR algorithm. Recall how, as discussed in section 4.1.2, KGR bares a strong algebraic correspondence to GSR. In particular, the posterior distribution over the underlying graph signal **f** is given by 

**==> picture [255 x 14] intentionally omitted <==**

where 

**==> picture [258 x 15] intentionally omitted <==**

The values for **U**[¯] and **D** _**G**_ ¯[are][modified][from][the][GSR][model][as][follows.] 

**==> picture [306 x 13] intentionally omitted <==**

with the elements of _**G**_ given by 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

146 

**==> picture [265 x 19] intentionally omitted <==**

With these modifications in place, we can make use of the same algorithm developed in section 6.2.2, since all the derivations otherwise remain the same. Therefore, in order to sample from the posterior distribution of the KGR model, we can simply reuse algorithm 8, replacing all instances of **U** with **U**[¯] , and all instances of **D** _**G**_ with **D** _**G**_ ¯[.] 

## **6.2.3.2 PO with RNC** 

In the case of Regression with Network Cohesion (RNC), the algorithm must be adjusted. Here, the relevant posterior distribution is over the parameter vector _**θ**_ , rather than the predicted signal **f** . This posterior distribution is given by 

**==> picture [276 x 37] intentionally omitted <==**

where 

**==> picture [345 x 37] intentionally omitted <==**

Recall that we can perform eigendecomposition on the matrix **X** _[⊤]_ **D** _**S**_ **X** as 

**==> picture [105 x 12] intentionally omitted <==**

and additionally define the diagonal matrix **D** _M_ as 

**==> picture [107 x 16] intentionally omitted <==**

Recall also, that the preconditioner used in the case of RNC is 

**==> picture [106 x 37] intentionally omitted <==**

We now present the expression that can be used to sample from the posterior distribution of _**θ**_ in theorem 6.2. 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

147 

**Theorem 6.2.** _Consider the following expression for the vector_ _**θ** ∈_ R _[N]_[+] _[M]_ 

**==> picture [393 x 37] intentionally omitted <==**

_where the matrix_ **Q**[�] _is given by_ 

**==> picture [281 x 36] intentionally omitted <==**

_If z_ 1 _, z_ 2 _∼N_ � **0** _,_ **I** ( _N_ + _M_ )� _, then_ 

**==> picture [133 x 36] intentionally omitted <==**

_Proof._ As in theorem 6.1, it suffices to show that 

**==> picture [194 x 37] intentionally omitted <==**

Note that the following identities hold. 

**==> picture [284 x 34] intentionally omitted <==**

First, let us consider the expected value. Since **E** [ **z** 1] = **E** [ **z** 2] = **0** , these terms do not contribute to the expected value of _**θ**_ . Therefore, **E** [ _**θ**_ ] is given by 

**==> picture [138 x 77] intentionally omitted <==**

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

148 

For the covariance, let us consider each of the three terms within the brackets of eq. (6.32) in isolation. Since the first term has no stochastic component, the covariance of this is zero. For the second term, the covariance is given by 

**==> picture [386 x 185] intentionally omitted <==**

Now consider the covariance of the third term. 

**==> picture [342 x 85] intentionally omitted <==**

Note that these two matrices summed together give 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

149 

**==> picture [282 x 160] intentionally omitted <==**

Note that here we have used the fact that **D** _M_ **Λ** _M_ **D** _M_ + _λ_ **D**[2] _M_[=] **[ I]** _[M]_[.][This][is][true][since] 

**==> picture [174 x 74] intentionally omitted <==**

Therefore, the covariance of the entire expression is given by 

**==> picture [116 x 53] intentionally omitted <==**

We have therefore shown that 

**==> picture [194 x 37] intentionally omitted <==**

completing the proof. 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

150 

Given this expression for _**θ**_ stated in eq. (6.32), a simple procedure for sampling from the posterior distribution of the RNC model is available. This is given in algorithm 9. 

## **Algorithm 9** Draw one sample from the RNC posterior distribution 

**==> picture [258 x 264] intentionally omitted <==**

**Output:** _**θ**_ 

## **6.2.3.3 PO with KG-RNC** 

For the case of Kernel Graph Regression with Network Cohesion (KG-RNC), the situation is algebraically very similar to that of RNC. Just as the algorithm for sampling from the KGR model posterior can be obtained by making a small modification to the GSR case as discussed in section 6.2.3.1, the same is true of KG-RNC, with only a small modification of the RNC algorithm. In particular, the posterior distribution over the parameter vector _**θ**_[ˆ] is given by 

**==> picture [273 x 37] intentionally omitted <==**

where 

**==> picture [345 x 37] intentionally omitted <==**

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

151 

Note that this is the same posterior distribution as in the RNC model, with the objects **U** and _**G**_ replaced by **U**[¯] and _**G**_[¯] . These have the same values as in section 6.2.3.1. In particular 

**==> picture [306 x 13] intentionally omitted <==**

with the elements of _**G**_ given by 

**==> picture [265 x 19] intentionally omitted <==**

Therefore, in order to draw samples from the distribution given in eq. (6.33), we can simply reuse algorithm 9, replacing every instance of **U** with **U**[¯] and every instance of _**G**_ with _**G**_[¯] . 

## **6.3 Variance Estimation: Prediction vs Sampling** 

So far in this chapter, we have addressed estimation of the posterior marginal variance and direct sampling from the posterior as separate objectives. In section 6.1, we proposed several methods based on a supervised learning approach, aiming to predict the entire marginal variance (i.e., the diagonal of the posterior covariance matrix), given our ability to “query” a subset of these matrix elements. On the other hand, in section 6.2, we developed methods for direct sampling from the posterior. However, it’s evident that a valid approach to estimating the marginal variance would be to simply draw samples, using the techniques discussed in section 6.2, and compute the sample variance as an estimator for the population variance. This naturally raises the question of whether this approach is superior to the supervised learning approaches discussed in section 6.1. 

Let us take the Graph Signal Reconstruction model as the primary example. If we have already computed the posterior mean, **f** _[⋆]_ = **P** _[−]_[1] **y** , then an unbiased estimator for the posterior marginal variance based on _K_ samples _{_ **f** _k}[K] k_ =1[is][clearly] 

**==> picture [257 x 30] intentionally omitted <==**

where the exponent is understood as element-wise. In order not to hold all _K_ samples in memory simultaneously, we can write this in recursive form as 

**==> picture [291 x 22] intentionally omitted <==**

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

152 

The relative error of this estimator follows from the properties of the _χ_[2] distribution, and is thus given by 

**==> picture [228 x 25] intentionally omitted <==**

meaning _K_ = 2 _/r_[2] samples are necessary to reduce the relative error to a fraction _r_ . For example, 50 samples would be required to reduce the relative error to 20%. However, one attractive feature of this estimator is that its accuracy is independent of the size of the graph. Whether this is also the case for the supervised learning estimators is not immediately clear. 

## **6.3.1 Experiments** 

In order to investigate the properties of these two approaches to estimating the posterior marginal variance, that is, the supervised learning approaches discussed in section 6.1, and the sample variance approach highlighted in section 6.3, we ran the following experiment. Graphs, comprising the Cartesian product of three random fully-connected sub-graphs, were created in increasing size. For each, we generated a random pattern of missingness _**S**_ by uniformly sampling each element from _{_ 0 _,_ 1 _}_ , and tested the three supervised learning approaches (with active learning), the Bekas diagonal estimator, and the sample-based approach for predicting the posterior marginal variance. As with the experiments in section 6.1.5, we used a diffusion filter with _**β**_ = [0 _._ 5 _,_ 0 _._ 7 _,_ 0 _._ 6] and set _γ_ = 1. Each estimator was given a budget of 50 linear system solves, and its prediction performance was measured by the _R_[2] score. The results are shown in fig. 6.2. 

As visible, RR, RNC and LFP all have similar performance over the range of graph sizes, with _R_[2] never dropping below 0.9. Of the three, LFP once again achieves the highest accuracy, although the difference compared to RR and RNC is fairly small. The sample-based estimator achieves an _R_[2] of around 0.85-0.9 across the range of graph sizes, with performance dropping as low as 0.7 but mostly remaining within this bound. Its performance is also between that of the Bekas diagonal estimator and the three supervised learning techniques over the whole range. 

While the supervised learning estimators are fairly consistent, there is some evidence that their performance is dropping as node number increases. Unfortunately, it is difficult to test this hypothesis since, in order to test the accuracy scores, it is necessary to solve for the entire posterior variance meaning the number of linear system solves required to run this experiment increases rapidly as the number of nodes increases. 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

153 

**==> picture [334 x 250] intentionally omitted <==**

**----- Start of picture text -----**<br>
1.0<br>0.9<br>0.8<br>0.7<br>R [2]<br>0.6<br>0.5<br>RR<br>0.4<br>RNC<br>LFP<br>0.3 Bekas<br>Sample<br>0.2<br>0 5000 10000 15000 20000 25000<br>Number of Nodes<br>**----- End of picture text -----**<br>


Figure 6.2: The predictive performance, as measured by _R_[2] , is shown for the three supervised learning strategies detailed in section 6.1.3, the Bekas diagonal estimator of section 6.1.2, and the sampling strategy of section 6.3. 

## **6.4 Conclusions** 

In this chapter, we have presented a detailed examination of various methods related to the posterior covariance of the tensor GSP models introduced in chapter 5. In the case of GSR, KGR, RNC and KG-RNC, the posterior distribution is a high-dimensional Gaussian with a precision matrix, **P** , characterised by Kronecker-structured operators. The implicit dimensionality of **P** makes direct decomposition and inversion operations challenging, necessitating the use of computationally efficient techniques that avoid the time and memory costs associated with more straightforward approaches. 

We concentrated on two distinct tasks. First, in section 6.1, we aimed to estimate the posterior marginal variance, i.e. the diagonal of **Σ** = **P** _[−]_[1] . In particular, we compared a recent stochastic algorithm devised by Bekas et al. [2007] against three supervised learning-based techniques. This was achieved by first noting that it is possible to compute (or “query”) a subset of the elements of **P** _[−]_[1] directly by solving the linear system **P** _[−]_[1] **e** _n_ , where **e** _n_ is a unit basis vector. Next, by creating a set of artificial explanatory variables associated with each element, the task of estimating the non-queried elements was framed in terms of a traditional supervised learning task. We proposed three separate estimators, namely Ridge Regression (RR), Regression with Network Cohesion (RNC), and Learned Filter Parameters (LFP), for prediction. On a synthetic dataset, all three were capable of achieving high accuracy ( _R_[2] _>_ 0 _._ 99) for a small fraction of 

Chapter 6. _Signal Uncertainty: Estimation and Sampling_ 

154 

the computational cost of computing the marginal variance in full. We also combined this with an active learning strategy which increased prediction accuracy further, especially at low query numbers. 

In section 6.2, we focused on the task of drawing samples directly from the posterior distribution. To achieve this, we made use of a technique known as Perturbation Optimisation (PO) [Orieux et al., 2012], which takes advantage of the special structure of the posterior precision matrix to reduce the computational cost to one linear system solve per sample. By coupling this with the symmetric preconditioner **Ψ** , we were able to remedy the numerical difficulties associated with the algorithm in its basic form to produce an efficient procedure using the CGM. We demonstrated that this procedure yielded the correct posterior distribution for the GSR, RNC, KGR, and KG-RNC algorithms in their general tensor form. 

Finally, in section 6.3, we explored whether the sampling algorithm developed in section 6.2 could serve as an alternative method for estimating the posterior marginal variance. By assessing the prediction accuracy over product graphs of increasing size, we found that the supervised learning techniques typically outperform the sampling strategy. However, for very large graphs, sampling may be preferable, as the relative error is independent of the graph’s size, while the supervised learning techniques show some signs of performance degradation as the number of nodes grows. Further research into this question would be valuable. 

## **Chapter 7** 

## **Reconstruction and Regression with Binary-Valued Graph** 

## **Signals** 

Up to this point in this thesis, our attention has been focused on reconstruction and regression models for real-valued graph signals, as discussed in chapters 3 to 6. In this chapter, we shift our attention to scenarios where the signal of interest is binary-valued, which can be employed to describe node classification tasks conducted over networks. For example, consider the task of predicting whether each user in a social network will engage with a specific online advertisement. Assuming it is shown to a subset of the user population, we can represent the outcome (click/no click) as a partially observed binary graph signal across the network. It is reasonable to assume that closely connected users will exhibit a more similar propensity to click than distantly connected users; in other words, we might expect that the click probability varies smoothly with respect to the topology of the graph. Hence, incorporating this relational information into a predictive task could potentially improve its accuracy. 

This example represents a binary classification task over the network since there are only two possible outcomes. However, there may also be situations in which each node must be classified into one of _C >_ 2 groups. Again, it may be reasonable to assume that the relative class probabilities vary smoothly over the graph. Figures 7.1 and 7.2 give visual representations of binary and multiclass classification tasks over a network, respectively. 

Within the graph signal processing community, a significant amount of research has been dedicated to the study of real-valued signals, since they are naturally well-suited to spectral analysis via the GFT and representation in terms of Gaussian random fields. By contrast, binary-valued graph signals, as well as other discrete or non-Gaussian distributions, have received notably 

155 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

156 

Figure 7.1: An example visualisation of a binary classification task over a network, with red and blue representing the true binary labels of each node. 

Figure 7.2: An example visualisation of a multiclass classification task over a network. Here, the five distinct colours represent the true class label of each node. 

less attention. In the machine learning community, binary graph signals have been studied in the context of semi-supervised learning, see for example Kondor and Lafferty [2002], Zhu et al. [2003]. However, there, the graph is usually constructed by considering a distance metric in a feature space, and the focus is on maximising the utility of unlabelled data using algorithms such as label propagation (see, for example, Zhang et al. [2017]). The GSP community, by contrast, focuses on statistical processes that occur over intrinsically graph-structured objects using spectral methods. While some work on binary reconstruction and regression from this perspective has occurred (see, for example, Tran et al. [2020]), many of the prominent GSP algorithms and frameworks are yet to be generalised to binary data. In this chapter, we build on some of the models already developed in this thesis (GSR, KGR and RNC) to define associated “logistic” reconstruction and regression algorithms (L-GSR, L-KGR and L-RNC). These models are targeted towards applications of interest to the GSP community and apply to multiway graph signals in an arbitrary number of dimensions. This means they are particularly suited to 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

157 

multivariate applications such as hyperspectral image processing, graph time series etc. 

This chapter is structured as follows. First, in section 7.1, we define a model for Logistic Graph Signal Reconstruction (L-GSR) on a Cartesian product graph. Here, we describe how the real-valued multiway GSR framework we developed in chapter 5 can be modified to produce a statistical model to describe _d_ -dimensional binary graph signals. By making use of the Conjugate Gradient Method (CGM) in conjunction with the Iteratively Reweighted Least Squares (IRLS) algorithm, we demonstrate how to efficiently estimate the underlying class probabilities at each node. Next, in section 7.2, we adapt this algorithm to accommodate multiclass classification problems. This necessitates the introduction of a new class of Kronecker operator, which appears in the preconditioned coefficient matrix. Using Gerschgorin’s circle theorem we can provide guarantees for the CGM convergence by ascertaining an upper bound for its condition number. In section 7.3, adapt the Kernel Graph Regression (KGR) and Regression with Network Cohesion (RNC) models developed in chapter 4, and adapt them for the task of binary and multiclass node classification, given additional explanatory variables. Finally, in section 7.4, we explore the behaviour of the L-GSR and L-RNC models on an image segmentation task. In particular, we analyse the interpretation of the hyperparameters _γ_ and _β_ in the context of the logistic models and provide intuition for how these can be set in practice. We also discuss some of the convergence issues associated with the IRLS algorithm and provide practical solutions for mediating them. 

## **7.1 Logistic Graph Signal Reconstruction (L-GSR)** 

In this section, we define a model for the reconstruction of binary signals existing on the nodes of a _d_ -dimensional Cartesian product graph, which we term Logistic Graph Signal Reconstruction (L-GSR). As before, the graph is characterised by _d_ graph Laplacians � **L**[(] _[i]_[)][�] _[d] i_ =1[,][with][the][total] Laplacian given by their Kronecker sum (see section 5.1). The partially observed graph signal, _**Y**_ , is an order- _d_ tensor of shape ( _N_ 1 _, N_ 2 _, .., Nd_ ), with binary-valued elements representing the two classes. This is accompanied by another binary tensor, _**S**_ , of the same shape which, as in previous chapters, contains the information about which elements of _**Y**_ were observed by holding ones where successful observations were made and zeros elsewhere. Where no observation was made (i.e. _**S**_ **n** = 0), the corresponding element _**Y**_ **n** is set to zero by default. The goal is to predict the value of the graph signal at elements where no observation was made using solely the topology of the graph. As such, the input data for this problem can be summarised as follows. 

**==> picture [360 x 25] intentionally omitted <==**

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

158 

In the following, we assume each observed element of the tensor _**Y**_ follows a Bernoulli distribution, according to some underlying latent probability tensor _**M**_ , which specifies the expected value of the outcome at each node. All other elements of _**Y**_ , which were not in the set of observed elements _S_ , are set to zero with probability one. This can be summarised by the following statistical model. 

**==> picture [277 x 43] intentionally omitted <==**

We refer to _**M** ∈_ [0 _,_ 1] _[N]_[1] _[,...,N][d]_ as the mean tensor. It has the same shape as _**Y**_ and elements contained within the interval [0 _,_ 1] describing the probability that the corresponding entry of _**Y**_ is one. For a given mean tensor, _**M**_ , the probability of observing a binary signal _**Y**_ is given by the following expression. 

**==> picture [290 x 23] intentionally omitted <==**

As such, the log-likelihood of observing a signal _**Y**_ , which is simply the natural log of this expression, is given by 

**==> picture [343 x 45] intentionally omitted <==**

where **s** = vecRM ( _**S**_ ) _,_ **y** = vecRM ( _**Y**_ ) and _**µ**_ = vecRM ( _**M**_ ). Here, the logarithm function is understood as being applied element-wise. 

The goal of our L-GSR model is to estimate the value of the latent probability tensor _**M**_ given the partially observed binary graph signal _**Y**_ . The key assumption that anchors the model to the graph, and avoids underspecification, is that the probability tensor varies smoothly with respect to the topology of the Cartesian product graph. In previous chapters, when working with realvalued signals, this was achieved by setting a Gaussian prior over the latent signal _**F**_ . However, since the elements of _**M**_ fall within the interval [0 _,_ 1], we need a distribution that naturally supports this range. To achieve this, we follow the approach of standard logistic regression (see, for example, Murphy [2012]), by describing the probability in terms of a logistic link function. In particular, we assume that the mean tensor, _**M**_ , is generated by applying the logistic function to a real-valued tensor graph signal _**F** ∈_ R _[N]_[1] _[×][...][×][N][d]_ as follows. 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

159 

**==> picture [327 x 24] intentionally omitted <==**

Here, the exponential and division should be interpreted as element-wise. Next, we assume that **f** = vecRM ( _**F**_ ) is smooth with respect to the topology of the graph by assigning it the following Gaussian prior. 

**==> picture [250 x 13] intentionally omitted <==**

As in previous chapters, the covariance matrix **H**[2] is the square of a graph filter operator, derived by applying a filter function _g_ ( _·_ ) to the product graph Laplacian. In particular, 

**==> picture [62 x 12] intentionally omitted <==**

where **U** is the Kronecker product of each of the eigenvector matrices of the individual factor graph Laplacians, and **DG** = diag (vecRM ( _**G**_ )) is the diagonalised spectral scaling tensor, created by applying an isotropic or anisotropic graph filter to the corresponding eigenvalues (see sections 5.1 and 5.1.3 for details). 

By applying this prior we encode the belief that _**F**_ is smooth with respect to the topology of the graph, which is then applied by proxy to the mean tensor _**M**_ . In particular, _**µ**_ is distributed on [0 _,_ 1] _[N]_ according to a multivariate logit-normal distribution. Note that this is distinct from the multivariate logistic-normal distribution, which is produced by applying a softmax function to a random Gaussian vector to produce vectors on a simplex [Atchinson and Shen, 1980]. Figure 7.3 gives some visual intuition for this by showing a colourmap of several smooth signals on a 2D lattice graph, along with the corresponding mean tensor _**M**_ . As visible, the qualitative smoothness properties of _**F**_ broadly translate under the transformation of the logistic link function. That is, increasingly smooth real-valued signals correspond to increasingly smooth signals on the unit interval. 

As previously stated, the goal of the L-GSR model is to find the most likely value of _**M**_ given _**Y**_ . Since we have a prior distribution over _**F**_ , we can derive an equation for its posterior distribution given _**Y**_ through the application of Bayes’ rule. The Maximum A Posteriori (MAP) estimator for _**F**_ corresponds to the value that minimises the negative log-likelihood of _**F** |_ _**Y**_ . Given the MAP estimator for _**F**_ , we can compute the most likely mean tensor _**M**_ by applying eq. (7.4). To this end, we define the objective function _ξ_ ( **f** ), which is equal to _−_ log _p_ ( **f** _|_ **y** ) up to an additive constant. 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

160 

**==> picture [282 x 328] intentionally omitted <==**

**----- Start of picture text -----**<br>
F M Most likely classification<br>ae<br>EE,<br>2 0 2 0.00 0.25 0.50 0.75 1.00 0 1<br>**----- End of picture text -----**<br>


Figure 7.3: An example visualisation of transforming a smooth signal via the logistic link function, on a 100 _×_ 100 grid of pixels ( _N_ 1 = 100 _, N_ 2 = 100). Left: a random smooth graph signal _**F**_ drawn from the distribution of eq. (7.5) with a diffusion filter. Middle: the value of the tensor _**M**_ found by applying the logistic link function of eq. (7.4). Right: the resultant most likely classification given by _**M**_ **n** _>_ 0 _._ 5 each pixel, **n** . Each row shows an increasingly smooth signal by increasing the value of _β_ characterising the graph filter. 

**==> picture [348 x 19] intentionally omitted <==**

The goal of the next section is to find an algorithm for minimising this expression with respect to **f** , i.e. to find the MAP estimator for _**F**_ , and subsequently compute the most likely value of the mean tensor _**M**_ . 

## **7.1.1 Solving for the MAP estimator with the IRLS algorithm** 

Unlike the normal models of the previous sections, no closed-form solution exists to minimise eq. (7.6), meaning we must resort to numerical methods. One standard approach is the Iteratively 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

161 

Reweighted Least Squares (IRLS) algorithm. The IRLS algorithm is a numerical method used to solve certain non-linear optimisation problems. It essentially works by iteratively solving a sequence of weighted least squares sub-problems until a satisfactory solution is found. As we will show, in our case, this is particularly attractive, since it is possible to leverage the properties of the Kronecker product to solve these simpler sub-problems efficiently. 

In the context of maximum likelihood estimation for generalised linear models, the IRLS algorithm is equivalent to Fisher’s scoring algorithm, which is a variant of the Newton-Raphson method [Nelder and Wedderburn, 1972]. Instead of using the actual Hessian matrix (second derivative of the log-likelihood), Fisher’s scoring algorithm uses its expected value, called the Fisher Information matrix. In this setting, each iteration of the IRLS algorithm involves reweighting the data based on the current estimate of the parameters, then solving a weighted least squares problem to update the parameters, akin to the update step in Fisher Scoring [Fan et al., 2020]. 

Fisher’s scoring algorithm begins with an initial estimate **f** 0, which is then iteratively refined to reach the global minimum according to the following formula. 

**==> picture [264 x 13] intentionally omitted <==**

where **g** ( **f** ) _∈_ R _[N]_ is the gradient of the optimisation objective _ξ_ ( **f** ) with respect to the vector **f** , and **P** ( **f** ) _∈_ R _[N][×][N]_ is the Hessian, which is the matrix of second derivatives. 

**==> picture [157 x 24] intentionally omitted <==**

In our case, the gradient is given by 

**==> picture [276 x 14] intentionally omitted <==**

and the Hessian is given by 

**==> picture [278 x 22] intentionally omitted <==**

where **D** _**µ**_ ( **f** ) is a diagonal matrix with the following definition. 

**==> picture [286 x 13] intentionally omitted <==**

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

162 

A derivation of the expressions for both the gradient and the Hessian in this context can be found in theorem A.8. Note that they are both evaluated at a given **f** . 

Consider the update formula given in eq. (7.7). Substituting in the derived values of **g** ( **f** ) and **P** ( **f** ), and using the shorthands 

**==> picture [273 x 14] intentionally omitted <==**

gives 

**==> picture [214 x 138] intentionally omitted <==**

where 

**==> picture [265 x 13] intentionally omitted <==**

As visible, each iteration of the IRLS algorithm reduces to solving the linear system **P** _[−] k_[1] **[t]** _[k]_[,][for] some vector **t** _k_ . As such, we must be able to compute a solution to this problem in a maximally efficient way. 

## **7.1.2 Completing IRLS iterations with the CGM** 

When it comes to solving the linear system **P** _[−] k_[1] **[t]** _[k]_[,][we][encounter][familiar][challenges][relating] to dimensionality and conditioning. Specifically, the implicit size of **P** _k_ can be substantial for tensor-valued graph signals, and the inverse-squared filter matrix **H** _[−]_[2] appearing in the definition of **P** _k_ [see eq. (7.9)] may suffer from severe ill-conditioning. In a similar manner to previous chapters, these issues can be overcome by employing the SIM or CGM techniques introduced in sections 3.2.2 and 3.2.3. 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

163 

In this chapter, our focus will be on the CGM for two primary reasons. Firstly, as the dimensionality of tensor-valued binary graph signals increases, it is likely that only a small fraction of nodes will have valid observed data in most practical applications. As demonstrated in section 3.3.3, the CGM exhibits superior scaling properties when the input graph signal _**Y**_ is sparsely observed. Secondly, as discussed in section 4.2.2, the CGM is applicable to GSR, KGR and RNC problems while the SIM is not suitable for RNC models. Therefore, for simplicity, and for the sake of brevity we focus on the CGM. 

Recall that the CGM seeks to solve a linear system by introducing the symmetric preconditioner **Ψ** , to reduce the condition number of the coefficient matrix. In the case of logistic GSR, we can obtain an alternative expression for the update formula with a reduced condition number as follows. 

**==> picture [167 x 13] intentionally omitted <==**

where, as in the case of standard real-valued GSR, 

**==> picture [47 x 10] intentionally omitted <==**

By instead solving the linear system **Q** _[−] k_[1][(] **[Ψ]** _[⊤]_ **[t]** _[k]_[) using the conjugate gradient method, and then] left-multiplying the result by **Ψ** , we can obtain **f** _k_ +1 with typically far fewer iterative steps than solving **P** _[−]_[1] **t** _k_ directly. In this case, **Q** _k_ is given by the following expression. 

**==> picture [271 x 13] intentionally omitted <==**

Note that this is similar to the preconditioned coefficient matrix appearing in standard GSR, with the modification that **D** _**S**_ has been replaced by **D** _[k]_ _**µ**_[.] 

The conditioning of the new coefficient matrix **Q** _k_ is significantly improved from the original problem. While the condition number, _κ_ , of **P** _k_ was potentially unbounded, _κ_ ( **Q** _k_ ) is guaranteed to have a maximum value of (0 _._ 25 + _γ_ ) _/γ_ . This is shown formally in theorem 7.1. 

**Theorem 7.1.** _The condition number, κ, of the preconditioned coefficient matrix_ **Q** _k, defined in eq._ (7.12) _, is bounded as follows._ 

**==> picture [248 x 23] intentionally omitted <==**

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

164 

_Proof._ As established in section 3.3.1, the worst-case convergence rate is achieved in the limit of a weak filter, where **D** _**G**_ = **I** _N_ . In this case, the condition number of **Q** _k_ is given by 

**==> picture [140 x 61] intentionally omitted <==**

Since **D** _[k]_ _**µ**_[=][diag] � **s** _◦_ _**µ** k ◦_ ( **1** _−_ _**µ** k_ )�, the maximum possible value along the diagonal of **D** _[k]_ _**µ**_ will be 0.25, occurring when the corresponding element of _**µ** k_ is 1 _/_ 2. Furthermore, since **s** is a binary vector, the smallest possible value along the diagonal is 0. Therefore, the ratio between the largest and smallest eigenvalues of **D** _[k]_ _**µ**_[+] _[ γ]_ **[I]** _[N]_[must][be][less][than][or][equal][to][(0] _[.]_[25 +] _[ γ]_[)] _[/γ]_[.] 

For completeness, we now give the full algorithm for logistic graph signal reconstruction in algorithm 10. Note that, by making use of the fast Kronecker product algorithm described in section 5.1.3, the runtime complexity of the CGM step is bounded by 

**==> picture [102 x 30] intentionally omitted <==**

The run time complexity of the overall algorithm of course depends on the convergence rate of the IRLS iterations. This is known to be super-linear, and approximately quadratic when a sufficiently accurate starting value is used [Burden and Faires, 2010]. Whilst an in-depth theoretical exploration of the IRLS algorithm for this particular application is beyond the scope of this chapter, in practice, the IRLS algorithm converges very quickly, usually taking on the order of 10 steps to achieve negligible error. 

## **7.2 Multiclass Logistic Graph Signal Reconstruction** 

So far we have been focused on binary-valued graph signals, which can be used to represent two-class classification tasks over a multiway network. However, in many practical applications, the task may involve classifying each node into one of multiple distinct groups. Therefore, the objective of this section is to extend and generalise the methods we have developed thus far to encompass multiclass classification problems. 

Consider the task of multiclass graph signal reconstruction. Here, the goal is to estimate the probability that each node, **n** , in a _d_ -dimensional Cartesian product graph belongs to each of _C >_ 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

165 

**Algorithm 10** Logistic Graph Signal Reconstruction 

**Input:** Observed binary tensor _**Y** ∈{_ 0 _,_ 1 _}[N]_[1] _[×][...][×][N][d]_ **Input:** Binary sensing tensor _**S** ∈{_ 0 _,_ 1 _}[N]_[1] _[×][...][×][N][d]_ **Input:** Cartesian product graph Laplacians � **L**[(] _[i]_[)] _∈_ R _[N][i][×][N][i]_[�] _[d] i_ =1 **Input:** Regularisation parameter _γ ∈_ R[+] **Input:** Graph filter function _g_ ( _·_ ; _**β**_ ) 

**y** _←_ vecRM ( _**Y**_ ) **s** _←_ vecRM ( _**S**_ ) Decompose each **L**[(] _[i]_[)] into **U**[(] _[i]_[)] **Λ**[(] _[i]_[)][ �] **U**[(] _[i]_[)][�] _[⊤]_ **U** _←_[�] **U**[(] _[i]_[)] Compute _**G** ∈_ R _[N]_[1] _[×][...][×][N][d]_ as _**G**_ **n** = _g_ � _**λ**_ ( **n** ); _**β**_ � (see eqs. (5.20) and (5.21)) **D** _**G** ←_ diag (vecRM ( _**G**_ )) **D** _**S** ←_ diag ( **s** ) **Ψ** _←_ **UD** _**G**_ Initialise **f** _∈_ R _[N]_ randomly **while** _|_ ∆ **f** _| >_ tol **do** 

**==> picture [340 x 85] intentionally omitted <==**

**end while** 

_**µ** ←_ **1** _/_ � **1** + exp( _−_ **f** )� **Output:** reshape� _**µ** ,_ ( _N_ 1 _, ...Nd_ )� 

2 distinct classes. To do this, we have access to the factor graph Laplacians � **L**[(] _[i]_[)] _∈_ R _[N][i][×][N][i]_[�] _[d] i_ =1[,] and the true class label at a subset of nodes, _S_ . The partially observed class labels can be represented as an order-( _d_ + 1) tensor graph signal, where the final dimension contains a “onehot” encoding of the class label. As such, the input data for multiclass L-GSR can be summarised as follows. 

**==> picture [372 x 22] intentionally omitted <==**

As in previous sections, the tensor _**S**_ , of shape ( _N_ 1 _× ... × Nd_ ), indicates which nodes in the product graph have been successfully observed by holding a one in the corresponding entry, and zeros elsewhere. Note that the observed graph signal, _**Y**_ , has an additional dummy dimension of length _C_ to represent the class label, which is not present in _**S**_ . Where no observation was made 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

166 

(i.e. _**S**_ **n** = 0), all values along the corresponding fibre _**Y**_ **n** _,_ : can be safely set to zero by default. Note that _**Y**_ **n** _,_ : can have a maximum of one non-zero entry. 

We describe the probability that node **n** has class _c_ by introducing another tensor, _**M**_ . Like _**Y**_ , this tensor has shape ( _N_ 1 _× ... × Nd × C_ ). Each fibre _**M**_ **n** _,_ : is interpreted as the probability mass function over the _C_ mutually exclusive classes at node **n** . In particular, 

**==> picture [208 x 30] intentionally omitted <==**

Since every length- _C_ fibre _**M**_ **n** _,_ : must sum to one, the tensor _**M**_ exists in the space of _N_ independent _C_ -dimensional simplexes with _C −_ 1 degrees of freedom. 

This implies that, for a given value of _**M**_ , the probability of observing a signal _**Y**_ is given by 

**==> picture [263 x 24] intentionally omitted <==**

As such, the log-likelihood of observing a signal _**Y**_ , for a given value of _Mt_ , is 

**==> picture [288 x 45] intentionally omitted <==**

where, as before, **s** = vecRM ( _**S**_ ) _,_ **y** = vecRM ( _**Y**_ ) and _**µ**_ = vecRM ( _**M**_ ). Furthermore, to enforce the restriction that all probabilities must sum to one, we can generate _**M**_ by applying a softmax function to each length- _C_ fibre of a tensor _**F**_ . 

**==> picture [362 x 28] intentionally omitted <==**

Here, _**F**_ is a real-valued tensor signal which, like _**M**_ and _**Y**_ , has shape ( _N_ 1 _× ... × Nd × C_ ). A graphical representation of the relation between _**F**_ , _**M**_ and the most likely classification is shown in fig. 7.4. The goal, then, of multiclass logistic graph signal reconstruction is to find the most likely value for the tensor _**F**_ , which allows us to make a prediction for the probability of each class by applying eq. (7.16). 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

167 

**==> picture [360 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
F M Most likely classification<br>**----- End of picture text -----**<br>


Figure 7.4: An example visualisation of transforming a smooth tensor signal via the softmax function on a 20 _×_ 20 grid of pixels ( _N_ 1 = 20 _, N_ 2 = 20 _, C_ = 3). Left: a random smooth tensor signal _**F**_ , drawn from the Gaussian distribution specified in eq. (7.17), split across three channels. Middle: the value of the tensor _**M**_ found by applying the softmax function of eq. (7.16) in the class dimension. Right: the resultant most likely classification given by the maximum probability class label for each pixel. 

Assuming no particular relational structure between the _C_ classes, we can encode the assumption that class probabilities should vary smoothly over the graph by assigning the following prior to _**F**_ . 

**==> picture [263 x 13] intentionally omitted <==**

By applying Bayes’ rule, we can therefore derive an expression _ξ_ ( **f** ), representing the negative log-likelihood of observing an underlying signal **f** given an observed signal **y** . 

**==> picture [325 x 19] intentionally omitted <==**

Once again, we can solve for the minimising value of **f** using the IRLS algorithm. In this case, the gradient and Hessian are respectively given by 

**==> picture [310 x 13] intentionally omitted <==**

and 

**==> picture [269 x 13] intentionally omitted <==**

Unlike the binary model where the Hessian was the sum of a diagonal matrix **D** _**µ**_ ( **f** ) and _γ_ **H** _[−]_[2] , the matrix **R** _**µ**_ ( **f** ) is no longer diagonal. In this case, **R** _**µ**_ ( **f** ) is given by 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

168 

**==> picture [341 x 31] intentionally omitted <==**

where **m** _n ∈_ R _[C]_ is the probability mass function at node _n_ (i.e. the _n_ -th lexicographically ordered fibre within the tensor _**M**_ ), and **∆** _n_ is a matrix of zeros, with a single one at element ( _n, n_ ). Given the definition of the Kronecker product, we can see that **R** _**µ**_ ( **f** ) is a block-diagonal matrix with the following structure. 

**==> picture [324 x 73] intentionally omitted <==**

Despite no longer being diagonal, we can still leverage the block structure of this matrix to multiply **R** _**µ**_ ( **f** ) onto an arbitrary vector, **v** , efficiently. This can be achieved as follows. 

**==> picture [361 x 19] intentionally omitted <==**

While a naive implementation of the product **R** _**µ**_ ( **f** ) **v** would have memory time and memory complexity _O_ � _C_[2] _N_[2][�] , by following the formula given in eq. (7.22), it can instead be achieved with time complexity _O_ ( _NC_[2] ) and memory complexity _O_ ( _NC_ ). 

Now consider the IRLS update formula. As before, we will use the following shorthands. 

**==> picture [273 x 14] intentionally omitted <==**

Applying the update formula gives 

**==> picture [284 x 145] intentionally omitted <==**

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

169 

where 

**==> picture [145 x 14] intentionally omitted <==**

As before, we can solve the linear system **P** _[−] k_[1] **[t]** _[k]_[by][introducing][a][symmetric][preconditioner] **[Ψ]**[.] The only modification is that it must be of dimension ( _NC × NC_ ), rather than ( _N × N_ ). This can be achieved as follows. 

**==> picture [77 x 11] intentionally omitted <==**

Using this, we can transform the linear system into 

**==> picture [167 x 13] intentionally omitted <==**

where 

**==> picture [307 x 15] intentionally omitted <==**

Once again, the effect of introducing this preconditioner is to radically improve the conditioning of the coefficient matrix. Again, while the condition number, _κ_ , of **P** _k_ is potentially unbounded, _κ_ ( **Q** _k_ ) can be strongly bounded. In particular, it is guaranteed to have a maximum value of (0 _._ 5+ _γ_ ) _/γ_ . The proof, which is somewhat more involved than the binary case, is given formally in theorem 7.2. 

**Theorem 7.2.** _The condition number of_ **Q** _k is bounded by a maximum value of_ 

**==> picture [245 x 23] intentionally omitted <==**

_Proof._ As established in section 3.3.1, the worst-case convergence rate is achieved in the limit of a weak filter, where **D** _**G**_ = **I** _N_ . In this case, the condition number of **Q** _k_ is given by 

**==> picture [204 x 68] intentionally omitted <==**

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

170 

Since **R** _[k]_ _**µ**_[is][block-diagonal,][the][set][of][associated][eigenvalues][is][equal][to][the][union][of][the][eigen-] values of each individual block. Furthermore, each block within **R** _[k]_ _**µ**_[is][of][the][form] 

**==> picture [114 x 19] intentionally omitted <==**

where **m** _∈_ R _[C]_ is a probability mass vector, and _s_ is either zero or one. For the case where _s ̸_ = 0, we can see that **B** must have at least one zero eigenvalue, with eigenvector **1** , since 

**==> picture [124 x 57] intentionally omitted <==**

Note, we have used the fact that **m** _[⊤]_ **1** = 1, since **m** represents a probability mass function and must therefore sum to one. Furthermore, we can show that all eigenvalues of **B** must be within the interval [0 _,_ 1 _/_ 2], no matter the value of **m** . To achieve this, we can make use of the Gerschgorin circle theorem [Gerschgorin, 1931]. This states that all eigenvalues of a square matrix must fall within at least one of the closed disks _D_ ( _aii, Ri_ ) _⊂_ C in the complex plane. Here, _aii_ are the centres of the disks given by the diagonal elements of the matrix, and _Ri_ are the radii of the disks, given by 

**==> picture [59 x 24] intentionally omitted <==**

i.e. the sum of the absolute value of the off-diagonal elements in row _i_ . Consider the structure of **B** when _s ̸_ = 0. 

**==> picture [286 x 73] intentionally omitted <==**

where _m_ = [ _m_ 1 _, m_ 2 _, ..., mC_ ]. The disk associated with row _c_ will be given by 

**==> picture [282 x 37] intentionally omitted <==**

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

171 

In our particular scenario, the matrix **B** is symmetric-real, guaranteeing that its eigenvalues are real. This implies that, instead of complex regions, each of these disks represents a real interval. As such, every eigenvalue is constrained to fall within the interval _mc_ (1 _− mc_ ) _± mc_ (1 _− mc_ ) = �0 _,_ 2 _mc_ (1 _− mc_ )�. The maximum width of this interval occurs when _mc_ = 0 _._ 5, resulting in an interval of [0 _,_ 0 _._ 5]. Consequently, the largest possible eigenvalue of matrix **B** is 0.5. 

Finally, since **R** _[k]_ _**µ**_[is][composed][of][blocks] **[B]** _[n]_[,][this][means][the][largest][possible][eigenvalue][of] **[R]** _[k]_ _**µ**_[is] 0.5, and the smallest is zero. Therefore 

**==> picture [107 x 24] intentionally omitted <==**

completing the proof. 

We now present the full algorithm for logistic graph signal reconstruction, which is given in algorithm 10. Note that, by making use of the fast Kronecker product algorithm described in section 5.1.3, the runtime complexity of the CGM step is bounded by 

**==> picture [136 x 31] intentionally omitted <==**

## **7.3 Logistic Graph Signal Regression** 

So far in this chapter, we have developed binary and multiclass multiway graph signal reconstruction algorithms, where no additional data exists to help predict the value of the graph signal at the unlabelled nodes. In this section, we explore several circumstances where explanatory variables are at our disposal and propose models to leverage this information to estimate the underlying class label probabilities. 

## **7.3.1 Logistic Kernel Graph Regression (L-KGR)** 

The first regression models we consider are binary and multiclass Logistic Kernel Graph Regression (L-KGR). The goal of L-KGR is to predict the underlying class probabilities at the nodes of a sequence of multiway graph signals, given that each signal is paired with an associated vector of explanatory variables. In this respect, it parallels the real-valued KGR model introduced in section 4.1 (and extended to general tensor signals in section 5.3), except here we are concerned 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

172 

**Algorithm 11** Multiclass Logistic Graph Signal Reconstruction 

**==> picture [413 x 395] intentionally omitted <==**

_**µ** ←_ exp( **f** ) _/_ �( **I** _N ⊗_ **1** _C_ ) exp( **f** )� _⊗_ **1** _C_ **Output:** reshape� _**µ** ,_ ( _N_ 1 _, ..., Nd, C_ )� 

with classification rather than real-valued regression. As we will demonstrate, mirroring the pattern of previous sections, the L-KGR model can be interpreted as a relatively straightforward extension of logistic graph signal reconstruction. 

## **7.3.1.1 Binary L-KGR** 

First, let us consider binary L-KGR. In this case, we have a sequence of _T_ partially observed binary tensor graph signals, _**Y** t_ , each with a shape of ( _N_ 1 _, ..., Nd_ ). As before, each signal is interpreted as existing on the nodes of a _d_ -dimensional Cartesian product graph, with factor graph Laplacians � **L**[(] _[i]_[)] _∈_ R _[N][i][×][N][i]_[�] _[d] i_ =1[.][Where][no][class][outcome][was][recorded,][the][relevant][element][in] the signal _**Y** t_ can default to zero. Furthermore, at each time instant, we have a length- _M_ vector 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

173 

of explanatory variables **x** _t_ , which is anticipated to have some non-linear explanatory relation to each _**Y** t_ . 

The sequence of partially observed signals can be assembled into a single tensor _**Y**_ of shape ( _T, N_ 1 _, ..., Nd_ ). This is accompanied by a binary sensing tensor, _**S**_ , of the same shape, which indicates which values were observed and which were absent. The explanation variables can also be aggregated into a single object, in this case, a matrix **X** with a shape of ( _T, M_ ). The goal is to leverage the explanatory variables, in conjunction with the topology of the underlying graph, to estimate the class probability at each node, at each time instant. The relevant input data can therefore be described as follows. 

**==> picture [231 x 31] intentionally omitted <==**

**==> picture [208 x 31] intentionally omitted <==**

Following the same pattern as the KGR algorithms of previous sections (see section 4.1.2 for details and further explanation), we can conveniently derive a logistic kernel graph regression model by making small modifications to the L-GSR model derived in section 7.1. 

As with L-GSR, we first assume each element of _**Y**_ is distributed according to a Bernoulli distribution, with a mean given by a latent mean tensor _**M**_ , which has the same shape as _**Y**_ (see eqs. (7.1) to (7.3)). However, in this case, we assume that _**M**_ is smooth with respect to both the topology of the graph, _and_ with respect to the feature space. (This is admittedly a somewhat vague statement on its own - see section 4.1 for a more detailed model derivation and section 4.1.2 for further intuition). This belief can be encoded by proxy via a tensor _**F**_ , which is again related to _**M**_ via the logistic link function of eq. (7.4). We implement these assumptions by establishing the following prior distribution for **f** = vecRM ( _**F**_ ). 

**==> picture [257 x 13] intentionally omitted <==**

As before, **K** is the _T × T_ kernel matrix created by applying a symmetric function, such as the Gaussian kernel, _κ_ ( _·, ·_ ) to pairs of feature vectors such that **K** _ij_ = _κ_ ( **x** _i,_ **x** _j_ ). Next, we compute the eigendecomposition of **K** as **K** = **VΛ** _K_ **V** _[⊤]_ . Finally, we define the transformed variables **U**[¯] and _**G**_[¯] as follows. 

**==> picture [291 x 19] intentionally omitted <==**

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

174 

where _λ_[(] _t[K]_[)] is the _t_ -th eigenvalue of **K** . This implies that 

**==> picture [252 x 13] intentionally omitted <==**

where **D** _**G**_ ¯[=][diag] �vecRM � _**G**_ ¯��. The L-KGR algorithm then follows by modifying algorithm 10 such that every instance of **U** and _**G**_ is substituted for **U**[¯] and _**G**_[¯] respectively. Note that, as with the KGR models of previous sections, this has an impact on the convergence rate of the CGM step, since the condition number of the preconditioned coefficient matrix **Q** _k_ is increased. As a result, the upper bound on the run time complexity for the whole algorithm is given by 

**==> picture [318 x 31] intentionally omitted <==**

## **7.3.1.2 Multiclass L-KGR** 

The same principles can be used to generate a multiclass logistic kernel graph regression algorithm. In this case, the input data is a sequence of _T_ partially observed multiway graph signals, where each observed node has been classified into one of _C >_ 2 classes. This can be represented by the binary tensor _**Y**_ with shape ( _T × N_ 1 _× ... × Nd × C_ ), where an extra dimension has been added containing a one-hot encoding of the class label. Where no data was recorded, the full length- _C_ fibre at time _t_ and node **n** can be set to zero. As such, the data is described as follows. 

**==> picture [243 x 31] intentionally omitted <==**

**==> picture [208 x 31] intentionally omitted <==**

Just as with the multiclass L-GSR model derived in section 7.2, we introduce the tensor _**M**_ , with the same shape as _**Y**_ , where each length- _C_ fibre _**M** t,_ **n** _,_ : describes the probability mass function over the _C_ classes for node **n** at time _t_ . As before, _**M**_ is constructed by applying a softmax function to each fibre of another tensor _**F**_ . 

**==> picture [383 x 28] intentionally omitted <==**

We then place a prior over the signal **f** = vecRM ( _**F**_ ) _∈_ R _[T NC]_ of 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

175 

**==> picture [268 x 13] intentionally omitted <==**

This encodes the belief that each of the _c_ class probabilities should vary smoothly (and independently) with respect to the topology of the graph and the feature space. once again, the full procedure for outputting the tensor _**M**_ can be achieved by running algorithm 11 after substituting the variables **U** _→_ **U**[¯] and _**G** →_ _**G**_[¯] , as described in eq. (7.26). Given the effect this substitution has on the preconditioned coefficient matrix **Q** _k_ appearing in each iteration of the IRLS algorithm, it is simple to show that the run time complexity of multiclass L-KGR becomes bounded by the following. 

**==> picture [362 x 31] intentionally omitted <==**

## **7.3.2 Logistic Regression with Network Cohesion (L-RNC)** 

In this section, we present models for binary and multiclass Logistic Regression with Network Cohesion (L-RNC). These models are relevant when there is a _d_ -dimensional Cartesian product graph, for which a subset of nodes have a known class label. In addition, each node has a length- _M_ vector of explanatory variables. The goal is to utilise both the topology of the graph and the explanatory variables to estimate the class probabilities at the unlabelled nodes. 

## **7.3.2.1 Binary L-RNC** 

First, let us consider binary L-RNC. In this scenario, we encounter a partially observed binary multiway graph signal _**Y**_ , with shape ( _N_ 1 _× ... × Nd_ ), where a subset of the nodes have been labelled with the true class. As before, _**Y**_ is interpreted as existing on the nodes of a known Cartesian product graph, with factor Laplacians � **L**[(] _[i]_[)] _∈_ R _[N][i][×][N][i]_[�] _[d] i_ =1[.][In][addition,][each][node] **[n]** in the product graph has an associated length- _M_ vector of explanatory variables, collected into the tensor _**X**_ with shape ( _N_ 1 _× ... × Nd × M_ ). The goal is to predict the class probabilities at each node **n** . Once again, we also have a binary tensor _**S**_ describing which nodes have been observed. As such, the data for the binary L-RNC algorithm can be summarised as follows. 

**==> picture [254 x 31] intentionally omitted <==**

**==> picture [196 x 31] intentionally omitted <==**

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

176 

As with the L-GSR model, we suppose that each observed element of _**Y**_ is a Bernoulli random variable, with the probability of success given by the tensor _**M** ∈_ [0 _,_ 1] _[N]_[1] _[×][...][×][N][d]_ . However, in the L-RNC model, we assume that the probability at each node is given by the logistic function applied to the sum of an intercept term and a linear combination of the explanatory variables at that node. As with the real-valued RNC model introduced in section 4.2, the intercept term is flexible and assumed to vary smoothly with respect to the topology of the product graph. Denoting _**µ**_ = vecRM ( _**M**_ ), this is summarised by the following expression. 

**==> picture [282 x 25] intentionally omitted <==**

Here, **c** = vecRM ( _**C**_ ) is the real-valued vector form of a tensor _**C**_ , which is assumed to vary smoothly with respect to the topology of the multiway graph, **X** is the tensor of explanatory variables reshaped into a matrix of dimensions ( _N × M_ ) (see eq. (5.49)), and **w** _∈_ R _[M]_ is the length- _M_ vector of coefficients specifying the contribution of each of the explanatory variables. As in previous sections on RNC, we can stack **c** and **w** into a single parameter vector _**θ**_ , such that 

**==> picture [275 x 25] intentionally omitted <==**

Furthermore, we can place a prior over _**θ**_ that encodes the belief that _**C**_ should be smooth with respect to the topology of the Cartesian product graph, as well as preventing overfitting of **w** with an L2 penalty. 

**==> picture [283 x 36] intentionally omitted <==**

As such, the MAP estimator for _**θ**_ is given by the minimiser of the following expression. 

**==> picture [394 x 37] intentionally omitted <==**

Proceeding in the same way as L-GSR, we must compute both the gradient, **g** �( _**θ**_ ), and the Hessian, **P**[�] ( _**θ**_ ), of this expression with respect to _**θ**_ . These are given by 

**==> picture [344 x 37] intentionally omitted <==**

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

177 

and 

**==> picture [353 x 37] intentionally omitted <==**

where, as with L-GSR, **D** _**µ**_ is the diagonal _N × N_ matrix given by 

**==> picture [288 x 13] intentionally omitted <==**

Then, using the shorthands 

**P** � ( _**θ** k_ ) = **P** � _k,_ **g** �( _**θ** k_ ) = � **g** _k,_ _**µ**_ ( _**θ** k_ ) = _**µ** k,_ and **D** _**µ**_ ( _**θ** k_ ) = **D** _[k]_ _**µ**_ 

the IRLS update formula can be derived as follows. 

**==> picture [320 x 235] intentionally omitted <==**

where 

**==> picture [299 x 37] intentionally omitted <==**

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

178 

Note that, in the derivation above, we have used the fact that **D** _**S**_ **D** _[k]_ _**µ**_[=] **[D]** _[k]_ _**µ**_ **[D]** _**[S]**_[=] **[D]** _[k]_ _**µ**_[.][This] implies that 

**==> picture [202 x 37] intentionally omitted <==**

As before, the linear system **P**[�] _[−] k_[1][�] **[t]** _[k]_[cannot][easily][be][solved][in][this][form][due][to][ill-conditioning.] To overcome this issue, we can again use the symmetrically preconditioned CGM. In particular, we can transform the system into 

**==> picture [175 x 14] intentionally omitted <==**

In order to define **Ψ**[�] _k_ and **Q**[�] _k_ , first we must compute the eigendecomposition of **X** _[⊤]_ **D** _[k]_ _**µ**_ **[X]**[.] 

**==> picture [268 x 14] intentionally omitted <==**

Next, we define the matrix **D** _[k] M_[as][follows.] 

**==> picture [262 x 16] intentionally omitted <==**

Then, the operators **Ψ**[�] _k_ and **Q**[�] _k_ are defined as follows. 

**==> picture [263 x 37] intentionally omitted <==**

and 

**==> picture [333 x 37] intentionally omitted <==**

Note that, in contrast to L-GSR, the preconditioning matrix **Ψ**[�] _k_ is changing on each iteration of the IRLS algorithm. We now have all the mechanics in place to compute the value of _**θ**_ that minimised eq. (7.33). This, in turn, can be used to compute _**M**_ , according to eq. (7.31). For clarity, we now present the complete L-RNC algorithm in algorithm 12. Once again, we expect the IRLS iterations to quickly converge. As such, the main computational bottleneck occurs in solving the CGM, which can be achieved efficiently by leveraging the Kronecker and block structure of the matrix **Q** _k_ . 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

179 

**Algorithm 12** Logistic Regression with Network Cohesion 

**Input:** Explanatory variables _**X** ∈_ R _[N]_[1] _[×][...][×][N][d][×][M]_ **Input:** Observed binary tensor _**Y** ∈{_ 0 _,_ 1 _}[N]_[1] _[×][...][×][N][d]_ **Input:** Binary sensing tensor _**S** ∈{_ 0 _,_ 1 _}[N]_[1] _[×][...][×][N][d]_ **Input:** Cartesian product graph Laplacians � **L**[(] _[i]_[)] _∈_ R _[N][i][×][N][i]_[�] _[d] i_ =1 **Input:** Regularisation parameter _γ ∈_ R[+] **Input:** Graph filter function _g_ ( _·_ ; _**β**_ ) **Input:** Regularisation parameter _λ ∈_ R[+] **X** _←_ reshape� _**X** ,_ ( _N, M_ )� **y** _←_ vecRM ( _**Y**_ ) **s** _←_ vecRM ( _**S**_ ) Decompose each **L**[(] _[i]_[)] into **U**[(] _[i]_[)] **Λ**[(] _[i]_[)][ �] **U**[(] _[i]_[)][�] _[⊤]_ **U** _←_[�] **U**[(] _[i]_[)] Compute _**G** ∈_ R _[N]_[1] _[×][...][×][N][d]_ as _**G**_ **n** = _g_ � _**λ**_ ( **n** ); _**β**_ � (see eqs. (5.20) and (5.21)) **D** _**G** ←_ diag (vecRM ( _**G**_ )) **D** _**S** ←_ diag ( **s** ) Initialise _**θ** ∈_ R _[N]_[+] _[M]_ randomly **while** _|_ ∆ _**θ** | >_ tol **do** _**µ** ←_ **1** _/_ **1** + exp � _−_ � **I** _N_ **X** � _**θ**_ � **D** _**µ** ←_ diag� **s** _◦_ _**µ** ◦_ (1 _−_ _**µ**_ )� Decompose **X** _[⊤]_ **D** _**µ**_ **X** into **U** _M_ **Λ** _M_ **U** _[⊤] M_ **D** _M ←_ ( **Λ** _M_ + _λ_ **I** _M_ ) _[−]_[1] _[/]_[2] **UD** _**G**_ **0 Ψ** _←_ � **0 U** _M_ **D** _M_ � **D** _**S**_ **t** _←_ � **y** _−_ _**µ**_ + **D** _**µ**_ � **I** _N_ **X** � _**θ**_ � **X** _[⊤]_ **D** _**S**_ � � **D** _**G**_ **U** _[⊤]_ **D** _**µ**_ **UD** _**G**_ + _γ_ **I** _NT_ **D** _**G**_ **U** _[⊤]_ **D** _**µ**_ **XU** _M_ **D** _M_ **Q** _←_ � **D** _M_ **U** _[⊤] M_ **[X]** _[⊤]_ **[D]** _**[µ]**_ **[UD]** _**[G]**_ **I** _M_ � _**θ** ←_ **ΨQ** _[−]_[1] **Ψ** _[⊤]_ **t** (solve with the CGM, leveraging the structure of **Q** ) **end while** _**µ** ←_ **1** _/_ **1** + exp � _−_ � **I** _N_ **X** � _**θ**_ � **Output:** reshape� _**µ** ,_ ( _N_ 1 _, ..., Nd_ )� 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

180 

## **7.3.2.2 Multiclass L-RNC** 

In this section, we consider the multiclass generalisation of the L-RNC model. The data available for this model is much the same as the binary version outlined in the previous section, except here we have a partially labelled graph signal where each observed node has been classified into one of _C >_ 2 groups. As with the L-GSR model developed in section 7.2, this input data can be described by a multiway tensor signal _**Y**_ , with shape ( _N_ 1 _, ..., Nd, C_ ), where the final dimension represents a “one-hot” encoding of the class label. Each element, **n** , is interpreted as existing on a Cartesian product graph with factor Laplacians � **L**[(] _[i]_[)] _∈_ R _[N][i][×][N][i]_[�] _[d] i_ =1[,][and][is][accompanied][by] a binary sensing tensor _**S**_ , with shape ( _N_ 1 _, ..., Nd_ ), indicating which nodes were observed and which were not. Once again, we also have a length- _M_ vector of explanatory variables at each node in the product graph, which can be collected into a single tensor _**X**_ . 

**==> picture [267 x 31] intentionally omitted <==**

**==> picture [196 x 31] intentionally omitted <==**

Just as in section 7.2, we describe the probability distribution over each of the _C_ classes at node **n** with the tensor _**M**_ , which has the same shape as _**Y**_ , where the probability mass function is given by the length- _C_ fibre _**M**_ **n** _,_ :. Given this, the log-likelihood of observing a signal _**Y**_ is given by 

**==> picture [288 x 44] intentionally omitted <==**

Furthermore, we assume that _**M**_ is generated by applying a softmax function to each length- _C_ fibre of another tensor _**F**_ . 

**==> picture [362 x 28] intentionally omitted <==**

The key feature of the multiclass L-RNC model is that each of the _C_ slices of the tensor _**F**_ , denoted as _**F**_ : _,c_ , are given by the sum of a flexible intercept _**C** t_ , and a weighted linear combination of the features at each node. Both the intercept and the weighting are unique to each slice, _c_ . This means, in order to describe the tensor _**F**_ , we need a set of _C_ intercepts and weights _{_ _**C** c,_ **w** _c}[C] c_ =1[.] 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

181 

These can both be aggregated into singe objects: _**C**_ , a tensor with shape ( _N_ 1 _, ..., Nd, C_ ) and **w** , a vector with length _MC_ . Then, _**F**_ is defined as follows. 

**==> picture [331 x 12] intentionally omitted <==**

As before, **X** is a matrix view of the tensor _**X**_ reshaped to have dimensions ( _N, M_ ). In vectorised form, this can be written as 

**==> picture [251 x 11] intentionally omitted <==**

The goal of L-RNC will be to find the most likely values for _**C**_ and **w** which, in turn, will allow us to compute _**M**_ , generating the predicted class probabilities across the product graph. Following the pattern of previous RNC models, we can stack **c** and **w** into a single vector _**θ**_ as follows. 

**==> picture [256 x 37] intentionally omitted <==**

Then, **f** can be rewritten as 

**==> picture [256 x 19] intentionally omitted <==**

As such, we can rewrite the formula for _**µ**_ in terms of _**θ**_ . 

**==> picture [313 x 33] intentionally omitted <==**

Next, we place the following prior over _**θ**_ , to encode the assumption that each of the flexible intercept terms should vary smoothly with respect to the topology of the graph, and to regularise the coefficient vector **w** . 

**==> picture [297 x 37] intentionally omitted <==**

This leads to the following negative log-likelihood. 

**==> picture [349 x 37] intentionally omitted <==**

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

182 

The gradient of _ξ_ ( _**θ**_ ) is the vector of length _NC_ + _MC_ given by 

**==> picture [386 x 37] intentionally omitted <==**

The Hessian **P**[�] ( _**θ**_ ) with shape ( _NC_ + _MC_ ) _×_ ( _NC_ + _MC_ ) is given by 

**==> picture [358 x 36] intentionally omitted <==**

where, as in section 7.2, 

**==> picture [343 x 31] intentionally omitted <==**

Using the shorthands 

**==> picture [281 x 15] intentionally omitted <==**

the IRLS algorithm then proceeds according to the following update formula. 

**==> picture [401 x 236] intentionally omitted <==**

where 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

183 

**==> picture [326 x 37] intentionally omitted <==**

As before, to overcome the ill-conditioning present in the linear system **P**[�] _[−] k_[1][�] **[t]** _[k]_[,][we][can][use][the] symmetrically preconditioned CGM. In particular, we can transform the system into 

**==> picture [175 x 14] intentionally omitted <==**

where **Q**[�] _k_ has a lower condition number than the matrix **P**[�] _k_ . In order to define **Ψ**[�] _k_ and **Q**[�] _k_ , first we must compute the eigendecomposition of ( **X** _[⊤] ⊗_ **I** _C_ ) **R** _[k]_ _**µ**_[(] **[X]** _[ ⊗]_ **[I]** _[C]_[).] 

**==> picture [299 x 14] intentionally omitted <==**

Next, we define the matrix **D** _[k] M_[as][follows.] 

**==> picture [262 x 16] intentionally omitted <==**

Then, the operators **Ψ**[�] _k_ and **Q**[�] _k_ are defined as follows. 

**==> picture [275 x 36] intentionally omitted <==**

and 

**==> picture [407 x 36] intentionally omitted <==**

This leads to the complete algorithm for computing the class probabilities, given in algorithm 13. 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

184 

**Algorithm 13** Multiclass Logistic Regression with Network Cohesion 

**Input:** Explanatory variables _**X** ∈_ R _[N]_[1] _[×][...][×][N][d][×][M]_ **Input:** Observed binary tensor _**Y** ∈{_ 0 _,_ 1 _}[N]_[1] _[×][...][×][N][d][×][C]_ **Input:** Binary sensing tensor _**S** ∈{_ 0 _,_ 1 _}[N]_[1] _[×][...][×][N][d]_ **Input:** Cartesian product graph Laplacians � **L**[(] _[i]_[)] _∈_ R _[N][i][×][N][i]_[�] _[d] i_ =1 **Input:** Graph regularisation parameter _γ ∈_ R[+] **Input:** Graph filter function _g_ ( _·_ ; _**β**_ ) **Input:** Feautre regularisation parameter _λ ∈_ R[+] 

**X** _←_ reshape� _**X** ,_ ( _N, M_ )� **y** _←_ vecRM ( _**Y**_ ) **s** _←_ vecRM ( _**S**_ ) Decompose each **L**[(] _[i]_[)] into **U**[(] _[i]_[)] **Λ**[(] _[i]_[)][ �] **U**[(] _[i]_[)][�] _[⊤]_ **U** _←_[�] **U**[(] _[i]_[)] Compute _**G** ∈_ R _[N]_[1] _[×][...][×][N][d]_ as _**G**_ **n** = _g_ � _**λ**_ ( **n** ); _**β**_ � (see eqs. (5.20) and (5.21)) **D** _**G** ←_ diag (vecRM ( _**G**_ )) **D** _**S** ←_ diag ( **s** ) Initialise _**θ** ∈_ R _[N]_[+] _[M]_ randomly **while** _|_ ∆ _**θ** | >_ tol **do** 

**==> picture [386 x 247] intentionally omitted <==**

## **end while** 

_**µ** ←_ exp �� **I** _N_ **X** _⊗_ **I** _C_ � _**θ**_ � _/_ �� **I** _N ⊗_ **1** _C_ � exp �� **I** _N_ **X** _⊗_ **I** _C_ � _**θ**_ �[�] _⊗_ **1** _C_ **Output:** reshape� _**µ** ,_ ( _N_ 1 _, ..., Nd_ )� 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

185 

## **7.4 Image segmentation experiments** 

In this section, we examine the behaviour of the binary and multiclass algorithms developed in this chapter using an image segmentation task. The objective is to estimate the true class label at unlabelled pixels within an image, where a subset of the pixels have been classified into two or more groups. As briefly discussed in section 3.1.3, we can interpret image data as a special case of a 2D graph signal, with underlying graphs being simple chains reflecting the image’s dimensions. By performing a Cartesian product of these factor graphs, we generate a lattice structure where each node corresponds to a pixel. 

In the following sections, we analyse the properties of the L-GSR and L-RNC models introduced earlier in this chapter, in both their binary and multiclass form. For the binary case, we consider a foreground/background separation task on standard RGB images sourced from the Berkeley Segmentation Dataset [Martin et al., 2001]. For the multiclass case, we consider a hyperspectral image segmentation task, with data captured by an airborne sensor of farmland that has been divided into seventeen classes based on land cover [Baumgardner et al., 2015]. 

Many sophisticated techniques, most notably utilising deep neural networks, exist for image segmentation tasks (refer to Minaee et al. [2022], Wang et al. [2022b] for a comprehensive review). Whilst the classical statistical models introduced in this section are unlikely to be competitive with such methods on image segmentation tasks, they bring the advantage of versatility, enabling classification over generic Cartesian product graphs. However, since image segmentation datasets are readily accessible and easy to interpret visually, they serve as a useful test bed to investigate the properties of our more general graph-based algorithms. As such, it is worth emphasising that the goal of this section is not to produce a state-of-the-art image segmentation algorithm, but only to verify and analyse the properties of the techniques presented in this chapter. 

## **7.4.1 Background/foreground separation** 

The first task we attempted was to separate the background from the foreground using four 481 _×_ 321 pixel images taken from the Berkeley Segmentation Dataset [Martin et al., 2001]. These images had been manually labelled on a per-pixel basis into multiple objects, which we manually divided into background and foreground. We then randomly selected a certain fraction of pixels to serve as the labelled set _S_ , generating the input graph signals _**Y**_ and _**S**_ , both of shape (481, 321). Then, we attempted to estimate the class probabilities of the remaining pixels using both the L-GSR and L-RNC algorithms on a lattice graph using an isotropic diffusion graph filter. For L-RNC, the algorithm also had access to the RGB pixel data, creating a tensor of explanatory variables, _**X**_ , with shape (481, 321, 3). To ensure that the algorithms generated sensible outputs, we ran preliminary tests with 10% of the pixels labelled. The results can be seen 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

186 

**==> picture [289 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
Image Ground truth M L-GSR M L-RNC<br>**----- End of picture text -----**<br>


Figure 7.5: A colourmap of the output probabilities, _**M**_ , from the L-GSR and L-RNC are shown, along with the original image and the ground truth for the four examples. These were generated with 10% of the pixels labelled, using an isotropic diffusion filter with _β_ = 50, and _γ_ = 5 _×_ 10 _[−]_[5] . For L-RNC, _λ_ was set to 10[4] . 

in fig. 7.5, where the output, _**M**_ , is depicted as a colourmap. As can be seen, both algorithms broadly succeed at separating the background from the foreground. 

## **7.4.1.1 Assessing accuracy as a function of label percentage** 

In the first experiment, we examined the accuracy of each method as a function of the fraction of labelled pixels. Figure 7.6 provides a visual depiction of the estimated probability tensor _**M**_ over a range of fractions. As expected, both methods progressively improve as the labelled fraction increases. The L-RNC model appears to outperform the L-GSR, particularly at lower label fractions, likely due to its access to the RGB colour profile in the explanatory tensor _**X**_ . L-GSR, on the other hand, only has access to the lattice graph structure and the location of the labelled pixels. This effect is visible in the first column, where the L-GSR model can only identify the approximate shape of the object, whereas the L-RNC model shows artefacts from the original image, such as the texture of the starfish body. 

To further scrutinise this, we measured each model’s accuracy across a range of label fractions for each image. Here, accuracy is gauged by counting the rate of correct predictions for all pixels, by determining whether the probability is less than or greater than 1/2. Simultaneously, we also measured each method’s runtime for each label fraction. The results, shown in fig. 7.7, reveal 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

187 

**==> picture [414 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
0.05% 0.1% 0.5% 1% 10%<br>1.00<br>L-GSR 0.75<br>0.50<br>L-RNC 0.25<br>et SD 0.00<br>**----- End of picture text -----**<br>


Figure 7.6: The estimated probability tensor, _**M**_ , output from the L-GSR and L-RNC models, is shown for several fractions of observed data. 

both methods steadily improving in accuracy as the label fraction increases. L-RNC generally outperforms L-GSR, especially at lower label percentages, confirming our visual intuition from fig. 7.6. However, this comes at the cost of a longer runtime, likely due to additional matrix and memory management operations when running the CGM with block matrices. 

It is clear that the runtime of both methods increases as the label fraction grows, consistent with the features of the CGM algorithm, which, as discussed in section 3.3.3, is expected to converge quicker when the fraction of missing data is higher. We also observe sporadic spikes in runtime above the general trend, which can likely be attributed to Jax’s JIT compiler, which periodically retraces functions to ascertain their impact on inputs of a specific shape and data type [Bradbury et al., 2018]. 

## **7.4.1.2 Qualitative effects of varying** _γ_ **and** _β_ 

The second experiment sought to assess the effects on the probability output of the L-GSR and L-RNC algorithms when _γ_ and _β_ are varied independently. After randomly selecting 0.05% of the pixels to have their true label revealed, we evaluated the output of the L-GSR and L-RNC algorithms over a range of _β_ values while maintaining _γ_ fixed at 5 _×_ 10 _[−]_[5] and, for L-RNC, _λ_ fixed at 100. Subsequently, we performed the experiment again keeping _β_ fixed at 100 and varying _γ_ . In both cases, an isotropic diffusion filter was used. The results from these experiments are depicted in figs. 7.8 and 7.9, respectively. 

As seen in fig. 7.8, an increase in beta tends to extend the range over which each labelled pixel can influence nearby probability. When _β_ is low, at 10, the labelled pixels only affect other pixels in the immediate vicinity, with the probability quickly reverting to 0.5 (i.e. unknown) for more distant unlabelled pixels. As _β_ increases, so does this influence range, which is most visible in the L-GSR model where, when _β_ = 500, the probability prediction becomes quite blurred. Furthermore, these results suggest that increasing _β_ assists the L-RNC model in utilising the RGB data, as the outline of the foreground object becomes more defined with the increase in _β_ . 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

188 

**==> picture [376 x 292] intentionally omitted <==**

**----- Start of picture text -----**<br>
L-GSR L-RNC<br>100%<br>90%<br>. |3<br>80%<br>| Starfish ef<br>70% Stag<br>Tiger<br>Horses<br>60% Y=7 |<br>= | )<br>6<br>5 {| |<br>4 eee<br>3 sh<br>2<br>1<br>a<br>0<br>0.01% 0.1% 1.0% 10.0% 0.01% 0.1% 1.0% 10.0%<br>Fraction labelled<br>Accuracy<br>Time [s]<br>**----- End of picture text -----**<br>


Figure 7.7: The accuracy on a per-pixel basis is shown for the L-GSR and L-RNC models for each of the four images as a function of the fraction of randomly selected pixels that were labelled 

**==> picture [414 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
β = 10 β = 50 β = 100 β = 200 β = 500<br>1.00<br>L-GSR 0.75<br>0.50<br>L-RNC 0.25<br>0.00<br>**----- End of picture text -----**<br>


Figure 7.8: A colourmap of the probability output of the L-GSR and L-RNC algorithms are shown for various increasing values of _β_ . Here, _γ_ is set to 5 _×_ 10 _[−]_[5] and for L-RNC, _λ_ is set to 10[4] . 

Figure 7.9 illustrates the impact of altering _γ_ . As visible, a lower _γ_ tends to accentuate the transition between class probabilities, with the model yielding probabilities that cluster around zero or one. Interestingly, in this low _γ_ region, the graph intercept predominates over the explanatory variables within the L-RNC model. On the other hand, with higher _γ_ values, we observe the L-GSR probabilities leaning towards 1/2 across the entire lattice. For the L-RNC model in this scenario, the influence of the graph intercept term wanes, allowing the explanatory variables to take precedence in the prediction process. 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

189 

**==> picture [414 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
γ = 10 [−] [6] γ = 10 [−] [5] γ = 5  ×  10 [−] [5] γ = 10 [−] [4] γ = 10 [−] [3]<br>1.00<br>L-GSR 0.75<br>“2 Seb<br>0.50<br>L-RNC 0.25<br>» « » * AAPL 0.00<br>**----- End of picture text -----**<br>


Figure 7.9: A colourmap of the probability output of the L-GSR and L-RNC algorithms are shown for various increasing values of _γ_ . Here, _β_ is set to 100 and for L-RNC, _λ_ is set to 10[4] . 

**==> picture [82 x 139] intentionally omitted <==**

**----- Start of picture text -----**<br>
None<br>Alfalfa<br>Corn-notill<br>Corn-mintill<br>Corn<br>Grass-pasture<br>Grass-trees<br>Grass-pasture-mowed<br>Hay-windrowed<br>Oats<br>Soybean-notill<br>Soybean-mintill<br>Soybean-clean<br>Wheat<br>Woods<br>Buildings-Grass-Trees-Drives<br>Stone-Steel-Towers<br>**----- End of picture text -----**<br>


Figure 7.10: An overview of the Indian Pines hyperspectral image dataset. On the left is an example reading of the intensity response from the channel representing a wavelength of 0 _._ 9 _×_ 10 _[−]_[6] m. On the right is the ground truth for the land cover types, along with the associated colour key. 

## **7.4.2 Multiclass segmentation with hyper-spectral images** 

In this section, we test the multiclass L-GSR and L-RNC algorithms on a segmentation task using a hyperspectral image of a patch of farmland in North-western Indiana [Baumgardner et al., 2015]. The image has been manually segmented into seventeen distinct classes representing different crop types and land covers. The image is 145 _×_ 145 pixels in shape, and has 200 channels representing the response over a wavelength range of 0 _._ 4 _−_ 2 _._ 5 _×_ 10 _[−]_[6] m, with some bands covering the region of water absorption removed. Figure 7.10 gives an overview of this dataset, with the image on the left an example reading from one of the wavelength channels, and the image on the right a colour representation of the different land types. 

In order to verify the algorithms behave as expected, we tested the output when 20% of the pixels had the correct class labelled. This generated the binary input tensor _**Y**_ of shape (145 _,_ 145 _,_ 17), with a one-hot encoding along the class dimension, and the sensing tensor _**S**_ of shape (144 _,_ 144). For the L-RNC algorithm, we allowed access to the pixel data as a tensor of explanatory variables _**X**_ , of shape (144 _,_ 144 _,_ 200). We then ran the L-GSR and L-RNC algorithms using an isotropic 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

190 

## Model input 

**==> picture [179 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
L-GSR L-RNC<br>**----- End of picture text -----**<br>


Figure 7.11: A colour representation of the predicted classes from the multiclass L-GSR an L-RNC algorithms as applied to the Indian Pines dataset. On the left, we represent the input _**Y**_ available to the models, which contains 20% of the labelled pixels randomly selected. 

diffusion filter with parameter _β_ = 20 and set _γ_ = 5 _×_ 10 _[−]_[3] . For the L-RNC algorithm, we used a regularisation parameter of _λ_ = 100. 

Both these algorithms produced tensors representing the class probabilities at each pixel in the form of a tensor _**M**_ of shape (144 _,_ 144 _,_ 17). From this, we obtained the most likely class by taking the maximum element along the final dimension. The results can be seen in fig. 7.11. The L-GSR model achieved an accuracy of 84%, and the L-RNC algorithm achieved 89%. 

## **7.5 Discussion** 

## **7.5.1 Convergence of the IRLS algorithm** 

In general, algorithms based on Newton’s method, including Iteratively Reweighted Least Squares (IRLS), frequently encounter convergence difficulties [Kelley, 2003]. In the course of our experimental work, we encountered two distinct problems, both of which we managed to rectify through relatively straightforward solutions. 

Initially, we employed 32-bit floating point numbers for all arrays, with a termination criterion for the IRLS iterations defined as the point at which the absolute change in the target vector or tensor had an average value less than 10 _[−]_[6] . Nevertheless, we often noted an issue where the algorithm failed to converge, with the average change in each element stagnating around the order of 10 _[−]_[5] . To mitigate this issue, we upgraded to 64-bit floating point arrays. Although this change resulted in marginally slower computational speeds and a somewhat larger memory footprint, it effectively addressed the convergence problem. 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

191 

A second challenge we faced manifested as either divergence or cyclic behaviour, where the target vector would oscillate through a finite series of points without ever achieving convergence. Broadly speaking, we found that these difficulties could be circumvented by selecting a more precise initial value for the iterative process. Our initial strategy was to simply set the initial estimate to a vector of zeros, but this approach led to inconsistent convergence outcomes. 

Instead, we found that using an initial estimate derived from the solution to the real-valued GSR/KGR/RNC problem proved to be more effective. To illustrate, for a binary L-GSR problem with inputs _**Y**_ , _**S**_ , _γ_ , and _β_ , our initial estimate was the solution to the real-valued GSR problem with inputs 2 _**Y** −_ _**S**_ , _**S**_ , _γ_ , and _β_ . The transformation _**Y** →_ 2 _**Y** −_ _**S**_ preserves all values equal to one, while all observed values that were zero are converted to negative one, with all unobserved values remaining at zero. This method provided a generally superior initial estimate for the underlying signal, and once implemented, eliminated all previously observed convergence issues. In the case of multiclass problems, we essentially solved the real-valued problem _C_ times, corresponding to each dimension of the class label. This strategy ensured a smoother and more consistent convergence across various hyperparameter settings. 

## **7.5.2 Efficient computation in the multiclass L-RNC algorithm** 

It is straightforward to see how the binary L-GSR and L-RNC algorithms can be executed efficiently, using the same ideas used consistently in this thesis. The CGM primarily entails repeated multiplications of the coefficient matrix by an arbitrary vector, while the IRLS algorithm involves repetitive execution of the CGM. In the L-GSR model, the coefficient matrix **Q** is constructed solely of diagonal and Kronecker-structured operators, enabling accelerated multiplication onto tensors. This is achieved by efficiently applying algorithm 4, as elaborated in section 5.1.3. In the L-RNC scenario, the coefficient matrix **Q**[�] is a block matrix. The blocks aligned along the diagonal consist only of diagonal and Kronecker operators, while the off-diagonal blocks can be directly computed. 

As we progress to the multiclass L-GSR algorithm, a complication emerges due to the presence of a non-diagonal, non-Kronecker-structured operator, **R** _**µ**_ , within the coefficient matrix. Nevertheless, as detailed in section 7.2 and explicitly stated in eq. (7.22), the action of **R** _**µ**_ on a vector or tensor can be computed efficiently by leveraging its special structure, with a time-complexity of _O_ ( _NC_ ). 

The multiclass L-RNC, however, presents two additional challenges. First, it becomes necessary to compute the matrix ( **X** _[⊤] ⊗_ **I** _C_ ) **R** _**µ**_ ( **X** _⊗_ **I** _C_ ), so that it can then be decomposed into **U** _M_ **Λ** _M_ ( **U** _M_ ) _[⊤]_ . We assume that this decomposition step, which entails solving the eigenvalue problem for a dense symmetric matrix of dimensions _MC × MC_ , is feasible. This assumption 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

192 

is likely reasonable for most problem scenarios. For instance, in our case study involving 200 explanatory variables and 17 classes, the process required the decomposition of a 3400 _×_ 3400 matrix. Nevertheless, efficient computation of the matrix ( **X** _[⊤] ⊗_ **I** _C_ ) **R** _**µ**_ ( **X** _⊗_ **I** _C_ ) is non-trivial. The straightforward strategy of instantiating the _NC × MC_ matrix **X** _⊗_ **I** _C_ directly, and then sequentially multiplying **R** _**µ**_ onto each column demands _C_[2] copies of **X** , which may be challenging for large problems. In our relatively modest example, this matrix would be of size (4 _._ 2 _×_ 10[6] ) _×_ 3400, amounting to almost 10GB of 64-bit floating point memory. With a memory complexity of _O_ ( _NMC_[2] ), this is potentially intractable. 

Fortunately, a more efficient approach is possible. The matrix ( **X** _[⊤] ⊗_ **I** _C_ ) **R** _**µ**_ ( **X** _⊗_ **I** _C_ ) _∈_ R _[MC][×][MC]_ can be viewed as a block matrix comprising _M_[2] blocks, each of dimensions _C × C_ . The computation of Block ( _i, j_ ) can be conducted as follows. 

**==> picture [300 x 13] intentionally omitted <==**

where, in this context, **X** _i ∈_ R _[N][×][C]_ is the _i_ -th column of **X** repeated _C_ times, and **M** is _**M**_ reshaped to have dimensions ( _N, C_ ). Thus the memory complexity of this approach is reduced to _O_ ( _NM_ + _NC_ ). 

The second complication that arises is in the computation of the block matrix **Q**[�] . Here, the upper right block is given by 

**==> picture [205 x 13] intentionally omitted <==**

and the lower left block is the transpose of this. Again, since this object has _NMC_[2] elements, instantiating it in memory may be problematic. Instead, we can efficiently compute its action on a vector **v** of length _MC_ by taking the following steps. 

1. **v** _∈_ R _[MC] ←_ **U** _M_ **D** _M_ **v** _(compute this as usual)_ 

2. **v** _∈_ R _[NC] ←_ vecRM � **X** reshape� **v** _,_ ( _M, C_ )�� _(compute using the standard row-major vec trick)_ 

3. **v** _∈_ R _[NC] ←_ **R** _**µ**_ **v** _(compute efficiently using eq._ (7.22) _)_ 

4. **v** _∈_ R _[NC] ←_ ( **UD** _**G** ⊗_ **I** _C_ ) _[⊤]_ **v** _(compute efficiently using fast Kronecker product)_ 

The reverse process, of multiplying the transpose of this block onto a vector of length _NC_ can be achieved by reversing these steps with each operation transposed. In both cases, this reduces the computational and memory footprint substantially. 

Chapter 7. _Reconstruction and Regression with Binary-Valued Graph Signals_ 

193 

## **7.6 Conclusions** 

In this chapter, we have considered reconstruction and regression tasks for binary and categorical multiway graph signals. Whilst related tasks have been considered in the machine learning community, in the context of semi-supervised learning Kondor and Lafferty [2002], Zhu et al. [2003], the aims of those models are distinct from our own. In SSL, the graph is usually formed by considering a distance metric in feature space, whereas we take the perspective of GSP, in which the graph is a fundamental structure that preexists, potentially with additional covariates. Although the graph signal processing community has a mature literature on real-valued signals, there have been few papers addressing reconstruction and regression with binary and categorical graph signals. The objective of this chapter has been to present novel classification models applicable to signals existing on general _d_ -dimensional Cartesian product graphs, a topic which to the best of our knowledge has not been addressed by the ML or GSP communities. 

In our models, we propose placing a Gaussian graph-spectral prior over a real-valued underlying tensor _**F**_ , which is subsequently transformed via the logistic function to generate class probabilities for each node in the product graph. These probabilities therefore vary smoothly with respect to the topology of the graph, inheriting properties from the graph filter, whilst remaining in the interval [0 _,_ 1]. 

In particular, we have developed three novel graph signal processing models by generalising the Graph Signal Reconstruction (GSR), Kernel Graph Regression (KGR), and Regression with Network Cohesion (RNC) models, which were developed earlier in this thesis for real-valued signals, to accommodate binary graph signals. This led to the creation of three “logistic” models: L-GSR, L-KGR, and L-RNC. Similar to their real-valued counterparts introduced in chapter 5, all three models are devised to handle signals residing on the nodes of general Cartesian product graphs, making them relevant for applications such as network time series modelling. Additionally, we introduced multiclass versions of these three algorithms to manage scenarios where nodes need to be classified into one of several groups or classes. 

These new logistic models required the introduction of a new Iteratively Reweighted Least Squares (IRLS) algorithm to solve for the posterior mean. We discussed the convergence properties of this algorithm in depth, and made proposals for increasing the chances of convergence. In particular, the multiclass models often failed to converge when the initial estimate was a tensor of zeros. However, the chances of success were improved dramatically when we used the solution to the equivalent real-valued problem, with a target tensor of 2 _**Y** −_ _**S**_ , as the initial estimate instead. 

## **Chapter 8** 

## **Conclusions** 

In this thesis, we have developed several novel Graph Signal Processing (GSP) models designed to estimate arbitrary missing values within multivariate graph signals. This final chapter gives an overview of all the models presented in this thesis, followed by a discussion of some of their key characteristics. 

## **8.1 Thesis summary** 

We began in chapter 3 by presenting a model for Graph Signal Reconstruction (GSR) on twodimensional Cartesian product graphs. Here, we proposed a formulation of two-dimensional graph filters by building on works such as Grassi et al. [2018], Ioannidis et al. [2016], Isufi et al. [2017], Loukas and Foucard [2016], who are specifically concerned with time-varying graph signals, to define anisotropic spectral operators on 2D Cartesian product graphs. This led to a Bayesian GSR model, for which we proposed two iterative algorithms for computing the posterior mean, namely the Stationary Iterative Method (SIM) and the Conjugate Gradient Method (CGM). We conducted a thorough analysis of these algorithms, highlighting their similarities and differences, with the objective of showing how the optimal choice depends on the hyperparameters and data composition. One key finding is that the SIM can be implemented in an eigendecomposition-free and/or distributed manner, by making use of Chebyshev polynomials, but the CGM cannot, as it relies on a preconditioner that is constructed via the GFT. Another is that the two methods have opposite behaviour with regard to the fraction of missing data in the input signal, with the CGM converging faster with more missing data and the SIM converging slower. 

In chapter 4, we considered multivariate regression models for partially observed graph signals. First, we highlighted two distinct scenarios that have appeared in the literature, namely when 

194 

Chapter 8. _Conclusions_ 

195 

the explanatory variables are exogenous (global) and endogenous (local). For the former, we extended the work of Venkitaraman et al. [2020, 2019], which consider non-parametric regression models for predicting graph signals _{_ **y** _t}_ as a function of global variables _{_ **x** _t}_ . In particular, our aim was to accommodate the case where arbitrary data was missing in the input signals _{_ **y** _t}_ , which leads to our modified Kernel Graph Regression (KGR) model. For the latter, we considered the work described in Li et al. [2019], where the goal is to predict a graph signal given that local explanatory variables exist at each node in the graph. Here, our objective was to extend this to multivariate signals that exist on the nodes of an arbitrary two-dimensional Cartesian product graph enabling new applications such as regression with graph time series data to be addressed. This resulted in our multivariate version of Regression with Network Cohesion (RNC). We find that, for KGR, the posterior mean can be computed using modified versions of the CGM or SIM algorithms introduced in chapter 3, with it remaining possible to implement the SIM in an eigendecomposition-free manner. For RNC, however, we find that only the CGM can be used, ruling out such implementations. Finally, we also proposed a hybrid model, KG-RNC, combining aspects of both KGR and RNC, applicable to scenarios where both exogenous and endogenous explanatory variables exist to aid the signal reconstruction process. 

In chapter 5, we took the models developed previously in the thesis, and generalised them to the Multiway Graph Signal Processing (MWGSP) framework [Stanley et al., 2020]. Here, we reviewed the tensor representations of multiway graph signals and highlighted the importance of an efficient implementation of chained Kronecker-structured graph-spectral operators [Antonian et al., 2023]. We then proposed a framework for general anisotropic low-pass graph filter functions in _d_ -dimensions to be any decreasing function of an inner product between a parameter vector _β_ and a vector of Laplacian eigenvalues _**λ**_ . This creates spectral operators that can be consistently interpreted as an analytic function of a Cartesian product graph Laplacian, also ensuring eigendecomposition-free implementations can be achieved using Chebyshev polynomials. We then took the GSR, KGR and RNC models developed prior in the thesis, and generalised them to tensor-valued graph signals in a general number of dimensions, illustrating the applicability of such models using a dataset of green bond yields. 

In chapter 6, we addressed the topic of uncertainty estimation and sampling. Whilst the general tensor versions of the GSR, KGR and RNC models introduced earlier in the thesis are Bayesian, with a posterior described by a multivariate Gaussian with a known covariance matrix **P** _[−]_[1] , the high dimensionality makes computing or storing the **P** _[−]_[1] directly intractable for even modestly-sized models. Therefore, in this chapter, we had two distinct aims: to extract valuable information from the posterior without directly computing the covariance matrix in full. The first aim was to estimate the marginal variance, i.e. the diagonal of **P** _[−]_[1] . We presented three novel techniques for this, which were based on the premise that it is possible to efficiently “query” elements from the diagonal of **P** _[−]_[1] by solving a linear system using the CGM or SIM. 

Chapter 8. _Conclusions_ 

196 

Introducing a set of artificial explanatory variables allowed us to cast the problem of diagonal estimation as a supervised learning problem. This was also supplemented by an active learning strategy which traded an increase in bias for a reduction in variance of the estimator, which is particularly effective at low query numbers. We compared our three estimators against a stochastic algorithm for this purpose from Bekas et al. [2007], demonstrating significantly better performance. In the second half of this chapter, we presented a method for drawing samples directly from the posterior using a technique known as perturbation optimisation [Orieux et al., 2012]. The computational cost of each sample was equal to the cost of commuting the posterior mean, which can also be achieved using the SIM or CGM. 

Finally, in chapter 7, we modified the tensor-valued GSR, KGR and RNC models presented in chapter 5, to accommodate binary and categorical graph signals. Whilst similar problems have been addressed for 1D graphs in the literature on semi-supervised learning Kondor and Lafferty [2002], Zhu et al. [2003], our models are applicable to general _d_ -dimensional product graphs, and are firmly grounded in GSP, using graph spectral priors. We present binary and multiclass logistic variants for GSR, KGR and RNC, which we term L-GSR, L-KGR and L-RNC. These models required a new Iteratively Reweighted Least Squares (IRLS) algorithm, the convergence behaviour of which we discussed in detail. One key observation is that the chance of successful convergence is increased by using a specially selected initial value for the iterative procedure. 

## **8.2 Future Work** 

In this concluding section, we briefly explore several areas where the tools and methodologies presented in this thesis could be expanded or improved upon in future work. These areas are categorised into the following themes: scalability, multiway filter design, graph and parameter learning, and Generalised Linear Models (GLMs). 

## **8.2.1 Scalability** 

The primary focus of this thesis has been on analysing and maximising the computational efficiency of the proposed algorithms. With the exception of the Chebyshev methods mentioned in the context of the SIM in section 3.2.2.1, we have generally assumed the availability of all eigenvectors and eigenvalues of the graph Laplacian as inputs to the problem. However, in the case of very large sparse graphs, like those encountered in online social networks, a complete decomposition may not be feasible due to memory and computational constraints. In instances where the Chebyshev SIM cannot be applied (for example, in situations where high levels of missing data result in slow convergence, or when performing RNC which precludes the use of the SIM), computing only the first _k_ eigenvectors and eigenvalues of **L** using methods such as 

Chapter 8. _Conclusions_ 

197 

restarted Arnoldi [Lehoucq et al., 1998] may be more practical. This approach would still allow for the implementation of the algorithms discussed in this thesis with a bandlimited filter, which retains only the first _k_ spectral components. While such partial decomposition methods offer computational advantages, they may result in diminished performance. Future research into these methods, including their compromises compared to complete decomposition approaches, would be of significant interest. 

Furthermore, efforts could be directed towards developing a modified version of the conjugate gradient method outlined in section 3.2.3, suitable for use with distributed or eigendecompositionfree approaches, like the Chebyshev polynomial approximation. This modification would facilitate efficient large-scale computations under varying levels of missing data by employing a decomposition-free variant of the CGM and the SIM accordingly. Additionally, it would allow for the execution of these algorithms on parallel computing architectures, such as GPUs/TPUs, potentially improving scalability even further. 

## **8.2.2 Multiway Filter Design** 

In this thesis, although some discussion is dedicated to filter design, the main emphasis has been on the implementation and analysis of reconstruction/regression algorithms, with filters serving merely as one component. Nonetheless, a detailed investigation into the choice and design of filters and their impacts, both independently and in more depth, would be highly beneficial, especially within the context of Multiway Graph Signal Processing (MWGSP). Research like that of Jiang et al. [2021], which delves into various methods of constructing filters for timevarying graph signals, provides a substantial foundation. A focused study on filter design for generic Cartesian product graphs across arbitrary dimensions would contribute valuable insights. 

In section 5.1.4, we introduced a method for developing multi-dimensional graph filters by applying a single decreasing function to the dot product between a parameter vector and the corresponding graph Laplacian eigenvalues. This strategy is straightforward to implement and ensures alignment with the Cartesian product structure, yet it might not offer the versatility found in other, more open-ended methodologies. For instance, exploring general polynomials of the factor Laplacians could be advantageous. Moreover, our proposed method only exhibits separability in the case of the exponential filter. 

**==> picture [280 x 30] intentionally omitted <==**

This prompts consideration for other forms that maintain separability into independent functions across each dimension. However, it is important to note that pursuing such separability might compromise the strict Cartesian product graph framework. 

Chapter 8. _Conclusions_ 

198 

## **8.2.3 Graph and parameter learning** 

In this thesis, we have generally assumed that the hyperparameters required as input into the algorithms (in our case, the graph filter strengths _**β**_ and the regularisation term _γ_ ) are predetermined. Additionally, the assumption has been that the graph structure is known a priori before model execution. An alternative approach, however, would involve learning these elements either individually or jointly as part of a comprehensive end-to-end model. Work such as Zhi et al. [2023] has already looked at simultaneous graph regression and parameter learning, while a large literature already exists on graph learning that could be incorporated in signal reconstruction and regression contexts [Dong et al., 2019]. Work such as Hu et al. [2015] has already looked into simultaneous signal reconstruction and graph learning, yet further exploration, particularly within the context of product graphs, could yield significant advancements. 

In the Bayesian context, it’s conceivable to develop a fully hierarchical model in which a noninformative prior is placed over both the hyperparameters and the graph itself. The model output would then not only be a distribution over the reconstructed signal but also over _**β** , λ_ and the graph adjacency matrix **A** . This would certainly present new challenges in terms of compute and memory as it would most likely necessitate Monte Carlo-based approaches, however, such a rich output could offer considerable value in specific applications. 

## **8.2.4 Generalised Linear Models (GLMs)** 

One underlying assumption running through all the models from chapters 3 to 5 is that the probability distribution underlying the graph signal is a multivariate Gaussian. In many cases this may be true, and in others such as the pollutant monitoring example in section 4.4, a simple transformation ( _x →_ log(1 + _x_ ) in that case) can help coerce the data to approximately fulfill this requirement. In chapter 7, we generalised this assumption to allow for binary and categorical data. Though not explicitly discussed, this was an example of a Generalised Linear Model (GLM) [Nelder and Wedderburn, 1972], where we used a logit/logistic link function to transform the output from the real line to probabilities on the [0 _,_ 1] interval. 

To embrace the full scope of GLMs, one could envisage modelling the system using the exponential family of distributions. This approach would allow for the representation of the observed signal through a variety of distributions, such as gamma or Poisson, thereby accommodating new forms of signal data, such as count data. Adopting this broader perspective presents both methodological challenges but also opportunities for exploring diverse modelling contexts. 

## **Appendix A** 

## **Proofs** 

**Theorem A.1.** _The posterior distribution for_ **F** _is given by_ 

**==> picture [278 x 13] intentionally omitted <==**

_where_ 

**==> picture [278 x 21] intentionally omitted <==**

_Proof._ Consider the matrix **S** _ϵ_ defined in the following manner. 

**==> picture [267 x 43] intentionally omitted <==**

We can use this definition to rewrite eq. (3.12) for the probability distribution of **Y** _|_ **F** . 

**==> picture [329 x 31] intentionally omitted <==**

In this way, the negative log-likelihood of an observation **Y** _|_ **F** is given by 

**==> picture [388 x 31] intentionally omitted <==**

up to an additive constant which does not depend on **F** . Note that, since **Y** = **S** _ϵ ◦_ **Y** , we can rewrite vec ( **S** _ϵ ◦_ **F** _−_ **Y** ) as 

199 

Appendix A. _Proofs_ 

200 

**==> picture [308 x 32] intentionally omitted <==**

Therefore, equation A.5 can be rewritten as 

**==> picture [352 x 61] intentionally omitted <==**

Now consider the full log-posterior. Using Bayes rule, this can be written as 

**==> picture [404 x 45] intentionally omitted <==**

Up to an additive constant not dependent **F** , this can be written as 

**==> picture [412 x 21] intentionally omitted <==**

Using the conjugacy of the normal distribution, by direct inspection we can conclude that the posterior covariance is given by 

**==> picture [278 x 21] intentionally omitted <==**

and that the posterior mean is given by **Σ** vec ( **Y** ). 

**Theorem A.2.** Consider the random matrix **Z** which is related to the random matrix **F** as follows. 

**==> picture [89 x 12] intentionally omitted <==**

Appendix A. _Proofs_ 

201 

or, equivalently, 

**==> picture [146 x 13] intentionally omitted <==**

Then the posterior mean for **Z** _|_ **Y** is given by 

**==> picture [220 x 15] intentionally omitted <==**

where 

**==> picture [182 x 13] intentionally omitted <==**

(Here we have abbreviated diag (vec ( **G** )) and diag (vec ( **S** )) as **DG** and **DS** respectively.) 

_Proof._ The conditional distribution of **Y** _|_ **Z** is obtained by substituting in the definition of **F** in terms of **Z** into the original conditional likelihood expression. 

**==> picture [224 x 19] intentionally omitted <==**

Similarly, since the prior specified for **F** is _N_ � **0** _, γ[−]_[1] **H**[2][�] , this implies that the prior over **Z** is simply 

**==> picture [110 x 14] intentionally omitted <==**

To see this, consider the following 

**==> picture [268 x 40] intentionally omitted <==**

If vec ( **Z** ) has covariance _γ[−]_[1] **I** , then vec ( **F** ) has covariance given by 

Appendix A. _Proofs_ 

202 

**==> picture [210 x 33] intentionally omitted <==**

by the definition of **H** . 

Now consider the transformed posterior 

**==> picture [208 x 82] intentionally omitted <==**

Up to an additive constant, this is equal to 

**==> picture [212 x 93] intentionally omitted <==**

By inspection, again, we can see that the posterior mean for **Z** is 

**==> picture [172 x 15] intentionally omitted <==**

**Theorem A.3.** _The number of steps required to reach a given level of precision for matrix splitting methods follows_ 

**==> picture [260 x 24] intentionally omitted <==**

Appendix A. _Proofs_ 

203 

_where the coefficient matrix is split as_ **M** _−_ **N** _._ 

_Proof._ In the SIM, we have that 

**==> picture [278 x 10] intentionally omitted <==**

where vec ( **F** ) represents the true solution to the linear system. This leads directly to an update equation given by 

**==> picture [288 x 11] intentionally omitted <==**

Subtracting eq. (A.12) from eq. (A.13) gives 

**==> picture [318 x 54] intentionally omitted <==**

where we denote the error at the _k_ -th iteration as vec ( **E** _k_ ) = vec ( **F** _k_ ) _−_ vec ( **F** ). From this it is clear to see that convergence will be achieved so long as the spectral radius _ρ_ ( **M** _[−]_[1] **N** ) is less than one. If this condition holds then, 

**==> picture [305 x 17] intentionally omitted <==**

In general, the number of iterations required to achieve some specified reduction in the magnitude of the error is proportional to one over the logarithm of the spectral radius 

**Theorem A.4.** _The values of nSIM and nCGM always increase when γ, within its valid range, decreases in both the strong a weak filter limits._ 

_Proof._ Consider each of the following expressions. 

**==> picture [127 x 78] intentionally omitted <==**

Appendix A. _Proofs_ 

204 

**==> picture [181 x 24] intentionally omitted <==**

**==> picture [162 x 25] intentionally omitted <==**

In order to prove the theorem, we must show that the partial derivative of each expression with respect to _γ_ is strictly negative over the domain 0 _≤ γ ≤∞_ . Let us compute this for each expression in turn. 

**==> picture [180 x 26] intentionally omitted <==**

**==> picture [154 x 33] intentionally omitted <==**

**==> picture [250 x 29] intentionally omitted <==**

**==> picture [178 x 32] intentionally omitted <==**

In each of these expressions, we have a fraction for which both the numerator and denominator can easily be shown to be strictly positive over the valid ranges of _γ_ and _m_ . Each expression also includes a negative sign in front. As such, every expression is strictly negative. 

**Theorem A.5.** _In the limit of a strong filter, for any fixed value of γ, the number of iterations for convergence will always increase as the proportion of missing data m increases for the SIM, whereas the number will always decrease for the CGM._ 

_Proof._ To prove this theorem it suffices to show that the partial derivative of _n_ SIM with respect to _m_ is always positive, whereas the partial derivative of _n_ CGM with respect to _m_ is always negative. They are respectively given by 

**==> picture [220 x 28] intentionally omitted <==**

Appendix A. _Proofs_ 

205 

**==> picture [174 x 33] intentionally omitted <==**

Since _γ_ is strictly positive and _m_ must be in the range 0 _≤ m ≤_ 1, clearly the first expression is always positive whereas the second is always negative. 

**Theorem A.6.** _In the RNC model, the posterior distribution over the combined parameter vector_ _**θ** is given by_ 

**==> picture [294 x 37] intentionally omitted <==**

_where_ 

**==> picture [338 x 37] intentionally omitted <==**

_Proof._ The distribution of **Y** given _**θ**_ is given in eq. (4.29). This can also be written as 

**==> picture [288 x 13] intentionally omitted <==**

The prior for _**θ**_ is given in equation eq. (4.30). Therefore, using Bayes’ rule, we can write 

**==> picture [328 x 69] intentionally omitted <==**

Using the same trick as in theorem A.1, where we parametrise **S** as **S** = lim _ϵ→_ 0 **S** _ϵ_ . Given this, we can rewrite the above expression as 

**==> picture [300 x 67] intentionally omitted <==**

Appendix A. _Proofs_ 

206 

Collecting like terms, and dropping a constant not dependent on _**θ**_ , this can be written as 

**==> picture [341 x 37] intentionally omitted <==**

Using the conjugacy of the normal distribution, we can conclude by direct inspection that the posterior covariance matrix is given by **P**[�] _[−]_[1] , and the posterior mean is given by 

**==> picture [82 x 37] intentionally omitted <==**

where 

**==> picture [166 x 37] intentionally omitted <==**

**Theorem A.7.** _This diagonal of the matrices_ **H** _and_ **H**[2] _can be efficiently calculated as follows._ 

**==> picture [293 x 12] intentionally omitted <==**

_and_ 

**==> picture [304 x 14] intentionally omitted <==**

_Proof._ To prove these statements, we can use the identity given in the front matter. 

**==> picture [285 x 13] intentionally omitted <==**

In the case of **H** = **U** diag (vecRM ( _**G**_ )) **U** _[⊤]_ , this corresponds to the following. 

**==> picture [336 x 14] intentionally omitted <==**

For **H**[2] = **U** diag (vecRM ( _**G**_ ))[2] **U** _[⊤]_ , this corresponds to the following. 

Appendix A. _Proofs_ 

207 

**==> picture [347 x 14] intentionally omitted <==**

**Theorem A.8.** _Consider the following function, ξ_ ( **f** ) _, which maps a vector_ **f** _∈_ R _[N] to a scalar._ 

**==> picture [348 x 19] intentionally omitted <==**

_The derivative of this function with respect to_ **f** _is given by_ 

**==> picture [276 x 13] intentionally omitted <==**

_and the Hessian is given by_ 

**==> picture [251 x 13] intentionally omitted <==**

_where_ 

**==> picture [156 x 13] intentionally omitted <==**

_Proof._ First, recall that the formula for _**µ**_ ( **f** ) is given by 

**==> picture [253 x 24] intentionally omitted <==**

This further implies that 

**==> picture [268 x 24] intentionally omitted <==**

**==> picture [289 x 34] intentionally omitted <==**

Note that all operations in these expressions, including division, logarithms, and exponentiation should be understood as element-wise. Using these equations, we can rewrite the expression for _ξ_ ( **f** ). 

_Bibliography_ 

208 

**==> picture [373 x 72] intentionally omitted <==**

Now, take the derivate of this expression with respect to **f** , using the chain rule for the middle term. 

**==> picture [208 x 95] intentionally omitted <==**

This is the given expression for the gradient, **g** ( **f** ). The Hessian can be found by taking the derivative of the gradient with respect to **f** . 

**==> picture [234 x 169] intentionally omitted <==**

## **Bibliography** 

- Abraham, R., Marsden, J. E., and Rat,iu, T. S. (1988). _Manifolds, tensor analysis, and applications_ . Springer-Verlag, New York, 2nd ed edition. 

- Ahmed, N., Natarajan, T., and Rao, K. (1974). Discrete cosine transform. _IEEE Transactions on Computers_ , C-23(1):90–93. 

- Anis, A., Gadde, A., and Ortega, A. (2016). Efficient sampling set selection for bandlimited graph signals using graph spectral proxies. _IEEE Transactions on Signal Processing_ , 64(14):3775– 3789. 

- Antonian, E., Peters, G. W., and Chantler, M. (2023). Pykronecker: A python library for the efficient manipulation of kronecker products and related structures. _Journal of Open Source Software_ , 8(81):4900. 

- Arroyo, A., Scalzo, B., Stankovi´c, L., and Mandic, D. P. (2022). Dynamic portfolio cuts: A spectral approach to graph-theoretic diversification. In _ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 5468–5472. 

- Atasoy, S., Donnelly, I., and Pearson, J. (2016). Human brain networks function in connectomespecific harmonic waves. _Nature Communications_ , 7(1). 

- Atchinson, J. and Shen, S. (1980). Logistic-normal distributions:Some properties and uses. _Biometrika_ , 67(2):261–272. 

- Aubert, G. and Kornprobst, P. (2006). _Mathematical problems in image processing_ . Applied mathematical sciences. Springer, New York, NY, 2 edition. 

- Barik, S., Bapat, R. B., and Pati, S. (2015). On the laplacian spectra of product graphs. _Applicable Analysis and Discrete Mathematics_ , 9:39–58. 

- Barik, S., Kalita, D., Pati, S., and Sahoo, G. (2018). Spectra of graphs resulting from various graph operations and products: a survey. _Special Matrices_ , 6:323 – 342. 

- Baumgardner, M. F., Biehl, L. L., and Landgrebe, D. A. (2015). 220 band aviris hyperspectral image data set: June 12, 1992 indian pine test site 3. 

209 

_Bibliography_ 

210 

- Bekas, C., Kokiopoulou, E., and Saad, Y. (2007). An estimator for the diagonal of a matrix. _Applied Numerical Mathematics_ , 57(11):1214–1229. 

- Belkin, M., Matveeva, I., and Niyogi, P. (2004a). Regularization and semi-supervised learning on large graphs. In Shawe-Taylor, J. and Singer, Y., editors, _Learning Theory_ , pages 624–638, Berlin, Heidelberg. Springer Berlin Heidelberg. 

- Belkin, M., Matveeva, I., and Niyogi, P. (2004b). Tikhonov regularization and semi-supervised learning on large graphs. In _2004 IEEE International Conference on Acoustics, Speech, and Signal Processing_ , volume 3, pages iii–1000. 

- Belkin, M. and Niyogi, P. (2002). Using manifold structure for partially labelled classification. In _Proceedings of the 15th International Conference on Neural Information Processing Systems_ , NIPS’02, page 953–960, Cambridge, MA, USA. MIT Press. 

- Belkin, M. and Niyogi, P. (2003). Laplacian eigenmaps for dimensionality reduction and data representation. _Neural Computation_ , 15(6):1373–1396. 

- Bhatia, R. (1997). _Matrix analysis_ . Number 169 in Graduate texts in mathematics. Springer, New York. 

- Box, G. E. P. and Muller, M. E. (1958). A Note on the Generation of Random Normal Deviates. _The Annals of Mathematical Statistics_ , 29(2):610 – 611. 

- Bradbury, J., Frostig, R., Hawkins, P., Johnson, M. J., Leary, C., Maclaurin, D., Necula, G., Paszke, A., VanderPlas, J., Wanderman-Milne, S., and Zhang, Q. (2018). JAX: composable transformations of Python+NumPy programs. 

- Brenner, S. C., Scott, L. R., and Scott, L. R. (2008). _The mathematical theory of finite element methods_ , volume 3. Springer. 

- Burden, R. and Faires, J. (2010). _Numerical Analysis_ . Cengage Learning. 

- Chakraborty, P. (2017). Trend Filtering in Network Time Series with Applications to Traffic Incident Detection. _Time Series Workshop, Neural Information Processing Systems_ , pages 1–4. 

- Chakraborty, P., Hegde, C., and Sharma, A. (2019). Data-driven parallelizable traffic incident detection using spatio- temporally denoised robust thresholds. _Transportation Research Part C_ , 105(June):81–99. 

- Cheeger, J. (1971). _A Lower Bound for the Smallest Eigenvalue of the Laplacian_ , pages 195–200. Princeton University Press, Princeton. 

- Chen, S., Sandryhaila, A., Moura, J. M. F., and Kovaˇcevi´c, J. (2015). Signal recovery on graphs: Variation minimization. _IEEE Transactions on Signal Processing_ , 63(17):4609–4624. 

_Bibliography_ 

211 

- Cheng, R. and Li, Q. (2021). Modeling the momentum spillover effect for stock prediction via attribute-driven graph attention networks. _Proceedings of the AAAI Conference on Artificial Intelligence_ , 35(1):55–62. 

- Chi, Y., Jiang, J., Zhou, F., and Xu, S. (2022). A distributed algorithm for reconstructing time-varying graph signals. _Circuits, Systems, and Signal Processing_ , 41(6):3624–3641. 

- Chong, Y., Ding, Y., Yan, Q., and Pan, S. (2020). Graph-based semi-supervised learning: A review. _Neurocomputing_ , 408:216–230. 

- Chung, F. (1997). _Spectral Graph Theory_ . Conference Board of Mathematical Sciences. American Mathematical Society. 

- Cichocki, A., Mandic, D., De Lathauwer, L., Zhou, G., Zhao, Q., Caiafa, C., and Phan, H. A. (2015). Tensor Decompositions for Signal Processing Applications: From two-way to multiway component analysis. _IEEE Signal Processing Magazine_ , 32(2):145–163. 

- Collatz, L. and Sinogowitz, U. (1957). Spektren endlicher grafen. _Abhandlungen aus dem Mathematischen Seminar der Universit¨at Hamburg_ , 21:63–77. 

- Colonnese, S., Petti, M., Farina, L., Scarano, G., and Cuomo, F. (2021). Protein-protein interaction prediction via graph signal processing. _IEEE Access_ , 9:142681–142692. 

- Cooley, J. W. and Tukey, J. W. (1965). An algorithm for the machine calculation of complex fourier series. _Mathematics of Computation_ , 19:297–301. 

- Cvetkovic, D., Doob, M., and Sachs, H. (1980). _Spectra of Graphs: Theory and Application_ . Pure and applied mathematics : a series of monographs and textbooks. Academic Press. 

- DeBoor, C. (1979). Efficient computer manipulation of tensor products. _ACM Transactions on Mathematmal Software_ , 5:173–182. 

- Dees, B. S., Stankovi´c, L., Constantinides, A. G., and Mandic, D. P. (2020). Portfolio cuts: A graph-theoretic framework to diversification. In _ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 8454–8458. 

- Defferrard, M., Bresson, X., and Vandergheynst, P. (2017). Convolutional neural networks on graphs with fast localized spectral filtering. 

- Demmel, J. W. (1997). _Applied numerical linear algebra_ . Society for Industrial and Applied Mathematics, Philadelphia. 

- DeResende, B. M. and Costa, L. d. (2020). Characterization and comparison of large directed networks through the spectra of the magnetic Laplacian. _Chaos: An Interdisciplinary Journal of Nonlinear Science_ , 30(7):073141. 

_Bibliography_ 

212 

- Dong, X., Mavroeidis, D., Calabrese, F., and Frossard, P. (2015). Multiscale event detection in social media. _Data Min. Knowl. Discov._ , 29(5):1374–1405. 

- Dong, X., Thanou, D., Frossard, P., and Vandergheynst, P. (2016). Learning laplacian matrix in smooth graph signal representations. _IEEE Transactions on Signal Processing_ , 64(23):6160– 6173. 

- Dong, X., Thanou, D., Rabbat, M., and Frossard, P. (2019). Learning graphs from data: A signal representation perspective. _IEEE Signal Processing Magazine_ , 36(3):44–63. 

- Donoho, D. L. and Grimes, C. (2003). Hessian eigenmaps: Locally linear embedding techniques for high-dimensional data. _Proceedings of the National Academy of Sciences_ , 100(10):5591– 5596. 

- Duhamel, P. and Vetterli, M. (1990). Fast fourier transforms: A tutorial review and a state of the art. _Signal Processing_ , 19(4):259–299. 

- Elias, V. R. M., Gogineni, V. C., Martins, W. A., and Werner, S. (2022). Kernel regression over graphs using random fourier features. _IEEE Transactions on Signal Processing_ , 70:936–949. 

- Elman, H. C. (1982). _Iterative methods for large, sparse, nonsymmetric systems of linear equations_ . PhD thesis, Yale University. 

- EPA (2023). Us environmental protection agency: Air quality system data mart. `https://www. epa.gov/outdoor-air-quality-data` . Accessed: April 10, 2023. 

- Fackler, P. L. (2019). Algorithm 993: Efficient computation with kronecker products. _ACM Trans. Math. Softw._ , 45(2). 

- Fan, J., Li, R., Zhang, C., and Zou, H. (2020). _Statistical Foundations of Data Science_ . Chapman & Hall/CRC Data Science Series. CRC Press. 

- Fanuel, M., Ala´ız, C. M., and Suykens, J. A. K. (2017). Magnetic eigenmaps for community detection in directed networks. _Physical Review E_ , 95(2). 

- Federal Reserve Bank of St. Louis (2023). Fred ® (federal reserve economic data) online api. accessed june 30th, 2023. `https://fred.stlouisfed.org` . 

- Feller, W. (1968). _An Introduction to Probability Theory and Its Applications: Volume I_ . Number v. 2 in Wiley series in probability and mathematical statistics. John Wiley & sons. 

- Fiedler, M. (1973). Algebraic connectivity of graphs. _Czechoslovak Mathematical Journal_ , 23:298–305. 

- Fletcher, R. (2013). _Practical Methods of Optimization_ . Wiley. 

_Bibliography_ 

213 

- Fortune, S. (1986). A sweepline algorithm for voronoi diagrams. In _Proceedings of the Second Annual Symposium on Computational Geometry_ , SCG ’86, page 313–322, New York, NY, USA. Association for Computing Machinery. 

- Friedman, J., Hastie, T., and Tibshirani, R. (2007). Sparse inverse covariance estimation with the graphical lasso. _Biostatistics_ , 9(3):432–441. 

- Furutani, S., Shibahara, T., Akiyama, M., Hato, K., and Aida, M. (2020). Graph signal processing for directed graphs based on the hermitian laplacian. In Brefeld, U., Fromont, E., Hotho, A., Knobbe, A., Maathuis, M., and Robardet, C., editors, _Machine Learning and Knowledge Discovery in Databases_ , pages 447–463, Cham. Springer International Publishing. 

- Gadde, A. and Ortega, A. (2015). A probabilistic interpretation of sampling theory of graph signals. In _2015 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 3257–3261. 

- Gama, F., Isufi, E., Leus, G., and Ribeiro, A. (2020). Graphs, convolutions, and neural networks: From graph filters to graph neural networks. _IEEE Signal Processing Magazine_ , 37(6):128–138. 

- Gao, F. and Han, L. (2010). Implementing the nelder-mead simplex algorithm with adaptive parameters. _Computational Optimization and Applications_ , 51(1):259–277. 

- Gao, F. and Han, L. (2012). Implementing the Nelder-Mead simplex algorithm with adaptive parameters. _Comput. Optim. Appl._ , 51(1):259–277. 

- Gao, J., Ying, X., Xu, C., Wang, J., Zhang, S., and Li, Z. (2021). Graph-based stock recommendation by time-aware relational attention network. _ACM Trans. Knowl. Discov. Data_ , 16(1). 

- Gerschgorin, S. (1931). Uber die abgrenzung der eigenwerte einer matrix. _Izvestija Akademii Nauk SSSR, Serija Matematika_ , 7(3):749–754. 

- Giraldo, J. H., Mahmood, A., Garcia-Garcia, B., Thanou, D., and Bouwmans, T. (2022). Reconstruction of time-varying graph signals via sobolev smoothness. _IEEE Transactions on Signal and Information Processing over Networks_ , 8:201–214. 

- Goldsberry, L., Huang, W., Wymbs, N. F., Grafton, S. T., Bassett, D. S., and Ribeiro, A. (2017). Brain signal analytics from graph signal processing perspective. In _2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 851–855. 

- Granata, J., Conner, M., and Tolimieri, R. (1992). Recursive Fast Algorithms and the Role of the Tensor Product. _IEEE Transactions on Signal Processing_ , 40(12):2921–2930. 

_Bibliography_ 

214 

- Grassi, F., Loukas, A., Perraudin, N., and Ricaud, B. (2018). A time-vertex signal processing framework: Scalable processing and meaningful representations for time-series on graphs. _IEEE Transactions on Signal Processing_ , 66(3):817–829. 

- Gribonval, R. (2011). Should penalized least squares regression be interpreted as maximum a posteriori estimation? _IEEE Transactions on Signal Processing_ , 59(5):2405–2410. 

- Grote, M. J. and Huckle, T. (1997). Parallel preconditioning with sparse approximate inverses. _SIAM Journal on Scientific Computing_ , 18(3):838–853. 

- Guestrin, C., Bodik, P., Thibaux, R., Paskin, M., and Madden, S. (2004). Distributed regression: an efficient framework for modeling sensor network data. In _Third International Symposium on Information Processing in Sensor Networks, 2004. IPSN 2004_ , pages 1–10. 

- Hammond, D. K., Vandergheynst, P., and Gribonval, R. (2011). Wavelets on graphs via spectral graph theory. _Applied and Computational Harmonic Analysis_ , 30(2):129–150. 

- Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N. J., Kern, R., Picus, M., Hoyer, S., van Kerkwijk, M. H., Brett, M., Haldane, A., del R´ıo, J. F., Wiebe, M., Peterson, P., G´erard-Marchant, P., Sheppard, K., Reddy, T., Weckesser, W., Abbasi, H., Gohlke, C., and Oliphant, T. E. (2020). Array programming with NumPy. _Nature_ , 585(7825):357–362. 

- Hartigan, J. A. and Wong, M. A. (1979). Algorithm as 136: A k-means clustering algorithm. _Journal of the Royal Statistical Society. Series C (Applied Statistics)_ , 28(1):100–108. 

- Harzheim, E. (2005). Chapter 4 - products of orders. In _Ordered Sets_ , volume 7 of _Advances in Mathematics_ . Springer-Verlag, New York. 

- Hasanzadeh, A., Liu, X., Duffield, N. G., Narayanan, K. R., and Chigoy, B. T. (2017). A graph signal processing approach for real-time traffic prediction in transportation networks. _arXiv: Signal Processing_ . 

- He, K., Stankovic, L., Liao, J., and Stankovic, V. (2018). Non-intrusive load disaggregation using graph signal processing. _IEEE Transactions on Smart Grid_ , 9(3):1739–1747. 

- Hestenes, M. R. and Stiefel, E. (1952). Methods of conjugate gradients for solving linear systems. _Journal of research of the National Bureau of Standards_ , 49:409–435. 

- Hoffman, A. J. (1969). The change in the least eigenvalued of the adjacency matrix of a graph under imbedding. _SIAM Journal on Applied Mathematics_ , 17(4):664–671. 

- Holmes, D. E. and Jain, L. C. (2008). Introduction to bayesian networks. In _Innovations in Bayesian Networks_ . 

_Bibliography_ 

215 

- Horn, R. A. and Johnson, C. R. (2012). _Matrix Analysis_ . Cambridge University Press, 2 edition. 

- Hu, C., Cheng, L., Sepulcre, J., Johnson, K. A., Fakhri, G. E., Lu, Y. M., and Li, Q. (2015). A spectral graph regression model for learning brain connectivity of alzheimer’s disease. _PLOS ONE_ , 10(5):1–24. 

- Huang, W., Bolton, T. A. W., Medaglia, J. D., Bassett, D. S., Ribeiro, A., and Van De Ville, D. (2018). A graph signal processing perspective on functional brain imaging. _Proceedings of the IEEE_ , 106(5):868–885. 

- Huckel, E. (1931). Quantentheoretische beitr¨age zum benzolproblem. _Zeitschrift f¨ur Physik_ , 70(3-4):204–286. 

- Hull, J. (2009). _Options, Futures and Other Derivatives_ . Eastern economy edition. Pearson/Prentice Hall. 

- Hutchinson, M. (1990). A stochastic estimator of the trace of the influence matrix for laplacian smoothing splines. _Communications in Statistics - Simulation and Computation_ , 19(2):433– 450. 

- Imrich, W. and Klavˇzar, S. (2000). _Product Graphs: Structure and Recognition_ . A WileyInterscience publication. Wiley. 

- Ioannidis, V. N., Romero, D., and Giannakis, G. B. (2016). Kernel-based reconstruction of spacetime functions via extended graphs. In _2016 50th Asilomar Conference on Signals, Systems and Computers_ , pages 1829–1833. 

- Ioannidis, V. N., Romero, D., and Giannakis, G. B. (2018). Inference of spatio-temporal functions over graphs via multikernel kriged kalman filtering. _IEEE Transactions on Signal Processing_ , 66(12):3228–3239. 

- Isufi, E., Gama, F., Shuman, D. I., and Segarra, S. (2024). Graph filters for signal processing and machine learning on graphs. _IEEE Transactions on Signal Processing_ , pages 1–32. 

- Isufi, E., Loukas, A., Simonetto, A., and Leus, G. (2017). Autoregressive moving average graph filtering. _IEEE Transactions on Signal Processing_ , 65(2):274–288. 

- Itani, S. and Thanou, D. (2021). A graph signal processing framework for the classification of temporal brain data. In _2020 28th European Signal Processing Conference (EUSIPCO)_ , pages 1180–1184. 

- Jablonski, I. (2017). Graph signal processing in applications to sensor networks, smart grids, and smart cities. _IEEE Sensors Journal_ , 17(23):7659–7666. 

- Jha, K., Saha, S., and Singh, H. (2022). Prediction of protein–protein interaction using graph neural networks. _Scientific Reports_ , 12(1). 

_Bibliography_ 

216 

- Jiang, J. (2012). Introduction to spectral graph theory. 

- Jiang, J., Feng, H., Tay, D. B., and Xu, S. (2021). Theory and design of joint time-vertex nonsubsampled filter banks. _IEEE Transactions on Signal Processing_ , 69:1968–1982. 

- Kalofolias, V. (2016). How to learn a graph from smooth signals. 

- Kaveh, A. and Alinejad, B. (2011). Laplacian matrices of product graphs: applications in structural mechanics. _Acta Mechanica_ , 222:331–350. 

- Kelley, C. T. (1995). _Iterative Methods for Linear and Nonlinear Equations_ . Society for Industrial and Applied Mathematics. 

- Kelley, C. T. (2003). _Solving Nonlinear Equations with Newton’s Method_ . Society for Industrial and Applied Mathematics. 

- Kiers, H. A. L. (2000). Towards a standardized notation and terminology in multiway analysis. _Journal of Chemometrics_ , 14(3):105–122. 

- Kipf, T. N. and Welling, M. (2017). Semi-supervised classification with graph convolutional networks. 

- Kolaczyk, E. D. (2009). _Statistical Analysis of Network Data_ . Springer New York. 

- Kolda, T. G. and Bader, B. W. (2009). Tensor decompositions and applications. _SIAM Review_ , 51(3):455–500. 

- Kondor, R. I. and Lafferty, J. (2002). Diffusion kernels on graphs and other discrete structures. In _Proceedings of the 19th international conference on machine learning_ , volume 2002, pages 315–322. 

- Kriege, N. M., Johansson, F. D., and Morris, C. (2020). A survey on graph kernels. _Applied Network Science_ , 5(1):1–42. 

- Lake, B. and Tenenbaum, J. B. (2010). Discovering structure by learning sparse graphs. In _Proceedings of the 32nd Annual Conference of the Cognitive Science Society_ . 

- Le, C. M. and Li, T. (2022). Linear Regression and Its Inference on Noisy Network-Linked Data. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 84(5):1851–1885. 

- Lehoucq, R. B., Sorensen, D. C., and Yang, C. (1998). ARPACK users’ guide - solution of large-scale eigenvalue problems with implicitly restarted Arnoldi methods. In _Software, environments, tools_ . 

- LeMagoarou, L. and Gribonval, R. (2016). Are there approximate fast fourier transforms on graphs? In _2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 4811–4815, Shanghai. IEEE. 

_Bibliography_ 

217 

- Leus, G., Marques, A. G., Moura, J. M., Ortega, A., and Shuman, D. I. (2023). Graph signal processing: History, development, impact, and outlook. _IEEE Signal Processing Magazine_ , 40(4):49–60. 

- Li, R., Yuan, X., Radfar, M., Marendy, P., Ni, W., O’Brien, T. J., and Casillas-Espinosa, P. M. (2023). Graph signal processing, graph neural network and graph learning on biological data: A systematic review. _IEEE Reviews in Biomedical Engineering_ , 16:109–135. 

- Li, T., Levina, E., and Zhu, J. (2019). Prediction models for network-linked data. _The Annals of Applied Statistics_ , 13(1):132 – 164. 

- Little, R. and Rubin, D. (2019). _Statistical Analysis with Missing Data_ . Wiley Series in Probability and Statistics. Wiley. 

- Loukas, A. and Foucard, D. (2016). Frequency analysis of time-varying graph signals. In _2016 IEEE Global Conference on Signal and Information Processing (GlobalSIP)_ , pages 346–350. 

- MacQueen, J. (1967). Classification and analysis of multivariate observations. In _5th Berkeley Symp. Math. Statist. Probability_ , pages 281–297. University of California Los Angeles LA USA. 

- Makhoul, J. (1980). A fast cosine transform in one and two dimensions. _IEEE Transactions on Acoustics, Speech, and Signal Processing_ , 28(1):27–34. 

- Marques, A. G., Kiyavash, N., Moura, J. M., Van De Ville, D., and Willett, R. (2020a). Graph signal processing: Foundations and emerging directions [from the guest editors]. _IEEE Signal Processing Magazine_ , 37(6):11–13. 

- Marques, A. G., Segarra, S., Leus, G., and Ribeiro, A. (2016). Sampling of graph signals with successive local aggregations. _IEEE Transactions on Signal Processing_ , 64(7):1832–1843. 

- Marques, A. G., Segarra, S., and Mateos, G. (2020b). Signal processing on directed graphs: The role of edge directionality when processing and learning from network data. _IEEE Signal Processing Magazine_ , 37(6):99–116. 

- Marti, G., Nielsen, F., Bi´nkowski, M., and Donnat, P. (2021). _A Review of Two Decades of Correlations, Hierarchies, Networks and Clustering in Financial Markets_ , pages 245–274. Springer International Publishing, Cham. 

- Martin, D., Fowlkes, C., Tal, D., and Malik, J. (2001). A database of human segmented natural images and its application to evaluating segmentation algorithms and measuring ecological statistics. In _Proc. 8th Int’l Conf. Computer Vision_ , volume 2, pages 416–423. 

- Mateos, G., Segarra, S., Marques, A. G., and Ribeiro, A. (2019). Connecting the dots: Identifying network structure via graph signal processing. _IEEE Signal Processing Magazine_ , 36(3):16–43. 

_Bibliography_ 

218 

- Menoret, M., Farrugia, N., Pasdeloup, B., and Gripon, V. (2017). Evaluating graph signal processing for neuroimaging through classification and dimensionality reduction. In _2017 IEEE Global Conference on Signal and Information Processing (GlobalSIP)_ , pages 618–622. 

- Miao, X., Jiang, A., Zhu, Y., and Kwan, H. K. (2022). A joint learning framework for gaussian processes regression and graph learning. _Signal Processing_ , 201:108708. 

- Mieghem, P. v. (2010). _Graph Spectra for Complex Networks_ . Cambridge University Press. 

- Minaee, S., Boykov, Y., Porikli, F., Plaza, A., Kehtarnavaz, N., and Terzopoulos, D. (2022). Image segmentation using deep learning: A survey. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , 44(7):3523–3542. 

- Murphy, K. P. (2012). _Machine learning: a probabilistic perspective_ . MIT Press, Cambridge, MA. 

- Narang, S. K., Gadde, A., and Ortega, A. (2013a). Signal processing techniques for interpolation in graph structured data. In _2013 IEEE International Conference on Acoustics, Speech and Signal Processing_ , pages 5445–5449. 

- Narang, S. K., Gadde, A., Sanou, E., and Ortega, A. (2013b). Localized iterative methods for interpolation in graph structured data. In _2013 IEEE Global Conference on Signal and Information Processing_ , pages 491–494. 

- Nelder, J. A. and Wedderburn, R. W. M. (1972). Generalized linear models. _Journal of the Royal Statistical Society. Series A (General)_ , 135(3):370–384. 

- ONS (2019). Local Authority Districts (December 2019) Boundaries UK BUC. `https://www.data.gov.uk/dataset/e73c1990-ad5d-4184-8fb1-b474b94918ba/ local-authority-districts-december-2019-boundaries-uk-buc` . Accessed: 202305-30. 

- Orieux, F., Feron, O., and Giovannelli, J.-F. (2012). Sampling high-dimensional gaussian distributions for general linear inverse problems. _IEEE Signal Processing Letters_ , 19(5):251–254. 

- Orn, G. G., Boem, F., and Toni, L. (2022). Graph-based learning for leak detection and localisation in water distribution networks*. _IFAC-PapersOnLine_ , 55(6):661–666. 

- Ortega, A. (2022). _Introduction to Graph Signal Processing_ . Cambridge University Press. 

- Ortega, A., Frossard, P., Kovaˇcevi´c, J., Moura, J. M. F., and Vandergheynst, P. (2018). Graph signal processing: Overview, challenges, and applications. _Proceedings of the IEEE_ , 106(5):808–828. 

_Bibliography_ 

219 

- Papandreou, G. and Yuille, A. L. (2010). Gaussian sampling by local perturbations. In Lafferty, J., Williams, C., Shawe-Taylor, J., Zemel, R., and Culotta, A., editors, _Advances in Neural Information Processing Systems_ , volume 23. Curran Associates, Inc. 

- Pare, P. E., Beck, C. L., and Basar, T. (2020). Modeling, estimation, and analysis of epidemics over networks: An overview. _Annual Reviews in Control_ , 50:345–360. 

- Pereyra, V. and Scherer, G. (1973). Efficient computer manipulation of tensor products with applications to multidimensional approximation. _Mathematics of Computation_ , 27:595–605. 

- Perraudin, N. and Vandergheynst, P. (2017). Stationary signal processing on graphs. _IEEE Transactions on Signal Processing_ , 65(13):3462–3477. 

- Peters, G., Zhu, R., Tzougas, G., Rabitti, G., and Yusuf, I. (2022). The role and significance of green bonds in funding transition to a low carbon economy: A case study forecasting portfolios of green bond instrument returns. _SSRN Electron. J._ 

- Pu, X., Chau, S. L., Dong, X., and Sejdinovic, D. (2021). Kernel-based graph learning from smooth signals: A functional viewpoint. _IEEE Transactions on Signal and Information Processing over Networks_ , 7:192–207. 

- Puschel, M. and Moura, J. M. F. (2003). The algebraic approach to the discrete cosine and sine transforms and their fast algorithms. _SIAM Journal on Computing_ , 32(5):1280–1316. 

- Puschel, M. and Moura, J. M. F. (2006). Algebraic signal processing theory. 

- Puschel, M. and Moura, J. M. F. (2008). Algebraic signal processing theory: Foundation and 1-d time. _IEEE Transactions on Signal Processing_ , 56(8):3572–3585. 

- Qiao, L., Zhang, L., Chen, S., and Shen, D. (2018). Data-driven graph construction and graph learning: A review. _Neurocomputing_ , 312:336–351. 

- Qiu, K., Mao, X., Shen, X., Wang, X., Li, T., and Gu, Y. (2017). Time-varying graph signal reconstruction. _IEEE Journal of Selected Topics in Signal Processing_ , 11(6):870–883. 

- Rabiner, L. and Gold, B. (1975). _Theory and Application of Digital Signal Processing_ . PrenticeHall signal processing series. Prentice-Hall. 

- Ramakrishna, R. and Scaglione, A. (2021). Grid-graph signal processing (grid-gsp): A graph signal processing framework for the power grid. _IEEE Transactions on Signal Processing_ , 69:2725–2739. 

- Rao, K. and Yip, P. (1990). _Discrete Cosine Transform: Algorithms, Advantages, Applications_ . Elsevier Science & Technology Books. 

_Bibliography_ 

220 

- Rasmussen, C. E. and Williams, C. K. I. (2005). _Gaussian Processes for Machine Learning_ . The MIT Press. 

- Renteln, P. (2013). _Manifolds, Tensors, and Forms: An Introduction for Mathematicians and Physicists_ . Cambridge University Press. 

- Rimleanscaia, O. and Isufi, E. (2020). Rational chebyshev graph filters. In _2020 54th Asilomar Conference on Signals, Systems, and Computers_ , pages 736–740. 

- Rivlin, T. (2020). _Chebyshev Polynomials_ . Dover Books on Mathematics. Dover Publications. 

- Romero, D., Ioannidis, V. N., and Giannakis, G. B. (2017a). Kernel-based reconstruction of space-time functions on dynamic graphs. _IEEE Journal of Selected Topics in Signal Processing_ , 11(6):856–869. 

- Romero, D., Ma, M., and Giannakis, G. B. (2017b). Kernel-based reconstruction of graph signals. _IEEE Transactions on Signal Processing_ , 65(3):764–778. 

- Roth, W. E. (1934). On direct product matrices. _Bulletin of the American Mathematical Society_ . Roweis, S. T. and Saul, L. K. (2000). Nonlinear dimensionality reduction by locally linear embedding. _Science_ , 290(5500):2323–2326. 

- Saad, Y. (2003). _Iterative Methods for Sparse Linear Systems_ . Society for Industrial and Applied Mathematics, second edition. 

- Saad, Y. and Schultz, M. H. (1986). Gmres: a generalized minimal residual algorithm for solving nonsymmetric linear systems. _Siam Journal on Scientific and Statistical Computing_ , 7:856– 869. 

- Sandryhaila, A. and Moura, J. M. F. (2013a). Classification via regularization on graphs. In _2013 IEEE Global Conference on Signal and Information Processing_ , pages 495–498. 

- Sandryhaila, A. and Moura, J. M. F. (2013b). Discrete signal processing on graphs. _IEEE Transactions on Signal Processing_ , 61(7):1644–1656. 

- Sandryhaila, A. and Moura, J. M. F. (2013c). Discrete signal processing on graphs: Frequency analysis. 

- Sardellitti, S., Barbarossa, S., and Di Lorenzo, P. (2017). On the graph fourier transform for directed graphs. _IEEE Journal of Selected Topics in Signal Processing_ , 11(6):796–811. 

- Sayama, H. (2016). Estimation of laplacian spectra of direct and strong product graphs. _Discrete Applied Mathematics_ , 205:160–170. 

- Scholkopf, B. and Smola, A. J. (2018). _Learning with Kernels: Support Vector Machines, Regularization, Optimization, and Beyond_ . The MIT Press. 

_Bibliography_ 

221 

- Shafipour, R., Khodabakhsh, A., Mateos, G., and Nikolova, E. (2019). A directed graph fourier transform with spread frequency components. _IEEE Transactions on Signal Processing_ , 67(4):946–960. 

- Shubin, M. A. (1994). Discrete magnetic laplacian. _Communications in Mathematical Physics_ , 164(2):259–275. 

- Shuman, D. I., Narang, S. K., Frossard, P., Ortega, A., and Vandergheynst, P. (2013). The emerging field of signal processing on graphs: Extending high-dimensional data analysis to networks and other irregular domains. _IEEE Signal Processing Magazine_ , 30(3):83–98. 

- Shuman, D. I., Vandergheynst, P., Kressner, D., and Frossard, P. (2018). Distributed signal processing via chebyshev polynomial approximation. _IEEE Transactions on Signal and Information Processing over Networks_ , 4(4):736–751. 

- Smith, W. and Smith, J. (1995). _Handbook of Real-Time Fast Fourier Transforms: Algorithms to Product Testing_ . Wiley. 

- Smola, A. J. and Kondor, R. (2003). Kernels and regularization on graphs. In Sch¨olkopf, B. and Warmuth, M. K., editors, _Learning Theory and Kernel Machines_ , pages 144–158, Berlin, Heidelberg. Springer Berlin Heidelberg. 

- Sneddon, I. (1995). _Fourier Transforms_ . Dover books on mathematics. Dover Publications. 

- Spielman, D. A. (2019). _Spectral and Algebraic Graph Theory_ . Upcoming. 

- Srivastava, D., Bagler, G., and Kumar, V. (2023). Graph signal processing on protein residue networks helps in studying its biophysical properties. _Physica A: Statistical Mechanics and its Applications_ , 615:128603. 

- Stanley, J. S., Chi, E. C., and Mishne, G. (2020). Multiway Graph Signal Processing on Tensors: Integrative Analysis of Irregular Geometries. _IEEE Signal Processing Magazine_ , 37(6):160– 173. 

- Tanaka, Y., Eldar, Y. C., Ortega, A., and Cheung, G. (2020). Sampling signals on graphs: From theory to applications. _IEEE Signal Processing Magazine_ , 37(6):14–30. 

- Tang, J. M. and Saad, Y. (2012). A probing method for computing the diagonal of a matrix inverse. _Numerical Linear Algebra with Applications_ , 19(3):485–501. 

- Tay, D. B. (2021). Sensor network data denoising via recursive graph median filters. _Signal Processing_ , 189:108302. 

- Tolimieri, R., An, M., Lu, C., and Burrus, C. S. (2013). _Algorithms for discrete Fourier transform and convolution_ . Signal Processing and Digital Filtering. Springer, New York, NY, 1989 edition. 

_Bibliography_ 

222 

- Tran, N., Ambos, H., and Jung, A. (2020). Classifying partially labeled networked data via logistic network lasso. In _ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 3832–3836. 

- Tseng, C.-C. (2020). Rational graph filter design using spectral transformation and iir digital filter. In _2020 IEEE REGION 10 CONFERENCE (TENCON)_ , pages 247–250. 

- Varma, R., Chen, S., and Kovaˇcevi´c, J. (2015). Spectrum-blind signal recovery on graphs. In _2015 IEEE 6th International Workshop on Computational Advances in Multi-Sensor Adaptive Processing (CAMSAP)_ , pages 81–84. 

- Venkitaraman, A., Chatterjee, S., and Handel, P. (2020). Gaussian processes over graphs. In _ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 5640–5644. 

- Venkitaraman, A., Chatterjee, S., and H¨andel, P. (2019). Predicting graph signals using kernel regression where the input signal is agnostic to a graph. _IEEE Transactions on Signal and Information Processing over Networks_ , 5(4):698–710. 

- Vinicius, J. d. M. C., Ying, J., and Palomar, D. P. (2020). Algorithms for learning graphs in financial markets. 

- Vono, M., Dobigeon, N., and Chainais, P. (2022). High-dimensional gaussian sampling: A review and a unifying approach based on a stochastic proximal point algorithm. _SIAM Review_ , 64(1):3–56. 

- Wagner, R., Baraniuk, R., Du, S., Johnson, D., and Cohen, A. (2006). An architecture for distributed wavelet analysis and processing in sensor networks. In _2006 5th International Conference on Information Processing in Sensor Networks_ , pages 243–250. 

- Wagner, R., Choi, H., Baraniuk, R., and Delouille, V. (2005). Distributed wavelet transform for irregular sensor network grids. In _IEEE/SP 13th Workshop on Statistical Signal Processing, 2005_ , pages 1196–1201. 

- Wang, J., Zhang, S., Xiao, Y., and Song, R. (2022a). A review on graph neural network methods in financial applications. 

- Wang, X., Liu, P., and Gu, Y. (2015a). Local-set-based graph signal reconstruction. _IEEE Transactions on Signal Processing_ , 63(9):2432–2444. 

- Wang, X., Wang, M., and Gu, Y. (2015b). A distributed tracking algorithm for reconstruction of graph signals. _IEEE Journal of Selected Topics in Signal Processing_ , 9(4):728–740. 

_Bibliography_ 

223 

- Wang, Y., Ahsan, U., Li, H., and Hagen, M. (2022b). A comprehensive review of modern object segmentation approaches. _Foundations and Trends in Computer Graphics and Vision_ , 13(2-3):111–283. 

- Wang, Y., Zhao, B., Li, X., Luan, W., and Liu, B. (2022c). Abnormal battery identification via graph signal processing method. In _2022 7th Asia Conference on Power and Electrical Engineering (ACPEE)_ , pages 208–212. 

- Wang, Y.-X., Sharpnack, J., Smola, A. J., and Tibshirani, R. J. (2016). Trend filtering on graphs. _J. Mach. Learn. Res._ , 17(1):3651–3691. 

- West, R. M. (2022). Best practice in statistics: The use of log transformation. _Annals of Clinical Biochemistry_ , 59(3):162–165. 

- Xiao, S., Wang, S., Dai, Y., and Guo, W. (2021a). Graph neural networks in node classification: survey and evaluation. _Machine Vision and Applications_ , 33(1). 

- Xiao, Z., Fang, H., and Wang, X. (2021b). Anomalous iot sensor data detection: An efficient approach enabled by nonlinear frequency-domain graph analysis. _IEEE Internet of Things Journal_ , 8(5):3812–3821. 

- Xiu, C., Sun, Y., and Peng, Q. (2022). Modelling traffic as multi-graph signals: Using domain knowledge to enhance the network-level passenger flow prediction in metro systems. _Journal of Rail Transport Planning & Management_ , 24:100342. 

- Ying, W., Rui, X., Xiaoyang, M., Qiang, F., Jinshuai, Z., and Runze, Z. (2022). Spectral graph theory-based recovery method for missing harmonic data. _IEEE Transactions on Power Delivery_ , 37(5):3688–3697. 

- Zhang, C., Florencio, D., and Chou, P. A. (2015). Graph signal processing - a probabilistic framework. Technical Report MSR-TR-2015-31, Microsoft Research. 

- Zhang, S., Deng, Q., and Ding, Z. (2023a). Signal processing over multilayer graphs: Theoretical foundations and practical applications. _IEEE Internet of Things Journal_ , pages 1–1. 

- Zhang, S., Ma, X., Fang, Z., Pan, H., Yang, G., and Arce, G. R. (2023b). Financial time series forecasting based on momentum-driven graph signal processing. _Applied Intelligence_ . 

- Zhang, X., He, Y., Brugnone, N., Perlmutter, M., and Hirn, M. (2021). Magnet: A neural network for directed graphs. 

- Zhang, Z.-W., Jing, X.-Y., and Wang, T.-J. (2017). Label propagation based semi-supervised learning for software defect prediction. _Autom. Softw. Eng._ , 24(1):47–69. 

_Bibliography_ 

224 

- Zheng, D., Ma, X., Wang, Y., Wang, Y., and Luo, H. (2022). Non-intrusive load monitoring based on the graph least squares reconstruction method. _IEEE Transactions on Power Delivery_ , 37(4):2562–2570. 

- Zhi, Y.-C., Ng, Y. C., and Dong, X. (2023). Gaussian processes on graphs via spectral kernel learning. _IEEE Transactions on Signal and Information Processing over Networks_ , 9:304–314. 

- Zhou, D. and Sch¨olkopf, B. (2004). A regularization framework for learning from graph data. In _ICML Workshop on Statistical Relational Learning and Its Connections to Other Fields_ . 

- Zhou, F., Jiang, J., and Tay, D. B. (2022a). Distributed reconstruction of time-varying graph signals via a modified newton’s method. _Journal of the Franklin Institute_ , 359(16):9401–9421. 

- Zhou, J., Cui, G., Hu, S., Zhang, Z., Yang, C., Liu, Z., Wang, L., Li, C., and Sun, M. (2020). Graph neural networks: A review of methods and applications. _AI Open_ , 1:57–81. 

- Zhou, X., Liu, S., Xu, W., Xin, K., Wu, Y., and Meng, F. (2022b). Bridging hydraulics and graph signal processing: A new perspective to estimate water distribution network pressures. _Water Research_ , 217:118416. 

- Zhu, X., Ghahramani, Z., and Lafferty, J. (2003). Semi-supervised learning using gaussian fields and harmonic functions. In _Proceedings of the Twentieth International Conference on International Conference on Machine Learning_ , ICML’03, page 912–919. AAAI Press. 

- Zhu, X. and Rabbat, M. (2012). Graph spectral compressed sensing for sensor networks. In _2012 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 2865–2868. 

_Bibliography_ 

225 

