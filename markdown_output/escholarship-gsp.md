## **UC San Diego** 

## **UC San Diego Electronic Theses and Dissertations** 

## **Title** 

Generalizing Graph Laplacian Learning: a Graph Signal Processing Perspective 

## **Permalink** 

https://escholarship.org/uc/item/8tv0t2m0 

## **Author** 

Shi, Changhao 

## **Publication Date** 

2024 

Peer reviewed|Thesis/dissertation 

eScholarship.org 

Powered by the California Digital Library University of California 

UNIVERSITY OF CALIFORNIA SAN DIEGO 

Generalizing Graph Laplacian Learning: a Graph Signal Processing Perspective 

A dissertation submitted in partial satisfaction of the requirements for the degree Doctor of Philosophy 

in 

Electrical Engineering (Machine Learning and Data Science) 

by 

Changhao Shi 

Committee in charge: 

Professor Gal Mishne, Chair Professor Mikio Aoi Professor Vikash Gilja Professor Piya Pal Professor Yusu Wang 

2025 

Copyright 

Changhao Shi, 2025 All rights reserved. 

The Dissertation of Changhao Shi is approved, and it is acceptable in quality and form for publication on microfilm and electronically. 

University of California San Diego 

2025 

iii 

## TABLE OF CONTENTS 

|Dissertation Approval Page . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|Dissertation Approval Page . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|iii|
|---|---|---|
|Table of Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||iv|
|List of Figures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||vi|
|List of Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||ix|
|Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||x|
|Vita . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|xi|
|Abstract of the Dissertation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||xii|
|Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||1|
|Chapter|1<br>Graphs and Signal Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|5|
|1.1|Combinatorial Graph Laplacian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|5|
|1.2|Graph Signals and Fourier Transforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|7|
|1.3|Graph Inference from Smooth Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|8|
|Chapter|2<br>Graph Inference from Noisy Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
|2.1|Gaussian Noise Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
|2.2|Exponential Family Noise Models. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
||2.2.1<br>Exponential Family Noise Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
||2.2.2<br>Graph Inference with Exponential Family Noise . . . . . . . . . . . . . . . . . . . .|15|
||2.2.3<br>Noise Model Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|17|
|2.3|Graph Inference Extensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|19|
||2.3.1<br>Graph Inference with Offsets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|19|
||2.3.2<br>Graph Inference from Time Series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|20|
|2.4|Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|22|
||2.4.1<br>Synthetic Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|22|
||2.4.2<br>Chicago Crime Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|28|
||2.4.3<br>Animals Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|31|
||2.4.4<br>Neural Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|32|
|Chapter|3<br>Graph Inference from Multi-Way Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . .|37|
|3.1|Multi-way Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|37|
|3.2|Graph Inference for Multi-way Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|40|
||3.2.1<br>Penalized MLE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|40|
||3.2.2<br>Multi-Way Graph Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|41|
||3.2.3<br>Structural Missing Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|43|
|3.3|Theoretical Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|44|



iv 

|3.4|Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|46|
|---|---|---|
||3.4.1<br>Synthetic Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|46|
||3.4.2<br>Molene Weather Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|50|
||3.4.3<br>COIL-20 Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|51|
|3.5|Proofs of Theoretical Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|52|
||3.5.1<br>Proof of Lemma 1: Effcient Computation . . . . . . . . . . . . . . . . . . . . . . . . .|52|
||3.5.2<br>Proof of Theorem 2: Existence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|54|
||3.5.3<br>Proof of Theorem 3: Uniqueness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|57|
||3.5.4<br>Proof of Theorem 4: Consistency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|58|
|Chapter|4<br>Generalized Product Graph Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|68|
|4.1|Kronecker Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|68|
|4.2|Generalized Inference of Product Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|70|
||4.2.1<br>MLE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|70|
||4.2.2<br>Kronecker Structured Graph Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|71|
||4.2.3<br>Connection to Strong Product Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|73|
|4.3|Theoretical Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|74|
|4.4|Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|76|
||4.4.1<br>Synthetic Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|76|
||4.4.2<br>EEG Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|79|
|4.5|Proofs of Theoretical Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|82|
||4.5.1<br>Proof of Theorem 6: Existence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|82|
||4.5.2<br>Proof of Theorem 7: Uniqueness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|84|
||4.5.3<br>Proof of Theorem 8: Consistency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|85|
|Chapter|5<br>Signal Denoising against Off-Manifold Adversarial Attacks . . . . . . . . . . . . .|99|
|5.1|Manifold Assumption and Adversarial Robustness . . . . . . . . . . . . . . . . . . . . . . . . .|99|
|5.2|Self-Supervised Purifcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|103|
||5.2.1<br>Problem Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|103|
||5.2.2<br>Self-supervised Online Purifcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|103|
||5.2.3<br>Online Purifcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|105|
||5.2.4<br>Self-Supervised Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|107|
|5.3|Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|109|
||5.3.1<br>White-box attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|111|
||5.3.2<br>Black-box attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|116|
|Chapter|6<br>Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|118|
|6.1|Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|118|
|6.2|Future Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|120|
|Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||122|



v 

## LIST OF FIGURES 

|Figure|2.1.|Graph Laplacian learning with Exponential Family Noise (GLEN). . . . . . .|13|
|---|---|---|---|
|Figure|2.2.|Examples of the inferred and ground truth graph Laplacian. The synthetic||
|||signals are generated with the Binomial noise model. Rows correspond||
|||to different graph generators and columns correspond to different graph||
|||inference methods or ground truth graphs. . . . . . . . . . . . . . . . . . . . . . . . . . . .|29|
|Figure|2.3.|Rank of the crimes by their mean occurrences (a), and graphs inferred from||
|||the Chicago crime dataset using original CGL (b) and GLEN with offsets||
|||(c). Nodes correspond to crime types. The width of the edges corresponds||
|||to the edge weights. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|30|
|Figure|2.4.|Heat-maps of the inferred graphs of GLS-1, GLS-2, CGL, and GLEN.||
|||Animals are ordered to refect their taxonomy, where each red square||
|||highlights one of the 5 animal ‘classes’. The corresponding animal ‘classes’||
|||and the ‘orders’ of mammals are shown on the right. . . . . . . . . . . . . . . . . . .|33|
|Figure|2.5.|Average raw neural spiking data compared against average denoised signals||
|||by GLEN-TV, for each target direction shown on the left. The brighter||
|||color indicates a higher fring rate. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|35|
|Figure|2.6.|Average raw neural spiking data compared against average denoised signals||
|||by GLEN-TV, for each target direction shown on the left. The brighter||
|||color indicates a higher fring rate. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|36|
|Figure|3.1.|An example of the Cartesian graph product. . . . . . . . . . . . . . . . . . . . . . . . . . .|38|
|Figure|3.2.|Comparison of different methods on various synthetic data. Each sub-fgure||
|||shows the trend of Rel-Err of the product or factor Laplacian matrices as_n_||
|||increases. Black dash lines ft the theory in (3.12) to our results. . . . . . . . . .|47|
|Figure|3.3.|Comparison of different methods on synthetic data in various scenarios.||
|||Each sub-fgure shows the PR-AUC of edge estimation as_n_increases. . . .|48|
|Figure|3.4.|Comparison of different methods on synthetic data in various scenarios.||
|||Each sub-fgure shows the trend of Rel-Err of the product or factor Lapla-||
|||cian matrices asmin(_p_1_, p_2))increases. Black dash lines ft the theory in||
|||(3.12) to our results.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|50|
|Figure|3.5.|The inferred factor graphs of Molene. Stations are placed according to||
|||their real coordinates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|51|



vi 

|Figure|3.6.|Comparing the learned station graph of PGL, TeraLasso, and MWGL (ours)||
|---|---|---|---|
|||on the Molene dataset with varying regularization. Laplacians are ordered||
|||with increasing sparsity from left to right. . . . . . . . . . . . . . . . . . . . . . . . . . . .|51|
|Figure|3.7.|(a) The inferred object graph and (b) selected imputations of the COIL-20||
|||dataset. The frst column is observed images and the other columns are||
|||reconstructions across missing angles. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|53|
|Figure|4.1.|An example of the Kronecker graph product. . . . . . . . . . . . . . . . . . . . . . . . . .|68|
|Figure|4.2.|Comparison of different methods on various synthetic Kronecker product||
|||graphs and signals. Each sub-fgure shows the trend of Rel-Err of the||
|||product (top row) or factor (middle and bottom rows) Laplacian matrices||
|||as_n_increases. Black dash lines ft the theory in (4.8) to the KSGL results.|76|
|Figure|4.3.|Comparison of different methods on various synthetic Kronecker product||
|||graphs and signals. Each sub-fgure shows the trend of PR-AUC of the||
|||product or factor edge prediction as_n_increases. . . . . . . . . . . . . . . . . . . . . . .|77|
|Figure|4.4.|Comparison of different methods on various synthetic strong product||
|||graphs and signals. Each sub-fgure shows the trend of Rel-Err as _n_ in-||
|||creases. Black dash lines ft the theory in (4.8) to our results. . . . . . . . . . . .|79|
|Figure|4.5.|Comparison of different methods on various synthetic strong product||
|||graphs and signals. Each sub-fgure shows the trend of PR-AUC of the||
|||product or factor edge prediction as_n_increases. . . . . . . . . . . . . . . . . . . . . . .|80|
|Figure|4.6.|The brain connectivity inferred by KSGL. Electrodes are placed by the||
|||10-20 system. The background color shows the mean activity of each status.|81|
|Figure|4.7.|The time graphs of the epileptic signals inferred by KSGL. . . . . . . . . . . . .|81|
|Figure|4.8.|Degree distributions of the learned brain graphs from normal and epileptic||
|||EEG of different patients. The red vertical lines indicate the average node||
|||degree of the distributions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|82|
|Figure|5.1.|An illustration of self-supervised online adversarial purifcation (SOAP). .|101|
|Figure|5.2.|Input digits of the encoder (left) and output digits of the decoder (right). . .|108|
|Figure|5.3.|Auxiliary loss vs. _ε_pfy. SOAP (green plot) reduces the high adversarial||
|||auxiliary loss (orange plot) to the low clean level (blue plot). The vertical||
|||dashed line is the value of_ε_adv. The trained models are FCN and ResNet-18||
|||for MNIST and CIFAR10, respectively, with a PGD attack. . . . . . . . . . . . . .|109|



vii 

|Figure|5.4.|Adversarial and purifed CIFAR10 examples by SOAP with Wide-ResNet-|
|---|---|---|
|||28 under PGD attacks. True classes are shown on the top of each column|
|||and the model predictions are shown under each image. . . . . . . . . . . . . . . . . 114|
|Figure|5.5.|Purifcation against auxiliary-aware PGD attacks. Plots are classifcation|
|||accuracy before (blue) and after (orange) purifcation. . . . . . . . . . . . . . . . . . 116|



viii 

## LIST OF TABLES 

|Table|2.1.|Exponential family distributions and link functions . . . . . . . . . . . . . . . . . . . .|13|
|---|---|---|---|
|Table|2.2.|Numerical comparison of graph learning with Poisson noise (N=20). . . . . .|23|
|Table|2.3.|Numerical comparison of graph learning with Binomial noises (N=20). . . .|24|
|Table|2.4.|Numerical comparison of graph learning with Poisson noise (N=50). . . . . .|25|
|Table|2.5.|Numerical comparison of graph learning with Binomial noises (N=50). . . .|26|
|Table|2.6.|Comparing PR-AUC on the animal classifcation task. . . . . . . . . . . . . . . . . . .|32|
|Table|5.1.|MNIST Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|112|
|Table|5.2.|CIFAR-10 results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|113|
|Table|5.3.|CIFAR-100 results. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|115|
|Table|5.4.|MNIST Black-box Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|117|



ix 

## ACKNOWLEDGEMENTS 

I would like to acknowledge Professor Gal Mishne for her generous support as the chair of my committee. Through multiple drafts and many long nights, her guidance has proved to be invaluable. I would also like to acknowledge Professor Mikio Aoi and Professor Eric C. Chi for their helpful discussion. 

Chapter 2, in full, has been submitted for publication in IEEE Transaction on Signal and Information Processing over Networks, Shi, Changhao; Mishne, Gal. The dissertation author was the primary investigator and author of this paper. 

Chapter 3, in full, is a reprint of the material as it appears in the Proceedings of The 27th International Conference on Artificial Intelligence and Statistics, Shi, Changhao; Mishne, Gal, 2024. The dissertation author was the primary investigator and author of this paper. 

Chapter 4, in full, has been prepared for publication, Shi, Changhao; Mishne, Gal. The dissertation author was the primary investigator and author of this paper. 

Chapter 5, in full, is a reprint of the material as it appears in the Proceedings of The 9th International Conference on Learning Representation, Shi, Changhao; Holtz, Chester; Mishne, Gal, 2021. The dissertation author was the primary investigator and author of this paper. 

x 

## VITA 

2014-2018 Bachelor of Science, Beihang University 

2018-2025 Doctor of Philosophy, University of California San Diego 

## PUBLICATIONS 

“Learning Cartesian Product Graphs with Laplacian Constraints” Proceedings of The 27th International Conference on Artificial Intelligence and Statistics, PMLR 238:2521-2529, 2024 

“Online Adversarial Purification based on Self-supervised Learning” International Conference on Learning Representations, 2021 

xi 

## ABSTRACT OF THE DISSERTATION 

Generalizing Graph Laplacian Learning: a Graph Signal Processing Perspective 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0013-02.png)


## Changhao Shi 

Doctor of Philosophy in Electrical Engineering (Machine Learning and Data Science) 

## University of California San Diego, 2025 

## Professor Gal Mishne, Chair 

Graph Signal Processing (GSP) extends classical signal processing (SP) to non-Euclidean domains. For a complex system, GSP studies the matrix representation of its graph abstraction. The spectral decomposition of these graph representations carries important geometric information, from which the Graph Fourier Transform (GFT) is established to analyze and process the data on the graph. GSP finds its applications in many fields, but a prominent problem of applying GSP is that the graph abstraction of the studied system is frequently unobserved. To tackle this problem, GSP resorts to a principled method for learning these graphs from smooth nodal observations (signals), called graph learning or network topology inference. 

This dissertation presents our recent efforts to expand the scope of graph learning. The 

xii 

first part of our work generalizes graph learning beyond Gaussian distributed data. We use conditional exponential family distributions to define a noise model on top of latent smooth signal representations. This results in a new graph signal generator encompassing other data types such as binary and count data. The combinatorial graph Laplacian and the latent smooth signal representations are then jointly inferred from the noisy observations. The second part focuses on imposing structural priors to the graph we learn. We are specifically interested in product graphs because they naturally model the factorized dependencies that emerge from multi-way signal processing. We formulate graph learning under the assumption of common graph products: the Cartesian, the Kronecker, and the strong product, and propose algorithms to solve the derived optimization problem. We also study the theoretical aspects of product graph learning and prove that the learned graph Laplacian converges to the true graph Laplacian asymptotically. For the third part which is beyond the scope of GSP, we present a deep learning framework that utilizes the geometry of data to defend against adversarial attacks. Instead of directly learning a graph, the underlying manifold is characterized by an auxiliary score induced by self-supervised representation learning. An application of this is adversarial defense. Realizing that adversarial samples are usually off-manifold, we retract these malicious samples back to the manifold using the guidance of the auxiliary tasks. Finally, we revisit the proposed methods and point out some promising future directions to explore. 

xiii 

## **Introduction** 

Graphs are powerful tools for modeling relationships among a set of entities in complex systems and have become prevalent in biology (Pavlopoulos et al., 2011), neuroscience (Bassett and Sporns, 2017), social science (Borgatti et al., 2009), and many other scientific fields. In machine learning and artificial intelligence, there is also a growing interest in graphs for model boosting (Shuman et al., 2013; Wu et al., 2020; Ji et al., 2021). 

As the graph of a system is frequently unobserved, a prominent problem in graph machine learning is how to construct a graph from available data for further use. While ad-hoc graph construction rules (e.g. k-nearest neighbor graphs) exist in many fields, it is arguably more appealing to learn those graphs in a more principled way. To be more specific, given a set of nodes and some nodal observations attached to them, we aim to infer their edge connectivity pattern. In the literature, this problem is termed graph learning or network topology inference (Mateos et al., 2019). 

Graph learning is a central problem in GSP, the subject that generalizes traditional SP to non-Euclidean domains (Shuman et al., 2013; Ortega et al., 2018). In analog to traditional SP, GSP uses eigenfunctions of various graph representations, such as adjacency and Laplacian matrices, to define a graph Fourier basis. These Fourier bases transform graph signals into the spectral domain, where frequency analysis and filtering can be applied. 

In this dissertation, we will dive into this intriguing field and discuss our recent efforts in generalizing the scope of graph learning. We will begin with Chapter 1 where we introduce some preliminaries and formally define the problem of graph learning from smooth signals. We focus on the combinatorial graph Laplacian and show why it is crucial for generalizing Fourier 

1 

Transform to non-Euclidean domains. This serves as the foundation of GSP and the necessity of graph learning naturally emerges when the underlying graph domain is unknown. Before we end this chapter, we present some prominent graph learning methods using the smoothness assumption. 

Although different graph learning methods exist, they are restricted to learning from either smooth graph signals or simple additive Gaussian noise. Other types of noisy data, such as discrete counts or binary digits, are rather common in real-world applications, yet are underexplored in graph inference. In Chapter 2, we propose a versatile graph inference framework for learning from graph signals corrupted by exponential family noise. Our framework generalizes previous methods from continuous smooth graph signals to various data types. We propose an alternating algorithm that jointly estimates the graph Laplacian and the unobserved smooth representation from the noisy signals. We also extend our approach to include an offset variable which models different levels of variation of the nodes. Since real-world graph signals are frequently non-independent and temporally correlated, we further adapt our original setting to a time-vertex formulation. We demonstrate on synthetic and real-world data that our new algorithms outperform competing Laplacian estimation methods that suffer from noise model mismatch. 

This is followed by our efforts in generalizing graph learning to multi-way signals, where product graphs emerge to model the factorized dependencies. Chapter 3 presents some theoretical and empirical results on Cartesian product graphs. The Cartesian graph product is a natural way for modeling higher-order conditional dependencies and is also the key for generalizing GSP to multi-way tensors. We establish statistical consistency for the penalized maximum likelihood estimation (MLE) of a Cartesian product Laplacian, and propose an efficient algorithm to solve the problem. We also extend our method for efficient joint graph learning and imputation in the presence of structural missing values. Experiments on synthetic and real-world datasets demonstrate that our method is superior to existing methods. 

Although Cartesian product proves to be useful for modeling multi-way dependencies, 

2 

the types of graph products that can be learned are still limited for modeling diverse dependency structures. Chapter 4 extends the scope further to Kronecker-structured graphs. Unlike Cartesian product, the Kronecker product models dependencies in a more intricate, non-separable way, but posits harder constraints on the graph learning problem. To tackle this non-convex problem, we propose an alternating scheme to optimize each factor graph in turn and provide theoretical guarantees for its asymptotic convergence. We also modify the proposed algorithm to learn factor graphs of the strong product, a denser graph product that covers the Kronecker product. We conduct experiments on synthetic and real-world graphs and demonstrate our approach’s efficacy and superior performance compared to existing methods. 

In Chapter 5, we present some verification of the geometric assumption in the deep learning world, using adversarial attacks. Deep neural networks are known to be vulnerable to adversarial examples, where a perturbation in the input space leads to an amplified shift in the latent network representation. We hypothesize that the clean data samples lie on a smooth manifold, and loosely show that an auxiliary loss induced by self-supervised representation learning can capture this underlying geometry. This leads to Self-supervised Online Adversarial Purification (SOAP), a novel defense strategy that uses a self-supervised loss to purify adversarial examples at test-time. Our approach leverages the label-independent nature of self-supervised signals, and counters the adversarial perturbation with respect to the self-supervised tasks. SOAP yields competitive robust accuracy against state-of-the-art adversarial training and purification methods, with considerably less training complexity. 

Finally, in Chapter 6, we discuss some delicacy and pitfalls of the presented works. Some promising future directions mark the end of this dissertation. 

We use the following notations throughout the paper. Lower-case and upper-case **bold** letters denote vectors and matrices respectively, and lower-case bold _italic_ letters denote random vectors. Let **1** and **0** denote the all 1 and all 0 vectors, and let **O** denote the all 0 matrix. Let **e** _[l] p[∈]_[R] _[p]_[denote a unit vector that has][ 1][ in its] _[ l]_[-th entry.][†][ denotes the Moore-Penrose pseudo-] inverse and det[†] denotes the pseudo-determinant. _◦_ denotes the Hadamard product. _⊗_ and _⊕_ 

3 

denote the Kronecker product and the Kronecker sum of two matrices, respectively. _×_ , □, and ⊠ are used to denote the Kronecker product, the Cartesian product, and the strong product of two graphs, respectively. With abuse of notation, _×_ also denotes the Cartesian product of two sets. For a node pair ( _v, u_ ), _∼_ denotes an edge connects them, and _̸∼_ denotes non-connection. For matrix norms, _∥·∥F_ denotes the Frobenius norm, _∥·∥_ 2 the operator norm, and _∥·∥_ 1 _,_ off the sum of the absolute values of all off-diagonal elements. For random variables, _∥·∥ψ_ 2 denotes the sub-Gaussian norm. ( _·_ )+ denotes the non-negative projection. [ _·_ ] _I,J_ denotes the sub-matrix of a _n × m_ matrix at a subset of indices ( _I, J_ ), where _I ⊆{_ 1 _,_ 2 _,..., n}_ and _J ⊆{_ 1 _,_ 2 _,..., m}_ . 

Finally, we introduce some graph product notations. Consider two factor graphs _G_ 1 = _{V_ 1 _, E_ 1 _,_ **W** 1 _}_ and _G_ 2 = _{V_ 2 _, E_ 2 _,_ **W** 2 _}_ , with cardinality _|V_ 1 _|_ = _p_ 1 and _|V_ 2 _|_ = _p_ 2. The Kronecker product of them is denoted as _G_ = _G_ 1 _× G_ 2, , and _|V |_ = _|V_ 1 _× V_ 2 _|_ = _p_ 1 _p_ 2. The weighted adjacency matrix of _G_ is the Kronecker product of the factor weights **W** 1 _⊗_ **W** 2, and similarly, the degree matrix of _G_ is **D** 1 _⊗_ **D** 2. This means that for a node pair ( _v_ 1 _, v_ 2) and ( _u_ 1 _, u_ 2) in the product graph _G_ , ( _v_ 1 _, v_ 2) _∼_ ( _u_ 1 _, u_ 2) holds iff _v_ 1 _∼ v_ 2 _∧ u_ 1 _∼ u_ 2. Another graph product that produces denser connectivity is the strong product. The weighted adjacency matrix of the strong product _G_ = _G_ 1 ⊠ _G_ 2 is **W** 1 _⊗_ **W** 2 + **W** 1 _⊕_ **W** 2. This shows that the edge set of the strong product graph _G_ 1 ⊠ _G_ 2 of _G_ 1 and _G_ 2 is the union of the Kronecker product _G_ 1 _⊗ G_ 2 and the Cartesian product _G_ 1□ _G_ 2 of them. 

4 

## **Chapter 1** 

## **Graphs and Signal Processing** 

## **1.1 Combinatorial Graph Laplacian** 

Consider an undirected, connected graph _G_ with _|V |_ = _p_ vertices and _|E |_ edges. A graph representation of _G_ is a matrix that fully determines the topology of _G_ . One of the most common graph representations is the weighted symmetric adjacency matrix **W** _∈_ S _[p]_ . Each entry of the weight matrix [ **W** ] _ij_ = [ **W** ] _ji ≥_ 0 encodes the weight of a node pair ( _i, j_ ), and [ **W** ] _i j_ = [ **W** ] _ji >_ 0 iff _eij ∈ E_ . We assume there are no self-loops, i.e. **W** _ii_ = 0. Another important graph representation is the combinatorial graph Laplacian matrix **L** . The Laplacian of the graph _G_ is defined as **L** = **D** _−_ **W** , where **D** denotes the diagonal degree matrix where [ **D** ] _ii_ = ∑ _j_ [ **W** ] _ij_ . The Laplacian is semi-positive definite (SPD), with at least one eigenvalue equal to 0. When the graph is connected, the 0-eigenvector is a constant function that has the same value on every node. This property is called intrinsic. 

The Laplacian matrix plays a vital role in spectral graph theory, graph machine learning, and many other scientific fields (Merris, 1994). It is the matrix form of the widely known discrete Laplace operator on a graph, and it also converges to the Laplace-Beltrami operator under certain conditions. In the context of GSP, the combinatorial graph Laplacian is important for inducing a notion of frequency on graphs. Consider the Laplacian eigendecomposition of a connected graph **L** = **U Λ U** _[T]_ and **u** _[T] l_ **[Lu]** _[l]_[=] _[ λ][l][,][∀][l][ ∈{]_[1] _[,]_[2] _[,...,][ p][}]_[.][Since] **[ L]**[ is SPD, we have][ 0][ =] _[ λ]_[1] _[ <][ λ]_[2] _[ ≤][λ]_[3] _[ ≤] ··· ≤ λp_ . The Laplacian quadratic term **u** _[T]_ **Lu** , also known as the Dirichlet energy, measures 

5 

the smoothness (variation) of **u** with respect to _G_ . This is perhaps not surprising since the Laplacian matrix resembles the discrete Laplace operator and **u** _[T]_ **Lu** = ∑ _i j_ [ **W** ] _i j_ ([ **u** ] _i −_ [ **u** ] _j_ )[2] . Nevertheless, it reveals that the lower eigenvectors of **L** vary smoothly on the graphs, and the higher eigenvectors of **L** fluctuate more fiercely. Their Laplacian quadratic, evaluated as the eigenvalues, serve as the frequency of these eigenvectors. Since these eigenvectors are naturally orthogonal, GSP uses them to define a form of Fourier transform on graphs. We will elaborate on this in the next section. 

Let **w** _∈_ R _[p]_[(] _[p][−]_[1][)] _[/]_[2] denote the vectorization of the graph weights, where [ **w** ] _i− j_ + 21[(] _[j][−]_[1][)(][2] _[p][−][j]_[)][ =] [ **W** ] _i j, ∀_ 1 _≤ j ≤ i ≤ p_ . Defining the linear maps from this non-negative weight vector to its corresponding weighted adjacency matrix and combinatorial graph Laplacian is helpful. We follow (Kumar et al., 2020) to define these operators. 

**Definition 1.1.1.** _Define A_ : R _[p]_[(] _[p][−]_[1][)] _[/]_[2] _→_ R _[p][×][p] ,_ **w** _�→ A_ **w** _as the following linear operator_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0020-03.png)


**Definition 1.1.2.** _Define L_ : R _[p]_[(] _[p][−]_[1][)] _[/]_[2] _→_ R _[p][×][p] ,_ **w** _�→ L_ **w** _as the following linear operator_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0020-05.png)


It is obvious that **W** = _A_ **w** . One can verify that _L_ **w** is a combinatorial graph Laplacian with weights **w** . We then define their adjoint operators. 

6 

**Definition 1.1.3.** _Define A[∗]_ : R _[p][×][p] →_ R _[p]_[(] _[p][−]_[1][)] _[/]_[2] _,_ **Q** _�→ A[∗]_ **Q** _as the following_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0021-01.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0021-02.png)


**Definition 1.1.4.** _Define L[∗]_ : R _[p][×][p] →_ R _[p]_[(] _[p][−]_[1][)] _[/]_[2] _,_ **Q** _�→ L[∗]_ **Q** _as the following_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0021-04.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0021-05.png)


## **1.2 Graph Signals and Fourier Transforms** 

A graph signal is a real-valued function _**x**_ : _V →_ R _[p]_ , which maps each vertex of the graph to a real value. The GFT[�] _**f**_ of _**x**_ is defined as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0021-08.png)


and the inverse GFT (IGFT) of � _**x**_ is defined as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0021-10.png)


Note that the GFT of _**f**_ is not necessarily unique because the Fourier basis, i.e. the eigendecomposition of **L** is not unique. The Fourier basis is also referred to as the spectral template. 

GFT represents a graph signal in the spectral domain and IGFT maps the spectral representation back to the vertex domain.[�] _**f**_ ( _λl_ ) corresponds to different frequency components of _**f**_ and GSP applies graph filters amplify or dampen these components. The graph spectral 

7 

filtering of a signal **x** 0 is 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0022-01.png)


where _{_ **u** _i, λi}, ∀_ 1 _≤ i ≤ p_ are the eigenvector-eigenvalue pairs of **L** . Similar to classical SP, one can design low-pass, high-pass, or band-pass filters by changing the value of _f_ ( _λl_ ). 

In reality, the low-pass characteristic is a commonly favored assumption. This reflects the phenomenon that many real-world graph signals are observed to be smooth on the graphs. The definition of a smooth signal varies across different contexts, but generally, a smooth graph signal **x** can be seen as the result of applying a low-pass graph filter _F_ ( **L** ) to a non-smooth signal **x** 0. When **x** 0 _∼ N_ ( **0** _,_ **I** _p_ ), the smooth signal follows the distribution 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0022-04.png)


This GSP formulation of applying a low-pass filter to white **x** 0, as well as different choices of the filter have been well-summarized by Kalofolias (2016). A particular choice is _F_ ( **L** ) = ~~_√_~~ **L**[†] . The smooth signals then follow an improper Gaussian distribution 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0022-06.png)


## **1.3 Graph Inference from Smooth Signals** 

The graph Laplacian plays a central role in defining the GFT. However, a prominent problem even before applying GSP is that the graph abstraction of the studied system is frequently unobserved. For example, in neuroscience, GSP has been successfully applied to fMRI data but the functional connectivity between brain regions is not always available Hu et al. (2015); Wang et al. (2020a); Gao et al. (2021). While ad-hoc graph construction rules (e.g. k-nearest neighbor graphs) exist in many fields, it is arguably more appealing to learn those graphs in a 

8 

more principled way. Thus GSP resorts to such a method for learning these graphs from the nodal observations (signals), called graph learning or graph inference. 

Consider a dataset **X** = [ **x** 1 _,_ **x** 2 _,...,_ **x** _n_ ] _∈_ R _[p][×][n]_ , where each row corresponds to a node and each column corresponds to an independent smooth graph signal **x** _j ∈_ R _[p]_ . The goal of graph inference is to learn such _G_ that the columns of **X** will be smooth on it. Laplacian-based graph learning methods solve the following optimization problem: 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0023-02.png)


where _L_ is the space of valid graph Laplacian matrices 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0023-04.png)


_h_ ( **L** ) is a regularization term, and _α_ is a trade-off parameter. (1.6) is consist of two terms. The first term is the graph Laplacian quadratic form, also known as the Dirichlet energy. It measures the overall smoothness of graph signals since Tr( **X** _[T]_ **LX** ) = ∑ _[n] k_ =1[∑][1] _[≤][i][<][j][≤][p]_ **[W]** _[i j]_[(] **[X]** _[ik][ −]_ **[X]** _[jk]_[)][2][.] Furthermore, consider the system in (1.3) and choose the low-pass filter _F_ ( **L** ) = _√_ **L**[†] . The smoothness term naturally arises in the density function of (1.5). These elucidate how (1.6) imposes the smoothness prior. The second regularization term serves two purposes. Firstly, it prevents trivial solutions such as fully disconnected graphs where **L** contains zero everywhere. Secondly, it imposes additional priors on the graph such as sparsity. 

In (1.6), the smoothness term can be formulated in various ways and the specific choice of regularization can also vary. This results in different objectives with different optimization methods. Here we briefly describe some popular graph learning methods and the specific forms of (1.6) they employ. Hu et al. (2015) and Dong et al. (2016) use the original smoothness term and choose the regularization term _h_ ( **L** ) to be the Frobenius norm of **L** . A trace equality constraint Tr ( **L** ) = _p_ is added to prevent trivial solutions. They formulate the problem as a 

9 

quadratic program with linear constraints and solve it through interior-point methods. Kalofolias (2016) reformulate the smoothness term as _∥_ **W** _◦_ **Z** _∥_ =[1] 2[Tr][(] **[X]** _[T]_ **[LX]**[)][, where] **[ Z]** _[ ∈]_ **[S]**[R] _[p][×][p]_[is the] squared Euclidean distance matrix across rows of **X** . They adapt the previous Frobenius norm regularization with a logarithmic barrier to promote connectivity and solve for **W** with primaldual optimization. Solving for **W** is equivalent to solving for **L** . Finally, Egilmez et al. (2017) propose the following objective 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0024-01.png)


where **S** is a data statistic and the design of **H** imposes different regularization on **L** . The authors propose to use block coordinate descent on the rows and columns of **L** for optimization. To reveal the connection between (1.6) and (1.8), let the data statistics be the commonly used sample covariance matrix **S** = **[XX][T]**[This makes the first term of][ (1.8)][ a scaled smoothness term since] _n_[.] _⟨_ **L** _,_ **S** _⟩_ =[1] _n_[Tr][(] **[LXX]** _[T]_[) =][1] _n_[Tr][(] **[X]** _[T]_ **[LX]**[)][.][The log-determinant regularization is also an interesting] choice because it emerges naturally from the MLE of (1.5). In fact, (1.8) is exactly a penalized MLE of the improper GMRF, whose precision matrix is the **L** . 

10 

## **Chapter 2 Graph Inference from Noisy Signals** 

In Chapter 1, we discussed how the combinatorial graph Laplacian helps define the Fourier transform and filters on the graphs and how it can be learned from smooth nodal observations. In this Chapter, we study a more realistic scenario of graph learning, which is when the observed signals are corrupted with noises. We start with the additive Gaussian noise model in Section 2.1, then extend it to the exponential family in Section 2.2. Section 2.3 further incorporates nodal offsets and temporal structures into the proposed generative model. We demonstrate our proposed methods in Section 2.4. 

## **2.1 Gaussian Noise Model** 

Consider a more realistic case where the observations **X** are noisy. Dong et al. Dong et al. (2016) model noisy observations as underlying smooth representations **y** corrupted by additive isotropic Gaussian noise _**ε**_ . Since smooth representations follow a Gaussian distribution, as shown in Eq. (1.3), the noisy observations also follow a Gaussian distribution 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0025-04.png)


11 

where _σε_ is the standard deviation of Gaussian noise _ε_ . Again let _F_ ( **L** ) = _√_ **L**[†] , the MAP estimation of unobserved smooth representation **y** from (2.1) amounts to 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0026-01.png)


where hyper-parameter _β_ reflects the variance of the noise _σε_[2][.][Based on][ (2.2)][, jointly learning] **L** and the unobserved smooth signal representations **Y** = [ **y** 1 _,_ **y** 2 _,...,_ **y** _n_ ] _∈_ R _[p][×][n]_ was proposed in Dong et al. (2016) as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0026-03.png)


where _h_ ( **L** ) is the same Frobenius norm and trace equality constraint Tr ( **L** ) = _p_ . To solve (2.3), their method switches between two steps where they fix one variable and solve for the other. The advantage of this optimization scheme is that each sub-problem objective is convex even though (2.3) is not. When **Y** is fixed ( **Y** -step), the problem coincides with the Laplacian learning from smooth signals as in (1.6). When **L** is fixed ( **L** -step), solving for **Y** 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0026-05.png)


enjoys a closed-form solution **Y** = ( **I** _p_ + _β_ **L** ) _[−]_[1] **X** that amounts to the Tikhonov filtering of **X** . 

## **2.2 Exponential Family Noise Models** 

In this section, we first present a versatile noise model that accounts for various data types with exponential family distributions. We then propose GLEN, an alternating algorithm that jointly infers the unknown graph and denoises the signals from the exponential family model. Two concrete examples of this generalized scenario, with Poisson and Binomial noise, conclude this section. Our method is demonstrated in Figure 2.1. 

12 

**Figure 2.1.** Graph Laplacian learning with Exponential Family Noise (GLEN). A. Diagram showing how GLEN jointly optimizes the unknown graph _G_ and the unknown latent smooth representation **Y** given observations **X** . GLEN alternates these two steps: (i) a graph learning step that infers _G_ from current **Y** estimation and (ii) a denoising step that smooths binary observations **X** using the current _G_ to obtain new **Y** . Each of the _M_ columns of **Y** (the red vertical waveform) is a smooth graph signal over _N_ nodes. B. Example of a Bernoulli graph signal **x** . A solid blue bar indicates a 1 and an empty bar indicates a 0. C. Example of a smooth graph signal **y** underlying the noisy Poisson observations. D. Example of temporally correlated smooth graph signals. 

## **2.2.1 Exponential Family Noise Model** 

We first propose a GSP-based framework to model the generative process of noisy signals of different data types, motivated by the Gaussian noise case. Specifically, the underlying smooth representation is generated from the same process as in (1.3), which is then connected to the 

**Table 2.1.** Exponential family distributions and link functions 

|Distribution|_θ_|_η_|_T_(**x**)|_A_(_η_)|g|
|---|---|---|---|---|---|
|Bernouli|_p_|log<br>_p_<br>1_−p_|x|log(1+_eη_)|logit|
|Binomial|_p_|log<br>_p_<br>1_−p_|x|_n_log(1+_eη_)|logit|
|Negative Binomial|_p_|log_p_|x|_−r_log(1_−eη_)|logit|
|Poisson|_λ_|log_λ_|x|_eη_|log|
|Gaussian|[_µ,σ_2]|[_µ/σ_2_,−_1_/_2_σ_2]|[_x,x_2]|_µ_2_/_2|identity|



13 

mean parameter of the exponential family distribution through a link function _g_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0028-01.png)


More precisely, we consider exponential family distributions of the following form 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0028-03.png)


specified by natural parameters _**η**_ , sufficient statistics _T_ ( **x** ), and the cumulant generating function _A_ ( _**η**_ ), which corresponds to the normalization factor of the probability distribution. We slightly abuse _T_ ( _·_ ) and _A_ ( _·_ ) to denote element-wise operations. Let the density function of _P_ ( _**η**_ ) be (2.6). Then the response model of noisy signals is given by 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0028-05.png)


In reminiscence of generalized linear models (GLMs), we link smooth signals to the mean parameters through the function _g_ so that (2.5) holds. We list common exponential family distributions in Table 2.1. 

When _p_ ( **x** _|_ **y** ) takes some specific exponential family distribution, _p_ ( **x** ) can find close relatives in the distribution zoo. Let **y** follow the same smooth signal distribution in (1.5). When the response is Poisson and the link function is logarithmic, _p_ ( **x** ) can be considered as an improper PLN distribution Aitchison and Ho (1989) with the precision matrix constrained to be a combinatorial graph Laplacian 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0028-08.png)


Similarly, one can obtain improper Bernoulli-Logit-Normal distributions or improper BinomialLogit-Normal distributions Aitchison and Shen (1980) from this framework, to name a few. The 

14 

Laplacian constraints distinguish these improper distributions from their counterparts in the PGM literature and permit a direct connection to GSP that has not been previously addressed. 

## **2.2.2 Graph Inference with Exponential Family Noise** 

We propose GLEN to learn the graph topology from the noisy observations as in (2.7). Following Dong et al. (2016), we consider the MAP estimate of the unobserved smooth representation **y** 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0029-03.png)


The full objective is then derived from the joint estimation of **Y** and **L** 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0029-05.png)


where _h_ ( **L** ) regularizes the graph and is up to the user’s choice. Here we slightly abuse the notation of _A_ to denote the element-wise computation. We also add a constraint for **y** which we explain below. The first two terms measure the fidelity of the inferred smooth representations **Y** with respect to noisy observation **X** . The last two terms are the same as (1.6), imposing smoothness and other structural priors on the inferred graph. When the distribution is isotropic Gaussian, (2.10) coincides with (2.3). If the regularization is chosen to be the same as (2.3), one can fully recover the method in Dong et al. (2016) for learning the graph from Gaussian observations (Sec. 2.1). 

GLEN alternates between an **L** -step and a **Y** -step to jointly learn these variables from (2.10), with a specific exponential family distribution as the noise model. At each step, we update the corresponding variables while the other variable is fixed. Similar to Dong et al. (2016), we obtain convexity in each sub-problem although the original problem is not jointly convex. Alg. 1 summarizes the full algorithm for general exponential family distributions. 

The **L** -step is akin to the smooth signal learning scenario with **Y** fixed. This is because 

15 

the choice of the exponential family distribution only affects the fidelity terms of (2.10). We simply replace the noisy **X** in (1.6) with the smooth signal representation **Y** to obtain the **L** -step 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0030-01.png)


Depending on the choice of regularization _h_ ( **L** ), previous methods Dong et al. (2016); Kalofolias (2016); Egilmez et al. (2017) can be readily plugged in. Here we propose a new regularization inspired by (1.8) 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0030-03.png)


Here _α_ 1 and _α_ 2 are non-negative trade-off parameters. Different from (1.8), the log-determinant term is also controlled by a trade-off parameter _α_ 1, which we found useful when dealing with exponential family noise. The resulting optimization problem is still convex and we use gradient descent to solve it. 

The **Y** -step denoises **X** using the current **L** estimation. When **L** is fixed, updating **Y** becomes the MAP in (2.9). However, the solution of (2.9) might not be meaningful: the fidelity might become dominant and the smoothness term might be simply ignored. Because the combinatorial graph Laplacian **L** is first-order intrinsic **L1** _N_ = **0** _N_ , the smoothness term cannot penalize large uniform signals when they are favored by the fidelity term. Thus, we solve a constrained optimization of **Y** 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0030-06.png)


The constraint prohibits **Y** to grow along the direction **1** , therefore striking for a balance between the fidelity and smoothness term. Since (2.13) does not enjoy a closed-form solution for general exponential family distributions, we resort to iterative methods. We apply the Newton-Raphson method with linear constraints to each smooth signal representation **y** _j_ . Let the gradient and 

16 

Hessian of the unconstrained problem be ∇ **y** _j_ and ∇[2] **y** _j_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0031-01.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0031-02.png)


We solve the following linear system 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0031-04.png)


and update **y** _j_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0031-06.png)


Here _ρ_ is the stepsize. Because (2.16) ensures that **1** _[T] p_[∆] **[y]** _[j]_[=][ 0][,] **[ 1]** _[T] p_ **[y]**[(] _j[t]_[)][=][ 0][ always hold so long as] **1** _[T] p_ **[y]**[(] _j_[1][)] = 0. Note that we use a Cholesky solver to solve the linear equation, avoiding explicit matrix inversion. The Cholesky solver has a similar _O_ ( _p_[3] ) complexity but is numerically more stable. For the sake of efficiency, we perform only one Newton-Raphson step for each **y** _j_ during a **Y** -step. This reduces computation, especially when **L** is poorly learned in the first few alternating steps. 

## **2.2.3 Noise Model Examples** 

Here we present the derivation of the solution for two specific examples with Poisson and Binomial distributions. 

## **Derivation of Poisson Observations** 

First, we derive the objective functions and update rules for the Poisson distribution. Given Poisson distribution as shown in Table 2.1 and the generalized objective in Eq. (2.10), we 

17 

## **Algorithm 1.** GLEN 

**Input:** noisy signals **X** = [ **x** 1 _,_ **x** 2 _,...,_ **x** _n_ ], exponential family distribution _P_ , trade-off parameters _α_ 1, _α_ 2, and _γ_ , stepsize _ρ_ and _λ_ **Onput:** graph Laplacian **L** , smooth signal representation **Y** = [ **y** 1 _,_ **y** 2 _,...,_ **y** _n_ ] Initialize **Y** and **L** , or **Y** , **L** , and _**µ**_ if using the offset **repeat** Solve **L** in (2.11) using gradient descent **for** _j_ = 1 _,_ 2 _,..., n_ **do** Calculate ∇ and ∇[2][in][(2.14)][and][(2.15)][,][(or][(2.33)][and][(2.34)][when][using][time-] **y** _j_ **y** _j_[as] vertex signals) Solve ∆ **y** _j_ from (2.16) and update **y** _j_ as in (2.17) **end for** Update _**µ**_ as in (2.27) if using the offset Calculate the loss using (2.10) **until** convergence. 

obtain the graph learning objective with Poisson noise: 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0032-03.png)


We abuse exp( _·_ ) to denote element-wise exponential operation. The gradient and Hessian for the unconstrained Newton–Raphson are then given by 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0032-05.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0032-06.png)


The update ∆ **y** _j_ is then obtained from Eq. (2.16). 

18 

## **Derivation of Binomial Observation** 

The second example uses the Binomial distribution. Given the Binomial distribution as shown in Table 2.1 with parameter _n_ = _R_ , we have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0033-02.png)


The Newton–Raphson for solving **Y** are derived similarly 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0033-04.png)


Again, the division is element-wise for the sake of simplicity. If we set _R_ = 1, then the Bernoulli noise model is obtained. 

## **2.3 Graph Inference Extensions** 

We present two extensions of GLEN. First, we add a constant offset _**µ**_ to the unobserved smooth signals **Y** . Next, we present an adaptation to the time-vertex formulation Grassi et al. (2017) where the data admits a joint graph-temporal structure, i.e. at every time point we observe a graph signal, and at each node of the graph we observe a time-series. 

## **2.3.1 Graph Inference with Offsets** 

In (2.7), we assume the underlying smooth representation always has zero offset (mean). However, such an assumption is not always favorable for real-world data. For example, when the noise model is Poisson, a non-zero offset is often useful for modeling different levels of exposure to an event. This motivates GLEN to model the offset explicitly when necessary. 

For the Gaussian noise model, the offset variable is redundant since graph inference 

19 

methods can work on the residuals of the observations **X** _−_[1][For general exponential] _p_ **[X1]** _[p]_ **[1]** _[T] p_[.] family noise, however, the offset contributes to the responses non-linearly, and accounting for its effects in GLEN is non-trivial. To resolve this issue, we add an offset term _**µ**_ to (2.10) which is jointly inferred with **Y** and **L** 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0034-01.png)


and the **Y** -step needs to be slightly modified 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0034-03.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0034-04.png)


The **Y** constraints here also prevent infinite solutions. Now we need to infer the offset variable _**µ**_ . Similar to the **Y** -step, we use unconstrained Newton-Raphson for the _**µ**_ -step 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0034-06.png)


where _λ_ is the stepsize and 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0034-08.png)


The extended GLEN cycles through these three steps to learn the Laplacian. 

## **2.3.2 Graph Inference from Time Series** 

In many real-world applications, graph signals, i.e., the columns of the input matrix **X** , are not always independent. A common case is that the graph signals have a natural temporal 

20 

order. In such a scenario, each row of the matrix, corresponding to a graph node, is a canonical 1-D time series, and **X** can be seen as a multivariate time-varying signal lying on the graph. For example, in neural data analysis, the input is often a count matrix whose rows correspond to neurons and columns correspond to time bins. While a graph on the rows models the functional connectivity of neurons, the columns should also vary smoothly across time. Such an assumption of temporal correlation merges classical signal processing with GSP and proves useful in many scenarios (e.g., neuroscience, sensor networks). 

The Time-Vertex signal processing framework Grassi et al. (2017); Liu et al. (2019) is specifically designed for this setting. For a time-varying graph signal **X** _∈_ R _[p][×][n]_ , the time-vertex GSP is defined on the Cartesian product of a graph _G_ that underlies the _p_ rows and a temporal graph _T_ that underlies the _n_ columns. The Laplacian quadratic form of a matrix signal **X** on the product graph _J_ is the summation of the quadratic forms along each dimension 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0035-02.png)


where vec( **X** ) is the column-wise vectorization of **X** , and **L** _J_ , **L** _G_ , **L** _T_ denote the Laplacians of _J_ , _G_ , _T_ , respectively. A smooth time-vertex signal is smooth on both factor graphs as measured in (2.30). The joint time-vertex Fourier transform (JFT) is simply applying the graph Fourier transform (GFT) on the _G_ dimension and the discrete Fourier transform (DFT) on the _T_ dimension. 

Here we assume the underlying representation of the input matrix is smooth on the time-vertex graph _J_ . As the temporal graph _T_ is known a priori (typically modeled as a path graph), we still need to learn **Y** and **L** _G_ . The optimization problem becomes the following: 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0035-05.png)


21 

where _γ_ controls the temporal smoothing effects of _T_ . A similar alternating optimization algorithm can be applied for (2.31). Since _T_ is already fixed, solving (2.31) only differs from (2.10) in the **Y** -step 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0036-01.png)


which uses both **L** _G_ and **L** _T_ for denoising. To use the Newton-Raphson method, we have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0036-03.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0036-04.png)


and solve Eq. (2.16) for the constrained updates. We term this method **GLEN** with **T** ime- **V** ertex (GLEN-TV). 

## **2.4 Experiments** 

In this section, we demonstrate GLEN and its extensions on synthetic graphs as well as multiple real-world datasets. All experiments are conducted with MATLAB. 

## **2.4.1 Synthetic Graphs** 

Synthetic experiments are important for evaluating graph learning methods because ground truth graphs are not frequently unavailable for real datasets. We simulate the generation of smooth graph signals using known graphs and evaluate the inferred graphs against them. ˝ ´ We consider three random graph models: 1) Erdos-Renyi model with parameter _p_ = 0 _._ 3; 2) Stochastic block model with two equal-sized blocks, intra-community parameter _p_ = 0 _._ 4 and inter-community parameter _q_ = 0 _._ 1; and 3) Watts-Strogatz small-world model, where we create an initial ring lattice with node degree 2 _K_ = 4 and rewire every edge with probability _p_ = 0 _._ 1. 

22 

**Table 2.2.** Numerical comparison of graph learning with Poisson noise (N=20). 

|Structure prediction|Structure prediction||
|---|---|---|
|Method|RE**L**_↓_<br>RE_edge ↓_|RE_deg ↓_|
|Erd˝os-R´enyi Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._226_±_0_._024 0_._434_±_0_._027|0_._154_±_0_._038|
|GLS-1 (Dong et al., 2016)|0_._218_±_0_._024 0_._427_±_0_._038|0_._146_±_0_._032|
|GLS-2 (Kalofolias, 2016)|0_._246_±_0_._032 0_._453_±_0_._045|0_._179_±_0_._040|
|CGL (Egilmez et al., 2017)|0_._202_±_0_._027 0_._380_±_0_._031|0_._142_±_0_._037|
|GLEN|**0**_._**129**_±_**0**_._**015 0**_._**279**_±_**0**_._**039 **|**0**_._**068**_±_**0**_._**017**|
|Stochastic Block Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._216_±_0_._022 0_._403_±_0_._036|0_._141_±_0_._027|
|GLS-1 (Dong et al., 2016)|0_._217_±_0_._024 0_._409_±_0_._039|0_._140_±_0_._028|
|GLS-2 (Kalofolias, 2016)|0_._243_±_0_._026 0_._432_±_0_._040|0_._173_±_0_._029|
|CGL (Egilmez et al., 2017)|0_._207_±_0_._022 0_._370_±_0_._027|0_._146_±_0_._029|
|GLEN|**0**_._**116**_±_**0**_._**015 0**_._**234**_±_**0**_._**044 **|**0**_._**063**_±_**0**_._**013**|
|Watts-Strogatz Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._120_±_0_._013 0_._214_±_0_._023|0_._072_±_0_._014|
|GLS-1 (Dong et al., 2016)|0_._176_±_0_._017 0_._318_±_0_._031|0_._101_±_0_._019|
|GLS-2 (Kalofolias, 2016)|0_._208_±_0_._018 0_._357_±_0_._030|0_._137_±_0_._020|
|CGL (Egilmez et al., 2017)|0_._184_±_0_._016 0_._306_±_0_._023|0_._129_±_0_._019|
|GLEN|**0**_._**100**_±_**0**_._**012 0**_._**172**_±_**0**_._**019 **|**0**_._**065**_±_**0**_._**013**|



## Weights prediction 

|Method|PR-AUC_↑_<br>F-score_↑_|NMI_↑_|DeltaCon_↑_|
|---|---|---|---|
||Erd˝os-R´enyi Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._914_±_0_._019 0_._870_±_0_._030|0_._574_±_0_._069|0_._907_±_0_._015|
|GLS-1 (Dong et al., 2016)|0_._845_±_0_._031 0_._807_±_0_._035|0_._460_±_0_._071|0_._871_±_0_._018|
|GLS-2 (Kalofolias, 2016)|0_._882_±_0_._025 0_._839_±_0_._031|0_._506_±_0_._073|0_._891_±_0_._015|
|CGL (Egilmez et al., 2017)|0_._909_±_0_._020 0_._861_±_0_._031|0_._548_±_0_._073|0_._900_±_0_._016|
|GLEN|**0**_._**926**_±_**0**_._**018 0**_._**890**_±_**0**_._**030 **|**0**_._**612**_±_**0**_._**084 **|**0**_._**918**_±_**0**_._**015**|
||Stochastic Block Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._930_±_0_._015 0_._897_±_0_._027|0_._643_±_0_._074|0_._911_±_0_._016|
|GLS-1 (Dong et al., 2016)|0_._841_±_0_._033 0_._817_±_0_._032|0_._493_±_0_._071|0_._870_±_0_._017|
|GLS-2 (Kalofolias, 2016)|0_._882_±_0_._031 0_._856_±_0_._053|0_._569_±_0_._079|0_._891_±_0_._018|
|CGL (Egilmez et al., 2017)|0_._924_±_0_._018 0_._889_±_0_._028|0_._633_±_0_._070|0_._909_±_0_._018|
|GLEN|**0**_._**941**_±_**0**_._**014 0**_._**920**_±_**0**_._**025 **|**0**_._**701**_±_**0**_._**071 **|**0**_._**925**_±_**0**_._**015**|
||Watts-Strogatz Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._938_±_0_._020 0_._930_±_0_._026|0_._747_±_0_._061|0_._933_±_0_._025|
|GLS-1 (Dong et al., 2016)|0_._878_±_0_._035 0_._880_±_0_._037|0_._638_±_0_._072|0_._896_±_0_._019|
|GLS-2 (Kalofolias, 2016)|0_._900_±_0_._034 0_._895_±_0_._033|0_._665_±_0_._066|0_._896_±_0_._019|
|CGL (Egilmez et al., 2017)|0_._950_±_0_._015 0_._941_±_0_._024|0_._769_±_0_._063|0_._806_±_0_._015|
|GLEN|**0**_._**960**_±_**0**_._**011 0**_._**960**_±_**0**_._**019 **|**0**_._**813**_±_**0**_._**055 **|**0**_._**941**_±_**0**_._**015**|



23 

**Table 2.3.** Numerical comparison of graph learning with Binomial noises (N=20). 

Structure prediction 

|Method|RE**L**_↓_<br>RE_edge ↓_|RE_deg ↓_|
|---|---|---|
|Erd˝os-R´enyi Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._161_±_0_._020 0_._342_±_0_._054|0_._089_±_0_._022|
|GLS-1 (Dong et al., 2016)|0_._202_±_0_._027 0_._395_±_0_._035|0_._133_±_0_._029|
|GLS-2 (Kalofolias, 2016)|0_._277_±_0_._030 0_._449_±_0_._035|0_._228_±_0_._030|
|CGL (Egilmez et al., 2017)|0_._220_±_0_._028 0_._338_±_0_._036|0_._188_±_0_._030|
|GLEN|**0**_._**112**_±_**0**_._**012 0**_._**234**_±_**0**_._**033 **|**0**_._**064**_±_**0**_._**014**|
|Stochastic Block Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._171_±_0_._027 0_._301_±_0_._038|0_._121_±_0_._033|
|GLS-1 (Dong et al., 2016)|0_._236_±_0_._037 0_._412_±_0_._048|0_._170_±_0_._041|
|GLS-2 (Kalofolias, 2016)|0_._302_±_0_._040 0_._460_±_0_._047|0_._251_±_0_._042|
|CGL (Egilmez et al., 2017)|0_._229_±_0_._031 0_._330_±_0_._038|0_._198_±_0_._032|
|GLEN|**0**_._**112**_±_**0**_._**019 0**_._**207**_±_**0**_._**036 **|**0**_._**074**_±_**0**_._**018**|
|Watts-Strogatz Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._149_±_0_._018 0_._229_±_0_._024|0_._115_±_0_._019|
|GLS-1 (Dong et al., 2016)|0_._213_±_0_._023 0_._347_±_0_._033|0_._152_±_0_._026|
|GLS-2 (Kalofolias, 2016)|0_._241_±_0_._028 0_._372_±_0_._035|0_._186_±_0_._030|
|CGL (Egilmez et al., 2017)|0_._187_±_0_._022 0_._284_±_0_._021|0_._145_±_0_._028|
|GLEN|**0**_._**098**_±_**0**_._**012 0**_._**161**_±_**0**_._**018 **|**0**_._**069**_±_**0**_._**013**|



## Weights prediction 

|Method|PR-AUC_↑_<br>F-score_↑_|NMI_↑_|DeltaCon_↑_|
|---|---|---|---|
||Erd˝os-R´enyi Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._904_±_0_._017 0_._868_±_0_._029|0_._575_±_0_._077|0_._893_±_0_._025|
|GLS-1 (Dong et al., 2016)|0_._868_±_0_._024 0_._840_±_0_._027|0_._511_±_0_._064|0_._887_±_0_._019|
|GLS-2 (Kalofolias, 2016)|0_._891_±_0_._018 0_._842_±_0_._024|0_._513_±_0_._056|0_._893_±_0_._014|
|CGL (Egilmez et al., 2017)|0_._914_±_0_._014 0_._877_±_0_._025|0_._593_±_0_._067|0_._909_±_0_._014|
|GLEN|**0**_._**112**_±_**0**_._**012 0**_._**901**_±_**0**_._**027 **|**0**_._**641**_±_**0**_._**083 **|**0**_._**921**_±_**0**_._**015**|
||Stochastic Block Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._920_±_0_._021 0_._895_±_0_._028|0_._651_±_0_._071|0_._906_±_0_._019|
|GLS-1 (Dong et al., 2016)|0_._859_±_0_._036 0_._848_±_0_._037|0_._556_±_0_._077|0_._882_±_0_._021|
|GLS-2 (Kalofolias, 2016)|0_._884_±_0_._030 0_._846_±_0_._033|0_._546_±_0_._068|0_._884_±_0_._019|
|CGL (Egilmez et al., 2017)|0_._923_±_0_._019 0_._896_±_0_._026|0_._651_±_0_._062|0_._911_±_0_._017|
|GLEN|**0**_._**112**_±_**0**_._**019 0**_._**929**_±_**0**_._**025 **|**0**_._**726**_±_**0**_._**067 **|**0**_._**929**_±_**0**_._**016**|
||Watts-Strogatz Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._951_±_0_._019 0_._945_±_0_._028|0_._779_±_0_._072|0_._928_±_0_._023|
|GLS-1 (Dong et al., 2016)|0_._884_±_0_._034 0_._895_±_0_._034|0_._667_±_0_._070|0_._895_±_0_._021|
|GLS-2 (Kalofolias, 2016)|0_._919_±_0_._028 0_._902_±_0_._032|0_._673_±_0_._071|0_._898_±_0_._020|
|CGL (Egilmez et al., 2017)|0_._955_±_0_._014 0_._946_±_0_._024|0_._782_±_0_._062|0_._928_±_0_._018|
|GLEN|**0**_._**964**_±_**0**_._**009 0**_._**964**_±_**0**_._**022 **|**0**_._**827**_±_**0**_._**069 **|**0**_._**943**_±_**0**_._**018**|



24 

**Table 2.4.** Numerical comparison of graph learning with Poisson noise (N=50). 

Structure prediction 

|Method|RE**L**_↓_<br>RE_edge ↓_|RE_deg ↓_|
|---|---|---|
|Erd˝os-R´enyi Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._263_±_0_._025 0_._774_±_0_._062|0_._161_±_0_._026|
|GLS-1 (Dong et al., 2016)|0_._192_±_0_._010 0_._614_±_0_._019|0_._095_±_0_._016|
|GLS-2 (Kalofolias, 2016)|0_._199_±_0_._009 0_._612_±_0_._022|0_._111_±_0_._013|
|CGL (Egilmez et al., 2017)|0_._206_±_0_._008 0_._613_±_0_._021|0_._122_±_0_._013|
|GLEN|**0**_._**177**_±_**0**_._**006 0**_._**610**_±_**0**_._**030 **|**0**_._**060**_±_**0**_._**008**|
|Stochastic Block Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._789_±_0_._021 0_._713_±_0_._022|0_._324_±_0_._038|
|GLS-1 (Dong et al., 2016)|0_._796_±_0_._020 0_._717_±_0_._021|0_._327_±_0_._033|
|GLS-2 (Kalofolias, 2016)|0_._801_±_0_._018 0_._726_±_0_._020|0_._342_±_0_._033|
|CGL (Egilmez et al., 2017)|0_._800_±_0_._020 0_._718_±_0_._021|0_._331_±_0_._038|
|GLEN|**0**_._**169**_±_**0**_._**007 0**_._**523**_±_**0**_._**028 **|**0**_._**066**_±_**0**_._**010**|
|Watts-Strogatz Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._147_±_0_._014 0_._249_±_0_._021|0_._099_±_0_._014|
|GLS-1 (Dong et al., 2016)|0_._192_±_0_._015 0_._337_±_0_._024|0_._120_±_0_._016|
|GLS-2 (Kalofolias, 2016)|0_._220_±_0_._017 0_._367_±_0_._025|0_._152_±_0_._018|
|CGL (Egilmez et al., 2017)|0_._196_±_0_._016 0_._319_±_0_._020|0_._140_±_0_._019|
|GLEN|**0**_._**110**_±_**0**_._**014 0**_._**180**_±_**0**_._**021 **|**0**_._**078**_±_**0**_._**014**|



## Weights prediction 

|Method|PR-AUC_↑_<br>F-score_↑_|NMI_↑_|DeltaCon_↑_|
|---|---|---|---|
||Erd˝os-R´enyi Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._741_±_0_._017 0_._672_±_0_._017|0_._228_±_0_._029|0_._776_±_0_._009|
|GLS-1 (Dong et al., 2016)|0_._754_±_0_._015 0_._678_±_0_._017|0_._230_±_0_._030|0_._782_±_0_._011|
|GLS-2 (Kalofolias, 2016)|0_._760_±_0_._015 0_._683_±_0_._016|0_._236_±_0_._031|0_._791_±_0_._009|
|CGL (Egilmez et al., 2017)|0_._754_±_0_._016 0_._678_±_0_._018|0_._230_±_0_._031|0_._791_±_0_._008|
|GLEN|**0**_._**767**_±_**0**_._**015 0**_._**690**_±_**0**_._**017 **|**0**_._**248**_±_**0**_._**031 **|**0**_._**800**_±_**0**_._**007**|
||Stochastic Block Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._789_±_0_._021 0_._713_±_0_._022|0_._324_±_0_._038|0_._796_±_0_._011|
|GLS-1 (Dong et al., 2016)|0_._796_±_0_._020 0_._717_±_0_._021|0_._327_±_0_._033|0_._798_±_0_._011|
|GLS-2 (Kalofolias, 2016)|0_._801_±_0_._018 0_._726_±_0_._020|0_._342_±_0_._033|0_._808_±_0_._009|
|CGL (Egilmez et al., 2017)|0_._800_±_0_._020 0_._718_±_0_._021|0_._331_±_0_._038|0_._806_±_0_._010|
|GLEN|**0**_._**811**_±_**0**_._**019 0**_._**734**_±_**0**_._**021 **|**0**_._**352**_±_**0**_._**037 **|**0**_._**815**_±_**0**_._**009**|
||Watts-Strogatz Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._963_±_0_._010 0_._935_±_0_._016|0_._813_±_0_._032|0_._908_±_0_._014|
|GLS-1 (Dong et al., 2016)|0_._856_±_0_._028 0_._853_±_0_._024|0_._664_±_0_._040|0_._866_±_0_._015|
|GLS-2 (Kalofolias, 2016)|0_._886_±_0_._023 0_._874_±_0_._020|0_._697_±_0_._036|0_._866_±_0_._014|
|CGL (Egilmez et al., 2017)|0_._965_±_0_._009 0_._935_±_0_._015|0_._814_±_0_._032|0_._904_±_0_._016|
|GLEN|**0**_._**975**_±_**0**_._**008 0**_._**967**_±_**0**_._**013 **|**0**_._**884**_±_**0**_._**032 **|**0**_._**922**_±_**0**_._**012**|



25 

**Table 2.5.** Numerical comparison of graph learning with Binomial noises (N=50). 

Structure prediction 

|Method|RE**L**_↓_<br>RE_edge ↓_|RE_deg ↓_|
|---|---|---|
|Erd˝os-R´enyi Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._193_±_0_._010 0_._647_±_0_._041|0_._079_±_0_._009|
|GLS-1 (Dong et al., 2016)|0_._168_±_0_._005 0_._547_±_0_._024|0_._077_±_0_._008|
|GLS-2 (Kalofolias, 2016)|0_._212_±_0_._010 0_._560_±_0_._021|0_._152_±_0_._015|
|CGL (Egilmez et al., 2017)|0_._229_±_0_._016 0_._558_±_0_._024|0_._177_±_0_._020|
|GLEN|**0**_._**159**_±_**0**_._**005 0**_._**540**_±_**0**_._**026 **|**0**_._**061**_±_**0**_._**006**|
|Stochastic Block Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._165_±_0_._007 0_._514_±_0_._032|0_._064_±_0_._008|
|GLS-1 (Dong et al., 2016)|0_._165_±_0_._007 0_._484_±_0_._022|0_._083_±_0_._011|
|GLS-2 (Kalofolias, 2016)|0_._215_±_0_._013 0_._507_±_0_._023|0_._160_±_0_._016|
|CGL (Egilmez et al., 2017)|0_._224_±_0_._013 0_._503_±_0_._020|0_._174_±_0_._016|
|GLEN|**0**_._**150**_±_**0**_._**006 0**_._**465**_±_**0**_._**026 **|**0**_._**059**_±_**0**_._**009**|
|Watts-Strogatz Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._193_±_0_._015 0_._290_±_0_._020|0_._153_±_0_._015|
|GLS-1 (Dong et al., 2016)|0_._228_±_0_._016 0_._350_±_0_._019|0_._177_±_0_._020|
|GLS-2 (Kalofolias, 2016)|0_._252_±_0_._020 0_._380_±_0_._025|0_._200_±_0_._022|
|CGL (Egilmez et al., 2017)|0_._219_±_0_._013 0_._351_±_0_._018|0_._161_±_0_._017|
|GLEN|**0**_._**116**_±_**0**_._**015 0**_._**177**_±_**0**_._**016 **|**0**_._**092**_±_**0**_._**017**|



## Weights prediction 

|Method|PR-AUC_↑_<br>F-score_↑_|NMI_↑_|DeltaCon_↑_|
|---|---|---|---|
||Erd˝os-R´enyi Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._803_±_0_._015 0_._719_±_0_._017|0_._291_±_0_._034|0_._804_±_0_._007|
|GLS-1 (Dong et al., 2016)|0_._799_±_0_._014 0_._718_±_0_._017|0_._289_±_0_._031|0_._807_±_0_._010|
|GLS-2 (Kalofolias, 2016)|0_._800_±_0_._016 0_._716_±_0_._017|0_._289_±_0_._031|0_._807_±_0_._007|
|CGL (Egilmez et al., 2017)|0_._795_±_0_._017 0_._709_±_0_._017|0_._282_±_0_._034|0_._803_±_0_._007|
|GLEN|**0**_._**804**_±_**0**_._**016 0**_._**720**_±_**0**_._**016 **|**0**_._**294**_±_**0**_._**032 **|**0**_._**811**_±_**0**_._**008**|
||Stochastic Block Model|||
|SCGL (Lake and Tenenbaum, 2010)|**0**_._**846**_±_**0**_._**016** 0_._764_±_0_._021|0_._402_±_0_._035|0_._821_±_0_._008|
|GLS-1 (Dong et al., 2016)|0_._833_±_0_._016 0_._760_±_0_._019|0_._398_±_0_._032|0_._819_±_0_._008|
|GLS-2 (Kalofolias, 2016)|0_._839_±_0_._015 0_._760_±_0_._017|0_._398_±_0_._034|0_._817_±_0_._007|
|CGL (Egilmez et al., 2017)|0_._831_±_0_._017 0_._749_±_0_._019|0_._381_±_0_._039|0_._815_±_0_._009|
|GLEN|0_._843_±_0_._016 **0**_._**765**_±_**0**_._**020 **|**0**_._**405**_±_**0**_._**038 **|**0**_._**826**_±_**0**_._**008**|
||Watts-Strogatz Model|||
|SCGL (Lake and Tenenbaum, 2010)|0_._969_±_0_._009 0_._943_±_0_._015|0_._829_±_0_._034|0_._905_±_0_._014|
|GLS-1 (Dong et al., 2016)|0_._878_±_0_._025 0_._876_±_0_._023|0_._699_±_0_._041|0_._861_±_0_._015|
|GLS-2 (Kalofolias, 2016)|0_._901_±_0_._023 0_._885_±_0_._021|0_._715_±_0_._037|0_._864_±_0_._016|
|CGL (Egilmez et al., 2017)|0_._967_±_0_._009 0_._937_±_0_._016|0_._817_±_0_._034|0_._902_±_0_._015|
|GLEN|**0**_._**976**_±_**0**_._**006 0**_._**959**_±_**0**_._**013 **|**0**_._**865**_±_**0**_._**032 **|**0**_._**925**_±_**0**_._**017**|



26 

Using each model, we generate 50 random graphs of _p_ = 20 or _p_ = 50 nodes, respectively. The edge weights in **W** of each graph are randomly sampled from a uniform distribution _U_ (0 _._ 1 _,_ 2), and the unnormalized Laplacian is computed as **L** _u_ = **D** _−_ **W** . We then normalize it as **L** 0 = _p_ Tr **L** ( **L** _u u_ )[to obtain the ground-truth Laplacian.][The signals of various data types are then] generated from the process in (2.7). We use the Poisson distribution and the Binomial distribution to demonstrate the efficacy of GLEN. We simulate _n_ = 2000 unbounded and bounded count signals respectively from each distribution and infer the synthetic graphs from these generated signals. The parameter of the Binomial distribution is set to _K_ = 8. We use the GSPBOX Perraudin et al. (2014) and the SWGT toolbox Hammond et al. (2011) for graph generation and signal processing. 

We compare GLEN with leading graph Laplacian learning methods: shifted combinatorial graph Laplacian learning (SCGL) Lake and Tenenbaum (2010), two methods for graph learning from smooth signals: GLS-1 Dong et al. (2016) and GLS-2 Kalofolias (2016), and combinatorial graph Laplacian learning (CGL) Egilmez et al. (2017). Because existing methods are designed for Gaussian distributions, we pre-process the non-Gaussian input signals to accommodate the model mismatch. For the Poisson noise model, we first log-transform and then centralize the count 1 signals: log( **x** + **1** _p_ ). For the Binomial noise model, we apply logit( _K_ **[x]**[+] +[1] 2[)][ where][ logit][(] _[·]_[) =][ log] 1 _−·_[.] These pre-processing strategies are also used to initialize the smooth representation **Y** in GLEN. For all the CGL experiments, we use **H** = 2 **I** _p −_ **1** _p_ **1** _[T] p_[to regularize] **[ L]**[, corresponding to type-1] regularization in Egilmez et al. (2017). For GLEN, we use type-2 regularization **H** = **I** _p −_ **1** _p_ **1** _[T] p_[.] 

We quantitatively compare our proposed methods with the baselines in terms of structure prediction and weight prediction. For structure prediction, we report the area under the precisionrecall curve (PR-AUC), F-score, normalized mutual information (NMI) Dong et al. (2016), and DeltaCon Koutra et al. (2013). These metrics evaluate the binary pattern of predicted edges given by the inferred Laplacian **L** _[∗]_ , but ignore the graph weights. We obtain the precision-recall curve from a series of thresholds and calculate the F-score, NMI, and DeltaCon using the best threshold on the curve (in terms of F-score). For weight prediction, we report the relative error (RE) of 

27 

estimated Laplacians, edges, and degrees against the ground truth, which reflects both structure and weight prediction. Following Egilmez et al. (2017), we first normalize the inferred Laplacian **L** _[∗]_ **L** _[∗]_ to obtain **L**[�] = _p_ Tr ( **L** _[∗]_ )[.][The relative error of Laplacian, is then computed as][ RE] **[L]**[ =] _[∥]_ **[L]**[�] _∥[−]_ **L** 0 **[L]** _∥_[0] _F[∥][F]_[.] For the relative error of edges, we vectorize the upper triangle of **W** to obtain vech( **L** ) _∈_ R _[p]_[(] _[p][−]_[1][)] _[/]_[2] , and compute the relative _ℓ_ 2 norm RE _edge_ = _[∥]_[vech] _∥_[(] vech **[L]**[�][)] _[−]_ ([vech] **L** 0) _∥_[(] 2 **[L]**[0][)] _[∥]_[2] . For the relative error of degrees, we compute the relative _ℓ_ 2 norm of the degrees RE _deg_ = _[∥]_[dia][g] _∥_[(] diag **[L]**[�][)] _[−]_ ([dia] **L** 0[g] ) _∥_[(] **[L]** 2[0][)] _[∥]_[2] , where diag( **L** ) is the vector of diagonal elements of the Laplacian. 

Trade-off parameters are important for graph learning methods to pose favorable regularization. For the selection of these hyperparameters, we perform a grid search in the parameter space of each method. We use the trade-off parameters that achieve the lowest average RE **L** across 50 random graphs and report the evaluating metrics of the inferred graphs under these settings. We report the average values and the standard deviations for comparison. 

Table 2.2 and 2.3 show the quantitative results of each method for the Poisson and Binomial noise models when _p_ = 20. Similarly, results of _p_ = 50 are shown in Table 2.4 and 2.5. We bold the **best** performance. As we can see, GLEN outperforms the baselines on all metrics for both Poisson and Binomial noise models. In particular, GLEN is substantially better than the baselines on the weight prediction metrics. This demonstrates that specifying the correct noise model is crucial for learning accurate graph geometries. The standard deviations of GLEN’s results are also smaller than the baselines in most scenarios, showing that GLEN is more stable and robust to varying graph generators. Figure 2.2 compares the inferred graphs of different methods (SCGL, GLS-1, GLS-2, CGL and GLEN) to the target ground truth graphs for the random graph models. 

## **2.4.2 Chicago Crime Dataset** 

Now we evaluate GLEN on a real dataset, the Chicago Crime Dataset Sensors (2017). Our goal is to learn a graph between different types of crime to reveal their patterns of concurrence. The dataset contains 32 types of crimes that occurred in 77 Chicago communities during every 

28 

29 

hour from 2001 to 2017. We first bin the data by year over the last 10 years and sum the counts within each bin, which leads to 770 graph signals over 32 crime types. We further remove “Ritualism” from the crime list since there is no record in the 10 years. This results in a 31 _×_ 770 count matrix, and we apply the graph learning methods to it. 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0044-01.png)


**----- Start of picture text -----**<br>
(a) Mean occurrences of the crimes<br>zz ¢ 3 8<br>Dp €x y 3<br>2 % 2 &<br>&% Azge &¢ « XN %~ee %%@% %9% aaa & &§<br>GSjboa. SSSA Aaah?3882 \S 3iS*oe? OyLo,ReyOne%,YmSyBe,F F ~ag8é18COs5<br><= PROS? Sq BY va<br>pSESuN~S.<SS \patteRt*THEFTnonce CRIM SE;XUAL ASSAULT"UN \NecL aNLloa iH/ZE<br>— iy<br>CAREyy | \ UMAN Tp wt posgex OFFENSER/ rrcreoAWAY)||SAWAS ¢QO WA<br>{ GaVy UenUg "Napfa “AFFICKiys a WANS<br>= whNNELLONe /<br>é & wbZipZ % &“og,byOe. Ney10 SS» & FSESSAP<br>F § 4% % ey Cr o § FP3h%<br>s& 2%53%% %% %My £523<br>§ 6%3 4 %. & 33°2<br>(b) CGL (c) GLEN<br>**----- End of picture text -----**<br>


**Figure 2.3.** Rank of the crimes by their mean occurrences (a), and graphs inferred from the Chicago crime dataset using original CGL (b) and GLEN with offsets (c). Nodes correspond to crime types. The width of the edges corresponds to the edge weights. 

Since each matrix entry indicates the number of crime occurrences in a specific region during one of the 10 years, we use Poisson distribution to model the count signals. However, since the crime rates vary dramatically by the type of crimes, we use the extended GLEN with offset variables as in Sec. 2.3.1 where the Poisson distribution is used. The offset of each crime is initialized as the logarithm of their mean occurrences. We compare our method with CGL and tune their hyper-parameters to encourage sparsity. The crime graphs learned by both methods 

30 

are shown in Figure 2.3. 

As we can see, CGL is more biased by the number of crime occurrences, tending to link crimes with similar frequencies. Furthermore, it fails to converge when we increase the regularization term to estimate a sparser graph. On the other hand, GLEN learns a more interpretable graph that better links similar crimes. For example, GLEN learns an edge between “Sex Offense”, “Criminal Sexual Assault”, and “Assualt”, which is ignored by CGL. The graph learned by GLEN is also more agnostic to the crime frequencies. 

## **2.4.3 Animals Dataset** 

We also evaluate our method on the Animals dataset Kemp and Tenenbaum (2008). The Animal dataset is a binary matrix of size 33 _×_ 102, where each row corresponds to an animal species and each column corresponds to a boolean feature such as “has wings?”, “has lungs?”, “is dangerous?”. Our goal is to learn a graph where each node represents a species and each edge represents the similarity between them. To accommodate smooth models to the binary signals, previous work Egilmez et al. (2017); Kumar et al. (2020) used a heuristic statistic **S** =[1] _n_ **[XX]** _[T]_[ +][1] 3 **[I]** suggested by Banerjee et al. (2008). We instead explicitly model the binary signals using the Bernoulli distribution, resulting in an improper Bernoulli-Logit-Normal model Aitchison and Shen (1980). This amounts to setting _R_ = 1 in the Binomial noise model for GLEN. 

We evaluate GLEN against existing methods both qualitatively and quantitatively. Although a ground-truth animal graph does not exist, we construct a pseudo-ground-truth using the scientific animal classification. Animal classification is a taxonomy that categorizes living forms into an 8-level hierarchical system: ‘domains’, ‘kingdoms’, ‘phyla’, ‘classes’, ‘orders’, ‘families’, ‘genera’, and ‘species’. For example, both tiger and squirrel belong to the Mammalia ‘class’, but they belong to Carnivora and Rodentia, respectively, on the more specific ‘order’ level. Their highest common level indicates their similarity. Thus, for a set of nodes that correspond to the listed animals, we connect two nodes if they belong to the same ‘class’. Given that over half of the animals belong to the Mammalia ‘class’, we only connect two Mammalia nodes if 

31 

they also belong to the same ‘order’. This gives us an unweighted graph that respects the animal similarities. 

Figure 2.4 shows the weighted adjacency matrices learned by GLS-1, CGL, and GLEN. First, we can see that GLEN learns a sparser graph with more clear community structures, compared with GLS-1 and CGL. GLEN identifies clear community structures between animal ‘classes’ and Mammalia ‘orders’. In contrast to GLEN, CGL ignores the insect sub-network “Bee-Butterfly-Ant-Cockroach” while GLS-1 learns more spurious edges. Next, we quantify the accuracy of the learned graphs using the ground-truth taxonomy graph. We perform a grid search for each method and report their highest PR-AUC. As shown in Table 2.6, GLEN achieves the highest PR-AUC. This implies that the graph learned by GLEN best reflects the animal taxonomy. 

**Table 2.6.** Comparing PR-AUC on the animal classification task. 

|Method|GLS-1|GLS-2|CGL|GLEN|
|---|---|---|---|---|
|PR-AUC|81.50|80.39|68.02|82.63|



## **2.4.4 Neural Dataset** 

We now turn to a dataset that has a graph-temporal structure. The _Area_ 2 ~~_B_~~ _ump_ dataset from the neural latent benchmark (NLB) Pei et al. (2021) consists of multiple trials of neural spiking activity and simultaneous behavior data of a macaque. The macaque is trained to control a cursor and perform center-out reaches toward one of eight target directions. In a subset of random trials, a bump interrupts the macaque shortly before the reach. The macaque’s neural activity is recorded from Brodmann’s area 2 of the somatosensory cortex, which has been shown to contain information about whole-arm kinematics. The neural recording is contained in a non-negative integer matrix **X** _∈_ Z+ _[N][×][T][×][K]_ , where each entry **X** _itk_ counts the firing of neuron _i ∈{_ 1 _,_ 2 _,..., N}_ in time bin _t ∈{_ 1 _,_ 2 _,..., T }_ during trial _k ∈{_ 1 _,_ 2 _,..., K}_ . Following the standard procedure in Pei et al. (2021), we resample the 1-ms resolution signals into 5-ms bins. 

32 

33 

Learning the interactions between the neurons from these spiking activity matrices relates functional connectivity patterns to behavior. Suppose a graph underlies the set of _N_ neurons, a graph signal **X** : _tk_ is the simultaneous spiking of all neurons at time _t_ in trial _k_ . Since graph signals are not independent but temporally correlated, we use GLEN-TV instead of GLEN to denoise the signals spatially and temporally. We infer a graph of neurons for each trial, bumped or not bumped, and analyze the inferred graphs across different conditions, the target directions. We model the observation with the Poisson distribution which is used in the standardized cosmoothing evaluation Macke et al. (2011). The objective function and alternating updates are obtained by plugging in the Poisson distribution to Eq. (2.31). 

We perform linear discriminant analysis (LDA) on the degree vector of learned Laplacians, using direction conditions as the eight class labels. LDA achieves 70 _._ 33% accuracy, indicating that the structural information in our learned graphs encodes the class conditions. When applying GLEN without the temporal modeling, LDA only achieves 67 _._ 86% accuracy, which indicates the importance of modeling temporal correlations. We also visualize the average spiking activity and the averaged denoised signals for all 8 conditions in Figure 2.6. The denoised signals are the exponential of learn smooth representation **Y** , which are interpreted as the firing rates of the neurons. Note that GLEN-TV smooths the signals both spatially and temporally. 

Chapter 2, in full, has been submitted for publication in IEEE Transaction on Signal and Information Processing over Networks, Shi, Changhao; Mishne, Gal. The dissertation author was the primary investigator and author of this paper. 

34 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0049-00.png)


**----- Start of picture text -----**<br>
Average Spiking Average Denoised Signals<br>Cc Cc<br>S9<br>0 [◦] oODD<br>Cc . Oo<br>ls ee ee, eee! ual le mn nub Ccae:=<br>20 40 60 80 100 120 20 40 60 80 100<br>___time/s time/s<br>Cc Cc<br>9 9<br>D> D><br>45 [◦] () oO<br>Cc Cc=<br>20 40 60 80 100 120 20 40 60 80 100<br>_ time/s time/s<br>S9<br>D<br>90 [◦] oO OoD<br>Cc Cc<br>pees =<br>20 40 60 80 100 120 20 40 60 80 100<br>___itime/s time/s<br>9 9<br>D> D><br>135 [◦] () oO<br>**----- End of picture text -----**<br>


**Figure 2.5.** Average raw neural spiking data compared against average denoised signals by GLEN-TV, for each target direction shown on the left. The brighter color indicates a higher firing rate. 

35 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0050-00.png)


**----- Start of picture text -----**<br>
Average Spiking Average Denoised Signals<br>Cc Cc<br>S9<br>D<br>180 [◦] ro) oOD<br>Cc Cc<br>20 40 60 80 100 120 20 40 60 80 100<br>tiMe/S time/s<br>so<br>Cc Cc<br>S S<br>D> D><br>225 [◦] () oO<br>Cc Cc<br>: He tged ee 1<br>: be a Fins en oe inte; ty<br>20 40 60 80 100 120 20 40 60 80 100<br>time/s time/s<br>S9<br>D<br>270 [◦] ro) oOD<br>Cc Cc<br>goo aeioe as : z<br>20 40 60 80 100 120 20 40 60 80 100<br>time/s _<br>S<br>D> D><br>315 [◦] () oO<br>**----- End of picture text -----**<br>


**Figure 2.6.** Average raw neural spiking data compared against average denoised signals by GLEN-TV, for each target direction shown on the left. The brighter color indicates a higher firing rate. 

36 

## **Chapter 3** 

## **Graph Inference from Multi-Way Signals** 

Multi-way arrays, or tensors, capture complex interactions between different modes of variations and have become prevalent in modern data analysis. GSP and GFT also adapt to the multi-way settings, leading to the studies of multi-way GSP (MWGSP) (Stanley et al., 2020). MWGSP imposes Cartesian product structures on the graph domain, which allows each factor graph to capture the dependencies of each mode. In this Chapter, we discuss how we adopt graph learning to multi-way settings. We first provide the context of MWGSP in Section 3.1. We then propose a penalized MLE for learning the Cartesian product graphs in Section 3.2, and study its theoretical behaviors in Section 3.3. Section 3.4 presents some empirical results of applying our method to synthetic and real-world datasets. 

## **3.1 Multi-way Signals** 

While graph Laplacian learning and covariance selection are useful for single-way analysis, they are not intended for multi-way tensors. A multi-way tensor, as opposed to a single-way vector, is a multi-dimensional array where each way or mode of the tensor represents a different source of variation. Consider such a multi-way scenario: a sensor network of _ps_ sensors with unknown connectivity and their measurements on _pt_ time points over a day. An example of single-way inference is to directly apply graph learning methods to learn a graph of sensors from the _pt_ 1-d spatial signals. Not surprisingly, this results in a sub-optimal solution 

37 

**Figure 3.1.** An example of the Cartesian graph product. 

since the dependencies between _pt_ time points are ignored. A more appealing approach is to learn a graph of size _ps pt_ , in which each node is a (sensor, time point) pair. However, this poses new computational challenges since _ps pt_ is usually huge. To circumvent the challenges, imposing graphs with the Cartesian product structure gains massive interest. An example of the Cartesian graph product is shown in Figure 3.1. As we can see, Cartesian product graphs are extremely suitable for multi-way data, since they offer a reasonable parsimony where only dependencies within ways are captured by factor graphs. It is even more appealing to learn Cartesian product graphs under the Laplacian constraints, which serve as the foundations of MWGSP. Owing to the Cartesian product Laplacian, the multi-way graph Fourier transform enjoys a concise form of separable mode-wise Fourier transform. 

In this chapter, we study the problem of learning the Cartesian product Laplacian from multi-way data. We consider the penalized MLE of the Cartesian product IGMRF and propose an efficient algorithm to solve the problem by leveraging the spectral properties of the Cartesian product Laplacian. A modified algorithm is also proposed for joint graph learning and missing value imputation. Theoretically, we establish the high-dimensional statistical consistency of the proposed penalized MLE and obtain an improved rate of convergence over non-product graph Laplacian learning. Our method provides a better solution than related GM works, which ignore the Laplacian constraints, and existing GSP works, which lack theoretical guarantees. 

To summarize our contributions: 

38 

- We are the first to consider the penalized MLE of Cartesian product Laplacian learning, and gain theoretical results on its asymptotic consistency, to the best of our knowledge. 

- We propose an efficient algorithm to solve the penalized MLE, which reduces the time complexity of the naive solution. We further extend the algorithm to the setting of structural missing data. 

- We demonstrate that our approach outperforms existing GSP and GM methods on synthetic and real-world datasets. 

As a side note, we emphasize that graph learning is intrinsically a different problem from covariance selection, although they bear a similar form. The parameter space of graph learning and covariance selection are two disjoint sets as Laplacian matrices are singular with constant 0-eigenvectors. Graph learning also requires that all conditional dependencies are positive, though this is also a GM subject under the study of M-matrices (Slawski and Hein, 2015). 

## **Related Works** 

The graphical lasso algorithm has been extended to matrix/tensor Gaussian distributions (Dawid, 1981; Gupta and Nagar, 1999) to learn Kronecker product precision matrices (Dutilleul, 1999; Zhang and Schneider, 2010; Leng and Tang, 2012; Tsiligkaridis et al., 2013). Further extensions replace the Kronecker product structure with the Kronecker sum (Kalaitzis et al., 2013; Greenewald et al., 2019; Wang et al., 2020b; Yoon and Kim, 2022), leading to Cartesian product graphs. Again, none of these graphical lasso methods learn precision matrices under Laplacian constraints but only bear a similar form to the Cartesian product Laplacian learning. 

In terms of learning Cartesian product graphs, Lodhi and Bajwa (2020) advocated directly optimizing the total variation on product Laplacian; Kadambari and Prabhakar Chepuri (2020); Kadambari and Chepuri (2021) decomposed the overall smoothness measurement into factorwise variation so that each factor graph can be learned separately; Einizade and Sardouie (2023) proposed to first estimate eigenfunctions of factor graph representations, and then solve the 

39 

spectral template problem as in (Segarra et al., 2017). However, these methods simplified the MLE to facilitate optimization, which generally leads to asymptotic inconsistencies. 

## **3.2 Graph Inference for Multi-way Signals** 

## **3.2.1 Penalized MLE** 

Let the random matrix _**X** ∈_ R _[p]_[1] _[×][p]_[2] represent a two-way graph signal that lives on the product graph _G_ . [ _**X**_ ] _i_ 1 _,i_ 2 is the signal on node ( _i_ 1 _, i_ 2). Given _n_ instantiations _{_ **X** 1 _,_ **X** 2 _,...,_ **X** _n}_ , our goal is to learn the factor graphs _G_ 1 _, G_ 2 and their Cartesian product _G_ from these nodal observations on _G_ . Note that to ease the presentation, we limit the number of factor graphs to two, but our formulation and solution can be easily generalized to more factors and higher-dimensional tensors _**X** ∈_ R _[p]_[1] _[×][p]_[2] _[×][p]_[3] _[×][...]_ . 

Let the random vector _**x**_ be the vectorization of _**X**_ and **S** =[1] _n_[∑] _k[n]_ =1 **[x]** _[k]_ **[x]** _[kT]_[be the SCM.] Since for _G_ = _G_ 1□ _G_ 2 we have **L** = **L** 1 _⊕_ **L** 2 (Barik et al., 2018), we derive the product graph learning objective 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0054-05.png)


(3.1) can be interpreted from either a GSP or a GM perspective, which we discuss below. 

## **GSP Interpretation:** 

We decompose _J_ ( _{_ **X** _k}_ ) := _⟨_ **L** 1 _⊕_ **L** 2 _,_ **S** _⟩_ = _⟨_ **L** 1 _,_ **S** 1 _⟩_ + _⟨_ **L** 2 _,_ **S** 2 _⟩_ , where 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0054-09.png)


This indicates that the variation on the product graph equals the sum of mode-wise variation, and Cartesian product graph learning encourages signals to be smooth on each factor. In contrast to existing non-consistent GSP methods, we use a log-determinant regularization naturally induced by MLE, which is crucial for the estimator to be consistent as we will show. 

40 

## **GM Interpretation:** 

Consider a random matrix-variate _**x**_ defined by a IGMRF _**x** ∼ N_ ( **0** _,_ ( **L** 1 _⊕_ **L** 2)[†] ). Then (3.1) is the penalized MLE of fitting this model to the product graph signals. Solving (3.1) amounts to enforcing the Laplacian structure on the Kronecker sum precision matrices. As the Laplacian constraints are essentially a structural prior, they are important for accurate estimation, especially when _n_ is small. We will show that our experiments verify this claim. 

## **3.2.2 Multi-Way Graph Learning** 

We now propose the **M** ulti- **W** ay **G** raph (Laplacian) **L** earning ( **MWGL** ) algorithm for solving (4.1). First we rewrite (4.1) as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0055-04.png)


since _⟨_ **L** _,_ **S** _⟩_ = _⟨L ,_ **wS** _⟩_ = **w** _[T] L[∗]_ **S** . The absolute sign of the _ℓ_ 1 norm of the sparsity regularization is redundant due to the non-negative constraints. We then use projected gradient descent to solve **w** 1 and **w** 2. The update of **w** 1 and **w** 2 is given by 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0055-06.png)


where for **H** 1 _∈_ R _[p]_[1] _[×][p]_[1] and **H** 2 _∈_ R _[p]_[2] _[×][p]_[2] we have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0055-08.png)


41 

The regularization parameters for each factor graph are _α_ 1 = _p_ 2 _α_ and _α_ 2 = _p_ 1 _α_ , but in practice, we can benefit from a free grid search of _α_ 1 and _α_ 2. With the learning rate _η_ of the user’s choice, alternating between (3.4) until stopping criteria is satisfied solves the Cartesian product graph learning problem. The above projected gradient descent scheme is guaranteed to converge in _O_ ([1] _t_[)][ for] _[ η]_[that is sufficiently small.] 

A closer look reveals that this solution is not computationally scalable. Computing the gradient involves taking the inverse of the product graph Laplacian, which can be huge when the number of factors increases. Even for the 2-factor case, the computational cost of inversion will explode quickly as the size of each factor graph grows. Fortunately, we can compute **H** 1 and **H** 2 efficiently using the following lemma. 

**Lemma 1** (Efficient Computation) **.** _The_ **H** 1 _and_ **H** 2 _matrices defined in_ (3.5) _can be efficiently computed as_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0056-03.png)


_where_ **L** 1 = **U** 1 **Λ** 1 **U** _[T]_ 1 _[and]_ **[L]**[2][=] **[ U]**[2] **[Λ]**[2] **[U]** _[T]_ 2 _[are][the][eigendecompositions][of][factor][Laplacian] matrices._ 

The key to obtaining (3.6) is to leverage the spectral structure of the Cartesian product Laplacian and its inverse. A similar strategy has been used in (Yoon and Kim, 2022), but here we do not suffer from the identifiability issue thanks to the Laplacian constraints. See the supplement for the details. Note that (3.6) only requires matrix operations on the factor scales and avoids taking the cumbersome inversion of **L** as in (3.5). These two steps together demand _O_ ( _p_[3] 1[+] _[ p]_[3] 2[)] time complexity (dominated by eigendecompositions), which is a significant reduction from the full matrix inversion _O_ ( _p_[3] ) = _O_ ( _p_[3] 1 _[p]_[3] 2[)][.][Alg. 2 summarizes the algorithm.] 

42 

## **Algorithm 2.** MWGL 

**Input:** graph signals _{_ **X** _k}_ , parameters _α, η_ Compute **S** 1 _,_ **S** 2 as in (3.2). Initialize **w** 1 and **w** 2. 

## **repeat** 

Compute **H** 1 and **H** 2 as in (3.6). Update **w** 1 and **w** 2 with (3.4). **until** convergence or reaching maximum iterations. **Output:** factor graph weights **w** 1 _,_ **w** 2 

## **3.2.3 Structural Missing Values** 

Missing values are common in real-world data. In some cases, there are random missing entries in **X** _k_ ; in other cases, the entire fiber _{_ [ **x** 1] _i,_ [ **x** 2] _i,...,_ [ **x** _n_ ] _i}_ of node _i_ is missing. Inferring connectivity of these missing nodes is generally impossible unless the underlying graph is a Cartesian product. An example, which we demonstrate in the experiments, is learning the product graph from multi-view object images when images of some (object, view) pairs are not accessible. For these missing nodes, their object edges are preserved by other views of the same object, and their view edges are preserved by other objects of the same view. 

We now propose to learn the graphs and impute the missing values simultaneously. Let Ψ[∁] be the set of missing nodes in the product graph. We treat missing values as contamination of the true data and refine the imputation before every projected gradient descent step in Alg. 2, i.e. we alternate between filling in the data and learning the factor graphs as before. Let **X**[(] _k[t]_[)] be the imputed signals at step _t_ and the signals on the observed nodes [ **X**[(] _k[t]_[)][]] Ψ[= [] **[X]** _[k]_[]] Ψ[are fixed.] Consider 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0057-07.png)


where _β_ is a trade-off parameter. We solve _{_ [ **X**[(] _k[t]_[)][]] Ψ[∁] _[}]_[ inexactly by alternating the following] steps 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0057-09.png)


43 

(3.8) is the partial solution of the Tikhonov filtering 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0058-01.png)


which are low-pass graph filters that smooth missing value imputations with current factor graph estimation. Note that we alternately filter the signals with factor graphs rather than employ one-pass filtering with the product graph. This eases the computation for the same reason as in Sec. 3.2.2. We term this algorithm **MWGL-Missing** and summarize it in Alg. 3. 

## **Algorithm 3.** MWGL-Missing 

**Input:** observed nodes Ψ _, {_ [ **X** _k_ ]Ψ _}_ , parameters _α, β , η_ 

Initialize **w** 1, **w** 2. 

## **repeat** 

Refine imputed values _{_ [ **X** _k_ ]Ψ∁ _}_ with (3.8). Update **S** 1 _,_ **S** 2 as in (3.2). Compute **H** 1 and **H** 2 as in (3.6). Update **w** 1 and **w** 2 with (3.4). **until** convergence or reaching maximum iterations. **Output:** factors **w** 1 _,_ **w** 2, imputed values _{_ [ **X** _k_ ]Ψ∁ _}_ 

## **3.3 Theoretical Results** 

Now we establish the statistical consistency and convergence rates for the Cartesian product Laplacian estimator as in (4.1). We first make two assumptions regarding the true underlying graph we were to estimate: 

(A1) Let _A_ = _{_ ( _i, j_ ) _|_ [ **w** ] _i− j_ + 21[(] _[j][−]_[1][)(][2] _[p][−][j]_[)] _[ >]_[ 0] _[,][i][ >][j][}]_[ be the support set of] **[ w]**[.][We assume the] graph is sparse and the cardinality of the support set is upper bounded by _|A | ≤ sp_ . 

- (A2) Let _{_ 0 _, λ_ 2 _,..., λp}_ be the eigenvalues of the true product Laplacian in a non-decreasing order. We assume these eigenvalues are bounded away from 0 and ∞ by a constant _z >_ 1, such that[1] _z[≤][λ]_[2] _[ <][ λ][p][ ≤][z]_[.] 

44 

Both assumptions are common in high-dimensional statistics literature. Also notice that in our case, bounding the Fiedler value (the second smallest eigenvalue) away from 0 implies that the graph is connected. 

**Theorem 2** (Existence of MLE) **.** _The penalized negative log-likelihood of Cartesian product Laplacian learning as in_ (4.1) _is lower-bounded, and there exists at least one global minimizer as the solution of the penalized MLE._ 

Ying et al. (2021) proved that the negative log-likelihood as in (1.8) is lower-bounded and the MLE exists. Since the Laplacian of Cartesian product graphs form a subset of all graph Laplacians, the same lower bound applies here. In fact, we derive a tighter lower bound for the Cartesian product graphs. It remains to show that the global minimizer can be achieved in this subspace of Cartesian product graphs. We demonstrate this by parameterizing the product Laplacian in (4.1) with **w** 1 and **w** 2. 

**Theorem 3** (Uniqueness of MLE) **.** _The objective function of penalized MLE is jointly convex with respect to the factor graphs, and its global minimizer uniquely exists._ 

The uniqueness is not surprising since the original graph Laplacian learning problem is convex, and the map from factor graphs to their Cartesian product is linear. 

**Theorem 4** (High-dimensional consistency) **.** _Suppose assumptions (A1) and (A2) hold. Then with sufficient observations_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0059-06.png)


_and regularization parameter_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0059-08.png)


45 

_the minimizer_ **L**[�] _of the penalized MLE as in_ (4.1) _is asymptotically consistent to the true Laplacian_ **L** _[∗] with the Frobenius error bound_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0060-01.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0060-02.png)


Theorem 4 not only proves that our proposed estimator is guaranteed to converge to the true Laplacian but also improves the rate of consistency from (Ying et al., 2021) by a factor of ~~�~~ min( _p_ 1 _, p_ 2). The improvement reflects the recurrence of factor dependencies in a single product graph signal. A similar trend has been observed in (Greenewald et al., 2019) when the graphical lasso generalizes to multi-dimensional tensors. The key to proving the improved rate is using Hanson-Wright inequality (Hanson and Wright, 1971; Rudelson and Vershynin, 2013) to obtain concentration results on individual modes of the multi-way tensor. For min( _p_ 1 _, p_ 2) = 1, our convergence rate coincides with the one in Ying et al. (2021). See detailed proofs of the above theorems in the supplement. 

## **3.4 Experiments** 

We conduct extensive experiments in MATLAB on both synthetic and real-world datasets to evaluate our method. See the supplement for more details. 

## **3.4.1 Synthetic Graphs** 

We first evaluate MWGL on synthetic graphs and signals. We use the following models to generate factor graphs: 

- (1) Erd˝os-R´enyi model with edge probability 0 _._ 3; 

- (2) Barab´asi-Albert model with preferential attachment 2 starting from 2 initial nodes; 

46 

**Figure 3.2.** Comparison of different methods on various synthetic data. Each sub-figure shows the trend of Rel-Err of the product or factor Laplacian matrices as _n_ increases. Black dash lines fit the theory in (3.12) to our results. 

- (3) Watts-Strogatz small-world model, where we create an initial ring lattice with degree 2 and rewire every edge of the graph with probability 0 _._ 1; 

## (4) and regular grid model. 

Edge weights are then randomly sampled from a uniform distribution _U_ (0 _._ 1 _,_ 2) for each edge. We generate weighted factor graphs of _p_ 1 = 20 and _p_ 2 = 25 nodes using each graph model and take their Cartesian product to obtain graphs of _p_ = _p_ 1 _p_ 2 = 500 nodes. The factor grid models are 4 _×_ 5 grids and 5 _×_ 5 grids. The signals are then generated from _**f** ∼ N_ ( **0** _,_ **L**[†] ). We generate _n_ = 10 _×_ 2ˆ _{_ 0 _,_ 1 _,...,_ 10 _}_ signals for each synthetic product graph, and evaluate graph learning methods under these different settings. We repeat this process to obtain 50 realizations for each graph model. 

We compare MWGL with multiple GSP and GM baselines. For the GSP baselines, we compare with the PGL (Product Graph Learning) method (Kadambari and Chepuri, 2021) 

47 

**Figure 3.3.** Comparison of different methods on synthetic data in various scenarios. Each sub-figure shows the PR-AUC of edge estimation as _n_ increases. 

and the PST (Product Spectral Template) method (Einizade and Sardouie, 2023). To compare with GM methods, we select the BiGLasso (Kalaitzis et al., 2013) and TeraLasso (Greenewald et al., 2019) algorithms that learn precision matrices of Kronecker sum structure. Since a precision matrix **Θ** learned GM methods is generally not a Laplacian, we select its positive “edges” **w Θ** = ( _−_ tril( **Θ** _, −_ 1))+ and build a true Laplacian _L_ **w Θ** for evaluation. tril stands for the Matlab operation of lower triangular vectorization. 

We use the relative error (Rel-Err) and the area under the precision-recall curve (PRAUC) as the main evaluation metrics. Since the selected GSP baselines impose the constraints Tr( **L** 1) = _p_ 1 and Tr( **L** 2) = _p_ 2 (thus Tr( **L** ) = Tr( **L1** _⊗_ **I** _p_ 2)+Tr( **I** _p_ 1 _⊗_ **L2** ) = 2 _p_ 1 _p_ 2), we normalize the true Laplacian and the Laplacian learned by other methods for the comparison of Rel-Err 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0062-03.png)


48 

The Rel-Err between the true and learned Laplacian in terms of the Frobenius norm is then computed as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0063-01.png)


similarly for the factor graphs. We perform a grid search to decide the best regularization parameter of each method. Figure 3.2 and Figure 3.3 show the averaged Rel-Err and PR-AUC across 50 realizations and the standard deviations on each setting. 

Our numerical results demonstrate that our MWGL outperforms both GSP and GM baselines in all the settings. PGL performs well in the low data regime but loses its advantage when _n_ increases. The plots indicate that PGL is inherently asymptotically inconsistent, which is reasonable since their objective function misses the integral log-determinant term of the MLE. PST improves fast as _n_ grows, since the estimated spectral template, i.e. Laplacian eigenvectors, becomes increasingly accurate. However, it still underperforms MWGL even when _n_ is large. For the GM baselines, TeraLasso outperforms BiGLasso and comes close to MWGL for large _n_ . But when _n_ is small, it underperforms MWGL and sometimes other GSP baselines, which shows the importance of the Laplacian constraints as a structural prior. Compared to all these baselines, our MWGL performs well in the full spectrum of _n_ . Also note that the Rel-Err curves of our method fit convergence rate in (3.12) very well (we solve for _c_ via regression), which validates our theoretical findings. 

We now evaluate MWGL on synthetic data with fixed _p_ but varying _p_ 1 and _p_ 2. Our main goal is to verify the convergence rate in 4 as a function of min ( _p_ 1 _, p_ 2), but we also compare MWGL with PGL and TeraLasso. We fix the size of product graphs to be _p_ = 256 and set _p_ 1 to be 4, 8, or 16, and _p_ 2 to be 64, 32, and 16, respectively. We use the same graph models stated in Sec. 3.4.1 to generate factor graphs. For regular grids, we always set the width to 2 and the height correspondingly. We generate _n_ = 80 graph signals and average the results across 50 realizations. Figure 3.4 shows that MWGL again outperforms selected baselines and matches the theoretical results. 

49 

**Figure 3.4.** Comparison of different methods on synthetic data in various scenarios. Each sub-figure shows the trend of Rel-Err of the product or factor Laplacian matrices as min( _p_ 1 _, p_ 2)) increases. Black dash lines fit the theory in (3.12) to our results. 

## **3.4.2 Molene Weather Data** 

We next consider the Molene weather dataset (Loukas and Perraudin, 2019), originally published by the French National Meteorological Service. The dataset contains hourly temperature recordings of 32 weather stations in Brest, France, during the month of January 2014. Our goal is to learn the product of a 32-node geographical graph of weather stations and a 24-node temporal graph of hours. The daily recordings of all stations form a graph signal, and we aim to learn the Cartesian product graph from the 31 daily signals. 

MWGL again learns reasonable factors as demonstrated in Figure 3.5. The learned weather station graph faithfully reflects their coordinates and altitudes. The 24 nodes of hours form a path graph, in alignment with their temporal order. 

We now compare our MWGL to PGL and TeraLasso, two methods that come close to MWGL on the synthetic data, on the Molene dataset across ranging regularization parameters. Figure 3.6 shows the weighted adjacency matrices (negative off-diagonal precision matrices for TeraLasso) of the station graphs learned by these methods. First, notice that TeraLasso learns few negative conditional dependencies among weather stations. Indeed it is reasonable that the temperature of different locations does not depend negatively, which indicates that the attractive Laplacian constraints are suitable structural priors for the problem. Also, notice that only MWGL learns connected graphs with varying regularization, and neither PGL nor TeraLasso learns connected graphs when sparsity increases. 

50 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0065-00.png)


**----- Start of picture text -----**<br>
(a)  Stations (b)  Hours<br>**----- End of picture text -----**<br>


**Figure 3.5.** The inferred factor graphs of Molene. Stations are placed according to their real coordinates. 

**Figure 3.6.** Comparing the learned station graph of PGL, TeraLasso, and MWGL (ours) on the Molene dataset with varying regularization. Laplacians are ordered with increasing sparsity from left to right. 

## **3.4.3 COIL-20 Dataset** 

We now evaluate MWGL-Missing on the Columbia Object Image Library 20 (COIL-20) dataset (Nene et al., 1996). COIL-20 consists of 128 _×_ 128 grey-scale images of 20 small 

51 

objects, where each object is placed on a turning table and captured by a fixed camera to obtain multi-views at evenly distributed angles. Images are taken every 5 degrees to produce 72 views per object, which we sub-sample to 36 views. Our goal is to learn a Cartesian product of a 20-node object graph and a 36-node view graph from the 16384 = 128 _×_ 128 graph signals. To create structural missingness, we remove the images from 180 to 360 degrees of half of the objects (25% of all data) and apply MWGL-Missing. 

Figure 3.7 shows MWGL-Missing learns meaningful graphs and imputations despite structural missingness. For the object graph, it learns strong connections between the most similar object pairs, such as the car models, and groups other similar objects together. The joint imputation, based on alternating Tikhonov filtering, also reasonably reconstructs the missing images by smoothing the inferred neighboring objects and views. As we can see, the imputation of symmetric objects (e.g., last row) relies on the view graph, and for the imputation of less symmetric objects (e.g., fourth row) the object graph plays a more important role. The limitation is that imputing a distinct object (e.g., third row) is generally challenging as it lacks meaningful neighbors. 

## **3.5 Proofs of Theoretical Results** 

## **3.5.1 Proof of Lemma 1: Efficient Computation** 

We first state the following lemma which characterizes the spectral structure of the Cartesian product Laplacian. 

**Lemma 5** (Eigen-decomposition of Cartesian Product) **.** _With proper ordering, the eigenvectors of the product graph Laplacian is the Kronecker product of the eigenvectors of the factor graph Laplacian_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0066-06.png)


_and the eigenvalues of the product graph Laplacian are the Kronecker sum of the eigenvalues of_ 

52 

**(a)** Objects 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0067-01.png)


**----- Start of picture text -----**<br>
(b)  Imputed images<br>**----- End of picture text -----**<br>


**Figure 3.7.** (a) The inferred object graph and (b) selected imputations of the COIL-20 dataset. The first column is observed images and the other columns are reconstructions across missing angles. 

## _the factor graph Laplacian_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0067-04.png)


Lemma. 5 follows from the properties of Kronecker product (Barik et al., 2018). Now we proceed to prove Lemma. 1. 

53 

_Proof._ We now derive the efficient computation of **H** 1 that avoids the expensive large matrix inversion. Let the eigen-decomposition of the factor Laplacians be _L_ **w** 1 = **U** 1 **Λ** 1 **U** _[T]_ 1[and] _L_ **w** 2 = **U** 2 **Λ** 2 **U** _[T]_ 2[.][By Lemma 5, we have the eigendecomposition of the product Laplacian] 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0068-01.png)


Additionally, we notice that the eigenvectors of **L**[†] are also **U** 1 _⊗_ **U** 2. This helps us derive the following 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0068-03.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0068-04.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0068-05.png)


Computation of **H** 2 is derived similarly. 

## **3.5.2 Proof of Theorem 2: Existence** 

_Proof._ Given **L** = **L** 1 _⊕_ **L** 2, we now prove that the global minimizer of the following penalized MLE 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0068-09.png)


54 

uniquely exists. Provided that both the product and factor graphs are connected, The feasible set over **w** 1 and **w** 2 is defined as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0069-01.png)


where **J** _p_ =[1] _p_ **[1]** _[p]_ **[1]** _[T] p_[and we have][ logdet][†][(] **[L]**[) =][ logdet][(] **[L]**[+] **[J]** _[p]_[)][. The conditions] _[ L]_ **[ w]**[1][+] **[J]** _[p]_ 1 _[∈][S]_ ++ _[p]_[1] and _L_ **w** 2 + **J** _p_ 2 _∈ S_ ++ _[p]_[2][constrain that] _[ G]_[1][and] _[ G]_[2][are connected.][Let] _[ {]_[0][ =] _[ λ]_[1] _[≤][λ]_[2] _[≤··· ≤][λ][p][}]_ be the eigenvalues of **L** and **S** 1 and **S** 2 as defined in Section (3.3). We first consider the MLE ( _α_ = 0) and bound the negative log-likelihood _Q_ ( **w** 1 _,_ **w** 2) as below 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0069-03.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0069-04.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0069-05.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0069-06.png)


where [ **S**[˜] 1] _i, j_ = _p_[1] 2[[] **[S]**[1][]] _i, j_[and][[] **[S]**[˜][2][]] _i, j_[=] _p_[1] 1[[] **[S]**[2][]] _i, j_[.][Inequality][(3.26)][holds][from][the][AM-GM] inequality, which states that the arithmetic mean of a list of real non-negative numbers is no less than their geometric mean. (3.27) is attributed to the properties of Cartesian product graphs, and (3.28) to that the summation of eigenvalues is equal to the trace of the Laplacian. Define the function 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0069-08.png)


55 

This function is lower-bounded at _t_ = _p−_ 1[so][long][as][min][(] _[L][ ∗]_ **[S]**[˜][1] _[ ∪][L][ ∗]_ **[S]**[˜][2][)] _[ >]_[ 0][.] min( _L[∗]_ **S**[˜] 1 _∪L[∗]_ **S**[˜] 2)[,] Therefore, we have that the negative log-likelihood is also lower-bounded 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0070-01.png)


We then notice that _q_ ( _t_ ) _→_ ∞ when _t →_ ∞. This is followed with _Q_ ( **w** 1 _,_ **w** 2) being coercive, since _∥_ [ **w** 1 _,_ **w** 2] _∥_ 2 _→_ ∞ ⇝ _p_ 2 _∥_ **w** 1 _∥_ 1 + _p_ 1 _∥_ **w** 2 _∥_ 1 _→_ ∞. This indicates that the global minimizer exists in cl(Ω **w** 1 _,_ **w** 2). 

Furthermore, since the open boundaries cl(Ω **w** 1 _,_ **w** 2) _\_ Ω **w** 1 _,_ **w** 2 are results of the connectivity constraint _L_ **w** 1 + **J** _p_ 1 _≻_ **O** and _L_ **w** 2 + **J** _p_ 2 _≻_ **O** , we have that cl(Ω **w** 1 _,_ **w** 2) _\_ Ω **w** 1 _,_ **w** 2 is a subset of disconnected **w** 1 and **w** 2. The set of disconnected **w** 1 and **w** 2 is written as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0070-04.png)


Since for the Cartesian product, any factor graph being disconnected leads to the product graph being disconnected, _∀_ ( **w** 1 _,_ **w** 2) _∈_ cl(Ω **w** 1 _,_ **w** 2) _\_ Ω **w** 1 _,_ **w** 2 we have logdet( **L** ) = _−_ ∞ ⇝ _Q_ ( **w** 1 _,_ **w** 2) _→_ ∞. This shows that any global minimizer over cl(Ω **w** 1 _,_ **w** 2) do not lie on those open boundaries, therefore (3.22) has at least a global minimizer in Ω **w** 1 _,_ **w** 2 so long as min( _L[∗]_ **S**[˜] 1 _∪ L[∗]_ **S**[˜] 2) _>_ 0. min( _L[∗]_ **S**[˜] 1 _∪ L[∗]_ **S**[˜] 2) _>_ 0 holds with probability 1. 

For the penalized MLE where _α >_ 0, we slightly modify (3.30) to obtain a new lower bound 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0070-07.png)


As min( _L[∗]_ **S**[˜] 1 _∪ L[∗]_ **S**[˜] 2)+ _α >_ 0 always hold, the penalized MLE always exists. 

56 

## **3.5.3 Proof of Theorem 3: Uniqueness** 

_Proof._ First we show that Ω **w** 1 _,_ **w** 2 is a convex set. Define the feasible set of **w** 1 and **w** 2 as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0071-02.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0071-03.png)


We can write Ω **w** 1 _,_ **w** 2 = Ω **w** 1 _×_ Ω **w** 2. Notice that both Ω **w** 1 and Ω **w** 2 are convex sets. For any **w**[(] 1[0][)] _[,]_ **[w]**[(] 1[1][)] _∈_ Ω **w** 1 and **w**[(] 2[0][)] _[,]_ **[w]**[(] 2[1][)] _∈_ Ω **w** 2 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0071-05.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0071-06.png)


where **w**[(] 1 _[a]_[)] = _a_ **w** 1[(][0][)][+(][1] _[−][a]_[)] **[w]**[(] 1[1][)] _>_ **0** and **w**[(] 2 _[b]_[)] = _b_ **w**[(] 2[0][)][+(][1] _[−][b]_[)] **[w]**[(] 2[1][)] _>_ **0** , since the PD matrices form a convex cone. Or one can simply realize that the linear interpolation of any two connected graphs (of the same node set) is also connected. Since the direct product of convex sets is a convex set, we know that Ω **w** 1 _,_ **w** 2 is a convex set. 

Then, it remains to show that _Q_ ( **w** 1 _,_ **w** 2) is a convex function. Define 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0071-09.png)


Since there are bijections between Ω **L** , Ω **w** , and Ω **w** 1 _,_ **w** 2, from now on, we slightly abuse the notation of the objective function _Q_ and switch back-and-forth upon a suitable parameterization _Q_ ( **L** ), _Q_ ( **w** ), or _Q_ ( **w** 1 _,_ **w** 2). Now we know that _Q_ ( **w** ) is a strictly convex function of **w** , and **w** is an affine function of ( **w** 1 _,_ **w** 2). This implies that _Q_ ( **w** 1 _,_ **w** 2) is also a strictly convex function. Therefore, the global minimizer of _Q_ is unique. 

57 

## **3.5.4 Proof of Theorem 4: Consistency** 

_Proof._ Now we prove that the penalized MLE in (3.22) is asymptotically consistent. We use a different proof from (Ying et al., 2021) in spirit that better aligns with the popular route in literature (Rothman et al., 2008; Greenewald et al., 2019). Let **L** _[∗]_ be the Laplacian of the true Cartesian product graph to estimate and _L_ **w** _[∗]_ = **L** _[∗]_ . Let **L** _[∗]_ 1[and] **[ L]** _[∗]_ 2[be the true factor Laplacian,] where _L_ **w** _[∗]_[Correspondingly, we denote the minimizer of] 1[=] **[ L]** _[∗]_ 1[,] _[ L]_ **[ w]** _[∗]_ 2[=] **[ L]** _[∗]_ 2[, and] **[ L]** _[∗]_[=] **[ L]** _[∗]_ 1 _[⊕]_ **[L]** _[∗]_ 2[.] (3.22) as **L**[ˆ] = **L**[ˆ] 1 _⊕_ **L**[ˆ] 2, where **L**[ˆ] = _L[∗]_ **w** ˆ , **L**[ˆ] 1 = _L[∗]_ **w** ˆ 1, and **L**[ˆ] 2 = _L[∗]_ **w** ˆ 2. We begin with defining a set of perturbations around **L** _[∗]_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0072-02.png)


_sp_ log _p_ where _rn,_ **p** = ~~�~~ _n_ min( _p_ 1 _,p_ 2)[for] **[ p]**[ = (] _[p][,][ p]_[1] _[,][ p]_[2][)][ and] 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0072-04.png)


Define the following convex function over _T_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0072-06.png)


Our goal now is to show that 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0072-08.png)


To see the rationale behind (3.42), notice that 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0072-10.png)


58 

since **L**[ˆ] minimize _Q_ ( **L** ). Provided that _F_ (∆ **L** ) is a convex function, (3.42) ultimately implies that 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0073-01.png)


To prove this is true, we first prove the following 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0073-03.png)


By contradiction, suppose there exists a ∆ _[′]_ **L** _[∈][K]_ **[L]** _[∗]_[, such that] _[ ∥]_[∆] _[′]_ **L** _[∥] F[>][ cr][n][,]_ **[p]**[ and] _[ F]_[(][∆] **L** _[′]_[)] _[ <]_[ 0][.][Let] _θ_ = _crn,_ **p**[Then] _∥_ ∆ _[′]_ **L** _[∥] F[<]_[ 1.] 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0073-05.png)


This contradicts with (3.42) since _θ_ ∆ _[′]_ **L** _[∈][T]_[ .][Thus (3.44) must holds under (3.42).] Now we move forward to prove (3.42). We write out _F_ (∆ **L** ) 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0073-07.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0073-08.png)


Consider the Taylor’s expansion of logdet( **L** _[∗]_ + _ν_ ∆ **L** + **J** _p_ ) with the integral remainder 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0073-10.png)


and further the remainder 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0073-12.png)


59 

Therefore we have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0074-01.png)


where 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0074-03.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0074-04.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0074-05.png)


We now bound each term separately. 

## **Bound** _I_ 1 **:** 

We follow the argument in Ying et al. (2020) and assume that the graph signals are sampled from the process referred to as conditioning by Kriging (Rue and Held, 2005). This process first sample from the proper GMRF _**x** ∼ N_ ( **0** _,_ ( **L** _[∗]_ + **J** _p_ ) _[−]_[1] ), then correct these samples by subtracting their mean to make them DC-intrinsic 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0074-09.png)


Let **Σ** = ( **L** _[∗]_ + **J** _p_ ) _[−]_[1] be the covariance matrix of the original proper GMRF. Since ∆ **L** _∈ K_ **L** _∗_ , we have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0074-11.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0074-12.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0074-13.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0074-14.png)


60 

where ∆ **L** = ∆ **L** 1 _⊕_ ∆ **L** 2 and [ **Σ**[˜] 1] _i, j_ = _p_[1] 2[[] **[Σ]**[1][]] _i, j_[and][[] **[Σ]**[ ˜][2][]] _i, j_[=] _p_[1] 1[[] **[Σ]**[2][]] _i, j_[.] **[Σ]**[1][and] **[Σ]**[2][are][defined] similarly as in the Section 3.2.2. 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0075-01.png)


We then have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0075-03.png)


Here we focus on _L[∗]_ **S** 1, and results on _L[∗]_ **S** 2 can be derived similarly. Let _m_ 1 = _i − j_ +[1] 2[(] _[j][ −]_[1][)(][2] _[p]_[1] _[ −][j]_[)][.][We rewrite][ [] _[L][ ∗]_ **[S]**[˜][1][]] _m_ 1[into the quadratic form of the entries of] **[ x]** 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0075-05.png)


_p_ 1( _p_ 1 _−_ 1) where **e** _m_ 1 _∈_ R 2 has one in the _{i − j_ +[1] 2[(] _[j][ −]_[1][)(][2] _[p]_[1] _[ −][j]_[)] _[}]_[-th entry and zeros otherwise.] 1 Let **x** _k_ = **Σ** 2 **z** _k_ , where _**z** k ∼ N_ ( **0** _,_ **I** _p_ ) is the source signal of the GSP system. We then write the above quadratic as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0075-07.png)


1 1 Let **M** _i, j_ = **Σ** 2 ( _L_ **e** _m_ 1 _⊗_ **I** _p_ 2) **Σ** 2 . By the Hanson-Wright inequality Hanson and Wright (1971); 

61 

Rudelson and Vershynin (2013), we have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0076-01.png)


where _K_ = 2 is the sub-Gaussian norm of **z** _k_ . (3.66) holds by the properties of matrix norms and the trace inequalities (Fang et al., 1994) 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0076-03.png)


where _∥L_ **e** _m_ 1 _⊗_ **I** _p_ 2 _∥_[2] _F_[=][ 4] _[p]_[2][and] _[ ∥][L]_ **[ e]** _[m]_ 1 _[⊗]_ **[I]** _[p]_ 2 _[∥]_ 2[=] _[ ∥][L]_ **[ e]** _[m]_ 1 _[∥]_ 2[=][ 2][.][Let] _[ ε]_[=] ~~_√_~~ _p_ 2 _h∥_ **Σ** _∥_ 2[and plug] (3.64) into (3.67) 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0076-05.png)


62 

Meanwhile 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0077-01.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0077-02.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0077-03.png)


Therefore 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0077-05.png)


and we reach the following concentration result for _L[∗]_ **S**[˜] 1 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0077-07.png)


Similarly for _L[∗]_ **S**[˜] 2 we derive for _m_ 2 = _i − j_ +[1] 2[(] _[j][ −]_[1][)(][2] _[p]_[2] _[ −][j]_[)] 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0077-09.png)


63 

By the union bound 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0078-01.png)


By calculation we then have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0078-03.png)


So with the probability stated in (3.82), we derive the following lower bound for _I_ 1 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0078-05.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0078-06.png)


## **Bound** _I_ 2 **:** 

From the min-max theorem, we have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0078-09.png)


64 

Then given the convexity of _λ_ max( _·_ ) and concavity of _λ_ min( _·_ ) 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0079-01.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0079-02.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0079-03.png)


Then with _n_ sufficiently large 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0079-05.png)


such that _∥_ ∆ **L** _∥_ 2 _≤∥_ ∆ **L** _∥F ≤ λ_ max( **L** _[∗]_ + **J** _p_ ), we obtain a lower bound for _I_ 2 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0079-07.png)


## **Bound** _I_ 3 **:** 

To bound _I_ 3, we use triangular inequality 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0079-10.png)


65 

to obtain 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0080-01.png)


**Bound** _I_ 1 + _I_ 2 + _I_ 3 **:** 

So overall 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0080-04.png)


Let _ε_ = _c_ 2� lo _n_ g _p_ with sufficiently large 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0080-06.png)


so that _ε ≤_ 8 ~~�~~ min( _p_ 1 _, p_ 2). Then choose 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0080-08.png)


such that _ε∥_ **Σ** _∥_ 2 _−_ 2 _α_ ~~�~~ min( _p_ 1 _, p_ 2) _≤_ 0. Also note that 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0080-10.png)


66 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0081-00.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0081-01.png)


so long as _c_ is sufficiently large 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0081-03.png)


This holds with a probability at least 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0081-05.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0081-06.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0081-07.png)


where _c[′]_ = _[c]_[1] _[c]_ 2[2] _[γ][≥]_[1 here is a tuning parameter.][Setting] _[ γ]_[=][ 1 retrieves Theorem. 4.] 64 _[−]_[2.] 

Chapter 3, in full, is a reprint of the material as it appears in the Proceedings of The 27th International Conference on Artificial Intelligence and Statistics, Shi, Changhao; Mishne, Gal, 2024. The dissertation author was the primary investigator and author of this paper. 

67 

## **Chapter 4 Generalized Product Graph Learning** 

In Chapter 3, we have seen how the Cartesian graph product models a non-interactive, parallel composition of factor graphs and serves as the foundation of MWGSP (Stanley et al., 2020). However, other types of graph products are still under-explored in GSP. In this Chapter, we discuss another graph product that is also useful for modeling mode-wise dependencies, the Kronecker graph product. In Section 4.1, we introduce the Kronecker graph product and present its use case in GM and GSP. We then propose a penalized MLE to solve the Laplacian of Kronecker product graphs in Section 4.2 and investigate its theoretical properties in Section 4.3. Empirical results on synthetic and real-world datasets are shown in Section 4.4. 

## **4.1 Kronecker Structures** 

The Kronecker graph product is a powerful model to simulate realistic graphs (Leskovec et al., 2010). Figure 4.1 shows an example of the Kronecker graph product. Unlike the Cartesian 

**Figure 4.1.** An example of the Kronecker graph product. 

68 

product, the Kronecker product wires factor graphs recursively to create a hierarchy with selfsimilarity. This model is shown to be useful for mimicking the network characteristics, such as degree distributions of real-world graphs. These beneficial properties pose the Kronecker product graph as worthy candidates for modeling multi-dimensional structures in GSP (Sandryhaila and Moura, 2014). Subsequently, how to learn rigorous Kronecker product graphs from the data emerges naturally as an interesting problem. 

In this chapter, we study the problem of learning the Kronecker product graph Laplacian from smooth multi-dimensional data. GSP has a probabilistic interpretation using the language of graphical models (GM), and graph learning from smooth signals boils down to the parameter estimation of the improper Gaussian Markov random field (IGMRF). We follow a similar route and formulate our problem as the penalized MLE of an IGMRF with Kronecker product constraints. As the problem is not jointly convex, we propose an algorithm that alternates between the optimization of each factor graph. We also provide theoretical results for the asymptotic convergence of the alternating algorithm, showing an improved convergence rate compared to when the product structure is not accounted for. Given that the strong graph product also bears a similar Kronecker product form, we also propose a variant of our algorithm to learn strong product graphs from smooth signals. We conduct experiments on synthetic and real-world graphs and demonstrate our approach’s efficacy and superior performance compared to existing methods. The connections and differences between our method and related GSP and GM methods will also be discussed. To summarize our contributions: 

- We are the first to consider the penalized MLE of Kronecker product graph Laplacian learning, and gain theoretical results on its asymptotic consistency, to the best of our knowledge. 

- We propose a new algorithm to solve the penalized MLE and a variant of it to solve strong product graph Laplacian learning. 

- We demonstrate that our approach outperforms existing GSP and GM methods on synthetic 

69 

## and real-world datasets. 

## **Related Work** 

Previous work mainly focuses on Cartesian product graphs Lodhi and Bajwa (2020); Kadambari and Prabhakar Chepuri (2020); Kadambari and Chepuri (2021); Einizade and Sardouie (2023); few have studied other products such as the Kronecker (Lodhi and Bajwa, 2020; Einizade and Sardouie, 2023). Lodhi and Bajwa (2020) proposed to learn the factor graphs under the trace constraints; Einizade and Sardouie (2023) posited that an accurate eigenbasis estimation of the factor graph shift operator (GSO) is known and solved for the eigenvalues. However, these methods either do not learn the combinatorial graph Laplacian, or fall short on their theoretical properties. 

The matrix variate normal distribution (Dawid, 1981; Gupta and Nagar, 1999) can be seen as a generalization of the GMRF to multi-way signals. The covariance matrices, and thus the precision matrices, are endowed with a Kronecker product structure, and the graphical lasso algorithm has been extended to learn these Kronecker graphical models (Dutilleul, 1999; Werner et al., 2008; Zhang and Schneider, 2010; Leng and Tang, 2012; Tsiligkaridis et al., 2013). Other matrix variate distributions replace the Kronecker product structure with the Kronecker sum (Kalaitzis et al., 2013; Greenewald et al., 2019; Wang et al., 2020b; Yoon and Kim, 2022), leading to Cartesian product graphs. While these graphical lasso methods bear a similar form to the Kronecker product graph Laplacian learning, none of these learn precision matrices under Laplacian constraints, and therefore the covariance matrices that are learned are not appropriate for use in GSP. 

## **4.2 Generalized Inference of Product Graphs** 

## **4.2.1 MLE** 

Let the random matrix _**X** ∈_ R _[p]_[1] _[×][p]_[2] represent a two-way graph signal that lives on the product graph _G_ . [ _**X**_ ] _i_ 1 _,i_ 2 is the signal on node ( _i_ 1 _, i_ 2). Given _n_ instantiations _{_ **X** 1 _,_ **X** 2 _,...,_ **X** _n}_ , 

70 

our goal is to learn the factor graphs _G_ 1 _, G_ 2 and their Kronecker product _G_ from these nodal observations on _G_ . Note that our argument can be generalized to more factors naturally, though not presented here. 

Let the random vector _**x**_ be the vectorization of _**X**_ and **S** =[1] _n_[∑] _k[n]_ =1 **[x]** _[k]_ **[x]** _[kT]_[be the SCM.] Since for _G_ = _G_ 1 _×G_ 2 we have **A** = **A** 1 _⊗_ **A** 2, we derive the non-penalized product graph learning objective 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0085-02.png)


It is worth to emphasize that **L** _̸_ = **L** 1 _⊗_ **L** 2 and thus logdet[†] ( **L** ) _̸_ = logdet[†] ( **L** 1)+logdet[†] ( **L** 2). This makes our problem substantially different from the MLE of matrix normal distributions (Dutilleul, 1999). Interestingly, except for the GSP merits, the Laplacian constraints also endow total positivity (Lauritzen et al., 2019), a GM property that is not compatible with other Kronecker structured distributions. 

## **4.2.2 Kronecker Structured Graph Learning** 

We propose the **K** ronecker **S** ructured **G** raph (Laplacian) **L** earning ( **KSGL** ) algorithm for solving (4.1). We formulate the penalized MLE (4.1) as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0085-06.png)


with _ℓ_ 1 penalization. Here **K** = _A L[∗]_ **S** denotes the pairwise square Euclidean distances of the signals. The absolute sign of the _ℓ_ 1 norm of the sparsity penalty is redundant due to the non-negative constraints. KSGL then operates in an alternating scheme to solve **w** 1 and **w** 2. The algorithm starts with initialization **w** 1 =[1] _[p]_[1][(] _[p]_[1] _[−]_[1][)] and **w** 2 =[1] _[p]_[2][(] _[p]_[2] _[−]_[1][)] . It then uses projected _p_ 1 **[1]** _p_ 2 **[1]** 2 2 gradient descent to solve for one variable while keeping the other fixed until the stopping criteria 

71 

## **Algorithm 4.** KSGL 

**Input:** graph signals _{_ **X** _k}_ , parameters _α, η_ Compute **S** and **K** . Initialize **w** 1 and **w** 2. **repeat repeat** Update **w** 1 as in: (4.3) for the Kronecker product or (4.6) for the strong product **until** convergence. **repeat** Update **w** 2 as in: (4.4) for the Kronecker product or (4.7) for the strong product **until w** 2 convergence. **until w** 1 and **w** 2 converge or maximum iterations. **Output:** factor graph weights **w** 1 _,_ **w** 2 

are met. The update of **w** 1 and **w** 2 is given by 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0086-03.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0086-04.png)


Here _m_ 1 = _i − j_ +[1] 2[(] _[j][ −]_[1][)(][2] _[p]_[1] _[ −][j]_[)][and] _[m]_[2][=] _[ i][ −][j]_[ +][1] 2[(] _[j][ −]_[1][)(][2] _[p]_[2] _[ −][j]_[)][.][The][subsets] _[I]_[1][=] _{_ ( _i −_ 1) _p_ 2 + 1 _,_ ( _i −_ 1) _p_ 2 + 2 _,..., ip_ 2 _}_ and _J_ 1 = _{_ ( _j −_ 1) _p_ 2 + 1 _,_ ( _j −_ 1) _p_ 2 + 2 _,..., jp_ 2 _}_ specify node pairs associated with [ **w** 1] _m_ 1, and similarly for the subsets _I_ 2 = _{i, p_ 2 + _i,...,_ ( _p_ 1 _−_ 1) _p_ 2 + _i}_ and _J_ 2 = _{ j, p_ 2 + _j,...,_ ( _p_ 1 _−_ 1) _p_ 2 + _j}_ . Alg. 4 summarizes the algorithm. 

72 

## **4.2.3 Connection to Strong Product Graphs** 

An alternative graph product with broad applications is the strong graph product. We now demonstrate how the strong product relates to the Kronecker product and how we can easily modify KSGL to learn strong product graphs. For factor graphs _G_ 1 and _G_ 2, consider adding self-loops to them and then taking the Kronecker product. The new product graph is also self-looped and its weighted adjacency matrix is ( **W** 1 + **I** _p_ 1) _⊗_ ( **W** 2 + **I** _p_ 2) = **W** 1 _⊗_ **W** 2 + **W** 1 _⊗_ **I** _p_ 2 + **I** _p_ 1 _⊗_ **W** 2 + **I** _p_ = ( **W** 1 _⊗_ **W** 2 + **W** 1 _⊕_ **W** 2)+ **I** _p_ . Removing the self-loops, we obtain exactly the strong product of _G_ 1 and _G_ 2. This relation helps us formulate the penalized MLE for learning strong product graphs based on (4.2) 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0087-02.png)


Here we plug in the self-looped strong product adjacency matrix since the pairwise distances are all 0 on the **K** diagonal and _A[∗]_ is also agnostic to its input diagonal values. Similarly, we use projected gradient descent to solve for **w** 1 or **w** 2 and then alternate between these two steps. The update of **w** 1 and **w** 2 is 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0087-04.png)


73 

## **4.3 Theoretical Results** 

Here we establish the statistical consistency and convergence rates for the penalized Kronecker product graph Laplacian estimator as in (4.2). We first make assumptions regarding the true underlying graph we were to estimate: 

- (A1) Let _S_ 1 and _S_ 2 be the support set of the true factor graphs. We assume the graphs are sparse and the cardinality of their supports is upper bounded by _|S_ 1 _| ≤ s_ 1 _p_ 1 and _|S_ 2 _| ≤ s_ 2 _p_ 2. 

- (A2) Let ( _d_ 1 _,_ min _, d_ 1 _,_ max) and ( _d_ 2 _,_ min _, d_ 2 _,_ max) be the minimum and maximum degrees of the true factor graphs. We assume these degrees are bounded away from 0 and ∞ by a constant _d >_ 1, such that _d_[1] _[≤][d]_[1] _[,]_[min] _[ ≤][d]_[1] _[,]_[max] _[ ≤][d]_[and] _d_[1] _[≤][d]_[2] _[,]_[min] _[ ≤][d]_[2] _[,]_[max] _[ ≤][d]_[.] 

- (A3) Let _{_ 0 _, λ_ 2 _,..., λp}_ be the eigenvalues of the true product graph Laplacian in a nondecreasing order. We assume these eigenvalues are bounded away from 0 and ∞ by a constant _z >_ 1, such that[1] _z[≤][λ]_[2] _[ <][ λ][p][ ≤][z]_[.] 

These assumptions are common in high-dimensional statistics. They also imply that the product and factor graphs are connected graphs. With the above assumptions, our first theorem states that a solution to the MLE problem always exists. Proofs of all the theorems can be found in the supplement. 

**Theorem 6** (Existence of MLE) **.** _The penalized negative log-likelihood of Kronecker product graph Laplacian learning as in_ (4.2) _is lower-bounded, and there exists at least one global minimizer as the solution of the penalized MLE._ 

Our proof largely follows (Ying et al., 2021; Shi and Mishne, 2023), which shows that the objective function is lower-bounded and the minimizer is achievable. However, note that since the original problem is not jointly convex, the solution is not unique. In fact, a set of solution ( **w** _[∗]_ 1 _[,]_ **[w]** _[∗]_ 2[)][ is not identifiable to the Kronecker graph product] _[ A]_ **[ w]**[1] _[ ⊗][A]_ **[ w]**[2][ since] _[ ∀][a][ >]_[ 0] _[,][a]_ **[w]** _[∗]_ 1 _[,]_[1] _a_ **[w]** 2 _[∗]_ 

74 

is also a solution. Nevertheless, our Theorem 7 states that the alternating optimization enjoys a unique solution in each sub-problem. 

**Theorem 7** (Uniqueness of MLE) **.** _The objective function of the penalized MLE is bi-convex with respect to each factor graph, and a global minimizer for each sub-problem uniquely exists._ 

The proof shows that when one of the factors is held fixed, optimizing the other factor becomes a convex problem. We then show that the Kronecker product graph Laplacian learned by KSGL is asymptotically consistent. 

**Theorem 8** (High-dimensional consistency) **.** _Suppose assumptions (A1), (A2), and (A3) hold for the true factor graphs and the initialization. Then with sufficiently large n and proper penalty α_ 1 _and α_ 2 _, the minimizer_ **L**[�] = _L_ ( **w** �) _of the penalized MLE as in_ (4.2) _is asymptotically consistent to the true Laplacian_ **L** _[∗] , and the Frobenius error is bounded by_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0089-04.png)


_with high probability._ 

The main idea is to prove that the solution of a sub-problem converges to the ground truth when the other factor is bounded. With a good initialization, induction shows that the product graph converges at a desirable rate. The final error depends on how close the initialization is to the ground truth. Theorem 8 shows that the learned product graph Laplacian converges to the true Laplacian asymptotically under mild conditions. Compared with the Laplacian GMRF convergence rate from (Ying et al., 2021), Kronecker product graph learning converges faster by a factor of _p_ 1 _p_ 2[This shows how leveraging the product structure] ~~�~~ _p_ 1+ _p_ 2[with similar probability.] prior benefits graph learning. The improvement of the convergence rate is similar to the ones in (Tsiligkaridis et al., 2013). 

75 

## **4.4 Experiments** 

We conduct extensive experiments on both synthetic and real-world datasets to evaluate 

our method. See the supplement for more details. 

## **4.4.1 Synthetic Graphs** 

**Figure 4.2.** Comparison of different methods on various synthetic Kronecker product graphs and signals. Each sub-figure shows the trend of Rel-Err of the product (top row) or factor (middle and bottom rows) Laplacian matrices as _n_ increases. Black dash lines fit the theory in (4.8) to the KSGL results. 

Since the ground truth graphs are often unavailable or not defined in real-world problems, we first evaluate our methods on synthetic signals where the underlying graph to be estimated is 

known. We follow Section 3.4 to generate factor graphs using the graph models below 

- (1) Erd˝os-R´enyi model with probability _p_ = 0 _._ 3; 

- (2) Barab´asi-Albert model with preferential attachment _m_ = 2 and _m_ 0 = 2 initial nodes; 

76 

**Figure 4.3.** Comparison of different methods on various synthetic Kronecker product graphs and signals. Each sub-figure shows the trend of PR-AUC of the product or factor edge prediction as _n_ increases. 

- (3) Watts-Strogatz small-world model, where a chain graph with node degree _d_ = 2 is rewired with probability _p_ = 0 _._ 1; 

## (4) and regular grids. 

We set the number of nodes to _p_ 1 = 20 and _p_ 2 = 25 for each factor, and the dimensions of regular grids are 4 _×_ 5 and 5 _×_ 5. To obtain weighted graphs, we randomly sample a weight from a uniform distribution _U_ (0 _._ 1 _,_ 2) for each edge. We then generate the signals from the IGMRF process _**f** ∼ N_ ( **0** _,_ **L**[†] ), where **L** is the Laplacian of the Kronecker product graph. To evaluate KSGL on the strong product, we also generate signals from strong product graphs **W** = **W** 1 _⊗_ **W** 2 + **W** 1 _⊕_ **W** 2. The goal of graph learning is to recover the underlying weighted graphs from the signals, where the number of the signals varies _n_ = 10 _×_ 2ˆ _{_ 0 _,_ 1 _,...,_ 10 _}_ . 

We create 50 realizations for each graph and dataset size and report the mean and standard deviation of the selected metrics: the relative error (Rel-Err) of the Laplacian and the area under 

77 

the precision-recall curve (PR-AUC) of edge prediction. The former Rel-Err computes the relative Frobenius error of the learned factor and product graph Laplacian matrices to their ground truth counterparts. To eliminate the ambiguity of the learned factor graphs, we normalize the graph Laplacian matrices by their cardinality Tr _p_ ( **LL** )[before computing the relative error.][The] latter PR-AUC considers the binary prediction of the ground truth edge patterns. We choose PR-AUC over ROC-AUC since the two classes are highly imbalanced (edge versus no edge). 

We evaluate KSGL against three competing methods that model the Kronecker structures: the PST (Product Spectral Template) method (Einizade and Sardouie, 2023), the FF (Flip-Flop) method (Dutilleul, 1999), and the Kronecker Graphical Lasso (KGLasso) method (Tsiligkaridis et al., 2013). PST is a GSP method that extracts the eigenvectors of factor GSOs from the signal covariance. FF solves the MLE of matrix normal distributions and KGLasso adds sparsity constraints to that, both of which fall into the GM category. For the strong product experiments, since the strong graph product is the union of the Kronecker and Cartesian graph product, we add Cartesian product graph learning methods for comparison: the PGL (Product Graph Learning) method (Kadambari and Chepuri, 2021), the TeraLasso (Tensor Graphical Lasso) method (Greenewald et al., 2019), and the MWGL method in the previous section. We follow the common grid-search procedure in each setting to select the best-performing hyper-parameters for each method. 

Figure 4.2 and Figure 4.3 shows the trend of Rel-Err and PR-AUC as the number of signals increases in different settings. As we can see, KSGL outperforms the competing methods in every setting. The Rel-Err of KSGL converges to 0 as the number of signals increases and its trend validates our theoretical results (black dash lines, top row). PST does not perform well because the spectral templates cannot be estimated accurately but only roughly approximated even with a large number of signals (see more details in the supplement). FF and KGLasso also underperform KSGL because of the inherent model mismatch, which is that the Laplacian of a Kronecker product graph is not the Kronecker product of the factor Laplacians. Another reason is that the precision matrices learned by FF and KGLasso are not Laplacian. Their 

78 

**Figure 4.4.** Comparison of different methods on various synthetic strong product graphs and signals. Each sub-figure shows the trend of Rel-Err as _n_ increases. Black dash lines fit the theory in (4.8) to our results. 

similar performance also shows that adding sparsity constraints to the problem does not benefit performance. 

Figure 4.4 and Figure 4.5 show the Rel-Err and PR-AUC results of strong product graph learning. Again KSGL behaves advantageously in almost every setting. The only exception is that PGL performs better in low data regimes on Erdos-R˝ enyi and Watts-Strogatz small-world´ graphs, but it fails to deliver as the number of signals increases due to the model mismatch. Among other competing methods, TeraLasso and MWGL perform the best overall, but they still fall behind KSGL by a margin. 

## **4.4.2 EEG Data** 

We now evaluate KSGL on real EEG recordings (Nasreddine, 2021). The EEG data are collected from epileptic patients using the 10-20 electrode system. The signals from 21 scalp electrodes are divided into 1-second segments, and we sub-sample the signals to get 50 

79 

**Figure 4.5.** Comparison of different methods on various synthetic strong product graphs and signals. Each sub-figure shows the trend of PR-AUC of the product or factor edge prediction as _n_ increases. 

samples per segment. Each segment is also annotated with a class label, indicating if the patient is undergoing a seizure and further which type of seizure it is. This results in 21 _×_ 50 multi-way signals of different categories from multiple patients. Our goal is to learn a graph of brain region (electrodes) and a graph of time from these multi-way signals. 

Because brain connectivity varies dramatically across individuals, we pick the EEG of a single patient to evaluate KSGL. This 7-year-old male patient had several complex partial seizures in the central cortical area (Cz, C3, C4), but also went through multiple seizures that are not visible on EEG. We apply KSGL to learn strong product graphs from his normal EEG and deceptive epileptic EEG. Figure 4.6 and 4.7 show the electrode graphs and time graphs learned by KSGL. Although the seizures are not obvious from the mean signal amplitude as expected, KSGL learns different connectivity patterns for these 2 statuses. In specific, KSGL learns denser connectivity around the central cortical area, matching the known lesion. The learned time graphs also show distinct patterns - the epileptic signals are more knitted than the 

80 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0095-00.png)


**----- Start of picture text -----**<br>
(a)  Normal (b)  Seizure<br>**----- End of picture text -----**<br>


**Figure 4.6.** The brain connectivity inferred by KSGL. Electrodes are placed by the 10-20 system. The background color shows the mean activity of each status. 

**(a)** Normal **(b)** Seizure 

**Figure 4.7.** The time graphs of the epileptic signals inferred by KSGL. 

normal signals. 

For the second part, we select another type of patient whose seizures are visible on the EEG. These patients all suffer from complex partial seizures, and we apply KSGL to their normal and epileptic EEG signals. Figure 4.8 shows the node degree distributions of the learned brain graphs. We observe that KSGL learns denser connectivity from the normal EEG and sparser connectivity from the abnormal EEG, and this pattern is consistent across all four patients. 

81 

**Figure 4.8.** Degree distributions of the learned brain graphs from normal and epileptic EEG of different patients. The red vertical lines indicate the average node degree of the distributions. 

## **4.5 Proofs of Theoretical Results** 

## **4.5.1 Proof of Theorem 6: Existence** 

_Proof._ Given _A_ **w** = _A_ **w** 1 _⊗ A_ **w** 2, we now prove that the global minimizer of the penalized MLE 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0096-04.png)


exists. Provided that both the product and factor graphs are connected, The feasible set over **w** 1 and **w** 2 is defined as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0096-06.png)


where **J** _p_ =[1] _p_ **[1]** _[p]_ **[1]** _[T] p_[and we have][ logdet][†][(] _[L]_ **[ w]**[) =][ logdet][(] _[L]_ **[ w]**[+] **[J]** _[p]_[)][. The conditions] _[ L]_ **[ w]**[1][+] **[J]** _[p]_ 1 _[∈]_ S++ _[p]_[1][and] _[ L]_ **[ w]**[2][+] **[J]** _[p]_ 2 _[∈]_[S] ++ _[p]_[2][constrain that] _[ G]_[1][and] _[ G]_[2][are connected.][Let] _[ {]_[0][ =] _[ λ]_[1] _[<][ λ]_[2] _[≤··· ≤] λp}_ be the eigenvalues of **L** = _L_ **w** . We first consider the original MLE and bound the negative 

82 

log-likelihood _Q_ ( **w** 1 _,_ **w** 2) when _α_ 1 = _α_ 2 = 0 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0097-01.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0097-02.png)


where [ **S**[˜] ] _i, j_ =[1] _p_[[] **[S]**[]] _i, j_[.][(4.14)][ is attributed to the fact that the summation of eigenvalues equals] the trace of the Laplacian. Define the function 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0097-04.png)


_p−_ 1 This function is lower-bounded at _t_ =[Therefore, we have] min( _L[∗]_ **S**[˜] )[, so long as][ min][(] _[L][ ∗]_ **[S]**[˜][)] _[ >]_[ 0][.] that the negative log-likelihood is also lower-bounded 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0097-06.png)


We then notice that _q_ ( _t_ ) _→_ ∞ when _t →_ ∞. This is followed by _Q_ ( **w** 1 _,_ **w** 2) being coercive. 

Now consider the penalized MLE. When the penalization _α_ 1 _>_ 0 and _α_ 2 _>_ 0, the penalized MLE _Q_ ( **w** 1 _,_ **w** 2) is still lower-bounded. Since 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0097-09.png)


the penalized MLE _Q_ ( **w** 1 _,_ **w** 2) is also coercive. Note that this only holds when we penalize the factor graphs. The penalized MLE wouldn’t be coercive if the _ℓ_ -1 penalization is on the product 

83 

graph. 

The above argument indicates that a global minimizer exists in cl(Ω **w** 1 _,_ **w** 2), and now we show that it exist in Ω **w** 1 _,_ **w** 2. Since the open boundaries cl(Ω **w** 1 _,_ **w** 2) _\_ Ω **w** 1 _,_ **w** 2 are results of the connectivity constraint _L_ **w** 1 + **J** _p_ 1 _≻_ **O** and _L_ **w** 2 + **J** _p_ 2 _≻_ **O** , we have that cl(Ω **w** 1 _,_ **w** 2) _\_ Ω **w** 1 _,_ **w** 2 is a subset of disconnected **w** 1 and **w** 2. The set of disconnected **w** 1 and **w** 2 is written as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0098-02.png)


For the Kronecker product, any factor graph being disconnected leads to the product graph being disconnected. Therefore, 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0098-04.png)


This shows that any global minimizer over cl(Ω **w** 1 _,_ **w** 2) do not lie on those open boundaries, therefore (4.9) has at least a global minimizer in Ω **w** 1 _,_ **w** 2 so long as min( _L[∗]_ **S**[˜] ) _>_ 0, which almost surely holds with probability 1. 

## **4.5.2 Proof of Theorem 7: Uniqueness** 

_Proof. Q_ ( **w** 1 _,_ **w** 2) is not jointly convex on **w** 1 and **w** 2, but it is bi-convex with respect to each separate variable. This means the MLE objective is convex with respect to **w** 1 when **w** 2 is fixed, and also convex with respect to **w** 2 when **w** 1 is fixed. Define the feasible set of **w** 1 and **w** 2 as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0098-08.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0098-09.png)


84 

and we have Ω **w** 1 _,_ **w** 2 = Ω **w** 1 _×_ Ω **w** 2. To see that both Ω **w** 1 and Ω **w** 2 are convex sets, we check that _∀_ **w**[0] 1 _[,]_ **[w]** 1[1] _[∈]_[Ω] **[w]** 1[and] _[ ∀]_ **[w]**[0] 2 _[,]_ **[w]** 2[1] _[∈]_[Ω] **[w]** 2 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0099-01.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0099-02.png)


where **w** _[a]_[The set of positive definite] 1[=] _[ a]_ **[w]**[0] 1[+(][1] _[−][a]_[)] **[w]** 1[1] _[>]_ **[ 0]**[ and] **[ w]** _[b]_ 2[=] _[ b]_ **[w]**[0] 2[+(][1] _[−][b]_[)] **[w]** 2[1] _[>]_ **[ 0]**[.] matrices forms a convex cone. 

Now to prove _Q_ ( **w** 1 _,_ **w** 2) is bi-convex, we again first consider the case where _α_ 1 = _α_ 2 = 0. The negative log-likelihood (4.11) is convex with respect to **w** . Because either **w** 1 or **w** 2 maps linearly to **w** when the other factor is fixed, (4.11) is bi-convex. The penalized MLE is then also bi-convex because both _α_ 1 _∥_ **w** 1 _∥_ 1 and _α_ 2 _∥_ **w** 2 _∥_ 1 are convex. Thus each sub-problem of the penalized MLE has a unique solution. 

## **4.5.3 Proof of Theorem 8: Consistency** 

_Proof._ We prove that the Kronecker product graphs learned by the alternating algorithm converge to the ground truth asymptotically. Let **L** _[∗]_ be the Laplacian of the true Kronecker product graph to be estimated and _L_ **w** _[∗]_ = **L** _[∗]_ . By the properties of Kronecker graph product, **L** _[∗]_ = **D** _[∗] −_ **W** _[∗]_ = **D** _[∗]_[Let] **[L]** _[∗]_ **[L]** _[∗]_[the][true][factor][Laplacian,][where] _[L]_ **[ w]** _[∗]_ 1 _[⊗]_ **[D]** _[∗]_ 2 _[−]_ **[W]** _[∗]_ 1 _[⊗]_ **[W]** _[∗]_ 2[.] 1[and] 2[be] 1[=] **[ L]** _[∗]_ 1[and] _L_ **w** _[∗]_[Although the factor Laplacians do not appear in the original problem formulation,] 2[=] **[ L]** _[∗]_ 2[.] they come in handy for deriving the consistency results. 

The algorithm starts with fixing **w** 2 = **w**[init] 2 and updating **w** 1. Let’s define a set of perturbations around **L** _[∗]_ 1 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0099-08.png)


85 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0100-00.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0100-01.png)


If we can show that 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0100-03.png)


then we will have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0100-05.png)


following that _Q_ ( **L** 1 _,_ **L** 2) is bi-convex, _F_ ( **O** 1) = 0, and _F_ ( **L**[�] 1 _−_ **L** _[∗]_ 1[) =] _[ Q]_[(] **[L]**[�][1] _[,]_ **[L]**[init] 2[)] _[−][Q]_[(] **[L]** 1 _[∗][,]_ **[L]**[init] 2[)] _[ ≤]_ 0. 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0100-07.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0100-08.png)


Using Taylor’s expansion of logdet( **L** _[∗]_ + _ν_ ∆ **L** + **J** _p_ ) with the integral remainder 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0100-10.png)


and further the remainder 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0100-12.png)


86 

Therefore we have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0101-01.png)


where 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0101-03.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0101-04.png)


## **Bound** _I_ 1 **:** 

The observations **x** ¯ are the samples from the improper GMRF (Ying et al., 2020) 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0101-07.png)


Let **Σ** = ( **L** _[∗]_ + **J** _p_ ) _[−]_[1] be the covariance matrix of the original proper GMRF. Let _m_ 1 = _i − j_ + 1 _[∀]_[1] _[ ≤][j][ <][ i][ ≤][p]_[ and] _[ L]_[ ∆] **[w]**[ =][ ∆] **[L]**[, we have] 2[(] _[j][ −]_[1][)(][2] _[p]_[1] _[ −][j]_[)] _[,]_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0101-09.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0101-10.png)


87 

_p_ 1( _p_ 1 _−_ 1) where **e** _m_ 1 _∈_ R 2 has 1 in the _m_ 1-th entry and 0s otherwise. Also, notice that 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0102-01.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0102-02.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0102-03.png)


which leads to 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0102-05.png)


Therefore, 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0102-07.png)


1 Now we bound the perturbation term. Let **x** _k_ = **Σ** 2 **z** _k_ , where **z** _k ∼ N_ ( **0** _,_ **I** _p_ ) is the source signal of the GSP system. From (4.39) we know 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0102-09.png)


88 

1 1 Let **M** _i, j_ = **Σ** 2 ( _L A[∗]_ ( _A_ **e** _m_ 1 _⊗_ **W**[init] 2[))] **[Σ]** 2 . We then apply the Hanson-Wright inequality (Hanson and Wright, 1971; Rudelson and Vershynin, 2013) to the quadratic 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0103-01.png)


where from (4.53) to (4.54) we use 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0103-03.png)


_h_ and from (4.54) to (4.55) we use _K ≤_ 2 for the sub-Gaussian norm of **z** _k_ . Let _ε_ = _∥L_ **w**[init] 2 _[∥] F[∥]_ **[Σ]** _[∥]_ 2 and plug (4.50) into (4.55), we arrive at 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0103-05.png)


The union bound indicates that 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0103-07.png)


89 

so 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0104-01.png)


Thus with the above probability and _ε ≤_ 4 _√_ 2 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0104-03.png)


## **Bound** _I_ 2 **:** 

From the min-max theorem, we have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0104-06.png)


Then given the convexity of _λ_ max( _·_ ) and concavity of _λ_ min( _·_ ) 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0104-08.png)


90 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0105-00.png)


Let **d** 1 denotes the diagonal of **D** 1. The Gershgorin circle theorem implies that 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0105-02.png)


Then with _n_ sufficiently large _n ≥_ 4 _c_[2] _pd_ 22[2] _∥,_ max **L** _[∗]_ + _[s]_[1] **J** _[p] p_[1] _∥_[ log][2] 2 _[ p]_ such that _∥_ ∆ **L** _∥_ 2 _≤_ 2 _cd_ 2 _,_ max _rn,_ **p** _≤∥_ **L** _[∗]_ + **J** _p∥_ 2, we obtain 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0105-04.png)


To factor ∆ **L** 1 out, note that 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0105-06.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0105-07.png)


and that _∥_ **W**[init] 2 _[∥]_[is lower and upper bounded] 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0105-09.png)


Thus 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0105-11.png)


91 

**Bound** _I_ 3 **:** 

With triangle inequality 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0106-02.png)


we can lower-bound _I_ 3 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0106-04.png)


**Bound** _I_ 1 + _I_ 2 + _I_ 3 **:** 

Overall, 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0106-07.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0106-08.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0106-09.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0106-10.png)


so that _ε ≤_ 4 ~~_√_~~ 2 is satisfied. Then choose 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0106-12.png)


92 

so that _ε_ ~~_[√]_~~ _p_ 2 _∥L_ **w** 2 _∥_ 2 _∥_ **Σ** _∥_ 2 _−_ 2 _α <_ 0 and 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0107-01.png)


We can also bound _∥_ ∆ **w** 1 _∥_ 1 _,A_ 1 by 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0107-03.png)


Now, to prove _F_ (∆ **L** 1) _≥_ 0, define a ratio factor _γ_ 1 _≥_ 1 that controls the _ℓ_ 1 penalty _[α] γ_ 1[1][=] _c[′′]_ 1 _[∥][L]_ **[ w]**[init] 2 _[∥]_ 2 _[∥]_ **[Σ]** _[∥]_ 2 _p_ 2 log _p_ . We obtain 2 ~~�~~ _n_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0107-05.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0107-06.png)


for sufficiently large _c_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0107-08.png)


93 

This happens with probability 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0108-01.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0108-02.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0108-03.png)


We have proved that the **w** 1 estimation is consistent when fixing **w** 2. 

Now we move forward to prove the consistency of **w** 2 when fixing **w** � 1 = **w**[(] 1[1][)][.][Similarly,] we aim to show 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0108-06.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0108-07.png)


where _rn,_ **p** = ~~�~~ _s_ 2 _pnp_ 2 lo1g _p_ . By symmetry, with high probability, for _ε_ = _c[′′]_ 2 ~~�~~ lo _n_ g _p_ and _n ≥[c]_ 2 _[′′]_[2] 32[lo][g] _[p]_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0108-09.png)


where ∆ **L** = **D**[(] 1[1][)] _[⊗]_[∆] **[D]** 2 _[−]_ **[W]**[(] 1[1][)] _[⊗]_[∆] **[W]** 2[.][Different from the previous derivation,] **[ L]**[(] 1[1][)] and **W**[(] 1[1][)] are 

94 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0109-00.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0109-01.png)


Then, let _d_ 1[(][1] _,_ max[)][be the maximum degree of] **[ W]**[(] 1[1][)][, by the Gershgorin circle theorem] 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0109-03.png)


Similar to (4.86), we choose a large enough _α_ 2 with a ratio factor _γ_ 2 _≥_ 1 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0109-05.png)


Similar to (4.78) and (4.88), we have 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0109-07.png)


and 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0109-09.png)


95 

Plugging in _ε_ = _c[′′]_ 2 ~~�~~ lo _n_ g _p_[, (4.104), (4.105), and (4.106), we obtain] 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0110-01.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0110-02.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0110-03.png)


for sufficiently large _n_ 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0110-05.png)


and _c_ 2 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0110-07.png)


where 0 _< ζ <_ 1 and 0 _< ι_ are additional ratio factors. We have now proved that the second iteration of the alternating optimization is consistent. With induction, one can show that 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0110-09.png)



![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0110-10.png)


96 

Finally, to show the convergence of the product graphs, we decompose the error as 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0111-01.png)


from which we obtain 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0111-03.png)


Here again for _κ_ the ratio factor 

and 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0111-06.png)


Since the above also holds for _∥_ ∆ **W** (2 _t_ +1) _∥F_ , we have proved 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0111-08.png)


with a high probability for sufficiently large _n_ . 

97 

Chapter 4, in full, has been prepared for publication, Shi, Changhao; Mishne, Gal. The dissertation author was the primary investigator and author of this paper. 

98 

## **Chapter 5 Signal Denoising against Off-Manifold Adversarial Attacks** 

In the remaining chapters, we shift gears from traditional statistical models to modern deep learning models. Classical graph inference is useful for learning the geometry of data, but it is not competent for complex datasets such as natural images. We hypothesize that deep learning captures the manifold of complex data, and verify this hypothesis via a prominent task in deep learning: defending against adversarial attacks. In Section 5.1, we first introduce the concepts of adversarial robustness and how we conjecture the manifold assumption helps improve the robustness of deep neural networks. We then present a framework for adversarial purification, i.e. pulling off-manifold adversarial examples back to the clean data manifold, in Section 5.2, leveraging tools of self-supervised learning. Our hypothesis is empirically verified in Section 5.3. 

## **5.1 Manifold Assumption and Adversarial Robustness** 

Deep neural networks have achieved remarkable results in many machine learning applications. However, these networks are known to be vulnerable to adversarial attacks, i.e. strategies that aim to find adversarial examples that are close or even perceptually indistinguishable from their natural counterparts but easily misclassified by the networks. This vulnerability raises theory-wise issues about the interpretability of deep learning as well as application-wise issues when deploying neural networks in security-sensitive applications. 

99 

Many strategies have been proposed to empower neural networks to defend against these adversaries. The current most widely used genre of defense strategies is adversarial training. Adversarial training is an on-the-fly data augmentation method that improves robustness by training the network not only with clean examples but adversarial ones as well. For example, Madry et al. (2017) propose projected gradient descent as a universal first-order attack and strengthen the network by presenting it with such adversarial examples during training (e.g., adversarial training). However, this method is computationally expensive as finding these adversarial examples involves sample-wise gradient computation at every epoch. 

Self-supervised representation learning aims to learn meaningful representations of unlabeled data where the supervision comes from the data itself. While this seems orthogonal to the study of adversarial vulnerability, recent works use representation learning as a lens to understand as well as improve adversarial robustness (Hendrycks et al., 2019; Mao et al., 2019; Chen et al., 2020b; Naseer et al., 2020). This recent line of research suggests that self-supervised learning, which often leads to a more informative and meaningful data representation, can benefit the robustness of deep networks. 

In this chapter, we study how self-supervised representation learning can improve adversarial robustness. We present Self-supervised Online Adversarial Purification (SOAP), a novel defense strategy that uses an auxiliary self-supervised loss to purify adversarial examples at test-time, as illustrated in Figure 5.1. During training, besides the classification task, we jointly train the network on a carefully selected self-supervised task. The multi-task learning improves the robustness of the network and more importantly, enables us to counter the adversarial perturbation at test-time by leveraging the label-independent nature of self-supervised signals. Experiments demonstrate that SOAP performs competitively on various architectures across different datasets with only a small computation overhead compared with vanilla training. Furthermore, we design a new attack strategy that targets both the classification and the auxiliary tasks, and show that our method is robust to this adaptive adversary as well. Code is available at https://github.com/Mishne-Lab/SOAP. 

100 

**(a)** Joint training of classification and auxiliary. **(b)** Test-time online purification 

**Figure 5.1.** An illustration of self-supervised online adversarial purification (SOAP). Left: joint training of the classification and the auxiliary task; Right: input adversarial example is purified iteratively to counter the representational shift, then classified. Note that the encoder is shared by both classification and purification. 

## **Related Work** 

Adversarial training aims to improve robustness through data augmentation, where the network is trained on adversarially perturbed examples instead of the clean original training samples (Goodfellow et al., 2014; Kurakin et al., 2016; Tramer` et al., 2017; Madry et al., 2017; Kannan et al., 2018; Zhang et al., 2019). By solving a min-max problem, the network learns a smoother data manifold and decision boundary which improve robustness. However, the computational cost of adversarial training is high because strong adversarial examples are typically found in an iterative manner with heavy gradient calculation. Compared with adversarial training, our method avoids solving the complex inner-max problem and thus is significantly more efficient in training. Our method does increase test-time computation but it is practically negligible per sample. 

Another genre of robust learning focuses on shifting the adversarial examples back to the clean data representation , namely purification. Gu and Rigazio (2014) exploited using a general DAE (Vincent et al., 2008) to remove adversarial noises; Meng and Chen (2017) train a reformer network, which is a collection of autoencoders, to move adversarial examples towards clean manifold; Liao et al. (2018) train a UNet that can denoise adversarial examples to their clean counterparts; Samangouei et al. (2018) train a GAN on clean examples and project the 

101 

adversarial examples to the manifold of the generator; Song et al. (2018) assume adversarial examples have lower probability and learn the image distribution with a PixelCNN so that they can maximize the probability of a given test example; Naseer et al. (2020) train a conditional GAN by letting it play a min-max game with a critic network in order to differentiate between clean and adversarial examples. In contrast to the above approaches, SOAP achieves better robust accuracy and does not require a GAN which is hard and inefficient to train. More importantly, our approach exploits a wider range of self-supervised signals for purification and conceptually can be applied to any format of data and not just images, given an appropriate self-supervised task. 

Self-supervised learning aims to learn intermediate representations of unlabeled data that are useful for unknown downstream tasks. This is done by solving a self-supervised task, or pretext task, where the supervision of the task comes from the data itself. Recently, a variety of self-supervised tasks have been proposed on images, including data reconstruction (Vincent et al., 2008; Rifai et al., 2011), relative positioning of patches (Doersch et al., 2015; Noroozi and Favaro, 2016), colorization (Zhang et al., 2016), transformation prediction (Dosovitskiy et al., 2014; Gidaris et al., 2018) or a combination of tasks (Doersch and Zisserman, 2017). 

More recently, studies have shown how self-supervised learning can improve adversarial robustness. Mao et al. (2019) find that adversarial attacks fool the networks by shifting latent representation to a false class. Hendrycks et al. (2019) observe that PGD adversarial training along with an auxiliary rotation prediction task improves robustness, while Naseer et al. (2020) use feature distortion as a self-supervised signal to find transferable attacks that generalize across different architectures and tasks. Chen et al. (2020b) combine adversarial training and self-supervised pre-training to boost fine-tuned robustness. These methods typically combine self-supervised learning with adversarial training, thus the computational cost is still high. In contrast, our approach achieves robust accuracy by test-time purification which uses a variety of self-supervised signals as auxiliary objectives. 

102 

## **5.2 Self-Supervised Purification** 

## **5.2.1 Problem Formulation** 

As aforementioned, Mao et al. (2019) observe that adversaries shift clean representations towards false classes to diminish robust accuracy. The small error in input space, carefully chosen by adversaries, gets amplified through the network and finally leads to wrong classification. A natural way to solve this is to perturb adversarial examples so as to shift their representation back to the true classes, i.e. purification. In this paper, we only consider classification as our main task, but our approach should be easily generalized to other tasks as well. 

Consider an encoder _z_ = _f_ ( _x_ ; _θ_ enc), a classifier _g_ ( _z_ ; _θ_ cls) on top of the representation _z_ , and the network _g ◦ f_ a composition of the encoder and the classifier. We formulate the purification problem as follows: for an adversarial example ( _x_ adv _, y_ ) and its clean counterpart ( _x, y_ ) (unknown to the network), a purification strategy _π_ aims to find _x_ pfy = _π_ ( _x_ adv) that is as close to the clean example _x_ as possible: _x_ pfy _→ x_ . However, this problem is underdetermined as different clean examples can share the same adversarial counterpart, i.e. there might be multiple or even infinite solutions for _x_ pfy. Thus, we consider the relaxation 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0117-04.png)


i.e. we accept _x_ pfy as long as _L_ cls is sufficiently small and the perturbation is bounded. Here _L_ cls is the cross entropy loss for classification and _ε_ adv is the budget of adversarial perturbation. However, this problem is still unsolvable since neither the true label _y_ nor the budget _ε_ adv is available at test-time. We need an alternative approach that can lead to a similar optimum. 

## **5.2.2 Self-supervised Online Purification** 

Let _h_ ( _z_ ; _θ_ aux) be an auxiliary device that shares the same representation _z_ with _g_ ( _z_ ; _θ_ cls), and _L_ aux be the auxiliary self-supervised objective. The intuition behind SOAP is that the shift 

103 

in representation _z_ that hinders classification will hinder the auxiliary self-supervised task as well. In other words, large _L_ aux often implies large _L_ cls. Therefore, we propose to use _L_ aux as an alternative to _L_ cls in Eq. (5.1). Then we can purify the adversarial examples using the auxiliary self-supervised signals, since the purified examples which perform better on the auxiliary task (small _L_ aux) should perform better on classification as well (small _L_ cls). 

During training, we jointly minimize the classification loss and self-supervised auxiliary 

loss 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0118-03.png)


where _α_ is a trade-off parameter between the two tasks. At test-time, given fixed network parameters _θ_ , we use the label-independent auxiliary objective to perform gradient descent _in the input space_ . The purification objective is 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0118-05.png)


where _ε_ pfy is the budget of purification. This is legitimate at test-time because unlike Eq. (5.1), the supervision or the purification signal comes from the data itself. Also, compared with vanilla training the only training increment of SOAP is an additional self-supervised regularization term. Thus, the computational complexity is largely reduced compared with adversarial training methods. In Sec. 5.3, we will show that adversarial examples do perform worse on auxiliary tasks and the gradient of the auxiliary loss provides useful information on improving robustness. Note that _ε_ adv is replaced with _ε_ pfy in Eq. (5.3), and we will discuss how to find appropriate _ε_ pfy in the next section. 

104 

## **5.2.3 Online Purification** 

Inspired by the PGD (Madry et al., 2017) attack (see Alg. 5), we propose a multi-step purifier (see Alg. 6) which can be seen as its inverse. In contrast to a PGD attack, which performs projected gradient _ascent_ on the input in order to maximize the cross entropy loss _L_ cls, the purifier performs projected gradient _descent_ on the input in order to minimize the auxiliary loss _L_ aux. The purifier achieves this goal by perturbing the adversarial examples, i.e. _π_ ( _x_ adv) = _x_ adv + _δ_ , while keeping the perturbation under a budget, i.e. _||δ ||_ ∞ _≤ ε_ pfy. Note that it is also plausible to use optimization-based algorithms in analog to some _ℓ_ 2 adversaries such as CW (Carlini and Wagner, 2017), however, this would require more steps of gradient descent at test-time. 

Taking the bound into account, the final objective of the purifier is to minimize the following 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0119-03.png)


For a multi-step purifier with step size _γ_ , at each step we calculate 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0119-05.png)


For step size _γ_ = _ε_ pfy and number of steps _T_ = 1, the multi-step purifier becomes a single-step purifier. This is analogous to PGD degrading to FGSM (Goodfellow et al., 2014) when the step size of the adversary _γ_ = _ε_ adv and the number of projected gradient ascent steps _T_ = 1 in Alg. 5. 

A remaining question is how to set _ε_ pfy when _ε_ adv is unknown. If _ε_ pfy is too small compared to the attack, it will not be sufficient to neutralize the adversarial perturbations. In the absence of knowledge of the attack _ε_ adv, we can use the auxiliary loss as a proxy to set the appropriate _ε_ pfy. In Figure 5.3 we plot the average auxiliary loss (green plot) of the purified examples for a range of _ε_ pfy values. The “elbows” of the auxiliary loss curves almost identify the 

105 

unknown _ε_ adv in every case with slight over-estimation. This suggests that the value for which the auxiliary loss approximately stops decreasing is a good estimate of _ε_ adv. Empirically, we find that using a slightly over-estimated _ε_ pfy benefits the accuracy after purification, similar to the claim by Song et al. (2018). This is because our network is trained with noisy examples and thus can handle the new noise introduced by purification. At test-time, we use the auxiliary loss to set _ε_ pfy in an online manner, by trying a range of values for _ε_ pfy and selecting the smallest one which minimizes the auxiliary loss for each _individual_ example. In the experiment section, we refer to the output of this selection procedure as _ε_ min-aux. We also empirically find for each sample the _ε_ pfy that results in the best adversarial accuracy, denoted _ε_ oracle in the experiment section. This is an upper bound on the performance SOAP can achieve. 

## **Algorithm 5.** PGD attack 

- 1: **Inputs:** _x_ : a test example; 

_T_ : the number of attack steps 

- 2: **Outputs:** _x_ adv: the adversarial example 

- 3: _δ ←_ 0 

4: **for** _t_ = 1 _,_ 2 _,..., T_ **do** 5: _ℓ ← L_ cls(( _g ◦ f_ )( _x_ + _δ_ ; _θ_ enc _, θ_ cls) _, y_ ) 

6: _δ ← δ_ + _γ_ sign(∇ _xℓ_ ) 7: _δ ←_ min(max( _δ , −ε_ adv) _, ε_ adv) 8: _δ ←_ min(max( _x_ + _δ ,_ 0) _,_ 1) _− x_ 

9: **end for** 10: _x_ adv _← x_ + _δ_ 

## **Algorithm 6.** Multi-step purification 

- 1: **Inputs:** _x_ : a test example; 

_T_ : the number of purification steps 

- 2: **Outputs:** _x_ pfy: the purified example 

3: _δ ←_ 0 4: **for** _t_ = 1 _,_ 2 _,..., T_ **do** 5: _ℓ ← L_ aux(( _h ◦ f_ )( _x_ + _δ_ ; _θ_ enc _, θ_ aux)) 6: _δ ← δ − γ_ sign(∇ _xℓ_ ) 7: _δ ←_ min(max( _δ , −ε_ pfy) _, ε_ pfy) 8: _δ ←_ min(max( _x_ + _δ ,_ 0) _,_ 1) _− x_ 

- 9: **end for** 

- 10: _x_ pfy _← x_ + _δ_ 

106 

## **5.2.4 Self-Supervised Signals** 

Theoretically, any existing self-supervised objective can be used for purification. However, due to the nature of purification and also for the sake of efficiency, not every self-supervised task is suitable. A suitable auxiliary task should be sensitive to the representation shift caused by adversarial perturbation, differentiable with respect to the entire input, e.g. every pixel for an image, and also efficient in both train and test-time. In addition, note that certain tasks are naturally incompatible with certain datasets. For example, a rotation-based self-supervised task cannot work on a rotation-invariant dataset. In this paper, we exploit three types of self-supervised signals: data reconstruction, rotation prediction and label consistency. 

## **Data Reconstruction** 

Data reconstruction (DR), including both deterministic data compression and probabilistic generative modeling, is probably one of the most natural forms of self-supervision. The latent representation, usually lying on a much lower dimensional space than the input space, is required to be comprehensive enough for the decoder to reconstruct the input data. 

To perform data reconstruction, we use a decoder network as the auxiliary device _h_ and require it to reconstruct the input from the latent representation _z_ . In order to better learn the underlying data manifold, as well as to increase robustness, the input is corrupted with additive Gaussian noise _η_ (and clipped) before fed into the encoder _f_ . The auxiliary loss is the _ℓ_ 2 distance between examples and their noisy reconstruction via the autoencoder _h ◦ f_ : 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0121-05.png)


In Figure 5.2, we present the outputs of an autoencoder trained using Eq. (5.4), for clean, adversarial and purified inputs. The purification shifts the representation of the adversarial examples closer to their original class (for example, 2 4, 8 and 9). Note that SOAP does not use the output of the autoencoder as a defense, but rather uses the autoencoder loss to purify the 

107 

**Figure 5.2.** Input digits of the encoder (left) and output digits of the decoder (right). From top to bottom are the clean digits, adversarially perturbed digits and purified digits, respectively. Red rectangles: the adversary fools the model to incorrectly classify the perturbed digit 8 as a 3 and the purification corrects the perception back to an 8. 

input. We plot the autoencdoer output here as we consider it as providing insight to how the trained model ‘sees’ these samples. 

## **Rotation Prediction** 

Rotation prediction (RP), as an image self-supervised task, was proposed by Gidaris et al. (2018). The authors rotate the original images in a dataset by a certain degree, then use a simple classifier to predict the degree of rotation using high-level representation by a convolutional neural network. The rationale is that the learned representation has to be semantically meaningful for the classifier to predict the rotation successfully. 

Following Gidaris et al. (2018), we make four copies of the image and rotate each of them by one of four degrees: Ω = _{_ 0 _[◦] ,_ 90 _[◦] ,_ 180 _[◦] ,_ 270 _[◦] }_ . The auxiliary task is a 4-way classification using representation _z_ = _f_ ( _x_ ), for which we use a simple linear classifier as the auxiliary device _h_ . The auxiliary loss is the summation of the 4-way classification cross-entropy of each rotated copy 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0122-05.png)


where _xω_ is a rotated input, and _h_ ( _·_ ) _ω_ is the predictive probability of it being rotated by _ω_ . While the standard rotation prediction task works well for training, we found that it tends to underestimate _ε_ pfy at test-time. Therefore, for purification, we replace the cross entropy classification 

108 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0123-00.png)


**----- Start of picture text -----**<br>
(a)  SOAP-DR (b)  SOAP-RP (c)  SOAP-LC<br>**----- End of picture text -----**<br>


**Figure 5.3.** Auxiliary loss vs. _ε_ pfy. SOAP (green plot) reduces the high adversarial auxiliary loss (orange plot) to the low clean level (blue plot). The vertical dashed line is the value of _ε_ adv. The trained models are FCN and ResNet-18 for MNIST and CIFAR10, respectively, with a PGD attack. 

loss by the mean square error between predictive distributions and one-hot targets. This increases the difficulty of the rotation prediction task and leads to better robust accuracy. 

## **Label consistency** 

The rationale of label consistency (LC) is that different data augmentations of the same sample should get consistent predictions from the network. This exact or similar concept is widely used in semi-supervised learning (Sajjadi et al., 2016; Laine and Aila, 2016), and also successfully applied in self-supervised contrastive learning (He et al., 2020; Chen et al., 2020a). 

We adopt label consistency to perform purification. The auxiliary task here is to minimize the _ℓ_ 2 distance between two augmentations _a_ 1( _x_ ) and _a_ 2( _x_ ) of a given image _x_ , in the logit space given by _g_ ( _·_ ). The auxiliary device of LC is the exact classifier, i.e. _h_ = _g_ , and the auxiliary loss 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0123-06.png)


## **5.3 Experiments** 

We evaluate SOAP on the MNIST, CIFAR10 and CIFAR100 datasets following Madry et al. (2017). 

109 

## **MNIST** 

For MNIST, we evaluate our method on a fully-connected network (FCN) and a convolutional neural network (CNN). For the auxiliary task, we evaluate the efficacy of data reconstruction. For the FCN _g_ ( _·_ ) is a linear classifier and _h_ ( _·_ ) is a fully-connected decoder; for the CNN _g_ ( _·_ ) is a 2-layer MLP and _h_ ( _·_ ) is a convolutional decoder. The output of the decoder is squashed into the range of [0 _,_ 1] by a sigmoid function. During training, the input digits are corrupted by an additive Gaussian noise ( _µ_ = 0 _, σ_ = 0 _._ 5). At test-time, _L_ aux of the reconstruction is computed without input corruption. SOAP runs _T_ = 5 iterations with step size _γ_ = 0 _._ 1. 

## **CIFAR** 

For CIFAR10 and CIFAR100, we evaluate our method on a ResNet-18 (He et al., 2016) and a 10-widen Wide-ResNet-28 (Zagoruyko and Komodakis, 2016). For the auxiliary task, we evaluate rotation prediction and label consistency. To train on rotation prediction, each rotated copy is corrupted by an additive Gaussian noise ( _µ_ = 0 _, σ_ = 0 _._ 1), encoded by _f_ ( _·_ ), and classified by a linear classifier _g_ ( _·_ ) for object recognition and by an auxiliary linear classifier _h_ ( _·_ ) for degree prediction. This results in a batch size 4 times larger than the original. At test-time, similar to DA, we compute _L_ aux on clean input images. 

To train on label consistency, we augment the input images twice using a composition of random flipping, random cropping and additive Gaussian corruption ( _µ_ = 0 _, σ_ = 0 _._ 1). Both of these two augmentations are used to train the classifier, therefore the batch size is twice as large as the original. At test-time, we use the input image as one copy and flip-crop the image to get another copy. Using the input image ensures that every pixel in the image is purified, and using definite flipping and cropping ensures there is enough difference between the input image and its augmentation. For both rotation prediction and label consistency, SOAP runs _T_ = 5 iterations with step size _γ_ = 4 _/_ 255. 

Note that we did not apply all auxiliary tasks on all datasets due to the compatibility issue 

110 

mentioned in Sec. 5.2.4. DR is not suitable for CIFAR as reconstruction via an autoencdoer is typically challenging on more realistic image datasets. RP is naturally incompatible with MNIST because the digits 0, 1, and 8 are self-symmetric; and digits 6 and 9 are interchangeable with 180 degree rotation. Similarly, LC is also not appropriate for MNIST because common data augmentations such as flipping and cropping are less meaningful on digits. 

## **5.3.1 White-box attacks** 

In Tables 5.1- 5.3 we compare SOAP against widely-used adversarial training (Goodfellow et al., 2014; Madry et al., 2017) and purification methods (Samangouei et al., 2018; Song et al., 2018) on a variety of _ℓ_ 2 and _ℓ_ ∞ bounded attacks: FGSM, PGD, CW, and DeepFool (Moosavi-Dezfooli et al., 2016). For MNIST, both FGSM and PGD are _ℓ_ ∞ bounded with _ε_ adv = 0 _._ 3, and the PGD runs 40 iterations with a step size of 0 _._ 01; CW and DeepFool are _ℓ_ 2 bounded with _ε_ adv = 4. For CIFAR10, FGSM and PGD are _ℓ_ ∞ bounded with _ε_ adv = 8 _/_ 255, and PGD runs 20 iterations with a step size of 2 _/_ 255; CW and DeepFool are _ℓ_ 2 bounded with _ε_ adv = 2. For CW and DeepFool which are optimization-based, resulted attacks that exceed the bound are projected to the _ε_ -ball. We mark the best performance for each attack by an underlined and bold **value** and the second best by bold **value** . We do not mark out the oracle accuracy but it does serve as an empirical upper bound of purification. 

For MNIST, SOAP-DR has great advantages over FGSM and PGD adversarial training on all attacks when the model has a small capacity (FCN). This is because adversarial training typically requires a large parameter set to learn a complex decision boundary while our method does not have this constraint. When using a larger CNN, SOAP outperforms FGSM adversarial training and comes close to Defense-GAN and PGD adversarial training on _ℓ_ ∞ attacks. SOAP also achieves better clean accuracy compared with all other methods. 

Note that FGSM AT achieves better accuracy under FGSM attacks than when there is no attack for the large-capacity networks. This is due to the label leaking effect (Kurakin et al., 2016): the model learns to classify examples from their perturbations rather than the examples 

111 

themselves. 

## **Table 5.1.** MNIST Results 

|Method|**FCN**|**FCN**|**FCN**|**FCN**||DF|**CNN**|**CNN**|**CNN**|**CNN**||DF|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||No Atk<br>FGSM|||PGD|CW||No Atk<br>FGSM|||PGD|CW||
|No Def<br>FGSM AT<br>PGD AT<br>Defense-GAN||**98.10**<br>79.76<br>76.82<br>95.84|16.87<br>**80.57**<br>60.70<br>**79.30**|0.49<br>2.95<br>57.07<br>**84.10**|0.01<br>6.22<br>31.68<br>**95.07**|1.40<br>17.24<br>13.82<br>**95.29**||**99.15**<br>98.78<br>98.97<br>95.92|1.49<br>**99.50**<br>**96.38**<br>90.30|0.00<br>33.70<br>**93.22**<br>**91.93**|0.00<br>0.02<br>**90.31**<br>**95.82**|0.69<br>6.16<br>75.55<br>**95.68**|
|SOAP-DR<br>_ε_pfy=0<br>_ε_pfy=_ε_min-aux<br>_ε_pfy=_ε_oracle_∗_||97.57<br>**97.56**<br>98.93|29.15<br>66.85<br>69.21|0.58<br>**61.88**<br>64.76|0.25<br>**86.81**<br>97.88|2.32<br>**87.02**<br>97.97||**99.04**<br>98.94<br>99.42|65.35<br>87.78<br>89.40|27.54<br>84.92<br>86.62|0.35<br>74.61<br>98.44|0.69<br>**81.27**<br>98.47|



For CIFAR10, on ResNet-18 SOAP-RP beats Pixel-Defend on all attacks except for FGSM and beats PGD adversarial training on _ℓ_ 2 attacks; on Wide-ResNet-28 it performs superiorly or equivalently against other methods on all attacks. SOAP-LC achieves superior accuracy compared with other methods, where the capacity is either small or large. Note that we chose Pixel-Defend as our purification baseline since Defense-GAN does not work on CIFAR10. Specifically, our method achieves over 50% accuracy under a strong PGD attack, which is 10% higher than PGD adversarial training. SOAP also exhibits great advantages over adversarial training on the _ℓ_ 2 attacks. Also, compared with vanilla training (‘No Def’) the multi-task training of SOAP improves robustness without purification ( _ε_ pfy = 0), which is similar on MNIST. Examples are shown in Figure 5.4. 

For CIFAR100, SOAP shows similar advantages over other methods. SOAP-RP beats PGD adversarial training on PGD attacks when using a large Wide-ResNet-28 model and on _ℓ_ 2 attacks in all cases; SOAP-LC again achieves superior accuracy compared with all other methods, where the capacity is either small or large. 

Our results demonstrate that SOAP is effective under both _ℓ_ ∞ and _ℓ_ 2 bounded attacks, as opposed to adversarial training which only defends effectively against _ℓ_ 2 attacks for MNIST 

112 

**Table 5.2.** CIFAR-10 results 

|Method|**ResNet-18**|**ResNet-18**|**ResNet-18**|**ResNet-18**||DF|**Wide-ResNet-28**|**Wide-ResNet-28**|**Wide-ResNet-28**|**Wide-ResNet-28**|**Wide-ResNet-28**|DF|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||No Atk<br>FGSM|||PGD|CW||No Atk<br>FGSM|||PGD|CW||
|No Def<br>FGSM AT<br>PGD AT<br>Pixel-Defend||**90.54**<br>72.73<br>74.23<br>79.00|15.42<br>44.16<br>**47.43**<br>39.85|0.00<br>37.40<br>**42.11**<br>29.89|0.00<br>2.69<br>3.14<br>**76.47**|6.26<br>24.58<br>25.84<br>**76.89**||**95.13**<br>72.20<br>85.92<br>83.68|14.82<br>**91.63**<br>51.58<br>41.37|0.00<br>0.01<br>41.50<br>39.00|0.00<br>0.00<br>2.06<br>79.30|3.28<br>14.41<br>24.08<br>**79.61**|
|SOAP-RP<br>_ε_pfy=0<br>_ε_pfy=_ε_min-aux<br>_ε_pfy=_ε_oracle_∗_<br>SOAP-LC<br>_ε_pfy=0<br>_ε_pfy=_ε_min-aux<br>_ε_pfy=_ε_oracle_∗_||73.64<br>71.97<br>87.57<br>86.36<br>**84.07**<br>94.06|5.77<br>35.80<br>37.60<br>22.81<br>**51.02**<br>59.45|0.47<br>38.53<br>39.40<br>0.15<br>**51.42**<br>62.29|0.00<br>68.22<br>79.80<br>0.00<br>**73.95**<br>86.94|13.65<br>68.44<br>84.34<br>8.52<br>**74.79**<br>88.88||88.68<br>90.94<br>95.55<br>**93.40**<br>91.89<br>96.93|30.21<br>51.11<br>52.69<br>59.23<br>**64.83**<br>71.85|8.52<br>**51.90**<br>52.61<br>3.55<br>**53.58**<br>63.10|0.08<br>**83.03**<br>86.99<br>0.01<br>**80.33**<br>88.96|10.67<br>**82.50**<br>90.49<br>46.98<br>60.56<br>73.66|



with a CNN. This implies that while the formulation of the purification in Eq. (5.4) mirrors an _ℓ_ ∞ bounded attack, our defense is not restricted to this specific type of attack, and the bound in Eq. (5.4) serves merely as a constraint on the purification perturbation rather than a-prior knowledge of the attack. 

## **Auxiliary-aware attacks** 

Previously, we focused on standard adversaries which only rely on the classification objectives. A natural question is: can an adversary easily find a stronger attack given the knowledge of our purification defense? In this section, we introduce a more ‘complete’ whitebox adversary which is aware of the purification method, and show that it is not straightforward to attack SOAP even with the knowledge of the auxiliary task used for purification. 

In contrast to canonical adversaries, here we consider adversaries that jointly optimize the cross-entropy loss and the auxiliary loss with respect to the input. As SOAP aims to minimize the auxiliary loss, the auxiliary-aware adversaries maximize the cross entropy loss while also minimizing the auxiliary loss at the same time. The intuition behind this is that the auxiliary- 

113 

%5 _ 2 x 2 :s eS: =oo P| ) q o:3 . ' Ez } h =a =5c | 2S 2 E 2 & : : Fea al = fies ; 7 a” j J i ' : <Se : r i | Le al = | 4 7 '.L ga ~. . _ 5 = % g% | Es S 8 : r —_ 3 a | 1 © 2 oO © c Cc @ ©—c 5° Ss: e . E — = . = : ©oe 7 4 Ee nm a4 E << tee : — xe) iS© . 2 : 3 wv = g S : : simul 8 : 5 ©oe - aE = : ‘i Es . sCc thbie 7, yvu |pi , 5 c & rot: | E i : Leae | z ; 2 ~ :pe Ajd 

114 

**Table 5.3.** CIFAR-100 results 

|Method|**ResNet-18**|**ResNet-18**|**ResNet-18**|**ResNet-18**||DF|**Wide-ResNet-28**|**Wide-ResNet-28**|**Wide-ResNet-28**|**Wide-ResNet-28**|**Wide-ResNet-28**|DF|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||No Atk<br>FGSM|||PGD|CW||No Atk<br>FGSM|||PGD|CW||
|No Def<br>FGSM AT<br>PGD AT||**65.56**<br>44.35<br>42.15|3.81<br>20.30<br>**21.92**|0.01<br>17.41<br>**20.04**|0.00<br>4.23<br>3.57|12.30<br>18.15<br>17.90||**78.16**<br>46.45<br>62.71|13.76<br>**88.24**<br>28.15|0.06<br>0.15<br>21.34|0.01<br>0.00<br>0.65|9.05<br>13.40<br>16.57|
|SOAP-RP<br>_ε_pfy=0<br>_ε_pfy=_ε_min-aux<br>_ε_pfy=_ε_oracle_∗_<br>SOAP-LC<br>_ε_pfy=0<br>_ε_pfy=_ε_min-aux<br>_ε_pfy=_ε_oracle_∗_||40.47<br>35.21<br>45.57<br>**57.86**<br>52.91<br>69.99|2.53<br>11.65<br>12.44<br>6.11<br>**22.93**<br>27.52|0.45<br>11.73<br>12.04<br>0.01<br>**27.55**<br>31.82|0.03<br>**32.97**<br>41.13<br>0.01<br>**50.26**<br>62.87|11.89<br>**33.51**<br>46.51<br>12.72<br>**50.57**<br>68.65||60.33<br>60.80<br>72.03<br>**74.04**<br>61.01<br>82.74|13.30<br>22.25<br>24.42<br>16.46<br>**31.40**<br>37.56|4.65<br>**22.00**<br>24.19<br>0.49<br>**37.53**<br>47.07|0.09<br>**54.11**<br>63.04<br>0.00<br>**56.09**<br>71.19|12.19<br>**54.70**<br>67.86<br>9.65<br>**53.79**<br>73.39|



aware adversaries try to find the auxiliary task “on-manifold” (Stutz et al., 2019) examples that can fool the classifier. The auxiliary-aware adversaries perform gradient ascent on the following combined objective 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0129-03.png)


where _β_ is a trade-off parameter between the cross entropy loss and the auxiliary loss. An = auxiliary-aware adversary degrades to a canonical one when _β_ 0 in the combined objective. 

As shown in Figure 5.5, an adversary cannot benefit from the knowledge of the defense in a straightforward way. When the trade-off parameter _β_ is negative (i.e. the adversary is attacking the auxiliary device as well), the attacks are weakened (blue plot) and purification based on all three auxiliaries achieves better robust accuracy (orange plot) as the amplitude of _β_ increases. When _β_ is positive, the accuracy of SOAP using data reconstruction and label consistency increases with _β_ . The reason for this is that the auxiliary component of the adapted attacks obfuscates the cross-entropy gradient, and thus weakens canonical attacks. The accuracy 

115 


![](markdown_output/escholarship-gsp_images/escholarship-gsp.pdf-0130-00.png)


**----- Start of picture text -----**<br>
(a)  SOAP-DR (b)  SOAP-RP (c)  SOAP-LC<br>**----- End of picture text -----**<br>


**Figure 5.5.** Purification against auxiliary-aware PGD attacks. Plots are classification accuracy before (blue) and after (orange) purification. 

of rotation prediction stays stable as _β_ varies, i.e. it is more sensitive to this kind of attack compared to the other tasks. 

## **5.3.2 Black-box attacks** 

Table 5.4 compares SOAP-DR with adversarial training against FGSM black-box attacks (Papernot et al., 2017). Following their approach, we let white-box adversaries, e.g. FGSM, attack a substitute model, with potentially different architecture, to generate the black-box adversarial examples for the target model. The substitute model is trained on a limited set of 150 test images unseen by the target model. These images are further labeled by the target model and augmented using a Jacobian-based method. SOAP significantly out-performs adversarial training on FCN; for CNN it out-performs FGSM adversarial training and comes close to PGD adversarial training. 

Chapter 5, in full, is a reprint of the material as it appears in the Proceedings of The 9th International Conference on Learning Representation, Shi, Changhao; Holtz, Chester; Mishne, Gal, 2021. The dissertation author was the primary investigator and author of this paper. 

116 

**Table 5.4.** MNIST Black-box Results 

||Target<br>Substitute|FCN|FCN|FCN|CNN|CNN|CNN|CNN|CNN|
|---|---|---|---|---|---|---|---|---|---|
|||No Atk||FCN||No Atk||FCN||
||No Def<br>FGSM AT<br>PGD AT||**98.10**<br>79.76<br>76.82|25.45<br>40.88<br>62.87|39.10<br>58.74<br>69.07||**99.15**<br>98.78<br>98.97|49.49<br>93.62<br>**97.79**|49.25<br>96.52<br>**98.09**|
||SOAP-DR<br>_ε_pfy=0<br>_ε_pfy=_ε_min-aux<br>_ε_pfy=_ε_oracle_∗_||**97.57**<br>97.56<br>98.93|**78.52**<br>**90.35**<br>94.34|**92.72**<br>**94.51**<br>97.33||**99.04**<br>98.94<br>99.42|95.25<br>**96.02**<br>98.12|97.43<br>**97.80**<br>98.81|



117 

## **Chapter 6** 

## **Conclusion** 

In summary, we study and generalize the graph learning problem to non-Gaussian and multi-way data. We also present a preliminary validation of the geometric assumption in the modern deep learning world. In this chapter, we first discuss some insights on the graph learning problem and conclude with some promising future directions to be explored. 

## **6.1 Discussion** 

Throughout this dissertation, an important remark of our efforts on graph learning is to realize the relations between GSP and GM. We typically describe the problem using the language of GSP, but it usually admits another GM interpretation. Graph learning is an original GSP task and targets the inference of graph topology from nodal observations, by leveraging various assumptions such as the smoothness prior (Dong et al., 2016). Its equivalence to IGMRF inference was later established (Egilmez et al., 2017), providing a new lens of graphical models under the Laplacian constraints. However, there are still some subtle differences between these two perspectives. The first subtle point is the choice of regularization. While the usage of regularization in the original GSP setup is flexible, in GM the log-determinant term is almost the sole choice for graph learning. This is because the log-determinant term is naturally induced by the improper MLE of the IGMRF, and thus enjoys favorable convergence properties. Obtaining theoretical results for general regularization terms is not impossible (Segarra et al., 2017) but 

118 

often difficult. This is also the reason that we chose the log-determinant term in the multi-way generalization and one of the key differences of MWGL to some prior methods. Another subtle point is the goal and evaluation of graph learning methods. In some earlier GSP graph learning works (Dong et al., 2016), the binary patterns of the graph, i.e. the existence of edges, are the primary subjects to be evaluated. In the synthetic simulation, sometimes the ground-truth are set to be unweighted graphs and the graph weights can be ignored. On the other hand, in GM, relative error has always been an important metric to evaluate the learned precision matrices and the ground-truth weighted graphs. 

It is also worth emphasizing again that the learning of Laplacian-constrained precision matrices is intrinsically different from classical covariance selection, though we draw GSP and GM parallel for ease of presentation. This is because the solution space of Laplacian-constrained precision matrices is completely disjoint from the counterpart of classical covariance selection. The Laplacian matrices are always singular with at least 1 zero eigenvalue, while covariance selection solves for non-singular precision matrices. The Laplacian constraints, however, can be loosened to remove the intrinsic property and enforce only the total positivity. 

Finally, we discuss several pitfalls of our proposed methods which can be improved in the following up. One of such pitfall is the efficiency of our graph learning methods. Although we proposed an efficient way to circumvent the expensive large matrix inversion for Cartesian product graph learning, such a trick has not been discovered for Kronecker and strong product graphs. Several spectral approximations of Kronecker and strong product graphs can yield the product Laplacian to be factorized approximately (Barik et al., 2018), but we found these to work poorly in practice. A more practical approximation can greatly improve the scale of the problem that KSGL can be applied to. GLEN is also haunted by the efficiency issue, as the graph signal denoising step loops over the entire set of signals. Using online learning methods might alleviate such inefficiency. Another downside is the lack of theoretical support for GLEN. While we theoretically proved the convergence rates of MWGL and KSGL, GLEN does not enjoy a similar guarantee. This also applies to SOAP where our manifold assumption is quite sloppy and 

119 

a theoretical analysis can help us better understand the adversarial purification. 

## **6.2 Future Works** 

GSP is a flourishing field and there remain many intriguing problems to be explored. Although we have generalized graph learning to non-Gaussian and multi-way settings, the smoothness assumption is so ubiquitous and versatile that it opens numerous opportunities in a more diverse world. For example, one can consider learning dynamic graphs that are non-static over time (Yamada et al., 2019). In our multi-way setting, when one axis corresponds to time, we fix the spatial graph on the other axis to be time-invariant. This is not always a realistic assumption. Learning dynamic graphs captures the subtle differences between neighboring timestamps and allows online adaptation on a larger time scale. Another example is to consider learning directed graphs (Marques et al., 2020). Throughout this dissertation, we use undirected graphs which manifest the Markov properties between random variables. On the other hand, some are interested in learning directed graphs to capture the casual relationship between random variables. 

Beyond the scope of GSP, modern geometric deep learning also offers opportunities to gloss the traditional methods in a fashionable way. One of the most important topics in the graph neural network (GNN) community is link prediction (Zhang and Chen, 2017, 2018; Cai et al., 2021). The link prediction task sets with a training dataset of known links between entities and requires the algorithm to predict the existence of hidden links. Since graph learning is equivalent to learning the edges between nodes, the link prediction task can be viewed as its supervised accommodation to the typical neural network setup. Finding out how useful the fully unsupervised graph learning prior such as the smoothness assumption is to the supervised link prediction task can be very interesting. One could imagine reformulating the link prediction task as a constrained optimization problem of graph learning where the training edges are the constraints. This also applies to graph rewiring (Topping et al., 2021; Arnaiz-Rodrıguez et al., 

120 

## 2022), the task of modifying an initial graph to facilitate specific downstream tasks. 

Finally, the recent prevalence of generative models suggests another interesting direction for applying graph learning techniques. Deep generative models such as diffusion models have demonstrated impressive capability in the generation of realistic images (Dhariwal and Nichol, 2021; Rombach et al., 2022; Saharia et al., 2022), videos (Ho et al., 2022b,a; Blattmann et al., 2023), audio (Kong et al., 2020; Liu et al., 2023), and also graphs (Niu et al., 2020; Jo et al., 2022; Huang et al., 2022; Kong et al., 2023). Graph learning in some sense is equivalent to a conditional graph generation task where the condition is the smooth graph signals or smooth data statistics. This encourages one to adopt deep generative models to graph learning. Previous studies (Shrivastava et al., 2019; Pu et al., 2021) use simple neural networks to unroll the optimization of graph learning or covariance selection to obtain a learning-based solver for these classical problems. A modern approach such as the diffusion model has great potential in these conditional or even unconditional graph generation tasks. 

121 

## **Bibliography** 

- Aitchison, J. and Ho, C. (1989). The multivariate Poisson-log normal distribution. _Biometrika_ , 76(4):643–653. 

- Aitchison, J. and Shen, S. M. (1980). Logistic-normal distributions: Some properties and uses. _Biometrika_ , 67(2):261–272. 

- Arnaiz-Rodrıguez, A., Begga, A., Escolano, F., and Oliver, N. M. (2022). Diffwire: Inductive graph rewiring via the lovasz bound.¨ In _Learning on Graphs Conference_ , pages 15–1. PMLR. 

- Banerjee, O., El Ghaoui, L., and d’Aspremont, A. (2008). Model selection through sparse maximum likelihood estimation for multivariate Gaussian or binary data. _The Journal of Machine Learning Research_ , 9:485–516. 

- Barik, S., Kalita, D., Pati, S., and Sahoo, G. (2018). Spectra of graphs resulting from various graph operations and products: a survey. _Special Matrices_ , 6(1):323–342. 

- Bassett, D. S. and Sporns, O. (2017). Network neuroscience. _Nature neuroscience_ , 20(3):353– 364. 

- Blattmann, A., Rombach, R., Ling, H., Dockhorn, T., Kim, S. W., Fidler, S., and Kreis, K. (2023). Align your latents: High-resolution video synthesis with latent diffusion models. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 22563–22575. 

- Borgatti, S. P., Mehra, A., Brass, D. J., and Labianca, G. (2009). Network analysis in the social sciences. _science_ , 323(5916):892–895. 

- Cai, L., Li, J., Wang, J., and Ji, S. (2021). Line graph neural networks for link prediction. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , 44(9):5103–5113. 

- Carlini, N. and Wagner, D. (2017). Towards evaluating the robustness of neural networks. In _2017 IEEE Symposium on Security and Privacy (SP)_ , pages 39–57. IEEE. 

- Chen, T., Kornblith, S., Norouzi, M., and Hinton, G. (2020a). A simple framework for contrastive 

122 

learning of visual representations. _arXiv preprint arXiv:2002.05709_ . 

- Chen, T., Liu, S., Chang, S., Cheng, Y., Amini, L., and Wang, Z. (2020b). Adversarial robustness: From self-supervised pre-training to fine-tuning. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 699–708. 

- Dawid, A. P. (1981). Some matrix-variate distribution theory: notational considerations and a bayesian application. _Biometrika_ , 68(1):265–274. 

- Dhariwal, P. and Nichol, A. (2021). Diffusion models beat gans on image synthesis. _Advances in neural information processing systems_ , 34:8780–8794. 

- Doersch, C., Gupta, A., and Efros, A. A. (2015). Unsupervised visual representation learning by context prediction. In _Proceedings of the IEEE international Conference on Computer Vision_ , pages 1422–1430. 

- Doersch, C. and Zisserman, A. (2017). Multi-task self-supervised visual learning. In _Proceedings of the IEEE International Conference on Computer Vision_ , pages 2051–2060. 

- Dong, X., Thanou, D., Frossard, P., and Vandergheynst, P. (2016). Learning Laplacian matrix in smooth graph signal representations. _IEEE Trans. Signal Process._ , 64(23):6160–6173. 

- Dosovitskiy, A., Springenberg, J. T., Riedmiller, M., and Brox, T. (2014). Discriminative unsupervised feature learning with convolutional neural networks. In _Advances in neural information processing systems_ , pages 766–774. 

- Dutilleul, P. (1999). The mle algorithm for the matrix normal distribution. _Journal of statistical computation and simulation_ , 64(2):105–123. 

- Egilmez, H. E., Pavez, E., and Ortega, A. (2017). Graph learning from data under Laplacian and structural constraints. _IEEE J. Sel. Topics Signal Process._ , 11(6):825–841. 

- Einizade, A. and Sardouie, S. H. (2023). Learning product graphs from spectral templates. _IEEE Transactions on Signal and Information Processing over Networks_ . 

- Fang, Y., Loparo, K. A., and Feng, X. (1994). Inequalities for the trace of matrix product. _IEEE Transactions on Automatic Control_ , 39(12):2489–2490. 

- Gao, S., Xia, X., Scheinost, D., and Mishne, G. (2021). Smooth graph learning for functional connectivity estimation. _NeuroImage_ , 239:118289. 

- Gidaris, S., Singh, P., and Komodakis, N. (2018). Unsupervised representation learning by predicting image rotations. _arXiv preprint arXiv:1803.07728_ . 

123 

- Goodfellow, I. J., Shlens, J., and Szegedy, C. (2014). Explaining and harnessing adversarial examples. _arXiv preprint arXiv:1412.6572_ . 

- Grassi, F., Loukas, A., Perraudin, N., and Ricaud, B. (2017). A time-vertex signal processing framework: Scalable processing and meaningful representations for time-series on graphs. _IEEE Trans. Signal Process._ , 66(3):817–829. 

- Greenewald, K., Zhou, S., and Hero III, A. (2019). Tensor graphical lasso (teralasso). _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 81(5):901–931. 

- Gu, S. and Rigazio, L. (2014). Towards deep neural network architectures robust to adversarial examples. _arXiv preprint arXiv:1412.5068_ . 

- Gupta, A. K. and Nagar, D. K. (1999). _Matrix variate distributions_ , volume 104. CRC Press. 

- Hammond, D. K., Vandergheynst, P., and Gribonval, R. (2011). Wavelets on graphs via spectral graph theory. _Applied and Computational Harmonic Analysis_ , 30(2):129–150. 

- Hanson, D. L. and Wright, F. T. (1971). A bound on tail probabilities for quadratic forms in independent random variables. _The Annals of Mathematical Statistics_ , 42(3):1079–1083. 

- He, K., Fan, H., Wu, Y., Xie, S., and Girshick, R. (2020). Momentum contrast for unsupervised visual representation learning. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 9729–9738. 

- He, K., Zhang, X., Ren, S., and Sun, J. (2016). Deep residual learning for image recognition. In _Proceedings of the IEEE conference on Computer Vision and Pattern Recognition_ , pages 770–778. 

- Hendrycks, D., Mazeika, M., Kadavath, S., and Song, D. (2019). Using self-supervised learning can improve model robustness and uncertainty. In _NeurIPS_ . 

- Ho, J., Chan, W., Saharia, C., Whang, J., Gao, R., Gritsenko, A., Kingma, D. P., Poole, B., Norouzi, M., Fleet, D. J., et al. (2022a). Imagen video: High definition video generation with diffusion models. _arXiv preprint arXiv:2210.02303_ . 

- Ho, J., Salimans, T., Gritsenko, A., Chan, W., Norouzi, M., and Fleet, D. J. (2022b). Video diffusion models. _Advances in Neural Information Processing Systems_ , 35:8633–8646. 

- Hu, C., Cheng, L., Sepulcre, J., Johnson, K. A., Fakhri, G. E., Lu, Y. M., and Li, Q. (2015). A spectral graph regression model for learning brain connectivity of Alzheimer’s disease. _PloS One_ , 10(5):e0128136. 

- Huang, H., Sun, L., Du, B., Fu, Y., and Lv, W. (2022). Graphgdp: Generative diffusion processes 

124 

for permutation invariant graph generation. In _2022 IEEE International Conference on Data Mining (ICDM)_ , pages 201–210. IEEE. 

- Ji, S., Pan, S., Cambria, E., Marttinen, P., and Philip, S. Y. (2021). A survey on knowledge graphs: Representation, acquisition, and applications. _IEEE transactions on neural networks and learning systems_ , 33(2):494–514. 

- Jo, J., Lee, S., and Hwang, S. J. (2022). Score-based generative modeling of graphs via the system of stochastic differential equations. In _International conference on machine learning_ , pages 10362–10383. PMLR. 

- Kadambari, S. K. and Chepuri, S. P. (2021). Product graph learning from multi-domain data with sparsity and rank constraints. _IEEE Transactions on Signal Processing_ , 69:5665–5680. 

- Kadambari, S. K. and Prabhakar Chepuri, S. (2020). Learning product graphs from multidomain signals. In _ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 5665–5669. 

- Kalaitzis, A., Lafferty, J., Lawrence, N. D., and Zhou, S. (2013). The bigraphical lasso. In _International Conference on Machine Learning_ , pages 1229–1237. PMLR. 

- Kalofolias, V. (2016). How to learn a graph from smooth signals. In _AISTATS_ , pages 920–929. PMLR. 

- Kannan, H., Kurakin, A., and Goodfellow, I. (2018). Adversarial logit pairing. _arXiv preprint arXiv:1803.06373_ . 

- Kemp, C. and Tenenbaum, J. B. (2008). The discovery of structural form. _Proceedings of the National Academy of Sciences_ , 105(31):10687–10692. 

- Kong, L., Cui, J., Sun, H., Zhuang, Y., Prakash, B. A., and Zhang, C. (2023). Autoregressive diffusion model for graph generation. In _International conference on machine learning_ , pages 17391–17408. PMLR. 

- Kong, Z., Ping, W., Huang, J., Zhao, K., and Catanzaro, B. (2020). Diffwave: A versatile diffusion model for audio synthesis. _arXiv preprint arXiv:2009.09761_ . 

- Koutra, D., Vogelstein, J. T., and Faloutsos, C. (2013). Deltacon: A principled massive-graph similarity function. In _Proceedings of the 2013 SIAM international conference on data mining_ , pages 162–170. SIAM. 

- Kumar, S., Ying, J., de Miranda Cardoso, J. V., and Palomar, D. P. (2020). A unified framework for structured graph learning via spectral constraints. _JMLR_ , 21(22):1–60. 

125 

- Kurakin, A., Goodfellow, I., and Bengio, S. (2016). Adversarial machine learning at scale. _arXiv preprint arXiv:1611.01236_ . 

- Laine, S. and Aila, T. (2016). Temporal ensembling for semi-supervised learning. _arXiv preprint arXiv:1610.02242_ . 

- Lake, B. and Tenenbaum, J. (2010). Discovering structure by learning sparse graphs. In _Proceedings of the 32nd Annual Conference of the CSS_ . 

- Lauritzen, S., Uhler, C., and Zwiernik, P. (2019). Maximum likelihood estimation in gaussian models under total positivity. _The Annals of Statistics_ , 47(4). 

- Leng, C. and Tang, C. Y. (2012). Sparse matrix graphical models. _Journal of the American Statistical Association_ , 107(499):1187–1200. 

- Leskovec, J., Chakrabarti, D., Kleinberg, J., Faloutsos, C., and Ghahramani, Z. (2010). Kronecker graphs: an approach to modeling networks. _Journal of Machine Learning Research_ , 11(2). 

- Liao, F., Liang, M., Dong, Y., Pang, T., Hu, X., and Zhu, J. (2018). Defense against adversarial attacks using high-level representation guided denoiser. In _Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition_ , pages 1778–1787. 

- Liu, H., Chen, Z., Yuan, Y., Mei, X., Liu, X., Mandic, D., Wang, W., and Plumbley, M. D. (2023). Audioldm: Text-to-audio generation with latent diffusion models. _arXiv preprint arXiv:2301.12503_ . 

- Liu, Y., Yang, L., You, K., Guo, W., and Wang, W. (2019). Graph learning based on spatiotemporal smoothness for time-varying graph signal. _IEEE Access_ , 7:62372–62386. 

- Lodhi, M. A. and Bajwa, W. U. (2020). Learning product graphs underlying smooth graph signals. _arXiv preprint arXiv:2002.11277_ . 

- Loukas, A. and Perraudin, N. (2019). Stationary time-vertex signal processing. _EURASIP journal on advances in signal processing_ , 2019(1):1–19. 

- Macke, J. H., Buesing, L., Cunningham, J. P., Yu, B. M., Shenoy, K. V., and Sahani, M. (2011). Empirical models of spiking in neural populations. _Advances in neural information processing systems_ , 24. 

- Madry, A., Makelov, A., Schmidt, L., Tsipras, D., and Vladu, A. (2017). Towards deep learning models resistant to adversarial attacks. _arXiv preprint arXiv:1706.06083_ . 

- Mao, C., Zhong, Z., Yang, J., Vondrick, C., and Ray, B. (2019). Metric learning for adversarial robustness. In _Advances in Neural Information Processing Systems_ , pages 480–491. 

126 

- Marques, A. G., Segarra, S., and Mateos, G. (2020). Signal processing on directed graphs: The role of edge directionality when processing and learning from network data. _IEEE Signal Processing Magazine_ , 37(6):99–116. 

- Mateos, G., Segarra, S., Marques, A. G., and Ribeiro, A. (2019). Connecting the dots: Identifying network structure via graph signal processing. _IEEE Signal Process. Mag._ , 36(3):16–43. 

- Meng, D. and Chen, H. (2017). Magnet: a two-pronged defense against adversarial examples. In _Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security_ , pages 135–147. 

- Merris, R. (1994). Laplacian matrices of graphs: a survey. _Linear algebra and its applications_ , 197:143–176. 

- Moosavi-Dezfooli, S.-M., Fawzi, A., and Frossard, P. (2016). Deepfool: a simple and accurate method to fool deep neural networks. In _Proceedings of the IEEE conference on Computer Vision and Pattern Recognition_ , pages 2574–2582. 

- Naseer, M., Khan, S., Hayat, M., Khan, F. S., and Porikli, F. (2020). A self-supervised approach for adversarial robustness. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 262–271. 

Nasreddine, W. (2021). Epileptic eeg dataset. https://data.mendeley.com/datasets/5pc2j46cbc. 

Nene, S. A., Nayar, S. K., Murase, H., et al. (1996). Columbia object image library (coil-20). 

- Niu, C., Song, Y., Song, J., Zhao, S., Grover, A., and Ermon, S. (2020). Permutation invariant graph generation via score-based generative modeling. In _International Conference on Artificial Intelligence and Statistics_ , pages 4474–4484. PMLR. 

- Noroozi, M. and Favaro, P. (2016). Unsupervised learning of visual representations by solving jigsaw puzzles. In _ECCV_ . 

- Ortega, A., Frossard, P., Kovaceviˇ c, J., Moura, J. M., and Vandergheynst, P. (2018).´ Graph signal processing: Overview, challenges, and applications. _Proceedings of the IEEE_ , 106(5):808–828. 

- Papernot, N., McDaniel, P., Goodfellow, I., Jha, S., Celik, Z. B., and Swami, A. (2017). Practical black-box attacks against machine learning. In _Proceedings of the 2017 ACM on Asia Conference on Computer and Communications Security_ , pages 506–519. 

- Pavlopoulos, G. A., Secrier, M., Moschopoulos, C. N., Soldatos, T. G., Kossida, S., Aerts, J., Schneider, R., and Bagos, P. G. (2011). Using graph theory to analyze biological networks. _BioData mining_ , 4:1–27. 

127 

- Pei, F., Ye, J., Zoltowski, D., Wu, A., Chowdhury, R. H., Sohn, H., O’Doherty, J. E., Shenoy, K. V., Kaufman, M. T., Churchland, M., et al. (2021). Neural latents benchmark’21: Evaluating latent variable models of neural population activity. _arXiv preprint arXiv:2109.04463_ . 

- Perraudin, N., Paratte, J., Shuman, D., Martin, L., Kalofolias, V., Vandergheynst, P., and Hammond, D. K. (2014). Gspbox: A toolbox for signal processing on graphs. _arXiv preprint arXiv:1408.5781_ . 

- Pu, X., Cao, T., Zhang, X., Dong, X., and Chen, S. (2021). Learning to learn graph topologies. _Advances in Neural Information Processing Systems_ , 34:4249–4262. 

- Rifai, S., Vincent, P., Muller, X., Glorot, X., and Bengio, Y. (2011). Contractive auto-encoders: Explicit invariance during feature extraction. In _ICML_ . 

- Rombach, R., Blattmann, A., Lorenz, D., Esser, P., and Ommer, B. (2022). High-resolution image synthesis with latent diffusion models. In _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 10684–10695. 

- Rothman, A. J., Bickel, P. J., Levina, E., and Zhu, J. (2008). Sparse permutation invariant covariance estimation. _Electronic Journal of Statistics_ , 2:494–515. 

- Rudelson, M. and Vershynin, R. (2013). Hanson-wright inequality and sub-gaussian concentration. _Electronic Communications in Probability_ , 18:1–9. 

- Rue, H. and Held, L. (2005). _Gaussian Markov random fields: theory and applications_ . Chapman and Hall/CRC. 

- Saharia, C., Chan, W., Saxena, S., Li, L., Whang, J., Denton, E. L., Ghasemipour, K., Gontijo Lopes, R., Karagol Ayan, B., Salimans, T., et al. (2022). Photorealistic text-to-image diffusion models with deep language understanding. _Advances in neural information processing systems_ , 35:36479–36494. 

- Sajjadi, M., Javanmardi, M., and Tasdizen, T. (2016). Regularization with stochastic transformations and perturbations for deep semi-supervised learning. In _Advances in neural information processing systems_ , pages 1163–1171. 

- Samangouei, P., Kabkab, M., and Chellappa, R. (2018). Defense-gan: Protecting classifiers against adversarial attacks using generative models. _arXiv preprint arXiv:1805.06605_ . 

- Sandryhaila, A. and Moura, J. M. (2014). Big data analysis with signal processing on graphs: Representation and processing of massive data sets with irregular structure. _IEEE signal processing magazine_ , 31(5):80–90. 

- Segarra, S., Marques, A. G., Mateos, G., and Ribeiro, A. (2017). Network topology inference 

128 

from spectral templates. _IEEE Trans. Signal Inf. Process_ , 3(3):467–483. 

- Sensors, B. W. S.-A. (2017). City of chicago— data portal.(nd). retrieved april 25, 2017. 

- Shi, C. and Mishne, G. (2023). Graph laplacian learning with exponential family noise. _arXiv preprint arXiv:2306.08201_ . 

- Shrivastava, H., Chen, X., Chen, B., Lan, G., Aluru, S., Liu, H., and Song, L. (2019). Glad: Learning sparse graph recovery. _arXiv preprint arXiv:1906.00271_ . 

- Shuman, D. I., Narang, S. K., Frossard, P., Ortega, A., and Vandergheynst, P. (2013). The emerging field of signal processing on graphs: Extending high-dimensional data analysis to networks and other irregular domains. _IEEE signal processing magazine_ , 30(3):83–98. 

- Slawski, M. and Hein, M. (2015). Estimation of positive definite M-matrices and structure learning for attractive Gaussian Markov random fields. _Linear Algebra and its Applications_ , 473:145–179. 

- Song, Y., Kim, T., Nowozin, S., Ermon, S., and Kushman, N. (2018). Pixeldefend: Leveraging generative models to understand and defend against adversarial examples. In _International Conference on Learning Representations_ . 

- Stanley, J. S., Chi, E. C., and Mishne, G. (2020). Multiway graph signal processing on tensors: Integrative analysis of irregular geometries. _IEEE signal processing magazine_ , 37(6):160–173. 

- Stutz, D., Hein, M., and Schiele, B. (2019). Disentangling adversarial robustness and generalization. In _Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition_ , pages 6976–6987. 

- Topping, J., Di Giovanni, F., Chamberlain, B. P., Dong, X., and Bronstein, M. M. (2021). Understanding over-squashing and bottlenecks on graphs via curvature. _arXiv preprint arXiv:2111.14522_ . 

- Tramer,` F., Kurakin, A., Papernot, N., Goodfellow, I., Boneh, D., and McDaniel, P. (2017). Ensemble adversarial training: Attacks and defenses. _arXiv preprint arXiv:1705.07204_ . 

- Tsiligkaridis, T., Hero III, A. O., and Zhou, S. (2013). On convergence of kronecker graphical lasso algorithms. _IEEE transactions on signal processing_ , 61(7):1743–1755. 

- Vincent, P., Larochelle, H., Bengio, Y., and Manzagol, P.-A. (2008). Extracting and composing robust features with denoising autoencoders. In _Proceedings of the 25th international Conference on Machine Learning_ , pages 1096–1103. 

- Wang, J., Xiao, L., Wilson, T. W., Stephen, J. M., Calhoun, V. D., and Wang, Y.-P. (2020a). 

129 

Examining brain maturation during adolescence using graph Laplacian learning based Fourier transform. _Journal of Neuroscience Methods_ , 338:108649. 

- Wang, Y., Jang, B., and Hero, A. (2020b). The sylvester graphical lasso (syglasso). In _International Conference on Artificial Intelligence and Statistics_ , pages 1943–1953. PMLR. 

- Werner, K., Jansson, M., and Stoica, P. (2008). On estimation of covariance matrices with kronecker product structure. _IEEE Transactions on Signal Processing_ , 56(2):478–491. 

- Wu, Z., Pan, S., Chen, F., Long, G., Zhang, C., and Philip, S. Y. (2020). A comprehensive survey on graph neural networks. _IEEE transactions on neural networks and learning systems_ , 32(1):4–24. 

- Yamada, K., Tanaka, Y., and Ortega, A. (2019). Time-varying graph learning based on sparseness of temporal variation. In _ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 5411–5415. IEEE. 

- Ying, J., de Miranda Cardoso, J. V., and Palomar, D. (2020). Nonconvex sparse graph learning under laplacian constrained graphical model. _Advances in Neural Information Processing Systems_ , 33:7101–7113. 

- Ying, J., de Miranda Cardoso, J. V., and Palomar, D. (2021). Minimax estimation of laplacian constrained precision matrices. In _International Conference on Artificial Intelligence and Statistics_ , pages 3736–3744. PMLR. 

- Yoon, J. H. and Kim, S. (2022). Eiglasso for scalable sparse kronecker-sum inverse covariance estimation. _The Journal of Machine Learning Research_ , 23(1):4733–4771. 

- Zagoruyko, S. and Komodakis, N. (2016). Wide residual networks. _arXiv preprint arXiv:1605.07146_ . 

- Zhang, H., Yu, Y., Jiao, J., Xing, E. P., Ghaoui, L. E., and Jordan, M. I. (2019). Theoretically principled trade-off between robustness and accuracy. _arXiv preprint arXiv:1901.08573_ . 

- Zhang, M. and Chen, Y. (2017). Weisfeiler-lehman neural machine for link prediction. In _Proceedings of the 23rd ACM SIGKDD international conference on knowledge discovery and data mining_ , pages 575–583. 

- Zhang, M. and Chen, Y. (2018). Link prediction based on graph neural networks. _Advances in neural information processing systems_ , 31. 

- Zhang, R., Isola, P., and Efros, A. A. (2016). Colorful image colorization. In _European Conference on Computer Vision_ , pages 649–666. Springer. 

130 

- Zhang, Y. and Schneider, J. (2010). Learning multiple tasks with a sparse matrix-normal penalty. _Advances in neural information processing systems_ , 23. 

131 

