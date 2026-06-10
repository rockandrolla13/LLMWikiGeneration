Proceedings of Machine Learning Research 266:1–4, 2025 14th Symposium on Conformal and Probabilistic Prediction with Applications 

## **Sequential Conformal Risk Control for Safe Railway Signaling Detection** 

**L´eo And´eol** leo.andeol@math.univ-toulouse.fr 

_Institute of Mathematics of Toulouse, University of Toulouse, Toulouse, France DTIPG, SNCF, Saint-Denis, France_ 

**Thomas Mass´ena** thomas.massena@irit.fr 

_Institut de Recherche en Informatique de Toulouse, University of Toulouse, Toulouse, France DTIPG, SNCF, Saint-Denis, France_ 

**Editor:** Khuong An Nguyen, Zhiyuan Luo, Harris Papadopoulos, Tuwe L¨ofstr¨om, Lars Carlsson and Henrik Bostr¨om 

## **Abstract** 

As machine learning becomes a more common tool in industry, its needs for certification increase. Conformal Prediction (Vovk et al., 2005), a framework for construction of prediction sets with tight coverage guarantees at any desired error rate, is an ideal tool for this purpose. However, adapting conformal methods to complex computer vision pipelines and providing appropriate guarantees is still a challenging task. Indeed, conformal approaches to object detection are often restricted to subtasks: often localization, and sometimes classification. In this study, we apply the comprehensive framework from And´eol et al. (2025) to the safety-critical task of railway signaling detection. 

**Keywords:** Conformal Risk Control, Sequential Conformal Risk Control, Object Detection, Railway Signaling 

## **1. Introduction** 

Conformal Prediction has been extensively studied in many classical tasks such as regression in Papadopoulos et al. (2002) and classification in Romano et al. (2020); Sadinle et al. (2019). Furthermore, industrial interest has recently motivated conformal applications in complex computer vision settings, such as object detection in Andeol et al. (2023); Timans et al. (2025) and semantic segmentation Mossina et al. (2024); Brunekreef et al. (2024). Recently, And´eol et al. (2025) proposed a comprehensive approach to apply conformal prediction to the complete object detection procedure applicable to any state-of-the-art model, including YOLO (Redmon et al., 2016) and DETR (Carion et al., 2020). In this work, we apply this method to the global task of railway signal detection, expanding on the previous work of Andeol et al. (2023) that only covered the localization of objects. 

## **2. Methodology** 

The object detection task commonly consists of three subtasks: confidence thresholding, localization and classification. We use the SeqCRC (Sequential Conformal Risk Control) of And´eol et al. (2025), an extension of Conformal Risk Control (Angelopoulos et al., 2024) that allows to control risks of multiple parameters chosen sequentially, as required in conformal object detection. 

More formally, we consider a deterministic object detector _f_ : _X →_ ( _B ×_ Σ _[K][−]_[1] _×_ [0 _,_ 1]) _[N]_[pred] that outputs _N_ pred predictions, constituted of a bounding box in _B_ = R[4] +[,][a] 

© 2025 L. And´eol & T. Mass´ena. 

And´eol Mass´ena 

|||Confidence|Confidence|Localization|Localization|Classification|Classification|Global|
|---|---|---|---|---|---|---|---|---|
|Model|mAP|SS|Risk|SS|Risk|SS|Risk|Risk|
|YOLO11x|0.879|1.29|0.000|1.25|0.004|1.01|0.001|0.0043|
|YOLO12x|0.895|1.27|0.001|1.21|0.005|**1.00**|0.002|0.0051|
|YOLO12x+|**0.911 **|**1.21**|0.001|**1.18**|0.005|**1.00**|0.001|0.0052|
|YOLO12x++|0.887|1.24|0.000|1.24|0.004|1.01|0.001|0.0049|



Figure 1: An image showing the conformalized bounding box in purple, the prediction in red, and the ground truth in green. 

Table 1: SeqCRC performance on object detection models. Set sizes (SS) indicate average set size for confidence filtering and classification, and average stretch in localization. All risks are controlled at target levels. Bold is best. 

classification distribution over _K_ classes, and a confidence score. After Non-Maximum Suppression, we construct three nested prediction sets: confidence Γ[cnf] _λ_[cnf][(] _[x]_[),][localization] Γ[loc][and][classification][Γ][cls][parameterized][by] _[λ]_[cnf] _[∈]_[Λ][cnf][,] _[λ]_[loc] _[∈]_[Λ][loc][,][and] _λ_[cnf] _,λ_[loc][(] _[x]_[),] _λ_[cnf] _,λ_[cls][(] _[x]_[),] _λ_[cls] _∈_ Λ[cls] respectively. We assume that ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) _,_ ( _X_ test _, Y_ test) are i.i.d., where each _Yi_ represents the set of ground-truth objects on image _Xi_ . The corresponding loss functions _L_[cnf] ( _λ_[cnf] ), _L_[loc] ( _λ_[cnf] _, λ_[loc] ) and _L_[cls] ( _λ_[cnf] _, λ_[cls] ) are assumed to be [0 _,_ 1]-valued, nonincreasing in each parameter and right-continuous. We then obtain the following guarantee: 

**Theorem 1 (Theorem 2 from And´eol et al. (2025))** _Let α_[cnf] _≥_ 0 _and α_[loc] _, α_[cls] _≥ α_[cnf] + _n_ +11 _[.][Then,][if][the][aforementioned][assumptions][hold][true,][and][if][L]_[cnf] _i_ ( _λ_[¯][cnf] ) _≤ α_[cnf] _almost surely, we have that the parameters λ[cnf] , λ[loc] and λ[cls] are well defined and_ E _L_[cnf] test[(] _[λ]_[cnf] +[)] _[≤][α]_[cnf] _[,]_ E max _L_[loc] test[(] _[λ]_[cnf] + _[, λ]_[loc] +[)] _[, L]_[cls] test[(] _[λ]_[cnf] + _[, λ]_[cls] +[)] _≤ α_[tot] = _α_[loc] + _α_[cls] _._ fo} OE ) 

## **3. Experiments** 

In these experiments we use YOLOv11 and YOLOv12 from Jocher et al. (2023); Tian et al. (2025). Models used a 640x640 resolution by default, replaced by 1080x1080 or 1280x1280 for YOLOv12+ and YOLOv12++ respectively. Then, we conduct our work using the TASV railway signaling dataset. It includes 37 classes and 12925 images, and is split as follows: 10% for validation, 10% for calibration and 10% for testing. The model training is conducted on the remaining 70% of the dataset. We set _α_[cnf] = 3 _·_ 10 _[−]_[3] , _α_[loc] = 5 _·_ 10 _[−]_[3] and _α_[cls] = 5 _·_ 10 _[−]_[3] for a global _α_[tot] = 10 _[−]_[2] . Following And´eol et al. (2025), we use the box ~~c~~ ount ~~r~~ ecall loss for confidence and the pixelwise loss for localization. The prediction sets are multiplicative for localization and employ Least Ambiguous Classifiers (LAC, Sadinle et al. (2019)) for the classification task. 

## **4. Discussion** 

Our results demonstrate the successful application of Sequential Conformal Risk Control to railway signaling detection. All models achieve risk control below the strict target levels ( _α_[tot] = 10 _[−]_[2] ), with YOLO12x+ achieving the best balance of accuracy (mAP = 0.911) and efficiency (minimal set sizes). Future work will aim for even lower error rates by enhancing the base models, incorporating temporal information from video, and designing domainspecific conformal losses and sets tailored to railway safety requirements. 

2 

Sequential Conformal Risk Control for Safe Railway Signaling Detection 

## **References** 

- Leo Andeol, Thomas Fel, Florence de Grancey, and Luca Mossina. Confident object detection via conformal prediction and conformal risk control: an application to railway signaling. In _Proceedings of the Twelfth Symposium on Conformal and Probabilistic Prediction with Applications_ , volume 204, pages 36–55. PMLR, 2023. URL `https://proceedings.mlr.press/v204/andeol23a.html` . 

- L´eo And´eol, Luca Mossina, Adrien Mazoyer, and S´ebastien Gerchinovitz. Conformal object detection by sequential risk control. _arXiv preprint arXiv:2505.24038_ , 2025. 

- Anastasios Nikolas Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, and Tal Schuster. Conformal risk control. In _The Twelfth International Conference on Learning Representations_ , 2024. URL `https://openreview.net/forum?id=33XGfHLtZg` . 

- Joren Brunekreef, Eric Marcus, Ray Sheombarsing, Jan-Jakob Sonke, and Jonas Teuwen. Kandinsky conformal prediction: efficient calibration of image segmentation algorithms. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 4135–4143, 2024. 

- Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, and Sergey Zagoruyko. End-to-end object detection with transformers. In _ECCV 2020_ , pages 213–229. Springer, 2020. 

- Glenn Jocher, Jing Qiu, and Ayush Chaurasia. Ultralytics YOLO, January 2023. URL `https://github.com/ultralytics/ultralytics` . 

- Luca Mossina, Joseba Dalmau, and L´eo And´eol. Conformal semantic image segmentation: Post-hoc quantification of predictive uncertainty. In _Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition_ , pages 3574–3584, 2024. 

- Harris Papadopoulos, Kostas Proedrou, Volodya Vovk, and Alex Gammerman. Inductive confidence machines for regression. In _Machine Learning: ECML 2002_ , 2002. 

- Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali Farhadi. You only look once: Unified, real-time object detection. In _Proceedings of the IEEE CVPR_ , June 2016. 

- Yaniv Romano, Matteo Sesia, and Emmanuel Candes. Classification with valid and adaptive coverage. In _Advances in Neural Information Processing Systems_ , volume 33, pages 3581– 3591, 2020. URL `https://proceedings.neurips.cc/paper_files/paper/2020/file/ 244edd7e85dc81602b7615cd705545f5-Paper.pdf` . 

- Mauricio Sadinle, Jing Lei, and Larry Wasserman. Least ambiguous set-valued classifiers with bounded error levels. _Journal of the American Statistical Association_ , 114(525): 223–234, 2019. doi: 10.1080/01621459.2017.1395341. URL `https://doi.org/10.1080/ 01621459.2017.1395341` . 

- Yunjie Tian, Qixiang Ye, and David Doermann. Yolov12: Attention-centric real-time object detectors. _arXiv preprint arXiv:2502.12524_ , 2025. 

3 

And´eol Mass´ena 

- Alexander Timans, Christoph-Nikolas Straehle, Kaspar Sakmann, and Eric Nalisnick. Adaptive bounding box uncertainties via two-step conformal prediction. In Aleˇs Leonardis, Elisa Ricci, Stefan Roth, Olga Russakovsky, Torsten Sattler, and G¨ul Varol, editors, _Computer Vision – ECCV 2024_ , pages 363–398, Cham, 2025. Springer Nature Switzerland. 

- Vladimir Vovk, Alexander Gammerman, and Glenn Shafer. _Algorithmic learning in a random world_ . Springer, 2005. 

4 

