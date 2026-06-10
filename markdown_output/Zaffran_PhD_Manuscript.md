## 

## Post-hoc predictive uncertainty quantification: methods with applications to electricity price forecasting 

Th`ese de doctorat de l’Institut Polytechnique de Paris pr´epar´ee `a l’ Ecole polytechnique[´] 

´Ecole doctorale n _[◦]_ 574 ´Ecole doctorale de math´ematiques Hadamard (EDMH) Sp´ecialit´e de doctorat : Math´ematiques appliqu´ees 

Th`ese pr´esent´ee et soutenue `a Paris, le 25 juin 2024, par 

## **MARGAUX ZAFFRAN** 

Composition du Jury : 

|Florence Forbes||
|---|---|
|Directrice de recherche, INRIA (STATIFY)|Pr´esidente|
|Pierre Pinson||
|Professeur, Imperial College London (Dyson School of Design<br>Engineering)|Rapporteur|
|´Etienne Roquain||
|Maˆıtre de conf´erences HdR, Sorbonne Universit´e (LPSM)|Rapporteur|
|Emmanuel Candes||
|Professeur, Stanford (Departments of Mathematics and Statistics)|Examinateur|
|´Eric Moulines||
|Professeur, ´Ecole polytechnique (CMAP)|Examinateur|
|Aaditya Ramdas||
|Professeur Assistant, Carnegie Mellon University (Departments of<br>Statistics and Machine Learning)|Examinateur|
|Julie Josse||
|Directrice de recherche, INRIA (PreMeDICaL)|Directrice de these|
|Aymeric Dieuleveut||
|Professeur, ´Ecole polytechnique (CMAP)|Co-directeur de these|
|Olivier F´eron||
|Chercheur s´enior, EDF R&D (OSIRIS)|Invit´e|
|Yannig Goude||
|Chercheur s´enior, EDF R&D (OSIRIS)|Invit´e|



574 

_À Joy,_ 

_On croyait en toi probablement plus que toi, Tu croyais en moi assurément plus que moi._ 

## **Abstract** 

The increasing use of renewable intermittent energy leads to more dependent and volatile energy markets. Therefore, an accurate electricity price forecasting is required to stabilize energy production planning, thus reducing the associated carbon emissions. The surge of more and more powerful statistical algorithms and machine learning offers promising prospects for tackling this problem. However, these methods provide ad hoc forecasts, with no indication of the degree of confidence to be placed in them. To ensure the trust of key actors in energy markets with regard to such decision-support tools, it is crucial to quantify their predictive uncertainty. This thesis focuses on developing predictive intervals for any underlying algorithm, including neural networks, without assumptions on the latter. While motivated by the electrical sector, the methods developed are generic: they can be applied in many sensitive fields. 

Split Conformal Prediction (SCP, Vovk et al., 2005; Papadopoulos et al., 2002; Lei et al., 2018) is a versatile procedure associating predictive intervals with any prediction model. Unlike existing probabilistic prediction methods, SCP is highly promising as it offers theoretical guarantees with finite sample size, under the sole distributional assumption that the data are exchangeable (i.e. the data distribution is invariant to permutation, a weaker assumption than independency with identical distribution). 

Formally, suppose we have _n_ data ( _Xi, Yi_ ) _[n] i_ =1 _[∈]_[R] _[d][×]_[R][,][where] _[Y]_[is][the][re-] sponse variable (e.g., electricity price) and _X ∈_ R _[d]_ the _d_ covariates (e.g., productions). The user sets a _miscoverage rate α ∈_ [0 _,_ 1] (typically 0.1 or 0.05). SCP constructs a predictive interval _Cn,α_ such that P _{Yn_ +1 _∈Cn,α_ ( _Xn_ +1) _} ≥_ 1 _− α_ : _Cn,α_ is said to be marginally _valid_ . Its length must be as small as possible to be informative ( _efficient_ ). An example of such an interval is given in Figure A. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0005-04.png)


**----- Start of picture text -----**<br>
800 Observed price<br>125 Predicted price<br>100 Predicted interval<br>600<br>75<br>400 50<br>21/01 23/01 25/01<br>200<br>0<br>2016 2017 2018 2019 2020<br>Date<br>/MWh)<br>(€<br>price<br>Spot<br>**----- End of picture text -----**<br>


Figure A: predictive intervals for electricity prices. 

However, SCP is not applicable on time series (such as electricity prices) as they are not exchangeable due to temporal dependence. To address this limitation, a first approach (Gibbs and Candès, 2021) relies on using an adaptive miscoverage rate _αt_ , that is updated according to previous performances and to an hyper-parameter _γ >_ 0, playing the role of a learning rate. Using Markov Chain theory, the first contribution of this thesis analyzes the influence of _γ_ on the efficiency of the resulting intervals. It allowed to propose a novel method 

v 

not requiring the choice of _γ_ —and therefore usable in practice—based on online expert aggregation. Following the electricity prices explosion in 2021, the second contribution of this thesis investigates the impact of this higher non-stationarity on probabilistic forecasts, and the improvements brought by different adaptive post-hoc layers such as SCP and online aggregation. 

Still, to improve electricity price point forecasts, one could leverage the emergence of open data platforms to integrate more explanatory variables such as commodity prices, or prices from other correlated markets. However, aggregating different data sources comes with methodological challenges, such as dealing with missing values, as time frequencies and market horizons may differ. Missing data are common in statistical practice and, paradoxically, their ocurrence increases with the quantity of data. 

A usual way to get point predictions is to replace the missing values ( `NA` s) by plausible values and then apply any learning algorithm on the completed data. Yet, there was no method for quantifying predictive uncertainty with `NA` s. The third and forth contributions of this thesis show that SCP applied on an imputed data set enjoys the exact same marginal _validity_ guarantees it would on a complete dataset. The strength of this result lies in its generality: it implies that the user can choose any imputation, even a naive one, without affecting the validity of the intervals, even for informative `NA` s (a complex and rarely studied scenario). However, The third and forth contributions of this thesis identify that `NA` s generate heteroskedasticity: the validity of the intervals depends on which covariates are observed. They propose the first algorithms to solve this problem, that are extremely simple to implement. Theoretically grounded, the assumptions on which they rely are nearly minimal according to hardness results. 

vi 

## **Résumé** 

L’utilisation croissante d’énergies renouvelables intermittentes rend les marchés de l’énergie plus dépendants et plus volatils. Par conséquent, une prévision précise du prix de l’électricité est nécessaire afin de stabiliser la planification de la production d’énergie et réduire ainsi les émissions de carbone associées. L’essor d’algorithmes statistiques et de l’apprentissage automatique de plus en plus puissants offre des perspectives prometteuses pour traiter ce problème. Cependant, ces méthodes fournissent des prévisions ad hoc, sans indication du degré de confiance à leur accorder. Pour garantir la confiance des acteurs des marchés de l’énergie à l’égard de ces outils d’aide à la décision, il est crucial de quantifier leur incertitude prédictive. Cette thèse porte sur le développement d’intervalles prédictifs pour tout algorithme de prédiction, y compris les réseaux neuronaux, sans hypothèses sur ce dernier. Bien que motivées par le secteur électrique, les méthodes développées sont génériques : elles peuvent être appliquées dans de nombreux autres domaines sensibles. 

La prédiction conforme par partition (SCP, Vovk et al., 2005; Papadopoulos et al., 2002; Lei et al., 2018) est une procédure polyvalente associant des intervalles prédictifs à tout modèle de prédiction. Contrairement aux méthodes de prédiction probabilistes existantes, CP est hautement prometteuse car elle offre des garanties théoriques à taille d’échantillon finie, sous la seule hypothèse distributionnelle que les données sont échangeables (c’est-à-dire que la distribution des données est invariante par permutation, ce qui est plus faible que des données indépendantes et identiquement distribuées). 

Formellement, supposons que nous disposons de _n_ données ( _Xi, Yi_ ) _[n] i_ =1 _[∈]_[R] _[d][ ×]_[ R] 800 Prix observ´e où _Y_ est la variable à prédire (e.g., le prix 125100 IntervallePrixPrix pr´evupr´evupr´evu 600 de l’électricité) et _X ∈_ R _[d]_ les _d_ covari75 ables (e.g., les productions). L’utilisateur 400 50 21/01 23/01 fixe un _taux de non-couverture α ∈_ [0 _,_ 1] 200 (typiquement 0.1 ou 0.05). SCP con0 2016 2017 2018 struit un intervalle prédictif _Cn,α_ tel que Date P _{Yn_ +1 _∈Cn,α_ ( _Xn_ +1) _} ≥_ 1 _−α_ : on dit que Figure B: intervalles prédictifs _Cn,α_ est _valide_ marginalement. Sa longueur de l’électricité. doit être la plus petite possible pour qu’il soit informatif ( _efficace_ ). Un exemple de tel intervalle est donné en Figure B. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0007-04.png)


**----- Start of picture text -----**<br>
800 Prix observ´e<br>IntervallePrixPrix pr´evupr´evupr´evu<br>100125100<br>600<br>75<br>400 50<br>21/01 23/01 25/01<br>200<br>0<br>2016 2017 2018 2019 2020<br>Date<br>/MWh)<br>(€<br>spot<br>Prix<br>**----- End of picture text -----**<br>


Figure B: intervalles prédictifs pour les prix de l’électricité. 

Cependant, SCP n’est pas applicable sur une séries temporelles (telles que les prix de l’électricité) car elles ne sont pas échangeables en raison de leur dépendance temporelle. Pour remédier à cette limitation, une première approche (Gibbs and Candès, 2021) repose 

vii 

sur l’utilisation d’un taux de non-couverture adaptatif _αt_ , qui est mis à jour en fonction des performances passées et d’un hyperparamètre _γ >_ 0, jouant le rôle d’un taux d’apprentissage. En utilisant la théorie des chaînes de Markov, la première contribution de cette thèse analyse l’influence de _γ_ sur l’efficacité des intervalles prédictifs associés. Cela a permis de proposer une nouvelle méthode ne nécessitant pas le choix de _γ_ —et donc utilisable en pratique—basée sur l’agrégation d’experts en ligne. Suite à l’explosion des prix de l’électricité en 2021, la deuxième contribution de cette thèse étudie l’impact de cette non-stationnarité accrue sur les prévisions probabilistes, et les améliorations apportées par différentes surcouches adaptatives telles que SCP et l’agrégation en ligne. 

Néanmoins, pour améliorer les prévisions des prix de l’électricité, nous pourrions tirer parti de l’émergence de plateformes de données ouvertes pour intégrer davantage de variables explicatives telles que les prix des matières premières ou les prix d’autres marchés corrélés. Cependant, l’agrégation de différentes sources de données s’accompagne de défis méthodologiques, tels que le traitement des valeurs manquantes, comme les fréquences temporelles et les horizons de marché peuvent différer. Les données manquantes sont courantes dans la pratique statistique et, paradoxalement, leur nombre augmente avec la quantité de données. 

Une approche traditionnelle pour obtenir des prédictions ponctuelles consiste à remplacer (imputer) les valeurs manquantes ( `NA` s) par des valeurs plausibles, puis à entraîner n’importe quel algorithme d’apprentissage sur les données complétées. Cependant, il n’existe aucune méthode permettant de quantifier l’incertitude prédictive avec les `NA` s. Les troisième et quatrième contributions de cette thèse montrent que SCP appliquée à un jeu de données imputé bénéficie exactement des mêmes garanties de _validité_ marginales que sur des données complètes. La force de ce résultat réside dans sa généralité : il implique que l’utilisateur peut choisir n’importe quelle imputation, même naïve, sans affecter la validité des intervalles, même pour des `NA` s informatives (un scénario complexe et rarement étudié). Cependant, Les troisième et quatrième contributions de cette thèse constatent que les `NA` génèrent de l’hétéroscédasticité : la validité des intervalles dépend de quelles variables explicatives sont observées. Ils proposent les premiers algorithmes pour résoudre ce problème, qui sont extrêmement simples à mettre en pratique. Théoriquement valides, les hypothèses sur lesquelles ils reposent sont presque minimales d’après de nouveaux résultats d’impossibilité. 

viii 

## **Remerciements** 

La recherche, et en particulier la thèse, est finalement une aventure grandement collective. Évidemment, mentors et collaborateurs façonnent les travaux de recherche, mais pas seulement : les cafés, les trajets en train pour se rendre en conférence, les inspirations prises de lectures ou d’exposés pédagogiques, les étudiants dont les questions défient toutes attentes, et les amitiés nouées en chemin également. Alors, pour clôturer le chapitre de la thèse, commençons par les canoniques remerciements. Ce chapitre sera sans doute le plus lu de cette thèse, je présente donc d’avance mes excuses si quelqu’un se sent oublié : paradoxalement ce sera également le moins relu de cette thèse ! 

Au commencement, il y avait Yannig. Professeur quand j’étais sur les bancs de l’ENSTA, je ne pouvais rêver mieux que l’entrée dans le milieu de la recherche que tu m’as permis d’effectuer à Bristol. J’ai ensuite eu la chance d’apprendre à tes côtés à EDF ce qui m’a définitivement orientée vers l’objectif d’une thèse CIFRE avec EDF. Et là encore, tu as insisté : non convaincue initialement par l’idée d’un sujet proche de la finance, tu es revenu m’en parler et tu m’as convaincue. Pour tout ça, déjà, merci. Merci également pour ta vision scientifique fine, toujours concrète mais rigoureuse. Enfin, merci pour ta bonne humeur et ta positivité en toutes circonstances, tes conseils avisés, tes coups de boost, et ta tranquillité inébranlable. 

Le binôme EDF était au complet avec Olivier. Olivier, ton écoute et ton attention m’ont profondément touchée tout au long de cette thèse. Merci pour le soin et la protection que tu accordes à tes doctorants. Tu as toujours été vigilant à prendre des décisions dans mon intérêt, et à réfléchir sur le long terme. Merci également de m’avoir initiée aux marchés de l’énergie, d’avoir répondu à toutes mes questions même quand elles se répétaient ou qu’elles étaient naïves. Sans ton apport expert, cette thèse serait à mes yeux incomplète car déconnectée de considérations concrètes. 

Julie, merci pour tout. Tu es un vrai modèle sur tous les aspects, et je suis plus que ravie de t’avoir fait confiance dès notre première discussion. Scientifiquement, ta vision interface parfaitement théorie et pratique utile, avec une précision mathématique et expérimentale fine, qui se retranscrivent dans ton amour de la rédaction. Tout ça en créant une équipe dynamique comme aucune autre, et en accordant sans faille du temps à tes étudiants. Je suis encore ébahie par ta capacité de concentration en visio et en talks. Au-delà de tout ça, ton énergie débordante, ton organisation indéfecticble, ton envie de transmission, ton écoute et ta compréhension (sur-)humaines, ta présence malgré ta distance, sont des qualités que j’admire (et je ne pense pas être la seule !). Merci. 

i 

Last but not least, Aymeric. Parfois, je me dis que tu ne t’attendais pas à passer autant de temps sur cette thèse quand tu en as accepté la co-direction. J’espère que tu ne regrettes pas, et je te remercie, vraiment. Merci de m’avoir accompagnée au plus près quand tout a débuté, et de m’avoir rassurée quand je doutais. Merci de transmettre ta passion, ton émerveillement, et ton excitation sur des sujets (mathématiques mais pas que) qui t’enthousiasment : c’est contagieux. Merci aussi pour les longues sessions au tableau, à se casser les dents sur des problèmes dont on oublie la formulation quand on est au milieu du chemin. Merci de ne jamais laisser tomber et de toujours y croire. Merci pour la méta-science et les réflexions sur la recherche, sur la gestion d’équipe ou de labos, et sur notre place en tant que chercheurs dans la société. Merci pour tous les à-côtés et les bons moments passés ensemble. 

Pour reprendre les mots de Julie, “ça ne pouvait pas être mieux”. Sans trop le savoir quand le montage de la thèse s’est fait, la complémentarité entre vous quatre était vraiment parfaite. Merci d’avoir créé cette équipe de choc et de m’y avoir accueillie. Merci aussi de m’avoir fait confiance quand on a ré-orienté cette thèse. J’ai hâte de voir l’avenir de nos échanges ! 

I would like to deeply thank my jury members. I am truly honored to have all of you in my jury, and, to be honest, a bit impressed too. First, I am indebted to you, Pierre and Étienne, for your precious reports. Pierre, thanks for your broad point of view and important connections to reality. Étienne, thanks for your extremely careful reading of (all of) my manuscript and precise comments. Then, many thanks to the examiners: Emmanuel, my whole PhD would be critically different if I did not attend one of your (excellent) talks; Florence, I am grateful to have you as President and in-person; Éric, you supported me in my professional evolution as a researcher; and Aaditya, I have to say that I always try to follow your advice and spread the word around me about them. For all of this, I feel really lucky. 

Ryan and Aaditya, I can’t wait to work with you on exciting topics! Many thanks for this amazing opportunity. I am also looking forward to join your teams: you both seem to be creating fruitful environments where everyone flourishes as human being. 

Indeed, I had the amazing chance to meet your students during a visiting trip to the US or in conferences. These events definitely opened my mind to new horizons. Thanks Madeleine and your team for hosting me in Stanford. Thanks to all the people who spent time with me, whether in Stanford, Berkeley, or Pittsburgh, all of our discussions shapened my perspectives (professionally and personally). 

A year before, I met Yaniv who hosted me for three wonderful months. Again, a huge thanks to you and your students for integrating me in the team, I came back with new vision on research. It was really an immense pleasure to work with you, and I hope we have more opportunities in the future to pursue our collaboration. I also came back with new friends (to quote one of them “it is not because it fades away that it did not exist”), and, sincerely, this trip have been a life changer on so many aspects. I am grateful for it to have 

ii 

existed. Thank you Meshi for being the best sergeant I could have hoped for, and thanks to the office mates (or their convex hull): Omer, Hagay, Noa, Naseem, Uri, Noam, and Nimrod. Morning breaks, ice creams, matches, trips and pomodoros, among other things, are cherished moments. Gilboa 23, what a team of roommates. In particular, Yeela, thank you for letting me your room; Hen, thank you for welcoming me, for deep discussions, and for sweet chocolate; Johanna, it was too short but I am so glad I met you, and Michael too. Il y a eu quelques français lors de ce séjour, et pas des moindres. Merci à Ruthy et Robert pour votre accueil à bras ouvert du début, qui s’est transformé en deuxième famille tout du long. Merci à Muriel, Gérard et toute votre famille pour ces quelques jours de fêtes ensemble, Muriel, nos discussions ont impacté ma fin de thèse sans aucun doute. 

Ces voyages ont en partie été possibles grâce à la Fondation L’Oréal – UNESCO, que je remercie de nouveau pour son soutien, et à l’association Séphora Berrebi. Emmanuelle et Gérard, je tiens encore à vous remercier chaleureusement, au-delà du voyage que vous avez permis de réaliser. Vous rencontrer et discuter avec vous a été une source d’inspiration et de confiance en l’avenir inébranlables. Je vous admire sincèrement, et je suis d’autant plus touchée et ravie d’avoir eu votre soutien. Merci. 

La transmission auprès de plus jeunes est quelque chose qui me tient à coeur, et cela a – je crois – un effet miroir : merci aux lycéennes rencontrées et aux étudiants auprès de qui j’ai eu la chance d’enseigner, vos sourires, vos questions, et votre confiance sont des vecteurs de motivation et de réflexion impressionants. Merci également à Grégoire, premier stagiaire formidable, c’était un vrai plaisir de travailler avec toi. 

Dans l’autre sens, ce bout de chemin a pu exister car j’ai rencontré des enseignants et mentors incroyables. En particulier, merci à Marseilleveyre et Monsieur Khelladi, Madame De Redon, Monsieur Torregrosa, Monsieur Jego et Monsieur Milliard. Ensuite, un très grand merci encore à Jeanne Nguyen, excellente chargée de TD de statistiques, sans qui je ne ferais vraisemblablement pas des stats aujourd’hui ! Then, a thousand of thanks to Matteo, from whom I learned so much during my first research experience. Enfin, merci à Philippe, pour un stage de master particulier (2020 oblige) et pourtant une super expérience : ton encadrement était plus que parfait pour moi, merci pour m’avoir partagé tes savoirs, points de vue, et ton enthousiasme serein. 

Il y a les professeurs, il y a les étudiants, mais il y a également les collègues qui font partie de cet environnement enrichissant et épanouissant. Alors, sans vous citer car pour sûr j’en oublierai, d’abord merci à toutes les personnes rencontrées en conférences, ici ou là, autour d’un café, d’un poster, d’un exposé ou d’un verre. Toutes nos discussions sont des trampolines pour avancer, pour apprécier la vie de chercheur, et pour démarrer la journée avec le sourire. Merci aux “plus vieux” qui prennent du temps avec nous. Merci aussi au groupe Jeunes Statisticien.ne.s de la SFdS et à la SFdS toute entière, et même plus encore, pour la bonne humeur et pour tout ce dont la communauté bénéficie grâce à vous, et notamment pour nous permettre de donner une voix à des sujets primordiaux qui me tiennent à coeur. Merci au groupe de travail conformal d’Orsay de m’avoir adoptée, 

iii 

et en particulier à Pierre et Jean-Baptiste. Merci Claire pour le temps passé à travailler ensemble et pour avoir canalisé mes couleurs extravagantes. 

Ensuite, les collègues du quotidien. Mes remerciements s’éternisent, et ça n’est pas prêt de s’arrêter : une thèse entre trois instituts, ça fait du monde ! 

Au tout début, bien sûr, EDF. Bulle d’oxygène au début de ma thèse confinée, R33, R39 et OSIRIS, merci. Pour la suite également, pour les sujets passionants que vous offrez, pour le recul que vous apportez, et pour les habitudes. Quelques encarts à la non-citation : merci d’abord à Édouard d’avoir cru en moi et de m’avoir montré la valeur d’un bon chef, merci à Clémence pour les conseils avisés et le smile, merci à Maximilien, la machine, nos routes se sont surprenament suivies de la prépa jusqu’au bureau à R33 (et ça va s’arrêter ici ;)), et enfin merci à Laura, Thomas et Pierre, accolytes doctorants d’Olivier, pour des discussions toujours chouettes. 

Ensuite, depuis le début aussi, l’INRIA et l’équipe de Julie, devenue PreMeDICaL depuis. Thank you all for creating such a dynamic team in which it is a pleasure to work in. Aude, Imke et Bénédicte en particulier, vous avoir côtoyées en distanciel, au jour le jour, ou en conférences, a été une chance. Réfléchir avec vous sur comment faire de la recherche et quelle est notre place a été précieux. Merci aux doctorants (ou pas) de Zénith pour leur accueil dès que je passais sur Montpellier. 

Finalement, le CMAP. J’y suis arrivée un peu sur le tard, mais j’y suis pour de bon maintenant. Merci à tous, que vous soyez en thèse, en post-doc ou permanents. Pour le coup, ici, je ne vais vraiment pas vous citer, on est bien trop nombreux pour que je ne fasse pas de faux pas. Merci à chacun d’entre vous pour tout ce que nous avons pu partager, et notamment pour les repas (trop tôt). Mention spéciale à l’équipe SIMPAS. Pour les moments partagés avec des chaussures de rando, de ski, un maillot, des cartes ou des cordes vocales bien utilisées, de jour comme de nuit, merci (au moins) à Achille, Antoine, Aymeric, Baptiste, Baptiste, Benjamin, Christoph, Clément, Clément, Constantin, Erwan, Erwan, Guillaume, Jean, Louis, Mahdi, Manon, Marylou, Maxence, Pablo, Paul, Pierre, Renaud, Solange, Thomas, Tom, Vincent. Merci tout particulier à l’équipe d’Aymeric (Constantin, Baptiste, Alexis, Renaud, Rémi, Damien, Mahmoud, Jean-Baptiste) pour l’entraide permanente, les relectures nombreuses et les répétitions. 

Parce qu’en recherche il y a une certaine proximité que je ne saurai expliquer, certains d’entre vous sont devenus bien plus que des compagnons de route. Manon, tu m’impressionnes de courage, de détermination, et de verre à moitié plein. Solange, colocationner avec toi n’est pas la meilleure idée pour suivre les exposés le lendemain mais qu’importe. Baptiste, nos rendez-vous du lundi soir me manquent déjà. Arthur, je recharge mes batteries quand je vois l’énergie que tu mets dans les combats qui comptent, qu’ils soient personnels ou sociétaux. Marie, boule de gentillesse pleine de pep’s, je t’attends pour le prochain karaoké. Constantin, nounours à la grosse voix, tu as vraisemblablement une vocation pour raconter des histoires loufoques qui font du bien. Baptiste, tu es le meilleur remonteur de moral qui existe et une machine à idées et conseils en tout genre. Alexis, je suis heureuse d’avoir pu découvrir ton univers et tes petits plats. Renaud, co-organisateur 

iv 

de GM, je suis ravie que la relève soit assurée également s’agissant des valeurs à défendre. 

Merci à mes coupaings d’ailleurs, qui supportent ma nullité en messages (et ce n’est pas peu dire). Promis, j’essaie de m’améliorer ! Mention spéciale ici aux filles de la Palaisienne : vous m’avez adoptée il y a maintenant 5 ans, et c’est non sans un pincement au coeur que cette aventure marque une pause. En rentrant dans le gymnase, je vous retrouvais les mardi et jeudi soirs, et ça n’avait pas de prix. Merci pour la nécessaire déconnexion, pour les rires et la sueur. Merci Marine d’avoir été une coach en or. Merci à la meilleure équipe : Elena, copine bien avant d’être co-équipière, Flore, Rire et Chansons sur pattes, Marie-Ange, duotte au top, et Marion, au dévouement inébranlable. 

Pour finir, merci à Carl pour tes traits d’esprit, ton humour fin, et les petites choses qui ont fait le quotidien plus rose. Merci également à Théo pour les dessins malgré le fait qu’on ne se comprenait pas toujours, ils sont magnifiques. Merci à Sylvie et Pierre pour votre accueil toujours à bras ouverts et votre écoute attentive. Tous ces moments m’ont ressourcée et restent gravés. 

Évidemment, merci à ma famille, qui m’a permis d’en arriver là, et me soutient malgré la distance. Merci de croire (beaucoup trop) en moi. Merci d’être là dans ce moment important, à Paris ou ailleurs, ça veut dire beaucoup pour moi. 

La vie est plus douce avec une bouillotte. Merci de faire exister ce nous. 

v 

## **Contents** 

|**I**<br>**1**<br>**2**<br>**3**<br>**4**<br>**II **<br>**5**|**Introduction**<br>**1**<br>**Forecasting Electricity Spot Prices**<br>**5**<br>1.1<br>Energy and electricity transition<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>5<br>1.2<br>Electricity markets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>6<br>1.3<br>Electricity price forecasting<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .<br>7<br>1.4<br>Probabilistic electricity price forecasting . . . . . . . . . . . . . . . . . . . .<br>8<br>**Thesis Outline and Main Contributions**<br>**9**<br>**Introduction to Conformal Prediction**<br>**11**<br>3.1<br>Supervised learning context and predictive uncertainty . . . . . . . . . . . .<br>11<br>3.2<br>Split Conformal Prediction (SCP) . . . . . . . . . . . . . . . . . . . . . . . .<br>19<br>3.3<br>On the design choices of CP and (empirical) conditional guarantees . . . . .<br>35<br>3.4<br>Avoiding data splitting: full CP and out-of-bags approaches . . . . . . . . .<br>43<br>3.5<br>Beyond exchangeability<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>51<br>**Technical Summary of the Contributions**<br>**57**<br>4.1<br>Contributions’ summary of Part II – Time Series . . . . . . . . . . . . . . .<br>57<br>4.2<br>Contributions’ summary of Part III – Missing Values . . . . . . . . . . . . .<br>59<br> **Time Series**<br>**63**<br>**Adaptive Conformal Predictions for Time Series**<br>**65**<br>5.1<br>Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>67<br>5.2<br>Setting: ACI for time series . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>69<br>5.3<br>Impact of _γ_ on ACI efciency . . . . . . . . . . . . . . . . . . . . . . . . . .<br>70<br>5.4<br>Adaptive strategies based on ACI . . . . . . . . . . . . . . . . . . . . . . . .<br>73<br>5.5<br>Numerical evaluation on synthetic data sets . . . . . . . . . . . . . . . . . .<br>74<br>5.6<br>Forecasting French electricity spot prices . . . . . . . . . . . . . . . . . . . .<br>79<br>5.7<br>Conclusion<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>81<br>5.A Details on Split Conformal Prediction<br>. . . . . . . . . . . . . . . . . . . . .<br>83<br>5.B<br>Proof of the results presented in Section 5.3 and additional numerical experi-<br>ments<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>87<br>5.C<br>Experimental details. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100<br>5.D Additional experiments on synthetic data sets . . . . . . . . . . . . . . . . . 103<br>5.E<br>Forecasting French electricity spot prices . . . . . . . . . . . . . . . . . . . . 106|
|---|---|



vii 

|**6**|**Adaptive Probabilistic Forecasting of French Electricity Spot Prices in**|**Adaptive Probabilistic Forecasting of French Electricity Spot Prices in**|
|---|---|---|
||**2020 **|**and 2021**<br>**111**|
||6.1|Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113|
||6.2|Data presentation and insightful new explanatory variables<br>. . . . . . . . . 115|
||6.3|Probabilistic forecasting methods . . . . . . . . . . . . . . . . . . . . . . . . 117|
||6.4|Adaptiveness as a wrapper around individual forecasts . . . . . . . . . . . . 121|
||6.5|Application and results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126|
||6.6|Conclusion and perspectives . . . . . . . . . . . . . . . . . . . . . . . . . . . 129|
||6.A|Results on the CRPS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131|
|**III**|**Missing Values**<br>**133**||
|**7**|**Conformal Prediction with Missing Values**<br>**135**||
||7.1|Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137|
||7.2|Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139|
||7.3|Warm-up: marginal coverage with `NA`s . . . . . . . . . . . . . . . . . . . . . 140|
||7.4|Challenge: `NA`s induce heteroskedasticity . . . . . . . . . . . . . . . . . . . . 141|
||7.5|Achieving mask-conditional-validity (MCV) . . . . . . . . . . . . . . . . . . 142|
||7.6|Towards asymptotic individualized coverage . . . . . . . . . . . . . . . . . . 146|
||7.7|Empirical study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147|
||7.8|Conclusion and perspectives . . . . . . . . . . . . . . . . . . . . . . . . . . . 151|
||7.A|Detailed perspective discussion<br>. . . . . . . . . . . . . . . . . . . . . . . . . 153|
||7.B|Illustration and details on CQR (Romano et al., 2019) procedure . . . . . . 154|
||7.C|Impute-then-predict+conformalization . . . . . . . . . . . . . . . . . . . . . 156|
||7.D|Gaussian linear model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157|
||7.E|Finite sample algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160|
||7.F|Infnite data results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165|
||7.G|Experimental study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168|
|**8**|**Predictive Uncertainty Quantifcation with Missing Covariates**<br>**175**||
||8.1|Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177|
||8.2|When is Mask-Conditional-Validity (MCV) a too lofty goal? . . . . . . . . . 183|
||8.3|Links between missing covariates and predictive uncertainty . . . . . . . . . 187|
||8.4|Principled unifed Missing Data Augmentation (MDA) framework:|
|||`CP-MDA-Nested`_⋆_<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194|
||8.5|A practical glimpse on the impacts of breaking the distribution’s assumptions201|
||8.A|Hardness results<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209|
||8.B|Link between missing covariates and uncertainty<br>. . . . . . . . . . . . . . . 214|
||8.C|Leave-one-out predictive sets for randomized algorithms . . . . . . . . . . . 218|
||8.D|Theory on `CP-MDA-Nested`_⋆_and CP-MDA-Nested . . . . . . . . . . . . . . . 220|



viii 

**IVConclusion and perspectives 225 Bibliography 231** 

ix 

## **Part I** 

## **Introduction** 

1 

3 

|||**Contents**|**Contents**|
|---|---|---|---|
|**1**|**Forecasting Electricity Spot Prices**||**5**|
||1.1|Energy and electricity transition<br>. . . . . . . . . . . . . . . . . . . . . . . .|5|
||1.2|Electricity markets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|6|
||1.3|Electricity price forecasting<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|7|
||1.4|Probabilistic electricity price forecasting . . . . . . . . . . . . . . . . . . . .|8|
|**2**|**Thesis Outline and Main Contributions**||**9**|
|**3**|**Introduction to Conformal Prediction**||**11**|
||3.1|Supervised learning context and predictive uncertainty . . . . . . . . . . . .|11|
|||3.1.1<br>Probabilistic modeling . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
|||3.1.2<br>Statistical learning . . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
|||3.1.3<br>On the importance of predictive uncertainty . . . . . . . . . . . . . .|14|
|||3.1.4<br>Quantile Regression<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|14|
|||3.1.5<br>Framework of interest, its limits and use cases . . . . . . . . . . . . .|17|
||3.2|Split Conformal Prediction (SCP) . . . . . . . . . . . . . . . . . . . . . . . .|19|
|||3.2.1<br>Standard mean-regression case and exchangeability . . . . . . . . . .|20|
|||3.2.2<br>Conformalized Quantile Regression (CQR) . . . . . . . . . . . . . . .|26|
|||3.2.3<br>Generalization of SCP: going beyond regression . . . . . . . . . . . .|29|
|||3.2.4<br>Some examples of SCP in classifcation . . . . . . . . . . . . . . . . .|31|
||3.3|On the design choices of CP and (empirical) conditional guarantees . . . . .|35|
|||3.3.1<br>What choices for the conformity scores? . . . . . . . . . . . . . . . .|35|
|||3.3.2<br>On distribution-free _X_-conditional validity . . . . . . . . . . . . . . .|37|
|||3.3.3<br>_Y_-conditional validity<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|41|
|||3.3.4<br>Impact of the calibration set on the coverage<br>. . . . . . . . . . . . .|42|
||3.4|Avoiding data splitting: full CP and out-of-bags approaches . . . . . . . . .|43|
|||3.4.1<br>Full Conformal Prediction . . . . . . . . . . . . . . . . . . . . . . . .|43|
|||3.4.2<br>Jackknife+ and leave-one-out CP . . . . . . . . . . . . . . . . . . . .|46|
|||3.4.3<br>CV+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|49|
||3.5|Beyond exchangeability<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|51|
|||3.5.1<br>Weighting strategies . . . . . . . . . . . . . . . . . . . . . . . . . . .|51|
|||3.5.2<br>Online setting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|53|
|**4**|**Technical Summary of the Contributions**||**57**|
||4.1|Contributions’ summary of Part II – Time Series . . . . . . . . . . . . . . .|57|
||4.2|Contributions’ summary of Part III – Missing Values . . . . . . . . . . . . .|59|



## **Chapter 1** 

## **Forecasting Electricity Spot Prices** 

This PhD thesis has been conducted under a CIFRE contract (industrial agreement for training through research) with EDF (Electricité de France, French main producer and supplier of electricity). 

## **1.1 Energy and electricity transition** 

## _“Who could have foreseen the climate crisis?”_ 

There is no need here to remind that according to IPBES (Intergovernmental SciencePolicy Platform on Biodiversity and Ecosystem Services) in 150 years, 83% of wildlife biomass and 41.5% of plant biomass have disappeared due to human activities; that the IPCC (Intergovernmental Panel on Climate Change) was created more than 35 years ago to ring the alarm; and that despite all of this only insufficient measures have been taken at the political and governmental levels (HCC-2021). Yet, this question is the tree that hides the actual forest: **what can we actually do to limit the climate crisis, or at least adapt to it?** 

Starting from the highest level, a partial natural answer is to reduce anthropogenic greenhouse gas emissions: this is necessary to meet the Paris Agreement requiring to ensure that the earth’s average temperature does not increase by more than 2°C before 2100, compared to 1850. Obviously, reducing our production and consumption would have a great quick impact on this. However, how to achieve it and whether we want to enforce it might be beyond the scope of an academic debate and most likely seems to belong to the citizens’ sphere. Closer to our concrete scope of applications, yet highly relevant, is how we produce energy and everything that lies around it. 

The last decades have witnessed important changes in the energy panorama, with an increasing integration of non-fossil fuels based energy production. For instance, major research and operational efforts have been deployed to develop renewable energies (RTE, 2022; IEA, 2022a)[1] . Especially, France did commit to reach carbon neutrality by 2050, and in particular by attaining 1/3 of renewable energies in gross final energy consumption by 2030. France also decided to support the development of nuclear plants (France-2023-491) to attain a decarbonized energy mix. In parallel, many usages have been electrified, or 

> 1RTE is the French Electricity Transmission Network, while IEA is the International Energy Agency. 

5 

_Chapter 1. Forecasting Electricity Spot Prices_ 

6 

are in their way to be, such as electric vehicles and distributed storages. Self-consumption (also known as consumer-producer, i.e. consuming the energy we produce) or even demand response programs (i.e. adapting the demand in concordance with the production, and not the traditional contrary) are also greatly incentivized (Bakare et al., 2023). 

The proliferation of these new uses of electricity and the growing importance of intermittent renewable energies are profoundly changing the energy landscape in Europe, and are at the root of major transformations in European electricity markets. In particular, they are becoming more dependent and volatile. **Therefore, an accurate electricity price forecasting is required to stabilize energy production planning and thus reduce the associated carbon emissions by increasing the investments in renewable energies and storage solutions. In this thesis, we focus on short-term prices.** 

## **1.2 Electricity markets** 

There are 4 main short-term markets in France, and more generally in Europe. 

- i) The first one, on which we will focus, is the _spot_ market. The spot electricity market is a blind auction market in which producers and consumers offer bids and offers for each hour, or for a block of hours, of the following day. The market closes at 12am of the day before the delivery. The 24 hourly prices are defined by a “pay-as-clear” principle: all players will exchange MegaWatt-hours at the same price, which, at first glance, can be seen as the cross between global supply and global demand. However, defining the price is more complex, as it takes into account interconnections between different countries, as well as so-called “block” offers. 

- ii) The second one is the _intraday_ market. It is a continuous trading market, offering hourly, half-hour and quarter-hour products. In contrast to the spot market, the prices are fixed on the fly in order to match the orders as soon as possible, with a closing time 5 to 15min before the delivery. 

- iii) Finally, the last two markets are the _system services_ and _balancing_ markets. These markets are handled by the transport system operator and are the ones responsible to ensure the perfect equilibrium between supply and offer at any time. 

These short-term markets are impacted by the transition described in Section 1.1. On the one hand, the need for greater security of electricity supply on different timescales is leading to an overhaul of system services, with the creation of new markets for these services at European level, notably in the new “Electricity balancing” regulatory framework adopted by the European Commission in 2017 (EU-2017/2195). On the other hand, the growing penetration of renewable energies has accentuated uncertainty over a short-term horizon of electricity production, affecting the operation of intraday markets, which are becoming the indispensable tool for managing forecasting errors in renewable production. In the German market, we are already seeing strong correlations between prices and wind generation, and it is only a matter of time before these phenomena appear in France. The presence of storage assets, whose price is steadily falling—even if quite high at the moment—, means that new market strategies can be put in place to stabilize supply and reduce costs. 

_1.3. Electricity price forecasting_ 

7 

## **1.3 Electricity price forecasting** 

In this fast-changing context, it is essential to have high-performance price forecasting methods for all short-term markets. 

Indeed, good price forecasts on successive markets enable us to _better anticipate the financial flows linked to renewable production and optimize the placement of production on the various markets_ . It is one of the essential elements for a good valuation of these production assets, which will _encourage investments in these low-carbon assets_ . 

Moreover, an accurate price forecast, both on successive markets and on the different hourly prices of a same market, enables to _optimize the management of flexibilities_ (physical battery or short-term consumption effacement contract, upward and downward adjustment flexibility of thermal power plants, etc.). In particular, raising the value of these flexibilities will encourage players to _invest in these assets, leading to a more secure power system_ . 

Yet, forecasting electricity prices is highly challenging due to all the aforementioned specificities of electricity: matching demand and production at all times, non-storable nature of electricity, exchanges between different countries via interconnections, the variable nature of generating facilities, etc. Specifically, these characteristics lead to negative or extremely high prices of non-negligible occurence (see Figure 1.1). This was before recent unfortunate fortuitous events that affected trememdously the markets, making them highly non-stationary, such as Covid-19 pandemic in 2020-2021 (IEA, 2021), the stress corrosion issue which affected French nuclear power plants in 2022 or the crisis of the gas markets triggered by Russia’s invasion of Ukraine (IEA, 2022b). Despite the increasing number of available historical data, state-of-the-art models (Weron, 2014; Lago et al., 2021) (from classical times series forecasting to deep learning methods), along with internal studies at EDF R&D[2] , did not obtain forecasts’ errors lower than 10% of the realized price[3] . As a reference, national consumption’s forecasts achieve errors around only 1% of the realized consumption. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0025-07.png)


**----- Start of picture text -----**<br>
3000<br>2500<br>2000<br>1500<br>1000 2 017 − 01 2017 − 07 2018 − 01 2018 − 07 2019 − 01 2019 − 07 2020 − 01 2020 − 07 2021 − 01<br>Date<br>500<br>0<br>2016 2017 2018 2019 2020 2021 2022 2023 2024<br>Date<br>/MWh)<br>€(<br>price<br>Spot<br>**----- End of picture text -----**<br>


Figure 1.1: Temporal evolution of the French electricity spot prices between 2016 and 2021. 

> 2We note here that operational forecasting tools available at EDF-Trading may be more efficient but they are using real time information that are not available as historical data. 

> 3Surprisingly, this holds for forecasts before 2020 as well as after 2020: the errors are more important after 2020, but as the prices are also higher, the relative error stays at the same order of magnitude. 

_Chapter 1. Forecasting Electricity Spot Prices_ 

8 

Leveraging the emergence of open data platforms such as ENTSO-E[4] Transparency Platform, or Eco2Mix Platform powered by RTE would likely improve electricity price forecasts. However, aggregating different data sources introduces a new demanding setting: the occurrence of missing values that comes along with computational and statistical challenges. For instance, it can be caused by different time frequencies or market horizons between fundamentally different explanatory variables. Also, the quality of the data evolves with time (as processes get consolidated) and anomalies can be observed. 

## **1.4 Probabilistic electricity price forecasting** 

Crucially, these forecasting methods provide ad hoc predictions, with no indication of the degree of confidence to be placed in them. To ensure the trust of key actors in energy markets with regard to such decision-support tools, it is crucial to **quantify their predictive uncertainty** . 

Furthermore, trading and energy management decisions (such as the ones mentioned in Section 1.3) require risk management tools which are based on probabilistic electricity price forecasting, leading to a rapid expansion of the literature in this area (see the review of Nowotarski and Weron, 2018). However, traditional probabilistic forecasts are only valid asymptotically or upon strong assumptions on the data that are typically not met by electricity prices (Gaussianity, stationarity). 

This supports the advancement of adaptive probabilistic approaches for forecasting prices, which can continuously learn and adjust to the evolving behaviors of electricity prices, resulting in accurate and reliable probabilistic forecasts even on non-stationary time series. 

In this PhD thesis, we propose to provide **theoretically grounded tools** able to quantify predictive uncertainty under **light assumptions on the underlying data distribution** and whose guarantees are agnostic to the prediction algorithm. We consider **post-hoc** methods, in order to allow their use in a plug-in fashion: any energy markets’ actor could keep its preferred operational pipeline and still turn the resulting predictions into guaranteed probabilistic forecasts. 

> 4ENTSO-E is the European Network of Transmission System Operators for Electricity. 

## **Chapter 2** 

## **Thesis Outline and Main Contributions** 

This manuscript is divided in three main parts. The rest of this introductory Part I is organized as follows. This chapter 2 provides a quick overview of the outline and main contributions. Chapter 3 is a pedagogical introduction to Conformal Prediction methods (see Table 2.1 for a reading guide), based on a tutorial designed during the completion of this PhD. Finally, in Chapter 4 we give a more technical and detailed summary of our contributions. 

Part II studies post-hoc predictive uncertainty quantification for time series. The first bottleneck to apply conformal methods in order to obtain guaranteed probabilistic electricity price forecasting in a post-hoc fashion is the highly non-stationary temporal aspect of electricity prices, breaking the exchangeability assumption. In Chapter 5 (based on a joint work with Olivier Féron, Yannig Goude, Julie Josse and Aymeric Dieuleveut) we propose a parameter-free algorithm tailored for time series, which is based on theoretically analysing the efficiency of Adaptive Conformal Inference (Gibbs and Candès, 2021). To investigate deeper how adaptive post-hoc probabilistic electricity prices forecast can be obtained, in Chapter 6 (based on the internship of Grégoire Dutot, co-supervised with Olivier Féron and Yannig Goude) we conduct an extensive application study on novel data set of recent turbulent French spot prices in 2020 and 2021. 

Another challenge that predictive uncertainty quantification for electricity prices forecasting faces is the occurence of missing values. Therefore, in Part III (based on joint works with Aymeric Dieuleveut, Julie Josse and Yaniv Romano) we analyse the interplay between missing values and predictive uncertainty quantification. In Chapter 7 we highlight that missing values induce heteroskedasticity, leading to uneven coverage depending on which features are observed. We design two algorithms that recover equalized coverage for any missingness under distributional assumptions on the missigness mechanism. In Chapter 8 we push forwards the theoretical 

9 

_Chapter 2. Thesis Outline and Main Contributions_ 

10 

analysis to understand precisely which distributional assumptions are unavoidable for theoretical informativeness. We also unify the previously proposed algorithms into a general framework that demontrastes empirical robustness to violations of the supposed missingness distribution. 

All these contributions are implemented with open source code available on this GitHub. The tutorial on which Chapter 3 is based has also been made openly available on this website. 

Each chapter is self-contained, thus the notations may slightly vary from chapter to chapter. 

|Related contribution|Related contribution|Relevant sections of Chapter 3|
|---|---|---|
|Ch. 3<br>Tutorial at:<br>▶_MASPIN days 2023_ (national),<br>with C. Boyer<br>▶_ENBIS 2023_ (European)<br>▶_UAI 2024_ (international),<br>with A. Dieuleveut<br>▶_ICML 2024_ (international),<br>with A. Dieuleveut||Split CP,<br>Section 3.2<br>Conditional validity,<br>Section 3.3<br>Full and _K_-fold CP,<br>Section 3.4<br>Non exchangeable,<br>Section 3.5|
||||
|Ch. 5<br>**M. Zafran**, O. Féron, Y. Goude,<br>J. Josse and A. Dieuleveut<br>_ICML 2022_ 1||<br>|
||||
|Ch. 6<br>G. Dutot_∗_, **M. Zafran**_∗_,<br>O. Féron and Y. Goude<br>submitted to _Applied Energy_2||<br>|
||||
|Ch. 7<br>**M. Zafran**, A. Dieuleveut,<br>J. Josse and Y. Romano<br>_ICML 2023_ 3||****<br>**()**<br>(****)|
|Ch. 8<br>**M. Zafran**, J. Josse,<br>Y. Romano and A. Dieuleveut<br>submitted to _JMLR_4||<br><br>|



Table 2.1: Summary of the scientific production ( _[∗]_ denotes equal contribution), with indications for a parsimonious reading of Chapter 3. 

> 1 “Adaptive Conformal Predictions for Time Series”. 

> 2 “Adaptive Probabilistic Forecasting of French Electricity Spot Prices”. 

> 3 “Conformal Prediction with Missing Values”. 

> 4 “Predictive Uncertainty Quantification with Missing Covariates”. 

## **Chapter 3** 

## **Introduction to Conformal Prediction** 

This chapter is a pedagogical introduction to conformal prediction. Therefore, some proofs are included in the body of the text as they are informative, and might have been modified or detailed with respect to the original papers. 

## **3.1 Supervised learning context and predictive uncertainty** 

The goal of supervised learning is to predict a _label Y ∈Y_ (also known as _response_ or _target_ or _outcome_ ), given some _features X ∈X_ (also known as _explanatory variables_ or _covariates_ ). We assume that the features and label spaces are measurable and that _X ⊆_ R _[d]_ , where _d ∈_ N _[∗]_ is the _problem’s dimension_ , i.e. the number of features. The nature of _Y_ defines the type of supervised learning task at hand. 

## **Example 3.1.1** (regression) **.** 

In _regression_ problems, the label to be predicted is continuous, i.e. _Y ⊆_ R. 

e.g., electricity prices 

**Example 3.1.2** (classification) **.** 

In _classification_ problems, the label to be predicted is categorical, i.e. the label set is finite, typically _Y ⊆_ N or _Y_ = _{−_ 1 _,_ 1 _}_ for the specific case of binary classification. 

In other words, predicting _Y ∈Y_ given _X ∈X_ corresponds to looking for a measurable function _f ∈M_ ( _X , Y_ ) _⊆Y[X]_ called a _predictor_ , such that _f_ ( _X_ ) “is close to” _Y_ , in a sense that remains to be defined. 

## **Definition 3.1.1** (loss function) **.** 

A measurable _loss function_ , noted _ℓ_ : _Y × Y �→_ R+, compares two points of _Y_ , typically by being such that for any ( _y, y[′]_ ) _∈Y_[2] , _ℓ_ ( _y, y[′]_ ) gets smaller as _y_ and _y[′]_ gets more similar. Usually, _y_ and _y[′]_ are the prediction of the studied predictor and the ground truth value. 

11 

_Chapter 3. Introduction to Conformal Prediction_ 

12 

**Example 3.1.3** (quadratic loss—regression) **.** 

In _regression_ , a standard loss function is _ℓ_ ( _y, y[′]_ ) = ( _y − y[′]_ )[2] . 

**Example 3.1.4** (0-1 loss—classification) **.** 

In _classification_ , a natural loss function is _ℓ_ ( _y, y[′]_ ) = 1 _{y_ = _y[′] }_ . 

## **3.1.1 Probabilistic modeling** 

Modeling the labels _Y_ and the features _X_ as random variables whose joint distribution is denoted _D_ , the goal of supervised learning is to find a function _f[⋆]_ that minimizes the expectation of the loss _ℓ_ over _D_ , referred to as the _ℓ-risk_ . 

**Definition 3.1.2** ( _ℓ_ –risk) **.** 

The _ℓ_ – _risk_ of a predictor is the expectation of the loss _ℓ_ evaluated on the labels and the predictor outputs under the distribution _D_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0030-10.png)


Any _f[⋆]_ minimizing the _ℓ_ –risk is a _ℓ-Bayes predictor_ and achieves the _ℓ_ –Bayes risk. 

**Definition 3.1.3** ( _ℓ_ –Bayes predictor) **.** 

An _ℓ_ – _Bayes predictor_ is a minimizer of the _ℓ_ –risk: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0030-14.png)


Moreover, the _ℓ–Bayes risk_ is defined as _R[⋆] ℓ_[:=] _[ R][ℓ]_[(] _[f][⋆]_[)][for][any] _[ℓ]_[–Bayes][predictor] _[f][⋆]_[.] 

**Example 3.1.5** (quadratic loss Bayes predictor—regression) **.** 

In regression, the quadratic–Bayes predictor is _f[⋆]_ ( _X_ ) = E [ _Y |X_ ]. 

**Example 3.1.6** (0-1 loss Bayes predictor—classification) **.** 

In classification, the 0-1–Bayes predictor is _f[⋆]_ ( _X_ ) _∈_ arg max _k∈{−_ 1 _,_ 1 _}_ P( _Y_ = _k|X_ ). 

## **3.1.2 Statistical learning** 

In practice, the distribution _D_ is unknown. Computing explicitly the _ℓ_ –risk and a fortiori exhibiting the _ℓ_ –Bayes predictor is therefore impossible. However, we typically have access to _n ∈_ N _[∗]_ independent and identically distributed (i.i.d.) random variables drawn from _D_ , forming a data set ( _Xi, Yi_ ) _[n] i_ =1 _[∈]_[(] _[X][× Y]_[)] _[n][∼D][⊗]_[(] _[n]_[)][.][One][can][leverage][this][data][set][in] order to learn a predictor based on the _historical/training data_ . 

_3.1. Supervised learning context and predictive uncertainty_ 

13 

**Definition 3.1.4** (statistical learning algorithm) **.** 

A _statistical learning algorithm_ is a measurable function 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0031-04.png)


More generally, a _stochastic_ statistical learning algorithm is a measurable function 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0031-06.png)


where _ξ_ encodes the randomness of _A_ . 

One goal of such a _statistical learning algorithm_ could be to attain a risk close to the _ℓ_ –Bayes risk _R[⋆] ℓ_[.][However,][again,][without][information][on] _[D]_[the][true] _[ℓ]_[–risk][of][a][predictor] can not be computed. Nonetheless, we can use the _training data_ as a surrogate for _D_ to estimate the _ℓ_ –risk by computing the so-called empirical _ℓ_ -risk. 

**Definition 3.1.5** (empirical _ℓ_ –risk) **.** 

The _empirical ℓ–risk_ of a predictor is the empirical average of its loss on the training data set: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0031-11.png)


**Remark 3.1.1** (consistency of the empirical _ℓ_ –risk) **.** 

The empirical _ℓ_ –risk is a consistent estimator of the _ℓ_ –risk. 

Many statistical learning algorithms are built so as to minimize the _empirical risk_ . By doing so, they aim at using _historical/training data_ to infer a predictor that should provide accurate prediction on any _X ∈X_ , even non-observed ones. To ensure this _generalization_ , the predictor has to be constrained to a fixed family of functions _F ⊂M_ ( _X , Y_ ), called a _model_ . 

**Definition 3.1.6** (empirical risk minimizer) **.** 

A _minimizer of the empirical risk_ over _F ⊂M_ ( _X , Y_ ) is a statistical learning algorithm _A_ such that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0031-17.png)


_Chapter 3. Introduction to Conformal Prediction_ 

14 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0032-02.png)


**----- Start of picture text -----**<br>
10 10 10<br>5 5 5<br>0 0 0<br>− 5 − 5 − 5<br>− 10 − 10 − 10<br>0 2 4 0 2 4 0 2 4<br>X X X<br>Figure 3.1: Three distinct data distributions with the same quadratic-Bayes predictor<br>(regression setting).<br>10 10 10<br>5 5 5<br>0 0 0<br>− 5 − 5 − 5<br>− 10 − 10 − 10<br>0 2 4 0 2 4 0 2 4<br>X X X<br>Y Y Y<br>Y Y Y<br>**----- End of picture text -----**<br>


Figure 3.1: Three distinct data distributions with the same quadratic-Bayes predictor (regression setting). 

Figure 3.2: Three distinct data distributions with the same conditional expectation, and different conditional quantiles in blue (regression setting). 

## **3.1.3 On the importance of predictive uncertainty** 

In the previous sections, we have explored the paradigm where one aims to predict a _single_ value, also referred to as _point prediction_ , without any indication of the degree of confidence that can be given to these predictions. By leveraging increasingly large data sets, statistical algorithms and machine learning methods are now frequently used to support high-stakes decision-making problems such as autonomous driving, medical or civic applications, among others. Yet, as it can be observed in Figure 3.1, an important drawback of this approach is that even the Bayes predictor does not allow to characterize the underlying distribution of _Y |X_ . Therefore, the same perfect predictions cover up different underlying phenomena. Quantifying uncertainty (e.g., as illustrated in Figure 3.2 through perfect predictive intervals based on the conditional quantiles of _Y |X_ ) conveys the information of the predictive uncertainty. To ensure the safe deployment of predictive models[1] it is crucial to quantify the inherent uncertainty of the resulting predictions, communicating the limits of predictive performance. 

## **3.1.4 Quantile Regression** 

In this subsection, we focus solely on the regression setting. 

An approach to take the predictive uncertainty into account is to consider the _quantiles_ of a random variable _Y_ , as they encapsulate the overall distribution of _Y_ . First, let’s consider the _univariate_ or _marginal quantiles_ , which do not take into account any link between _Y_ and some features _X_ (i.e. they take the expectation over _X_ ). 

1 By a slight abuse of language, we commonly use “model” instead of “statistical learning algorithm”. 

_3.1. Supervised learning context and predictive uncertainty_ 

15 

**Definition 3.1.7** (univariate quantile) **.** 

The _quantile_ of level _β ∈_ [0 _,_ 1] of _Y_ , denoted _QY_ ( _β_ ), is defined as: 

_QY_ ( _β_ ) := inf _{y ∈_ R _,_ P( _Y ≤ y_ ) _≥ β}_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0033-05.png)


_QY_ ( _·_ ) is the _quantile function_ , which is the generalized inverse of the cumulative distribution function _FY_ . 

It can be estimated through the _empirical quantile_ of level _β_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0033-08.png)


_a_ Similarly, let _qβ,_ inf ( _Y_ 1 _, . . . , Yn_ ) := _⌊β × n⌋_ smallest value of ( _Y_ 1 _, . . . , Yn_ ). 

**Example 3.1.7** (median) **.** 

The quantile of level _β_ = 0 _._ 5 is better known as the _median_ . 

_�→ q_ 0 _._ 5 ( _Y_ 1 _, . . . , Yn_ ) is the _⌈_ 0 _._ 5 _× n⌉_ smallest value of ( _Y_ 1 _, . . . , Yn_ ), i.e. the smallest value of ( _Y_ 1 _, . . . , Yn_ ) which is larger than at least half of ( _Y_ 1 _, . . . , Yn_ ), known as the _empirical median_ of ( _Y_ 1 _, . . . , Yn_ ); 

- _�→ QY_ (0 _._ 5) is the _median_ of the distribution of _Y_ . 

Just like the expectation is the natural minimizer of the quadratic loss, the quantiles minimize the _pinball loss_ described below, and widely used to estimate quantiles in practice. This is formalized in Remark 3.1.2. 

**Definition 3.1.8** (pinball loss) **.** 

The _pinball loss_ of level _β ∈_ [0 _,_ 1] is defined as: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0033-17.png)


**Remark 3.1.2** (minimizing the pinball loss retrieves the quantile) **.** Let _β ∈_ [0 _,_ 1]. Assume arg min _q∈Y_ E _DY_ [ _ℓβ_ ( _Y, q_ )] _̸_ = _∅_ . Set _qβ[⋆][∈]_[arg min] _q∈Y_[E] _[D] Y_[[] _[ℓ][β]_[(] _[Y, q]_[)]][.] Then if _FY_ is continuous and strictly increasing, we have that _qβ[⋆]_[=] _[ F][ −] Y_[1][(] _[β]_[)][.] 

_Proof._ First, as _qβ[⋆][∈]_[arg min] _q∈Y_[E] _[D] Y_[[] _[ℓ][β]_[(] _[Y, q]_[)]][,][we][have:] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0033-20.png)


_Chapter 3. Introduction to Conformal Prediction_ 

16 

Then, let _q[′] ∈_ R. Remark that for any _y_ = _q[′]_ , _[∂ℓ] ∂q[β]_[(] _[y, q][′]_[)][does][exist.][Furthermore,][for] any _y_ = _q[′]_ , we have that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0034-03.png)


As _FY_ is continuous, _Y_ = _qβ[⋆]_[almost][surely.] 

Therefore, by differentiation under the integral sign, we obtain: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0034-06.png)


Finally, as _FY_ is also strictly increasing, we get: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0034-08.png)


Building on the marginal quantiles _QY_ , an interesting notion is the conditional quantiles _QY |X_ : it leverages the information of the features _X_ to describe the distribution of _Y_ . Formally, the conditional quantiles portray the conditional distribution of _Y |X_ . This is essential when the underlying distribution is heteroskedastic and the predictive uncertainty varies depending on _X_ , such as in Figures 3.1 and 3.2. 

**Definition 3.1.9** (conditional quantile) **.** 

The _conditional quantile_ of level _β ∈_ [0 _,_ 1] of _Y |X_ , denoted _QY |X_ ( _β_ ), is defined as: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0034-12.png)


Armed with this definition of conditional quantiles, one can perform _quantile regression_ by considering the pinball loss—in place of mean regression based on the quadratic loss—in order to learn the predictive uncertainty of _Y |X_ . 

**Definition 3.1.10** (quantile regression) **.** 

_Quantile regression_ for the level _β ∈_ [0 _,_ 1] aims at minimizing the associated pinball risk, that is solving: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0034-16.png)


Such a _fβ[⋆]_[satisfies][P] � _Y ≤ fβ[⋆]_[(] _[X]_[)] _[ |][X]_ � = _β_ if _FY |X_ is continuous. 

_3.1. Supervised learning context and predictive uncertainty_ 

17 

**Example 3.1.8** (median regression) **.** 

Minimizing the risk associated to the _absolute error ℓ_ ( _y, y[′]_ ) := _|y − y[′] |_ = _ℓ_ 0 _._ 5( _y, y[′]_ ) corresponds to _median regression_ : 

median [ _Y |X_ ] = _QY |X_ (0 _._ 5) _∈_ arg min E _D_ [ _|Y − f_ ( _X_ ) _||X_ ] _. f ∈M_ ( _X ,Y_ ) 

An illustration of quantile regression for various levels _β_ along with the associated pinball losses is provided in Figure 3.3. 

**Remark 3.1.3** (no theoretical guarantees in general) **.** 

One may consider building a predictive intervals (such as the ones illustrated in Figure 3.2) through the conditional quantiles of _Y |X_ . Indeed, using the exact quantiles, we have for any _β ∈_ [0 _,_ 1]: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0035-08.png)


However, as discussed in Section 3.1.2, in practice we do not have access to _QY |X_ ( _·_ ) and we have to estimate it to obtain a _Q_[�] _Y |X_ ( _·_ ) e.g., by minimizing the empirical risk. Then, with a finite number of observations _n_ , in general: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0035-10.png)


Consequently, without further assumptions such as consistency and infinite data or distributional assumptions, quantile regression is not sufficient for providing guaranteed predictive uncertainty quantification. 

## **3.1.5 Framework of interest, its limits and use cases** 

Our goal is to predict _Y ∈Y_ given its covariates _X ∈X_ with a notion of **confidence** , i.e. with a quantification of the predictive uncertainty. Formally, given a _miscoverage rate_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0035-14.png)


**----- Start of picture text -----**<br>
β = 0.05<br>4 2 β = 0.1<br>β = 0.3<br>3 β = 0.5<br>0 β = 0.7<br>β = 0.9<br>2<br>β = 0.95<br>− 2<br>1<br>− 4<br>0<br>− 4 − 2 0 2 4 0 1 2 3 4 5<br>Y − f ( X ) X<br>))<br>( X<br>( Y, f Y<br>ℓβ<br>**----- End of picture text -----**<br>


Figure 3.3: Illustration of quantile regression for various quantile levels _β_ representated by the colors. Left: pinball losses. Right: estimated quantile regressions. 

_Chapter 3. Introduction to Conformal Prediction_ 

18 

_α ∈_ [0 _,_ 1], typically small, we aim at building a _predictive set Cα_ such that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0036-03.png)


where _Cα_ should be as small as possible in order to be informative. Indeed, the predictive set given in Example 3.1.9 which outputs _Y_ with probability 1 _− α_ , and the empty set otherwise, is _exactly_ valid, yet it is critically uninformative. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0036-05.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0036-06.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0036-07.png)


We remind that in practice we only access a data set ( _Xi, Yi_ ) _[n] i_ =1 _[∈]_[(] _[X][× Y]_[)] _[n]_[,][and][aim] at predicting on an unseen individual _Xn_ +1. Therefore, we build an estimator _C_[�] _n,α_ of the predictive sets using a statistical learning algorithm on the training data set, in the objective that it satisfies Equation (MV) (we then say that _C_[�] _n,α_ is _marginally valid_ ) while being as small as possible (we then say that _C_[�] _n,α_ is _efficient_ ). 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0036-09.png)


In this thesis, we study estimators satisfying Equation (MV), to quantify predictive uncertainty in the statistical learning setting. Yet, several constraints typically arise: 

i) The learner generally has access only to a finite number of data points; 

- ii) Data set from the real world derives from unknown distributions. If large deviations are sometimes easy to check, smaller ones can still lead to important statistical failure; 

- iii) The multiplicity and heterogeneity of used models as well as the complexity to finely analyse some of them ask for generic methods that do not assume any specific learning algorithm and can be plugged-in on top of any existing pipeline. 

To answer these concerns, we focus on methods satisfying Equation (MV) on _i_ ) finite sample data sets, in opposition to asymptotic guarantees, _ii_ ) without relying on distributional assumptions with respect to _D_ , and _iii_ ) which can be used with any learning algorithm. 

## **On the importance of the post-hoc design** 

Let us pause here to underline the importance of the last point _iii_ ). We see the estimation of _C_[�] _n,α_ as an add-on to an existing learning pipeline _A_ , which turns the (point) predictions of _A_ into predictive sets with guaranteed coverage, irrespectively of the quality of _A_ on the considered data set. In other words, _C_[�] _n,α_ **can be plugged-in in a post-hoc fashion on top of any** _A_ **, with no impact of the choice of** _A_ **on the validity of Equation (MV)** . Of course, even if the choice of _A_ does not affect Equation (MV), it will nonetheless impact the shape of the predictive sets: the lower the performances of _A_ , the larger the predictive sets will be. This is in fact a good property of our framework as the final user can analyze the quality of the predictive sets to understand how reliable _A_ is on the current task at hand. 

_3.2. Split Conformal Prediction (SCP)_ 

19 

_Conformal prediction_ (CP, Vovk et al., 2005) is a versatile framework achieving Equation (MV) in finite sample with no assumption on the distribution _D_ , and in a post-hoc fashion. Therefore, we focus in this PhD thesis on CP approaches, and the subsequent sections of this introductory chapter are devoted to provide a detailed overview of CP. Before diving into this introduction, let us first pause to highlight exactly the statement of Equation (MV) and how it should be understood. 

**Remark 3.1.4** (no free lunch) **.** 

▶ What type of predictive uncertainty quantification would we like to have? Given historical data ( _Xi, Yi_ ) _[n] i_ =1[and][new][features] _[X][n]_[+1][,][we][would][like][to][find] � _Cn,α_ ( _Xn_ +1) such that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0037-05.png)


which means that the coverage does not vary with _i_ ) the training sample ( _Xi, Yi_ ) _[n] i_ =1 (i.e. no under/over-covering depending on the training set draw) nor _ii_ ) the covariates _Xn_ +1 (e.g., whether we predict on week end or week day). 

▶ What can we have? 

In Equation (MV), the probability is taken not only on the new label _Yn_ +1, but also on the new features _Xn_ +1 as well as on the training set ( _Xi, Yi_ ) _[n] i_ =1[(through] � _Cn,α_ ). In fact, as developed in Section 3.3.2, the previous wish Equation (UQ dream) is impossible to achieve under our set of assumptions. On the one hand, we will see that it achieving conditional validity on the covariates _Xn_ +1 in an informative distribution-free fashion is impossible. On the other hand, we will also see that some CP approaches still manage to ensure some form of conditional validity on the training set. 

Given Remark 3.1.4, CP predictive sets do not have to be understood as a “magic wand” to probabilistic prediction and predictive uncertainty quantification. We believe that CP should be used as a last protective layer to be plugged-in after the best learning pipeline that can be designed, tailored for the application at hand. The strength of CP is precisely that it can be used in combination with any learning pipeline and still provide a valid marginal guarantee, leading to robust prediction if the underlying pipeline is corrupted, and achieving stronger guarantees than expected otherwise. 

However, developing extensions of CP that refines the guarantee is of great interest. It constitutes a branch of the literature, that we will discuss hereafter. 

## **3.2 Split Conformal Prediction (SCP)** 

We start this introductive overview of CP by presenting Split CP (SCP, Vovk et al., 2005; Papadopoulos et al., 2002; Lei et al., 2018). Historically, SCP was introduced after Full CP, and is in fact a particular case of it. However, we find it more pedagogical to start with SCP. 

_Chapter 3. Introduction to Conformal Prediction_ 

20 

## **3.2.1 Standard mean-regression case and exchangeability** 

Let us begin by explaining SCP in the very simple case where the base learning algorithm _A_ performs mean-regression and outputs a function _µ_ ˆ based on some training data. 

SCP first splits the _n_ points of the training set into two disjoint sets Tr _,_ Cal _⊂_ �1 _, n_ �, to create a _proper training set_ , Tr of size #Tr, and a _calibration set_ , Cal of size # _Cal_ . On the proper training set, a mean-regression model _µ_ ˆ (chosen by the user) is fitted, and then used to predict on the calibration set. _Conformity scores s_ ( _x, y_ ; ˆ _µ_ ) := _|y − µ_ ˆ( _x_ ) _|_ are computed to assess how well the fitted model _µ_ ˆ predicts the response values of the calibration points, forming the set _S_ = �( _Si_ := _s_ ( _Xi, Yi_ ; ˆ _µ_ )) _i∈_ Cal� _∪{_ + _∞}_ . Finally, the (1 _− α_ )-th quantile of these scores _q_ 1 _−α_ ( _S_ ) is computed to define the size of the predictive interval: _C_[�] _n,α_ ( _·_ ) := [ˆ _µ_ ( _·_ ) _± q_ 1 _−α_ ( _S_ )]. 

ˆ **Remark 3.2.1** ( _µ_ can be independent of Tr) **.** 

When we say that “ ˆ _µ_ is fitted on the proper training set”, we include the extreme case where _µ_ ˆ is in fact independent of Tr, e.g., when obtaining a model from a third party. The important point is that _µ_ ˆ has to be independent of the calibration set. 

## **Remark 3.2.2** (on the + _∞_ in _S_ ) **.** 

When forming the set of scores _S_ , we have cautiously added + _∞_ . This is crucial to ensure finite sample guarantees: ideally we would like to use the true quantile of the scores’ distribution but once again, this quantity is unknown, and to estimate it we apply a finite-sample correction. See Lemma 3.2.1 for a formal derivation. One can think of it as including a worst-case scenario for the unknown value of _s_ ( _Xn_ +1 _, Yn_ +1; ˆ _µ_ ). In 1 fact, this is strictly equivalent to taking the �(1 _− α_ ) �1 + #Cal �� empirical quantile of �( _s_ ( _Xi, Yi_ ; ˆ _µ_ )) _i∈_ Cal�. 

An illustration is provided in Figure 3.4 in the case where _d_ = 1, i.e. when there is only one explanatory variable. We present in Algorithm 1 the pseudo-code of SCP in the particular case explained above. 

Let us now state formally the theoretical guarantees enjoyed by Algorithm 1. As the calibration set is used to estimate the quantiles of the “errors” made by _µ_ ˆ and infer their order of magnitude at test time, we intuit that if the calibration and test points are i.i.d. then we could show that this method achieves Equation (MV). In fact, we only need a weaker notion than i.i.d. which allows for some dependence structure: _exchangeability_ . 

**Definition 3.2.1** (exchangeability) **.** 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0038-12.png)


_Toy case: Z_ 1 and _Z_ 2 are exchangeable if ( _Z_ 1 _, Z_ 2) = ( _[d] Z_ 2 _, Z_ 1). 

Exchangeability implies that the ( _Xi, Yi_ ) _[n] i_ =1[are identically distributed.][Denoting] _[ D]_[ their] 

_3.2. Split Conformal Prediction (SCP)_ 

21 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0039-02.png)


**----- Start of picture text -----**<br>
Train Cal Test<br>2<br>▶ Create a proper training set, a cal-<br>0<br>Step 1 ibration set, and keep the test set,<br>by randomly splitting the data set<br>− 2<br>0 2 4<br>X<br>2<br>0 On the proper training set:<br>Step 2 − 2 ▶ Learn (or get) µ ˆ<br>0 2 4<br>X<br>On the calibration set:<br>2<br>▶ Predict with µ ˆ<br>0<br>▶ Get the | residuals | , a.k.a.<br>Step 3 conformity scores<br>− 2<br>▶ Compute the (1 −α ) empirical quan-<br>tile of  S =  {| residuals |} Cal ∪{ + ∞} ,<br>0 2 4<br>X noted q 1 −α  ( S )<br>2<br>On the test set:<br>0<br>Step 4 ▶ Predict with µ ˆ<br>− 2 ˆ<br>▶ Build C [�] n,α ( x ): [ µ ( x )  ± q 1 −α  ( S )]<br>0 2 4<br>X<br>Y<br>Y<br>Y<br>Y<br>**----- End of picture text -----**<br>


Figure 3.4: Schematic illustration of the Split Conformal Prediction procedure. Special case of a mean-regression task, with the absolute value of the residuals as conformity scores. 

_Chapter 3. Introduction to Conformal Prediction_ 

22 

**Algorithm 1** SCP in mean-regression using the absolute value of the residuals as conformity scores 

**Input:** Mean-regression algorithm _A_ , miscoverage rate _α_ , training set ( _Xi, Yi_ ) _[n] i_ =1 **Output:** Prediction interval _C_[�] _n,α_ 

Calib. Train 

1: Randomly split the training data ( _Xi, Yi_ ) _[n] i_ =1[into][a][proper][training][set][(size][#][Tr][)][and] a calibration set (size #Cal) 

2: Get _µ_ ˆ ( _by training A on the proper training set_ ( _Xi, Yi_ ) _i∈_ Tr) 

3: On the calibration set, get prediction values with _µ_ ˆ 

4: Obtain a set of #Cal + 1 conformity scores : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0040-09.png)


Obtain a set of #Cal conformity scores: _S_ = _{Si, i ∈_ Cal _}_ 

5: Compute the 1 _− α_ quantile of these scores: _q_ 1 _−α_ ( _S_ ) 

1 Compute the �(1 _− α_ ) �1 + #Cal �� quantile of these scores: _q_ 1 _−α_ ( _S_ ) 

6: For a new point _Xn_ +1, return 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0040-14.png)


marginal distribution as earlier, we note _D_[exch(] _[n]_[)] the set of exchangeable joint distributions of marginal _D_ . 

**Example 3.2.1** (i.i.d.) **.** 

An i.i.d. sequence is exchangeable. 

**Example 3.2.2** (sampling without replacement) **.** 

A sequence ( _U_ 1 _, . . . , Un_ ) obtained through sampling without replacement from _{u_ 1 _, . . . , un}_ is exchangeable (but not i.i.d.). 

**Example 3.2.3** (multivariate gaussian) **.** 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0040-21.png)


**----- Start of picture text -----**<br>
m σ [2]<br>   <br>   2 <br> ...   ... γ <br>The components of N  ...  ,  γ [2] ...  with m ∈ R, ( σ, γ )  ∈ R [2] + [,]<br> m   σ [2] <br>are exchangeable even when γ = 0 (thus even when they are not independent).<br>**----- End of picture text -----**<br>


Equipped with the notion of exchangeability, we can now show that SCP for meanregression with absolute value of the residuals as conformity score (Algorithm 1) achieves Equation (MV) for any sample size, whatever the learning algorithm _A_ is and for any distribution _D_ as long as ( _Xi, Yi_ ) _[n] i_ =1[+1] _[∼D]_[E][(] _[n]_[+1)] _[∈D]_[exch(] _[n]_[+1)][(][Vovk][et][al.][,][2005][;][Papadopoulos] 

_3.2. Split Conformal Prediction (SCP)_ 

23 

et al., 2002; Lei et al., 2018). 

**Theorem 3.2.1** (marginal validity of SCP—mean-regression, absolute residuals) **.** 

SCP for mean-regression with absolute value of the residuals as conformity score (Algorithm 1) outputs _C_[�] _n,α_ such that for any distribution _D_ , for any associated exchangeable joint distribution _D_[E][(Cal] _[∪{][n]_[+1] _[}]_[)] _∈D_[exch(Cal] _[∪{][n]_[+1] _[}]_[)] : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0041-05.png)


Additionally, if the scores _{Si}i∈_ Cal _∪{Sn_ +1 _}_ are almost surely (a.s.) distinct: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0041-07.png)


We defer the remarks of Theorem 3.2.1 after its proofs, which relies on the following quantile lemma 3.2.1 (see also Tibshirani et al., 2019). 

**Lemma 3.2.1** (quantile lemma) **.** 

If ( _U_ 1 _, . . . , Un, Un_ +1) are exchangeable, then for any _β ∈_ ]0 _,_ 1[: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0041-11.png)


Additionally, if _U_ 1 _, . . . , Un, Un_ +1 are almost surely distinct, then: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0041-13.png)


_Proof._ Let _β ∈_ ]0 _,_ 1[. 

First, observe that _{Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un,_ + _∞_ ) _} ⇐⇒{Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1) _}_ . By exchangeability, and using Lemma 3.2.2 with the function 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0041-16.png)


we obtain that for any _i ∈_ �1 _, n_ +1�: _{Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un_ +1) _}_ = _[d] {Ui ≤ qβ_ ( _U_ 1 _, . . . , Un_ +1) _}_ . _d_ Therefore, for any _i ∈_ �1 _, n_ + 1�, it holds that P ( _Un_ +1 _≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)) = P ( _Ui ≤ qβ_ ( _U_ 1 _, . . . , Un, Un_ +1)). Thus: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0041-18.png)


_Chapter 3. Introduction to Conformal Prediction_ 

24 

proving the first statement. 

For the second statement, remark that by definition of _qβ_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0042-04.png)


By exchangeability and the fact that there are no ties ( _U_ 1 _, . . . , Un, Un_ +1 are a.s. distinct), rank( _Un_ +1) _∼U_ ( _{_ 1 _, . . . , n_ + 1 _}_ ). Thus: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0042-06.png)


_Proof of Theorem 3.2.1._ When ( _Xi, Yi_ ) _[n] i_ =1[+1][are][exchangeable,][the][scores] _[{][S][i][}][i][∈]_[Cal] _[ ∪{][S][n]_[+1] _[}]_ are exchangeable, due to Lemma 3.2.2 with the function _g_ ( _Xi, Yi_ ) _[n] i_ =1[+1] := ( _|Yi − µ_ ˆ ( _Xi_ ) _|_ ) _[n] i_ =1[+1][.] � � Therefore, applying the quantile lemma to the scores concludes the proof, as: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0042-08.png)


**Lemma 3.2.2** (function of exchangeable sequences) **.** 

Let ( _U_ 1 _, . . . , Un, Un_ +1) be exchangeable. Let _σ_ be a permutation on �1 _, n_ + 1�. For any random function _g_ such that _g_ ( _·_ ) = _h_ ( _·_ ; _ξ_ ) with _h_ a deterministic function, and _ξ_ encoding the randomness of _g_ and independent of ( _U_ 1 _, . . . , Un, Un_ +1), it holds: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0042-11.png)


This includes the particular case where _g_ is a deterministic function. 

The strength of Theorem 3.2.1 is that the coverage holds for any finite sample size, for any data distribution _D_ as long as the data set is exchangeable, and whatever the quality of the fitted model _µ_ ˆ is. Again, if _µ_ ˆ is a bad predictor (e.g., predicting constantly 10 when the data is distributed as in Figure 3.4) then the length of the predictive interval is critically large. But precisely, this can be used as a diagnostic tool indicating that the modelisation is not tailored for the underlying problem. 

**Remark 3.2.3** (the upper bound is not sufficient for efficiency) **.** 

Talking about efficiency, the upper bound in Theorem 3.2.1 decreases with the calibration size. This is a positive result as an efficient predictive interval will achieve exactly 1 _− α_ coverage, but it is not a sufficient condition for efficiency. Indeed, again, the naive predictor presented in Example 3.1.9 has a probability of coverage of exactly 1 _− α_ but is critically unefficient. 

_3.2. Split Conformal Prediction (SCP)_ 

25 

**Remark 3.2.4** (the guarantee is conditional on Tr) **.** 

Importantly, remark here that the probability is taken over _D_[E][(Cal] _[∪{][n]_[+1] _[}]_[)] , excluding the proper training set Tr: the validity is _conditional_ on Tr, thus the validity holds conditionally on the fitted model _µ_ ˆ, regardless of its accuracy. 

**Remark 3.2.5** (the guarantee is not conditional on _X_ ) **.** 

However, we insist again here that the probability controlled in Theorem 3.2.1 is not conditional neither on the training data nor on the test features _Xn_ +1. In particular, for _x ∈X_ , P _Yn_ +1 _∈ C_[�] _n,α_ ( _Xn_ +1) _|Xn_ +1 = _x ≥_ 1 _− α_ . � � 

Through SCP with absolute value of the mean-residuals, we move from a situation where two quantile regressions do not have any form of validity in finite sample and could under-cover drastically (Figure 3.5a), to a setting where we do achieve marginal validity in finite sample for any distribution (Figure 3.5b). However, in practice, one usually aims at _X_ -conditional coverage (Figure 3.5c), a guarantee that is not achieved by SCP in meanregression using the absolute value of the residuals as conformity scores. _X_ -conditionally valid predictive sets are such that the random variable which is _the indicator of coverage is independent of X_ , i.e. a point is equally likely to be covered whatever is the _X_ -draw. 

While marginal coverage allows the distribution of the indicator of coverage to vary across regions of the features space, i.e. the predictive sets can be non-adaptive, the stronger notion of _X_ -conditional coverage ensures that the indicator of coverage is evenly distributed, i.e. the predictive sets are fully adaptive. These differences are illustrated in Figure 3.5. Therefore, a _X_ -conditionally valid estimator of the predictive sets is necessarily adaptive to _X_ . 

However, SCP as described in the previous Section 3.2.1 is critically non-adaptive as its predictive intervals depend on the features _x_ only through the intervals’ location, but their shape is constant (symmetric and constant length accross the features space). One could think that a better methodology’s design would then lead to guaranteed _X_ -conditional coverage. Unfortunately, this is all the more wrong. As shown in Vovk (2012); Lei and Wasserman (2014); Barber et al. (2021a) and detailed later in Section 3.3.2, it is impossible to achieve _informative X_ -conditional validity under our set of assumptions. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0043-09.png)


**----- Start of picture text -----**<br>
2 2 2<br>0 0 0<br>− 2 − 2 − 2<br>− 4 − 4 − 4<br>0 2 4 0 2 4 0 2 4<br>X X X<br>(a) No nominal coverage (b) Marginal coverage (c) X -conditional coverage<br>Y Y Y<br>**----- End of picture text -----**<br>


Figure 3.5: Illustration of various notion of coverage. 

_Chapter 3. Introduction to Conformal Prediction_ 

26 

## **Informal theorem** 

Without distribution assumption, in finite sample, a perfectly _X_ -conditionally valid � � _Cn,α_ is such that P measure _Cn,α_ ( _x_ ) = _∞ ≥_ 1 _− α_ for any non-atomic _x_ . � � � � 

In practice, as one can not accept to only have marginal coverage even empirically (see Figure 3.5b), there have been important research effort to get closer to _X_ -conditional coverage. We can separate this line of work into two different branches: one trying to achieve some form of approximate conditional coverage in finite sample, i.e. they target P _D_ E( _n_ +1) _Yn_ +1 _∈ C_[�] _n,α_ ( _Xn_ +1) _|Xn_ +1 _∈V_ ( _x_ ) _≥_ 1 _− α_ with _V_ ( _x_ ) representing some region � � or neighbourhood around _x_ (Romano et al., 2020a; Guan, 2022; Jung et al., 2023; Gibbs et al., 2023, to name just a few), relying on the fact that the impossibility result naturally only holds for non-atomic points _x_ , and on any atomic _x_ an instinctive idea is to only calibrate with calibration points for which _Xi_ = _x, i ∈_ Cal (this is related to Mondrian CP which groups data points according to a family of groups _G_ to achieve _G_ -conditional validity, Vovk et al., 2005); and the other one aiming at asymptotic (with the sample size) _X_ -conditional coverage based on the intuition that enjoying asymptotic theoretical guarantees goes hand in hand with enhanced empirical performances, these works are usually based on estimating the overall c.d.f. or p.d.f. of the data using consistent estimators (Romano et al., 2019; Kivaranovic et al., 2020; Cauchois et al., 2021; Chernozhukov et al., 2021; Sesia and Romano, 2021; Izbicki et al., 2022, among others). In the next subsection, we present one of them (Conformalized Quantile Regression, Romano et al., 2019) as it played a key role in the growing interest of the machine learning community towards CP, and is one of the most used CP algorithm in practice. 

## **3.2.2 Conformalized Quantile Regression (CQR)** 

Conformalized Quantile Regression (CQR, Romano et al., 2019) first splits the _n_ points of the training set into two disjoint sets Tr _,_ Cal _⊂_ �1 _, n_ �, to create a _proper training set_ , Tr, and a _calibration set_ , Cal. On the proper training set, two quantile regression algorithms (chosen by the user) are fitted (QR[�] lower and QR[�] upper), and then used to predict on the calibration set. _Conformity scores s_ � _x, y_ ; QR[�] lower _,_ QR[�] upper� := max �QR�lower( _x_ ) _− y, y −_ QR[�] upper( _x_ )� are computed to assess how well the fitted interval predicts the response values of the calibration points, forming the set _S_ = �� _Si_ := _s_ � _Xi, Yi_ ; QR[�] lower _,_ QR[�] upper�� _i∈_ Cal� _∪{_ + _∞}_ . Finally, the (1 _− α_ )-th quantile of these scores _q_ 1 _−α_ ( _S_ ) is computed to define the correction � of the predictive interval: _C_[�] _n,α_ ( _·_ ) := �QRlower( _·_ ) _− q_ 1 _−α_ ( _S_ ) ; QR[�] upper( _·_ ) + _q_ 1 _−α_ ( _S_ )�. An illustration of CQR is given in Figure 3.6 for _d_ = 1. Contrary to Figure 3.4, we use a heteroskedastic distribution to illustrate the impact and interest of the quantile regressions. The idea behind the new conformity scores is the following: the score is negative for any point that belongs to the initial interval, and positive otherwise (see also Step 2 in Figure 3.6). Hence, if the initial interval is too sharp (resp. overly conservative) then more (resp. less) than _α_ of the scores will be positive, leading to a positive (resp. negative) _q_ 1 _−α_ ( _S_ ) and thus the final interval will be enlarged (resp. shrinked) in comparison with the initial interval, when adding _q_ 1 _−α_ ( _S_ ) to its bound. Finally, the value of the scores 

_3.2. Split Conformal Prediction (SCP)_ 

27 

## **Algorithm 2** CQR 

**Input:** Quantile regression algorithm _A_ , miscoverage rate _α_ , training set ( _Xi, Yi_ ) _[n] i_ =1 **Output:** Prediction interval _C_[�] _n,α_ 

Calib. Train 

1: Randomly split the training data ( _Xi, Yi_ ) _[n] i_ =1[into][a][proper][training][set][(size][#][Tr][)][and] a calibration set (size #Cal) 

2: Get QR[�] lower and QR[�] upper ( _by training A on the proper training set_ ( _Xi, Yi_ ) _i∈_ Tr) 

3: On the calibration set, get prediction values with QR[�] lower and QR[�] upper 

4: Obtain a set of #Cal + 1 conformity scores : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0045-09.png)


Obtain a set of #Cal conformity scoress: _S_ = _{Si, i ∈_ Cal _}_ 

5: Compute the 1 _− α_ quantile of these scores: _q_ 1 _−α_ ( _S_ ) 

1 Compute the �(1 _− α_ ) �1 + #Cal �� quantile of these scores: _q_ 1 _−α_ ( _S_ ) 

6: For a new point _Xn_ +1, return 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0045-14.png)


reflect how far the point is from the initial interval bound, conveying the information of how much enlargement or shrinkage is required to ensure marginal validity. Algorithm 2 provides a formal description. 

Note that, exactly as for SCP for mean-regression with absolute values of the residuals as conformity scores, Remarks 3.2.1 and 3.2.2 (stating that the fitted model can in fact be independent of Tr, and explaning the reason behind the + _∞_ ) apply to CQR. Due to the very same reason, one can start to feel that in fact SCP in mean-regression with absolute values of the residuals as conformity scores and CQR share the same construction. We will formalize this intuition further in Section 3.2.3. For now we state the theoretical validity of CQR, from Romano et al. (2019). 

**Theorem 3.2.2** (marginal validity of CQR) **.** 

CQR (Algorithm 2) outputs _C_[�] _n,α_ such that for any distribution _D_ , for any associated exchangeable joint distribution _D_[E][(Cal] _[∪{][n]_[+1] _[}]_[)] _∈D_[exch(Cal] _[∪{][n]_[+1] _[}]_[)] : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0045-19.png)


Additionally, if the scores _{Si}i∈_ Cal _∪{Sn_ +1 _}_ are almost surely (a.s.) distinct: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0045-21.png)


_Chapter 3. Introduction to Conformal Prediction_ 

28 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0046-02.png)


**----- Start of picture text -----**<br>
Train Cal Test<br>2<br>0 ▶ Create a proper training set, a cal-<br>Step 1 ibration set, and keep the test set,<br>− 2 by randomly splitting the data set<br>− 4<br>0 2 4<br>X<br>2<br>0<br>On the proper training set:<br>Step 2 − 2 ▶ Learn (or get) QR [�] lower and QR [�] upper<br>− 4<br>0 2 4<br>X<br>+ + + + + + On the calibration set:<br>+ +<br>▶ Predict with QR [�] lower and QR [�] upper<br>Step 3 - - ▶ Get the scores  S =  {Si} Cal  ∪{ + ∞}<br>-<br>- - - +<br>+ ▶ Compute the (1 −α ) empirical quan-<br>tile of S , noted q 1 −α  ( S )<br>�<br>�→ Si := max �QRlower ( Xi )  − Yi, Yi − QR [�] upper ( Xi )�<br>2 On the test set:<br>0 ▶ Predict with QR [�] lower and QR [�] upper<br>Step 4 − 2 ▶ Build� �<br>Cn,α ( x ) = QRlower( x )  − q 1 −α  ( S );<br>�<br>− 4 �<br>0 2 4 QRupper( x ) +  q 1 −α  ( S )�<br>X<br>Y<br>Y<br>Y<br>**----- End of picture text -----**<br>


Figure 3.6: Schematic illustration of the Conformalized Quantile Regression procedure. 

_3.2. Split Conformal Prediction (SCP)_ 

29 

_Proof._ First, on any ( _Xi, Yi_ ) _[n] i_ =1[+1][exchangeable][sequence,][CQR][builds][scores] _[{][S][i][}] i∈_ Cal _[∪] {Sn_ +1 _}_ that are exchangeable due to Lemma 3.2.2. Then, observe that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0047-03.png)


Note that this last equation is equivalent to Equation (3.1) above. Now, it only remains to apply the quantile lemma 3.2.1 to conclude the proof. 

Remarks 3.2.4 and 3.2.5 apply to CQR as well: it is valid conditionally to Tr, and, importantly, even though it does improve _X_ -conditional coverage in practice, it does not enjoy theoretical guarantees on this. This is expected given our discussion on the impossibility of _X_ -conditional coverage in Section 3.3.2. It is even more expected as CQR is adaptive on _X_ only through the quantile regression, while the conformal scores and correction are independent of _X_ : the key step that is devoted to retrieving validity is independent of _X_ , thus there was no hope for finite sample disitribution-free _X_ -conditional validity by design. However, Sesia and Candès (2020) provides asymptotic guarantees on _X_ -conditional validity of CQR under consistency of the quantile regression algorithm. 

**Remark 3.2.6** (CQR validity holds regardless of the quantile regression levels) **.** The marginal validity of CQR holds for any quantile regression algorithm. This means that in particularly, the levels of these quantile regressions can be picked arbitrarily. While a natural choice might be lower = _α/_ 2 and upper = 1 _− α/_ 2, Romano et al. (2019) suggest to choose them via cross-validation as it seems to enhance the resulting intervals’ efficiency. 

## **3.2.3 Generalization of SCP: going beyond regression** 

As hinted by the design of Algorithms 1 and 2 and the proofs of the associated Theorems 3.2.1 and 3.2.2, SCP with absolute value of mean-regression residuals and CQR are in fact two particular instances of a global algorithm, SCP, that is general enough to even tackle the classification problems. SCP is a wrapper around any learning algorithm _A_ (e.g., any mean regressor for Algorithm 1, or any quantile regressor for Algorithm 2) that is fitted on an 

_Chapter 3. Introduction to Conformal Prediction_ 

30 

## **Algorithm 3** General SCP 

**Input:** Learning algorithm _A_ , conformity score function _s_ , miscoverage rate _α_ , training set ( _Xi, Yi_ ) _[n] i_ =1 **Output:** Prediction set _C_[�] _n,α_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0048-04.png)


1: Randomly split the training data ( _Xi, Yi_ ) _[n] i_ =1[into][a][proper][training][set][(size][#][Tr][)][and] a calibration set (size #Cal) 

2: Get _A_[ˆ] ( _by training A on the proper training set_ ( _Xi, Yi_ ) _i∈_ Tr) 

3: On the calibration set, obtain a set of #Cal + 1 conformity scores : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0048-08.png)


▶ SCP absolute value of the mean-residuals (Algorithm 1): _s x, y_ ; _A_[ˆ] := _|y − µ_ ˆ ( _x_ ) _|_ � � � ▶ CQR (Algorithm 2): _s_ � _x, y_ ; _A_[ˆ] � := max �QRlower( _x_ ) _− y, y −_ QR[�] upper( _x_ )� 

4: Compute the 1 _− α_ quantile of these scores: _q_ 1 _−α_ ( _S_ ) 

- 5: For a new point _Xn_ +1, return 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0048-12.png)


In particular cases, this set boils down to: ▶ _C_[�] _n,α_ ( _Xn_ +1) = [ˆ _µ_ ( _Xn_ +1) _± q_ 1 _−α_ ( _S_ )] in SCP absolute value of the mean-residuals � ▶ _C_[�] _n,α_ ( _Xn_ +1) = �QRlower ( _Xn_ +1) _− q_ 1 _−α_ ( _S_ ) ; QR[�] upper ( _Xn_ +1) + _q_ 1 _−α_ ( _S_ )� in CQR 

independent training set to produce _A_[ˆ] : given a conformity score function tailored to the learning algorithm _A_ (e.g., absolute value of the residuals in Algorithm 1, or the signed score of Algorithm 2), used to construct _S_ = _s Xi, Yi_ ; _A_[ˆ] _∪{_ + _∞}_ in order to �� � �� _i∈_ Cal� assess how well the fitted model _A_[ˆ] predicts the response values of the calibration points, it builds a predictive set containing only the labels leading to a score on _Xn_ +1 which is smaller than a 1 _− α_ fraction of the calibration scores, i.e. _{y ∈Y_ such that _s_ ( _x, y_ ; _A_[ˆ] ) _≤ q_ 1 _−α_ ( _S_ ) _}_ . A pseudo-code of SCP is provided in Algorithm 3. 

**Theorem 3.2.3** (marginal validity of SCP) **.** 

SCP (Algorithm 3) outputs _C_[�] _n,α_ such that for any distribution _D_ , for any associated exchangeable joint distribution _D_[E][(Cal] _[∪{][n]_[+1] _[}]_[)] _∈D_[exch(Cal] _[∪{][n]_[+1] _[}]_[)] : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0048-17.png)


Additionally, if the scores _{Si}i∈_ Cal _∪{Sn_ +1 _}_ are almost surely (a.s.) distinct: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0048-19.png)


_Proof._ First, on any ( _Xi, Yi_ ) _[n] i_ =1[+1][exchangeable][sequence,][SCP][builds][scores] _[{][S][i][}] i∈_ Cal _[∪] {Sn_ +1 _}_ that are exchangeable due to Lemma 3.2.2. Then, it only remains to apply the 

_3.2. Split Conformal Prediction (SCP)_ 

31 

quantile lemma 3.2.1. 

**Remark 3.2.7** (randomized SCP) **.** 

To ensure that the upper bound always holds, even when ties among scores occur with non-zero probability, one can add a randomization in SCP algorithm. Formally, before introducing this tie-breaking randomization, let us first rewrite the predictive set: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0049-05.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0049-06.png)


## **3.2.4 Some examples of SCP in classification** 

The generalized framework introduced in the previous section does not make any assumption on the label space _Y_ . Indeed, while we have only introduced regression-tailored algorithm so far, SCP–and more generally CP– is general enough to encapsulate classification tasks. Let us focus here in presenting two traditional SCP algorithms for classification. 

The framework is the following. Assume that the label space is _Y_ = _{_ 1 _, . . . , C} ⊆_ N _[∗]_ where _C_ = # _Y_ is the number of classes. We consider that the learning algorithm fits a ˆ model _A_[ˆ] _[not.]_ = _p_ , which is a function that outputs a vector of estimated probabilities for each class (e.g., after a softmax layer). 

ˆ A first idea of tailored conformity scores is s ( _x, y_ ; ˆ _p_ ) = 1 _− p_ ( _x_ ) _y_ . Indeed, by doing so the score is large (resp. small) when the model predicts a low (resp. high) estimated probability on the true class. Note that now, the predictive set _C_[�] _n,α_ ( _Xn_ +1) = _{y_ such that s ( _Xn_ +1 _, y_ ; ˆ _p_ ) _≤ q_ 1 _−α_ ( _S_ ) _}_ does not boil down to any explicit expression, and we have to try all the possible _y_ . As _Y_ is finite, unlike in the regression setting, this task is doable. Examples 3.2.4 and 3.2.5 provide a toy example of how such an algorithm would work in practice. In these examples, we emphasize that ( _i_ ) the quality of the fitted model impacts the size of the predictive set (to see this, compare the predictive set of Example 3.2.4 to the one of Example 3.2.5), as discussed previously; ( _ii_ ) the level of difficulty to predict on test point is poorly reflected in the predictive set (to see this, the text in gray shows that the final predictive sets stay constant on a different prediction). Point ( _ii_ ) is due to 

_Chapter 3. Introduction to Conformal Prediction_ 

32 

the design of the conformity score, see Remark 3.2.8. 

**Remark 3.2.8** (efficiency yet non-adaptivity of the simplest classification scores) **.** 

While this conformity score function allows to output the most efficient set possible (i.e. achieving the smallest average set size, Sadinle et al., 2018), it does not allow to discriminate between “easy” and “hard” test point. In practice, it leads to predictive sets that under-cover (resp. over-cover) on “hard” (resp. “easy”) subgroups. This is due to the fact that the same threshold _q_ 1 _−α_ ( _S_ ) is applied to any test point. 

## **Example 3.2.4** (toy use case of classification SCP with the simplest score) **.** 

Let consider a toy use case where we want to classify households according to the best electricity tariff to propose them in order to align electricity production and consumption (this is a simplified example of demand-side management). In this context, assume _Y_ = _{_ “N” _,_ “B” _,_ “D” _}_ where “N” stands for neutral (constant standard tariff), “B” stands for bitariff (such as (off)-peak hours, with lower and higer tariffs) and “D” stands for dynamic (i.e. the price switches between low, standard and high tariffs depending of the day with 2 days early notice to the consumers). 

We want to build predictive sets at the level _α_ = 0 _._ 1, and we have access to a calibration data set with #Cal = 10 points. 

▶ model 

1. Compute the scores on the calibration set using s ( _x, y_ ; ˆ _p_ ) = 1 _− p_ ˆ( _x_ ) _y_ . 

|1. Compu|te the scores on the calibration set using<br>s (_x, y_;ˆ_p_) = 1_−_ˆ_p_(_x_)_y_.|
|---|---|
|_Yi, i ∈_Cal|“N”<br>“N”<br>“N”<br>“B”<br>“B”<br>“B”<br>“B”<br>“D”<br>“D”<br>“D”|
|ˆ_p_N(_Xi_)<br>ˆ_p_B(_Xi_)<br>ˆ_p_D(_Xi_)|0.95<br>0.02<br>0.03<br>0.90<br>0.05<br>0.05<br>0.85<br>0.10<br>0.05<br>0.15<br>0.60<br>0.25<br>0.15<br>0.55<br>0.30<br>0.20<br>0.50<br>0.30<br>0.15<br>0.45<br>0.40<br>0.15<br>0.40<br>0.45<br>0.25<br>0.35<br>0.40<br>0.20<br>0.45<br>0.35|
|_Si_<br>0.05<br>0.1<br>0.15<br>0.40<br>0.45<br>0.50<br>0.55<br>0.55<br>0.6<br>0.65<br>Defne _S_ =_{Si, i ∈_Cal_} ∪{_+_∞}._||



2. Compute their empirical quantile: _q_ 1 _−α_ ( _S_ ) = 0 _._ 65. 

3. Predict on a new point _Xn_ +1: _p_ ˆ( _Xn_ +1) = (0 _._ 05 _,_ 0 _._ 60 _,_ 0 _._ 35). 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0050-13.png)


**----- Start of picture text -----**<br>
(or less predictable: p ˆ( Xn +1) = (0 . 25 ,  0 . 4 ,  0 . 35))<br>4. For each possible label, evaluate the scores on this new point<br>�→ s ( Xn +1 ,  “N”; ˆ p ) = 0 . 95 (or 0.75) “N” ∈/ C [�] n,α  ( Xn +1)<br>�→ s ( Xn +1 ,  “B”; ˆ p ) = 0 . 40  ≤ q 1 −α ( S ) (or 0 . 6 ≤ q 1 −α  ( S )) “B” ∈ C [�] n,α  ( Xn +1)<br>�→ s ( Xn +1 ,  “D”; ˆ p ) = 0 . 65  ≤ q 1 −α ( S ) (or 0 . 65 ≤ q 1 −α  ( S )) “D” ∈ C [�] n,α  ( Xn +1)<br>5. Form the predictive set associated to Xn +1: C [�] n,α  ( Xn +1) =  { “B”, “D” } .<br>**----- End of picture text -----**<br>


_3.2. Split Conformal Prediction (SCP)_ 

33 

**Example 3.2.5** (toy use case of classification SCP with the simplest score) **.** Let consider again the demand-side management toy use case where _Y_ = _{_ “N” _,_ “B” _,_ “D” _}_ , and we wish to build predictive sets at the level _α_ = 0 _._ 1. Assume we have access to a calibration data set with #Cal = 10 points. ▶ Confident fitted model 

1. Compute the scores on the calibration set (compared to the previous example above, the subsequent scores are less uniform as we illustrate the case where the underlying model is more truthfully confident). 

_Yi, i ∈_ Cal “N” “N” “N” “B” “B” “B” “B” “D” “D” “D” _p_ ˆN( _Xi_ ) 0.95 0.90 0.85 0.05 0.05 0.05 0.05 0.10 0.10 0.15 _p_ ˆB( _Xi_ ) 0.02 0.05 0.10 0.85 0.80 0.75 0.70 0.25 0.30 0.30 _p_ ˆD( _Xi_ ) 0.03 0.05 0.05 0.10 0.15 0.20 0.25 0.65 0.60 0.55 _Si_ 0.05 0.1 0.15 0.15 0.20 0.25 0.30 0.35 0.40 0.45 Define _S_ = _{Si, i ∈_ Cal _} ∪{_ + _∞}._ 

2. Compute their empirical quantile: _q_ 1 _−α_ ( _S_ ) = 0 _._ 45. 

3. Predict on a new point _Xn_ +1: _p_ ˆ( _Xn_ +1) = (0 _._ 05 _,_ 0 _._ 60 _,_ 0 _._ 35). 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0051-07.png)


**----- Start of picture text -----**<br>
(or more predictable: p ˆ( Xn +1) = (0 . 05 ,  0 . 9 ,  0 . 05))<br>**----- End of picture text -----**<br>


4. For each possible label, evaluate the scores on this new point _Xn_ +1. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0051-09.png)


**----- Start of picture text -----**<br>
�→ s ( Xn +1 ,  “N”; ˆ p ) = 0 . 95 (or 0.95) “N” ∈/ C [�] n,α  ( Xn +1)<br>�→ s ( Xn +1 ,  “B”; ˆ p ) = 0 . 40  ≤ q 1 −α ( S ) (or 0 . 1 ≤ q 1 −α  ( S )) “B” ∈ C [�] n,α  ( Xn +1)<br>�→ s ( Xn +1 ,  “D”; ˆ p ) = 0 . 65 (or 0.95) “D” ∈/ C [�] n,α  ( Xn +1)<br>**----- End of picture text -----**<br>


5. Form the predictive set associated to _Xn_ +1: _C_[�] _n,α_ ( _Xn_ +1) = _{_ “B” _}_ . 

Other conformity score functions can be used to alleviate this issue and improve adaptiveness. One of them was proposed in Romano et al. (2020b) and is based on the intuitive idea that one may want to include classes by decreasing order of estimated probabilities until reaching a theoretically valid threshold, that might be different from 1 _− α_ . Formally, given ˆ a predictor of estimated probabilities _p_ ( _·_ ), for any _x ∈X_ define _σx_ : _{_ 1 _, . . . ,_ # _Y} �→Y_ such ˆ ˆ that _p_ ( _x_ ) _σx_ (1) _≥ . . . ≥ p_ ( _x_ ) _σx_ (# _Y_ ). In other words, _σx_ associates the descending ordering of the estimated probabilities on _x_ . Then, for any given features _x ∈X_ , and any label _y ∈Y_ , the conformity score function is s ( _x, y_ ; ˆ _p_ ) :=[�] _[σ] l_ =1 _x[−]_[1][(] _[y]_[)] _p_ ˆ( _x_ ) _σx_ ( _l_ ), that is, the sum of the estimated probabilities associated to classes at least as large as that of the true class _y_ . Finally, on a test point _Xn_ +1, it returns the set of classes � _σXn_ +1(1) _, . . . , σXn_ +1( _r[⋆]_ )�, where _r r[⋆]_ := argmax1 _≤r≤C_ �� _k_ =1 _[p]_[ˆ][(] _[X][n]_[+1][)] _[σ] Xn_ +1[(] _[k]_[)] _[<][ q]_[1] _[−][α]_[(] _[S]_[)] � + 1. An illustration of the scores and predictive set construction is provided in Figure 3.7, along with a detailed toy use case example in Example 3.2.6 which highlights that this time the predictive sets adapts to the complexity of the test point. 

_Chapter 3. Introduction to Conformal Prediction_ 

34 

**Example 3.2.6** (toy use case of classification SCP with adaptive score) **.** Let consider again the demand-side management toy use case where _Y_ = _{_ “N” _,_ “B” _,_ “D” _}_ , and we wish to build predictive sets at the level _α_ = 0 _._ 1. Assume we have access to a calibration data set with #Cal = 10 points. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0052-03.png)


**----- Start of picture text -----**<br>
1. Compute the scores on the calibration set using s ( x, y ; ˆ p ) := [�] [σ] l =1 x [−] [1][(] [y] [)] p ˆ( x ) σx ( l ).<br>Yi, i ∈ Cal “N” “N” “N” “B” “B” “B” “B” “D” “D” “D”<br>p ˆN( Xi ) 0.95 0.90 0.85 0.05 0.05 0.05 0.10 0.25 0.10 0.15<br>p ˆB( Xi ) 0.02 0.05 0.10 0.85 0.80 0.75 0.75 0.40 0.30 0.30<br>p ˆD( Xi ) 0.03 0.05 0.05 0.10 0.15 0.20 0.15 0.35 0.60 0.55<br>Si 0.95 0.90 0.85 0.85 0.80 0.75 0.75 0.75 0.60 0.55<br>Define S =  {Si, i ∈ Cal } ∪{ + ∞}.<br>2. Compute their empirical quantile: q 1 −α ( S ) = 0 . 95.<br>▶ Unconfident prediction on the test point:<br>3. Predict on a new point Xn +1, evaluate r [⋆] to reach q 1 −α ( S ) and obtain the<br>associated predictive set:<br>ˆ �<br>p ( Xn +1) = (0 . 05 ,  0 . 45 ,  0 . 5) , r [⋆] = 2 = ⇒ Cn,α  ( Xn +1) =  { “B”, “D” }<br>▶ Confident prediction on the test point:<br>3bis. Predict on a new point Xn +1, evaluate r [⋆] to reach q 1 −α ( S ) and obtain the<br>associated predictive set:<br>ˆ �<br>p ( Xn +1) = (0 . 03 ,  0 . 95 ,  0 . 02) , r [⋆] = 1 = ⇒ Cn,α  ( Xn +1) =  { “B” }<br>**----- End of picture text -----**<br>



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0052-04.png)


**----- Start of picture text -----**<br>
B D N B D N<br>Estimated probabilities Cumulative estimated probabilities<br>**----- End of picture text -----**<br>


Figure 3.7: Illustration of Romano et al. (2020b) predictive sets construction. Figure highly inspired by Angelopoulos and Bates (2023). 

_3.3. On the design choices of CP and (empirical) conditional guarantees_ 

35 

## **Wrapping up** 

We have described a simple procedure, coined Split Conformal Prediction—a special case of the more generic framework of CP described in Section 3.4—, which quantifies the uncertainty of **any predictive algorithm** _A_ by returning predictive sets that enjoy **finite sample distribution-free** coverage guarantees, as long as the data set is _exchangeable_ . In the reminder of this introductory chapter, our goal is to discussion _inherent bottlenecks_ of (split) CP and provide an overview of the current research’ state in addressing them. Namely, Section 3.3 develops on the conditional guarantees, both empirically and theoretically; in Section 3.4 we present CP approaches that alleviate the statistical cost of data splitting; and lastly, in Section 3.5 we discuss extensions of CP when the unique assumption—data exchangeability—is not met. The research community on conformal methods has been growing quickly in the recent years. Therefore, these research directions are not exhaustive, the current research effort including also many branches that develop CP in specific domains. 

## **3.3 On the design choices of CP and (empirical) conditional guarantees** 

Intrinsically, CP guarantees hold marginally over the test point (its features and its label) as well as marginally over the calibration set. They are obtained thanks to the fact that the _conformity scores_ built by SCP are exchangeable. This is a fundamental point: the key step, and in a sense the definition, of CP (beyond SCP) is the **construction of exchangeable conformity scores** . In this section, we precisely propose to analyse the impact of the conformity scores definition, and then to study what conditional guarantees can be obtained by CP (beyond SCP). 

## **3.3.1 What choices for the conformity scores?** 

The conformity scores are the cornerstone of CP, and their definition is crucial as they are the random variables that incorporate all the underlying information: the data distribution along with the fitted model behavior. A badly designed conformity function leads to predictive sets that are uninformative: taking an extreme case, an uninformed but legit possibility is to draw the scores i.i.d. from any exogenous distribution, e.g., _N_ (0 _,_ 1). While the resulting predictive sets do not convey any useful information, this procedure benefits from the theoretical framework of CP and is valid. A more down-to-earth analysis is to remember the insights of the previous Section 3.2: while for any score function, the guarantees are marginal over nearly all the problem’s randomness, yet some score functions are associated to predictive sets empirically closer to conditional validity (e.g., CQR is closer to conditional validity than SCP with absolute value mean-residuals, adaptive classification (Example 3.2.6) is closer to conditional validity than the simplest classification case (Examples 3.2.4 and 3.2.5)). 

_Chapter 3. Introduction to Conformal Prediction_ 

36 

Focusing temporarily on the regression setting, Table 3.1 illustrates the impact of the conformity score. All the methods presented in this table enjoy the exact same theoretical guarantees. However, their empirical performances and uses differ drastically. On the one hand, SCP with mean-regression and absolute value of the residuals is critically nonadaptive while CQR benefits from enhanced adaptivity. On the other hand, CQR can not be plugged in an operational pipeline predicting a mean value (i.e., using CQR, one can not say “The electricity prices tomorrow should be 90€/MWh _±_ 5€/MWh.” but only e.g., “The electricity prices tomorrow should be in between 87€/MWh and 97€/MWh”[2] ) unlike for SCP with mean-regression and absolute value of the residuals. In fact, they are in-betweens, and for example, in this figure, we add another conformity score function that we did not cover before and which is slightly less adaptive than CQR but is plugged on top of a mean-regression algorithm. Introduced in Lei et al. (2018), it consists in reweighting the absolute value of the residuals by an estimation of the dispersion of the exact same ˆ residuals _ρ_ . 

Designing insightful conformity score function might appear intricate. In practice, it can be easier to think about the desired shape of the predictive sets. Interestingly, Gupta et al. (2022) shows that SCP’s output can be obtained equivalently through the design of the predictive sets themselves instead of defining the conformity function _s_ . A model _A_[ˆ] (chosen by the user) is fitted on the proper training set as in SCP. Then, a sequence of nested predictive sets taking their values in _Y_ is built, _Rt ·_ ; _A_[ˆ][some] _[T][⊆]_[R][,][such][that] � � �� _t∈T_[for] for any _t ≤ t[′] ∈T_[2] , for any _x ∈X_ , _Rt x_ ; _A_[ˆ] _⊆ Rt′ x_ ; _A_[ˆ] , and at the limits _R_ inf _T ≡∅_ � � � � and _R_ sup _T ≡Y_ . For instance, with a mean regression, the parallel of the absolute values ˆ of the residuals conformity scores in terms of nested sets leads to _Rt_ ( _·_ ; ˆ _µ_ ) _≡_ [ _µ_ ( _·_ ) _± t_ ] and _T_ = R+. _Entry radius_ of _y_ in the sets given by _x_ are then computed on each of the ˆ calibration points as _r_ ( _x, y_ ) := inf _t ∈T_ : _y ∈ Rt x_ ; _A_[ˆ] . Then, under exchangeability � � �� 

||**Simplest SCP**<br>Vovk et al. (2005)|**Simplest SCP**<br>Vovk et al. (2005)|**Simplest SCP**<br>Vovk et al. (2005)||**Locally weighted SCP**<br>Lei et al. (2018)|**Locally weighted SCP**<br>Lei et al. (2018)|**Locally weighted SCP**<br>Lei et al. (2018)|**CQR**<br>Romano et al. (2019)|**CQR**<br>Romano et al. (2019)|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|s( ˆ_A_(_X_)_, Y_)<br>�_Cα_(_x_)<br>Visu.|_|_ˆ_µ_(_X_)_−Y |_<br>[ˆ_µ_(_x_)_± q_1_−α_(_S_)]<br>0<br>2<br>4<br>_X_<br>_−_4<br>_−_2<br>0<br>2<br>_Y_||||_|_ˆ_µ_(_X_)_−Y |_<br>ˆ_ρ_(_X_)<br>[ˆ_µ_(_x_)_± q_1_−α_(_S_)ˆ_ρ_(_x_)]|||max(�<br>QRlower(_X_)_−Y,_<br>_Y −_�<br>QRupper(_X_))<br>[�<br>QRlower(_x_)_−q_1_−α_(_S_);<br>�<br>QRupper(_x_) +_q_1_−α_(_S_)]<br>0<br>2<br>4<br>_X_<br>_−_4<br>_−_2<br>0<br>2<br>_Y_||
|||4<br>2<br>0<br>2|||_−_4<br>_−_2<br>0<br>2<br>_Y_|||_−_4<br>_−_2<br>0<br>2<br>_Y_||
|||0<br>2<br>4<br>_X_||||0<br>2<br>4<br>_X_||||
|||||||||||
||black-box around a “us-<br>able” prediction||||black-box around a “us-<br>able” prediction|||adaptive||
|<br>not adaptive|||||limited adaptiveness<br>no black-box around a “us-<br>able” prediction|||||



Table 3.1: A comparison of some classical regression conformity scores. 

> 2Note that to overcome this, an idea is to apply CQR directly on residuals of a mean-regression model. 

_3.3. On the design choices of CP and (empirical) conditional guarantees_ 

37 

of the data points, (ˆ _r_ ( _Xi, Yi_ )) _[n] i_ =1[are][exchangeable][and][play][the][role][of][the][conformity] scores. Denote the set of entry radii _R_ = �(ˆ _r_ ( _Xi, Yi_ )) _i∈_ Cal� _∪{_ + _∞}_ . We can finally define ˆ the predictive set as _C_[�] _n,α_ ( _x_ ) := _Rq_ 1 _−α_ ( _R_ ) � _x_ ; _A_[ˆ] � = _{y ∈Y_ such that _r_ ( _x, y_ ) _≤ q_ 1 _−α_ ( _R_ ) _}_ . This formalism is appealing as it allows to first design the geometric shape of the predictive set, and only then deduce the algorithm to be deployed in order to output it. To illustrate this, we provide below some canonical examples of equivalences between the conformity score and the nested sets points of view. 

**Example 3.3.1** (Nested sets for the absolute value of the mean-regression residuals) **.** 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0055-04.png)


**Example 3.3.2** (Nested sets for CQR) **.** 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0055-06.png)


**Example 3.3.3** (Nested sets for the simplest classification) **.** 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0055-08.png)


**Example 3.3.4** (Nested sets for adaptive scores in classification) **.** ˆ Given a predictor of estimated probabilities _p_ ( _·_ ), for any _x ∈X_ , define _σx_ : ˆ ˆ _{_ 1 _, . . . ,_ # _Y} �→Y_ such that _p_ ( _x_ ) _σx_ (1) _≥ . . . ≥ p_ ( _x_ ) _σx_ (# _Y_ ). In other words, _σx_ associates the descending ordering. Let _x ∈X_ . 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0055-10.png)


## **3.3.2 On distribution-free** _X_ **-conditional validity** 

Some scores allow to get “closer” to _X_ -conditional coverage than others. However, unfortunately, as sketched at the end of Section 3.2.1, it is impossible to achieve informative distribution-free _X_ -conditional validity. To state this negative result (that traces back to Vovk, 2012; Lei and Wasserman, 2014), let us first formally defined distribution _X_ - conditional validity. 

_Chapter 3. Introduction to Conformal Prediction_ 

38 

**Definition 3.3.1** (distribution-free _X_ -conditional validity) **.** 

An estimator _C_[�] _n,α_ achieves distribution-free _X_ -conditional validity if for any distribution _D_ , for any associated exchangeable joint distribution _D_[E][(] _[n]_[+1)] _∈D_[exch(] _[n]_[+1)] , we have that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0056-04.png)


**Theorem 3.3.1** (impossibility of informative _X_ -conditional validity) **.** 

Assume _C_[�] _n,α_ is distribution-free _X_ -conditionally valid. Then, for any _D_ , for _DX_ – almost all _DX_ –non-atoms _x ∈X_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0056-07.png)


We provide below a proof which is highly inspired from the ones in Vovk (2012); Lei and Wasserman (2014), but the former is not constructive and the latter made the additional strong assumption that _C_[�] _n,α_ is also training-conditional. The remarks on Theorem 3.3.1 are deferred after this proof. 

_Proof._ Assume _C_[�] _n,α_ be _X_ -conditionally valid, as defined in Definition 3.3.1. 

Let _P_ a distribution on _X × Y_ , and let _x_ 0 _∈_ non-atom ( _PX_ ). 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0056-11.png)


Before diving in the details of the proof, let us define the total variation distance between two distributions _P_ and _Q_ on _Z_ , denoted _TV_ ( _P, Q_ ): 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0056-13.png)


▶ _Classification case._ 

Let _y ∈Y_ . 

Define _Q_ another distribution on _X × Y_ such that for any _A ⊆X_ and for any _B ⊆Y_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0056-17.png)


with _Sy_ defined on _Y_ , which is a dirac on _y_ . 

On the one hand, exactly as in the regression case, by construction, _TV_ ( _P, Q_ ) _≤ PX_ ( _E_ ) _≤ εn_ . Hence, using Lemma 3.3.1, _TV_ � _P[⊗]_[(] _[n]_[)] _, Q[⊗]_[(] _[n]_[)][�] _≤ ε_ . Therefore, for any _A ⊆X_ and for any _B ⊆Y_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0056-20.png)


_3.3. On the design choices of CP and (empirical) conditional guarantees_ 

39 

On the other hand, let _x ∈ E_ . As _C_[�] _n,α_ is distribution-free _X_ -conditionally valid, it satisfies: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0057-03.png)


Combining with Equation (3.2), we finally get: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0057-05.png)


which concludes the proof for the classification case by letting _ε →_ 0. 

▶ _Regression case._ 

Let _D >_ 0. 

Define _Q_ another distribution on _X × Y_ such that for any _A ⊆X_ and for any _B ⊆Y_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0057-10.png)


with _R_ defined on _Y_ , uniform on [ _−D_ ; _D_ ]. 

On the one hand, by construction, _TV_ ( _P, Q_ ) _≤ PX_ ( _E_ ) _≤ εn_ . Hence, using Lemma 3.3.1, _TV_ � _P[⊗]_[(] _[n]_[)] _, Q[⊗]_[(] _[n]_[)][�] _≤ ε_ . Therefore, for any _A ⊆X_ and for any _B ⊆Y_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0057-13.png)


On the other hand, let _x ∈ E_ . As _C_[�] _n,α_ is distribution-free _X_ -conditionally valid, it satisfies: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0057-15.png)


Note that Λ _C_ � _n,α_ ( _x_ ) _∩_ [ _−D_ ; _D_ ] _×_ 21 _D[≤]_[1][.][Therefore,][using][Lemma][3.3.2][,][for][any] _[t >]_[ 0][:] � � 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0057-17.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0057-18.png)


_Chapter 3. Introduction to Conformal Prediction_ 

40 

Combining with Equation (3.2), we finally get: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0058-03.png)


Letting _ε →_ 0 and _D →_ + _∞_ , the result is proven for the regression case. 

This proof relies on the following Lemmas 3.3.1 and 3.3.2, whose proofs are available in Section 8.A. 

**Lemma 3.3.1** (total variation distance between i.i.d. distributions) **.** 

For _P_ and _Q_ two probability distributions, and _n ∈_ N _[∗]_ , it holds: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0058-08.png)


**Lemma 3.3.2** (concentration for bounded random variable with high expectation) **.** Let _Z_ be a random variable such that 0 _≤ Z ≤_ 1 and E [ _Z_ ] _≥ β_ with _β ∈_ [0 _,_ 1]. Then, for any _t >_ 0, it holds P ( _Z ≥_ 1 _− t_ ) _≥_ 1 _−_[1] _[−] t[β]_[.] 

**Remark 3.3.1** (distribution-free _X_ -conditional hardness result apply beyond CP) **.** Theorem 3.3.1 proves that if an estimator is _X_ -conditionally valid on all distributions _D_[exch(] _[n]_[+1)] , then its predictive sets will necessarily be critically large and thus uninformative. To put it differently, this result holds for any estimator that is _X_ -conditionally valid on all distributions _D_[exch(] _[n]_[+1)] , regardless on its underlying construction, which implies that the impossibility result holds beyond CP approaches. 

**Remark 3.3.2** ( _X_ -conditional estimators are overly large even on easy cases) **.** 

Theorem 3.3.1 proves that if an estimator is distribution-free _X_ -conditionally valid, then under any given _D_ , its predictive sets will necessarily be critically large and thus uninformative. Crucially, it implies that on _any_ distribution _D_ including the “nicest” ones (e.g., say _Y_ is constant), the predictive set is useless: this is because in order to be _X_ -conditionally valid on all distributions _D_[exch(] _[n]_[+1)] it has to be overly conservative in any situation to ensure _X_ -conditional coverage on more complex distributions. 

**Remark 3.3.3** (the lower bounds in Theorem 3.3.1 are tight) **.** 

Notice that, again, the naive predictor presented in Example 3.1.9—outputting _Y_ with probability 1 _− α_ and the empty set otherwise—is perfectly distribution-free conditionally valid (on _X_ , on the calibration set, and on _Y_ ). However, the probability that its regression sets have infinite measure, or that its classification sets include any given label _y_ , is exactly 1 _− α_ as both events only occur when it outputs _Y_ . Therefore, the lower bound in Theorem 3.3.1 is tight. 

_3.3. On the design choices of CP and (empirical) conditional guarantees_ 

41 

**Remark 3.3.4** (interpretation of the classification case) **.** 

For classification, the result of Theorem 3.3.1 implies that _every label_ is likely to be included in any distribution-free _X_ -conditionally valid predictive set. Henceforth, the predictive set is likely to be large: especially, for any _D_ , for _DX_ –almost all _DX_ –non-atoms _x ∈X_ , E _D⊗_ ( _n_ ) # _C_[�] _n,α_ ( _x_ ) _≥_ (1 _− α_ )# _Y_ . � � 

A natural question now is: can we relax the notion of _X_ -conditional validity to make it a less lofty goal? Some elements of answer are provided in Barber et al. (2021a) in the regression setting. Their main result studies the following relaxation. 

**Definition 3.3.2** (distribution-free (1 _− α, δ_ )– _X_ -conditional validity) **.** 

Let _δ >_ 0 be a tolerance level. An estimator _C_[�] _n,α_ achieves distribution-free (1 _− α, δ_ )– _X_ -conditional validity if for any distribution _D_ , for any X _⊆X_ such that P _DX_ ( _X ∈_ X) _≥ δ_ , and for any associated exchangeable joint distribution _D_[E][(] _[n]_[+1)] _∈D_[exch(] _[n]_[+1)] , we have: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0059-07.png)


The idea behind Definition 3.3.2 is that for any region of the features space that is large enough (in probability), then validity should be achieved on this region. 

**Theorem 3.3.2** (hardness of informative (1 _− α, δ_ )– _X_ -conditional validity) **.** 

Let _δ >_ 0 be a tolerance level. Assume _C_[�] _n,α_ is distribution-free (1 _− α, δ_ )– _X_ -conditionally valid. Then, for any _D_ such that _DX_ does not have atoms, it holds: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0059-11.png)


In other words and simplifying, Theorem 3.3.2 shows that an estimator achieving (1 _− α, δ_ )– _X_ -conditional validity can not be more efficient than an estimator achieving distribution-free marginal validity at the level 1 _− αδ_ . However, in practice we are interested by the case where _δ_ is small, leading to marginally valid estimators at the level 1 _− αδ_ that are particularly inefficient, therefore the same would be true for (1 _− α, δ_ )– _X_ -conditionally valid ones. This calls for further relaxation of _X_ -conditional validity. 

## **3.3.3** _Y_ **-conditional validity** 

Another form of conditional validity that might be desired in practice is to be valid conditional on _Y_ . Indeed, one might want to cover at the same level whether the electricity 

_Chapter 3. Introduction to Conformal Prediction_ 

42 

price is low or high for example. In classification, this is achievable for SCP (Vovk, 2012) by comparing the score on a given _y ∈Y_ only with calibration scores obtained by data points with the same label. This is described more formally in Algorithm 4. While this approach achieve _Y_ -conditional validity, observe that it comes at the cost of smaller calibration sets. We have not touched upon this point until now, and will do so in the following Section 3.3.4, but we can already state that the smaller the calibration set, the higher the variance of our empirical quantile of the scores. For instance, this is all the most true in Algorithm 4 if there is important class imbalance in our data set and a class is unfrequent. To overcome this limitation, a very recent work (Ding et al., 2023) proposed to instead obtain cluster-conditional coverage, after having clustered the calibration data (therefore, an additional split is required to learn a mapping between the labels and the clusters). 

## **3.3.4 Impact of the calibration set on the coverage** 

Let us now focus on the effect of the calibration set randomness in the coverage of the SCP predictive sets. As mentioned, SCP guarantee is conditional on the proper training set but marginalized over the calibration random variables. Vovk (2012) show that we can obtain a coverage guarantee after conditioning on the calibration set. It relies on deriving instead a probability approximately correct bound. We state one of the results in Theorem 3.3.3. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0060-05.png)


SCP outputs _C_[�] _n,α_ such that for any distribution _D_ and any 0 _< δ ≤_ 0 _._ 5: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0060-07.png)


To state it differently, the bound of Theorem 3.3.3 controls the deviation of miscoverage with respect to the nominal level _α_ of a predictive set built on a given calibration set. In particular, this deviation vanished with high probability when #Cal increases. We refer the interested reader to Vovk (2012) for a complete proof and a tighter 

**Algorithm 4** SCP in classification with _Y_ -conditional coverage 

**Input:** Learning algorithm _A_ , conformity score function _s_ , miscoverage rate _α_ , training set ( _Xi, Yi_ ) _[n] i_ =1 **Output:** Prediction set _C_[�] _n,α_ 

1: Randomly split the training data ( _Xi, Yi_ ) _[n] i_ =1[into][a][proper][training][set][(size][#][Tr][)][and] a calibration set (size #Cal) 

2: Get _A_[ˆ] ( _by training A on the proper training set_ ( _Xi, Yi_ ) _i∈_ Tr) 

- 3: **for** any candidate _y ∈Y_ **do** 

4: On the calibration set, obtain a set of #Cal _y_ + 1 conformity scores : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0060-15.png)


5: **end for** 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0060-17.png)


_3.4. Avoiding data splitting: full CP and out-of-bags approaches_ 

43 

bound. The proof relies on the observation that P _D Yn_ +1 _∈/ C_[�] _n,α_ ( _Xn_ +1) _|_ ( _Xi, Yi_ ) _[n] i_ =1 _∼_ � � Beta ( _⌈_ (1 _− α_ ) (#Cal + 1) _⌉,_ #Cal + 1 _−⌈_ (1 _− α_ ) (#Cal + 1) _⌉_ ) whose variance is approximately _[α]_[(][1] _[−][α]_[)][Overall,][these][results][give][precise][tools][to][analyse][the][influence][of][(the][size] #Cal+2[.] of) the calibration set on the predictive coverage. If fitting a regression or classification model requires more data point than estimating a univariate quantity such as the 1 _− α_ quantile of the scores’ distribution, the variance induced by a small calibration should still be kept at a small enough level in order to output reliable predictive sets. Indeed, we do not want our predictions to greatly vary if we re-run the procedure on other i.i.d. data. Hence, there is a trade-off between proper training set (higher model accuracy induces efficient predictive sets) and calibration set (variability of the predictive sets), which depends on the target miscoverage level _α_ . This is critically data and machine learning model dependent, but as an educated rule of thumb, in non-pathological scenarii, keeping between 30% and 10% of the training data for calibration has demonstrated to be a good compromise (Sesia and Candès, 2020, which studies extensively CQR and other related methods). 

## **3.4 Avoiding data splitting: full CP and out-of-bags approaches** 

Therefore, splitting the training set might not be possible or desirable in practice. Again, to rephrase, when _n_ is significantly small, one can not afford to throw away some observations and reduce the actual training size supplied to the learning algorithm _A_ . Generally, keeping some fresh training data apart for calibration lowers the statistical efficiency (i.e. _A_[�] gets poorer accuracy, leading to larger predictive sets) and increases the statistical variability. However, having access to calibration pointd that are exchangeable with the test point was key to SCP theory as it allowed the method to treat the test point as if part of calibration data. The goal of this section is to see if, and how, we can avoid data splitting or at least alleviate the impact of splitting. 

## **3.4.1 Full Conformal Prediction** 

**Failure of naive approach.** A naive idea to avoid data splitting would be to keep all of training point to fit _A_ . Then, we could evaluate conformity scores on the exact same point and obtain a 1 _− α_ empirical quantile of these score. Finally, a predictive set could be the set of all the _y_ achieving a smaller score on the test features than this 1 _− α_ empirical quantile. More formally: 

1. Get _A_[ˆ] by training the algorithm _A_ on ( _Xi, Yi_ ) _[n] i_ 

   - _i_ =1[.] 

- _n_ 

- 2. Get the empirical quantile _q_ 1 _−α_ ( _S_ ) of the set of scores _S_ = s _Xi, Yi_ ; _A_[ˆ] � � �� _i_ =1 _[∪{∞}][.]_ 

3. Output the set _y_ such that s _Xn_ +1 _, y_ ; _A_[ˆ] _≤ q_ 1 _−α_ ( _S_ ) . � � � � 

> However, _A_[ˆ] has been obtained using the training set ( _Xi, Yi_ ) _[n] i_ =1[but][did][not][use] _[X][n]_[+1][.] Therefore we are comparing a _test_ score to _train_ scores. Thus s _Xn_ +1 _, y_ ; _A_[ˆ] typically � � 

_Chapter 3. Introduction to Conformal Prediction_ 

44 

_n_ stochastically dominates any element of s _Xi, Yi_ ; _A_[ˆ] . This in turn implies that �� � �� _i_ =1� such a set will typically under cover in practice, and can not enjoy any form of theoretical validity: they lost the backbone of SCP, as the scores are not exchangeable anymore. 

In order to recover validity, we have to compare a score on _y_ that is comparable to train scores. Full CP (Vovk et al., 2005) achieves this by retraining _A_ for any possible _y_ as the value of _Yn_ +1. By doing so, the score on each test _y_ is a train score, and when checking whether it is smaller to the empirical quantile of other training scores, we should be able to invoke the quantile Lemma 3.2.1 as the training data and the test data have (supposedly) been treated equally. A rigorous description of Full CP is given in Algorithm 5. 

To state the theoretical validity of Full CP, we have to consider an additional assumption on the learning algorithm _A_ . Indeed, when describing with words Full CP, we justified the procedure by explaining that the scores are now exchangeable as all the data points have been treated equally. However, this is not always true: if the algorithm _A_ ignores the last element of its input data set, then having re-trained by including the candidate _y_ has no influence and the score on this candidate still stochastically dominate the true training score. To ensure that exchangeability is preserved, we consider only algorithms _A_ that are invariant to permutation of their input. This is formally described in Definition 3.4.1, for both deterministic and stochastic _A_ . 

**Definition 3.4.1** (symmetrical algorithm) **.** 

▶ A _deterministic_ learning algorithm _A_ is symmetric if for any data set ( _Xi, Yi_ ) _[n] i_ =1[,] for any permutation _σ_ on �1 _, n_ �: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0062-07.png)


▶ A _stochastic_ learning algorithm _A_ is symmetric if for any data set ( _Xi, Yi_ ) _[n] i_ =1[,] for any permutation _σ_ on �1 _, n_ �, there exists a coupling that maps _ξ ∼U_ ([0 _,_ 1]) to _ξσ[′][∼U]_[([0] _[,]_[ 1])][,][which][depends][only][on] _[σ]_[,][such][that] _[a]_[,][for][a.s.][(] _[X][i][, Y][i]_[)] _[n] i_ =1[:] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0062-09.png)


> _a_ This is the definition provided in Kim and Barber (2023). 

## **Algorithm 5** Full CP 

**Input:** Learning algorithm _A_ , conformity score function _s_ , miscoverage rate _α_ , training set ( _Xi, Yi_ ) _[n] i_ =1[,][test][point] _[X][n]_[+1] **Output:** Prediction set _C_[�] _n,α_ 

1: **for** any candidate _y ∈Y_ **do** 2: Get _A_[ˆ] _y_ by training _A_ on _{_ ( _Xi, Yi_ ) _[n] i_ =1 _[} ∪{]_[(] _[X][n]_[+1] _[,][ y]_[)] _[}]_ 

- 3: Obtain a set of training scores 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0062-15.png)


_3.4. Avoiding data splitting: full CP and out-of-bags approaches_ 

45 

**Theorem 3.4.1** (marginal validity of Full CP) **.** 

FCP (Algorithm 5) with a symmetric algorithm _A_ outputs _C_[�] _n,α_ such that for any distribution _D_ , for any associated exchangeable joint distribution _D_[E][(] _[n]_[+1)] _∈ D_[exch(] _[n]_[+1)] : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0063-04.png)


Additionally, if the scores _{Si}[n] i_ =1[+1][are][almost][surely][(a.s.)][distinct:] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0063-06.png)


_Proof._ Assume ( _Xi, Yi_ ) _[n] i_ =1[+1][are][exchangeable,][and][that] _[A]_[is][symmetric][(possibly][stochastic).] Let _σ_ be a permutation on �1 _, n_ + 1�. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0063-08.png)


Therefore, the scores are exchangeable and it only remains to apply the quantile Lemma 3.2.1. 

**Remark 3.4.1** (SCP is a particular case of Full CP) **.** 

SCP can be seen as a special case of Full CP where Full CP is only applied on the calibration data set, and the learning algorithm _A_ is independent of its input and always output some function _A_ that has in fact been trained only on the proper training set (this algorithm is indeed symmetric as it is independent of any component of its input). 

Theorem 3.4.1 shows that this cautious treatment of the test point allows to retrieve validity without having to split the training data set. However, this comes with the need to fit numerous models. When _Y_ is not discrete, this is even impossible to perform exactly and it is usually approximated by binning _Y_ (Chen et al., 2016, 2018), but even while doing so, or when _Y_ is discrete, it can be computationally costly if there are many bins or classes, or if the learning algorithm _A_ has heavy computational load. 

Exact computation is feasible in ridge or lasso regression (Nouretdinov et al., 2001; Burnaev and Vovk, 2014; Lei, 2019), nearest neighbors or kernel smoothing algorithms (Cherubin et al., 2021), and approximations can be achieved under smooth and “regular” (such as convex) regression estimators (Ndiaye and Takeuchi, 2019) or algorithms satisfying (prediction) stability assumptions (Ndiaye, 2022), or when the predictive set of Full CP is in fact an interval (Ndiaye and Takeuchi, 2022). 

_Chapter 3. Introduction to Conformal Prediction_ 

46 

**Example 3.4.1** (standard FCP sets with an interpolating algorithm) **.** 

Assume _A_ interpolates. Then, for any candidate _y ∈Y_ , _A_[ˆ] _y_ is such that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0064-04.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0064-05.png)


Henceforth, Full CP _(with standard score functions)_ with an interpolating algorithm outputs _Y_ for any new test point. 

Note that in this case all the scores are almost surely equals. As such this example does not contradict the upper bound of Theorem 3.4.1. 

## **3.4.2 Jackknife+ and leave-one-out CP** 

A natural question that arises now is whether there exist theoretically valid intermediate methods between SCP and Full CP. An idea is to leverage leave-one-out strategies, in order to use all of the training data (unlike SCP) but only have _n_ model fits (which often is smaller than for FCP). The first natural idea based on leave-one-out is to fit _n_ model, leaving out a different training point to fit each model, and obtain a conformity score on the left out point. Then, the 1 _− α_ empirical quantile of these scores is computed and used to correct the prediction made on the test point by a model fitted this time on the _n_ training points. This is formalized below. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0064-10.png)


1. For any _j ∈_ �1 _, n_ �: get _A_[ˆ] _−j_ by training _A_ on ( _Xi, Yi_ ) _i[n]_ =1. _i_ = _j_ 

2. Get the empirical quantile _q_ 1 _−α_ ( _S_ ) of the set of scores 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0064-12.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0064-13.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0064-14.png)


However, without stability assumptions on _A_ , there is absolutely no guarantee on the prediction of _A_[ˆ] with scores based on ( _A_[ˆ] _−i_ ) _i_ (Barber et al., 2021b). Indeed, this naive algorithm is comparing a score on the test point obtained through an algorithm that has seen _n_ points, while the reference “calibration” scores rely on learning on _n −_ 1 data points. To circumvent this issue, Barber et al. (2021b) introduce the Jackknife+ algorithm that treats the training points and the test point similarly: the idea is, that for each _i ∈_ �1 _, n_ �, the algorithm learns a model leaving the _i_ -th point out to evaluate conformity on it, while also assessing the conformity of potential test points with this fitted model. Jackknife+ is written only for mean-regression and scores that are the absolute value of the residuals, but 

_3.4. Avoiding data splitting: full CP and out-of-bags approaches_ 

47 

Gupta et al. (2022) have shown that a tighter leave-one-out set can be built in a general setting. The core idea is exactly the same, hence we present here only the generalized and tighter version formalized in Gupta et al. (2022) but in terms of conformity scores, in Algorithm 6 (we recall that Gupta et al., 2022, work in their novel nested sets framework). 

Again, the predictive set is built by looping over all possible _y ∈Y_ which can be tricky in practice. We refer the reader to Gupta et al. (2022) for an efficient implementation (linear time in _n_ ) of this algorithm, when each of the 1 s _Xi, Yi_ ; _A_[ˆ] _−i <_ s _Xn_ +1 _, y_ ; _A_[ˆ] _−i_ � � � � �� takes value 1 only on an interval. In this case, it is possible to derive a Jackknife+ version of the algorithm, whose predictive sets include the ones of leave-one-out CP. This is a generalization of Jackknife+, which was written only for mean-regression and absolute value of the residuals scores, suggested again in Gupta et al. (2022). We rephrase it in terms of conformity scores in Algorithm 7 (recall from Definition 3.1.7 that _qβ,_ inf( _U_ 1 _, . . . , Un_ ) := _⌊β × n⌋_ smallest value of ( _U_ 1 _, . . . , Un_ ).). Theorem 3.4.2 specifies the theoretical guarantees that this algorithm obtain. 

**Theorem 3.4.2** (marginal validity of leave-one-out-CP and JK+) **.** 

Algorithms 6 and 7 with a symmetric algorithm _A_ output _C_[�] _n,α_ such that for any distribution _D_ , for any associated exchangeable joint distribution _D_[E][(] _[n]_[+1)] _∈D_[exch(] _[n]_[+1)] : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0065-06.png)


_Proof._ We prove the result for Algorithm 6, as its predictive sets are included in the ones of Algorithm 7 (when those are well-defined). 

**Algorithm 6** Leave-one-out CP 

**Input:** Learning algorithm _A_ , conformity score function _s_ , miscoverage rate _α_ , training set ( _Xi, Yi_ ) _[n] i_ =1[,][test][point] _[X][n]_[+1] **Output:** Prediction set _C_[�] _n,α_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0065-10.png)


1: **for** _j ∈_ �1 _, n_ � **do** 2: Get _A_[ˆ] _−j_ by training _A_ on ( _Xi, Yi_ ) _i[n]_ =1 _i_ = _j_ 

- 3: **end for** 

- 4: For a new point _Xn_ +1, return 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0065-14.png)


_Chapter 3. Introduction to Conformal Prediction_ 

48 

**Algorithm 7** Generalized Jackknife+ 

**Input:** Learning algorithm _A_ , conformity score function _s_ , miscoverage rate _α_ , training set ( _Xi, Yi_ ) _[n] i_ =1[,][test][point] _[X][n]_[+1] **Output:** Prediction set _C_[�] _n,α_ ( _Xn_ +1) 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0066-04.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0066-05.png)


- 4: **end for** 

- 5: Return 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0066-08.png)


_Step 1._ Remark that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0066-10.png)


with _S_[(] _[i]_[)] _[,j]_ := _s_ � _X_[(] _[i]_[)] _, Y_[(] _[i]_[)] ; _A_[ˆ] _−_ ( _i,j_ )� is the score on data point _i_ of the predictor that has been fitted without seeing nor data point _i_ nor data point _j_ , for ( _i, j_ ) _∈_ �1 _, n_ + 1�[2] and extending _A_[ˆ] _−i_ to _A_[ˆ] _−_ ( _i,j_ ) := _A_ ( _Xj, Yj_ ) _[n]_[+1] _k_ =1 , where the _n_ + 1 data point is added. � _k/∈{i,j}_ � Denote by C _A_ the function building the comparison matrix _C ∈{_ 0 _,_ 1 _}_[(] _[n]_[+1)] _[×]_[(] _[n]_[+1)] : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0066-12.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0066-13.png)


- (1 _− α_ )( _n_ + 1) _} ≤_ 2 _α_ ( _n_ + 1). This is shown for _any_ comparison matrix. 

_Step 3._ The last (and crucial) step of leave-one-out conformal predictors is to show that thanks to the algorithm symmetry and data exchangeability, for any permutation _σ_ on _d_ �1 _, n_ + 1� it holds: � _Cσ_ ( _i_ ) _,σ_ ( _j_ )� _i,j_ = ( _Ci,j_ ) _i,j_ . 

Consider the general case where _A_ is a randomized algorithm and let _σ_ a permutation on �1 _, n_ + 1�, and ( _i, j_ ) _∈_ �1 _, n_ + 1�[2] . 

_3.4. Avoiding data splitting: full CP and out-of-bags approaches_ 

49 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0067-02.png)


This holds for any ( _i, j_ ) _∈_ �1 _, n_ + 1�[2] , hence, denoting Π _σ_ the matrix permutation associated with _σ_ (i.e. �Π _[T] σ[C]_[Π] _[σ]_ � _i,j_[=] _[ C][σ]_[(] _[i]_[)] _[,σ]_[(] _[j]_[)][for][any][(] _[i, j]_[)] _[ ∈]_[�][1] _[, n]_[ + 1][�][2][):] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0067-04.png)


This concludes the proof as therefore each element of �1 _, n_ + 1� is equally likely to _n_ +1 belong to _{i ∈_ �1 _, n_ + 1� : � _Ci,j ≥_ (1 _− α_ )( _n_ + 1) _}_ . _j_ =1 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0067-06.png)


The theoretical guarantee of leave-one-out-CP and JK+ presents a loss of coverage: the lower bound on the coverage is now in 1 _−_ 2 _α_ . Empirically, it achieves approximately 1 _− α_ coverage, a bound also obtained in theory under algorithmic stability assumptions. However, this factor 2 is not an artefact of the proof, and Barber et al. (2021b) derive an example in which the lower bound is attained (asymptotically with _n_ ). This example relies on a highly non-stable learning algorithm due to its intrinsic design as well as due to the data distribution on which it is applied. In other words, to suffer from this loss of coverage, the combination of data distribution and algorithm should provoke important prediction unstability. In particular, it ˆ _n_ should be the case that some of the _A−i_[say][for] _[i][ ∈]_[bad][,][would][be][associated] � � _i_ =1[,] to higher scores than the rest of the models (i.e. for _i ∈/_ bad), but that between all the _i ∈_ bad there is no clear ranking between the _i_ . 

## **3.4.3 CV+** 

For cases where _n_ is already too large, an analogous of the corrected leave-one-out predictive sets can be defined for _k_ -fold cross-validated scheme. The idea traces back to Vovk (2015), but we present here the version generalized by Gupta et al. (2022) from the suggested CV+ algorithm of Barber et al. (2021b). As in the previous subsection, we rephrase it in terms of conformity scores in Algorithm 8. We provide its theoretical guarantees in Theorem 3.4.3. 

_Chapter 3. Introduction to Conformal Prediction_ 

50 

## **Algorithm 8** _K_ -fold CP 

**Input:** Learning algorithm _A_ , conformity score function _s_ , miscoverage rate _α_ , number of fold _K ∈_ N _[∗]_ , training set ( _Xi, Yi_ ) _[n] i_ =1[,][test][point] _[X][n]_[+1] **Output:** Prediction set _C_[�] _n,α_ 

1: Randomly split ( _Xi, Yi_ ) _[n] i_ =1[into] _[K]_[folds] _[F]_[1] _[, . . . , F][K]_[(we][denote] _[k]_[(] _[i]_[)][the][subset][that] includes _i_ ) 2: **for** _k ∈_ �1 _, K_ � **do** 3: Get _A_[ˆ] _−k_ by training _A_ on ( _Xi, Yi_ ) _k_ ( _i_ )= _k_ 

- 4: **end for** 

5: For a new point _Xn_ +1, return 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0068-07.png)


## **Theorem 3.4.3** (marginal validity of _K_ -fold CP CV+) **.** 

Algorithm 8 with _K ∈_ N _[∗]_ folds and with a symmetric algorithm _A_ outputs _C_[�] _n,α_ such that for any distribution _D_ , for any associated exchangeable joint distribution _D_[E][(] _[n]_[+1)] _∈D_[exch(] _[n]_[+1)] : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0068-10.png)


In summary (Figure 3.8), there is a vast range of methods going from no splitting to a single split, passing through _K_ -fold/CV+ approaches, enjoying finite sample distribution free marginal validity with any (symmetric) algorithm. While distribution-free _X_ -conditional validity can not be attained by any of these methods, distribution-free _Y_ -conditional 

## Statistical efficiency 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0068-13.png)


**----- Start of picture text -----**<br>
Computational efficiency<br>SCP CV+ Jackknife+ FCP<br>**----- End of picture text -----**<br>


Nested Conformal Prediction 

Figure 3.8: Range of CP frameworks in the spectrum of splitting strategies. 

_3.5. Beyond exchangeability_ 

51 

coverage is achievable at least in theory, and, finally, training-conditional coverage is obtained through PAC bounds for SCP (for which training-conditional coverage refers to calibration-conditional), but also _K_ -fold CP/CV+ whose bound emphasizes that the controlling quantity is _n/K_ which should be large, however Full CP and leave-one-out CP/Jackknife+ do not benefit from any training-conditional coverage unless stability assumptions are made on the learning algorithm _A_ (Vovk, 2012; Bian and Barber, 2023; Liang and Barber, 2023). 

## **3.5 Beyond exchangeability** 

The last issue that we consider in this introductory chapter is how to extend CP to nonexchangeable settings? This is particularly challenging as it the one and only assumption required by conformal. Yet, it is an important direction to explore as exchangeability does not hold in many practical applications. Indeed, it can be broken by: 

- Shifts between the training data and the test data, and in particular: 

   - i) Covariate shift, i.e. _DX_[(train)] = _DX_[(test)] while _DY_[(train)] _|X_ = _DY_[(test)] _|X_[;] 

   - ii) Label shift, i.e. _DY_[(train)] = _DY_[(test)] while _DX_[(train)] _|Y_ = _DX_[(test)] _|Y_[;] 

   - iii) Arbitrary distribution shift on both the label and the covariates; 

- Possibly many shifts, not only one, not necessarily a finite number; 

- Temporal dependence, distributional drifts and non-stationarity. 

This line of research has been especially active in the recent years. In this section, we focus on the main common ideas giving only some reference points that should allow an interested reader to navigate the overall literature more easily afterwards. 

Under additional assumptions on the data distribution, such as strongly mixing noise, or on the quality of the fitted model that should be close to the generative model, theoretical results can be obtained in the data dependent context (see, e.g., Chernozhukov et al., 2018). Otherwise, there are two main settings: one in which we can rely on weighting strategy with a priori knowledge or estimation, and one in which we use feedback on the fly to understand (with a delay) how to adapt the predictive set estimator. The underlying assumption in all these methods is that even though data is not exchangeable anymore, there is some information from the historical data that we can leverage cautiously to build enhanced (in comparison with subsampling the historical data set) yet robust and not corrupted predictive sets. 

## **3.5.1 Weighting strategies** 

The idea of weighting approaches is to assign more importance to the data points that we trust more or are closer in distribution to the test point. Until now, we have formalized CP as evaluating an empirical quantile of scores _{q_ 1 _−α_ ( _{_ ( _Si_ ) _[n] i_ =1 _[} ∪{]_[+] _[∞}]_[) :=] _[ ⌈]_[(1] _[ −][α]_[)(] _[n]_[ + 1)] _[⌉]_ smallest value of _{_ ( _Si_ ) _[n] i_ =1 _[} ∪{]_[+] _[∞}}]_[.][In order to introduce weighting strategies,][it is useful] 

_Chapter 3. Introduction to Conformal Prediction_ 

52 

to note that in fact this is equivalent to considering _QDS_ (1 _− α_ ), with _DS_ the empirical distribution of the scores, i.e. _DS_ := _n_ +11 � _ni_ =1 _[δ][S] i_[+] _n_ +11 _[δ]_[+] _[∞]_[.] 

Tibshirani et al. (2019) introduced first the concept of weighted exchangeability (we refer the interested reader to the original paper for details) justifying weighted CP. They consider a setting in which the training data is drawn i.i.d. from some distribution _D_ , _⊗_ ( _n_ ) ( _Xi, Yi_ ) _[n] i_ =1 _[∼]_ � _DX × DY |X_ � , and we aim at predicting _Yn_ +1 observing _Xn_ +1, with ( _Xn_ +1 _, Yn_ +1) _∼ D_[�] _X × DY |X_ for some distribution _D_[�] _X_ = _DX_ . The key idea is that if we _DX_ ( _x_ ) know the ratio[d][ �][then][the][normalized/probability][weights][defined][by:] d _DX_ ( _x_ )[:=] _[ w]_[(] _[x]_[)][,] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0070-04.png)


ensure that the data points are weighted exchangeable. Therefore, outputting the set 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0070-06.png)


with Ω _S_ :=[�] _[n] i_ =1 _[ω][i]_[ (] _[X][n]_[+1][)] _[ δ][S] i_[+] _[ ω][n]_[+1][ (] _[X][n]_[+1][)] _[ δ]_[+] _[∞]_[,][is][a][marginally][valid][procedure.] 

Similarly, Podkopaev and Ramdas (2021) suggest to use this idea in situation where there is a label shift. Precisely, suppose again that the training data is drawn i.i.d. from _⊗_ ( _n_ ) some distribution _D_ , ( _Xi, Yi_ ) _[n] i_ =1 _[∼]_ � _DX|Y × DY_ � , and we aim at _classifying Yn_ +1 observing _Xn_ +1, with ( _Xn_ +1 _, Yn_ +1) _∼DX|Y × D_[�] _Y_ for some distribution _D_[�] _Y_ = _DY_ . The challenge here is that the actuel test label is unknown, unlike the test features _Xn_ +1. However, in classification we can loop over all possible classes. Therefore, based on the ratio _w_ ( _y_ ) :=[d] d[ �] _DDYY_ ( ( _yy_ ))[,][one][can][constructs][normalized/probability][weights][for][each][possible] class _y ∈Y_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0070-09.png)


for any _i ∈_ �1 _, n_ �. Then, the predictive set is 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0070-11.png)


with Ω _[y] S_[:=][ �] _i[n]_ =1 _[ω][i]_[ (] _[y]_[)] _[ δ][S] i_[+] _[ ω][n]_[+1][ (] _[y]_[)] _[ δ]_[+] _[∞]_[,][is][a][marginally][valid][procedure.] 

In practice, both these likelihood ratio (for covariate and for label shifts) have to be estimated and the guarantees do not go through directly, even though improved empirical performances are obtained. Jin and Candès (2023) provide some theory on the loss of coverage incurred by an estimation. 

Similar reweighting approaches have been further developped in the context of causal inference (Lei and Candès, 2021; Gui et al., 2023b), survival analysis (Candès et al., 2023) and active learning (Fannjiang et al., 2022). 

What if the rupture point was unknown, the estimation of the likelihood ratio is not possible, or the data distribution is slightly drifting? 

_3.5. Beyond exchangeability_ 

53 

If we still can assume an access to some i.i.d. data points, but do not want to suppose estimation of the likelihood ratio is possible (possibly because different shifts are in fact plausible), it is possible to leverage tools from the distributionally robust optimization literature. In particular, Cauchois et al. (2024) provide predictive sets that are valid for any distribution shift (both on _Y_ and _X_ ) as long as the shift remains bounded in _f_ -divergence (e.g., Kullback-Leibler divergence) with respect to the train distribution. 

If instead we cannot assume i.i.d. data points even in the training set, Barber et al. (2023) proposes to apply weights ( _wi_ ) _[n] i_ =1[pre-defined][by][the][user][to][each][data][point,][relying] on the same weighted quantile function than in Tibshirani et al. (2019); Podkopaev and Ramdas (2021). For example, in a time series context, one could apply exponential weights decaying in time (oldest points would receive lower weights) at a speed depending on the memory we consider representative. Importantly though, these weights can not be chosen in a way that depends on ( _Xi, Yi_ ) _[n] i_ =1[+1][.][The][main][theoretical][result][provided][in][the][paper] bounds the coverage loss due to the violation of exchangeability in the data set. Particularly, denoting again ( _ωi_ ) _i[n]_ =1[+1][the][normalized][weights][associated][to][the][chosen][weights][(] _[w][i]_[)] _[n] i_ =1[,] their main result proves the following control on the coverage loss, which we state informally. 

## **Informal theorem** 

Running weighted-CP with data independent normalized weights ( _ωi_ ) _[n] i_ =1[+1][achieves:] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0071-06.png)


where _S_[(] _[i]_[)] := ( _S_ 1 _, . . . , Si−_ 1 _, Sn_ +1 _, Si_ +1 _, . . . , Si_ ), i.e. the set of scores when the test score _Sn_ +1 and the _i_ -th score _Si_ have been swapped. 

This result highlights that if we can choose the weights adequatly, then coverage can be recovered. Maybe most importantly, it also sheds lights on the standard CP framework under violation of exchangeability. Indeed, taking uniform weights we recover the standard CP setting, and the result provides a characterization on the coverage deterioration depending on the strength of violation of exchangeability. 

## **3.5.2 Online setting** 

Generalizing the time series framework, let us consider now that we have access to an initial data stream, ( _Xt, Yt_ ) _[T] t_ =1[0][,][and][that][we][aim][at][building][predictive][sets] _[C]_[�] _[t,α]_[for][some] _T_ 1 subsequent observations. Our goal is that the predictive sets sequence enjoy theoretical guarantees without making any assumption on the data stream. This is highly challenging as it includes adversarial sequences. However, in this setting, we assume that at any prediction step _t ∈_ � _T_ 0 + 1 _, T_ 0 + _T_ 1�, _Yt−T_ 0 _, . . . , Yt−_ 1 have been revealed[3] . For example, this typically represents electricity prices forecasting where we have access to historical data on which to fit a model, and when predicting sequentially the next prices, any previous outcomes have already been revealed. 

3 This setting can be generalized to encapsulate forecast horizons _h >_ 1. 

_Chapter 3. Introduction to Conformal Prediction_ 

54 

In this setting, our ideal goal remains to control the probability of coverage with respect to the data distribution, that is building the smallest predictive set such that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0072-03.png)


However, when considering any data stream without restrictions, including adversarial ones, this goal appears to be lofty. Therefore, in general, we focus on achieving realized frequency type guarantees, averaged over all the sequence, which we write as: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0072-05.png)


or asymptotically: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0072-07.png)


The key difference here is that the guarantee we target is not in probability anymore, and it allows to use strategies whose theory rely on deterministic arguments. The pioneer work in this framework is that of Gibbs and Candès (2021). They propose Adaptive Conformal Inference (ACI) that adapts iteratively the quantile level of the scores’ quantile, depending on the coverages of the previous steps. Precisely, let _αT_ 0+1 = _α_ and fix some _γ >_ 0, which controls the speed of reaction to previous iterates. It can also be understood as playing the role of learning rate in an online gradient descent algorithm with respect to the pinball loss. The update scheme can be written as follows: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0072-09.png)


where the set of scores is now indexed by the time that passes, _St_ , to incorporate any pipeline such as re-training on the current data stream. 

In other words, if ACI does not cover at time _t_ , then _αt_ +1 _≤ αt_ , and the size of the predictive set increases; conversely when it covers. Importantly, nothing prevents _αt ≤_ 0 or _αt ≥_ 1. While the later is rare (as _α_ is typically small), the former can happen frequently for some _γ_ , producing by convention _C_[�] _t,αt ≡Y_ . 

ACI, and some later extensions of it, enjoy an asymptotic valid frequency _for any data sequence_ . 

## **Informal theorem** 

For any sequence of data, we have with probability one that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0072-15.png)


In particular, it follows that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0072-17.png)


_3.5. Beyond exchangeability_ 

55 

Crucially, this long-term frequency result does not provide guidelines on how to pick _γ_ , or even the contrary as it favors large _γ_ that are associated to more frequent uninformative sets (i.e. outputting _Y_ ) as well as more instalibility. In Chapter 5, based on Zaffran et al. (2022), we propose deeper theoretical analysis on the influence of _γ_ on the efficiency of the resulting predictive sets. This allows us to provide a practical algorithm, `AgACI` , based on online aggregation based on expert advice, which is parameter-free and does not require to choose _γ_ . 

More recent developments include: Gibbs and Candès (2023) improving on ACI by online aggregation on a grid of different _γ_ , similarly to what we propose in Chapter 5 through `AgACI` , at the crucial difference that the aggregation is on the value of _αt_ and not on the lower and upper bounds independently, which permits to derive theoretical guarantees on the regret of the proposed method; Bastani et al. (2022) which achieves stronger coverage guarantees (conditional on the effective level, and conditional on specified subsets of the explanatory variables); Bhatnagar et al. (2023) enjoying anytime regret bound, by leveraging tools from the strongly adaptive regret minimization literature; Angelopoulos et al. (2023) which extends upon ACI ideas by relying on control theory to add more information on the temporal structure, notably on the scores; Angelopoulos et al. (2024) proposing to use adaptive learning rates _γt_ in ACI, and even retrieving asymptotic control in probability when the data points are in fact i.i.d., i.e. lim _T_ 1 _→_ + _∞_ P _YT_ 1 _∈ C_[�] _T_ 1 _,α_ ( _XT_ 1) _−→_ 1 _− α_ . � � A very recent work (Yang et al., 2024) takes the counterpoint of most of these works by explicitly optimizing for efficiency of the intervals, while preserving long-term coverage. 

## **Chapter 4** 

## **Technical Summary of the Contributions** 

This chapter detail each contributions of this manuscript. While motivated by the task of forecasting electricity prices, the methods developed are generic: they can be applied in _any_ sensitive fields. 

## **– 4.1 Contributions’ summary of Part II Time Series** 

**Chapter 5 detailed summary.** Our approach is to illustrate the usefulness of ACI on time series with general dependency and non-stationarity, as it was initially developed for distribution shifts. 

We start by studying theoretically, using Markov Chain theory, the impact of _γ_ on the length of the predictive intervals, in order to describe not only the _validity_ but also the _efficiency_ of ACI. This is critical as the convergence rate of ACI favors large _γ_ , which are associated to frequent uninformative predictive sets. Moreover, ACI is usually applied without knowing the type of data it will encounter. If the scores are actually exchangeable, ACI’s _validity_ would not improve upon SCP (known to be _valid_ ), thus assessing ACI’s impact on _efficiency_ is necessary. Thereby, we first provide an analysis in the exchangeable case, then in the auto-regressive one (time series). Define _L_ ( _αt_ ) the length of the interval predicted by ACI at time _t_ (dependence in _γ_ is hidden), and _L_ 0 the length of the interval predicted by the non-adaptive algorithm (or equivalently, _γ_ = 0). 

**Theorem 4.1.1.** _Assume that: (i) α ∈_ Q _; (ii) the scores are exchangeable with quantile function Q; (iii) the quantile function Q is perfectly estimated at each time; (iv) the quantile function Q is bounded and C_[4] ([0 _,_ 1]) _. Then, for all γ >_ 0 _,_ ( _αt_ ) _t>T_ 0 _forms a Markov T_ 0+ _T_ 1 _Chain, that admits a stationary distribution πγ, and T_ 11 _t_ =� _T_ 0+1 _L_ ( _αt_ ) _T_ 1 _−→→a.s._ + _∞_[E] _[π][γ]_[[] _[L]_[]] _[not.]_ = E _α_ ˜ _∼πγ_ [ _L_ (˜ _α_ )] _. Moreover, as γ →_ 0 _,_ E _πγ_ [ _L_ ] = _L_ 0 + _Q[′′]_ (1 _− α_ ) _[γ]_ 2 _[α]_[(1] _[ −][α]_[) +] _[ O]_[(] _[γ]_[3] _[/]_[2][)] _[.]_ 

For standard distributions, _Q[′′]_ (1 _− α_ ) _>_ 0, and Theorem 4.1.1 implies that ACI on exchangeable scores degrades the efficiency linearly with _γ_ compared to CP: _γ_ = 0 (standard SCP) is better. 

57 

_Chapter 4. Technical Summary of the Contributions_ 

58 

A second theorem along with numerical analysis prove that, if the residuals are autoregressive of coefficient _ϕ_ (the higher the more important the temporal dependence) and the calibration is perfect, then there exists an optimal _γ[∗] >_ 0 minimizing the average length for high _ϕ_ , and its value depends on the time dependence strength. 

These results stress that choosing _γ_ is crucial but its optimal value, with respect to efficiency, depends on the unknown data distribution. Therefore, we design `AgACI` , a parameter-free method using online expert aggregation (Cesa-Bianchi and Lugosi, 2006). Based on the pinball loss of level 1 _−[α]_ 2[(resp.] _[α]_ 2[),] `[AgACI]`[assigns][weights][to][each][expert][(an] expert is a version of ACI with some _γ_ ) depending on their previous performances in order to output a unique upper bound (resp. lower bound) which is the weighted mean of the experts upper (resp. lower) bounds. 

Finally, we compare ACI with various _γ_ , `AgACI` and benchmark methods, on extensive synthetic experiments of increasing temporal dependence and on the task on forecasting French electricity prices in 2019. These experiments highlight that: 

- Benchmark methods are not robust to the increase of the temporal dependence; 

- ACI is robust to this increase, maintaining validity in all settings with a well-chosen _γ_ ; 

- `AgACI` is robust to this increase without choosing _γ_ , at the cost of not being the smallest. 

**Chapter 6 detailed summary.** To go further on the application to electricity prices forecasting, we conduct extensive experiments on a novel data set containing the French electricity spot prices during the turbulent 2020-2021 years. First, we build a new explanatory variable revealing high predictive power, namely the nuclear availability. Then, we benchmark state-of-the-art probabilistic electricity prices forecastings methods, showcasing that picking _a_ model a priori is complex as _i_ ) they all behave very differently, and _ii_ ) none of them maintains coverage on the most hazardous period of late 2021. Therefore, we study the performance of operational fixed prediction models that can be made adaptive through a plugged-in layer, useful when facing non-stationarity without completely retraining the underlying model. We consider two post-hoc layers: _i_ ) online CP through a proposal of novel conformalization that respects the forecast horizon during calibration, coined `OSSCP-horizon` , as well as `AgACI` , and _ii_ ) online aggregation of individual forecasts. Both approaches enhance the coverage of the resulting predictive intervals, and combining them through the aggregation of various `AgACI` appears to be the best strategy, on this particular task at least. Moreover, analysing this specific aggregation sheds light on many domain phenomena thanks to the aggregation weights interpretability: we are able to observe ruptures on 2020 Easter’s day (significantly lower prices due to Covid19 lockdown on top of Easter’s day) or on early October 2021 (corresponding to the increase in gas and carbon emission prices), and to showcase the importance of aggregating the lower and upper bounds independently as they model very distinct phenomena. 

_4.2. Contributions’ summary of Part III – Missing Values_ 

59 

## **– 4.2 Contributions’ summary of Part III Missing Values** 

To encode missing values, we define the mask, or missing pattern, _M ∈M ⊆{_ 0 _,_ 1 _}[d]_ as the binary random vector such that, for any _i ∈_ �1 _, d_ �, _Mi_ = 1 if and only if _Xi_ is missing. Therefore, there exists at most 2 _[d]_ masks: this number grows exponentially in the problem’s dimension, posing statistical and computational challenges. One of the most popular strategies to deal with missing values in a supervised learning framework suggests imputing the missing entries with plausible values to get completed data, on which any analysis can be performed (Le Morvan et al., 2021). This is called _impute-then-predict_ . 

**Chapter 7 detailed summary.** We study CP with missing covariates, aiming to build � predictive sets that now depend on the mask, i.e. _Cn,α_ ( _X, M_ ). Specifically, we study downstream Quantile Regression (QR) based CP, like CQR (Romano et al., 2019), on impute-then-predict strategies. Still, the proposed approaches also encapsulate other regression algorithms, and even classification. 

We show that CP on impute-then-predict is _marginally_ valid regardless of the model, missingness distribution, and imputation function. We describe how different masks (i.e. the set of observed covariates) introduce additional heteroskedasticity: _the predictive uncertainty strongly depends on the set of covariates observed_ . We therefore focus on achieving valid coverage _conditionally on the mask_ , coined MCV – Mask-Conditional-Validity. MCV is desirable in practice, as occurrence of missing values are linked to important attributes. 

Traditional approaches such as QR and CQR fail to achieve MCV because they do not account for this core connection between missing values and uncertainty. Figure 4.1 shows on a toy example with only 3 features – thus 2[3] _−_ 1 = 7 possible masks – how the coverage of QR and CQR varies depending on the mask. Both methods dramatically undercover when the most important variable ( _X_ 2) is missing, and the loss of coverage worsens when 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0077-07.png)


**----- Start of picture text -----**<br>
QR (no guarantee) CQR (marginal validity)<br>1 . 0<br>1  − ↵<br>0 . 8 Lowest<br>Lowest mask<br>mask cov.<br>cov.<br>0 . 6 ✗ MCV: ✗ ✓ MCV: ✗<br>CQR-MDA with exact masking CQR-MDA with nested masking<br>(mask-conditional-validity - MCV) (mask-conditional-validity - MCV)<br>1 . 0<br>Lowest Lowest<br>1  − ↵ mask mask<br>cov. cov.<br>0 . 8<br>0 . 6 ✓ MCV: ✓ ✓ MCV: ✓<br>X Marginalfullyobserved XX 11missing , X 2)missing XX 22missing , X 3)missing XX 31missing , X 3)missing X Marginalfullyobserved XX 11missing , X 2)missing XX 22missing , X 3)missing XX 31missing , X 3)missing<br>( ( ( ( ( (<br>coverage<br>Average<br>coverage<br>Average<br>**----- End of picture text -----**<br>


Figure 4.1: Coverage of the predictive intervals depending on which features are missing, among the 3 features. Evaluation over 200 runs. 

_Chapter 4. Technical Summary of the Contributions_ 

60 

additional features are missing. 

We show how to form prediction intervals that are MCV, by suggesting two conformal methods sharing the same core idea of missing data augmentation (MDA): the calibration data is artificially masked to match the mask of the test point. 

The first one, _CP-MDA with exact masking_ , relies on building an ideal calibration set whose data points have the exact same mask as of the test point. We show its MCV under exchangeability and Missing Completely At Random. 

The second one, _CP-MDA with nested masking_ , does not require such an ideal calibration set. Instead, it builds a calibration set in which the data points have _at least_ the same mask as the test point, i.e., this artificial masking results in calibration points having possibly more missing values than the test point. We show the latter method also achieves MCV, at the cost of an additional assumption: stochastic domination of the quantiles. 

Figure 4.1 illustrates CP-MDA’s MCV, as their lowest mask coverage is above 1 _− α_ . We strengthen the empirical validation of our algorithms through more complex synthetic experiments than in Figure 4.1, along with semi-synthetic experiments where only the distribution of _M_ given ( _X, Y_ ) is controlled but not the distribution of ( _X, Y_ ). And finally, we conduct experiments on real critical care data. All of these experiments confirm that MDA achieves MCV while CQR fails to ensure MCV. 

**Chapter 8 detailed summary.** Following the introduction of MCV criterion in Chapter 7, our objective in this chapter is to deepen the discussion on when and how it is possible to achieve MCV. Notably, we are interested in understanding _i_ ) what assumptions are necessary to ensure informative MCV is achievable, _ii_ ) how to design a MCV-tailored methodology with general probabilistic models, and _iii_ ) what happens when these assumptions are not satisfied. 

First, we provide hardness results on (distribution-free) MCV. 

**Theorem 4.2.1.** _If any C_[�] _n,α is distribution-free MCV then for any distribution P , for any mask m such that PM_ ( _m_ ) _>_ 0 _, it holds:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0078-10.png)


In other words, any distribution-free MCV estimator outputs uninformative predictive sets on any mask that does not represent a high enough proportion of the training data. We deepen the analysis and show that this remain true _i_ ) if we suppose that the estimator is MCV only when _M_ and _X_ are independent, and _ii_ ) if we suppose that the estimator is MCV only when _M_ is independent of _Y_ given _X_ . Therefore, to hopefully construct an estimator that provides meaningful MCV, it has to be MCV only on distribution such that the dependence between _M_ and the pair ( _X, Y_ ) is constrained. Importantly, this theoretical analysis brings new insights on the achievability of _X_ -group-conditional validity (i.e. conditioning on the event _X ∈V_ ( _x_ )), beyond MCV. 

_4.2. Contributions’ summary of Part III – Missing Values_ 

61 

Second, we investigate the interplay between missing values and quantile regression. Characterizing it is hard in general, but becomes explicit under a multivariate Gaussian setting or linear model. We show that _i_ ) predictive uncertainty often increases with more missing values: we provide formal statements of this idea (in terms of conditional variance, inter-quantile distance and predictive interval length) and exhibit assumptions under which these properties are satisfied; _ii_ ) when one aim at estimating quantiles, it is crucial that the learner is able to retrieve the mask to construct intervals, in contrast to classic mean regression where the mask is not as essential; _iii_ ) especially, data dependent imputation might not be the best choice for predictive uncertainty quantification that is adaptive to the mask. 

Third, we unify the algorithmic framework of Chapter 7 into a unique methodology, coined `CP-MDA-Nested` _[⋆]_ , that explicitly allows for the classification setting. It bridges the gap between the precision of strict subsampling to obtain the exact same mask (associated with high coverage variance), and the variance reduction of keeping all of the observations (associated with overly conservative predictive sets), by allowing any subsampling scheme, as long as it is independent of the calibration and test features and labels. Moreover, we draw an important analogy between `CP-MDA-Nested` _[⋆]_ and leave-one-out or _K_ -fold CP approaches. This enables us to provide theoretical guarantees on `CP-MDA-Nested` _[⋆]_ in terms of MCV, under exchangeability and Missing Completely At Random assumptions. 

Lastly, we conduct broader experiments than in Chapter 7 showcasing that `CP-MDA-Nested` _[⋆]_ is empirically robust to strong dependence between _M_ and _X_ , as it maintains MCV under various Missing At Random and Missing Non At Random scenarios. However, when _Y ⊥⊥M |X_ is not satisfied, `CP-MDA-Nested` _[⋆]_ does not ensure MCV experimentally, unless the imputation is accurate enough. Overall, these numerical experiments emphasize the robustness of `CP-MDA-Nested` _[⋆]_ beyond its theoretical scope of validity. 

## **Part II** 

## **Time Series** 

63 

## **Chapter 5** 

## **Adaptive Conformal Predictions for Time Series** 

Uncertainty quantification of predictive models is crucial in decision-making problems. Conformal prediction is a general and theoretically sound answer. However, it requires exchangeable data, excluding time series. While recent works tackled this issue, we argue that Adaptive Conformal Inference (ACI, Gibbs and Candès, 2021), developed for distribution-shift time series, is a good procedure for time series with general dependency. We theoretically analyse the impact of the learning rate on its efficiency in the exchangeable and auto-regressive case. We propose a parameter-free method, AgACI, that adaptively builds upon ACI based on online expert aggregation. We lead extensive fair simulations against competing methods that advocate for ACI’s use in time series. We conduct a real case study: electricity price forecasting. The proposed aggregation algorithm provides efficient prediction intervals for day-ahead forecasting. All the code and data to reproduce the experiments are made available on GitHub. 

65 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

66 

||**Contents**|
|---|---|
||5.1<br>Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>67<br>5.2<br>Setting: ACI for time series . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>69<br>5.3<br>Impact of _γ_ on ACI efciency . . . . . . . . . . . . . . . . . . . . . . . . . .<br>70<br>5.3.1<br>Exchangeable case . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>71<br>5.3.2<br>AR(1) case<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>71<br>5.4<br>Adaptive strategies based on ACI . . . . . . . . . . . . . . . . . . . . . . . .<br>73<br>5.5<br>Numerical evaluation on synthetic data sets . . . . . . . . . . . . . . . . . .<br>74<br>5.5.1<br>Data generation process and settings . . . . . . . . . . . . . . . . . .<br>75<br>5.5.2<br>Impact of _γ_, performance of AgACI<br>. . . . . . . . . . . . . . . . . .<br>76<br>5.5.3<br>Description of baseline methods . . . . . . . . . . . . . . . . . . . . .<br>77<br>5.5.4<br>Experimental results: impact of _ϕ, θ_<br>. . . . . . . . . . . . . . . . . .<br>78<br>5.6<br>Forecasting French electricity spot prices . . . . . . . . . . . . . . . . . . . .<br>79<br>5.6.1<br>Presentation of the price data . . . . . . . . . . . . . . . . . . . . . .<br>79<br>5.6.2<br>Price prediction with predictive intervals in 2019 . . . . . . . . . . .<br>80<br>5.7<br>Conclusion<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>81<br>5.A Details on Split Conformal Prediction<br>. . . . . . . . . . . . . . . . . . . . .<br>83<br>5.B<br>Proof of the results presented in Section 5.3 and additional numerical experi-<br>ments<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>87<br>5.C<br>Experimental details. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100<br>5.D Additional experiments on synthetic data sets . . . . . . . . . . . . . . . . . 103<br>5.E<br>Forecasting French electricity spot prices . . . . . . . . . . . . . . . . . . . . 106|



_5.1. Introduction_ 

67 

## **5.1 Introduction** 

The increasing use of renewable intermittent energy leads to more dependent and volatile energy markets. Therefore, an accurate electricity price forecasting is required to stabilize energy production planning, gathering loads of research work as evidenced by recent substantial reviews (Weron, 2014; Lago et al., 2018, 2021). Furthermore, probabilistic forecasts are needed to develop risk-based strategies (Gaillard et al., 2016; Maciejowska et al., 2016; Nowotarski and Weron, 2018; Uniejewski and Weron, 2021). On the one hand, the lack of uncertainty quantification of predictive models is a major barrier to the adoption of powerful machine learning methods. On the other hand, probabilistic forecasts are only valid asymptotically or upon strong assumptions on the data. 

Conformal prediction (CP, Vovk et al., 1999, 2005; Papadopoulos et al., 2002) is a promising framework to overcome both issues. It is a general procedure to build predictive intervals for any (black box) predictive model, such as neural networks, which are _valid_ (i.e. achieve nominal marginal coverage) in finite sample and without any distributional assumptions except that the data are exchangeable. 

Thereby, CP has received increasing attention lately, favored by the development of _split conformal prediction_ (SCP, Lei et al., 2018, reformulated from _inductive_ CP, Papadopoulos et al., 2002). More formally, suppose we have _n_ training samples ( _xi, yi_ ) _∈_ R _[d] ×_ R, _i ∈_ �1 _, n_ �, realizations of random variables ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ), and that we aim at predicting a new observation _yn_ +1 at _xn_ +1. Given a _miscoverage rate α ∈_ [0 _,_ 1] fixed by the user (typically 0.1 or 0.05) the aim is to build a predictive interval _Cα_ such that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0085-06.png)


with _Cα_ as small as possible, in order to be informative. For the sequel, we call a _valid interval_ an interval satisfying equation (5.1) and an _efficient interval_ when it is as small as possible (Vovk et al., 2005; Shafer and Vovk, 2008). 

To achieve this, SCP first splits the _n_ points of the training set into two sets Tr _,_ Cal _⊂_ �1 _,_ n�, to create a _proper training set_ , Tr, and a _calibration set_ , Cal. On the proper training set a regression model _µ_ ˆ (chosen by the user) is fitted, and then used to predict on the calibration set. A _conformity score_ is applied to assess the conformity between the calibration’s response values and the predicted values, giving _S_ Cal = _{_ ( _si_ ) _i∈_ Cal _}_ . In regression, usually the absolute ˆ ˆ value of the residuals is used, i.e. _si_ = _|µ_ ( _xi_ ) _−yi|_ . Finally, a corrected[1] (1 _−α_ )-th quantile of these scores _Q_[�] 1 _−α_ ˆ( _S_ Cal) is computed to define the size of the interval, which, in its simplest ˆ form, is centered on the predicted value: _Cα_ ( _xn_ +1) = _C_[�] _α_ ˆ( _xn_ +1) := [ _µ_ ( _xn_ +1) _± Q_[�] 1 _−α_ ˆ( _S_ Cal)]. These steps are detailed in Section 5.A, and illustrated in Figure 5.9. More details on CP, including beyond regression, are given in Vovk et al. (2005); Angelopoulos and Bates (2023). 

The cornerstone of SCP _validity_ results is the exchangeability assumption of the data (see Lei et al., 2018, and Section 5.A.3). However, this assumption is not met in time series forecasting problems. Despite the lack of theoretical guarantees, several works have 

> 1The correction _α → α_ ˆ is needed because of the inflation of quantiles in finite sample (see Lemma 2 in Romano et al. (2019) or Section 2 in Lei et al. (2018)). 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

68 

applied CP to time series. Dashevskiy and Luo (2008, 2011) apply original ( _inductive_ ) CP (Papadopoulos et al., 2002) to both simulated (using Auto-Regressive Moving Average (ARMA) processes) and real network traffic data and obtain _valid_ intervals. Wisniewski et al. (2020); Kath and Ziel (2021) apply SCP respectively to financial data (e.g. markets makers’ net positions) and to electricity price forecasting on various markets. In order to account for the temporal aspect, they consider an online version of SCP. In both studies, the _validity_ varied greatly depending on the markets and the underlying regression model, suggesting that further developments of CP and theoretical guarantees for time series are needed. 

To this end, Chernozhukov et al. (2018) extend the CP theory to ergodic cases in order to include dependent data. Xu and Xie (2021) improve on that theory and propose a new algorithm, Ensemble Prediction Interval (EnbPI), adapted to time series by adding a sequential aspect. 

Another case that breaks the exchangeability assumption is _distribution shift_ , which allows for example to deal with cases where the test data is shifted with respect to the training data. Tibshirani et al. (2019) consider covariate shift while Cauchois et al. (2024) tackle a joint distributional shift setting (that is, of ( _X, Y_ )). In both studies, a single shift in the distribution is considered, a major limitation for applying these methods to time series. In an adversarial setting, Gibbs and Candès (2021) propose Adaptive Conformal Inference (ACI), accounting for an undefined number of shifts on the joint distribution. It is based on refitting the predictive model, as well as updating online the quantile level used by a recursive scheme depending on an hyper-parameter _γ_ (a learning rate). Furthermore, they prove an asymptotic _validity_ result for any data distribution. 

We argue in this work that the design and guarantees of ACI can be beneficial for dependent data without distribution shifts. 

**Contributions.** We propose to analyse ACI (Gibbs and Candès, 2021) in the context of time series with general dependency and make the following contributions: 

• Relying on an asymptotic analysis of ACI’s behaviour for simple time series distribution, we prove that ACI deteriorates _efficiency_ in an exchangeable case (closed-form expression) while improving it in an AR setting (numerical approximation) with a wellchosen _γ_ (Section 5.3). 

• We introduce AgACI, a parameter-free method using online expert aggregation, to avoid choosing _γ_ , achieving good performances in terms of _validity_ and _efficiency_ (Section 5.4). 

• We compare ACI to EnbPI and online SCP on extensive synthetic experiments and we propose an easy-to-interpret visualisation combining _validity_ and _efficiency_ (Section 5.5). 

• We forecast and give predictive intervals on French electricity prices, an area where accurate predictions, but also controlled predictive intervals, are required (Section 5.6). 

To allow for better benchmarking of existing and new methods, we provide (re-)implementations in Python of (all) the described methods and a complete pipeline of analysis on GitHub. As explained in Section 5.4, the code for AgACI is, for now, the only one available only in R. 

**Notations.** In the sequel, the following notations are used: � _a, b_ � := _{a, a_ + 1 _, . . . , b}_ ; 

_5.2._ ~~_Setting_~~ _: ACI for time series_ 

69 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0087-02.png)


**----- Start of picture text -----**<br>
1<br>0<br>− 1<br>0 200 400 500 550 600 650 700 750 800 850 900 950 1000<br>t t<br>εt<br>**----- End of picture text -----**<br>


Figure 5.1: ACI on one simulated path _εt_ , _t_ = 1 _, . . . ,_ 1000, from an AR(1) process (in black). The first 500 values form the initial calibration set (left subplot), and predicted interval bounds are computed on the last 500 points (right) for _γ_ = 0, _γ_ = 0 _._ 01 and _γ_ = 0 _._ 05. 

Q refers to the set of rational numbers; _C_[4] ([0 _,_ 1]) refers to the set of 4-times continuously differentiable functions on [0 _,_ 1];[not.] = defines a notation; # _A_ is the cardinal of the set _A_ . 

## **5.2 Setting: ACI for time series** 

In this section, we introduce ACI and our framework. We consider _T_ 0 observations ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xT_ 0 _, yT_ 0) in R _[d] ×_ R. The aim is to predict the response values and give predictive intervals for _T_ 1 subsequent observations _xT_ 0+1 _, . . . , xT_ 0+ _T_ 1 sequentially: at any prediction step _t ∈_ � _T_ 0 + 1 _, T_ 0 + _T_ 1�, _yt−T_ 0 _, . . . , yt−_ 1 have been revealed. Thereby, the data (( _xt−T_ 0 _, yt−T_ 0) _, . . . ,_ ( _xt−_ 1 _, yt−_ 1)) are used for the construction of the predicted interval. 

**Adaptive Conformal Inference.** Proposed by Gibbs and Candès (2021), ACI is designed to adapt CP to temporal distribution shifts. The idea of ACI is twofold. First, one considers an online procedure with a random split[2] , i.e., Trt and Calt are random subsets of the last _T_ 0 points. Second, to improve adaptation when the data is highly shifted, an _effective miscoverage level αt_ , updated recursively, is used instead of the target level _α_ . Set _α_ 1 = _α_ , and for _t ≥_ 1 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0087-08.png)


for _γ ≥_ 0[3] . If ACI does not cover at time _t_ , then _αt_ +1 _≤ αt_ , and the size of the predictive interval increases; conversely when it covers. Nothing prevents _αt ≤_ 0 or _αt ≥_ 1. While the ˆ later is rare (as _α_ is small) and produces by convention _C_[�] _αt_ ( _·_ ) = _{µ_ ( _·_ ) _}_ (i.e. _Q_[�] 1 _−αt_ = 0) , the former can happen frequently for some _γ_ , giving _C_[�] _αt ≡_ R ( _Q_[�] 1 _−αt_ = + _∞_ ). 

**How to deal with infinite intervals.** A specificity of ACI’s algorithm is thus to often produce infinite intervals. Defining the _average_ length of an interval is then impossible. In order to assess the _efficiency_ in the following, we consider two solutions: (i) imputing the length of infinite intervals by (twice) the overall maximum of the residuals, or _Q_ (1) if the residual’s quantile function is known and bounded[4] ; (ii) focusing on the median instead. 

**ACI on time series with general dependency.** As highlighted by Wisniewski et al. (2020); Kath and Ziel (2021), the first step to adapt a method for dependent time series 

> 2Figure 5.5(a) with training and calibration part shuffled randomly. 

> 3ACI actually wraps around _any_ CP procedure, here the definition is given using mean regression SCP. 

> 4This happens in practice when the response and prediction are bounded, e.g., thanks to physical/real constraints as for the spot prices presented in Section 5.6.1, that are bounded by market rules. 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

70 

is to work online which is the case for ACI. Moreover, the update of the quantile level according to the previous error implies that ACI could cope with a fitted model that has not correctly caught the temporal evolution, such as a trend, a seasonality pattern or a dependence on the past. Therefore, ACI is a perfect candidate for CP for time series with general dependency. To account for the temporal structure, we change the random split to a sequential split.[5] 

To gain understanding on ACI in the context of dependent temporal data, we analyse a situation where a fitted regression model _µ_ ˆ produces AR(1) residuals, thus _yt − µ_ ˆ( _xt_ ) = _εt_ , where _εt_ is an AR(1) process: _εt_ +1 = 0 _._ 99 _εt_ + _ξt_ +1, with _ξt ∼N_ (0 _,_ 0 _._ 01). We plot this toy example in Figure 5.1, for _T_ 0 = _T_ 1 = 500. Three versions of ACI are compared: _γ_ = 0, the quantile level is not updated but the calibration set Calt is; _γ_ = 0 _._ 01 and _γ_ = 0 _._ 05. To obtain an insightful visualisation[6] , we represent the interval [ _±Q_[�] 1 _−αt_ ( _S_ Calt)] instead of � _Cαt_ ( _xt_ ). When no intervals are displayed, ACI is predicting R. Here and in the sequel, we use _α_ = 0 _._ 1. 

In this toy example, the coverage rate among many observations is _valid_ for _γ ∈ {_ 0 _._ 01 _,_ 0 _._ 05 _}_ (90% and 92% of points included) but not for _γ_ = 0 (72.6%). Moreover, Figure 5.1 shows that the type of errors depends on _γ_ . For _γ_ = 0, ACI excludes consecutive observations (e.g. for _t ∈_ [810 _,_ 860], zoomed-in plot). For _γ ∈{_ 0 _._ 01 _,_ 0 _._ 05 _}_ , ACI manages to adapt to these observations, and the higher the _γ_ , the less the adaptation is delayed. Furthermore, when the residuals are small and far from both interval bounds, ACI quickly reduces the interval’s length and produces more _efficient_ intervals. Consequently, ACI may also not cover on points for which the residuals have a relatively small values compared to the calibration’s values (e.g. for _t ∈_ [760 _,_ 785]). 

## **5.3 Impact of** _γ_ **on ACI efficiency** 

The choice of the parameter _γ_ strongly impacts the behaviour of ACI: while the method always satisfies the _asymptotic validity_ property, i.e. _T_ 1 � _Tt_ =1[1] _[{][y][t][∈][/][C]_[�] _[α] t_[(] _[x][t]_[)] _[}] −→a.s. T →∞[α]_ (Proposition 4.1 in Gibbs and Candès, 2021), this property does not give any insight on the length of resulting intervals. Besides, this guarantee directly stems from the fact that _T_ 1 � _Tt_ =1[1] _[{][y][t][∈][/][C]_[�] _[α] t_[(] _[x][t]_[)] _[} −][α][≤]_[2] _[/]_[(] _[γT]_[)][.][This][tends][to][suggest][the][use][of][larger] _[γ]_[values,] that unfortunately generate frequent infinite intervals. Here, we thus analyse the impact of _γ_ on ACI’s _efficiency_ in simple yet insightful cases: in Section 5.3.1, focusing on the exchangeable case, then in Section 5.3.2, with a simple AR process on the residuals. 

**Approach.** Our focus is on the impact of the key parameter _γ_ . Analysing simple theoretical distributions allows to build intuition on the behaviour of the algorithm for more complex data structure. In order to derive theoretical results, we thus make supplementary modelling assumptions on the residuals, and do not consider the impact of the calibration set: we introduce _Q_ the quantile function of the scores and assume, for all _α_ ˆ and _t_ , � ˆ _Q_ 1 _−α_ ˆ( _S_ Calt) = _Q_ (1 _− α_ ). This corresponds to considering the limit as #Cal _→∞_ . This 

> 5As in Figure 5.5(a). This is also consistent with OSSCP (Sec. 5.5.3). 

> 6We suggest focusing the visualisation on the scores to analyse the behaviour of CP methods, as they are at the core of the _validity_ proof. A detailed discussion on this is given in App. 5.A.5 

_5.3. Impact of γ on ACI efficiency_ 

71 

allows to focus on the impact of recursive updates in (5.2) and describe their behaviour by relying on Markov Chain theory. 

## **5.3.1 Exchangeable case** 

ACI is usually applied in an adversarial context. If the scores are actually exchangeable, ACI’s _validity_ would not improve upon SCP (known to be quasi-exactly _valid_ ), thus assessing ACI’s impact on _efficiency_ is necessary. Define _L_ ( _αt_ ) = 2 _Q_ (1 _− αt_ ) the length of the interval predicted by the adaptive algorithm at time _t_ , and _L_ 0 = 2 _Q_ (1 _− α_ ) the length of the interval predicted by the non-adaptive algorithm (or equivalently, _γ_ = 0). 

**Theorem 5.3.1.** _Assume that: (i) α ∈_ Q _; (ii) the scores are exchangeable with quantile function Q; (iii) the quantile function is perfectly estimated at each time (as defined above); (iv) the quantile function Q is bounded and C_[4] ([0 _,_ 1]) _. Then, for all γ >_ 0 _,_ ( _αt_ ) _t>_ 0 _forms a Markov Chain, that admits a stationary distribution πγ, and_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0089-06.png)


_Moreover, as γ →_ 0 _,_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0089-08.png)


**Interpretation of assumptions.** Assumption (i) is weak since a practitioner will always select _α ∈_ Q while assumption (ii) describes the classical exchangeable setting. The main assumptions are (iii) and (iv): (iii) can be interpreted as considering an infinite calibration set while (iv) is necessary[7] in order to define E _πγ_ [ _L_ ]: here, we extend _Q_ (1 _− α_ ˆ) by _Q_ (1) for _α_ ˆ _<_ 0. When _Q_[ˆ] _≡ Q_[ˆ] _t_ is the empirical quantile function on a calibration set Cal, the convergence in Theorem 5.3.1 holds conditionally to Cal. Finally, the regularity assumption on _Q_ is purely technical. 

**Interpretation of the result.** For standard distributions, _Q[′′]_ (1 _− α_ ) _>_ 0,[8] and Theorem 5.3.1 implies that ACI on exchangeable scores _degrades_ the _efficiency_ linearly with _γ_ compared to CP. This is an important takeaway from the analysis, that underlines that such adaptive algorithms may actually hinder the performance if the data does not have any temporal dependency, and a small _γ_ is preferable. For example, if the residuals are standard gaussians, for _α_ = 0 _._ 01, setting _γ_ = 0 _._ 03 (resp. _γ_ = 0 _._ 05) will increase the length by 1.59% (resp. by 3.38%) with respect to _γ_ = 0. 

## **5.3.2 AR(1) case** 

We now consider the case of (highly) correlated residuals, which happens in many practical time series applications. 

> 7 _∀γ>_ 0, P _πγ_ (˜ _α ≤_ 0) _>_ 0: we need _|Q_ (1) _|< ∞_ to define E _πγ_ [ _L_ ]. 

> 8as _Q′_ ( _x_ ) = _f_ ( _Q_ 1( _x_ ))[with] _[f]_[the][scores’][probability][density][function,] _[Q][′]_[(] _[x]_[)][increases][locally][around] _[x]_[if][and] only if _f_ decreases locally around _Q_ ( _x_ ) ( _Q_ is increasing). Thus, _Q[′′]_ ( _x_ ) _>_ 0 if and only if _f_ decreases locally around _Q_ ( _x_ ). Thereby, for _x_ = 1 _− α_ high (usually the case), _Q[′′]_ (1 _− α_ ) _>_ 0 for standard distributions. 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

72 

**Definition 5.3.1** (AR(1) clipped) **.** _εt_ +1 = _ϕεt_ + _ξt_ +1 with ( _ξt_ ) _t_ i.i.d. random variables admitting a continuous density with respect to Lebesgue measure, of support _S_ clipped at a large value _R_ , and [ _−R, R_ ] _⊂S_ 

**Theorem 5.3.2.** _Assume that: (i) α ∈_ Q _; (ii) the residuals follow an AR(1) process clipped at R of parameter ϕ (Definition 5.3.1); (iii) the quantile function Q of the stationary distribution of_ ( _εt_ ) _t is known. Then_ ( _αt, εt−_ 1) _is a homogeneous Markov Chain in_ R[2] _that admits a unique stationary distribution πγ,ϕ. Moreover,_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0090-04.png)


We numerically estimate _γϕ[∗]_[=][ argmin] _[γ]_[E] _[π] γ,ϕ_[[] _[L]_[]][ in Figure][ 5.2][.][To do so, AR(1) processes] of length _T_ = 10[6] are simulated for various _ϕ_ and asymptotic variance 1. ACI is applied on each of them, with 100 different _γ ∈_ [0 _,_ 0 _._ 2]. Figure 5.2 (left) represents the average length depending on _γ_ for each _ϕ_ , and (right) the values of _γ_ minimizing this average length for each _ϕ_ (for 25 repetitions of the experiment). The average length is computed after imputing all the infinite intervals’ length by the maximum of the process, as explained in Section 5.2. A similar study using instead the median length is provided after the proofs in Section 5.B. 

**Interpretation.** We make the following observations: 

1. For high _ϕ_ , ACI indeed improves for a strictly positive _γ_ upon _γ_ = 0. This proves that ACI can be used to produce smaller intervals for time series CP. The function _γ �→_ E _πγ,ϕ_ [ _L_ ] decreases until _γϕ[∗]_[, then increases again, as expected because very large] _[ γ]_[cause the algorithm] to be less stable and produce numerous infinite intervals. 

2. In Figure 5.2 (left), zoomed-in plot, the black line represents asymptotic result of Theorem 5.3.1. We retrieve here that the expected length is minimal for _γ_ = 0 and grows linearly with _γ_ around 0. This behaviour is very similar for _ϕ_ = 0 _._ 6. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0090-09.png)


**----- Start of picture text -----**<br>
ϕ  =0 ϕ  =0.85 ϕ  =0.98 ϕ  =0.997<br>ϕ  =0.6 ϕ  =0.95 ϕ  =0.99 ϕ  =0.999<br>Thm. 3.1<br>0 . 08<br>4<br>0.01 0.03 0 . 06<br>0 . 04<br>3<br>0 . 02<br>2<br>0 . 00<br>0 . 00 0 . 05 0 . 10 0 . 15 0 . 20 0.0 0.6 0.85 0.95 0.980.99 0.997 0.999<br>γ ϕ<br>length<br>∗<br>Average γ<br>**----- End of picture text -----**<br>


Figure 5.2: Left: evolution of the mean length depending on _γ_ for various _ϕ_ . Right: _γ[∗]_ minimizing the average length for each _ϕ_ (each cross has a size proportional to the number of runs for which _γ[∗]_ was the minimizer). 

_5.4. Adaptive strategies based on ACI_ 

73 

3. For any _γ_ , the function _ϕ �→_ E _πγ,ϕ_ [ _L_ ] is decreasing (Figure 5.2, left). Indeed, stronger correlation between residuals (i.e., a higher _ϕ_ ), allows to build smaller intervals. This confirms that ACI’s impact strengthens with the strength of the temporal dependence. 4. Surprisingly, the function _ϕ �→ γϕ[∗]_[,][that][corresponds][to][the][optimal][learning][rate][for] a given signal, _is non-monotonic_ , (Figure 5.2, right). As _γ_ = 0 is optimal for _ϕ_ = 0, the function first increases. However, the optimal learning rate then diminishes as _ϕ_ increases. This sheds light on the complex intrinsic tradeoffs of the method: for small values of _ϕ_ , using _γ >_ 0 simply degrades the _efficiency_ ; for “moderate” values of _ϕ_ using a larger _γ_ is necessary to quickly benefit from the short-term dependency between residuals; finally, for larger values of _ϕ_ , the process exhibits a longer memory, thus it is crucial to find a smaller learning rate that produces more stable intervals, even if it means that the algorithm won’t adapt as quickly. 

**What if** _Q_ = _Q_[ˆ] **?** While our analysis provides a first step by comparing ACI to CP in the ideal case where the quantile distribution is known (for both methods), the impact of the finite-Cal is of interest. Indeed, if Cal is small, ACI can help to attain coverage **conditionally to a given** Cal even in the i.i.d. case. Yet intuitively, **marginally** , the randomness induced by ACI in the i.i.d. case would negatively impact efficiency w.r.t. _γ_ = 0, even in the finite-Cal case. Finite sample trade-offs and general analysis of the case _Q ̸_ = _Q_[ˆ] is an important open direction. 

Overall, these results highlight the importance of the choice of _γ_ , as not choosing _γ[∗]_ can lead to significantly larger intervals. In addition, they provide insights on the corresponding dynamics. Yet the choice of _γ_ in more complex practical settings remains difficult: this calls for adaptive strategies. 

## **5.4 Adaptive strategies based on ACI** 

To prevent the critical choice of _γ_ an ideal solution is an adaptive strategy with a time dependent _γ_ . We propose two strategies based on running ACI for _K ∈_ N values _{_ ( _γk_ ) _k≤K}_ of _γ_ , chosen by the user. Overall, this does not increase the computational cost because Trt and Calt are shared between all ACI; thus the only additional cost is the computation of the _K_ different quantiles. For any _xt_ , denote _C_[�] _αt,k_ ( _xt_ ) the interval at time _t_ built by ACI using _γk_ . 

**Naive strategy.** A simple strategy is to use at each step the _γ_ that achieved in the past the best _efficiency_ while ensuring _validity_ . For stability purposes, consider a warm-up period _Tw ≤ T_ 1 _−_ 1. For each _t ≥ T_ 0+ _Tw_ , we select _kt[∗]_ +1 _[∈]_[argmin] _k∈At_ � _t[−]_[1][ �] _[t] s_ =1[length][(] _[C]_[ �] _[α] s,k_[(] _[x][s]_[))] � with _At_ = _{k ∈_ �1 _, K_ � _| t[−]_[1][ �] _[t] s_ =1[1] _ys∈C_[�] _αs,k_ ( _xs_ ) _[≥]_[1] _[ −][α][}]_[or] _[k] t[∗]_ +1 _[∈]_[argmin] _k∈_ �1 _,K_ � _[{|]_[1] _[ −][α][ −] t[−]_[1][ �] _[t] s_ =1[1] _ys∈C_[�] _αs,k_ ( _xs_ ) _[|}]_[if] _[A][t]_[=] _[ ∅]_[.][For][the][first] _[T][w]_[steps,][an][arbitrary][strategy][is][applied] (in simulations, _γ_ = 0 for _t ≤ Tw_ = 50). 

**Online Expert Aggregation on ACI (AgACI).** Instead of picking one _γ_ in the grid, we introduce an adaptive aggregation of _experts_ (Cesa-Bianchi and Lugosi, 2006), with expert _k_ being ACI with parameter _γk_ . This strategy is detailed in Algorithm 9, and schematised in Figure 5.3. At each step _t_ , it performs two independent aggregations of the _K_ -ACI intervals 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

74 

� _Cαt,k_ ( _·_ )[not.] = [[ˆ] _b_[(] _t,k[ℓ]_[)][(] _[·]_[)] _[,]_[ˆ] _[b]_[(] _t,k[u]_[)][(] _[·]_[)]][,][one][for][each][bound,][and][outputs] _[C]_[�] _[t]_[(] _[·]_[)][not.] = [[˜] _b_[(] _t[ℓ]_[)][(] _[·]_[)] _[,]_[˜] _[b]_[(] _t[u]_[)] ( _·_ )]. Aggregation computes an optimal weighted mean of the experts (Line 11), where the weights _ωt,k_[(] _[ℓ]_[)][,] _[ω] t,k_[(] _[u]_[)][assigned][to][expert] _[k]_[depend][on][all][experts][performances][(suffered] _[losses]_[)] at time steps 1 _, · · · , t_ (Line 9). We use the pinball loss _ρβ_ , as it is frequent in quantile regression, where the pinball parameter _β_ is chosen to _α/_ 2 (resp. 1 _− α/_ 2) for the lower (resp. upper) bound. These losses are plugged in the _aggregation rule_ Φ. Finally, the aggregation rule can include the computation of the gradients of the loss ( _gradient trick_ , see Cesa-Bianchi and Lugosi, 2006, for more details). As aggregation rules require bounded experts, a thresholding step is added (Line 5). Note that the pinball loss helps to avoid large intervals (e.g. it strongly penalizes infinite or very large intervals). 

We chose Φ to be the Bernstein Online Aggregation (BOA, Wintenberger, 2017, see Section 5.C.1 for a brief description), that was successfully applied for financial data (Berrisch and Ziel, 2023; Remlinger et al., 2023). We rely on R package OPERA (Gaillard and Goude, 2021), which allows the user to easily select among many other aggregation rules (EWA (Vovk, 1990), ML-Poly (Gaillard et al., 2014) or FTRL (Shalev-Shwartz and Singer, 2007; Hazan, 2019), etc.) that give similar results in our experiments. We use the gradient trick in the simulations. In the sequel, AgACI refers to AgACI using BOA and gradient trick. 

**Algorithm 9** Online Expert Aggregation on ACI (AgACI) 

**Input:** Miscoverage rate _α_ , grid _{γk, k ∈_ �1 _, K_ � _}_ , aggregation rule Φ, threshold values _M_[(] _[ℓ]_[)] _, M_[(] _[u]_[)] . 1: Let _β_[(] _[ℓ]_[)] = _α/_ 2 and _β_[(] _[u]_[)] = 1 _− α/_ 2 

2: **for** _t ∈_ � _T_ 0 + 1 _, T_ 0 + _T_ 1� **do** 

3: **for** _k ∈_ �1 _, K_ � **do** 4: Compute[ˆ] _b_[(] _t,k[·]_[)][(] _[x][t]_[)][using][ACI][with] _[γ][k]_[.] 5: **if**[ˆ] _b_[(] _[·]_[)] _[∈][/]_[R] **[then]**[set][ ˆ] _[b]_[(] _[·]_[)] _t,k_[(] _[x][t]_[)] _t,k_[(] _[x][t]_[) =] _[ M]_[(] _[·]_[)] 6: **end for** 7: Set _C_[�] _t_ ( _xt_ ) = [[˜] _b_[(] _t[ℓ]_[)][(] _[x][t]_[)] _[,]_[˜] _[b]_[(] _t[u]_[)] ( _xt_ )] 8: **for** _k ∈_ �1 _, K_ � **do** _ω_[(] _[·]_[)] _t,k_[= Φ (] _[{][ ρ] β_[(] _[·]_[)][(] _[y][s][,]_[ˆ] _[b]_[(] _s,l[·]_[)][(] _[x][s]_[))] _[, s][ ∈]_[�] _[T]_[0][ + 1] _[, t]_[�] _[,]_ 9: _l ∈_ �1 _, K_ � _}_ ) 10: **end for** 11: Define[˜] _b_[(] _t_ +1 _[·]_[)][(] _[x]_[) =] � _Kk_ =1 _[ω] Kt_[(] _,[·] k_[)][ˆ] _[b]_[(] _t_ + _[·]_[)] 1 _,k_[(] _[x]_[)] for any _x ∈_ R _[d]_ � _l_ =1 _[ω] t,l_[(] _[·]_[)] 12: **end for** 

## **5.5 Numerical evaluation on synthetic data sets** 

In this section we conduct synthetic experiments on a wide range of data sets presented in Section 5.5.1. The goal of this section is twofold. First, in Section 5.5.2, comparing our proposed adaptive strategies to ACI with a wide range of _γ_ values. Second, in Section 5.5.4, 

_5.5. Numerical evaluation on synthetic data sets_ 

75 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0093-02.png)


**----- Start of picture text -----**<br>
Experts Previous upper Weights Weighted Forecasts Experts<br>bounds mean at t + 1<br>(a8 a agPoty- . (419) ( (L»x) ( C v)<br>. To+1 . t . t+] . .<br>. . . . .<br>. . . . .<br>Sh) ee<br>bids QL<br>To+1 t t+1<br>. . . . .<br>. . . . .<br>. . . . .<br>.a<br>\<br>**----- End of picture text -----**<br>


Figure 5.3: Scheme of AgACI algorithm, upper bound _u_ only, for a forecast at time _t_ + 1. A similar procedure is performed independently for the lower bound _ℓ_ in parallel. 

comparing performances of AgACI and ACI to that of competitors – namely EnbPI and online sequential SCP, described in Section 5.5.3. 

## **5.5.1 Data generation process and settings** 

We generate data according to: 

_Yt_ = 10 sin ( _πXt,_ 1 _Xt,_ 2) + 20 ( _Xt,_ 3 _−_ 0 _._ 5)[2] + 10 _Xt,_ 4 + 5 _Xt,_ 5 + 0 _Xt,_ 6 + _εt,_ (5.3) where the _Xt_ are multivariate uniformly distributed on [0 _,_ 1], and _Xt,_ 6 represents an uninformative variable. The noise _εt_ is generated from an ARMA(1,1) process of parameters _ϕ_ and _θ_ , i.e. _εt_ +1 = _ϕεt_ + _ξt_ +1 + _θξt_ , with _ξt_ a white noise called the _innovation_ (see Section 5.C.2 for details). When the noise is i.i.d., one retrieves the simulations from Friedman et al. (1983). The temporal dependence is present only in the noise in order to control its strength and its impact on the algorithms’ performance. 

Given the non-linear structure of the data generating process, we use a random forest (RF) as predictive model, with the same hyper-parameters through all the experiments (specified in Section 5.C.3). 

To assess the impact of the temporal structure, we vary _ϕ_ and _θ_ in _{_ 0 _._ 1 _,_ 0 _._ 8 _,_ 0 _._ 9 _,_ 0 _._ 95 _,_ 0 _._ 99 _}_ . To focus on the impact of the dependence structure, the value of the innovation’s variance is selected so that the asymptotic variance of _εt_ is independent of _ϕ, θ_ : here we choose lim _t→∞_ Var( _εt_ ) = 10. For each set of parameters, we generate _n_ = 500 samples ( _εt_ ) _t∈_ 1 _,T_ 0+ _T_ 1 with _T_ 0 = 200. In the sequel we display the results on an ARMA(1,1) which are representative of all the results obtained. For the sake of simplicity, we consider _ϕ_ = _θ_ . Complementary results (i) for an asymptotic variance of 1 (corresponding to a higher _signal to noise_ ratio), (ii) for AR(1) and MA(1) models are available in Section 5.D. 

**Joint visualisation of validity & efficiency.** In order to simultaneously assess _validity_ and _efficiency_ , in Figures 5.4, 5.6 and 5.8, we represent on the same graph the 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

76 

empirical coverage and average median length (used for _efficiency_ as imputing the infinite bounds by the maximum of the whole sequence is not always feasible in practice). In those three figures, the vertical dotted line represents the target miscoverage rate, _α_ = 0 _._ 1. Consequently, a method is _valid_ when it lies at the right of this line, and the lower the better. 

## **5.5.2 Impact of** _γ_ **, performance of AgACI** 

Figure 5.4 illustrates the behaviour of ACI (with multiple values of _γ_ ), the naive strategy (empty triangles) and AgACI (black stars) for increasing (from left to right) values of _ϕ_ , _θ_ , with _T_ 1 = 200. In particular, the top row shows the joint _validity_ & _efficiency_ and, for this figure only, we add in the bottom row the same graph using the average length after imputation (see details in Section 5.D) to assess _efficiency_ in another way. 

When _γ_ is small, one observes an undercoverage, which increases when the temporal dependency of _ε_ increases. Increasing _γ_ enables ACI to increase the interval’s size faster when we do not cover, and thus to improve _validity_ , which is achieved for high values of _γ_ ; however this also increases the frequency of uninformative (infinite) intervals, as deduced from the bottom row of Figure 5.4, where the average length after imputation grows with _γ_ . Remark that these results do not contradict the validity result recalled at the beginning of Section 5.3, which is only asymptotic while we predict on 200 points. For _ϕ, θ_ small, we observe that similarly to Theorem 5.3.1, the _efficiency_ does not improve with _γ_ . For moderate values of _ϕ, θ ∈{_ 0 _._ 8 _,_ 0 _._ 9 _,_ 0 _._ 95 _}_ , we observe that the average median length is decreasing with _γ_ for _γ ≥_ 0 _._ 01. This effect is observable on average but not present in all the 500 experiments. One possible explanation is that the shrinking effect of ACI on the predicted interval enables to significantly reduce the predicted interval when _γ_ is large, and this effect is, on average, more important than the number of large intervals. 

Moreover, the naive strategy is clearly not _valid_ : indeed it results in greedily choosing a _γ_ that achieved good results in the past, and is consequently slightly more likely to fail to 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0094-07.png)


**----- Start of picture text -----**<br>
ϕ  =  θ =0.1 ϕ  =  θ =0.8 ϕ  =  θ =0.9 ϕ  =  θ =0.95 ϕ  =  θ =0.99<br>14<br>γ<br>0 . 0700<br>13 0 . 0400<br>0 . 0100<br>AgACI<br>12 Naive method 0 . 0070<br>0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 0040<br>16 0 . 0010<br>15 0 . 0007<br>0 . 0004<br>14<br>0 . 0001<br>13<br>0 . 0000<br>12<br>0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90<br>Coverage Coverage Coverage Coverage Coverage<br>length<br>median<br>Average<br>imputation<br>after<br>length,<br>Average<br>**----- End of picture text -----**<br>


Figure 5.4: ACI performance with various _θ_ , _ϕ_ and _γ_ on data simulated according to equation (5.3) with a Gaussian ARMA(1,1) noise of asymptotic variance 10 (see Section 5.C.2). Top row: average median length w.r.t. the coverage. Bottom row: average length after imputation w.r.t. the coverage. Stars correspond to AgACI, and empty triangles to the naive choice. 

_5.5. Numerical evaluation on synthetic data sets_ 

77 

cover in future steps. Thereby, we do not consider it anymore. Finally, AgACI achieves _valid_ coverage without increasing the median length with respect to each expert, and even improves the coverage. Overall, it appears to be a good candidate as a parameter-free method. 

## **5.5.3 Description of baseline methods** 

We consider as baseline _online sequential split conformal prediction_ (OSSCP), a generalisation of SCP[9] . The other competitor is EnbPI (Xu and Xie, 2021), specifically designed for time series. Pseudo-codes and details are given in Section 5.C.4. Offline SCP (for which Trt _≡_ Tr0 and Calt _≡_ Cal0) is not considered as a competitor because it is unfair to compare an _offline_ algorithm to one that uses more recent data points. This corresponds to comparing a prediction at horizon _T_ large to one at horizon _T_ small. This is a limitation of the comparison in Xu and Xie (2021). 

**OSSCP.** We consider an online version of SCP by refitting the underlying regression model and recalibrating using the newest points. Moreover, to appropriately account for the temporal structure of the data, we use a _sequential split_ as in Wisniewski et al. (2020): at any _t_ , the time indices in Trt are smaller than those of Calt. Not randomizing aims at excluding future observations from Trt, which may lead to an under-estimation of the errors on Calt, thus eventually to smaller intervals with under-coverage. We compare both splitting strategies on simulations in Section 5.D.4. OSSCP procedure is schematised in Figure 5.5(a). 

**Original EnbPI.** EnbPI, Ensemble Prediction Interval (Xu and Xie, 2021), works by updating the list of _conformity scores_ with the most recent ones so that the intervals adapt to latest performances, without refitting the underlying regression model. Thereby, the predicted intervals can adapt to seasonality and trend. In EnbPI, _B_ bootstrap samples of the training set are generated and the regression algorithm is fitted on each bootstrap sample producing _B_ predictors. Finally, the predictors are aggregated in two ways: first, for each training point of index _t ≤ T_ 0, EnbPI aggregates only the subset of predictors trained on bootstrap sample _excluding_ ( _xt, yt_ ). This way, EnbPI constructs a set of hold-out calibration scores. Second, for test points of index _t > T_ 0 EnbPI aggregates all the _B_ predictors. A sketch of EnbPI is presented in Figure 5.5(b). Note that in Xu and Xie (2021) they use a classical bootstrap procedure, not dedicated to time series. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0095-07.png)


**----- Start of picture text -----**<br>
Unused data Proper training set Calibration set Test point<br>(a) OSSCP (b) EnbPI<br>**----- End of picture text -----**<br>


Figure 5.5: Scheme of the two baselines: OSSCP and EnbPI. In (a), Tr and Cal have equal size, but it can be changed. 

> 9Recall here that inductive CP and SCP are equivalent methods. 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

78 

They show empirically that it leads to _valid_ coverage on real world time series, such as hourly wind power production and solar irradiation, while offline SCP fails to attain _valid_ coverage. 

**EnbPI V2.** Xu and Xie (2021) used the mean aggregation during the training phase and the (1 _− α_ )-th quantile of the predictors for the prediction. We consider using the mean aggregation all along the procedure as mixing both aggregations may hurt the performance of the algorithm (as shown in the following simulations). Note that simultaneously to our work, authors released an updated version on ArXiv (Xu and Xie, 2021), incorporating a similar change. 

## **5.5.4 Experimental results: impact of** _ϕ, θ_ 

Figure 5.6 presents the results for data generated as in Section 5.5.1, for various ( _ϕ, θ_ ). Each sample contains 300 observations, with _T_ 0 = 200 and _T_ 1 = 100. We compare AgACI (with _K_ = 30 experts), ACI (with _γ ∈{_ 0 _._ 01 _,_ 0 _._ 05 _}_ ), OSSCP, EnbPI and EnbPI V2 (with mean aggregation). To assess the impact and interest of an online procedure, we also add offline SCP. Finally, to ensure the robustness of our conclusions each experiment is repeated _n_ = 500 times, and Figure 5.6 includes the standard errors (given by ~~_√_~~ _σ_ ˆ _nn_[,][where] _[σ]_[ˆ] _[n]_[is][the] empirical standard deviation). 

Each color is associated to a set ( _ϕ, θ_ ), each marker to an algorithm. To improve readability, we often link markers of the same method. There are thus two ways of analysing Figure 5.6: for a given method, the lines highlight the evolution of its performance with ( _ϕ, θ_ ); for a given data distribution, the set of markers of its color allows to compare the methods. Figure 5.6, and results on AR(1) in Section 5.D.2.1, highlight that in an AR(1) or ARMA(1,1) process: 

- Refitting the method (OSSCP vs Offline SCP) brings a significant improvement, that increases with higher dependence (higher values for _ϕ_ and _θ_ ). 

- All methods produce smaller intervals for _ϕ_ = _θ_ = 0 _._ 99. 

- EnbPI loses coverage while producing shorter intervals when the dependence increases. The performance of EnbPI depends significantly on the type and strength of dependence. 

- EnbPI V2 is closer to the target coverage than EnbPI. 

- OSSCP loses _validity_ & coverage as _ϕ_ and _θ_ increase. 

- While ACI with _γ_ = 0 _._ 01 also struggles for high values of _ϕ_ and _θ_ such as 0.99, we observe that it still attains _valid_ coverage with a well chosen _γ_ . Most importantly, ACI performances are robust to the increase of the dependence strength: except for the _ϕ_ = _θ_ = 0 _._ 99, its markers are really close to each other. 

- AgACI always nearly attains _validity_ (coverage is over 89 _._ 8% for all _ϕ_ ), and achieves the best _efficiency_ performance among _valid_ methods. 

Note that ACI’s _valid_ coverage with some _γ_ comes at the price of predicting more infinite intervals. A more detailed analysis on this phenomenon is conducted in Section 5.D.3. This can also be observed in graphs obtained with the average length after imputation, which are similar to Figure 5.6 and Section 5.D.2.1. In these graphs, the _validity_ remains unchanged as expected, but the _efficiency_ is more degraded for ACI with _γ_ = 0 _._ 05 and for AgACI, 

_5.6. Forecasting French electricity spot prices_ 

79 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0097-02.png)


**----- Start of picture text -----**<br>
OSSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021), γ = 0 . 01<br>O✏ine SSCP (ad. from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021), γ = 0 . 05<br>EnbPI (Xu & Xie, 2021) AgACI<br>EnbPI V2<br>14<br>13<br>12 0 . 895 0 . 900 0 . 905<br>'  =  ✓ =0.1<br>11 '  =  ✓ =0.8<br>'  =  ✓ =0.9<br>'  =  ✓ =0.95<br>'  =  ✓ =0.99<br>10<br>0 . 83 0 . 84 0 . 85 0 . 86 0 . 87 0 . 88 0 . 89 0 . 90 0 . 91<br>Coverage<br>length<br>median<br>Average<br>**----- End of picture text -----**<br>


Figure 5.6: Performance of various CP methods on data simulated according to equation (5.3) with a Gaussian ARMA(1,1) noise of asymptotic variance 10 (see Section 5.C.2). Results aggregated from 500 independent runs. Empirical standard errors displayed. 

since they produce more often uninformative intervals, as observed in Figure 5.4. 

   - **Summary.** We highlight the following takeaways: 

1. The temporal dependence impacts the _validity_ . 

2. Online is significantly better than offline. 

3. **OSSCP.** Achieves _valid_ coverage for _ϕ_ and _θ_ smaller than 0.9, but is not robust to the increasing dependence. 

4. **EnbPI.** Its _validity_ strongly depends on the data distribution (it is _valid_ on a MA(1) noise, not in AR(1) and ARMA(1,1) noise). When the method is _valid_ , it produces the smallest intervals. EnbPI V2 method should be preferred. 

5. **ACI.** Achieves _valid_ coverage for every simulation settings with a well chosen _γ_ , or for dependence such that _ϕ <_ 0 _._ 95. It is robust to the strength of the dependence. 

6. **AgACI.** Achieves _valid_ coverage for every simulation setting, with good _efficiency_ . 

## **5.6 Forecasting French electricity spot prices** 

In this last section, the task of forecasting French electricity spot prices with predictive intervals is considered in order to assess the methods on a real time series, and most importantly to show the relevance of ACI and AgACI in practice for time series without distribution shifts. 

## **5.6.1 Presentation of the price data** 

The data set contains the French electricity spot prices, set by an auction market, from 2016 to 2019. Each day _D_ before 12 AM, any producer (resp. supplier) submit their orders for the 24 hours of day _D_ + 1. An order consists of an electricity volume in MWh offered for sale (resp. required to be purchased) and a price in €/MWh, at which they accept to sell (resp. buy) this volume. At 12 AM, the algorithm “Euphemia” (EUPHEMIA) fixes 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

80 

the 24 hourly prices of day _D_ + 1 according to these offers and additional constraints. Thereby, it is an hourly data set, containing (3 _×_ 365 + 366) _×_ 24 = 35064 observations. Our aim is to predict at day _D_ (before 12 AM) the 24 prices of day _D_ + 1. Given the prices’ construction, we consider the following explanatory variables: day-ahead forecast consumption, day-of-the-week, 24 prices of the day _D −_ 1 and 24 prices of the day _D −_ 7. An extract of the considered data set is presented in Section 5.E.1. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0098-03.png)


**----- Start of picture text -----**<br>
800 Observed price<br>125 Predicted price<br>100 Predicted interval<br>600<br>75<br>400 50<br>21/01 23/01 25/01<br>200<br>0<br>2016 2017 2018 2019 2020<br>Date<br>/MWh)<br>€<br>(<br>price<br>Spot<br>**----- End of picture text -----**<br>


Figure 5.7: French electricity spot prices, from 2016 to 2019. Predicted intervals on the 25th of January 2019, using AgACI. 

These prices exhibits medium to high peaks, as illustrated in Figure 5.7 where the French prices had reached 800 €/MWh in fall 2016, compared to an average price of approximately 40 €/MWh in 2019. These extreme events are mainly due to the non-storability of electricity and the inelasticity of the demand: when the demand is high compared to the available production, production units with expensive production costs must be called, leading to a huge market price. 

## **5.6.2 Price prediction with predictive intervals in 2019** 

Since the 24 hours have very distinct patterns, we fit one model per hour, using again RF. We predict for the year 2019, using a sliding window of 3 years, as described in Figure 5.5(a), using one year and 6 months as proper training set and the most recent year and a half for calibration. The results are represented in Figure 5.8. 

**OSSCP** over-covers but to a lesser extent than the offline version. This can be explained by a low presence of peaks during the test period. Indeed, by updating the whole procedure, the high peaks are “forgotten" which leads to small intervals while it is not the case for the offline version which leads to too large intervals. Thereby, online versions can help to improve _efficiency_ , in addition to _validity_ . **EnbPI** attains a _valid_ coverage by over-covering. The under-coverage observed in the simulation study is not systematic, as in Xu and Xie (2021). **ACI** gives the smallest intervals with a correct coverage, for _γ_ = 0 _._ 01 and _γ_ = 0 _._ 05. The update of the quantile level enables to shrink the intervals. While the simulation in Section 5.5.4 study outlines that ACI improves _validity_ , this application illustrates that it can provide _efficient_ interval. **AgACI** is more _efficient_ than _γ_ = 0 while maintaining 

_5.7. Conclusion_ 

81 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0099-02.png)


**----- Start of picture text -----**<br>
26<br>OSSCP<br>Offline SSCP<br>EnbPI V2<br>24<br>ACI γ = 0<br>ACI γ = 0 . 01<br>22 ACI γ = 0 . 05<br>AgACI<br>0.9 0.91 0.92 0.93<br>Coverage<br>length<br>Median<br>**----- End of picture text -----**<br>


Figure 5.8: Performance of different CP methods on hourly spot electricity prices in France, trained from 2016 to 2018 and forecasted on 2019. Median length with respect to empirical coverage. 

_validity_ . Yet it slightly over-covers, and is slightly less _efficient_ than ACI with a well chosen _γ_ . 

An illustration of the predicted intervals is given in the inset graphic of Figure 5.7, for AgACI, to highlight the practical relevance of such an approach on the spot prices. 

However, as expected, these intervals only enjoy a _marginally_ valid frequency. They do not have _conditional_ guarantees. Especially, in this forecasting task, the predicted intervals cover the true prices around 88% of the time on week ends and Mondays, and 93% of the time on Tuesdays to Fridays (see Section 5.E.2). Further developments are needed to improve this unbalanced coverage. 

## **5.7 Conclusion** 

This article shows why and how ACI can be used for interval prediction in the context of time series with general dependencies. We prove that ACI deteriorates _efficiency_ compared to CP in the exchangeable case and analyse the dependency on _γ_ in the AR case with the support of numerical simulations. We propose an algorithm, AgACI, based on online expert aggregation, that wraps around ACI to avoid the choice of _γ_ . We conduct extensive experiments on synthetic time series for various strengths and structures of time dependence, demonstrating ACI’s robustness and better performances than baselines, with well chosen _γ_ or using AgACI. Finally we perform a detailed application study on the high-stakes electricity price forecasting problem in the energy transition era. Future work includes theoretical study of the proposed aggregation algorithm, including whether it preserves the asymptotic _validity_ observed experimentally or to quantify its _efficiency_ with respect to the performances of each expert. 

## **Appendix to Adaptive Conformal Predictions for Time Series** 

The appendices are organized as follows. First, Section 5.A provides details about the Split Conformal Prediction procedure. Second, Section 5.B proves the results of Section 5.3 and conducts the numerical analysis of Section 5.3.2 in the case where the _efficiency_ is computed using the median length. Then, Section 5.C contains details on the experimental setup (brief description of BOA, hyper-parameters, settings, pseudo-codes of competing algorithms). Finally, Sections 5.D and 5.E contain complementary numerical results, respectively on synthetic data sets and on the French electricity spot prices data set. 

## **5.A Details on Split Conformal Prediction** 

In this section, we introduce and review the simplest theoretical properties of Split Conformal Prediction (SCP). More specifically, we present the whole algorithm, the theoretical guarantees and discuss the visualisation challenges arising when visualising a CP procedure. 

## **5.A.1 Split Conformal Prediction Algorithm** 

**Algorithm 10** Split Conformal Algorithm, with absolute value residuals scores 

**Input:** Regression algorithm _A_ , significance level _α_ , examples _z_ 1 _, . . . , zT_ with _zt_ = ( _xt, yt_ ). **Output:** Prediction interval _C_[ˆ] _α_ ( _x_ ) for any _x ∈_ R _[d]_ . 

1: Randomly split _{_ 1 _, . . . , T }_ into two disjoint sets Tr and Cal. 

ˆ 2: Fit a mean regression function: _µ_ ( _·_ ) _←A_ ( _{zt, t ∈_ Tr _}_ ) 

3: **for** _j ∈_ Cal **do** ˆ 4: Set _sj_ = _|yj − µ_ ( _xj_ ) _|_ , the _conformity scores_ 

- 5: **end for** 

- 6: Set _S_ Cal = _{sj, j ∈_ Cal _}_ 

- 7: Compute _Q_[�] 1 _−α_ SCP ( _S_ Cal), the 1 _− α_[SCP] -th empirical quantile of _S_ Cal, with 1 _− α_[SCP] := (1 _− α_ ) (1 + 1 _/_ #Cal). ˆ 

- 8: Set _C_[ˆ] _α_ ( _x_ ) = _µ_ ( _x_ ) _± Q_[�] 1 _−α_ SCP ( _S_ Cal) , for any _x ∈_ R _[d]_ . � � 

## **5.A.2 Illustration of the SCP procedure** 

Figure 5.9 provides a visualisation of the SCP procedure in a regression task. The conformity scores are taken to be the absolute value of the residuals. 

83 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

84 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0102-02.png)


**----- Start of picture text -----**<br>
2<br>▶ Create a proper training set, a cali-<br>Step 0<br>bration set, and keep your test set,<br>1<br>by randomly splitting your data set.<br>− 2<br>0 2 4<br>x<br>2<br>Step 0 On the proper training set:<br>2 ˆ<br>▶ Learn µ<br>− 2<br>0 2 4<br>x<br>On the calibration set:<br>2 ▶ Predict with µ ˆ<br>Step 0 ▶ Get the residualsˆ ε ˆ i and form the<br>3 scores si =  |εi|<br>− 2 1<br>▶ Compute the (1  − α )  ×  (1 + #Cal [)]<br>empirical quantile of the si , noted<br>0 2 x 4 Q 1 −α ˆ ( si )<br>2<br>On the test set:<br>Step 0 ˆ<br>▶ Predict with µ<br>4<br>− 2 ▶ Build C [ˆ] α ˆ( x ): [ˆ µ ( x )  ± Q 1 −α ˆ ( si )]<br>0 2 4<br>x<br>y<br>y<br>y<br>y<br>**----- End of picture text -----**<br>


Figure 5.9: Schematic illustration of the Split Conformal Prediction procedure. Special case of a regression task, where the conformity scores are the absolute value of the residuals, as it is standard. 

_5.A. Details on Split Conformal Prediction_ 

85 

## **5.A.3 Theoretical guarantees of Split Conformal Prediction** 

Conformal prediction relies on the assumption that the data is exchangeable. 

**Definition 5.A.1** (Exchangeability) **.** ( _Xt, Yt_ ) _[T] t_ =1[are][exchangeable][if][for][any][permutation] _σ_ of �1 _, T_ � we have: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0103-05.png)


where _L_ designates the joint distribution. 

Lei et al. (2018) proves the following Theorem 5.A.1 about SCP quasi-exact _validity_ . 

**Theorem 5.A.1.** _Suppose_ ( _Xt, Yt_ ) _[T] t_ =1[+1] _[are][exchangeable,][and][we][apply][algorithm][10][on]_ ( _Xt, Yt_ ) _[T] t_ =1 _[to][predict][an][interval][on][X][T]_[+1] _[,][C]_[ˆ] _[α]_[ (] _[X][T]_[+1][)] _[.][Then][we][have:]_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0103-09.png)


_If, in addition, the scores S_ Cal _have a continuous joint distribution, we also have an upper bound:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0103-11.png)


## **5.A.4 Examples of dependent scores when data noise is exchangeable** 

In this subsection, we provide two examples that highlight the importance of adapting CP to time series. In these examples, the scores are non exchangeable while the true noise of the data is exchangeable. 

**Example 5.A.1** (Endogenous and not perfectly estimated) **.** Assume _Xt_ = _Yt−_ 1 _∈_ R and that 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0103-15.png)


where _εt_ is a white noise. This corresponds to an order-1 Auto-Regressive (i.e. AR(1)). 

ˆ Assume that the fitted model is _f_[ˆ] _t_ ( _x_ ) = ˆ _ax_ , with _a ̸_ = _a_ . Then, for any _t_ , we have that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0103-18.png)


ˆ with _ξt_ = _εt − aεt−_ 1. 

The residual process (ˆ _εt_ ) _t≥_ 0 is an ARMA(1,1) (Auto-Regressive Moving-Average, see ˆ section 5.C.2) of parameters _ϕ_ = _a_ and _θ_ = _−a_ . 

Thus, we have generated dependent residuals (ARMA residuals) even though the underlying model only had white noise. 

**Example 5.A.2** (Exogenous and misspecified) **.** Assume _Xt ∈_ R[2] and that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0103-23.png)


_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

86 

with _εt ∼ N_ (0 _,_ 1), _X_ 2 _,t_ +1 = _ϕX_ 2 _,t_ + _ξt, ξt ∼ N_ (0 _,_ 1) and _X_ 1 _,t_ can be any random i.i.d. i.i.d. variable. 

Assume that we misspecify the model so that the fitted model is _f_[ˆ] _t_ ( _x_ ) = _ax_ 1 for any _t ≥_ 0. Then, for any _t ≥_ 0, we have that 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0104-04.png)


Thus, we have generated dependent residuals (Auto-Regressive residuals) even if the underlying model only had i.i.d. Gaussian noise. 

## **5.A.5 How should we visualise CP predicted intervals?** 

We propose to have a closer look at how are constructed the prediction of this method. In this aim, we introduce model 5.A.1. 

## **Model 5.A.1.** 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0104-09.png)


In this model 5.A.1, the explanatory variables are deterministic. A generation from this model is represented in Figure 5.10. The first subplot, Figure 5.10a, represents _xt_ across time. The second subplot, Figure 5.10b, represents the noise _εt_ across time. Finally, the last subplot, Figure 5.10c, represents the whole process _Yt_ across time. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0104-11.png)


**----- Start of picture text -----**<br>
15 1 15<br>0<br>10 10<br>− 1<br>5 5<br>0 500 1000 0 500 1000 0 500 1000<br>t t t<br>(a) ft ( xt ) (b) εt (c) yt<br> εt<br>) t ) + t<br>( fxt εt (  fxt<br>y  = t<br>**----- End of picture text -----**<br>


Figure 5.10: Representation of data simulated according to model 5.A.1. 

The aim is to predict intervals of coverage 0.9 for values of _Yt_ , at _t >_ 500, that is to say _T_ 0 = 500 here. For simplicity, we assume _f_[ˆ] _t_ = _ft_ at each time step _t_ and we do not represent the points used to obtain this perfect regression model. There are two ways of visualizing the predictions, that are represented in each row of Figure 5.11. If the focus of the analysis is on a specific application with the aim of analysing the whole prediction, it is relevant to represent the response _yt_ itself and the associated intervals. This is represented in the first row of Figure 5.11. Nevertheless, to better understand a CP method, it is relevant to represent the scores and the corresponding intervals, rescaled. This is represented in the second row of Figure 5.11 (even if the residuals are displayed and not their absolute value, i.e. the scores). 

_5.B. Proof of the results presented in Section 5.3 and additional numerical experiments_ 87 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0105-01.png)


**----- Start of picture text -----**<br>
15<br>10<br>5<br>0 200 400 500 550 600 650 700 750 800 850 900 950 1000<br>t t<br>1<br>0<br>− 1<br>0 200 400 500 550 600 650 700 750 800 850 900 950 1000<br>t t<br>yt<br>ˆ εt<br>**----- End of picture text -----**<br>


Figure 5.11: Visualisation of OSSCP on simulated data, from model model 5.A.1. 1000 data points are generated. The 500 first ones form the initial calibration set, displayed on the first subplot of each row. The 500 last ones are the ones the algorithm tries to predict. They are displayed on the right subplot of each row. Observed values are in black, predicted intervals bounds are displayed in orange 

To better understand the difference between the two visualizations, let’s look specifically at some observations. In the first line of the Figure 5.11, we can see that the intervals widen for _t ∈_ [801; 900], while struggling to include the observations. Nevertheless, it is difficult to understand the underlying phenomenon on such a plot. Indeed, the points seem very similar to those for _t ∈_ [660; 720]. What considerably influences the CP are the scores and not the observed values. Thus, in the second line, at times _t ∈_ [801; 900], we observe more clearly that the values go out of the previous range of values, being around 1.5 in absolute value. This explains why the intervals widen: the calibration set contains more and more high values, which increases the value of the quantile and, therefore, the length of the interval. To conclude, to analyse and assess the performances of CP procedures, we recommend representing the intervals around the _conformity scores_ (or the residuals, depending on the score function) rather than the observed values. This is because the scores are what truly determine the conformal behaviour. 

## **5.B Proof of the results presented in Section 5.3 and additional numerical experiments** 

## **5.B.1 Proof of Theorem 5.3.1** 

We recall here Theorem 5.3.1. 

**Theorem 5.3.1.** _Assume that: (i) α ∈_ Q _; (ii) the scores are exchangeable with quantile function Q; (iii) the quantile function is perfectly estimated at each time (as defined above); (iv) the quantile function Q is bounded and C_[4] ([0 _,_ 1]) _. Then, for all γ >_ 0 _,_ ( _αt_ ) _t>_ 0 _forms a Markov Chain, that admits a stationary distribution πγ, and_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0105-08.png)


_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

88 

_Moreover, as γ →_ 0 _,_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0106-03.png)


To prove Theorem 5.3.1, we rely on the following lemmas, that will be proved after the theorem. We denote _Bβ_ a Bernoulli random variable of parameter _β_ and _P_ ( _x_ ) designates the projection of _x_ onto [0 _,_ 1]. Finally, for _γ >_ 0, define the following Markov Chain: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0106-05.png)


We introduce ( _p, q_ ) _∈_ N _×_ N _[∗]_ , _p < q_ , s.t. _α_ = _[p] q_[,][and:] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0106-07.png)


**Lemma 5.B.1** (Finite state space) **.** _Assume that α ∈_ Q _. Then, for any γ >_ 0 _, the Markov Chain defined by α_ 1 _∈A and αt_ +1 = _αt_ + _γ_ � _α − BP_ ( _αt_ )� _, for t >_ 0 _has a finite state space A._ 

**Lemma 5.B.2** (Irreducibility) **.** _Assume that α ∈_ Q _. Then, for any γ >_ 0 _, the Markov Chain defined by Equation_ (5.4) _, for t >_ 0 _and α_ 1 _∈A, is irreducible._ 

Thereby we will prove that the chain admits a unique stationary distribution _πγ_ , we now compute the first four moments of the stationary distribution in Lemmas 5.B.3 to 5.B.6. The final proof relies on a Taylor expansion, that requires to control these four moments. 

**Lemma 5.B.3** (Expectation) **.** _Let γ >_ 0 _and consider again the Markov Chain defined in equation_ (5.4) _. We have:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0106-12.png)


**Lemma 5.B.4** (Second order moment) **.** _Let γ >_ 0 _and consider again the Markov Chain defined in equation_ (5.4) _. As γ →_ 0 _, we have:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0106-14.png)


**Lemma 5.B.5** (Third order moment) **.** _Let γ >_ 0 _and consider again the Markov Chain defined in equation_ (5.4) _. As γ →_ 0 _, we have:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0106-16.png)


**Lemma 5.B.6** (Fourth order moment) **.** _Let γ >_ 0 _and consider again the Markov Chain defined in equation_ (5.4) _. As γ →_ 0 _, we have:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0106-18.png)


_5.B. Proof of the results presented in Section 5.3 and additional numerical experiments_ 89 

The proofs of these Lemmas are postponed to Sections 5.B.2 and 5.B.3. Here, we first give the proof of the main theorem. 

_Proof of Theorem 5.3.1._ Let _γ >_ 0. For any _t >_ 0 we have, for the recursion introduced in Equation (5.2), that 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0107-03.png)


_d_ where _St_ is the conformity score at time _t_ . Noting that 1 _St>_ ˆ _Qt_ (1 _−P_ ( _αt_ )) = _B_ P( _St>_ ˆ _Qt_ (1 _−P_ ( _αt_ ))), we obtain: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0107-05.png)


where the second line results from assumption (ii) and (iii), and the last equation from assumption (iii) only. Consequently, by induction, the chain defined by Equation (5.2) and 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0107-07.png)


with _α_ 1 = _α_ , have the same distribution. 

Using assumption (i), Lemma 5.B.1 ensures that the state space _A_ of the Markov Chain defined in equation (5.6) is finite. Furthermore, Lemma 5.B.2 also ensures that the chain is irreducible. Therefore, the chain is irreducible on a finite state space, thus it admits a unique stationary distribution, noted _πγ_ and for any positive function _f_ such that � _f_ d _πγ < ∞_ , we have (Meyn and Tweedie, 2012, Theorem 17.1.7): 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0107-10.png)


Remark that _L_ ( _β_ ) = 2 _Q_ (1 _− P_ ( _β_ )) for any _β_ . Therefore, combined with previous result we get the first result of Theorem 5.3.1: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0107-12.png)


We now need to characterize E _α_ ˜ _∼πγ_ [ _L_ (˜ _α_ )] = 2E _α_ ˜ _∼πγ_ [ _Q_ (1 _− P_ (˜ _α_ ))] as _γ →_ 0. Assume ˜ ˜ that _Q ∈C_[4] ([0 _,_ 1]). Using Taylor series expansion, for any _α ∈A_ , there exists _β_ ( _α_ ) _∈_ [0 _,_ 1]: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0107-14.png)


To conclude, we take the expectation under _πγ_ of equation (5.7), which gives: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0107-16.png)


_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

90 

Injecting results of Lemmas 5.B.3 to 5.B.5 in equation (5.8), we obtain: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0108-03.png)


Finally, we can control the last term since _Q ∈C_[4] ([0 _,_ 1]) by assumption, thus there exists _M >_ 0 such that for any _x ∈_ [0 _,_ 1], _|Q[′′′′]_ (1 _− x_ ) _|< M_ . Hence, using Lemma 5.B.6 we obtain: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0108-05.png)


Finally, combining equations (5.9) and (5.10) to conclude the proof by obtaining: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0108-07.png)


This concludes the proof of Theorem 5.3.1. 

**Remark: is it possible to use only 3 moments?** The proof here relies on the control of the first four moments. It is not clear that the same result could be obtained using only a third order Taylor expansion, as we would then require a bound on E[ _|P_ ( _α_ ˜) _− α|_[3] ], which is _not_ guaranteed to be _O_ ( _γ_[3] _[/]_[2] ), contrary to E[( _P_ (˜ _α_ ) _− α_ )[3] ]. 

## **5.B.2 Proof of Lemmas 5.B.1 and 5.B.2** 

_Proof of Lemma 5.B.1._ Let _γ >_ 0 and denote _α_ = _[p] q_[with][0] _[ < p < q]_[and][(] _[p, q]_[)] _[ ∈]_[N][2][.][We] denote _E_ the state space of the Markov Chain defined by equation (5.6), starting from _a ∈A_ . We show that _E_ = _A_ . 

First, ( _αt_ ) is stritcly bounded by _γ_ ( _α −_ 1) and 1+ _γα_ . Thus _E ⊂_ ] _γ_ ( _α −_ 1) _, γα_ [. Secondly, for any starting point _α_ 1 _∈A_ , we can observe that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0108-13.png)


where gcd( _a, b_ ) is the greatest common divisor of _a_ and _b_ . We have used at the last line that _α_ 1 _∈A_ writes as _α_ + _[γ] q_[gcd][(] _[q][ −][p, p]_[)] _[k]_[,][for][some] _[k][∈]_[Z][.][Combining][both][results,][we][get] that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0108-15.png)


_5.B. Proof of the results presented in Section 5.3 and additional numerical experiments_ 91 

This shows that the state space is finite and a subset of _A_ . The reciprocal implication is proved in the following Lemma, together with irreducibility. 

_Proof of Lemma 5.B.2._ Our objective is to show that there is a path of positive probability going from any point of the state space _A_ to any point of the same state space _A_ . Note that the chain always has at most two options when on a state _x_ : make a step _γα_ , with probability 1 _− P_ ( _x_ ), or a step _γ_ ( _α −_ 1), with probability _P_ ( _x_ ). 

Let ( _x, y_ ) _∈A_[2] . Thereby, there exist ( _k, n_ ) _,_ ( _l, m_ ) _∈_ N[2] such that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0109-04.png)


Thus, starting from _x_ , to attain _y_ , the chain has to make the path _y − x_ = ( _l − k_ ) _γα_ + ( _m − n_ ) _γ_ ( _α −_ 1). 

Noting that for any _h ∈_ N we have _γα_ ( _q − p_ ) _h_ + _γ_ ( _α −_ 1) _hp_ = 0, we can equivalently write that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0109-07.png)


with ( _u, v_ ) _∈_ N[2] _\ {_ (0 _,_ 0) _}_ . 

Thus, for any ( _x, y_ ) _∈A_[2] there exists ( _u, v_ ) _∈_ N[2] _\ {_ (0 _,_ 0) _}_ such that _y − x_ = _uγα_ + _vγ_ ( _α −_ 1). 

Let’s show by induction on _u_ + _v_ that for any ( _u, v_ ) _∈_ N[2] , and ( _x, y_ ) _∈A_[2] satisfying Equation (5.12) there exists a path of strictly positive probability between _x_ and _y_ . 

**Initialization.** Suppose first that _u_ + _v_ = 1. Then, there are two options: _u_ = 1 and _v_ = 0 or the reverse. Assume the former: Equation (5.12) gives _y_ = _x_ + _γα_ and necessarily _x <_ 1 since _y <_ 1 + _γα_ because _y ∈A_ . Thereby the step _γα_ has a probability 1 _− P_ ( _x_ ) _>_ 0 to occur. Thus the chain can attain _y_ starting from _x_ , i.e., P( _α_ 2 = _y|α_ 1 = _x_ ) _>_ 0. The second case works similarly, by observing that necessarily _x >_ 0. 

**Heredity.** Let _m ∈_ N. We assume that for any ( _u, v_ ) _∈_ N[2] such that _u_ + _v_ = _m_ , and ( _x, y_ ) _∈A_[2] satisfying Equation (5.12) there exists a path of strictly positive probability between _x_ and _y_ , or formally there exists _t ∈_ N such that P( _αt_ = _y|α_ 1 = _x_ ) _>_ 0. 

Suppose now that _u_ + _v_ = _m_ + 1 with _m ∈_ N _[∗]_ . If _v_ = 0, then _y_ = _x_ + _uγα_ and similarly than for _v_ = 0 and _u_ = 1, the step _γα_ is probable. Let _z_ = _x_ + _γα_ . We have: 

• P( _α_ 2 = _z|α_ 1 = _x_ ) = 1 _− P_ ( _x_ ) _>_ 0. 

- By our induction hypothesis, ( _y, z_ ) satisfy Eq. 5.12 with _u_ + _v_ = _m_ , thus there exists 

- _t_ such that P( _αt_ = _y|α_ 2 = _y_ ) _>_ 0. 

Overall, P( _αt_ = _y|α_ 1 = _x_ ) _>_ 0. 

If instead _u_ = 0, then _y_ = _x_ + _vγ_ ( _α −_ 1) and as for _u_ = 0 and _v_ = 1, the step _γα_ is of strictly positive probability and we conclude similarly. 

Finally, if both _u_ and _v_ are non-null, then we can make the step _γ_ ( _α −_ 1) if _x >_ 0 and the step _γα_ otherwise, before using our induction hypothesis. 

This shows that we can build a path of strictly positive probability for any ( _x, y_ ) _∈A_[2] , and thereby that the chain is irreducible. 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

92 

## **5.B.3 Control of the four moments: Lemmas 5.B.3 to 5.B.6** 

In the following Lemmas, to compute the first order moments of _πγ_ , we consider the chain _αt_ +1 = _αt_ + _γ_ � _α − BP_ ( _αt_ )� for _t >_ 0, launched from the stationary distribution _α_ 1 _∼ πγ_ . Thanks to the stationarity property, for all _t ≥_ 1, _αt ∼ πγ_ . 

_Proof of Lemma 5.B.3._ Let _γ >_ 0. To derive E _πγ_ [( _P_ ( _α_ 1) _− α_ )] we start by equation (5.6) with _t_ = 1: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0110-05.png)


_Proof of Lemma 5.B.4._ Let _γ >_ 0. To derive E _πγ_ �( _P_ ( _α_ 1) _− α_ )[2][�] we start by equation (5.6) with _t_ = 1: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0110-07.png)


Consequently, 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0110-09.png)


We can compute E _πγ_ [ _P_ ( _α_ 1)(1 _− P_ ( _α_ 1))]: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0110-11.png)


_5.B. Proof of the results presented in Section 5.3 and additional numerical experiments_ 93 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0111-01.png)


Reinjecting equation (5.14) in equation (5.13): 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0111-03.png)


We are now going to derive an upper and lower bound of E _πγ_ �( _P_ ( _α_ 1) _− α_ )[2][�] . Note that sign( _α − P_ ( _α_ 1)) = _−_ sign( _α_ 1 _− P_ ( _α_ 1)), thus E _πγ_ [( _α − P_ ( _α_ 1))( _α_ 1 _− P_ ( _α_ 1))] _≤_ 0. Hence we obtain the following upper bound: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0111-05.png)


Furthermore, using again this observation, and additionally that _|α − P_ ( _α_ 1) _|≤_ 1 and _|α_ 1 _− P_ ( _α_ 1) _|≤ γ_ and from equation (5.15), we can obtain: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0111-07.png)


where the second inequality holds by observing that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0111-09.png)


with _Cα_ = min( _α_[2] _,_ (1 _− α_ )[2] ). 

Gathering equations (5.16) and (5.17), we obtain: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0111-12.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0111-13.png)


_Proof of Lemma 5.B.5._ Let _γ >_ 0. We start again by using equation (5.6) and removing the first terms as E _πγ_ �( _α_ 2 _− α_ )[3][�] = E _πγ_ �( _α_ 1 _− α_ )[3][�] . Then we will isolate E _πγ_ �( _P_ ( _α_ 1) _− α_ )[3][�] and finally we will dominate each term obtained. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0111-15.png)


_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

94 

Hence, 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0112-03.png)


To conclude, we can bound each term of the right hand side of equation (5.19). In order of appearance we obtain: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0112-05.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0112-06.png)


where the last equality is obtained by using Lemma 5.B.4. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0112-08.png)


again using Lemma 5.B.4, and with _Dγ,α_ = max(1 + _γα, γ_ (1 _− α_ )) _− α_ = _O_ (1). 

_5.B. Proof of the results presented in Section 5.3 and additional numerical experiments_ 95 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0113-01.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0113-02.png)


where the last inequality comes from Lemma 5.B.4 a third time. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0113-04.png)


Gathering equations (5.20) to (5.24) together with equation (5.19), we obtain the following upper bound: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0113-06.png)


which leads to: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0113-08.png)


_Proof of Lemma 5.B.6._ Let _γ >_ 0. For the fourth order moment, the proof works in the same way for the third order moment, Lemma 5.B.5. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0113-10.png)


_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

96 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0114-02.png)


We are now going to dominate each term of the right hand side of equation (5.26) in order of appearance. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0114-04.png)


where the last inequality holds using Lemma 5.B.5. 

_5.B. Proof of the results presented in Section 5.3 and additional numerical experiments_ 97 

again where we’ve used Lemma 5.B.5, and re-used its notation 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0115-02.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0115-03.png)


Hence we have 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0115-05.png)


Again where we’ve used Lemma 5.B.5. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0115-07.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0115-08.png)


Gathering equations (5.27) to (5.33) together with equation (5.26), we obtain finally: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0115-10.png)


## **5.B.4 Proof of Theorem 5.3.2** 

In this section, we prove Theorem 5.3.2. Recall the theorem: 

**Theorem 5.3.2.** _Assume that: (i) α ∈_ Q _; (ii) the residuals follow an AR(1) process (i.e., εt_ +1 = _ϕεt_ + _ξt_ +1 _with_ ( _ξt_ ) _t i.i.d. random variables admitting a continuous density with respect to Lebesgue measure, of support S) clipped at a large value R, and_ [ _−R, R_ ] _⊂S; (iii) the quantile function Q of the stationary distribution of_ ( _εt_ ) _t is known. Then_ ( _αt, εt−_ 1) _is a homogeneous Markov Chain in_ R[2] _that admits a unique stationary distribution πγ,ϕ. Moreover,_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0115-14.png)


_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

98 

We consider _Zt_ = ( _αt, εt−_ 1) defined in the state-space _Z_ = _A ×_ [ _−R, R_ ] by 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0116-03.png)


That is, ( _αt_ ) _t≥_ 0 is the recurrence defined by Equation (5.2), and ( _εt_ ) _t≥_ 0 is an AR(1) process with parameters _ϕ_ clipped at some large value _R_ . Finally, ( _ξt_ ) _t_ is a sequence of i.i.d. r.v. admitting a continuous density with respect to the Lebesgue measure, of support _S ⊃_ [ _−R, R_ ]. 

This chain is defined for parameters _α, R_ considered as fixed, and we focus on the influence of _γ, ϕ_ . The main difference w.r.t. the previous section is that the state space is not countable anymore. More precisely, the state space is a product of a finite discrete set and an interval of R. 

The state-space _Z_ is _A ×_ [ _−R, R_ ], where _A_ is defined in the previous Section 5.B.1, equation (5.5). We equip _Z_ with the _σ_ -algebra _F_ = _P_ ( _A_ ) _× B_ (R), where _P_ ( _A_ ) is the power-set of the finite set _A_ and _B_ (R) is the borel set of R. 

**Lemma 5.B.7.** _The sequence_ ( _Zt_ ) _t≥_ 0 _is a Markov chain. Moreover, the chain is Harrisrecurrent, and admits a stationary distribution πγ,ϕ._ 

_Proof._ We observe that 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0116-09.png)


For a function _Fγ,ϕ_ : R[2] _×_ R. Consequently, _Zt_ follows a _Non-Linear State Space_ model (Meyn and Tweedie, 2012, Section 2.2.2 and Chapter 7). We denote _Pγ,ϕ_ the probability kernel or Markov transition function, that is, for any _z_ = ( _a, e_ ) _∈Z_ , and _F ∈F_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0116-11.png)


Remark that relying on Equation (5.35), we have an explicit formula for _Pγ,ϕ_ . Defining the sequence of functions ( _Ft_ ) _t≥_ 1 such that 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0116-13.png)


where _z_ 0 and ( _ξi_ ) are arbitrary real numbers. By induction we have that for any initial condition _Z_ 0 = _z_ 0 _∈Z_ and any _t ∈_ N, 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0116-15.png)


which immediately implies that the _t_ -step transition function may be expressed as 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0116-17.png)


where _p_ is the distribution of _ξ_ . 

_5.B. Proof of the results presented in Section 5.3 and additional numerical experiments_ 99 

We first prove that the chain is _ψ_ -irreductible, for _ψ_ = _µ ⊗ λ_ Leb, with _µ_ the uniform probability measure on _A_ and _λ_ Leb the Lebesgue measure on [ _−R_ ; _R_ ].[10] 

For any _z_ 0 = ( _a_ 0 _, e_ 0) _∈Z_ and _F_ = _{a[′] } × O_ , with _O_ open set, such that _ψ_ ( _F_ ) _̸_ = 0 we have that, for some _t_ large enough 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0117-03.png)


Indeed, 

1. There exists a path ( _a_ 0 _, . . . , at_ = _a[′]_ ) in _A_ from _a_ 0 to _a[′]_ such that for all _s ∈ {_ 1 _, . . . , t −_ 1 _}_ , 0 _< as <_ 1; and _as_ +1 _− as ∈{γ_ ( _α −_ 1) _, γα}_ similarly to the proof of Lemma 5.B.2 since _α ∈_ Q. 

2. Let _Es_ +1 be the event such that we obtain _as_ +1 from _as_ . Technically, if 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0117-07.png)


- b. conversely, if _as_ +1 _− as_ = _γα_ , _Es_ +1 = _{ξs_ such that _|ϕεs−_ 1 + _ξs|≤ Q_ 1 _−as}_ . 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0117-09.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0117-10.png)


Indeed (for case a.): 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0117-12.png)


with _δ >_ 0 by the assumption (ii) (esp. the fact that the support _S_ of _ξs_ includes _−_ [ _R, R_ ]). 

The proof is similar for case b. 

Consequently, P( _Zt ∈ F |Z_ 0 = _z_ 0) _> δ[t] >_ 0. 

4. The argument extends to the case where _a[′] <_ (0 _,_ 1), relying on the fact that _ψ_ ( _F_ ) _>_ 0. Moreover, the argument can be extended to show that for any _a[′] , O_ , there exists _δ[′]_ such that for all _a_ 0 _, e_ 0, there exists _t ≤ Cα,γ_ (e.g., _Cα,γ_ = _αγ_ 2[)][such][that] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0117-17.png)


Which proves that the chain will visit infinitely many times any Borel set _F_ with probability 1, and is consequently Harris-recurrent (Meyn and Tweedie, 2012, Chapter 9). Using Theorem 10.0.1 in Meyn and Tweedie (2012), we conclude that the chain admits a unique stationary distribution _πγ,ϕ_ . 

Finally, applying (Theorem 17.1.7 Meyn and Tweedie, 2012) to the later result gives: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0117-20.png)


> 10Moreover _ψ_ is transformed to remove mass from the sets that cannot be reached by the chain ( _Zt_ ) _t_ , i.e., if _B_ is such that P( _Zt ∈ B_ ) = 0 for all _t_ . This only concerns extremely marginal points, possible only _α >_ 1 or _α_ = min _A_ , for which we assign a zero mass to _α × U_ for some _U_ . 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

100 

## **5.B.5 Numerical study of ACI efficiency with AR(1) residuals, with respect to the median length** 

We here reproduce the same experiment as in Section 5.3.2, but focus on the _efficiency_ as the median of the intervals’ lengths instead of the average (after imputation). Results are given in Figure 5.12. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0118-04.png)


**----- Start of picture text -----**<br>
ϕ  =0 ϕ  =0.85 ϕ  =0.98 ϕ  =0.997<br>ϕ  =0.6 ϕ  =0.95 ϕ  =0.99 ϕ  =0.999<br>3 . 5 0 . 20<br>3 . 0 0 . 15<br>2 . 5 0 . 10<br>2 . 0 0 . 05<br>1 . 5 0 . 00<br>0 . 00 0 . 05 0 . 10 0 . 15 0 . 20 0.0 0.6 0.85 0.95 0.980.99 0.997 0.999<br>γ ϕ<br>length +<br>Median γ<br>**----- End of picture text -----**<br>


Figure 5.12: Left: evolution of the median length depending on _γ_ for various _ϕ_ . Right: _γ_[+] minimizing the median length for each _ϕ_ . 

Observations are very similar to the average length case, especially regarding (i) the monotonicity of the median interval length w.r.t. _ϕ_ , (ii) the existence of a minimum _γϕ_[+] to the function _γ �→_ Medßfl _,_ ’[ff[˜] ] := argminm Eßfl _,_ ’[ _|_ ff[˜] _−_ m _|_ ] (iii) the non-monotonicity of _ϕ �→ γϕ_[+][.] 

## **5.C Experimental details.** 

## **5.C.1 Details on the BOA procedure** 

The Bernstein Online Aggregation (BOA) procedure (Wintenberger, 2017) is a type of aggregation rule Φ. The weights outputted by BOA have an exponential form. In the exponent is plugged the difference between the loss suffered by the last aggregated forecast and the current squared loss suffered by the expert, instead of plugging the losses suffered by the experts (this would be Exponential Weighted Aggregation, Vovk, 1990). As stated in Wintenberger (2017), “this procedure favors online learners that predicted accurately and which past predictions losses are close to the loss of the last aggregative online learner, ensuring the stability in time and a small quadratic variation”. For more details, we refer the reader to the original paper Wintenberger (2017). 

## **5.C.2 Details ARMA(1,1) processes** 

**Definition 5.C.1** (ARMA(1,1) process) **.** We say that _εt_ is an ARMA(1,1) process if for any _t_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0118-12.png)


with: 

_5.C. Experimental details._ 

101 

- _θ_ + _ϕ ̸_ = 0, _|ϕ|<_ 1 and _|θ|<_ 1; 

- _ξt_ is a white noise of variance _σ_[2] , called the _innovation_ . 

The asymptotic variance of this process is: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0119-05.png)


An ARMA(1,1) is thus characterised by three parameters: the coefficients _ϕ_ and _θ_ and the innovation’s variance _σ_[2] . The larger the coefficients, in absolute value, the greater the time dependence and variance. Note that when _ϕ_ = 0, the ARMA(0,1) process corresponds to a MA(1) and when _θ_ = 0, the ARMA(1,0) process corresponds to an AR(1). 

To fix the asymptotic variance of an ARMA(1,1) of parameters _ϕ_ and _θ_ to _v_ , we fix _σ_[2] = _v_ 1 _−_ 12 _−ϕθϕ_ +[2] _θ_[2][.] 

## **5.C.3 Random forest parameters** 

All the random forests model have the same parameters, that are the following: 

- Number of trees: 1000 

- Minimum sample per leaf: 1 (default) 

- Maximum number of features: _d_ (default) 

Furthermore, for EnbPI, as there is already an individual bootstrap in the algorithm, the random forest regressors do not bootstrap them again. 

## **5.C.4 Details about the baselines and comparison** 

## 5.C.4.1 EnbPI full algorithm 

In order to be self-contained and precise the modifications done in EnbPI V2, the EnbPI algorithm from Xu and Xie (2021) is recalled in the following. In purple we precise the difference in EnbPI V2. 

**Remark on the bootstrap approach.** The bootstrap scheme is not adapted to time series, even if such strategies have been developed (Härdle et al., 2003; Kreiss and Paparoditis, 2012; Cai and Davies, 2012), and could be used to improve the adequation of EnbPI with the time series framework. Furthermore, recent works have proposed modifications of RF in the dependent setting (Goehry, 2020; Goehry et al., 2021; Saha et al., 2021). Generalizing these improvements to any ensemble method and use it for EnbPI could also enhance its performance, but is out of the scope of this paper. 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

102 

**Algorithm 11** Sequential Distribution-free Ensemble Batch Prediction Intervals (EnbPI) 

**Input:** Training data _{_ ( _xi, yi_ ) _}[T] i_ =1[,][regression][algorithm] _[A]_[,][decision][threshold] _[α]_[,][aggre-] gation function _ϕ_ , number of bootstrap models _B_ , the batch size _s_ , and test data _{_ ( _xt, yt_ ) _}t[T]_ =[+] _T[T]_ +1[1][,][with] _[y][t]_[revealed][only][after][the][batch][of] _[s]_[prediction][intervals][with] _[t]_[in] the batch are constructed. **Output:** Ensemble prediction intervals _{Cα_ ( _xt_ ) _}[T] t_ =[+] _T[T]_ +1[1] 1: **for** _b_ = 1 _, . . . , B_ **do** 2: Sample with replacement an index set _Sb_ = ( _i_ 1 _, . . . , iT_ ) from indices (1 _, . . . , T_ ) 3: Compute _f_[ˆ] _[b]_ = _A_ ( _{_ ( _xi, yi_ ) _| i ∈ Sb}_ ) 4: **end for** 5: Initialise _ε_ = _{}_ 6: **for** _i_ = 1 _, . . . , T_ **do** ˆ ˆ 7: _f−[ϕ] i_[(] _[x][i]_[) =] _[ ϕ] f[b]_ ( _xi_ ) _| i ∈/ Sb_ �� �� 8: Compute _ε_ ˆ _[ϕ] i_[=] _yi − f_ ˆ _−ϕi_[(] _[x][i]_[)] ��� ��� ˆ 9: _ε_ = _ε ∪{ε[ϕ] i[}]_ 10: **end for** 11: **for** _t_ = _T_ + 1 _, . . . , T_ + _T_ 1 **do** ˆ _T_ 12: Let _f_[ˆ] _−[ϕ] t_[(] _[x][t]_[)][=][(1] _[ −][α]_[)][quantile][of] _f−[ϕ] i_[(] _[x][t]_[)] **[V2:]**[this][is][replaced][by] � � _i_ =1 **[EnbPI]** ˆ ˆ _T f−[ϕ] t_[(] _[x][t]_[) =] _[ ϕ] f−[ϕ] i_[(] _[x][t]_[)] . �� � _i_ =1� 13: Let _wt[ϕ]_[= (1] _[ −][α]_[)][quantile][of] _[ε]_ ˆ 14: Return _CT,t[ϕ,α]_[(] _[x][t]_[) =] � _f−[ϕ] t_[(] _[x][t]_[)] _[ ±][ w] t[ϕ]_ � 15: **if** _t − T_ = 0 mod _s_ **then** 16: **for** _j_ = _t −_ 1 _, . . . , t −_ 1 **do** 17: Compute _ε_ ˆ _[ϕ] j_[=] ��� _yj − f_ ˆ _−ϕj_[(] _[x][t]_[)] ��� 18: _**ε**_ = ( _**ε** −{ε_ ˆ _[ϕ]_ 1 _[}]_[)] _[ ∪{][ε]_[ˆ] _[ϕ] i[}]_[and][reset][index][of] _**[ε]**_ 19: **end for** 20: **end if** 

- 21: **end for** 

## 5.C.4.2 Details on the implementation 

We conclude this section by summarizing computational aspects of the methods. One of the contributions is to provide a unified experimental framework. Therefore, in Table 5.1, we display the current available code for these methods, and what is available in the proposed repository. 

Table 5.1: Summary of available code online for each method and the proposed code in the repository. The programming language is specified, and, when relevant, the nature of the code. 

|Methods|Currently available<br>Language<br>Details|Contribution|
|---|---|---|
|||Language<br>Options|
|CP<br>OSCP<br>EnbPI<br>ACI|R<br>not available<br>Python<br>R script<br>no general function|Python<br>Python<br>randomised split<br>Python<br>same aggregation function<br>Python<br>randomised split|



_5.D. Additional experiments on synthetic data sets_ 

103 

## **5.D Additional experiments on synthetic data sets** 

In this section, we provide supplemental results on the synthetic data sets presented in Section 5.5.1. 

First, in Section 5.D.1 the sensitivity analysis of ACI _γ_ as well as the comparison to the naive strategy and AgACI is extended to AR(1) and MA(1) processes of asymptotic variance 10. 

Then, in Section 5.D.2, the comparison of all the CP methods for time series (initiated in Section 5.5.4) is also extended to these noises, that is AR(1) and MA(1) processes of asymptotic variance 10 (Section 5.D.2.1), and to ARMA(1,1), AR(1) and MA(1) processes of asymptotic variance 1 (Section 5.D.2.2). 

Next, we discuss in Section 5.5.4 that the improved _validity_ for _γ_ = 0 _._ 05 in comparison to _γ_ = 0 _._ 01 comes at the cost of more infinite intervals. This analysis is detailed in Section 5.D.3. 

Finally, we compare randomized and sequential split in Section 5.D.4. 

**Imputation.** The rationale to impute the infinite intervals is the following. We take the maximum of the absolute values of the residuals on the test set, noted _|ε|_ max. Then, for any _t ∈_ � _T_ 0 + 1 _, T_ 0 + _T_ 1�, if the predicted upper (resp. lower) bound[ˆ] _b_[(] _t[u]_[)] ( _xt_ ) is such that ˆ _bt_ ( _xt_ ) _> µ_ ˆ _t_ ( _xt_ ) + _|ε|_ max (resp. ˆ _bt_[(] _[ℓ]_[)][(] _[x][t]_[)] _[<][µ]_[ˆ] _[t]_[(] _[x][t]_[)] _[ −|][ε][|]_[max][)][we][impute][it][by] _[µ]_[ˆ] _[t]_[(] _[x][t]_[) +] _[ |][ε][|]_[max] (resp. _µ_ ˆ _t_ ( _xt_ ) _−|ε|_ max). 

## **5.D.1 Additional experimental results of ACI sensitivity to** _γ_ **, presented in Section 5.5.2** 

In this subsection, we provide similar results to those of Section 5.5.2, for different models on the noise. Especially, we consider AR(1) and MA(1) processes. 

**Observations.** The behaviour of the AR(1) process is very similar to the one of ARMA(1,1). On the other hand, for the MA case, the dependence structure is too weak to observe a significant effect of _γ_ . All ACI methods produce nearly valid intervals, with coverage above 89 _._ 25%. 

Results are given in Figures 5.13 and 5.14. 

## **5.D.2 Comparison to baselines, extension of Section 5.5.4** 

## 5.D.2.1 Asymptotic variance fixed to 10. 

Figure 5.15 displays the results on data generated according to Section 5.5.1, for an asymptotic variance of the noise of 10 (as in Figure 5.6), when this noise is an AR(1) or MA(1) process. 

**Observations.** As in the previous section, the methods’ performances are greatly impacted by the type and strength of dependence structure. Figure 5.15 shows that while ARMA(1,1) and AR(1) noises lead to similar patterns, it is not the case for an MA(1) noise. In the latter, _θ_ has little influence: the five performances (one for each _θ_ ) are similar within each method. In addition, offline sequential SCP is very close to OSSCP. This is expected 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

104 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0122-02.png)


**----- Start of picture text -----**<br>
ϕ  =0.1 , θ = 0 ϕ  =0.8 , θ = 0 ϕ  =0.9 , θ = 0 ϕ  =0.95 , θ = 0 ϕ  =0.99 , θ = 0<br>14<br>γ<br>0 . 0700<br>13 0 . 0400<br>0 . 0100<br>AgACI<br>12 Naive method 0 . 0070<br>0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 0040<br>16 0 . 0010<br>15 0 . 0007<br>0 . 0004<br>14<br>0 . 0001<br>13<br>0 . 0000<br>12<br>0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90 0 . 86 0 . 88 0 . 90<br>Coverage Coverage Coverage Coverage Coverage<br>length<br>median<br>Average<br>imputation<br>after<br>length,<br>Average<br>**----- End of picture text -----**<br>


Figure 5.13: ACI performance with various _θ_ , _ϕ_ and _γ_ on data simulated according to equation (5.3) with a Gaussian AR(1) noise of asymptotic variance 10 (see Section 5.C.2). Top row: average median length with respect to the coverage. Bottom row: percentage of infinite intervals. Stars correspond to the proposed online expert aggregation strategy, and empty triangles to the naive choice. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0122-04.png)


**----- Start of picture text -----**<br>
ϕ  = 0 , θ =0.1 ϕ  = 0 , θ =0.8 ϕ  = 0 , θ =0.9 ϕ  = 0 , θ =0.95 ϕ  = 0 , θ =0.99<br>AgACI<br>Naive method γ<br>13 . 8 0 . 0700<br>0 . 0400<br>13 . 6 0 . 0100<br>0 . 0070<br>0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 0040<br>0 . 0010<br>0 . 0007<br>15<br>0 . 0004<br>0 . 0001<br>14 0 . 0000<br>0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000 0 . 8925 0 . 8950 0 . 8975 0 . 9000<br>Coverage Coverage Coverage Coverage Coverage<br>length<br>median<br>Average<br>imputation<br>after<br>length,<br>Average<br>**----- End of picture text -----**<br>


Figure 5.14: ACI performance with various _θ_ , _ϕ_ and _γ_ on data simulated according to equation (5.3) with a Gaussian MA(1) noise of asymptotic variance 10 (see Section 5.C.2). Top row: average median length with respect to the coverage. Bottom row: percentage of infinite intervals. Stars correspond to the proposed online expert aggregation strategy, and empty triangles to the naive choice. 

as a MA(1) process has very short memory, and the temporal dependence is thus small even for _θ_ = 0 _._ 99. 

## 5.D.2.2 Asymptotic variance fixed to 1. 

We now fix the asymptotic variance of the noise to 1. The results are plotted in Figure 5.16. Note that this is an easier setting than previously, as the signal to noise ratio is higher for this asymptotic variance. 

**Observations.** Similarly to Figure 5.15, _θ_ has little influence when the noise is a MA(1). On AR(1) and ARMA(1,1) noises (left and middle subplots), the patterns are similar. First, we observe again the improvement thanks to the online mode (empty squares versus solid ones), which increases when the dependence increases. Second, all the methods achieve _validity_ or are significantly closer to achieving it than when the asymptotic variance is set to 10 (this is related to the high signal to noise ratio mentioned at the beginning of 

_5.D. Additional experiments on synthetic data sets_ 

105 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0123-02.png)


**----- Start of picture text -----**<br>
OSSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 01<br>Offline SSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 05<br>EnbPI (Xu & Xie, 2021) AgACI<br>EnbPI V2<br>AR(1) noise MA(1) noise<br>14<br>13 . 8 ϕ  =  θ =0.1<br>13 ϕ  =  θ =0.8<br>ϕ  =  θ =0.9<br>ϕ  =  θ =0.95<br>12 13 . 6 ϕ  =  θ =0.99<br>0 . 895 0 . 900 0 . 905<br>13 . 4<br>11<br>13 . 2<br>10<br>0 . 84 0 . 86 0 . 88 0 . 90 0 . 895 0 . 900 0 . 905<br>Coverage Coverage<br>length<br>median<br>Average<br>**----- End of picture text -----**<br>


Figure 5.15: Performance of various interval prediction methods on data simulated according to equation (5.3) with a Gaussian AR(1) (left) and MA(1) (right) noise of asymptotic variance 10 (see Section 5.C.2). Results aggregated from 500 independent runs. Empirical standard errors are displayed. 

this section). Third, EnbPI V2 is _valid_ for _ϕ_ = _θ ≤_ 0 _._ 95 and provides the most _efficient_ intervals for theses values. Nevertheless, its performances, as well as those of EnbPI, follow a clear trend (similar to that of Figure 5.6): when the dependence increases, the coverage decreases, as well as the length. EnbPI does not seem to be robust to the increasing temporal dependence in these experiments. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0123-05.png)


**----- Start of picture text -----**<br>
OSSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 01<br>Offline SSCP (adapted from Lei et al., 2018) ACI (Gibbs & Cand`es, 2021),  γ = 0 . 05<br>EnbPI (Xu & Xie, 2021) AgACI<br>EnbPI V2<br>ARMA(1,1) noise AR(1) noise MA(1) noise<br>9 . 0 9 . 0<br>8 . 8 ϕ  =  θ =0.1<br>ϕ  =  θ =0.8<br>8 . 5 8 . 5 8 . 6 ϕ  =  θ =0.9<br>ϕ  =  θ =0.95<br>ϕ  =  θ =0.99<br>8 . 4<br>8 . 0 8 . 0<br>8 . 2<br>8 . 0<br>7 . 5<br>0 . 89 0 . 90 0 . 91 0 . 89 0 . 90 0 . 91 0 . 895 0 . 900 0 . 905 0 . 910<br>Coverage Coverage Coverage<br>length<br>median<br>Average<br>**----- End of picture text -----**<br>


Figure 5.16: Performance of interval prediction methods on data simulated according to equation (5.3) with an ARMA(1,1) (left), AR(1) (center) and MA(1) (right) noise with 1 _−ϕ_[2] a _N_ (0 _,_ 1 1 _−_ 2 _ϕθ_ + _θ_[2][)] _[innovation]_[.][Results][aggregated][from][500][independent][runs.][Empirical] standard errors are displayed. 

## **5.D.3 Closer look at intervals** 

In this subsection, we investigate further the infite intervals generated by ACI for ARMA(1,1), AR(1) and MA(1) noise models. We report the results in Table 5.2. The central two columns present the percentage of infinite intervals, for _γ_ = 0 _._ 01 and _γ_ = 0 _._ 05. A first obvious observation is that the number of infinite intervals is orders of magnitude smaller for _γ_ = 0 _._ 01 than for _γ_ = 0 _._ 05. The last column represents the proportion of points for which _γ_ = 0 _._ 05 predicts R and that are _not_ covered for _γ_ = 0 _._ 01. This suggests that for those intervals, predicting an infinite interval was somehow justified in the sense that the point 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

106 

Table 5.2: Percentage of infinite intervals for ACI, on an ARMA(1,1) noise (first five rows), on an AR(1) noise ( _θ_ = 0, next five rows) and a MA(1) noise ( _ϕ_ = 0, last five rows). The central two columns present the percentage of infinite intervals, for _γ_ = 0 _._ 01 and _γ_ = 0 _._ 05. The last column represents the proportion of points for which _γ_ = 0 _._ 05 predicts R and that are _not_ covered for _γ_ = 0 _._ 01. 

|Noise parameters|_γ_ = 0_._01|_γ_ = 0_._05|Intersection|
|---|---|---|---|
|||||
|_ϕ_=_θ_ = 0_._1<br>_ϕ_=_θ_ = 0_._8<br>_ϕ_=_θ_ = 0_._9<br>_ϕ_=_θ_ = 0_._95<br>_ϕ_=_θ_ = 0_._99|0<br>0<br>0<br>0.03<br>0.04|1.12<br>2.76<br>3.72<br>4.45<br>6.22|53 out of 562<br>(9.43%)<br>263 out of 1381<br>(19.04%)<br>425 out of 1862<br>(22.83%)<br>514 out of 2224<br>(23.11%)<br>554 out of 3109<br>(17.82%)|
|_ϕ_= 0_._1<br>_ϕ_= 0_._8<br>_ϕ_= 0_._9<br>_ϕ_= 0_._95<br>_ϕ_= 0_._99|0<br>0<br>0<br>0.03<br>0.06|1<br>2.75<br>3.24<br>4.32<br>6.15|37 out of 500<br>(7.40%)<br>212 out of 1373<br>(15.44%)<br>359 out of 1622<br>(22.13%)<br>488 out of 2160<br>(22.59%)<br>560 out of 3073<br>(18.22%)|
|_θ_ = 0_._1<br>_θ_ = 0_._8<br>_θ_ = 0_._9<br>_θ_ = 0_._95<br>_θ_ = 0_._99|0<br>0<br>0<br>0<br>0|1.03<br>1.42<br>1.54<br>1.54<br>1.56|38 out of 516<br>(7.36%)<br>49 out of 710<br>(6.90%)<br>47 out of 772<br>(6.09%)<br>45 out of 770<br>(5.84%)<br>53 out of 781<br>(6.79%)|



was seemingly challenging to cover (as _γ_ = 0 _._ 01 failed to cover). For example, in the first line ( _ϕ_ = _θ_ = 0 _._ 1) we read that there are 562 points that result in infinite intervals for _γ_ = 0 _._ 05, among which 53 lead to finite predictions for _γ_ = 0 _._ 01 failing to cover on that point. This means only 9.43 % of 562 infinite intervals that can be considered as “somehow justified”. This analysis highlights that _γ_ = 0 _._ 05 seem to predict more infinite intervals than necessary, to compensate for easy errors as explained in Section 5.2. 

## **5.D.4 Randomised, sequential and other splits.** 

In Figure 5.17, we compare the sequential split strategy (dark markers) used in our experiments to the randomised version (clear markers), on online SCP. We observe that the intervals produced by the randomised version are significantly smaller than the sequential one, while covering slightly less. 

Another splitting strategy would consist in calibrating on the first points and training on the last ones. Up to our knowledge, this has not been used in practice. This way, we could hope to obtain a better model for the point prediction task. Nevertheless, we would be calibrating on really different data than the test ones. Thereby, the impact of this scheme regarding the interval prediction task performance is not straightforward. This is why we focus here on the sequential split, which is the most intuitive approach. Analysing further all of these effects theoretically or with extensive numerical experiments would be beneficial to the time series conformal prediction domain. 

## **5.E Forecasting French electricity spot prices** 

_5.E. Forecasting French electricity spot prices_ 

107 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0125-02.png)


**----- Start of picture text -----**<br>
Online Sequential SCP (OSSCP, adapted from Lei et al., 2018)<br>Online Randomised SCP (Online SCP, adapted from Lei et al., 2018)<br>ARMA(1,1) noise AR(1) noise MA(1) noise<br>13 . 825<br>14 14<br>13 . 800 ϕ  =  θ =0.1<br>13 13 13 . 775 ϕϕ  = =  θ θ =0.8=0.9<br>ϕ  =  θ =0.95<br>ϕ  =  θ =0.99<br>13 . 750<br>12 12<br>13 . 725<br>11 11 13 . 700<br>0 . 87 0 . 88 0 . 89 0 . 90 0 . 86 0 . 87 0 . 88 0 . 89 0 . 90 0 . 900 0 . 901 0 . 902 0 . 903 0 . 904<br>Coverage Coverage Coverage<br>length<br>median<br>Average<br>**----- End of picture text -----**<br>


Figure 5.17: Performance of interval prediction methods on data simulated according to equation (5.3) with a Gaussian ARMA(1,1) (left), AR(1) (middle) and MA(1) (right) noise of asymptotic variance 10 (see Section 5.C.2). Randomised methods are displayed. Results aggregated from 500 independent runs. Empirical standard errors are displayed. 

## **5.E.1 Details about the data set** 

Table 5.3 presents an extract of the French electricity spot prices data set used in Section 5.6. In this table, 2 _×_ 23 columns are hidden for clarity and space: the 24 prices of _D −_ 7 and the 24 prices of _D −_ 7 are used as variables. 

Table 5.3: Extract of the built data set, for French electricity spot price forecasting. 

|Date and time|Price<br>Price D-1<br>Price D-7<br>For. cons.<br>DOW|
|---|---|
|||
|11/01/16 0PM<br>11/01/16 1PM<br>...<br>12/01/16 0PM<br>12/01/16 1PM<br>...<br>18/01/16 0PM<br>18/01/16 1PM<br>...|21.95<br>15.58<br>13.78<br>58800<br>Monday<br>20.04<br>19.05<br>13.44<br>57600<br>Monday<br>...<br>...<br>...<br>...<br>...<br>21.51<br>21.95<br>25.03<br>61600<br>Tuesday<br>19.81<br>20.04<br>24.42<br>59800<br>Tuesday<br>...<br>...<br>...<br>...<br>...<br>38.14<br>37.86<br>21.95<br>70400<br>Monday<br>35.66<br>34.60<br>20.04<br>69500<br>Monday<br>...<br>...<br>...<br>...<br>...|



## **5.E.2 Forecasting year 2019** 

In Figure 5.18 we observe that on January 25, 2019, the forecasts are very different from the actual values. Nevertheless, the prediction intervals manage to include these observations for almost all hours (except after 5 pm) and almost all methods (EnbPI does not include points earlier, starting at 11 am). 

_Chapter 5. Adaptive Conformal Predictions for Time Series_ 

108 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0126-02.png)


**----- Start of picture text -----**<br>
150<br>Observed price Observed price<br>125 Predicted price 125 Predicted price<br>Predicted interval Predicted interval<br>100 100<br>75 75<br>50 50<br>(a) OSSCP (b) ACI with γ = 0 . 01<br>120 Observed price Observed price<br>125<br>Predicted price Predicted price<br>100 Predicted interval Predicted interval<br>100<br>80<br>75<br>60<br>50<br>(c) EnbPI V2 (d) ACI with γ = 0 . 05<br>2019-01-212019-01-222019-01-232019-01-242019-01-252019-01-26 2019-01-212019-01-222019-01-232019-01-242019-01-252019-01-26<br>2019-01-212019-01-222019-01-232019-01-242019-01-252019-01-26 2019-01-212019-01-222019-01-232019-01-242019-01-252019-01-26<br>/MWh) /MWh)<br>(€ (€<br>price price<br>Spot Spot<br>/MWh) /MWh)<br>(€ (€<br>price price<br>Spot Spot<br>**----- End of picture text -----**<br>


Figure 5.18: Representation of predicted intervals around point forecasts on the 25th of January of 2019. 

In Figure 5.19 we observe that the four algorithms suffer from an unbalanced coverage depending on the day-of-the-week (each algorithm in a different extent). That is, they cover more than 90% of the observations on Tuesdays to Fridays, but less than 90% on Mondays and week-ends (Saturdays and Sundays). 

_5.E. Forecasting French electricity spot prices_ 

109 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0127-02.png)


**----- Start of picture text -----**<br>
95 95<br>90 90<br>(a) OSSCP (b) ACI with γ = 0 . 01<br>95 95<br>90 90<br>(c) EnbPI V2 (d) ACI with γ = 0 . 05<br>95<br>90<br>(e) AgACI<br>MondayTuesdayWednesdayThursdayFridaySaturdaySunday MondayTuesdayWednesdayThursdayFridaySaturdaySunday<br>MondayTuesdayWednesdayThursdayFridaySaturdaySunday MondayTuesdayWednesdayThursdayFridaySaturdaySunday<br>MondayTuesdayWednesdayThursdayFridaySaturdaySunday<br>coverage coverage<br>Average Average<br>coverage coverage<br>Average Average<br>coverage<br>Average<br>**----- End of picture text -----**<br>


Figure 5.19: Coverage proportion during 2019 depending on the day-of-the-week. 

## **Chapter 6** 

## **Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and 2021** 

Electricity price forecasting (EPF) plays a major role for electricity companies as a fundamental entry for trading decisions or energy management operations. As electricity can not be stored, electricity prices are highly volatile which make EPF a particularly difficult task. This is all the more true when dramatic fortuitous events disrupt the markets. Trading and more generally energy management decisions require risk management tools which are based on probabilistic EPF (PEPF). In this challenging context, we argue in favor of the deployment of highly adaptive black-boxes strategies allowing to turn any forecasts into a robust adaptive predictive interval, such as conformal prediction and online aggregation, as a fundamental last layer of any operational pipeline. 

We propose to investigate a novel data set containing the French electricity spot prices during the turbulent 2020-2021 years, and build a new explanatory feature revealing high predictive power, namely the nuclear availability. Benchmarking state-of-the-art PEPF on this data set highlights the difficulty of choosing a given model, as they all behave very differently in practice, and none of them is reliable. However, we propose an adequate conformalisation, `OSSCP-horizon` , that improves the performances of PEPF methods, even in the most hazardous period of late 2021. Finally, we emphasize that combining it with online aggregation significantly outperforms any other approaches, and should be the preferred pipeline, as it provides trustworthy probabilistic forecasts. 

111 

_Chapter 6. Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and_ 112 _2021_ 

_2021_ 

||**Contents**|
|---|---|
||6.1<br>Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113<br>6.2<br>Data presentation and insightful new explanatory variables<br>. . . . . . . . . 115<br>6.2.1<br>Dataset’s description . . . . . . . . . . . . . . . . . . . . . . . . . . . 115<br>6.2.2<br>First point forecast and feature importance . . . . . . . . . . . . . . 116<br>6.3<br>Probabilistic forecasting methods . . . . . . . . . . . . . . . . . . . . . . . . 117<br>6.3.1<br>Framework<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118<br>6.3.2<br>Quantile regression methods . . . . . . . . . . . . . . . . . . . . . . . 118<br>6.3.3<br>Conformal methods: add-on to traditional probabilistic approaches . 120<br>6.4<br>Adaptiveness as a wrapper around individual forecasts . . . . . . . . . . . . 121<br>6.4.1<br>Online aggregation based strategies . . . . . . . . . . . . . . . . . . . 122<br>6.4.2<br>Adaptive conformal approaches . . . . . . . . . . . . . . . . . . . . . 122<br>6.5<br>Application and results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126<br>6.5.1<br>Setting and evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . 126<br>6.5.2<br>Results<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127<br>6.6<br>Conclusion and perspectives . . . . . . . . . . . . . . . . . . . . . . . . . . . 129<br>6.A Results on the CRPS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131|



_6.1. Introduction_ 

113 

## **6.1 Introduction** 

Electricity price forecasting (EPF) plays a major role for electricity companies as a fundamental entry for trading decisions or energy management operations. As electricity can not be stored, electricity prices are highly volatile which make EPF a particularly difficult task (Weron, 2014; Lago et al., 2021). 

The increase of renewable production in many countries (RTE, 2022; IEA, 2022a), the development of storage devices or more generally demand response programs (e.g., electrical vehicle smart charging (Nassar et al., 2022), electric water heater management (Amabile et al., 2021; Moreno et al., 2023)) simultaneously entails a need for good EPF and generates more complexity for price modelling. Furthermore, prices can be affected by fortuitous events such as Covid-19 pandemic in 2020-2021 (IEA, 2021), the stress corrosion issue which affected French nuclear power plants in 2022 or the crisis of the gas markets triggered by Russia’s invasion of Ukraine (IEA, 2022b). Trading and more generally energy management decisions require risk management tools which are based on probabilistic EPF (Bunn et al., 2016). This supports the advancement of adaptive probabilistic approaches for forecasting prices, which can continuously learn and adjust to the evolving behaviors of EP, resulting in accurate and reliable probabilistic forecasts. 

The literature on EPF is growing rapidly and most papers deals with point forecasts (Weron, 2014; Lago et al., 2021). We focus on short term (day-ahead) EPF as the mainstay of short-term power trading in Europe is the day-ahead market. As proposed in (Lago et al., 2021), models used for forecasting electricity prices can be categorized as either statistical, machine learning or hybrid models. 

**Statistical models** are dominated by auto-regressive models and their variants, in particular the state ot the art Lasso Estimated AutoRegressive (LEAR) model proposed by Uniejewski et al. (2016) and recently used as state of the art benchmark in (Lago et al., 2021; Tschora et al., 2022). It consists in a high dimensional ARX model where the fitting process is done by minimizing an elastic net regularization. The high dimension (arround 250 parameters) comes from a large number of lags of prices and forecasts of variable of interests (generation, zonal prices, consumption). As highlighted by Lago et al. (2021) pre-processing of EP such as log transformations or more generally variance stabilizing transformations (Uniejewski et al., 2018) are a common practice to deal with heavy tailed distribution. Regarding non-stationarity of the prices, regime switching ARX models are proposed in (Nitka et al., 2021). Marcjasz et al. (2018) propose to average a set of point forecasts obtained from learning with different time windows to derive probabilistic forecasts. 

The utilisation of **machine learning** tools including deep learning approaches for electricity price forecasting (EPF) has grown over the past decade. Recent studies (Tschora et al., 2022; Jędrzejewski et al., 2022) reveal that complex ML methods such as deep neural networks can achieve better forecasting performances than the LEAR model at the cost of significantly higher computational cost. The relatively important dimension of these models require a significant amount of data for their calibration, making them poor candidate to adapt to abrupt changes in price distribution (Çağatay Berke Bozlak and Yaşar, 2024). Yang et al. (2023) show how graphical neural network could be used to model spatial 

_Chapter 6. Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and_ 114 _2021_ 

_2021_ 

dependency to forecast the day-ahead electricity prices of the Nord Pool market. 

**Probabilistic price forecasting** is progressively becoming more popular in the forecasting literature following the GEFCom2014 energy forecasting competition (Hong et al., 2016). This is a natural goal as the final objective EPF is to optimize a financial risk criteria (Bjorgan et al., 1999; Deschatre et al., 2021). Most of the previous parametric statistical models are based on statistical assumptions and could be naturally extended to produce probabilistic forecast (more or less accurate as we will explore in this paper). Relaxing distributional assumption, non parametric regression models such as quantile regression have been investigated (Uniejewski and Weron, 2021). In Loizidis et al. (2024), machine learning models coupled with boostrap methods are compared with classical time series models for German and Finnish day-ahead market. Marcjasz et al. (2023) recently proposed a distributional network that outperforms state-of-the-art benchmarks. Nickelsen and Müller (2024) present a Bayesian forecasting framework for the German continuous intraday market and show that orthogonal matching pursuit methods can outperform LEAR. Cornell et al. (2024) propose quantile regression with varying training-length periods and model averaging to forecast prices of the South Australia region of the Australian National Electricity Market. 

PEPF models face many pitfalls: extreme price spikes, non-stationarity due to exogenous factors inducing time-varying mean and/or volatility. Conformal methods (Vovk et al., 1999; Papadopoulos et al., 2002; Vovk et al., 2005) and more specifically adaptive conformal methods, proposed for example by Gibbs and Candès (2021); Zaffran et al. (2022), are a way to adapt PEPF models in a very general way. It can be applied to any of the previously cited PEPFs to improve them. We propose to extend the work of Zaffran et al. (2022) to forecast electricity prices in France during the turbulent period 2020-2022. Another framework allowing to adapt PEPF models is online aggregation under expert advice (Cesa-Bianchi and Lugosi, 2006), which was successfully used in financial non-stationary environments (Remlinger et al., 2023; Berrisch and Ziel, 2024a). Our aim is to investigate if and how it is possible to make adaptive an existing probabilistic forecasting algorithm. This approach is driven by an operational concern: proposing a plug-in tool that can be applied to any underlying model eases its integration in the current pipeline. 

**Contributions** We list below our main contributions: 

- **New data** : we study the recent turbulent period 2020-2022 and we add a new feature, the nuclear availability 

- **Benchmark** : we consider state-of-the-art PEPF methods, their windowed versions (rolling window estimation) and benchmark them on this new dataset 

- **Analysis** of the improvements (or not) of existing **online conformal methods** 

- Suggestion of **novel online conformal strategy** coined `OSSCP-horizon` 

- Unified framework of **sequential aggregation** of all these probabilistic forecasting 

_6.2. Data presentation and insightful new explanatory variables_ 

115 

- **Understanding the benefits** of these 2 frameworks of probabilistic post-processing (i.e. CP and aggregation) and how they can help each other: _sequential aggregation with conformalized expert is the best_ 

## **6.2 Data presentation and insightful new explanatory variables** 

## **6.2.1 Dataset’s description** 

The considered dataset spans approximately 6 years of observations at a hourly frequency, from January 11th, 2016 to December 31st, 2021, and is decomposed of a training set (from January 11th, 2016 to December 31st, 2018) to estimate the parameters of the models, a validation test (year 2019) to estimate the hyperparameters, and a test set (years 2020 and 2021) to evaluate the performances (see Figure 6.1). We consider the task of forecasting day-ahead (DAH) prices on the French EPEX market. As the 24 hours of day _d_ are fixed from EUPHEMIA[1] ’s market clearing at 12:00pm of day _d −_ 1, the features considered to predict each of them are selected so that they are available before 12:00pm of day _d −_ 1. More precisely the dataset contains the following features, for a target at day _d_ , hour _h_ : 

- the 24 French DAH prices at days _d −_ 1 and _d −_ 7; 

Figure 6.1: Evolution of the Spot prices (first panel), Residual Load (second panel), Nuclear availability (third panel) and commodity prices (last panel) from 2016 to 2021 ( _x_ -axis). 

> 1EUPHEMIA is the algorithm that solves the market coupling problem for the Central West European region, used by EPEX to compute the day-head power prices 

_Chapter 6. Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and_ 

116 

_2021_ 

- the observed daily price of Gas on the French PEG market at _d −_ 1 and the monthahead futures prices for Oil (Brent) and Coal (CIF ARA Argus-McCloskey); 

- the forecasted residual load signal built with data available before 12pm at _d −_ 1: the load forecasts for the 24 hours of day _d_ , estimated on day _d −_ 2, minus the renewable production forecasts (i.e., wind and solar forecasts estimated on day _d −_ 2, and the observed run-of-river electricity on _d-2_ ); 

- the availability of French nuclear electricity on day _d_ , i.e. the announced available capacity of nuclear generation; 

- the observed electricity generation from all production types at _d −_ 2 and _d −_ 7 (in the case of nuclear energy, the production is divided by the nuclear availability); 

- the EUR vs. GBP and EUR vs. USD exchange rate (last observed at _d −_ 1); 

- the total electricity volume exchanges between France and all its neighbors (observed at _d −_ 2); 

- the specific electricity volume exchanges between France and Germany (observed at _d −_ 2); 

- dummy variables, including dummy variables for French holidays (as a percentage of the total population concerned), holiday bridges, weekends, and weekdays; 

- the time of year as a sine and cosine function, as well as a clock variable to capture a possible trend. 

## **6.2.2 First point forecast and feature importance** 

The proposed dataset comprises features classically used to forecast electricity prices, and also a new feature, the nuclear availability, for we intuit that nuclear availability has a significant impact on DAH prices due to the French energy mix. 

At first we proceed a point forecast exercise, with Lasso CV and Random forest models, to detect the most important features and highlight the relevance of the proposed new variables. Here, the meaning of the term “feature importance” varies according to the model: in the case of Lasso CV, it refers to the value of the coefficient associated to a given feature, whereas for Random Forest it refers to the Mean Decrease in Impurity (MDI). 

In Figure 6.2, we observe the top 20 mean feature importances over both models trained in 2020. Spot price at H-23 of the previous day is the “most important” feature for the Lasso CV model. This is coherent with what is found in (Maciejowska et al., 2022; Ziel and Weron, 2018). The MDI-based importances computed for the Random Forest suggests the same conclusion, even though high correlation between all _d-1_ spot prices makes the interpretation harder. The Lasso CV model, which allows for a better modelisation with highly correlated features, suggests that gas prices and nuclear availability have a high explanatory power. This speaks in favour of an inclusion of these features in EPF prediction models, at least in the case of the French market. 

_6.3. Probabilistic forecasting methods_ 

117 

Figure 6.2: Feature ( _y_ -axis) importance ( _x_ -axis) for Lasso CV (left panel) and Random Forest (right panel) models. The colors are associated with a type of feature. 

Figure 6.3: Evolution of normalized feature importance ( _y_ -axis) for Lasso CV (left panel) and Random Forest (right panel) models over the whole test period ( _x_ -axis). The colors are associated with the features. 

We also compute the feature importance of both model over every days in the test period and observe the evolution in the predominance of the various feature groups. To do so, we first aggregate features into groups: “Change” for all exchange rates, “Commodity price” for gas, coal and oil prices, “Exchange” for all hourly power volumes exchanges, and the rest of features groups are hourly features aggregated at a daily level. The group aggregation consists in summing up the absolute importance value of all features belonging to this group, then normalize these values by the total sum over all groups. Figure 6.3 represents the evolution we obtain. We observe a considerable change in the relative group’s explanatory power: for both the Random Forest and Lasso model, we observe a significant increase in the aggregated explanatory power of the commodity prices, at the expense of the residual load forecast. This indicates an important distribution shift in the relationships between the times series by September 2021. 

## **6.3 Probabilistic forecasting methods** 

**Notations** Given the nature of the data and in particular the hourly patterns, we will build one model per hour, as explained in Section 6.5.1. From now on, the temporal index _t_ is used and it elapses at a daily rate (i.e., for a given hour _h_ ). _t_ = 1 corresponds to the beginning of the training data, _t_ = _T_ 0 marks the end of the training data and _t_ = _T_ 1 refers to the last test observation to be predicted. In other words, we aim at predicting the French spot prices between _T_ 0 + 1 and _T_ 1, corresponding to the years 2020 and 2021 (see Figure 6.1). 

_Chapter 6. Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and_ 118 _2021_ 

_2021_ 

## **6.3.1 Framework** 

One objective of probabilistic forecast is to build _Prediction Intervals_ (PIs) for a variable _Yt_ depending on the covariates _Xt_ . Let _α ∈_ [0 _,_ 1] be a _miscoverage rate_ . A PI at the 1 _− α_ level is expected to contain at least 1 _− α_ of the realisations: P ( _Yt ∈_ PI1 _−α_ ( _Xt_ )) _≥_ 1 _− α_ , while being as small as possible. In order to retrieve as much information as possible about the distribution of _Yt_ , one can consider multiple values of the miscoverage rate _α_ . 

A PI can be characterized by two “point forecasts”: its lower ( _ℓ_ ( _X_ )) and upper ( _u_ ( _X_ )) bounds. A natural choice for the PI is _ℓ_ ( _X_ ) = _Qα/_ 2( _X_ ) and _u_ ( _X_ ) = _Q_ 1 _−α/_ 2( _X_ ), where _Qβ_ is the _β_ -th quantile of the cumulative function distribution (c.d.f.) of the price conditionally to the covariates used to forecast. 

However, in practice, these true _Q_ are never known and we have to estimate them, e.g., using quantile regression (Koenker, 2005). This approach is detailed in Section 6.3.2. 

Another path is to post-process individual predictors (see Section 6.3.3). The individual predictors can either estimate the mean as in point forecasting and the post-processing step will turn them into PI, or directly estimate a conditional quantile (as described in Section 6.3.2). 

## **6.3.2 Quantile regression methods** 

We present here the quantile regression methods that we retained for our benchmark study. These methods were chosen for their good performance on time series data, and in particular on electricity related data. They are all quite easy to fit automatically and have a relatively low computational cost (this is a key asset due to the intensive benchmark including rolling window estimation). 

## 6.3.2.1 Description of the methods 

**Basics on Quantile Regression (QR)** QR (Koenker, 2005) replaces the usual quadratic loss by the _pinball loss_ to forecast a conditional quantile of the distribution of _Y_ (i.e. the price) given the features _X_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0136-11.png)


ˆ ˆ ˆ ˆ for any _x_ , with _ρβ_ the _pinball loss_ of level _β_ : _ρβ_ ( _y−y_ ) = (1 _−β_ ) _|y−y|_ 1 _{y ≤ y}_ + _β|y−y|_ 1 _{y ≥ y_ ˆ _}_ , and _G_ the class of regressors considered, e.g. linear models, Lasso (QLR-Lasso), additive non-linear models (QGAM) or gradient boosting regressors (QGB). 

**Quantile Linear Regression (Linear QR) and Quantile Lasso (Lasso QR)** The class of regressors _G_ is restricted to linear models. For Lasso QR, We perform a Lasso selection process (Tibshirani, 1996) to deal with the pretty high number of covariates, the class of regressors is thus the linear models on all possible subsets of covariates. 

**Quantile Generalized Additive Models (QGAM)** Generalized Additive Models (GAMs) (Hastie and Tibshirani, 1986) consists in explaining the conditional expectation 

_6.3. Probabilistic forecasting methods_ 

119 

_µ_ ( _X_ ) of _Y_ over _X_ with a semi-parametric additive structure. The estimation of GAMs is based on a (regularized) mean squared error (MSE) criterion. Our objective is to use GAMs for a QR problem. One could replace the MSE by the pinball loss function in the estimation process as described in the previous paragraph. However, Fasiolo et al. (2020) demonstrate that the pinball loss is statistically sub-optimal in this framework and proposes a procedures based on the smooth Extended Log-F loss instead. 

**Quantile Random Forests (QRF)** Meinshausen (2006) adapts Random Forests to the QR task. The same forest is built than for mean-regression, that is a forest grown in order to minimize the mean squared error. However, to adapt to the quantile task at hand, the final decision rule for prediction now corresponds to evaluating an empirical conditional quantile (conditional on the fact that the features of the test point belongs to the corresponding leaves). 

**Quantile (tree based) Gradient Boosting (QGB)** Gradient boosting machine (Friedman, 2001) are widely used in the forecasting community where it has demonstrated excellent performance for different applications on tabular data (Grinsztajn et al., 2022) or time series (Makridakis et al., 2022). As for the Random Forests, the regressors are here regression trees. The boosting algorithm consists in adding a sequence of simple models (called weak learners and trained on a subsample randomly selected of the training set) obtained by sequentially fitting a quantile regression tree to the residuals by minimizing the pinball loss, which is a key difference with QRF. 

## 6.3.2.2 Operational pipeline 

We explore these prediction methods through their implementation in the Python package `scikit-learn` package (Pedregosa et al., 2011) for linear quantile regression, Lasso and QGB. QRF are implemented through `scikit-garden` . The QGAM are implemented in the `R` package (Fasiolo et al., 2021). 

All of these models depend on hyper-parameters, and QGAM additionally requires an exact formula. In particular, we optimized for the regularizer (Lasso), the number of trees and their maximum depth (QRF and QGB), as well as the learning rate and fraction of samples (QGB), and the formula (QGAM). Their estimation is based on grid-searching on the validation set after estimation of mean-regression models on the training set, as illustrated in Figure 6.1. Therefore, the formula of the QGAM is the same for all quantiles. It includes: 

- _linear effects_ : for the indicator of the week days; 

- _univariate non-linear terms_ : the announced French nuclear availability, the lagged 2 days of the fossil hard coal and observed nuclear productions, the square root of the lagged one day of the Gaz prices, cosin and sin of the time of year; 

- _functional smooth effects:_ as proposed in Amara-Ouali et al. (2023) in the context of electricity load forecasting, we model the lagged (one day and one week) prices and 

_Chapter 6. Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and_ 120 _2021_ 

the load forecast effects via a functional smooth effect. It allows to capture the effect of these functional (in function of time) covariates over the price at a given instant of the day. 

In this paper we do not consider online re-estimation of the hyperparameters, which in practice is very time consuming and statistically challenging. We study the performance of operational fixed prediction models that can be made adaptive through a plugged-in layer, useful when facing non-stationarity without completely retraining them. 

Also, as illustrated in the preliminary results of Figure 6.4, before September 2021, only QRF and QGAM achieved _validity_ . We explore strategies to recover validity in Section 6.3.3. What is more, none of the probabilistic methods attain the target coverage level after September 2021. Indeed, the high explosion of the prices after this date, both in average and in variability, calls for more adaptive strategies, that we discuss in Section 6.4. Note that the standard rolling training procedure did adapt to this change as illustrated by the lengths of the PIs after September 2021, but more adaptiveness is required given the strength of the shift and variability. 

## **6.3.3 Conformal methods: add-on to traditional probabilistic approaches** 

Conformal Prediction (CP) (Vovk et al., 1999; Papadopoulos et al., 2002; Vovk et al., 2005) builds PI around any kind of prediction models. These intervals are valid (achieving marginal nominal coverage) in finite samples under the only assumption of exchangeability of the data. Therefore, CP has to be seen as an add-on protective layer to existing probabilistic 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0138-06.png)


**----- Start of picture text -----**<br>
QRF QGB Linear QR Lasso QR QGAM<br>Before 2021-09-01<br>1 . 0<br>y =  x 400<br>0 . 9<br>300<br>0 . 8<br>0 . 7 200<br>0 . 6<br>100<br>0 . 5<br>0 . 4 0<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>After 2021-09-01<br>1 . 0<br>y =  x 400<br>0 . 9<br>300<br>0 . 8<br>0 . 7 200<br>0 . 6<br>100<br>0 . 5<br>0 . 4 0<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>Target coverage Target coverage<br>coverage width<br>Empirical Interval<br>coverage width<br>Empirical Interval<br>**----- End of picture text -----**<br>


Figure 6.4: PIs’s performance of individual probabilistic forecasts at test time, before September 2021 (top row) and after September 2021 (bottom row), for various target coverage levels ( _x_ -axis). The left column represents the average empirical coverage: the closest to the _y_ = _x_ line the better, and above it is best. The right column represents the average interval width: the lower the better. The colors and shapes are associated with the models. The shaded regions correspond to the 5% and 95% empirical quantiles after bootstrapping 500 times the test time series, see Section 6.5.1 for details. 

_6.4. Adaptiveness as a wrapper around individual forecasts_ 

121 

(or not) forecasts, that is able to robustify them in terms of validity but whose efficiency and shape will always rely on the quality of the underlying forecast. 

Suppose that we have _T_ 0 random variables _{_ ( _Xt, Yt_ ) _}[T] t_ =1[0][.][For][a][given][miscoverage][rate] _α ∈_ [0 _,_ 1], we aim at building a _marginally valid_ PI _C_[�] _α_ of _YT_ 0+1, i.e. _C_[�] _α_ should satisfy: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0139-04.png)


To achieve this, Split Conformal Prediction (SCP) (Papadopoulos et al., 2002; Lei et al., 2018) randomly splits the _T_ 0 data points into a training set Tr and a calibration ˆ set Cal. A regression model _µ_ is then fitted on Tr and used to predict on Cal to obtain a set of conformity scores _S_ Cal = _{St_ := _s_ ( _Xt, Yt_ ; ˆ _µ_ ) _, t ∈_ Cal _}_ . These scores assess the conformity between the calibration’s observed values and the predicted ones: the smaller the better. In the case of regression, they are usually computed using the absolute value ˆ ˜ of the residuals, i.e. _St_ := _s_ ( _Xt, Yt_ ; ˆ _µ_ ) = _|µ_ ( _Xt_ ) _− Yt|_ . A corrected[2] (1 _− α_ )-th empirical quantile of the conformity scores _Q_ 1 _−α_ ˜( _S_ Cal) is obtained, to finally build the prediction interval _C_[�] _α_ := _{y_ : _s_ ( _XT_ 0+1 _, y_ ; ˆ _µ_ ) _≤ Q_ 1 _−α_ ˜( _S_ Cal) _}_ . In the standard regression case, it boils down to _C_[�] _α_ ( _XT_ 0+1) = [ˆ _µ_ ( _XT_ 0+1) _± Q_ 1 _−α_ ˜( _S_ Cal)]. This procedure is guaranteed theoretically to satisfy Equation (6.1) for any model _µ_ ˆ, any sample size _T_ 0, as long as the calibration and test data are exchangeable. 

Proposed by Romano et al. (2019), Conformalized Quantile Regression (CQR) benefits simultaneously from the adaptiveness of classical QR methods and from the theoretical guarantees ensured by CP. Instead of training a mean regression model on the training set Tr, ˆ CQR requires to fit two conditional quantile regression models _qℓ_ ( _·_ ) _,_ ˆ _qu_ ( _·_ )[3] . In this context, the conformity scores now quantify the error made by the fitted PI _C_[�] ( _x_ ) := [ _q_ ˆ _ℓ_ ( _x_ ) _,_ ˆ _qu_ ( _x_ )]. ˆ ˆ Precisely, _St_ := _s_ ( _Xt, Yt_ ; ˆ _qℓ,_ ˆ _qu_ ) = max _{qℓ_ ( _Xt_ ) _− Yt_ ; _Yt − qu_ ( _Xt_ ) _}_ . Accordingly, the PI becomes _C_[�] _α_ ( _XT_ 0+1) = [ˆ _qℓ_ ( _XT_ 0+1) _− Q_ 1 _−α_ ˜( _S_ Cal) _,_ ˆ _qu_ ( _XT_ 0+1) + _Q_ 1 _−α_ ˜( _S_ Cal)]. 

To account for the temporal aspect of time series, an online and sequential version of SCP is usually considered, in which the split leading to Tr and Cal is not random, but constrained so that any point in Tr occurs before any point in Cal (Wisniewski et al., 2020; Zaffran et al., 2022). See Figure 6.5 for an illustration. 

## **6.4 Adaptiveness as a wrapper around individual forecasts** 

The online setting—in which the environment reveals the true value before the next prediction—allows to post-process individual predictors to adapt to previous errors (e.g., as done in CP). This approach demonstrates all its interest when stationarity – and consequently neither exchangeability – does not hold, as in our case study. One way to implement such a post-processing, coming from the online literature, is online aggregation 

> 2The correction 1 _− α_ ˜ = (1 _− α_ )(1 + #Cal1[)][is][needed][to][ensure][finite][sample][validity,][because][of][the][inflation] of the quantiles. 

> 3Usually _ℓ_ = _α/_ 2 and _u_ = 1 _− α/_ 2, but this is not necessary. Romano et al. (2019) suggest to choose these values by cross-validation, to improve PI’s efficiency. 

_Chapter 6. Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and_ 122 _2021_ 

_2021_ 

of predictors, as described in Section 6.4.1[4] . Another strategy, within the CP framework, is to modify the calibration step of CP (see Section 6.4.2) and make it adaptive. 

## **6.4.1 Online aggregation based strategies** 

Adaptive aggregation of _experts_ (Cesa-Bianchi and Lugosi, 2006), with _K ∈_ N _[∗]_ experts ˆ denoted _ft_[(] _[k]_[)] ( _·_ )[various][individual][forecasters][for][the][prices][at][time] _[t]_[(that] � � _k∈_ �1 _,K_ �[being] is a corresponding day _d_ on a given hour _h_ ) such as the ones introduced in Section 6.3.2, computes an optimal weighted mean of the experts. At each time _t_ (i.e., day _d_ , for a given hour _h_ ), the weights _ωt_[(] _[k]_[)] assigned to expert _k_ depend on all experts’ suffered _losses_ , i.e. their performances on the previous time steps until _t −_ 1. In our case, these performances are evaluated through the pinball loss _ρβ_ , standard in quantile regression, with the pinball parameter _β_ being the target quantile level. These losses are plugged in the _aggregation rule_ Φ, outputting the aggregation weights. Finally, the aggregation rule can include the computation of the gradients of the loss ( _gradient trick_ , see (Cesa-Bianchi and Lugosi, 2006) for more details). As aggregation rules require bounded experts, a thresholding step is added. Concretely, the aggregated predictor at time _t_ , _f_[ˆ] _t_[Φ][(] _[·]_[)][,][is][defined][by] _K f_ ˆ _t_[Φ][(] _[X][t]_[) =] � _ωt_[(] _[k]_[)] _ft_[(] _[k]_[)] ( _Xt_ ) _. k_ =1 In our experiments, the different forecasts obtained are aggregated quantile by quantile, using the appropriate pinball loss as a score. The aggregation rule Φ is set to be the Bernstein Online Aggregation (BOA) (Wintenberger, 2017) algorithm, along with the gradient trick.We use the R package OPERA (Gaillard and Goude, 2021) to perform such an aggregation, and reorder the quantiles predicted by the aggregation models to avoid quantile crossing. 

Recently, Berrisch and Ziel (2023) proposed an approach that jointly aggregates every quantile forecasting model together and gives directly a probabilistic prediction as an output, instead of performing independent aggregation for each quantile level. Berrisch and Ziel (2023)’s method reduces the number of aggregation parameters to be computed, while yielding preferable probabilistic performances. It is available in the R-Package `profoc` (Berrisch and Ziel, 2024b), compatible with the BOA method with the gradient trick and automatically reordering the predicted quantiles. It has to be noted that we did not explore the full range of tuning possibilities allowed by this method. In our experiments, both approaches performed similarly. Therefore, to avoid overloading the analysis, we present in this paper only the first method. 

## **6.4.2 Adaptive conformal approaches** 

In addition to online aggregation, we consider another post-processing of individual forecasters which consists in adding a conformal layer on top of them, adaptively. As explained 

> 4This does not include Quantile Regression Averaging (QRA) (Nowotarski and Weron, 2014) as it is an offline averaging, thus non-adaptive. 

_6.4. Adaptiveness as a wrapper around individual forecasts_ 

123 

in Section 6.3.3, CP requires exchangeable data, an assumption clearly not satisfied in a time series setting, and even less in our highly non-stationary case study. 

The first theoretically grounded result on CP for dependent data is given by Chernozhukov et al. (2018): it shows that when the data is strongly mixing and the learned model is close “enough” to the underlying data generation process then CP guarantees still hold, along with proposing an extension for full CP[5] under which the previous theorem holds. Again, this is not sufficient to encapsulate our setting. 

In practice, Online Sequential Split Conformal Prediction (OSSCP) is often used to take into account the temporal structure, introduced in Wisniewski et al. (2020); Zaffran et al. (2022). The idea is (i) to enforce a sequential split where all the training observations are temporally consecutive, and preceding the ones of the calibration set and (ii) to update this split in order to incorporate the newly observed data points at each prediction step _t_ + 1, forgiving the oldest ones, leading to adaptive sets Tr _t_ and Cal _t_ . See Figure 6.5 (a) for an illustration. Note that OSSCP does not enjoy any form of theoretical guarantees beyond the exchangeable setting, despite its good empirical performances in the time series framework, as highlighted in (Zaffran et al., 2022). 

## 6.4.2.1 Improving CP online adaptiveness: `OSSCP-horizon` 

One drawback of OSSCP is that the set on which the models were fitted can be far from the points on which it will be applied (either calibration or test points). If the temporal data suffers from a strong distribution shift, this may hinder the accuracy of the base learner, and therefore the performances of the PI, both in terms of coverage (the exchangeability assumption is not satisfied anymore) and in terms of efficiency, i.e. interval’s length (as large errors cause large intervals). 

In order to avoid high errors on the calibration and test points, we propose a new approach, coined `OSSCP-horizon` . The idea is to ensure that the underlying model is trained on the data just preceding each calibration point: in other words, to only compute test errors of horizon one, as is the forecast horizon. More generally, for any forecasting task at horizon _h_ , `OSSCP-horizon` computes calibration errors of horizon _h_ . See Figure 6.5 (b) for an illustration. Formally, at prediction time _T_ + 1, `OSSCP-horizon` thus builds the calibration set as follows: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0141-08.png)


- Compute the calibration score _St_ = _s Xt, Yt_ ; ˆ _qℓ[−]_[(] _[t]_[)] _,_ ˆ _qu[−]_[(] _[t]_[)] and add it to the set of � � 

- scores _S_ Cal _T_ . 

> 5Full CP is a version of CP that does not require to split the data, at the cost of a bigger computational burden. This is the reason why we do not consider it in this work, along with the fact that full CP can be plugged in on an existing pipeline, making it particularly appealing for operational purposes. The interested reader on full CP can have a look at (Vovk et al., 2005) 

> 6 ˆ ˆ For a horizon _h ̸_ = 1, then _qℓ[−]_[(] _[t]_[)] , _qu[−]_[(] _[t]_[)] are fitted on �� _Xt−|_ Tr _|, Yt−|_ Tr _|_ � _, . . . ,_ ( _Xt−h, Yt−h_ )�. 

124 

_2021_ 

_Chapter 6. Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0142-03.png)


**----- Start of picture text -----**<br>
Unused data Proper training set Calibration set Test point<br>(a) OSSCP (b) OSSCP-horizon<br>**----- End of picture text -----**<br>


Figure 6.5: Scheme of OSSCP (a) and our proposal (b), `OSSCP-horizon` , when the horizon is 1. 

After having built _S_ Cal _T_ = _{ST −|_ Cal _|_ +1 _, . . . , sT }_ , `OSSCP-horizon` computes the PI for the test point _XT_ +1: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0142-06.png)


Again, while demonstrating empirical improvements upon standard OSSCP in the temporal setting, `OSSCP-horizon` does not enjoy any form of theoretical guarantees. To theoretically account for the online setting, a popular method is Adaptive Conformal Inference (ACI) (Gibbs and Candès, 2021). 

## 6.4.2.2 Adaptive Conformal Inference (ACI) 

Proposed in (Gibbs and Candès, 2021), ACI adapts CP to an arbitrary online setting, including temporal distribution shits. To do so, ACI recursively updates the _effective_ ˜ miscoverage rate _α_ := _αt_ used in the computation of the PI. Set _α_ 1 = _α_ . For _t ≥ T_ 0, and for a chosen _γ ≥_ 0 the ACI update formula is: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0142-10.png)


The underlying idea is the following. If the PI does not cover at time _t_ , then _αt_ +1 _≤ αt_ which increases the size of the PI. Conversely, the size of the interval decreases gently at time _t_ +1 when it covers at time _t_ . As noted in (Zaffran et al., 2022), it is possible to have _αt ≥_ 1 or _αt ≤_ 0: the former case is quite rare and produces by convention _C_[�] _αt_ = [ˆ _qℓ_ ( _·_ ) _,_ ˆ _qu_ ( _·_ )]; however, the latter can happen frequently, especially for a high _γ_ , giving a prediction interval of infinite size ( _C_[�] _αt ≡_ R). 

The main theoretical result on ACI is that for any sequence ( _Xt, Yt_ ) _t_ , 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0142-13.png)


_6.4. Adaptiveness as a wrapper around individual forecasts_ 

125 

It shows the asymptotically valid frequency of ACI intervals for any arbitrary (possibly adversarial) distribution. 

Note that the convergence rate is in _γ[−]_[1] , hence favoring large _γ_ which are the ones leading to more variability and in the extreme case to infinite PIs (discussed previously). This illustrates the need for guidance on how to choose properly _γ_ , and even avoid having to choose it and being able to switch between different _γ_ depending on the current data distribution’s evolution. 

## 6.4.2.3 AgACI 

The goal of AgACI, proposed in (Zaffran et al., 2022), is precisely to provide a parameterfree method based on ACI, that can adapt to temporal changes in the data distribution adaptively. Given a list of _K γ_ values _{γk}[K] k_ =1[,][AgACI][works][as][an][adaptive][aggregation][of] experts (Cesa-Bianchi and Lugosi, 2006) (see also Section 6.4.1), with expert _k_ being ACI with parameter _γk_ . At each prediction step _t_ , it performs two independent aggregations of the _K_ ACI intervals _C_[�] _αt,k_ ( _·_ )[not.] = [[ˆ] _b_[(] _t,k[ℓ]_[)][(] _[·]_[)] _[,]_[ˆ] _[b] t,k_[(] _[u]_[)][(] _[·]_[)]][,][one][for][each][bound,][and][outputs] _[C]_[�] _[t]_[(] _[·]_[)][ not.] = [[˜] _b_[(] _t[ℓ]_[)][(] _[·]_[)] _[,]_[˜] _[b]_[(] _t[u]_[)] ( _·_ )]. According to Zaffran et al. (2022), the standard different aggregation rules gave similar results. In this work, we restrict ourselves to the setting of (Zaffran et al., 2022), that is BOA, with the gradient trick. 

## 6.4.2.4 Latest related works 

Since the analysis presented in this paper was performed, the line of research on adaptive and online conformal approaches has been expanding fast. Recent developments include: Gibbs and Candès (2023) improving on ACI by online aggregation on a grid of different _γ_ , similarly to AgACI, at the crucial difference that the aggregation is on the value of _αt_ and not on the lower and upper bounds independently (Section 6.5.2 highlights why we argue in favor of different aggregations); Bastani et al. (2022) who achieve stronger coverage guarantees (conditional on the effective level, and conditional on specified subsets of the explanatory variables); Bhatnagar et al. (2023) enjoy anytime regret bound, by leveraging tools from the strongly adaptive regret minimization literature; Angelopoulos et al. (2023) who extend upon ACI ideas by relying on control theory to add more information on the temporal structure; Angelopoulos et al. (2024) proposing to use adaptive learning rates _γt_ in ACI. 

Our goal in this analysis is to deeply investigate the improvements, or not, brought by conformal as one of the layers for probabilistic forecasts with an operational lens. Therefore, we restricted the study to OSSCP, `OSSCP-horizon` , and AgACI as it has already shown benefits on electricity prices and does not require to select any hyper-parameter (Zaffran et al., 2022). Indeed, it allows us to easily understand what is the cause of the improved or declined performance. Furthermore, the most recent works are either complex structures (thus less interpretable) or depend on hyper-parameter tuning, making them more costly to implement in operational use. 

_Chapter 6. Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and_ 126 _2021_ 

## **6.5 Application and results** 

## **6.5.1 Setting and evaluation** 

**Experimental details** In order to span a wide range of the price distribution function, we vary the PIs’ miscoverage level 1 _− α >_ 0 _._ 6. For the final probabilistic forecasts, the overall training set comprises 4 years of data, from 2016 to 2019 included (i.e. merging the training and validation sets). 

Due to training time constraints, we trained and evaluated the considered models on hours 3, 8, 13, 18, and 23 of every day. These 5 hours encompass best the different phases of hourly electricity prices in a given day, while uniformly covering the 24 hours of the day. 

Finally, due to the high non-stationarity, we trained each of the base models presented in Section 6.3.2 on different window sizes: approximately 4 years, 3 years, 2 years, 1 year, 270 days, 180 days, and 90 days. For the sake of clarity, for each analysis performed, the largest window size will be selected and presented in this paper. In the same vein, the calibration size of the conformal approaches (Sections 6.3.3 and 6.4.2) varies among 25%, 50% and 75% of the overall windowed training set. Again, to ease interpretation of our results, we present here only the results for a calibration set of proportion 50% (except if stated otherwise) as it allows for an intermediary adaptation speed, hence being a good trade-off between up-to-date quantile regression models and calibration set large enough to perform the estimation of the highly non-stationary conformal correction. We recall that in the i.i.d. setting a general rule of thumb for the calibration size is around 25% (Sesia and Candès, 2020). In our study, the impact of non-stationarity induces a need for a trade-off between adaptivity and the calibration window length. 

**Evaluation procedure** The main challenge of evaluating a probabilistic forecast is that the true distribution of the underlying process cannot be observed. Hence, it is impossible 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0144-07.png)


**----- Start of picture text -----**<br>
QR OSSCQR OSSCQR-horizon AgACI on OSSCQR-horizon<br>Before 2021-09-01<br>1 . 0<br>y =  x<br>0 . 9 150<br>0 . 8<br>100<br>0 . 7<br>0 . 6 50<br>0 . 5<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>After 2021-09-01<br>1 . 0<br>y =  x<br>0 . 9 150<br>0 . 8<br>100<br>0 . 7<br>0 . 6 50<br>0 . 5<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>Target coverage Target coverage<br>coverage width<br>Empirical Interval<br>coverage width<br>Empirical Interval<br>**----- End of picture text -----**<br>


Figure 6.6: PIs’s performances with different levels of conformalisation on the **quantile linear model** , before September 2021 (top row) and after September 2021 (bottom row), for various target coverage levels ( _x_ -axis). The colors and shapes are associated with the conformalisation layers. The shaded regions correspond to the 5% and 95% empirical quantiles after bootstrapping 500 times the test time series. 

_6.5. Application and results_ 

127 

to compare the estimated distribution with the actual distribution of the true spot prices. ˆ ˆ This is not the case for a sequence of PIs _b_[(] _[ℓ]_[)] ( _·_ ) _, b_[(] _[u]_[)] ( _·_ )[can][be][evaluated][through:] �� �� _t_[that] 

• **empirical average coverage** , _T_ 1 _−_ 1 _T_ 0 _t_ =� _TT_ 01+1 1 � _yt ∈_ �ˆ _b_[(] _[ℓ]_[)] ( _xt_ ) _,_ ˆ _b_[(] _[u]_[)] ( _xt_ )��, that should be close and above to the target level 1 _− α_ for _validity_ (also known as _reliability_ ), 

- **empirical average length** , _T_ 1 _−_ 1 _T_ 0 � _T_ 1 ˆ _b_[(] _[u]_[)] ( _xt_ ) _−_ ˆ _b_[(] _[ℓ]_[)] ( _xt_ ), for _efficiency_[7] (also _t_ = _T_ 0+1 

- known as _sharpness_ ). 

For each of these metrics, confidence intervals are constructed by time series bootstrapping (non-overlapping moving block bootstrap) (Kunsch, 1989; Politis and Romano, 1994). 

Results on the CRPS are provided in 6.A. Indeed, our goal is really to compare PIs and not predictive distributions. Therefore, the forecasts’ objective is truly to **be as sharp as possible while satisfying validity** . 

## **6.5.2 Results** 

**Impact of the conformalisations** In Figures 6.6 and 6.7 we represent the performance of Linear Quantile Regression and Quantile Random Forest respectively, with various layers of conformalisation. The display choice of these two base models is motivated by the fact that they represent a diverse range of modelisation. 

In both cases, we observe that a naive conformalisation – in the form of OSSCP – does not allow to achieve the nominal coverage level, neither before nor after September 2021. 

Yet, our proposal `OSSCP-horizon` does improve drastically the coverage level: before September 2021 it manages to reach the target level while improving the lengths of the PIs, and after September 2021 it allows to reduce the gap with the target considerably (linear model), while recovering the approximatively satisfactory performances of the individual QRF that was deteriorated by OSSCP. 

Finally, making the conformalisation even more adaptive through the use of AgACI especially enhances validity after September 2021. Yet, it has to be noted that it seems to be insufficiently adaptive to perfectly reach the target level. 

**Analysis of various aggregations** Therefore, we go further and add another adaptive post-processing layer by performing online aggregagation. In Figure 6.8 we compare the performances of various aggregations, each of them considering a different set of experts (individual forecasts, `OSSSCP-horizon` forecasts, AgACI forecasts, and all of them). As a baseline, we add the uniform average of all of these experts. For each of the aggregation, we compared aggregating forecasts with a unique window size for training with aggregating forecasts with multiple training window size (hence augmenting the number of experts in 

> 7Indeed, achieving exactly 1 _− α_ coverage can be trivially done by outputting 1 _− α_ of the time R and the empty set otherwise, which is critically uninformative. Thus, one wants to attain _validity_ while minimizing the size of the resulting intervals, that is maximizing _efficiency_ . 

_Chapter 6. Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and_ 

128 

_2021_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0146-03.png)


**----- Start of picture text -----**<br>
QR OSSCQR OSSCQR-horizon AgACI on OSSCQR-horizon<br>Before 2021-09-01<br>1 . 0 y =  x 300<br>0 . 8 250<br>0 . 6 200<br>150<br>0 . 4<br>100<br>0 . 2<br>50<br>0 . 0<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>After 2021-09-01<br>1 . 0 y =  x 300<br>0 . 8 250<br>0 . 6 200<br>150<br>0 . 4<br>100<br>0 . 2<br>50<br>0 . 0<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>Target coverage Target coverage<br>coverage width<br>Empirical Interval<br>coverage width<br>Empirical Interval<br>**----- End of picture text -----**<br>


Figure 6.7: Same caption than Figure 6.6 but for the **quantile random forest model** . 

the set). This latter strategy is usually referred to as _windowing_ (Marcjasz et al., 2018). We selected the best aggregation (namely aggregating AgACI forecasts with windowing) and, for the sake of readability and for coherence, we displayed in Figure 6.8 all the aggregations with windowing. It has to be noted that there is a lot of variability, as it can be seen in Figure 6.8, and that for some aggregation the best choice was in fact without windowing. 

Figure 6.8 highlights that online aggregation improves considerably the robustness to non-stationarity in terms of validity. Furthermore, after September 2021, online aggregation on AgACI forecasts enhances the sharpness of the forecasts with respect to the uniform average, that has similar coverage. This can be explained by the fact that the individual performances degrade in this non-stationary environment, leading to aggregation’s weights close to uniform so as to minimise the risk (as we will also see in the next analysis). 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0146-07.png)


**----- Start of picture text -----**<br>
BOA on Individual forecasts BOA on Conformalized forecasts BOA on AgACI forecasts BOA on All Uniform average<br>Before 2021-09-01<br>1 . 00 y =  x 250<br>0 . 95 200<br>0 . 90<br>150<br>0 . 85<br>0 . 80 100<br>0 . 75 50<br>0 . 70<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>After 2021-09-01<br>1 . 00 y =  x 250<br>0 . 95 200<br>0 . 90<br>150<br>0 . 85<br>0 . 80 100<br>0 . 75 50<br>0 . 70<br>0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975 0 . 800 0 . 825 0 . 850 0 . 875 0 . 900 0 . 925 0 . 950 0 . 975<br>Target coverage Target coverage<br>coverage width<br>Empirical Interval<br>coverage width<br>Empirical Interval<br>**----- End of picture text -----**<br>


Figure 6.8: PIs’s performances of online aggregation on multiple set of experts with windowing, before September 2021 (top row) and after September 2021 (bottom row), for various target coverage levels ( _x_ -axis). The colors and shapes are associated with the set of experts. The shaded regions correspond to the 5% and 95% empirical quantiles after bootstrapping 500 times the test time series. 

_6.6. Conclusion and perspectives_ 

129 

**Analysis of aggregation of various AgACI: applying the best conformalisation possible (AgACI) on each model and then aggregating them** In Figure 6.9 we represent the evolution of the weights associated to each of the AgACI (the color representing the base model, and the shade of it indicating the calibration percentage) with time _x_ -axis, for various coverage level (columns). To improve readability, we display these weights for the aggregation without windowing. 

The first striking observation is the presence of temporal ruptures in the weights’ distribution. They are informative as they are associated with domain phenomena, which depend on the considered bound (lower or upper). Particularly, the first one happening is the big negative spike in Easter 2020 (April 13, 2020, see top row of Figure 6.1) due to both the public holiday and the Covid-19 lockdown. This especially affects the lower bound. The second one occurs in the second fortnight of September 2020 when the first extreme positive peaks take place, impacting the upper bound. These positive spikes are mainly due to a very low wind generation in France (less than 1 GW) and more generally in Europe, along with a French nuclear production well below its level of previous years at the same time. The last significant rupture is around October 2021, when spot prices start to rise drastically and get more and more volatile, corresponding to the increase in level and volatility of gas and carbon emission prices. This one affects both the lower and upper bounds. In particular, the weights’ distribution becomes uniform after this rupture, which is expected in a setting where the aggregation tries to minimize the risk with experts performing poorly. 

The second observation is that the methods on which the aggregation places the most of the weights is different depending on the bound: remarkably, at the levels 0.95 and 0.98, the lower bound places high mass on quantile random forests, while the upper bound relies more on qgam. This can be explained by the fact that the various methods depend differently on the provided features: additive models such as qgam or linear ones have a great extrapolation ability, while random forests and gradient boosting benefit from more flexibility on features’ interaction modeling. This idea is also reflected in Figures 6.2 and 6.3 comparing the feature importance in Lasso with the one of Random forest. 

Lastly, for high levels of coverage such as 0.95 and 0.98, the aggregation also places weights on different training size depending on the bound. While the upper bound favors small training size, the lower bound encourages large training size. This might be due to the effective sample size which is required to appropriately learn the lower quantiles of the prices, which are less impacted by the non-stationarity; while the upper bound is particularly complex to model, and having more data points correct the predictive model through conformalisation might be a better usage of the available data. 

These three key observations argue in favor aggregating independently the upper and lower bounds. 

## **6.6 Conclusion and perspectives** 

In this study, we have analysed the performances of a wide range of probabilistic methods in a particularly challenging task: forecasting electricity spot prices in France in 2020 and 

_Chapter 6. Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and_ 130 _2021_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0148-01.png)


**----- Start of picture text -----**<br>
QRF (75 %) QGB (75 %) Lasso QR (75 %) Linear QR (75 %) QGAM (75 %)<br>QRF (50 %) QGB (50 %) Lasso QR (50 %) Linear QR (50 %) QGAM (50 %)<br>QRF (25 %) QGB (25 %) Lasso QR (25 %) Linear QR (25 %) QGAM (25 %)<br>1  − α  = 0.6 1  − α  = 0.9 1  − α  = 0.95 1  − α  = 0.98<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>1 . 0 1 . 0 1 . 0 1 . 0<br>0 . 5 0 . 5 0 . 5 0 . 5<br>0 . 0 0 . 0 0 . 0 0 . 0<br>2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02 2020-01-112020-07-292021-02-142021-09-02<br>bound<br>Upper<br>bound<br>Lower<br>**----- End of picture text -----**<br>


Figure 6.9: Temporal evolution ( _x_ -axis) of the weights associated with each expert in the online aggregation, for different values of (columns). The top row (resp. bottom row) shows the weights assigned for the upper (resp. lower) bound forecast. The colors correspond to the base model on which AgACI is applied to, and the transparency to the proportion of training data kept for actually fitting these base models. 

2021. On the design, we have highlighted the importance of including the new explanatory variable corresponding to the nuclear plants’ availability. We were also able to bring new insights into the post-processing of individual forecasts, such as conformalisation or aggregation. Indeed, our extensive experiments demonstrate that _i_ ) conformalisation, when appropriately done as through `OSSCP-horizon` , considerably improves PI’s quality despite the non-stationarity, _ii_ ) online aggregation of experts is extremely powerful in terms of adaptiveness bringing enhanced PI’s performances and taking advantage of windowing, _iii_ ) combining both conformalisation and online aggregation appears on this data set to be the best strategy, and most importantly sheds light on many domain phenomena thanks to great interpretability. 

There are many avenues for future works. From the electricity lens, the prices have continued to evolve significantly since 2022 and pursuing the study on newer data would undoubtedly yield new knowledge. Speaking of which, our study did not investigate the crucial question of peaks and extreme forecasts, dominant in electricity prices. Works on online procedure tailored for extremes have already been deployed (Himych et al., 2024), and it might be relevant to see how it can be paired with conformal approaches. Another natural perspective that would deepen our understanding on the benefits of conformalisation is to conformalize the aggregated models as suggested in Susmann et al. (2024), as opposed to aggregating the conformalized models which is what we performed. It would also be interesting to assess the performances of the most recent online conformal algorithms (listed in Section 6.4.2.4), that might be better suited for non-stationarity. Finally, our angle of approach is to showcase the advantages of black-box plugs-in such as CP and aggregation. It is attractive to couple it with recent developments that enhance the interpretability of complex statistical models, such as Wood et al. (2022). 

## **Appendix to Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and 2021** 

## **6.A Results on the CRPS** 

To assess the performance of a probabilistic method on the overall range of quantiles, one can use the Continuous Ranked Probability Score (CRPS). This score is originally described in terms of the predictive CDS _F_[ˆ] _d,h_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0149-03.png)


Interestingly, the CRPS can be reformulated (to a multiplicative constant) as : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0149-05.png)


where _F_[ˆ] _[−]_[1][actually][corresponds][to][the][predicted][value][at][quantile] _[α]_[.][By][approximating] _d,h_[(] _[α]_[)] this integral as a Riemann sum, we can transform pinball scores over multiple quantiles into one single metric. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0149-07.png)


**----- Start of picture text -----**<br>
QR OSSCQR OSSCQR-horizon AgACI on OSSCQR-horizon<br>17 . 5<br>15 . 0<br>12 . 5<br>10 . 0<br>7 . 5<br>5 . 0<br>2 . 5<br>0 . 0<br>Date<br>2020 − 01 2020 − 04 2020 − 07 2020 − 10 2021 − 01 2021 − 04 2021 − 07 2021 − 10 2022 − 01<br>CRPS<br>**----- End of picture text -----**<br>


Figure 6.10: PIs’s CRPS with different levels of conformalisation on the **quantile linear model** , depending on the time. The colors and shapes are associated with the conformalisation layers. 

131 

_Chapter 6. Adaptive Probabilistic Forecasting of French Electricity Spot Prices in 2020 and_ 

132 

_2021_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0150-03.png)


**----- Start of picture text -----**<br>
QR OSSCQR OSSCQR-horizon AgACI on OSSCQR-horizon<br>120<br>100<br>80<br>60<br>40<br>20<br>0<br>Date<br>2020 − 01 2020 − 04 2020 − 07 2020 − 10 2021 − 01 2021 − 04 2021 − 07 2021 − 10 2022 − 01<br>CRPS<br>**----- End of picture text -----**<br>


Figure 6.11: Same caption than Figure 6.10 but for the **quantile random forest model** . 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0150-05.png)


**----- Start of picture text -----**<br>
BOA on Individual forecasts BOA on Conformalized forecasts BOA on AgACI forecasts BOA on All Uniform average<br>16<br>14<br>12<br>10<br>8<br>6<br>4<br>2<br>0<br>Date<br>2020 − 01 2020 − 04 2020 − 07 2020 − 10 2021 − 01 2021 − 04 2021 − 07 2021 − 10 2022 − 01<br>2020 − 03 2020 − 05 2020 − 07 2020 − 09 2020 − 11 2021 − 01 2021 − 03 2021 − 05 2021 − 07 2021 − 09<br>CRPS<br>**----- End of picture text -----**<br>


Figure 6.12: PIs’s CRPS of online aggregation on multiple set of experts with windowing, depending on the time. The colors and shapes are associated with the set of experts. 

## **Part III** 

## **Missing Values** 

133 

## **Chapter 7** 

## **Conformal Prediction with Missing Values** 

Conformal prediction is a theoretically grounded framework for constructing predictive intervals. We study conformal prediction with missing values in the covariates – a setting that brings new challenges to uncertainty quantification. We first show that the marginal coverage guarantee of conformal prediction holds on imputed data for any missingness distribution and almost all imputation functions. However, we emphasize that the average coverage varies depending on the pattern of missing values: conformal methods tend to construct prediction intervals that under-cover the response conditionally to some missing patterns. This motivates our novel generalized conformalized quantile regression framework, missing data augmentation, which yields prediction intervals that are valid conditionally to the patterns of missing values, despite their exponential number. We then show that a universally consistent quantile regression algorithm trained on the imputed data is Bayes optimal for the pinball risk, thus achieving valid coverage conditionally to any given data point. Moreover, we examine the case of a linear model, which demonstrates the importance of our proposal in overcoming the heteroskedasticity induced by missing values. Using synthetic and data from critical care, we corroborate our theory and report improved performance of our methods. 

135 

_Chapter 7. Conformal Prediction with Missing Values_ 

136 

||**Contents**|
|---|---|
||7.1<br>Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137<br>7.2<br>Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139<br>7.3<br>Warm-up: marginal coverage with `NA`s . . . . . . . . . . . . . . . . . . . . . 140<br>7.4<br>Challenge: `NA`s induce heteroskedasticity . . . . . . . . . . . . . . . . . . . . 141<br>7.5<br>Achieving mask-conditional-validity (MCV) . . . . . . . . . . . . . . . . . . 142<br>7.5.1<br>Missing Data Augmentation (MDA) . . . . . . . . . . . . . . . . . . 143<br>7.5.2<br>Theoretical guarantees in fnite sample . . . . . . . . . . . . . . . . . 145<br>7.6<br>Towards asymptotic individualized coverage . . . . . . . . . . . . . . . . . . 146<br>7.7<br>Empirical study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147<br>7.7.1<br>Synthetic experiments: Gaussian linear data . . . . . . . . . . . . . . 148<br>7.7.2<br>Semi-synthetic experiments . . . . . . . . . . . . . . . . . . . . . . . 149<br>7.7.3<br>Predicting the level of platelets for trauma patients . . . . . . . . . . 150<br>7.8<br>Conclusion and perspectives . . . . . . . . . . . . . . . . . . . . . . . . . . . 151<br>7.A Detailed perspective discussion<br>. . . . . . . . . . . . . . . . . . . . . . . . . 153<br>7.B<br>Illustration and details on CQR (Romano et al., 2019) procedure . . . . . . 154<br>7.C<br>Impute-then-predict+conformalization . . . . . . . . . . . . . . . . . . . . . 156<br>7.D Gaussian linear model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157<br>7.E<br>Finite sample algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160<br>7.F<br>Infnite data results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165<br>7.G Experimental study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168|



_7.1. Introduction_ 

137 

## **7.1 Introduction** 

By leveraging increasingly large data sets, statistical algorithms and machine learning methods can be used to support high-stakes decision-making problems such as autonomous driving, medical or civic applications, and more. To ensure the safe deployment of predictive models it is crucial to quantify the uncertainty of the resulting predictions, communicating the limits of predictive performance. Uncertainty quantification attracts a lot of attention in recent years, particularly methods that are based on Conformal Prediction (CP) (Vovk et al., 2005; Papadopoulos et al., 2002; Lei et al., 2018). CP provides controlled predictive regions for any underlying predictive algorithm (e.g., neural networks and random forests), in finite samples with no assumption on the data distribution except for the exchangeability of the train and test data. More precisely, for a _miscoverage rate α ∈_ [0 _,_ 1], CP outputs a _marginally valid_ prediction interval _C_[�] _α_ for the test response _Y_ given its corresponding covariates _X_ , that is: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0155-04.png)


Split CP (Papadopoulos et al., 2002; Lei et al., 2018) achieves Eq. (7.1) by keeping a hold-out set, the _calibration set_ , used to evaluate the performance of a fixed predictive model. 

At the same time, as the volume of data increases, the volume of missing values also increases. There is a vast literature on this topic (Little, 2019; Josse and Reiter, 2018), and a recent survey even identified more than 150 different implementations (Mayer et al., 2019). Missing values create additional challenges to the task of supervised learning, as traditional machine learning algorithms can not handle incomplete data (Josse et al., 2019; Le Morvan et al., 2020b,a, 2021; Ayme et al., 2022; Van Ness et al., 2022). One of the most popular strategies to deal with missing values suggests imputing the missing entries with plausible values to get completed data, on which any analysis can be performed. The drawback of this “impute-then-predict” approach is that single imputation can distort the joint and marginal distribution of the data. Yet, Josse et al. (2019); Le Morvan et al. (2020b, 2021) showed that such impute-then-predict strategies are Bayes consistent, under the assumption that a universally consistent learner is applied on an imputed data set. However, this line of work focuses on point prediction with missing values that aim to predict the most likely outcome. In contrast, our goal is quantifying predictive uncertainty, which was not explored with missing values although its enormous importance. 

## **Contributions.** 

We study CP with missing covariates. Specifically, we study downstream quantile regression (QR) based CP, like CQR (Romano et al., 2019), on impute-then-predict strategies. Still, the proposed approaches also encapsulate other regression basemodels, and even classification. 

After setting background in Section 7.2, our first contribution is showing that CP on impute-then-predict is _marginally_ valid regardless of the model, missingness distribution, and imputation function (Section 7.3). 

_Chapter 7. Conformal Prediction with Missing Values_ 

138 

Then, we focus on the specificity of uncertainty quantification _with missing values_ . In Section 7.4, we describe how different masks (i.e. the set of observed features) introduce additional heteroskedasticity: _the uncertainty on the output strongly depends on the set of predictive features observed_ . We therefore focus on achieving valid coverage _conditionally on the mask_ , coined MCV – Mask-Conditional-Validity. MCV is desirable in practice, as occurrence of missing values are linked to important attributes (see Section 7.5). 

Traditional approaches such as QR and CQR fail to achieve MCV because they do not account for this core connection between missing values and uncertainty. This is illustrated on synthetic data in Figure 7.1. In Figure 7.1a, a toy example with only 3 features, thus 2[3] _−_ 1 = 7 possible masks, shows how the coverage of QR and CQR varies depending on the mask. Both methods dramatically undercover when the most important variable ( _X_ 2) is missing, and the loss of coverage worsens when additional features are missing. In particular, for each method, one mask ( _X_ 1 and _X_ 2 missing, highlighted in red) leads to the _lowest mask coverage_ . Achieving MCV corresponds to a lowest mask coverage greater than 1 _− α_ . In Figure 7.1b, the dimension is 10: instead of the 2[10] _−_ 1 = 1023 different masks, we only report the lowest mask coverage for increasing sample sizes. It highlights that QR (green _×_ ) and CQR (orange _×_ ) do not meet the lowest mask coverage target of 90%, even for large sample sizes. 

This motivates our second contribution: we show in Section 7.5 how to form prediction intervals that are MCV. This is highly challenging since there are exponentially many possible patterns to consider. Therefore, the naive solution to perform a calibration for each mask would fail as in finite samples, we often observe test samples with a mask that have low (or even null) frequency of appearance in the calibration set. To tackle this issue, we suggest two conformal methods that share the same core idea of missing data augmentation (MDA): the calibration data is artificially masked to match the mask of the point we consider at test time. The first method, _CP-MDA with exact masking_ , relies on building an ideal calibration set for which the data points have the exact same mask as 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0156-05.png)


**----- Start of picture text -----**<br>
QR (no guarantee) CQR (marginal validity)<br>1 . 0<br>1  − 0 ↵. 8 Lowest Lowestmask 1  − 0 .α 8 QR (no guarantee)<br>maskcov. cov. CQR<br>0 . 6 ✗ MCV: ✗ ✓ MCV: ✗ (marginal validity)<br>1  − 1 .↵ 0 CQR-MDA (mask-conditional-validit with exact y masking - MCV) Lowestmaskcov. CQR-MDA (mask-conditional-validit with nested y - masking MCV) Lowestmaskcov. 00 .. 64 CQR-MDA (mask-conditional-validity CQR-MDA (mask-conditional-validity Target coverage, withwith i.e. 1 exactnested  − α -- masking MCV)MCV) masking<br>0 . 8<br>0 . 2<br>0 . 6 ✓ MCV: ✓ ✓ MCV: ✓<br>Training size<br>50 100 500 1000 2500 5000 20000<br>X Marginalfullyobserved X ( X 11missing , X 2)missing X ( X 22missing , X 3)missing X ( X 31missing , X 3)missing X Marginalfullyobserved X ( X 11missing , X 2)missing X ( X 22missing , X 3)missing X ( X 31missing , X 3)missing<br>coverage<br>Average coverage<br>mask<br>coverage Lowest<br>Average<br>**----- End of picture text -----**<br>


(b) Lowest mask coverage as a function of the training size. Results evaluated over 100 repetitions, and the (tiny) error bars correspond to standard errors. 

(a) Coverage of the predictive intervals depending on which features are missing, among the 3 features. Evaluation over 200 runs. 

Figure 7.1: Methods are Quantile Regression (QR), Conformalized Quantile Regression (CQR), and two novel procedures **CP-MDA-Exact** and **CP-MDA-Nested** , on top of CQR. Settings are given in Section 7.7, in a nutshell: data follows a Gaussian linear model where missing values are independent of everything else and of proportion 20%; the dimension of the problem is 3 in Figure 7.1a while in 7.1b it is 10. 

_7.2. Background_ 

139 

of the test point. We show its MCV under exchangeability and Missing Completely At Random assumptions. Our second method, _CP-MDA with nested masking_ , does not require such an ideal calibration set. Instead, we artificially construct a calibration set in which the data points have _at least_ the same mask as the test point, i.e., this artificial masking results in calibration points having possibly more missing values than the test point. We show the latter method also achieves the desired coverage conditional on the mask, but at the cost of an additional assumption for validity: stochastic domination of the quantiles. Figure 7.1 illustrates those findings: both methods are MCV, as their lowest mask coverage is above 1 _− α_ . 

Our third contribution further supports our design choice to use QR. We show that QR on impute-then-predict strategy is Bayes-consistent – it can achieve the strongest form of coverage conditional on the observed test features (Section 7.6). 

Lastly, we support our proposal using both (semi)-synthetic experiments and real medical data (Section 7.7). The code to reproduce our experiments is available on GitHub. 

## **7.2 Background** 

**Background on missing values.** Consider a data set with _n_ exchangeable realizations of the random variable ( _X, M, Y_ ) _∈_ R _[d] × {_ 0 _,_ 1 _}[d] ×_ R: �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][��] _[n] k_ =1[,][where] _[X]_ represents the features, _M_ the missing pattern, or mask, and _Y_ an outcome to predict. For _j ∈_ �1 _, d_ �, _Mj_ = 0 when _Xj_ is observed and _Mj_ = 1 when _Xj_ is missing, i.e. `NA` (Not Available). We note _M_ = _{_ 0 _,_ 1 _}[d]_ the set of masks. For a pattern _m ∈M, X_ obs( _m_ ) is the random vector of observed components, and _X_ mis( _m_ ) is the random vector of unobserved ones. For example, if we observe ( `NA` _,_ 6 _,_ 2) then _m_ = (1 _,_ 0 _,_ 0) and _X_ obs( _m_ ) = (6 _,_ 2). Our goal is to predict a new outcome _Y_[(] _[n]_[+1)] given _X_ obs[(] _[n]_[+1)] ( _M_[(] _[n]_[+1)] )[and] _[M]_[(] _[n]_[+1)][.] 

**Assumption A1** (exchangeability) **.** The random variables � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1][are][ex-] changeable. 

Following Rubin (1976), we consider three well-known missingness mechanisms. 

**Definition 7.2.1** (Missing Completely At Random (MCAR)) **.** For any _m ∈M_ , P ( _M_ = _m|X_ ) = P ( _M_ = _m_ ). 

**Definition 7.2.2** (Missing At Random (MAR)) **.** 

For any _m ∈M_ , P ( _M_ = _m|X_ ) = P � _M_ = _m|X_ obs( _m_ )�. 

**Definition 7.2.3** (Missing Non At Random (MNAR)) **.** If the missing data is not MAR, it is MNAR. Thus, its probability distribution depends on _X_ , including the missing values. 

**Impute-then-predict.** As most predictive algorithms can not directly handle missing values, we impute the incomplete data using an imputation function Φ which maps observed values to themselves and missing values to a function of the observed values. With notations from Le Morvan et al. (2021) we note _ϕ[m]_ : R _[|]_[obs(] _[m]_[)] _[|] →_ R _[|]_[mis(] _[m]_[)] _[|]_ the imputation function which takes as input observed values and outputs imputed values, i.e. 

_Chapter 7. Conformal Prediction with Missing Values_ 

140 

plausible values, given a mask _m ∈M_ . Then, the imputation function Φ belongs to _F[I]_ := �Φ : R _[d] × M →_ R _[d]_ : _∀j ∈_ �1 _, d_ � _,_ Φ _j_ ( _X, M_ ) = _Xj_ 1 _Mj_ =0 + _ϕ[M] j_ � _X_ obs( _M_ )� 1 _Mj_ =1� _._ Additionally, _F∞[I]_[is][the][restriction][of] _[F][I]_[to] _[C][∞]_[functions][which][include][deterministic] imputation, such as mean imputation or imputation by regression. The imputed data set is formed by the realizations of the _n_ random variables (Φ ( _X, M_ ) _, M, Y_ ). In practice, Φ is obtained as the result of an algorithm _I_ trained on �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)][��] _[n] k_ =1[+1][.] **Assumption A2** (Symmetrical imputation) **.** The imputation function Φ is the output of ( _d_ ) an algorithm _I_ treating its input data points symmetrically: _I_ (( _X_[(] _[σ]_[(] _[k]_[))] _, M_[(] _[σ]_[(] _[k]_[))] ) _[n] k_ =1[+1][)] = _I_ (( _X_[(] _[k]_[)] _, M_[(] _[k]_[)] ) _[n] k_ =1[+1][)] _[ conditionally on]_[(] _[X]_[(] _[k]_[)] _[, M]_[(] _[k]_[)][)] _[n] k_ =1[+1][and for any permutation] _[ σ]_[ on][ �][1] _[, n]_[+1][�][.] 

Assumption A2 is very mild and satisfied by all existing imputation methods for exchangeable data. In particular, it is valid for iterative regression imputation which allows out-of-sample imputation. 

**Background on (split) conformal prediction.** Split, or inductive, CP (SCP) (Papadopoulos et al., 2002; Lei et al., 2018) builds predictive regions by first splitting the _n_ points of the training set into two disjoint sets Tr _,_ Cal _⊂_ �1 _,_ n�, to create a _proper training set_ , Tr, and a _calibration set_ , Cal. On the proper training set, a model _f_[ˆ] (chosen by the user) is fitted, and then used to predict on the calibration set. _Conformity scores S_ Cal = _{_ ( _s_ ( _X_[(] _[k]_[)] _, Y_[(] _[k]_[)] )) _k∈_ Cal _}_ are computed to assess how well the fitted model _f_[ˆ] predicts the response values of the calibration points. For example, Conformalized Quantile Regression (CQR, Romano et al., 2019) fits two quantile regressions _q_ ˆlow and _q_ ˆupp, on the proper training ˆ set. The conformity scores are defined by _s_ ( _x, y_ ) = max(ˆ _q_ low( _x_ ) _− y, y − q_ upp( _x_ )). Finally, ˜ a corrected (1 _− α_ )-th quantile of these scores _Q_[�] 1 _−α_ ˜( _S_ Cal) is computed (called _correction term_ ) to define the predictive region: _C_[�] _α_ ( _x_ ) := _{y_ such that _s_ ( _y, f_[ˆ] ( _x_ )) _≤ Q_[�] 1 _−α_ ˜( _S_ Cal) _}_ .[1] An illustration of CQR is provided in Section 7.B. 

This procedure satisfies Eq. (7.1) for any _f_[ˆ] , any (finite) sample size _n_ , as long as the data points are exchangeable.[2] Moreover, if the scores are almost surely distinct, the coverage holds almost exactly: P( _Y ∈ C_[�] _α_ ( _X_ )) _≤_ 1 _− α_ + #Cal+11[.] 

For more details on SCP, we refer to Angelopoulos and Bates (2023); Vovk et al. (2005), as well as to Manokhin (2022). 

## **7.3 Warm-up: marginal coverage with** `NA` **s** 

A first idea to get valid predictive intervals _C_[�] _α_ ( _X, M_ ) in the presence of missing values _M_ is to apply CP in combination with impute-then-predict, which we refer to as _impute-thenpredict+conformalization_ . More details on this approach are given in Section 7.C.1 for both classification and regression tasks, although our main focus is regression. It turns out that such a simple approach is marginally (exactly) valid. 

> 1The correction _α → α_ ˜ is needed because of the inflation of quantiles in finite sample (see Lemma 2 in Romano et al. (2019) or Section 2 in Lei et al. (2018)). 

> 2Only the calibration and test data points need to be exchangeable. 

_7.4. Challenge:_ _`NA` s induce heteroskedasticity_ 

141 

**Definition 7.3.1** (Marginal validity) **.** A method outputting intervals _C_[�] _α_ is marginally valid if the following lower bound is satisfied, and exactly valid if the following upper bound is also satisfied: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0159-03.png)


Indeed, symmetric imputation preserves exchangeability. 

**Lemma 7.3.1** (Imputation preserves exchangeability) **.** _Let A1 hold. Then, for any missing mechanism, for any imputation function_ Φ _satisfying A2, the imputed random variables_ �Φ � _X_[(] _[k]_[)] _, M_[(] _[k]_[)][�] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1] _[are][exchangeable.]_ 

Note that if we replace A1 by an i.i.d. assumption, the imputed data set is only exchangeable but not i.i.d. without further assumptions on _I_ . Indeed, even simple mean imputation breaks independence. 

**Proposition 7.3.1** ((Exact) validity of impute-then-predict+conformalization) **.** _If A1 and A2 are satisfied, impute-then-predict+conformalization is marginally valid. If moreover the scores are almost surely distinct, it is exactly valid._ 

This is an important first positive result (proved in Section 7.C.2) showing that CP applied on an imputed data set has the same validity properties as on complete data, regardless of the missing value mechanism (MCAR, MAR or MNAR) and of the symmetric imputation scheme. Note that similar propositions could be derived for full CP (Vovk et al., 2005) and Jackknife+ (Barber et al., 2021b). 

Proposition 7.3.1 complements the work by Yang (2015), that also guarantees _marginal_ coverage for full CP, with the striking difference of having a complete training data. 

## **7.4 Challenge:** `NA` **s induce heteroskedasticity** 

To better understand the interplay between missing values and conditional coverage with respect to the mask, we consider an illustrative example of a Gaussian linear model. 

**Model 7.4.1** (Gaussian linear model) **.** The data is generated according to a linear model and the covariates are Gaussian conditionally to the pattern: 

- _Y_ = _β[T] X_ + _ε_ , _ε ∼N_ (0 _, σε_[2][)] _[ ⊥⊥]_[(] _[X, M]_[)][,] _[β][∈]_[R] _[d]_[.] 

- for all _m ∈M_ , there exist _µ[m]_ and Σ _[m]_ such that _X|_ ( _M_ = _m_ ) _∼N_ ( _µ[m] ,_ Σ _[m]_ ) _._ 

In particular, Model 7.4.1 is verified when _X_ is Gaussian and the missing data is MCAR. Model 7.4.1 is more general: it even includes MNAR examples (Ayme et al., 2022). 

**Proposition 7.4.1** (Oracle intervals) **.** _The oracle predictive interval is defined as the smallest valid interval knowing X_ obs( _M_ ) _and M . Under Model 7.4.1, its length only depends on the mask. For any m ∈M this oracle length is:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0159-17.png)


_See Section 7.D for the definition of µ[m]_ mis _|_ obs _[and]_[ Σ] _[m]_ mis _|_ obs _[and the quantiles of][ Y][ |]_[(] _[X]_[obs(] _[m]_[)] _[, M]_[=] _m_ ) _._ 

_Chapter 7. Conformal Prediction with Missing Values_ 

142 

Eq. (7.2) stresses that even when the noise of the generative model is homoskedastic, _missing values induce heteroskedasticity_ . Indeed, the covariance of the conditional distribution of _Y |_ ( _X_ obs( _m_ ) _, M_ = _m_ ) depends on _m_ . Furthermore, the uncertainty increases when missing values are associated with larger regression coefficients (i.e. the most predictive variables): if _β_ mis( _m_ ) is large, then _L[∗] α_[(] _[m]_[)][is][also][large,][as][Σ] _[m]_ mis _|_ obs[is] positive. In the extreme case where all the variables are missing, i.e. _m_ = (1 _, · · · ,_ 1), _L[∗] α_[(] _[m]_[) = 2] _[q]_ 1 _[N] −_[(0] _[α]_ 2 _[,]_[1)] ~~�~~ _β_ Σ _[m] β[T]_ + _σε_[2] = _q_ 1 _[Y] −[α]_ 2 _[−][q][Y][α]_ 2[.][On][the][contrary,][if] _[m]_[ = (0] _[,][ · · ·][ ,]_[ 0)][(that][is] all _Xj_ are observed), _β_ mis( _m_ ) is empty and _L[∗] α_[(] _[m]_[) = 2] _[q]_ 1 _[N] −_[(0] _[α]_ 2 _[,]_[1)] _σε_ = _q_ 1 _[ε] −[α]_ 2 _[−][q][ε][α]_ 2[.][We][illustrate] this induced heteroskedasticity and the impact of the predictive power in Figure 7.1a, and in Section 7.D along with a discussion emphasizing that even with the Bayes predictor for the conditional mean, mean-based CP does not yield intervals that are MCV. 

The above analysis motivates the following two design choices we make in this work. First, we advocate working with QR models rather than classic regression ones, as the former can handle heteroskedastic data. Second, we recommend providing the mask information to the model in addition to the input covariates, as the mask may further encourage the model to construct an interval with a length adaptive to the given mask. Therefore, we focus on CQR (Romano et al., 2019)[3] , an adaptive version of SCP, and concatenate the mask to the features. However, the predictive intervals of this procedure may not necessarily provide valid coverage conditionally on the masks, especially in finite samples as shown in Figure 7.1b (orange crosses). This is because the quality of the prediction at some ( _X, M_ ) depends strongly on _M_ , as there is an exponential number of patterns (2 _[d]_ ) for a finite training size, whereas the correction term is calculated independently of the masks. 

## **7.5 Achieving mask-conditional-validity (MCV)** 

We now aim at achieving _mask-conditional-validity_ (MCV) defined as follows using an ordering on the masks. 

˚ ˘ ˚ ˘ **Definition 7.5.1** (Included masks) **.** Let ( _m, m_ ) _∈M_[2] , _m ⊂ m_ if for any _j ∈_ �1 _, d_ � such ˚ ˘ ˘ ˚ that _mj_ = 1 then _mj_ = 1, i.e. _m_ includes at least the same missing values than _m_ . **Definition 7.5.2** (MCV) **.** A method is MCV if for any _m ∈M_ the following lower bound is satisfied, and exactly MCV if for any _m ∈M_ the following upper bound is also satisfied: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0160-07.png)


**On the relevance of MCV.** In a medical application context, it is very common to have missing data completely at random (MCAR) when a measurement device fails or the medical team forgot to fill out some forms. As a general rule, from an _equity standpoint_ , a patient whose data is missing should not be penalized (because of “bad luck”) by being 

> 3Note that our proposed framework is not based on CQR, this is only one instance of it. 

_7.5. Achieving mask-conditional-validity (MCV)_ 

143 

assigned a prediction interval that is less likely to include the true response than if the data were complete. 

Furthermore, the mask can also be linked to an external unobserved feature corresponding to a meaningful category. Consider the problem of predicting a disease among a population. Aggregating data from multiple hospitals with different practices and measurement devices can imply different features are observed for each patient. This can be viewed as a MCAR setting when _identically distributed_ patients[4] are assigned an hospital at random. Patterns are then linked to the cities, that themselves are related to socio-economical data. 

Overall, the missing patterns form _meaningful categories_ and _ensuring MCV yields more equitable treatment_ . Therefore, a method achieving marginal coverage by systematically failing on a given pattern, even in a MCAR setting, is not suitable. Finally, in non-MCAR cases, the pattern may be exactly related to critical discriminating features. 

## **7.5.1 Missing Data Augmentation (MDA)** 

To obtain a MCV procedure, we suggest modifying the calibration set according to the mask of the test point, while the training step is unchanged. More precisely, the mask of the test point is applied to the calibration set, as illustrated in Figure 7.2. The rationale is to mimic the missing pattern of the test point by artificially augmenting the calibration set with that mask. It ensures that the correction term is computed using data with (at least) the same missing values as the test point. We refer to this strategy as _CP with Missing Data Augmentation_ (CP-MDA), and derive two versions of it. Algorithms 12 and 13 are written using CQR as the base conformal procedure, but they work with any conformal method as we describe in Section 7.E.1. 

**Algorithm 12 – CP-MDA-Exact.** CP-MDA with _exact masking_ consists of keeping the _artificially_ masked calibration points (l. 7) that have exactly the same missing pattern as the test point (l. 5). Then Algorithm 12 performs as impute-then-predict+conformalization: impute the calibration set (l. 10), predict on it and get the calibration scores (l. 11), compute their quantile to obtain the correction term (l. 14), and finally impute and predict the test point with the fixed fitted model by adding and subtracting the correction term (l. 15) to 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0161-08.png)


**----- Start of picture text -----**<br>
CP-MDA with exact masking:<br>calibration set<br>-1 1<br>Test point 4 2<br>3 1<br>Initial calibration set 0 1<br>-1 -10 6 1 CP-MDA with nested masking:<br>4 -2 2 calibration set temporary test points<br>-1 1 3 1<br>5 1 1<br>4 2 3 1<br>0 1 and<br>5 3<br>0 1 3 1<br>**----- End of picture text -----**<br>


Figure 7.2: CP-MDA illustration. Augmented calibration set according to one test point. For CP-MDA-Nested, the augmented masks of the calibration set are also applied temporarily to the test point. 

> 4say, for example young children whose input/output distribution is _not_ dependent on the neighborhood. 

_Chapter 7. Conformal Prediction with Missing Values_ 

144 

**Algorithm 12** CP-MDA-Exact (with CQR) 

**Input:** Imputation algorithm _I_ , quantile regression algorithm _QR_ , significance level _α_ , training set �� _x_[(] _[k]_[)] _, m_[(] _[k]_[)] _, y_[(] _[k]_[)][��] _[n] k_ =1[,][test][point] � _x_[(][test][)] _, m_[(][test][)][�] **Output:** Prediction interval _C_[�] _α_ � _x_[(][test][)] _, m_[(][test][)][�] 

1: Randomly split _{_ 1 _, . . . , n}_ into 2 disjoint sets Tr & Cal 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0162-05.png)


- 4: Fit _QR_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0162-07.png)


// Generate an augmented calibration set: 5: Cal[(][test][)] = k _∈_ Cal such that m[(k)] _⊂_ m[(][test][)][�] � 

6: **for** _k ∈_ Cal[(][test][)] **do** 

� 7: _m_[(] _[k]_[)] = _m_[(][test][)] //Additional masking 8: **end for** Augmented calibration set generated. // 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0162-11.png)


12: **end for** 

13: Set _S_ = _{s_[(] _[k]_[)] _, k ∈_ Cal[(][test][)] _}_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0162-14.png)


the initial conditional quantile estimates. Note that Algorithm 12 is described for one test point for simplicity but extends easily to many test points. The computations are then shared: the training part (l. 1-4) is common to any test point and the correction term (l. 5-14) can be reused for any new test point with the same mask. 

In high dimensions, many calibration points may be discarded when applying CP-MDAExact since it is likely that their missing patterns would not be included in the one of the test point.[5] This limitation brings us to the second algorithm we propose, CP-MDA-Nested. 

**Algorithm 13 – CP-MDA-Nested.** CP-MDA with _nested masking_ avoids the removal of calibration points whose masks are not included in that of the test point. Instead, we apply the mask of the test point to the calibration points, and so we keep all the observations (l. 3). Next, we impute the masked calibration points (l. 6) before computing their scores _s_[(] _[k]_[)] (l. 7). Then, for each calibration point, the fitted quantile regressors are used to predict on the test point with a temporary mask, which matches the mask of the given augmented calibration point. These predictions are corrected with the score of the calibration point (l. 8-9) and stored in two bags _Z[α]_ 2[for][the][lower][interval][boundary,][and] _Z_ 1 _−[α]_[the][upper][interval][boundary][(l.][11][-][12][).][The][prediction][is][finally][obtained][by] 2[for] 

> 5Yet, these discarded points could be used for training but this comes at the cost of fitting a different model for each pattern; such a path is reasonable if the data is scarce. 

_7.5. Achieving mask-conditional-validity (MCV)_ 

145 

**Algorithm 13** CP-MDA-Nested (with CQR) 

**Input:** Same as Algorithm 12 **Output:** Same as Algorithm 12 1: Compute lines 1 to 4 of Algorithm 12 // Generate an augmented calibration set: 2: **for** _k ∈_ Cal **do** Additional nested masking � 3: _m_[(] _[k]_[)] = max( _m_[(][test][)] _, m_[(] _[k]_[)] ) 4: **end for** Augmented calibration set generated. // 5: **for** _k ∈_ Cal **do** 6: Impute the calibration set: _x_[(] imp _[k]_[)][:= Φ] � _x_[(] _[k]_[)] _, m_ �[(] _[k]_[)][�] 7: Set _s_[(] _[k]_[)] = max(ˆ _q[α]_ 2[(] _[x]_ imp[(] _[k]_[)][)] _[ −][y]_[(] _[k]_[)] _[, y]_[(] _[k]_[)] _[ −][q]_[ˆ][1] _[−][α]_ 2[(] _[x]_ imp[(] _[k]_[)][))] ˆ � 8: Set _z_[(] _α_ 2 _[k]_[)] = _q[α]_ 2 _[◦]_[Φ] � _x_[(][test][)] _, m_[(] _[k]_[)][�] _− s_[(] _[k]_[)] 9: Set _z_ 1[(] _[k] −_[)] _[α]_ 2[=] _[q]_[ˆ][1] _[−][α]_ 2 _[◦]_[Φ] � _x_[(][test][)] _, m_ �[(] _[k]_[)][�] + _s_[(] _[k]_[)] 10: **end for** 11: Set _Z[α] α[∈]_[Cal] _[}]_ 2[=] _[ {][z]_[(] 2 _[k]_[)] _[, k]_ 12: Set _Z_ 1 _−[α]_ 2[=] _[ {][z]_ 1[(] _[k] −_[)] _[α]_ 2 _[, k][∈]_[Cal] _[}]_ 13: Compute _Q_[�] _α_ ˜ _Z[α]_ � 2 � 14: Compute _Q_[�] 1 _−α_ ˜ _Z_ 1 _−[α]_ � 2 � 15: Set _C_[�] _α_ � _x_[(][test][)] _, m_[(][test][)][�] = [ _Q_[�] _α_ ˜ � _Z[α]_ 2 � ; _Q_[�] 1 _−α_ ˜ � _Z_ 1 _−[α]_ 2 �] 

taking the _α_ quantiles of the bags _Z_ (l. 13-15). 

The rationale for predicting on temporary test points with the mask of a given augmented calibration point is that we want to treat the test and calibration points in the same way.[6] We should note that this method may tend to achieve conservative coverage, since the augmented calibration set may have masks that overly include the missing pattern of the test point, i.e., the augmented points may have more missing values than the test point. 

## **7.5.2 Theoretical guarantees in finite sample** 

Let us consider the following assumptions. 

**Assumption A3** ( _Y_ is not explained by _M_ ) **.** ( _Y ⊥⊥ M_ ) _|X_ . 

**Assumption A4** (Stochastic domination of the quantiles) **.** Let ( _m,_ ˚ _m_ ˘ ) _∈M_[2] . If _m_ ˚ _⊂ m_ ˘ then for any _δ ∈_ [0 _,_ 0 _._ 5]: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0163-10.png)


A4 grasps the underlying intuition that the conditional distribution of _Y |_ ( _X_ obs( _m_ ) _, M_ = _m_ ) tends to have larger deviations when the number of observed variables is smaller, in concordance with the intuition that observing predictive variables reduce the conditional randomness of _Y |X_ obs. 

> 6This motivation is similar to the one of Jackknife+ (Barber et al., 2021b) and out-of-bags methods (Gupta et al., 2022). 

_Chapter 7. Conformal Prediction with Missing Values_ 

146 

The following theorems (proved in Section 7.E) state the finite sample guarantees of CP-MDA. 

**Theorem 7.5.1** (MCV of CP-MDA) **.** _Assume the missing mechanism is MCAR, and A1 to A3. Then:_ 

   _1. CP-MDA-Exact is MCV;_ 

   _2. if the scores are almost surely distinct, CP-MDA-Exact is exactly MCV;_ 

_3. if A4 also holds, CP-MDA-Nested is MCV, up to a technical minor modification of_ 

_the output._ 

The challenge in proving MCV of CP-MDA-Nested is that the augmented calibration and test points are not exchangeable conditional on the mask and thus may result in under-coverage. However, by imposing A4 we prove that this violation of exchangeability still leads to MCV (and often conservative MCV) (see Lemma 7.E.1). We conjecture that CP-MDA-Nested attains MCV (without any modification), as also supported by experiments. However, we could not prove it without making an independence assumption which we prefer to avoid as exchangeability is key to imputation methods. Instead, we prove in Theorem 7.E.2 the MCV of any variant outputting [ _Q_[�] _α_ ˜( _Z[m] α_[˜] _[Q]_[�][1] _[−][α]_[˜][(] _[Z]_ 1 _[m]_[˜] _−[α]_[for] _[Z][m] α_[˜] 2[);] 2[)]] 2 the subset of _Z[α]_[with][points][using][mask] _[m]_[˜][at][l.][6][-][9][.] 2[composed] 

**Theorem 7.5.2** (Marginal validity of CP-MDA) **.** _Under the same assumptions as Theorem 7.5.1 (i) CP-MDA-Exact is marginally valid; (ii) if A4 also holds, CP-MDA-Nested is marginally valid (with the same caveats as in Theorem 7.5.1)._ 

## **7.6 Towards asymptotic individualized coverage** 

Achieving validity conditionally on the mask is an important step towards conditional coverage: in practice one aims at the strongest coverage conditional on _both X_ and _M_ . Lei and Wasserman (2014); Vovk (2012); Barber et al. (2021a) studied a related question (without considering missing patterns) and concluded that it is impossible to achieve _informative_ intervals satisfying conditional coverage, P( _Y ∈ C_[�] _α_ ( _x_ ) _|X_ = _x_ ) _≥_ 1 _− α_ for any _x ∈X_ in the distribution-free and finite samples setting. Still, we can analyze the asymptotic regime, similarly to Theorem 1 of Sesia and Candès (2020), which proves the asymptotic conditional validity of CQR (without the presence of missing values) under consistency assumptions on the underlying quantile regressor. Here, by contrast, we study the asymptotic conditional validity of the impute-then-predict+conformalization procedure, by analyzing the consistency of impute-then-regress in Quantile Regression (QR). That is, we aim at showing that we satisfy the required assumption of consistency to invoke Theorem 1 of Sesia and Candès (2020). The proofs of this section are given in Section 7.F. 

To analyze the consistency of impute-then-predict procedures for QR, we extend the work of Le Morvan et al. (2021) on mean regression. QR with missing values, for a quantile level _β_ , aims at solving 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0164-12.png)


_7.7. Empirical study_ 

147 

with _ℓβ_ the pinball loss _ℓβ_ ( _y,_ ˆ _y_ ) = _ρβ_ ( _y − y_ ˆ) and _ρβ_ ( _u_ ) = _β|u|_ 1 _{u≥_ 0 _}_ + (1 _− β_ ) _|u|_ 1 _{u≤_ 0 _}_ . An associated _ℓβ_ -Bayes predictor minimizes Eq. (7.3). Its risk is called the _ℓβ_ -Bayes risk, noted _R[∗] ℓβ_[.][Impute-then-predict][procedure][in][QR][aims][at][solving] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0165-03.png)


for Φ any imputation. Let _gℓ[∗] β ,_ Φ _[∈]_[arg min] _g Rℓβ ,_ Φ( _g_ ). The following proposition states that _Rℓβ ,_ Φ( _gℓ[∗] β ,_ Φ[) =] _[ R][∗] ℓβ_[and][the][consistency][of][a][universal][learner.] 

**Proposition 7.6.1** ( _ℓβ_ -consistency of an universal learner) **.** _Let β ∈_ [0 _,_ 1] _. If X admits a density on_ R _[d] , then, for almost all imputation function_ Φ _∈F∞[I][,][(i)][g] ℓ[∗] β ,_ Φ _[◦]_[Φ] _[is][ℓ][β][-Bayes-] optimal (ii) any universally consistent algorithm for QR trained on the data imputed by_ Φ _is ℓβ-Bayes-consistent (i.e., asymptotically in the training set size)._ 

Note that this QR case does not require E � _ε|X_ obs( _M_ ) _, M_ � = 0, contrary to the quadratic loss case (Le Morvan et al., 2021). We conclude our asymptotic analysis of conditional coverage with Corollary 7.6.1. 

**Corollary 7.6.1.** _For any missing mechanism, for almost all imputation function_ Φ _∈F∞[I][,] if FY |_ ( _X_ obs( _M_ ) _,M_ ) _is continuous, a universally consistent quantile regressor trained on the imputed data set yields asymptotic conditional coverage._ 

In words, the intervals obtained by taking Bayes predictors of levels _α/_ 2 and 1 _− α/_ 2 are exactly valid conditionally to both the mask _M_ and the observed variables _X_ obs( _M_ ), if _FY |_ ( _X_ obs( _M_ ) _,M_ ) is continuous. Importantly, while this result is asymptotic, it holds for _any_ missing mechanism and it considers individualized conditional coverage. 

## **7.7 Empirical study** 

**Setup.** In all experiments, the data are imputed using iterative regression ( `iterative ridge` implemented in Scikit-learn, Pedregosa et al. (2011)).[7] We compare the performance of our CQR-MDA-Exact and CQR-MDA-Nested (that is CP-MDA based on CQR) to CQR as well as to a vanilla QR (without any calibration). The predictive models are fitted on the imputed data concatenated with the mask. Without concatenating the mask to the features, the mask-conditional coverage of QR is worsened, as demonstrated in Section 7.4. The prediction algorithm is a Neural Network (NN), fitted to minimize the pinball loss (Sesia and Romano, 2021, see Section 7.G.1 for details). For the vanilla QR, we use both the training and calibration sets for training. 

**Synthetic and semi-synthetic experiments.** We designed the training and calibration data to have 20% of MCAR values. To evaluate the test marginal coverage P( _Y ∈ C_[�] _α_ ( _X, M_ )), missing values are introduced in the test set according to the same distribution as on the training and calibration sets. Then, to compute an estimator of P( _Y ∈ C_[�] _α_ ( _X, m_ ) _|M_ = _m_ ) for each _m ∈M_ , we fix to a constant the number of observations 

> 7Theoretical results hold for any symmetric imputation. In practice, constant, mean and MICE imputations gave similar results. 

_Chapter 7. Conformal Prediction with Missing Values_ 

148 

per pattern, to ensure that the variability in coverage is not impacted by P ( _M_ = _m_ ). All experiments are repeated 100 times with different splits. 

## **7.7.1 Synthetic experiments: Gaussian linear data** 

**Data generation.** The data is generated with _d_ = 10 according to Model 7.4.1, with _X ∼ N_ ( _µ,_ Σ), _µ_ = (1 _, · · · ,_ 1) _[T]_ and Σ = _ϕ_ (1 _, · · · ,_ 1) _[T]_ (1 _, · · · ,_ 1)+(1 _−ϕ_ ) _Id_ , _ϕ_ = 0 _._ 8, Gaussian noise _ε ∼N_ (0 _,_ 1) and the following regression coefficients[8] _β_ =(1 _,_ 2 _,−_ 1 _,_ 3 _,−_ 0 _._ 5 _,−_ 1 _,_ 0 _._ 3 _,_ 1 _._ 7 _,_ 0 _._ 4 _,−_ 0 _._ 3) _[T] ._ Here, the oracle intervals are known (Proposition 7.4.1). 

**Lowest and highest mask coverage, and associated length.** Figures 7.1b and 7.8 (Section 7.G.2) and Figure 7.9 (Section 7.G.2) show the lowest and highest mask coverage and their associated length as a function of the training set size. The calibration size is fixed to 1000 and the test set contains 2000 points with the mask leading to the lowest coverage (here it corresponds to cases where only _X_ 4 is observed) and 2000 points with the mask leading to the highest coverage (here it corresponds to all the variables observed). These figures highlight that: 

- **CQR** and **QR** conditional coverage improve when the training size increases (Corollary 7.6.1); 

- **Both versions of CQR-MDA** are MCV (Theorem 7.5.1); 

- **CQR-MDA-Exact** is exactly MCV as highest and lowest mask coverage are exactly 90% (Theorem 7.5.1); 

- **CQR-MDA-Exact** ’s lengths converge to the oracle ones with increasing training size, showing it is not conservative, while **CQR-MDA-Nested** is overly conservative. 

**Coverage and length by mask size.** Figure 7.3 displays the average coverage and intervals’ length as a function of the pattern size, i.e., the performance metrics are aggregated by the masks with the same number of missing variables; the first violin plot of each panel corresponds to the marginal coverage (see Section 7.G.2 for QR results). Note that only the pattern sizes are presented and not the patterns themselves as there are 2 _[d]_ = 1024 possible masks.[9] For each pattern size, 100 observations are drawn according to the distribution of _M |_ size( _M_ ) in the test set. The training and calibration sizes are respectively 500 and 250 (Figure 7.11 contains the results for other sizes). Figure 7.3 shows that: 

- **CQR** is marginally valid (Proposition 7.3.1); 

- **CQR** and **QR** undercover with an increasing number of missing values. This can be explained because their length nearly does not vary with the size of the missing pattern, despite having the mask concatenated with the features; 

- **Both versions of CQR-MDA** are marginally valid (Th. 7.5.2) and mask(-size)conditionally-valid (Th. 7.5.1); 

> 8For dimension 3, in Figure 7.1a, the same model is used, keeping only the 3 first features and their associated parameters. 

> 9Note that in practice the relationship between the coverage and the number of missing values is not necessarily monotonic as a mask with only one missing value can lead to more uncertainty than a mask with many missing values, see Section 7.D. 

_7.7. Empirical study_ 

149 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0167-02.png)


**----- Start of picture text -----**<br>
CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 00<br>0 . 75<br>0 . 50<br>15 Oracle length<br>10<br>5<br>NANANANANANANANANANA NANANANANANANANANANA NANANANANA NANANANANA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg.<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 7.3: Average coverage (top) and length (bottom) as a function of the number of missing values ( `NA` ). The first violin plot shows the marginal coverage. #Tr = 500 and #Cal = 250. The marginal test set includes 2000 observations. The mask-conditional test set includes 100 individuals for each missing data pattern size. 

- **CQR-MDA-Exact** is exactly mask(-size)-conditionally-valid (Theorem 7.5.1) and its length is close to the oracle ones. It has more variability for the patterns with few missing values as for these masks Cal[(][test][)] is smaller. 

Similar experiments with 40% of missing values are available in Section 7.G.3. Briefly, it corresponds to a setting where CP-MDA-Nested is preferable over CP-MDA-Exact as the former outputs smaller intervals and is less variable. 

## **7.7.2 Semi-synthetic experiments** 

We consider 6 benchmark real data sets for regression: `meps_19` , `meps_20` , `meps_21` (MEPS), `bio` , `bike` and `concrete` (Dua and Graff, 2017), where we introduce missing values in their quantitative features, each of them having a probability 0.2 of being missing (i.e. it is a MCAR mechanism), as in the synthetic experiments. Note that therefore some patterns have a low (or null) frequency of appearance in the training sets of `bio` and `concrete` . The sample sizes for training, calibration, and testing, and simulation details are provided in Section 7.G.4, along with results for smaller training and calibration sets. 

Figure 7.4 depicts the results by combining _validity_ and _efficiency_ (length) for `meps_19` , `bio` , `concrete` , and `bike` , where this graph follows the visualization used in Zaffran et al. (2022). The results for `meps_20` and `meps_21` are given in Section 7.G.4, as they are similar to `meps_19` . Each of the panels in Figure 7.4 summarizes the results for one data set, with the average coverage shown in the _x_ -axis and the average length in the _y_ -axis. A method is mask-conditionally-valid if all the markers of its color are at the right of the vertical dotted line (90%). The design of Figure 7.4 requires a different interpretation than Figure 7.3 (or the subsequent Figure 7.5). For each method we report, for the pattern having the highest (or lowest) coverage, its length and coverage. However, as this pattern may depend on the method, the length for the highest/lowest should not be directly compared between methods. We observe that: 

_Chapter 7. Conformal Prediction with Missing Values_ 

150 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0168-02.png)


**----- Start of picture text -----**<br>
meps_19 ( d  = 139,  l  = 5) bio ( d  = 9, l  = 9) concrete ( d  = 8, l  = 8) bike ( d  = 18, l  = 4)<br>20 60<br>25<br>440<br>18<br>50<br>20<br>16 420<br>40<br>15<br>14 400<br>0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9 0 . 85 0 . 90<br>Average coverage Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 7.4: Validity and efficiency with missing values for 4 data sets (panels) with _d_ features, including _l_ quantitative ones in which missing values are introduced with probability 0.2. Colors represent the methods. Diamonds (♦) represent marginal coverage while the patterns giving the lowest and highest mask coverage are represented with triangles (▼ and ▲). Vertical dotted lines represent the target coverage. 

• **CQR** is marginally valid (orange ♦, Proposition 7.3.1), but not MCV as the lowest mask coverage (orange ▼) is far below 90% ( `bio` , `concrete` , and `bike` data sets); 

• **CQR-MDA-Exact** is marginally valid (purple ♦, Theorem 7.5.2). It is also exactly MCV, as the lowest (purple ▼) and highest (purple ▲) mask coverages are about 90% (Theorem 7.5.1); 

• **CQR-MDA-Nested** is marginally valid (blue ♦, Theorem 7.5.2). It is also MCV, as the lowest (blue ▼) mask coverage is larger than 90% (Theorem 7.5.1). 

## **7.7.3 Predicting the level of platelets for trauma patients** 

We study the applicability and robustness of CPMDA on the critical care TraumaBase® data. We focus on predicting the level of platelets of severely injured patients upon arrival at the hospital. This level is directly related to the occurrence of hemorrhagic shock and is difficult to obtain in real-time: predicting it accurately could be crucial to anticipate the need for transfusion and blood resources. In addition, this prediction task appears to be challenging as Jiang et al. (2022) achieved an average relative prediction error ˆ ( _∥y − y∥_[2] _/∥y∥_[2] ) that is no lower than 0.23. This highlights the need for reliable uncertainty 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0168-09.png)


**----- Start of picture text -----**<br>
CQR<br>1 . 8 CQR-MDA-Exact<br>CQR-MDA-Nested<br>1 . 6 Marginal<br>Mask-type<br>1 . 4<br>1 . 2<br>0 . 90 0 . 92 0 . 94<br>Average coverage<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 7.5: Average coverage and length on the TraumaBase® analysis. See the caption of Figure 7.4 for details. Other symbols than diamond correspond to computing the average per mask. Each individual’s prediction is obtained by using 15390 observations for training, and 7694 for calibration. 

_7.8. Conclusion and perspectives_ 

151 

quantification. 

After applying inclusion and exclusion criteria obtained by medical doctors and following the pipeline of Sportisse et al. (2020) described in Section 7.G.5, we left with a subset of 28855 patients and 7 features. Missing values vary from 0% to 24% by features, with a total average of 7%. 

**Results.** The results are summarized in Figure 7.5, where we use different markers to denote the different masks. To ensure a fair comparison between the conformal methods, we only keep the missing patterns for which there are more than 200 individuals; this excludes 7 patterns. Finally, since we found that the vanilla QR tends to be overly conservative, we refer to Section 7.G.5 for its results. Figure 7.5 shows that all conformal approaches achieve marginal coverage higher than the desired 90% level (diamonds ♦). Furthermore, for each mask (each set of linked markers) **CQR-MDA** improves coverage compared to **CQR** by approaching 90%, and efficiency by reducing the average length. Noticeably, for the pattern corresponding to all features observed (squares ■), **CQR-MDA** has a coverage rate above 90% while **CQR** is below the target level. Therefore, we believe **CQR-MDA** should be recommended as it improves upon the vanilla impute-then-regress+CQR approach. 

## **7.8 Conclusion and perspectives** 

In this paper, we study the interplay between uncertainty quantification and missing values. We show that missing values introduce heteroskedasticity in the prediction task. This brings challenges on how to provide uncertainty estimators that are valid conditionally on the missing patterns, which are addressed by this work. Our analysis leaves several directions open: (1) obtaining results _beyond the MCAR assumption_ for CP-MDA, both theoretically and numerically, (2) extending the (numerical) analysis to non-split approaches, (3) investigating the numerical performances of other conditional CP approaches (such as Sesia and Candès (2020); Izbicki et al. (2020, 2022); Lin et al. (2021)), (4) studying the impact of the imputation on QR with finite samples. A more detailed discussion on these directions is provided in Section 7.A. 

## **Appendix to Conformal Prediction with Missing Values** 

The appendices are organized as follows. 

Section 7.A provides a more detailed discussion on open directions and perspectives. Section 7.B describes CQR, used in the paper. 

Section 7.C provides an explicit description of impute-then-predict+conformalization 

(Section 7.C.1), along with its proof of validity, that is the proofs for Section 7.3 (Section 7.C.2). 

Then, Section 7.D contains the proofs for the Gaussian linear model oracle intervals presented in Section 7.4 (Section 7.D.1), along with the discussion on how mean-based approaches fail (Section 7.D.2). 

Section 7.E gives the general statement of CP-MDA-Exact (Section 7.E.1), and the proofs of the validity theorems for CP-MDA-Exact (Section 7.E.2), along with the theoretical study of CP-MDA-Nested (Section 7.E.3). 

Section 7.F provides all the proofs about consistency and asymptotic conditional coverage presented in Section 7.6. 

Finally, Section 7.G contains all the details for the experimental study and additional results completing Section 7.7. More precisely, Section 7.G.1 gives more details about the settings. Section 7.G.2 contains results on synthetic data with 20% of MCAR missing values, while Section 7.G.3 shows the results on synthetic data when the proportion of MCAR missing values is 40%. Section 7.G.4 describes the real data sets used for the semi-synthetic experiments, and presents the remaining results. Section 7.G.5 presents the real medical data set (TraumaBase®), the pipeline and settings used and the results obtained by QR on this data set. 

## **7.A Detailed perspective discussion** 

First, obtaining results _beyond the MCAR assumption_ for CP-MDA. On the numerical side, preliminary experiments show promising results, indicating CP-MDA’s robustness, but a detailed numerical study is needed. On the theoretical side, understanding the limits of CP-MDA validity is of high importance. Results without assumptions on the missingness distribution seem impossible to obtain. Even with MAR data, the task of pointwise prediction can be very challenging if the output distribution strongly depends on the pattern (Ayme et al., 2022). As the impossibility results of conditional validity (Lei and 

153 

_Chapter 7. Conformal Prediction with Missing Values_ 

154 

Wasserman, 2014; Vovk, 2012; Barber et al., 2021a), assumptions on the missing mechanism are needed. 

Second, extending the (numerical) analysis to non-split approaches (e.g., based on the Jackknife) would be relevant, as it could improve the base model and therefore how the heteroskedasticity is taken into account. Note that CP-MDA can be written to take into account this splitting strategy, and thus our theoretical results on MCV would directly extend. 

Third, investigating the numerical performances of other conditional CP approaches (such as Sesia and Candès (2020); Izbicki et al. (2020, 2022); Lin et al. (2021)) within the MDA framework is of interest. In this paper, we analyze empirically the instance of CP-MDA on top of CQR as it is the simplest version of QR based CP, but the theory and motivation of this work is not specific to CQR. Exactly as CQR, none of the aforementioned methods would provide MCV if used out of the box. But if combined with CP-MDA, then all of them will be granted MCV. 

Finally, while our approach is to be agnostic to the imputation chosen (similarly to CP being agnostic to the underlying model), an interesting research path is to study the impact of the imputation on QR with finite samples. 

## **7.B Illustration and details on CQR (Romano et al., 2019) procedure** 

Figure 7.6 provides a visualization and step by step description of CQR. 

_7.B. Illustration and details on CQR (Romano et al., 2019) procedure_ 

155 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0173-02.png)


**----- Start of picture text -----**<br>
Train Cal Test<br>2<br>0 ▶ Create a proper training set, a cal-<br>Step 1 ibration set, and keep the test set,<br>− 2 by randomly splitting the data set<br>− 4<br>0 2 4<br>X<br>2<br>0<br>On the proper training set:<br>Step 2 − 2 ▶ Learn (or get) q ˆlow and q ˆupp<br>− 4<br>0 2 4<br>X<br>+ + + + + + On the calibration set:<br>+ +<br>▶ Predict with q ˆlow and q ˆupp<br>Step 3 ▶ Get the scores s [(] [k] [)] (see below)<br>- - - 1<br>- - - + ▶ Compute the (1  − α )  ×  (1 + #Cal [)]<br>+<br>empirical quantile of the�  s [(] [k] [)] , noted<br>Q 1 −α ˆ ( S )<br>�→ s [(] [k] [)] := max q ˆlow x [(] [k] [)][�] − y [(] [k] [)] , y [(] [k] [)] − q ˆupp x [(] [k] [)][��]<br>� � �<br>2 On the test set:<br>0 ▶ Predict with q ˆlow and q ˆupp<br>Step 4 − 2 ▶ Buildˆ ˆ<br>Cα ˆ( x ) = q low( x )  − Q [�] 1 −α ˆ ( S );<br>�<br>− 4 ˆ<br>q upp( x ) + Q [�] 1 −α ˆ ( S )<br>0 2 4 �<br>X<br>Y<br>Y<br>Y<br>**----- End of picture text -----**<br>


Figure 7.6: Schematic illustration of Conformalized Quantile Regression (CQR) (Romano et al., 2019). 

_Chapter 7. Conformal Prediction with Missing Values_ 

156 

## **7.C Impute-then-predict+conformalization** 

## **7.C.1 Description of the algorithm** 

**Algorithm 14** SCP on impute-then-predict 

**Input:** Imputation algorithm _I_ , predictive algorithm _A_ , conformity score function _s_ , significance level _α_ , training set �� _X_[(1)] _, M_[(1)] _, Y_[(1)][�] _, · · · ,_ � _X_[(] _[n]_[)] _, M_[(] _[n]_[)] _, Y_[(] _[n]_[)][��] . **Output:** Prediction interval _C_[�] _α_ ( _X, M_ ). 

- 1: Randomly split _{_ 1 _, . . . , n}_ into two disjoint sets Tr and Cal. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0174-07.png)


- 7: **end for** 

- 8: Set _S_ Cal = _{S_[(] _[k]_[)] _, k ∈_ Cal _}_ 

- 9: Compute _Q_[�] 1 _−α_ SCP ( _S_ Cal), the 1 _− α_[SCP] -th empirical quantile of _S_ Cal, with 1 _− α_[SCP] := (1 _− α_ ) (1 + 1 _/_ #Cal). 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0174-11.png)


Similarly, Algorithm 12 can be written to include any underlying predictive algorithm (regression or classification) and any score function. 

## **7.C.2 Proof of exchangeability after imputation** 

In this subsection, we provide a more formal statement of Lemma 7.3.1 and Proposition 7.3.1 in respectively Lemma 7.C.1 and Proposition 7.C.1. To that end, we introduce a notion of symmetrical imputation _on a set T_ , for _T ⊂_ �1 _, n_ + 1�. 

**Assumption A5** (Symmetrical imputation on a set _T_ ) **.** 

For a given set of points _{X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] _}k∈T_ the imputation function Φ is the output of ( _d_ ) an algorithm _I_ that treats the data points in _T_ symmetrically: _I_ ( _{X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] _}k∈T_ ) = _I_ ( _{X_[(] _[σ]_[(] _[k]_[))] _, M_[(] _[σ]_[(] _[k]_[))] _, Y_[(] _[σ]_[(] _[k]_[))] _}_ ) _k∈T_ conditionally to _{X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] _}k∈T_ and for any permutation _σ_ on �1 _,_ # _T_ �. 

**Lemma 7.C.1** (Imputation preserves exchangeability) **.** _Let A1 hold. Then, for any missing mechanism, for any imputation function_ Φ _satisfying A5, the imputed random variables_ �Φ � _X_[(] _[k]_[)] _, M_[(] _[k]_[)][�] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈T[are][exchangeable.]_ 

**Proposition 7.C.1** ((Exact) validity of impute-then-predict+conformalization) **.** _If A1 is satisfied, then we have the following three results._ 

_1._ _**Full CP:** if A5 is satisfied for T_ = �1 _, n_ + 1� _(i.e., the imputation algorithm treats all points symmetrically), then impute-then-predict+Full CP is marginally valid. If moreover the scores are almost surely distinct, it is exactly valid._ 

_OR_ 

_7.D. Gaussian linear model_ 

157 

_2._ _**Jackknife+** if A5 is satisfied for T_ = �1 _, n_ + 1� _(i.e., the imputation algorithm treats all points symmetrically), then impute-then-predict+Jackknife+ is marginally valid (of level_ 1 _−_ 2 _α)._ 

_OR_ 

_3._ _**SCP** with the split_ �1 _, n_ + 1� = Tr[�] Cal[�] Test _and if A5 is satisfied for T_ = Cal[�] Test _(i.e., the imputation treats all points in_ Cal[�] Test _symmetrically) then impute-then-predict+conformalization is marginally valid. If moreover the scores are almost surely distinct, it is exactly valid._ 

_Remark_ 7.C.1 (Imputation choices for SCP) _._ In the latter case, for SCP, the coverage result can be derived conditionally on Tr, thus the coverage results holds for: (i) any deterministic imputation function (conditionally on Tr) (that is any arbitrary function of Tr), or (ii) any stochastic imputation function treating Cal and Test symmetrically (iii) any combination of both. 

_Proof of Lemma 7.C.1._ 

Φ is the output of an imputing algorithm _I_ trained on �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈T_ �. Assume � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈T_[are][exchangeable][(][A1][).] Thus, if _I_ treats the data points in _T_ symmetrically, �Φ( _X_[(] _[k]_[)] _, M_[(] _[k]_[)] ) _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈T_[are] exchangeable (see proof of Theorem 1b in (Barber et al., 2023) for example). 

_Proof of Proposition 7.C.1._ Proposition 7.C.1 is a consequence of Lemma 7.C.1 with different choices of _T_ , that enable to apply the following results: 

1. Full CP: Vovk et al. (2005), also re-stated in Barber et al. (2023) 

2. Jackknife+: Barber et al. (2021b) 

3. SCP: Lei et al. (2018) or Papadopoulos et al. (2002) and Angelopoulos and Bates (2023) for a generic version with any score function (note that the coverage is proved conditionally on Tr). 

## **7.D Gaussian linear model** 

## **7.D.1 Distribution of** _Y |_ ( _X_ obs( _m_ ) _, M_ ) **and oracle intervals** 

**Proposition 7.D.1** (Distribution of _Y |_ ( _X_ obs( _M_ ) _, M_ ) (Le Morvan et al., 2020b)) **.** _Under Model 7.4.1, for any m ∈{_ 0 _,_ 1 _}[d] :_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0175-15.png)


_with:_ 

_Chapter 7. Conformal Prediction with Missing Values_ 

158 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0176-02.png)


**Proposition 7.D.2** (Oracle intervals) **.** _Under Model 7.4.1, for any m ∈{_ 0 _,_ 1 _}[d] , for any δ ∈_ (0 _,_ 1) _:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0176-04.png)


_and the oracle predictive interval length is given by:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0176-06.png)


_Proof._ Using multivariate Gaussian conditioning (Eaton, 1983), for any subset of indices _L ∈_ �1 _, d_ �: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0176-08.png)


with _K_ = _L_[¯] (the complement indices) and: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0176-10.png)


Given that _Y_ = _β[T] X_ + _ε_ , with _ε ∼N_ (0 _, σε_[2][)] _[ ⊥⊥]_[(] _[X, M]_[)][,][the][following][holds:] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0176-12.png)


and by Equation (7.6), _βK[T][X][K][|]_[(] _[X][L][, M]_[)] _[∼N]_[(] _[β] K[T][µ][M] K|L[, β] K[T]_[Σ] _[M] K|L[β][K]_[)][,][and][(] _[ε][|]_[(] _[X][L][, M]_[))] _[∼] N_ (0 _, σε_[2][)][,][and][(] _[β] K[T][X][K][⊥⊥][ε]_[)] _[|]_[(] _[X][L][, M]_[)][.][Thus:] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0176-14.png)


Consequently, for any _δ ∈_ (0 _,_ 1): 

For any pattern _m ∈{_ 0 _,_ 1 _}[d]_ , applying Equation (7.7) with _K_ = mis( _m_ ) = obs( _m_ ), _L_ = obs( _m_ ), we have, for any _δ ∈_ (0 _,_ 1): 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0176-17.png)


and: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0176-19.png)


with: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0176-21.png)


_7.D. Gaussian linear model_ 

159 

## **7.D.2 Discussion on how mean-based approaches fail** 

Under Model 7.4.1, the Bayes predictor for a quadratic loss in presence of missing values – E � _Y |_ � _X_ obs( _M_ ) _, M_ �� – is fully characterized (Le Morvan et al., 2020b,a; Ayme et al., 2022). Figure 7.7 is obtained by generating the data according to Model 7.4.1 with _d_ = 3, _β_ = (1 _,_ 2 _, −_ 1) _[T]_ and _σε_ = 1, with multivariate Gaussian _X_ and MCAR mechanism ( _X ⊥⊥ M_ ) (which is a particular case of Model 7.4.1 with _µ[m] ≡ µ_ and Σ _[m] ≡_ Σ). The left panel represents the method _Oracle mean + SCP_ where SCP is applied on the regressor being the Bayes predictor for the mean with absolute residuals as the score function. The first violin plot represents the marginal coverage whereas the other 7 represent conditional coverage with respect to the different possible patterns: conditional on observing all the variables, on observing all the variables except _X_ 1, except _X_ 2 etc (see Section 7.7 for details on the simulation process). 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0177-04.png)


**----- Start of picture text -----**<br>
Marginal X 1 missing X 1 and X 2 missing<br>No missing values X 2 missing X 1 and X 3 missing<br>X 3 missing X 2 and X 3 missing<br>1 . 0<br>0 . 9<br>0 . 8<br>0 . 7<br>0 . 6<br>0 . 5<br>Oracle mean + SCP Oracle mean + SCP per pattern size<br>coverage<br>Average<br>**----- End of picture text -----**<br>


Figure 7.7: Calibration set contains 500 points. Test size for each pattern is of 500 individuals and for marginal is of 2000. 200 repetitions allow to display violin plots, the horizontal black line representing the mean. 

**SCP on a (oracle) mean regressor lacks of conditional coverage with respect to the mask.** Figure 7.7 (left) highlights that even with the best mean regressor (the Bayes predictor) and an homoskedastic noise, usual SCP intervals: 

- over-cover when there are no missing values; 

- cover less for a mask _m_ ˘ than for a mask _m_ ˚ when _m_ ˚ _⊂ m_ ˘ (e.g. _m_ ˚ = (1 _,_ 0 _,_ 0) only _X_ 1 is missing, _m_ ˘ = (1 _,_ 1 _,_ 0) that is _X_ 1 and _X_ 2 are missing); 

- cover less when the most informative variable ( _X_ 2) is missing. 

To tackle this issue, one could calibrate conditionally to the missing data patterns. This is in the same vein as calibrating conditionally to the categories of a categorical variable or to different groups (Romano et al., 2020a). This strategy is not viable as there are 2 _[d]_ patterns: the number of subsets grows exponentially with the dimension, implying the creation of subsets with too little data to perform the calibration. As an alternative, one could consider to perform calibration conditionally to the pattern size (e.g. when _d_ = 3, either 0 missing value, 1 or 2). This is possible as there are only _d_ different pattern sizes. 

_Chapter 7. Conformal Prediction with Missing Values_ 

160 

**Calibrating by pattern size does not provide validity conditionally to the missing data patterns.** Figure 7.7 (right) shows the coverages of _Oracle mean + SCP per pattern size_ where SCP is applied on the Bayes predictor for the mean and the calibration is protected by pattern size. The previous statements still hold with this strategy, even if the coverage disparities are smaller. Therefore, it is not enough to calibrate per pattern size. 

## **7.E Finite sample algorithms** 

## **7.E.1 General statement of Algorithm 12** 

We provide in Algorithm 15 a general statement of CP-MDA-Exact handling any learning algorithm (both regression and classification) and any score function. 

## **Algorithm 15** CP-MDA-Exact 

**Input:** Imputation algorithm _I_ , predictive algorithm _A_ , conformity score function _sg_ paramatrized by a model _g_ , significance level _α_ , training set �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][��] _[n] k_ =1[,] test point � _X_[(][test][)] _, M_[(][test][)][�] . **Output:** Prediction interval _C_[�] _α_ � _x_[(][test][)] _, m_[(][test][)][�] . 1: Randomly split _{_ 1 _, . . . , n}_ into two disjoint sets Tr and Cal. 2: Fit the imputation function: Φ( _·_ ) _←I_ ��� _X_[(] _[k]_[)] _, M_[(] _[k]_[)][�] _, k ∈_ Tr�� 3: Impute the training set: � _X_ imp[(] _[k]_[)] � _k∈_ Tr[:=] �Φ � _X_[(] _[k]_[)] _, M_[(] _[k]_[)][��] _k∈_ Tr ˆ 4: Fit algorithm _A_ : _g_ ( _·_ ) _←A_ ��� _X_ imp[(] _[k]_[)] _[, Y]_[(] _[k]_[)][�] _, k ∈_ Tr�� // Generate an augmented calibration set: 5: Cal[(][test][)] = k _∈_ Cal such that M[(k)] _⊂_ M[(][test][)][�] � 

- 6: **for** _k ∈_ Cal[(][test][)] **do** � 

- 7: _M_[(] _[k]_[)] = _M_[(][test][)] Additional masking 

- 8: **end for** Augmented calibration set generated. // 

9: Impute the calibration set: � _X_ imp[(] _[k]_[)] � _k∈_ Cal[(][test][)][:=] �Φ � _X_[(] _[k]_[)] _, M_[�][(] _[k]_[)][��] _k∈_ Cal[(][test][)] 10: **for** _k ∈_ Cal[(][test][)] **do** 11: Set _S_[(] _[k]_[)] = _sg_ ˆ � _Y_[(] _[k]_[)] _, X_ imp[(] _[k]_[)] �, the _conformity scores_ 

- 12: **end for** 

- 13: Set _S_ Cal = _{S_[(] _[k]_[)] _, k ∈_ Cal[(][test][)] _}_ ˜ ˜ 

- 14: Compute _Q_[�] 1 _−α_ ˜ ( _S_ Cal), the 1 _− α_ -th empirical quantile of _S_ Cal, with 1 _− α_ := (1 _− α_ ) (1 + 1 _/_ # _S_ Cal). 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0178-13.png)


## **7.E.2 Mask-conditional valitidy of CP-MDA-Exact** 

Before proving the results, we introduce a slightly stronger notion of mask-conditionalvalidity, when the calibration set is itself of random cardinality. 

**Definition 7.E.1** (Mask-conditional-validity-random-calibration-size) **.** A method is maskconditionally-valid with a random calibration size #Cal if for any _m ∈M_ , the lower bound is satisfied, and exactly mask-conditionally-valid if for any _m ∈M_ , 1 _≤ c ≤ n_ , the upper 

_7.E. Finite sample algorithms_ 

161 

bound is also 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0179-03.png)


We start by proving Theorem 7.E.1 that implies the result on CP-MDA-Exact in Theorem 7.5.1. 

**Theorem 7.E.1.** _[Conditional validity of CP-MDA-Exact with calibration of random cardinality] Assume the missing mechanism is MCAR, and that Assumptions A1 to A3 hold. Then:_ 

> _• CP-MDA-Exact is valid with a random calibration size_ #Cal _conditionally to the missing patterns;_ 

_• if the scores S_[(] _[k]_[)] _are almost surely distinct, CP-MDA-Exact is exactly mask-conditionallyvalid with a random calibration size_ #Cal _._ 

_Proof of Theorem 7.E.1._ Let Tr and Cal be two disjoint sets on �1 _, n_ �. Let ˆ _g_ be some model. Given A1, the sequence �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[,]_ � _X_[(test)] _, M_[(test)] _, Y_[(test)][��] is exchangeable. Therefore, the sequence �� _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[,]_ � _X_[(test)] _, Y_[(test)][��] is also exchangeable. Let _m_ in _M_ . We define Cal _[m]_ = � _k ∈_ Cal such that M[(k)] _⊂_ m�. Let _c ∈_ �1 _,_ #Cal�. 

As the _M ⊥⊥ X_ (missingness is MCAR) and ( _M ⊥⊥ Y_ ) _|X_ (Assumption A3), then _M ⊥ ⊥_ ( _X, Y_ ), and #Cal _[m] ⊥⊥_ � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[,]_ � _X_[(test)] _, Y_[(test)][�] . It follows that the sequence �� _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[m][ ,]_ � _X_[(test)] _, Y_[(test)][��] is exchangeable conditionally to #Cal _[m]_ = _c_ . Similarly, _M_[(test)] _⊥⊥_ � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[,]_ � _X_[(test)] _, Y_[(test)][�] . Thus the sequence _{_ � _X_[(] _[k]_[)] _, M_[(test)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[m][ ,]_ � _X_[(test)] _, M_[(test)] _, Y_[(test)][�] _}_ is exchangeable conditionally to #Cal _[m]_ = _c_ and _M_[(test)] = _m_ . 

Therefore, we can now invoke Proposition 7.3.1 in combination with Lemma 1 of Romano et al. (2020a) to conclude the proof. But we can state a more rigorous version here, since in fact Cal _[m]_ is a random variable (as discussed in Definition 7.E.1). 

Since the algorithm _I_ treats the calibration and test data points symmetrically (A5 with _T_ = Cal[�] Test), A5 also holds for any _T[′] ⊂T_ . Therefore, by Lemma 7.C.1 the sequence ��Φ( _X_[(] _[k]_[)] _, M_[(test)] ) _, M_[(test)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[m][ ,]_ �Φ( _X_[(test)] _, M_[(test)] ) _, M_[(test)] _, Y_[(test)][��] is exchangeable conditionally to #Cal _[m]_ = _c_ and _M_[(test)] = _m_ . 

The conclusion follows from usual arguments (Papadopoulos et al., 2002; Lei et al., 2018; Angelopoulos and Bates, 2023). Precisely, �� _sg_ ˆ( _Y_[(] _[k]_[)] _,_ Φ( _X_[(] _[k]_[)] _, M_[(test)] ))� _k∈_ Cal _[m][ , s][g]_[ˆ][(] _[Y]_[(test)] _[,]_[ Φ(] _[X]_[(test)] _[, M]_[(test)][))] � is exchangeable conditionally to #Cal _[m]_ = _c_ and _M_[(test)] = _m_ . Therefore, 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0179-13.png)


_Chapter 7. Conformal Prediction with Missing Values_ 

162 

and if the �� _sg_ ˆ( _Y_[(] _[k]_[)] _,_ Φ( _X_[(] _[k]_[)] _, M_[(test)] ))� _k∈_ Cal _[m][ , s][g]_[ˆ][(] _[Y]_[(test)] _[,]_[ Φ(] _[X]_[(test)] _[, M]_[(test)][))] � are almost surely distinct (i.e. have a continuous distribution) then (Lei et al., 2018; Romano et al., 2019): 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0180-03.png)


This proves the first two points (with respect to Definition 7.E.1) of Theorem 7.5.1, by observing that 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0180-05.png)


Then, the proof of Theorem 7.5.2 (marginal validity of the CP-MDA-Exact) is direct by marginalizing the result of Theorem 7.5.1. 

## **7.E.3 Validities of CP-MDA-Nested.** 

Next, we give more details on the results on CP-MDA-Nested. 

## 7.E.3.1 Mask-conditional-validity of CP-MDA-Nested. 

Let _m ∈M_ . 

We start by describing the links between CP-MDA-Nested and CP-MDA-Exact. CPMDA-Exact can be re-written in the same way as CP-MDA-Nested, but keeping the subselection step of l. 5. 

Indeed, first mention that the output of Algorithm 12 can be written in the following ways: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0180-13.png)


With _Z[m] α α[∈]_[Cal][and][M][�][(k)][= m] _[}]_[,][and][similarly][for][the][upper][bag.][Recall][that] 2[:=] _[ {][z]_[(] 2 _[k]_[)] _[, k]_ ˆ � we have: _z_[(] _α_ 2 _[k]_[)] = _q[α]_ 2 _[◦]_[Φ] � _x_[(][test][)] _, m_[(] _[k]_[)][�] _− s_[(] _[k]_[)] _._ 

On the other hand, the output predictive interval of Algorithm 13 is then written as: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0180-16.png)


_7.E. Finite sample algorithms_ 

163 

With these notations, _Z[α]_[be][partitioned][as] 2[can] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0181-03.png)


With 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0181-05.png)


The result of Algorithm 12 implies that for any mask _m ∈M_ , we have : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0181-07.png)


i.e. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0181-09.png)


Where: _Q_ 1 _−α_ ˜ ( _S_ ) is the (1 _−α_ )(1+1 _/_ # _S_ )-quantile of _S_ and _S[m]_ = _{s_[(] _[k]_[)] for _k ∈_ Cal and M[�][(k)] = m _}_ . Equivalently: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0181-11.png)


In the following Lemma, we show that for _m_ ˜ _⊃ m_ the result extends under Assumption A4. 

˜ **Lemma 7.E.1.** _Assume Assumption A4. For any m ∈M, for any m ⊃ m_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0181-14.png)


_This inequality shows the conservativeness of the quantiles of the bags resulting from larger_ ˜ _missing patterns m than m when the construction of the output of Algorithm 13._ 

_While inequality Equation_ (7.11) _is “tight” in the sense that the probability is almost exactly_ 1 _− α (item 2 of Theorem 7.5.1), the proof hereafter shows that Equation_ (7.12) _can be pessimistic in terms of actual coverage, as one may have_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0181-17.png)


_More precisely, we have the following inequality:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0181-19.png)


_Chapter 7. Conformal Prediction with Missing Values_ 

164 

The interpretation of that Lemma is that the intervals resulting from the prediction on _x_[test] _, m_ ˜ (more data hidden) and corrected with the residuals of the calibration points ˜ ( _X[k] , M[k]_ = _m, Y[k]_ ) have a _larger_ probability of containing _Y_[test] , conditionally to _X_ obs( _m_ ) than the interval built using prediction on _x_[test] _, m_ (more data available) and corrected with the residuals of the calibration points ( _X[k] , M[k]_ = _m, Y[k]_ ) (more data available) 

˜ _Proof of Lemma 7.E.1._ We start by invoking Equation (7.10) for _m_ : 

ˆ ˜ P � _Y_[(test)] _∈/_ � _q[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][)] _[ −][Q]_[�][1] _[−][α]_[˜] � _S[m]_[˜][�] ; ˆ _q_ 1 _−[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][) +] _[Q]_[�][1] _[−][α]_[˜] � _S[m]_[˜][��] _|M_[(test)] = _m_ � _≤ α._ (7.14) 

Consequently, by the tower property of conditional expectations: 

E �P � _Y_[(test)] _∈/_ � _q_ ˆ _[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][)] _[ −][Q]_[�][1] _[−][α]_[˜] � _S[m]_[˜][�] ; ˆ _q_ 1 _−[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][) +] _[Q]_[�][1] _[−][α]_[˜] � _S[m]_[˜][�����] � _M_[(test)] = _m, S_ ˜[( ˜] _[m]_[)] _, X_ obs( ˜[(test)] _m_ )����� _M_ (test) = _m_ ˜ � _≤ α ._ (7.15) 

ˆ ˜ Observe that _q[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][)] _[ −][Q]_[�][1] _[−][α]_[˜] � _S[m]_[˜][�] is _{M_[(test)] = _m, S_[( ˜] _[m]_[)] _, X_ obs( ˜[(test)] _m_ ) _[}]_[-measurable.] Moreover, by Assumption A4, we have that for any _δ ∈_ [0 _,_ 0 _._ 5]: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0182-08.png)


� In other words the conditional distribution of _Y_ given _X_ obs( � _m_ ) and _M_ = _m_ “stochastically dominates” the conditional distribution of _Y_ given _X_ obs( _m_ ) and _M_ = _m_ . 

We thus have, with _FZ_ denoting the cumulative distribution function of� _Z_ : _FY |_ ( _X_ obs( _m_ � ) _[,M]_[=][ �] _[m]_[)] the cumulative distribution function of _Y |_ ( _X_ obs( � _m_ ) _, M_ = _m_ ): 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0182-11.png)


ˆ _m_ At (i) we use (7.17) _FY |_ ( _X_ obs( _m_ ) _,M_ = _m_ )( _q[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][)] _[−][Q]_[�][1] _[−][α]_[˜][(] _[S]_[˜] )) _≤ FY |_ ( _X_ obs( _m_ �) _[,M]_[=][ �] _m_ )[(] _[q]_[ˆ] _[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][)] _[−] Q_ �1 _−α_ ˜( _Sm_[˜] )), and (7.16): _FY |_ ( _X_ obs( _m_ ) _,M_ = _m_ )( _q_ ˆ1 _− α_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][) +] _[Q]_[�][1] _[−][α]_[˜][(] _[S] m_[˜] )) _≥ FY |_ ( _X_ obs( _m_ �) _[,M]_[=][ �] _m_ )[(] _[q]_[ˆ] 1 _−[α]_ 2 _[◦]_ Φ( _X_[(test)] _, m_ ˜ )+ _Q_[�] 1 _−α_ ˜( _Sm_[˜] )) by A4. Remark that here we assume that � _q_ ˆ1 _−[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][) +] _[Q]_[�][1] _[−][α]_[˜][(] _[S]_[ ˜] _[m]_[)] � _≥_ ˆ median� (Y[(test)] _|_ (X[(test)] obs(m)� _[,]_[ M =][˜m][)][ and] � _q[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][)] _[ −][Q]_[�][1] _[−][α]_[˜][(] _[S]_[ ˜] _[m]_[)] � _≤_ median(Y[test] _|_ (X[(test)] obs(m)� _[,]_[ M =] m). 

We obtain Equation (7.13) in Lemma 7.E.1 by plugging (7.18) in (7.15), then Equation (7.12) by the tower property. 

**Theorem 7.E.2.** _Assume the missing mechanism is MCAR, and that Assumptions A1 to A3 hold. Additionally Assumption A4 is satisfied._ 

_Consider the partition described in Equation_ (7.8) _, and consider CP-MDA-Nested running on a test point with missing pattern m_[(test)] _, with any of the following outputs, instead of l. 15 C_[�] _α_ � _x_[(] _[test]_[)] _, m_[(] _[test]_[)][�] = [ _Q_[�] _α_ ˜ � _Z[α]_ 2 � ; _Q_[�] 1 _−α_ ˜ � _Z_ 1 _−[α]_ 2 �] _:_ 

_7.F. Infinite data results_ 

165 

_1. C_[�] _α_ � _x_[(] _[test]_[)] _, m_[(] _[test]_[)][�] = [ _Q_[�] _α_ ˜( _Z[m] α_ 2[˜][);] _[Q]_[�][1] _[−][α]_[˜][(] _[Z]_ 1 _[m]_[˜] _−[α]_ 2[)]] _[where][m]_[˜] _[⊃][m]_[(test)] _[is][an][arbitrary] choice._ 

_2. C_[�] _α_ � _x_[(] _[test]_[)] _, m_[(] _[test]_[)][�] = [ _Q_[�] _α_ ˜( _Z[m] α_ 2[ˆ][);] _[Q]_[�][1] _[−][α]_[˜][(] _[Z]_ 1 _[m]_[ˆ] _−[α]_ 2[)]] _[where][m]_[ˆ] _[is][a][randomly][selected][pattern] in {_ ˜ _m, m_ ˜ _⊃ m_[(test)] _}, possibly with varying probability depending on the cardinality of the sets Z[m]_[˜] _α/_ 2 _[.]_ 

_Then the resulting algorithm is mask-conditionally-valid._ 

_Proof of Theorem 7.E.2._ The proof immediately follows from Equation (7.12), and gives the result without difficulty for any arbitrary pattern or random variable independent of all other randomness. 

Extension to a choice that involves the cardinality of the sets _Zα/[m]_[˜] 2[,][leveraging][the] independence between these cardinals and the coverage properties (same as in the proof of Theorem 7.E.1). 

Then, the proof of Theorem 7.5.2 (marginal validity of the CP-MDA-Nested) is direct by marginalizing the result of Theorem 7.E.2. 

## **7.F data results** 

**Proposition 7.6.1 (** _ℓβ_ **-consistency of an universal learner).** _Let β ∈_ [0 _,_ 1] _. If X admits a density on X , then, for almost all imputation function_ Φ _∈F∞[I][,][the][function] gℓ[∗] β ,_ Φ _[◦]_[Φ] _[is][Bayes][optimal][for][the][pinball][risk][of][level][β][.]_ 

_Proof of Proposition 7.6.1._ The proof starts in the exact same way than Le Morvan et al. (2021), based on their Lemmas A.1 and A.2. For completeness, we copy here the statements of these lemmas without their proof and rewrite the two first parts of the main proof. 

Let Φ be an imputation function such that for each missing data pattern _m_ , _ϕ[m] ∈ C[∞]_[�] R _[|]_[obs(] _[m]_[)] _[|] ,_ R _[|]_[mis(] _[m]_[)] _[|]_[�] . 

**Lemma 7.F.1** (Lemma A.1 in Le Morvan et al. (2021)) **.** _Let ϕ[m] ∈C[∞]_[�] R _[|]_[obs(] _[m]_[)] _[|] ,_ R _[|]_[mis(] _[m]_[)] _[|]_[�] _be the imputation function for missing data pattern m, and let M[m]_ = � _x ∈_ R _[d]_ : _x_ mis( _m_ ) = _ϕ[m]_[ �] _x_ obs(( _m_ ))�� _. For all m, M[m] is an |_ obs(( _m_ )) _|dimensional manifold._ 

In Lemma 7.F.1, _M[m]_ represents the manifold in which the data points are sent once imputed by _ϕ[m]_ . Lemma 7.F.1 states that this manifold is of dimension _|_ obs( _m_ ) _|_ . 

**Lemma 7.F.2** (Lemma A.2 in Le Morvan et al. (2021)) **.** _Let m and m[′] be two distinct missing data patterns with the same number of missing (resp. observed) values |_ mis _| (resp |_ obs _|). Let ϕ[m] ∈C[∞]_[�] R _[|]_[obs(] _[m]_[)] _[|] ,_ R _[|]_[mis(] _[m]_[)] _[|]_[�] _be the imputation function for missing data pattern m, and let M[m]_ = � _x ∈_ R _[d]_ : _x_ mis( _m_ ) = _ϕ[m]_[ �] _x_ obs( _m_ )�� _. We define similarly_ Φ[(] _[m][′]_[)] _and M_[(] _[m][′]_[)] _. For almost all imputation functions ϕ[m] and_ Φ[(] _[m][′]_[)] _,_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0183-15.png)


_Chapter 7. Conformal Prediction with Missing Values_ 

166 

Note that, as by Lemma 7.F.1 dim ( _M[m]_ ) = dim _M_[(] _[m][′]_[)][�] = _|_ obs _|_ = _d−|_ mis _|_ , Lemma 7.F.2 � states that dim _M[m] ∩M_[(] _[m][′]_[)][�] _≤_ dim ( _M[m]_ ) = dim _M_[(] _[m][′]_[)][�] . � � Now, to prove Proposition 7.6.1 the missing data patterns are ordered as in Le Morvan et al. (2021): the first one will be the one in which all the variables are missing, while the last one will be the one in which all the variables are observed. For two data patterns with the same number of missing variables, the ordering is picked at random. We denote by _m_ ( _i_ ) the _i_ -th missing data pattern according to this ordering. 

We are going to build a function _g_ Φ which, composed with Φ, will reach the _ℓ_ -Bayes risk. 

For each missing data pattern, and starting by _m_ (1) of all variables missing, we can define _g_ Φ on the data points from the current missing data pattern. More precisely, for each _i_ , _g_ Φ is built for every imputed data point belonging to _M_[(] _[m]_[(] _[i]_[))] except for those already considered in previous steps (one imputed data point can belong to multiple manifolds): 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0184-05.png)


That is, _g_ Φ _◦_ Φ( _X, M_ ) will equal _f_[˜] _[∗]_ ( _X, M_ ) except possibly if Φ( _X, M_ ) = Φ( _Y_[˜] ) for some _Y_[˜] that has more missing values than _X, M_ . Therefore, for each missing data pattern _m_ ( _i_ ), _g_ Φ _◦_ Φ equals _f_[˜] _[∗]_ except on[�] _k<i[M]_[(] _[m]_[(] _[k]_[))][.][The][question][that][remains][is:] what is the dimension of _M_[(] _[m]_[(] _[i]_[))][ ���] _k<i[M]_[(] _[m]_[(] _[k]_[))][�] , these points for which there is no necessarily equality between _g_ Φ _◦_ Φ and _f_[˜] _[∗]_ . First, note that _M_[(] _[m]_[(] _[i]_[))][ ���] _k<i[M]_[(] _[m]_[(] _[k]_[))][�] = � _k<i_ � _M_[(] _[m]_[(] _[i]_[))][ �] _M_[(] _[m]_[(] _[k]_[))][�] . For each space in this reunion, there are two cases: 

- either _|_ obs( _m_ ( _k_ )) _|< |_ obs( _m_ ( _i_ )) _|_ : using Lemma 7.F.1, dim � _M_[(] _[m]_[(] _[k]_[))][�] = _|_ obs( _m_ ( _k_ )) _|< |_ obs( _m_ ( _i_ )) _|_ = dim � _M_[(] _[m]_[(] _[i]_[))][�] . Thus, _M_[(] _[m]_[(] _[i]_[))][ �] _M_[(] _[m]_[(] _[k]_[))] is of measure zero in _M_[(] _[m]_[(] _[i]_[))] . 

- either _|_ obs( _m_ ( _k_ )) _|_ = _|_ obs( _m_ ( _i_ )) _|_ : using Lemma 7.F.2, _M_[(] _[m]_[(] _[i]_[))][ �] _M_[(] _[m]_[(] _[k]_[))] is of dimension 0 or smaller than dim � _M_[(] _[m]_[(] _[i]_[))][�] , thus it is of measure zero in _M_[(] _[m]_[(] _[i]_[))] . 

Therefore, the set of data points for which _g_ Φ _◦_ Φ does not equal the oracle is of measure 0 for each missing data pattern. 

Let _β ∈_ [0 _,_ 1]. We can now write down the _ℓβ_ -risk of this built function: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0184-11.png)


where ( _i_ ) holds thanks to the shape of _ρβ_ . For any _w ∈_ R and any _λ ∈_ R+: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0184-13.png)


_7.F. Infinite data results_ 

167 

Furthermore, _ρβ_ is convex, thus for any ( _u, v_ ) _∈_ R[2] : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0185-03.png)


> As _f_[˜] _[∗]_ and _g[∗] ◦_ Φ are equals almost everywhere on each missing subspace, it holds that 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0185-05.png)


Indeed, decomposing by pattern one can write: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0185-07.png)


and thus by equality almost everywhere for each pattern every term in this sum is null. Therefore one obtains: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0185-09.png)


Thus: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0185-11.png)


and _g[∗] ◦_ Φ is Bayes optimal. This implies that _R[∗] ℓβ ,_ Φ[=] _[ R][∗] ℓβ_[.][Thus,][a][universally][consistent] algorithm learning _g_ Φ chained with Φ will lead to a Bayes consistent function. 

_Proof of Corollary 7.6.1._ Corollary 7.6.1 states that “For any missing mechanism, for almost all imputation function Φ _∈F∞[I]_[,][if] _[F] Y |_ ( _X_ obs( _M_ ) _,M_ )[is][continuous,][a][universally][consistent] quantile regressor trained on the imputed data set yields asymptotic conditional coverage.”. Let _β ∈_ [0 _,_ 1]. 

Remark that Proposition 7.6.1 states that for any missing mechanism, for almost all imputation function Φ _∈F∞[I]_[a][universally][consistent][quantile][regressor][trained][on][the] imputed data set achieves the Bayes risk asymptotically. We will thus show that any _ℓβ_ -Bayes predictor _fβ[∗]_[(any][function][achieving][the] _[ℓ][β]_[-Bayes-risk)][is][such][that][P][(] _[Y][≤] fβ[∗]_[(] _[X, M]_[)] _[|][X]_[obs(] _[M]_[)] _[, M]_[)][=] _[β]_[if] _[F][Y][ |]_[(] _[X]_ obs( _M_ ) _[,M]_[)][is][continuous.] Therefore, any two Bayes predictors _fα/[∗]_ 2[and] _[f]_ 1 _[∗] −α/_ 2[form][an][interval][[] _[f] α/[∗]_ 2[(] _[X, M]_[);] _[ f]_ 1 _[∗] −α/_ 2[(] _[X, M]_[)]][that][achieves] conditional coverage (conditionally to _X_ obs( _M_ ) and _M_ ). 

Let _fβ[∗]_[be][a] _[ℓ][β]_[-Bayes][predictor.][Then:] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0185-16.png)


_Chapter 7. Conformal Prediction with Missing Values_ 

168 

Let ( _x, m_ ) _∈X × M_ . Denote _Hx,m_ ( _z_ ) := E � _ρβ_ ( _Y − z_ ) _|X_ obs( _M_ ) = _x_ obs( _m_ ) _, M_ = _m_ �. As _Y_ = _z_ almost surely, we have: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0186-03.png)


Therefore _Hx,m[′]_[(] _[z]_[)] _[ ≤]_[0][if][and][only][if] _[β][≤]_[P] � _Y ≤ z|X_ obs( _M_ ) = _x_ obs( _m_ ) _, M_ = _m_ �. Thus, _z_ minimizes _Hx,m_ if and only if _β_ = P � _Y ≤ z|X_ obs( _M_ ) = _x_ obs( _m_ ) _, M_ = _m_ �. 

If _FY |_ ( _X_ obs( _M_ ) _,M_ ) is continuous, there exists at least a solution, that might not be unique if it is not additionally strictly increasing. Therefore, if _FY |_ ( _X_ obs( _M_ ) _,M_ ) is continuous, all the _ℓβ_ -Bayes predictors can be written as _fβ[∗]_[(] _[x, m]_[) =] _[ q][x,m]_[with] 

P � _Y ≤ qx,m|X_ obs( _M_ ) = _x_ obs( _m_ ) _, M_ = _m_ � = P � _Y ≤ fβ[∗]_[(] _[x, m]_[)] _[|][X]_ obs( _M_ )[=] _[ x]_ obs( _m_ ) _[, M]_[=] _[ m]_ � = _β._ 

## **7.G Experimental study** 

## **7.G.1 Settings detail** 

**Quantile Neural Network.** The architecture and optimization of the Quantile Neural Network used in the experiments is taken from Sesia and Romano (2021) (their code is freely available). This is the description provided in the original paper of the neural network: “The network is composed of three fully connected layers with a hidden dimension of 64, and ReLU activation functions. We use the pinball loss to estimate the conditional quantiles, with a dropout regularization of rate 0.1. The network is optimized using Adam Kingma and Ba (2014) with a learning rate equal to 0.0005. We tune the optimal number of epochs by cross validation, minimizing the loss function on the hold-out data points; the maximal number of epochs is set to 2000.” 

## **7.G.2 Gaussian linear results** 

Figure 7.9 is the analogous of Figure 7.8, but by evaluating the performances on the mask leading to the highest coverage. 

Hereafter, we present in Figure 7.10 the exact same figure than Figure 7.3 but with a panel (the first) for vanilla QR. The 3 other methods are displayed again to facilitate the comparison. 

Finally, Figure 7.11 is the analogous of Figure 7.10, but for a training set containing 1000 observations and a calibration set containing 500 observations. 

_7.G. Experimental study_ 

169 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0187-02.png)


**----- Start of picture text -----**<br>
15 . 0<br>0 . 8<br>12 . 5 QR<br>CQR<br>0 . 6 10 . 0 CQR-MDA-exact<br>CQR-MDA-nested<br>7 . 5<br>Oracle<br>0 . 4<br>5 . 0<br>0 . 2 2 . 5<br>Training size Training size<br>50 100 500 1000 2500 5000 20000 50 100 500 1000 2500 5000 20000<br>mask<br>maskcoverage thelengthon lowestcoverage<br>Lowest thewith<br>Average<br>**----- End of picture text -----**<br>


Figure 7.8: Coverage and interval’s length for the mask leading to the lowest coverage. Model is NN. Calibration size fixed to 1000. The mask is concatenated in the features. Data is imputed using Iterative Ridge. 100 repetitions allow to display error bars, corresponding to standard error. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0187-04.png)


**----- Start of picture text -----**<br>
1 . 0<br>0 . 9 8<br>QR<br>0 . 8 CQR<br>6 CQR-MDA-exact<br>0 . 7 CQR-MDA-nested<br>Oracle<br>0 . 6<br>4<br>0 . 5<br>2<br>Training size Training size<br>7.9: Coverage and interval’s length for the mask leading to the highest<br>caption of Figure 7.8 for the setting.<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 0<br>0 . 8<br>0 . 6<br>0 . 4<br>15 Oracle length<br>10<br>5<br>50 100 500 1000 2500 5000 20000 50 100 500 1000 2500 5000 20000<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>mask<br>the coverage<br>coverage<br>on<br>mask highest<br>length<br>Highest the<br>with<br>Average<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 7.9: Coverage and interval’s length for the mask leading to the highest coverage. See caption of Figure 7.8 for the setting. 

Figure 7.10: Average coverage (top) and length (bottom) as a function of the pattern size, i.e. the number of missing values ( `NA` ). First violin plot corresponds to marginal coverage. Stars correspond to the oracle length. Settings are: model is NN, train size is 500, calibration size is 250. The marginal test set includes 2000 observations. The conditional test set includes 100 individuals for each possible missing data pattern size. The mask is concatenated to the features. Data is imputed using Iterative Ridge. 100 repetitions are performed. 

## **7.G.3 Higher proportion of missing values** 

We present synthetic experiments where the proportion of MCAR missing values is of 40% (instead of 20% in Figure 7.3). Except from this, the settings are exactly the same than the ones of Figure 7.3. Precisely, the data is generated with _d_ = 10 according to Model 7.4.1, with _X ∼N_ ( _µ,_ Σ), _µ_ = (1 _, · · · ,_ 1) _[T]_ and Σ = _ϕ_ (1 _, · · · ,_ 1) _[T]_ (1 _, · · · ,_ 1) + 

_Chapter 7. Conformal Prediction with Missing Values_ 

170 

(1 _− ϕ_ ) _Id_ , _ϕ_ = 0 _._ 8, Gaussian noise _ε ∼N_ (0 _,_ 1) and the following regression coefficients _β_ = (1 _,_ 2 _, −_ 1 _,_ 3 _, −_ 0 _._ 5 _, −_ 1 _,_ 0 _._ 3 _,_ 1 _._ 7 _,_ 0 _._ 4 _, −_ 0 _._ 3) _[T]_ . For each pattern size, 100 observations are drawn according to the distribution of _M |_ size( _M_ ) in the test set. The training and calibration sizes are respectively 500 and 250. The experiment is repeated 100 times. The results are displayed in Figure 7.12. 

Interestingly, although expected, these experiments lead CP-MDA-Exact to frequently output infinite intervals. This is because the subsampling step with few calibration data – with respect to the dimension and proportion of missing values – reached a point where there are not enough observations for CP-MDA-Exact to calibrate accurately for some patterns. 

To compare CP-MDA-Exact and CP-MDA-Nested in this setting, Figure 7.12 is obtained by replacing the infinite intervals by _k∈_ max _Tr∪Cal[y]_[(] _[k]_[)] _[−] k∈Tr_ min _∪Cal[y]_[(] _[k]_[)][.][It][highlights][that][CP-] MDA-Exact is less _efficient_ (i.e. outputs larger intervals) than CP-MDA-Nested for patterns with less than 4 `NA` s. With a smaller calibration set or a higher proportion of missing values, this effect would be amplified and generalized to more patterns. Figure 7.12 also emphasizes that CP-MDA-Exact leads to more coverage variability than CP-MDA-Nested, on the patterns for which CP-MDA-Exact does not almost surely cover. 

## **7.G.4 Semi-synthetic experiments** 

In the semi-synthetic experiments, two settings are examined: one where the training size is small in comparison to the number of parameters of the Neural Network – “Medium” –, and one where the training size is even smaller so that some masks have a really low (or null) frequency of appearance in the training set – “Small”. In both cases, the calibration size is approximately half the training size. Figure 7.4 presented the results for the “Medium” case. 

Figure 7.13 represents the results for these settings, using the same parameters than Figure 7.4. For the results on the two other `meps` data sets ( `meps_20` and `meps_21` ) see Figure 7.14, which repeats the visualisation of `meps_19` to ease comparison. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0188-08.png)


**----- Start of picture text -----**<br>
QR CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 0<br>0 . 8<br>0 . 6<br>15 Oracle length<br>10<br>5<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 7.11: Model is NN. Train size is 1000. Calibration size fixed to 500. The marginal test set includes 2000 observations. The conditional test set includes 100 individuals for each possible missing data pattern size. The mask is concatenated in the features. Data is imputed using Iterative Ridge. 100 repetitions are performed. 

_7.G. Experimental study_ 

171 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0189-02.png)


**----- Start of picture text -----**<br>
QR CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 00<br>0 . 75<br>0 . 50<br>40 Oracle length<br>20<br>Figure 7.12: Same caption than Figure 7.10.<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Table 7.1: Semi-synthetic settings: training and calibration sizes for each of the 6 data sets depending on the setting. 

|||`meps_19`<br>_d_= 139<br>_l_= 5<br>_n_= 15785|`meps_20`<br>_d_= 139<br>_l_= 5<br>_n_= 1754|`meps_21`<br>_d_= 139<br>_l_= 5<br>1<br>_n_= 15656|`bio`<br>_d_= 9<br>_l_= 9<br>_n_= 45730|`bike`<br>_d_= 18<br>_l_= 4<br>_n_= 10886|`concrete`<br>_d_= 8<br>_l_= 8<br>_n_= 1030|
|---|---|---|---|---|---|---|---|
|||||||||
|Small|Tr size<br>Cal size|500<br>250|500<br>250|500<br>250|500<br>250|500<br>250|330<br>100|
|||||||||
|Medium|Tr size<br>Cal size|1000<br>500|1000<br>500|1000<br>500|1000<br>500|1000<br>500|630<br>200|




![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0189-05.png)


**----- Start of picture text -----**<br>
meps_19 ( d  = 139,  l  = 5) bio ( d  = 9, l  = 9) concrete ( d  = 8, l  = 8) bike ( d  = 18, l  = 4)<br>20 60<br>30 450<br>18<br>50<br>425<br>16<br>20<br>40 400<br>14<br>375<br>10 12 30<br>0 . 6 0 . 8 0 . 6 0 . 8 0 . 6 0 . 8 0 . 8 0 . 9<br>Average coverage Average coverage Average coverage Average coverage<br>QR CQR-MDA-Exact Marginal Highest Small<br>CQR CQR-MDA-Nested Lowest Medium<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 7.13: Model is NN. The mask is concatenated in the features. Data is imputed using Iterative Ridge. 100 repetitions are performed, allowing to display the standard error as error bars. The vertical dotted lines represent the target coverage of 90%. 

## **7.G.5 Real data** 

**Data set description.** Sportisse et al. (2020) selected 7 variables to model the level of platelets, after discussion with medical doctors. Thus, we followed their pipeline. Here are the 7 variables used: 

- `Age` : the age of the patient (no missing values); 

- `Lactate` : the conjugate base of lactic acid, upon arrival at the hospital (17.66% missing values); 

_Chapter 7. Conformal Prediction with Missing Values_ 

172 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0190-02.png)


**----- Start of picture text -----**<br>
meps_19 ( d  = 139, l  = 5) meps_20 ( d  = 139, l  = 5) meps_21 ( d  = 139,  l  = 5)<br>35<br>30<br>25<br>20<br>15<br>10<br>0 . 5 0 . 6 0 . 7 0 . 8 0 . 9 0 . 5 0 . 6 0 . 7 0 . 8 0 . 9 0 . 5 0 . 6 0 . 7 0 . 8 0 . 9<br>Average coverage Average coverage Average coverage<br>QR CQR-MDA-Exact Marginal Highest Small<br>CQR CQR-MDA-Nested Lowest Medium<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 7.14: Same caption than Figure 7.13. 

- `Delta_hemo` : the difference between the hemoglobin upon arrival at hospital and the one in the ambulance (23.82% missing values); 

- `VE` : binary variable indicating if a Volume Expander was applied in the ambulance. A volume expander is a type of intravenous therapy that has the function of providing volume for the circulatory system (2.46% missing values); 

- `RBC` : a binary index which indicates whether the transfusion of Red Blood Cells Concentrates is performed (0.37% missing values); 

- `SI` : the shock index. It indicates the level of occult shock based on heart rate (HR) and systolic blood pressure (SBP), that is SI = SBP[HR][,][upon][arrival][at][hospital][(2.09%] missing values); 

- `HR` : the heart rate measured upon arrival of hospital (1.62% missing values). 

**Splitting strategy.** To study the coverage conditionally on the masks, we must handle the scarcity of some of them. For each individual in the data set, we make only one prediction, this way avoiding too many repetitions of the same test point when computing the average. We split the data set into 5 folds, and predict on each fold by training the procedure on the 4 others, with 15390 observations for training, and 7694 for calibration. 

_7.G. Experimental study_ 

173 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0191-02.png)


**----- Start of picture text -----**<br>
QR<br>4 . 0 CQR<br>CQR-MDA-Exact<br>3 . 5 CQR-MDA-Nested<br>Marginal<br>3 . 0 Mask-type<br>2 . 5<br>2 . 0<br>1 . 5<br>1 . 0<br>0 . 90 0 . 92 0 . 94 0 . 96 0 . 98<br>Average coverage<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 7.15: Average coverage and length on the TraumaBase® data when predicting the platelets level. Colors correspond to the methods. Diamond (♦) corresponds to taking the average among all individuals. Other symbols correspond to computing the average among the individuals having a fixed mask. The vertical dotted line represents the target coverage of 90%. Model is NN. The mask is concatenated to the features. Imputation is Iterative Ridge. Each individual is predicted using 15390 observations for training, and 7694 for calibration. 

## **Chapter 8** 

## **Predictive Uncertainty Quantification with Missing Covariates** 

Predictive uncertainty quantification is crucial in decision-making problems. We investigate how to adequately quantify predictive uncertainty with missing covariates. A bottleneck is that missing values induce heteroskedasticity on the response’s predictive distribution given the observed covariates. Thus, we focus on building predictive sets for the response that are valid _conditionally_ to the missing values pattern. We show that this goal is impossible to achieve informatively in a distribution-free fashion, and we propose useful restrictions on the distribution class. Motivated by these hardness results, we characterize how missing values and predictive uncertainty intertwine. Particularly, we rigorously formalize the idea that the more missing values, the higher the predictive uncertainty. Then, we introduce a generalized framework, coined `CP-MDA-Nested` _[⋆]_ , outputting predictive sets in both regression and classification. Under independence between the missing value pattern and both the features and the response (an assumption justified by our hardness results), these predictive sets are valid conditionally to any pattern of missing values. Moreover, it provides great flexibility in the trade-off between _statistical variability_ and _efficiency_ . Finally, we experimentally assess the performances of `CP-MDA-Nested` _[⋆]_ beyond its scope of theoretical validity, demonstrating promising outcomes in more challenging configurations than independence. 

175 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

176 

||**Contents**|
|---|---|
||8.1<br>Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177<br>8.1.1<br>Literature’s background . . . . . . . . . . . . . . . . . . . . . . . . . 180<br>8.1.2<br>Overview of our contributions (and outline) . . . . . . . . . . . . . . 181<br>8.2<br>When is Mask-Conditional-Validity (MCV) a too lofty goal? . . . . . . . . . 183<br>8.2.1<br>Fully distribution-free result . . . . . . . . . . . . . . . . . . . . . . . 184<br>8.2.2<br>Restricting the class of admissible missingness distributions . . . . . 186<br>8.3<br>Links between missing covariates and predictive uncertainty . . . . . . . . . 187<br>8.3.1<br>Increasing uncertainty with nested masks<br>. . . . . . . . . . . . . . . 187<br>8.3.2<br>Guidelines for practitioners: which information through imputation<br>for quantile regression? . . . . . . . . . . . . . . . . . . . . . . . . . . 193<br>8.4<br>Principled unifed Missing Data Augmentation (MDA) framework:<br>`CP-MDA-Nested`_⋆_<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194<br>8.4.1<br>Presentation of `CP-MDA-Nested`_⋆_<br>. . . . . . . . . . . . . . . . . . . . 194<br>8.4.2<br>Theoretical guarantees on CP-MDA-Nested and `CP-MDA-Nested`_⋆_<br>leveraging their connection to leave-one-out CP . . . . . . . . . . . . 199<br>8.5<br>A practical glimpse on the impacts of breaking the distribution’s assumptions201<br>8.5.1<br>Experiments under _P_MCAR_,_Y_⊥⊥_M_|_X . . . . . . . . . . . . . . . . . . . . 201<br>8.5.2<br>Beyond MCAR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204<br>8.5.3<br>Breaking _Y ⊥⊥M |X_ Assumption . . . . . . . . . . . . . . . . . . . . . 207<br>8.A Hardness results<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209<br>8.B<br>Link between missing covariates and uncertainty<br>. . . . . . . . . . . . . . . 214<br>8.C<br>Leave-one-out predictive sets for randomized algorithms . . . . . . . . . . . 218<br>8.D Theory on `CP-MDA-Nested`_⋆_and CP-MDA-Nested . . . . . . . . . . . . . . . 220|



_8.1. Introduction_ 

177 

## **8.1 Introduction** 

**Predictive uncertainty quantification.** Over the last decades, major research efforts on statistical and machine learning algorithms have enabled them to leverage large data sets. They are now used to support high-stakes decision-making problems such as medical, energy, or civic applications, to name just a few. To ensure the safe deployment of these models and their adoption by society, it is crucial to acknowledge that these point predictions remain uncertain, and to quantify this uncertainty, communicating the limits of predictive performance. Therefore, uncertainty quantification has received much attention in recent years, particularly in the form of building prediction sets. 

Formally, the aim is to build a predictive set for the response _Y ∈Y_ , after observing the random vector _X ∈X ⊆_ R _[d]_ which contains _d ∈_ N _[∗]_ explanatory variables. Given a _miscoverage level α ∈_ [0 _,_ 1], a _marginally valid_ predictive set _Cα_ ( _·_ ) is a function satisfying 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0195-05.png)


The goal is that _Cα_ ( _·_ ) is as small as possible while being marginally valid. Distributionfree uncertainty quantification tools are powerful as they require minimal assumptions on the data generation process—typically only access to a sequence of _n_ exchangeable data points—making them usable on a wide range of applications, unlike traditional probabilistic approaches. 

Importantly, it has to be noted that Equation (8.1) averages among all probable ( _X, Y_ ), and thus might over-cover easy data points (say, e.g., young patients) at the cost of undercovering harder data points (say, e.g., older patients). Therefore, one branch of the literature studied how Equation (8.1) could be turned into a stronger goal. Specifically, Vovk (2012); Lei and Wasserman (2014); Barber et al. (2021a) emphasize trade-offs between theory and practice. They investigate the implications of designing a practical distribution-free method, that is one which outputs sets _Cα_ ( _·_ ) such that 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0195-08.png)


Unfortunately, they showed that Equation (8.2) is impossible to achieve in an informative way (i.e., typically _Cα_ ( _·_ ) _≡Y_ with high probability) if no assumptions on the data distributions are made. Moreover, finding natural relaxations that are compatible with informative distribution-free predictive sets seems also hard: restrictions to conditioning on _x ∈_ X, for an arbitrary mass positive X _⊆X_ , is still hard to achieve informatively (Barber et al., 2021a). 

**Missing values.** Somewhat paradoxically, as the quantity of data rises, the number of missing data also increases. This phenomenon is modeled through the introduction of a third random variable called the _mask_ or _missing pattern_ , denoted by _M ∈M ⊆{_ 0 _,_ 1 _}[d]_ , encoding which variables have not been observed. That is, the mask _M_ is the indicator vector such that for any _j ∈_ �1 _, d_ �, _Mj_ = 1 whenever _Xj_ is missing (not observed), and _Mj_ = 0 otherwise. As a consequence, we are working on _P_ :={distributions on ( _X , M, Y_ )}. For a given pattern _m ∈M, X_ obs( _m_ ) is the random vector of observed features, and _X_ mis( _m_ ) is the 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

178 

random vector of unobserved ones. For example, if we observe ( `NA` _,_ 6 _,_ 2) then _m_ = (1 _,_ 0 _,_ 0) and _x_ obs( _m_ ) = (6 _,_ 2). Notice that the number of different missing patterns, i.e., the size or cardinality of _M_ := # _M_ , typically grows exponentially in the dimension (for _M_ = _{_ 0 _,_ 1 _}[d]_ there are 2 _[d]_ different patterns). 

The way we deal with those missing values will typically depend on the downstream task at hand. While there is a vast range of studies in the inferential setting (Little, 2019; Josse and Reiter, 2018) with numerous implementations (Mayer et al., 2019), the research effort is scarcer on the prediction framework (Josse et al., 2019; Le Morvan et al., 2020b,a, 2021; Ayme et al., 2022; Van Ness et al., 2022; Ayme et al., 2023; Zaffran et al., 2023; Ayme et al., 2024). It is mostly limited to _point prediction_ , except for Zaffran et al. (2023). The literature on both inference and prediction highlights the necessity of taking into account the missingness distribution. Following Rubin (1976), we consider three well-known missingness mechanisms. 

**Definition 8.1.1** (Missing Completely At Random (MCAR)) **.** The missing pattern distribution is said to be Missing Completely At Random (MCAR) if _M ⊥⊥ X_ . We denote _P_ MCAR the corresponding set of distributions, i.e. _P_ MCAR := _{P ∈P,_ such that for any _m ∈M,_ P _P_ ( _M_ = _m|X_ ) = P _P_ ( _M_ = _m_ ), that is _M ⊥⊥ X}_ . 

**Definition 8.1.2** (Missing At Random (MAR)) **.** The missing pattern distribution is said to be Missing At Random (MAR) if _M_ only depends on the observed components of _X_ . We denote _P_ MAR the corresponding set of distributions, i.e. _P_ MAR := _{P ∈P,_ such that for any _m ∈M_ , P _P_ ( _M_ = _m|X_ ) = P _P_ � _M_ = _m|X_ obs( _m_ )��. 

**Definition 8.1.3** (Missing Non At Random (MNAR)) **.** The missing pattern distribution is said to be Missing Non At Random (MNAR) if _M_ can depend on the observed values of _X_ but also on its missing components. We denote _P_ MNAR the corresponding set of distributions, i.e. _P_ MNAR := _P_ . 

_Remark_ 8.1.1 _._ We thus have _P_ MCAR _⊂P_ MAR _⊂P_ MNAR = _P_ . 

**Predictive framework with missing covariates.** In a predictive framework, the dependence between _Y_ and _M_ plays a key role, maybe even bigger than the relationship between ( _X, M_ ). Indeed, in some situations, _Y_ can be a direct function of _M_ : the missingness conveys in itself information about the label. Therefore, these cases are particularly challenging in a predictive framework, as some patterns on the one hand can induce an important label distributional shift, and on the other hand be rarely observed due to the high cardinality of _M_ . Thus, we focus on settings where there is _not_ such a direct dependency, that is Assumption A1. Yet, as we will show in the paper, it remains that the lack of observation of some features influences the uncertainty of the prediction of _Y_ from _X_ obs( _M_ ). 

**Assumption A1** ( _M_ does not explain _Y_ ) **.** We say that _Y_ is independent of _M_ given _X_ if _Y ⊥⊥M |X_ . The associated distribution belongs to _P_ Y _⊥⊥_ M _|_ X. 

_8.1. Introduction_ 

179 

Definitions 8.1.1 to 8.1.3 and Assumption A1 will be our main assumptions on the joint distribution of ( _X, M, Y_ ) throughout the manuscript. Our interest is in building predictive sets from _n_ observations � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[on a new test point] � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)] _, Y_[(] _[n]_[+1)][�] . We thus also make assumptions on the _links between those samples_ : the usual backbone assumption is that we have access to _n_ +1 independent and identically distributed (i.i.d.) draws from a distribution _Q_ in a set _Q_ , with _Q_ being typically one of _P_ MCAR, _P_ MAR, _P_ , etc. The data distribution thus belongs to � _Q[⊗]_[(] _[n]_[+1)] _, Q ∈Q_ �, which we denote _Q[⊗]_[(] _[n]_[+1)] . Furthermore, we also consider here a relaxation of i.i.d., namely _exchangeability_ , which is often sufficient to obtain guarantees in distribution-free predictive inference. 

**Assumption A2** (exchangeability) **.** The random variables � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1][are][ex-] changeable, i.e., their distribution does not change when we permute them. We denote _Q_[exch(] _[n]_[+1)] = � _Q_[exch(] _[n]_[+1)] _, Q ∈Q_ � the set of distributions of exchangeable random variables, with marginal distribution in _Q_ . 

An i.i.d. sequence is a fortiori exchangeable, while the reverse is not true (for example, sampling without replacement leads to a sequence that is exchangeable but not i.i.d.). _Remark_ 8.1.2 _._ We thus have that for any _Q_ , _Q[⊗]_[(] _[n]_[+1)] _⊂Q_[exch(] _[n]_[+1)] . 

**Predictive uncertainty quantification under missing covariates.** When features are missing, Equation (8.1) extends with _Cα_ a function of two arguments: _X_ and _M_ . Specifically, _Cα_ is a _marginally valid_ predictive set for the test response _Y_ given its corresponding covariates _X_ and the mask _M_ if: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0197-06.png)


However, marginal validity (MV) is not enough from an equity stand point and might result in discriminating between observations depending on their missing pattern (Zaffran et al., 2023). Indeed, missing values create heteroskedasticity in the resulting distribution of _Y_ given _X_ obs( _M_ ). Therefore, they argue that when facing missing values one should aim at _mask-conditional-validity_ (MCV) even in the MCAR setting, i.e.: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0197-08.png)


Equation (MCV) is similar in spirit and motivation than Equation (8.2) but on a discrete space. Hence the impossibility results on _X_ -conditional coverage do not hold anymore. However, (MCV) is a challenging goal as it requires the coverage to be controlled on _any_ mask _m ∈M_ , even those rarely observed at train time. 

In the sequel, to highlight the underlying dependencies and randomness, any estimator of _Cα_ ( _·, ·_ ) fitted on a data set � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[is][denoted][as] _[C]_[�] _[n,α]_[(] _[·][,][ ·]_[)][.][We][call][a] _method_ a function that, for any _α ∈_ [0 _,_ 1], takes as input � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[and][outputs] an estimator _C_[�] _n,α_ ( _·, ·_ ). Table 8.1 reminds the notations. 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

180 

|Name|Defnition||Comment|
|---|---|---|---|
|#_A_|Cardinal of the set _A_|||
|P(_A_)|Power set of _A_|||
|_d_|Number of features|||
|_X_|Features space||_X ⊆_R_d_|
|_Y_|Label space|||
|_M_|Missing values pattern space||_M ⊆{_0_,_1_}d_|
|`NA`|Not Available (or missing value)|||
|obs(_m_)|Indices of the observed components for mask _m ∈M_||obs(_m_)_∈_N_|_obs(_m_)_|_|
||(there are _|_obs(_m_)_|_:= �_d_<br>_i_=1 _mi_ of them)|||
|mis(_m_)|Indices of the missing components for mask _m ∈M_||mis(_m_)_∈_N_|_mis(_m_)_|_|
||(there are _|_mis(_m_)_|_:=_d −_�_d_<br>_i_=1 _mi_ of them)|||
|_P_|Set of distributions on (_X, M, Y_)|||
|_P_MAR|Set of distributions on (_X, M, Y_) such that _X_ is|Missing At Random||
|_P_MCAR|Set of distributions on (_X, M, Y_) such that _X_ is|Missing Completely At Random||
|_P_Y_⊥⊥_M_|_X|Set of distributions on (_X, M, Y_) such that _Y ⊥⊥M |X_|||
|_n_|Number of training observations||_n_+ 1 is the test index|
|_P ⊗_(_n_+1)|Product distribution of _P_ with itself _n_+ 1 times||_P ∈P_|
|_Q⊗_(_n_+1)|(i.e., distribution of<br>�<br>_X_(_k_)_, M_(_k_)_, Y_ (_k_)�_n_+1<br>_k_=1 drawn <br>�<br>_Q⊗_(_n_+1)_, Q ∈Q_<br>�|i.i.d. with marginal _P_)|_Q ⊆P_|
|_P_ exch(_n_+1)|Exchangeable distribution of _n_+ 1 random variables of distribution _P_||_P ∈P_|
|_Q_exch(_n_+1)|�<br>_Q_exch(_n_+1)_, Q ∈Q_<br>�||_Q ⊆P_|
|_α_|Miscoverage rate||_α ∈_[0_,_1]|
|_Cα_(_·, ·_)|Predictive set function aiming at 1_−α_ coverage||_Cα_ :_X × M −→_P(_Y_)|
|�_Cn,α_(_·, ·_)|Estimator for _Cα_(_·, ·_) based on<br>�<br>_X_(_k_)_, M_(_k_)_, Y_ (_k_)�|_n_<br>_k_=1, through a _method_||
|MV|Marginal validity|||
|MCV|Mask-conditional-validity|||



Table 8.1: Summary of notations. 

## **8.1.1 Literature’s background** 

Very recent papers have investigated uncertainty quantification with missing values. Both Gui et al. (2023a) and Shao and Zhang (2023) consider the question of distribution-free uncertainty quantification for matrix completion tasks. While the former considers building predictive sets for all of the missing entries, the latter focuses on what they call _matrix prediction_ where predictive sets are required only for the last “individual” of the data set. Seedat et al. (2023) addresses the related but distinct problem of missing values in the responses, which is generally known as the semi-supervised setting. They introduce a self-supervised learning approach for incorporating unlabeled training data into the conformalization process. In the same framework, Lee et al. (2024) leverages tools from the causal inference literature to achieve stronger guarantees such as feature and outcome’s missingness conditional coverage, which are, in spirit, close to our focus (yet in a different framework). 

Closer to our work of predictive uncertainty quantification under missing covariates is Zaffran et al. (2023), as they focus on the same setting (i.e., to predict _Y_ given _X_ , where _X_ might suffer from missing values both at train time and test time). After showing that _impute-then-predict+conformalization_ is marginally valid (MV) for any missing mechanism and imputation, they introduce the harder goal of _mask-conditional-validity_ (MCV), motivated by an illustration on the heteroskedasticity generated by the missing values on a Gaussian Linear Model. They present a novel methodology, _Missing Data_ 

_8.1. Introduction_ 

181 

_Augmentation_ (MDA), which combines with conformal prediction (CP, Vovk et al., 2005) in order to produce MCV sets. CP-MDA includes two algorithms, CP-MDA-Exact and CP-MDA-Nested, the former requiring a strict subsampling step on the training set, while the latter allows to keep the whole training data, which in turns induce large predictive sets. Zaffran et al. (2023) provide theoretical guarantees on the MCV of CP-MDA-Exact and on a technical minor modification of CP-MDA-Nested, under MCAR and _Y ⊥⊥M |X_ assumptions. 

## **8.1.2 Overview of our contributions (and outline)** 

In short, our objective is to tackle the following question: **when and how is it possible to achieve MCV?** Notably, we are interested in understanding _i_ ) what assumptions are necessary to ensure MCV, _ii_ ) how to design a tailored methodology, and _iii_ ) what happens when these assumptions are not satisfied. 

We start by proving hardness results on distribution-free MCV in Section 8.2. Notably, for a MCV method outputting _C_[�] _n,α_ ( _·, ·_ ) with no assumption except from having access to _n_ i.i.d. draws, we prove that the predictive interval is most often uninformative: for any _m ∈M_ the probability that, say, _C_[�] _n,α_ ( _·, m_ ) _≡Y_ is higher than 1 _− α −_ ∆ _m,n_ , where ∆ _m,n_ gets negligible when the mask _m_ is nearly not observed in a sample of size _n_ . In other words, a method that is distribution-free MCV will output uninformative intervals on any mask that does not represent a high enough proportion of the training data. We go further and show that the exact same trade-off still holds for a method that is MCV only on distributions that are MAR, or MCAR, or similarly on distributions such that _Y ⊥⊥M |X_ , i.e., restricting an algorithm to be MCV only when _Y ⊥⊥M |X_ would still output uninformative sets on rarely observed masks: it is necessary to add another assumption on the dependence between _X_ and _M_ (such as MCAR) to allow for informative MCV on any mask. Importantly, this theoretical analysis brings new insights on the achievability of _X_ -group-conditional validity, beyond MCV[1] . 

This motivates the investigation of the quantile regression and missing values interplay in Section 8.3, so as to provide guidelines for practical design of probabilistic prediction with missing covariates. This interplay is hard to characterize in general but becomes explicit under missingness assumptions’, or a multivariate Gaussian setting or linear model. Our key findings are ( _i_ —Section 8.3.1) that the uncertainty often increases with more missing values: we analyze different mathematical statements of this main idea (in terms of conditional variance, inter-quantile distance, or predictive interval length) and evaluate theoretically under which distributional assumptions they are satisfied, in particular under MCAR and _Y ⊥⊥M |X_ , motivating our methodological design of Section 8.4; ( _ii_ —Section 8.3.2) if the goal is to estimate quantiles, it is essential to be able to retrieve the mask to construct intervals, in contrast to classic mean regression where the mask is not as crucial. 

> 1Precisely, we provide a rigorous quantification of Vladmir Vovk’s comment on _X_ -conditional validity: “of course, the condition that _x_ be a non-atom is essential: if _PX_ ( _x_ ) _>_ 0, an inductive conformal predictor that ignores all examples with objects different from _x_ will have 1 _− α_ object conditional validity and can give narrow predictions if the training set is big enough to contain many examples with _x_ as their object” rephrased from Vovk (2012) to match our notations. 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

182 

In Section 8.4, we propose a unified framework, `CP-MDA-Nested` _[⋆]_ , building predictive sets with missing covariates for both regression and classification tasks. Precisely, it bridges the gap between CP-MDA-Exact and CP-MDA-Nested introduced in Zaffran et al. (2023), by encapsulating these two algorithms as well as any in between with more flexible subsampling schemes, allowing to fix the trade-off between coverage variance (CP-MDA-Exact) and overly conservative predictive sets (CP-MDA-Nested). Leveraging the similarity between `CP-MDA-Nested` _[⋆]_ and leave-one-out conformal approaches (Vovk, 2015; Barber et al., 2021b; Gupta et al., 2022) we provide theory on the marginal validity of `CP-MDA-Nested` _[⋆]_ without subsampling, which holds regardless of the missingness distribution (without any assumption on the dependence between _M_ and _X_ , but also without any assumption on the relationship between _M_ and _Y_ conditionally on _X_ ). Moreover, we also establish that `CP-MDA-Nested` _[⋆]_ is MCV for a wide range of subsampling schemes under MCAR and _Y ⊥⊥M |X_ . 

Finally, in Section 8.5 we conduct synthetic experiments beyond the MCAR and _Y ⊥⊥M |X_ assumptions. Precisely, we generate missingness that is either MAR (5 different settings), MNAR (11 different settings) or such that _Y ̸⊥⊥M |X_ . `CP-MDA-Nested` _[⋆]_ empirically maintains MCV under MAR and MNAR missingness. When _Y ⊥⊥M |X_ is not satisfied, `CP-MDA-Nested` _[⋆]_ does not ensure MCV experimentally, unless the imputation is accurate enough. Overall, these numerical experiments showcase the robustness of `CP-MDA-Nested` _[⋆]_ beyond its theoretical scope of validity. 

In the following Table 8.2, we summarize and organize our main contributions. We report the theoretical results on the possibility to achieve informative MCV, either positive results ( ) or negative hardness results ( ), along with our more general result on marginal validity. Moreover, we locate experimental results by indicating the figures that align with particular setups. In particular, we distinguish two kinds of experiments: _Numerical extension_ of results beyond the conditions where the theory is applicable, which demonstrates promising outcomes in more challenging configurations, and _Numerical confirmation_ of results anticipated by theoretical analysis, that is the outcomes of the experiment either _i_ ) were already expected based on the theory or _ii_ ) confirm that the theoretical assumptions can not be relaxed to the corresponding distributional setting. 

||_P_MCAR<br>_P_MAR<br>_P_MNAR =_P_||
|---|---|---|
|_P_Y_⊥⊥_M_|_X|`CP-MDA-Nested`_⋆_: <br>?<br>Hardness: <br>_Theory_<br>_Theorem 8.4.2_<br>_Proposition 8.2.2_<br>Figures 8.5a and 8.5b<br>Figures 8.6a, 8.6b, 8.7a and 8.7b<br>_Num. extension_<br>Figure 8.4<br>Remark 8.5.1<br>_Num. confrmation_||
|_P_|Hardness: <br>Hardness: <br>Hardness: <br>_Theory_<br>_Proposition 8.2.1_<br>_Proposition 8.2.1_<br>_Theorem 8.2.1_<br>`CP-MDA-Nested`_⋆_: MV<br>_Theorem 8.4.1_<br>Figure 8.8a<br>_Num. extension_<br>Figure 8.8b<br>Remark 8.5.1<br>Remark 8.5.1<br>_Num. confrmation_||



Table 8.2: Summary of the main theoretical results. 

_8.2. When is Mask-Conditional-Validity (MCV) a too lofty goal?_ 

183 

## **8.2 When is Mask-Conditional-Validity (MCV) a too lofty goal?** 

We will show in this section that purely distribution-free MCV guarantees are often uninformative. As a consequence, we will have to impose some non-parametric assumption on the underlying data distribution. We thus have to define the concept of MCV with respect to a class of distributions _D_ (MCV- _D_ ), and to study the sets _D_ that allow for informative MCV- _D_ . 

**Definition 8.2.1** (MCV- _D_ ) **.** Let _D_ be a set of distributions on ( _X × M × Y_ ) _[n]_[+1] . A method outputting _C_[�] _n,α_ ( _·, ·_ ) based on � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[for][any] _[α][ ∈]_[[0] _[,]_[ 1]][is][MCV-] _[D]_[if] _for any distribution D ∈D_ and any _α ∈_ [0 _,_ 1], we have: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0201-05.png)


If _D_ = _P_[exch(] _[n]_[+1)] we recover the holy grail of being MCV for any exchangeable distribution, i.e., the most distribution-free result we could target. If _D_ is not specified thereon, it will refer to MCV- _P_[exch(] _[n]_[+1)] . An easier goal is to aim at MCV- _P[⊗]_[(] _[n]_[+1)] , that is MCV on i.i.d. distributions. 

_Remark_ 8.2.1 _._ For any sets _D ⊆D[′]_ , a method that is MCV- _D[′]_ is also MCV- _D_ , i.e., MCV- _D[′] ⇒_ MCV- _D_ . 

A naive idea to ensure MCV is to split the data set into # _M_ sub data sets, one for each mask, and run any marginally valid method on each of the data sets independently. However, as # _M_ grows exponentially in the dimension, this is not practical as it will generate small (or even empty) data sets for some masks. In particular, as long as P( _M_ = _m_ ) is low with respect to _n_ for a given _m ∈M_ , estimation on the sub data set is hard, and even finite sample method such as conformal prediction (Vovk et al., 2005) will suffer from important statistical variability or uninformativeness. Therefore, in practice, we usually need to go beyond this solution if we aim to achieve MCV for any mask, even those rarely observed at train times. Nevertheless, the task appears challenging without restricting the link between _M_ and ( _X, Y_ ), precisely due to the lack of information available in the data set. The question we tackle in this section is the following: **is it possible to achieve** _**distribution-free**_ **MCV in an informative way for any mask in** _M_ **, even those occurring with low probability?** 

**Link with group conditional coverage.** More generally, the question is that of finding on which subspace of the features it is possible to obtain meaningful conditional guarantees. Thus, the results demonstrated in this section give some answers to the broader question of when is _group-feature-conditional validity_ achievable (a relaxation of Equation (8.2)), which has attracted considerable interest lately (see e.g., Romano et al., 2020a; Barber et al., 2021a; Guan, 2022; Jung et al., 2023; Gibbs and Candès, 2023, to name just a few). 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

184 

## **Our hardness results shed light on** _X_ **-group-conditional coverage.** 

In the rest of this section, _M_ can be interpreted as any additional random variable, that may (or may not) depend on _X_ , on which we aim at achieving distribution-free conditional validity. For example, _M_ could represent subgroups of _X_ , eventually overlapping. Specifically, assume _M_ = _{_ 0 _,_ 1 _}[|G|]_ for _G_ a collection of groups on _X_ , then _M_ is an indicator vector on whether _X_ belongs to each group of _G_ or not. A particular case of this generalization is _G_ = � _{X ∈X_ : _Xj_ is missing _}[d] j_ =1�, recovering our missing covariates setting with _M_ the missing pattern. While our discussion in this section is written towards the missing covariates setting, the interested reader might replace “missing pattern” or “mask” by “groups” whenever it makes sense[2] , and the corresponding result will hold without further restriction or assumptions on the way the groups are designed. 

## **8.2.1 Fully distribution-free result** 

Our first result, Theorem 8.2.1, confirms the previous intuition: any MCV- _P[⊗]_[(] _[n]_[+1)] method typically does output the whole set _Y_ with high probability for any distribution, on low probability masks. 

**Theorem 8.2.1** (Trade-off set size and mask probability) **.** _Suppose that a method outputting_ � _Cn,α is MCV-P[⊗]_[(] _[n]_[+1)] _. Then_ for any _P ∈P and any m ∈M such that PM_ ( _m_ ) _>_ 0 _, it holds:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0202-07.png)


Since for any _x >_ 0 and _n ∈_ N _[∗]_ , it holds 1 _−_ (1 _− x_ ) _[n] < nx_ , Theorem 8.2.1 implies that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0202-09.png)


Theorem 8.2.1 provides a lower bound on the probability that the predictive set is uninformative for any _m ∈M_ (i.e., typically Λ( _C_[�] _n,α_ ( _·, m_ )) = _∞_ or # _C_[�] _n,α_ ( _·, m_ ) _≥_ # _Y_ (1 _− α_ )). 

_Remark_ 8.2.2 (MCV- _P[⊗]_[(] _[n]_[+1)] implies uninformative sets even on simple distributions) _._ Crucially, this lower bound holds for _any_ distribution in _P_ . This implies that the hardness 

> 2The only result that does not extend is Proposition 8.2.1 for _P_ MAR, as by construction it relies on the missingness structure. 

_8.2. When is Mask-Conditional-Validity (MCV) a too lofty goal?_ 

185 

result applies also to smooth, nonpathological, distributions. Particularly, it means that any method that is fully distribution-free MCV (i.e., MCV- _P[⊗]_[(] _[n]_[+1)] ) will be subject to the lower bound even when applied to data whose actual distribution is as simple as possible (e.g., MCAR and _Y ⊥⊥M |X_ ). 

_Remark_ 8.2.3 (Informative sets implies the method is not MCV- _P[⊗]_[(] _[n]_[+1)] ) _._ Conversely, for a given method constructing predictive sets _C_[�] _n,α_ , assume that there exists a distribution _P ∈P_ and a mask _m_ such that _PM_ ( _m_ ) _>_ 0 and ∆ _m,n <_[1] _[−]_ 2 _[α]_ and under which _C_[�] _n,α_ is consistently of finite measure for different random draws from _P[⊗]_[(] _[n]_[+1)] . Then, this method is not MCV- _P[⊗]_[(] _[n]_[+1)] , as otherwise under _P[⊗]_[(] _[n]_[+1)] the predictive set would be of infinite measure with probability at least 0.25 for _α ≤_ 0 _._ 5 according to Theorem 8.2.1 (since 1 _− α −_ ∆ _m,n ≥_[1] _[−]_ 2 _[α] ≥_ 0 _._ 25). 

**Interpretation of the lower bound.** Let us now decompose the lower bound. The first term, 1 _− α_ , is an “irreducible term”. Indeed, the estimator outputting _Y_ with probability 1 _− α_ and the empty set _∅_ with probability _α_ (where the probability corresponds to an exogenous Bernoulli random variable) is valid conditionally on everything, thus a fortiori on _M_ . Hence, the lower bound has to be smaller than 1 _− α_ as the set of MCV estimators includes this naive one. 

For a given distribution _P_ , the second term, ∆ _m,n_ , becomes negligible on any _m ∈M_ such that _PM_ ( _m_ ) is small with respect to _n_ , making the lower bound be nearly 1 _− α_ . This reflects the intuition that it is impossible to achieve informative conditional coverage when conditioning on events whose effective sample size is limited. In other words, the smaller the probability of the event occurring, the larger the training size must be to compensate and make “sure” that enough observations are drawn from that event. 

Note that as _P[⊗]_[(] _[n]_[+1)] _⊂P_[exch(] _[n]_[+1)] , any MCV- _P_[exch(] _[n]_[+1)] estimator is MCV- _P[⊗]_[(] _[n]_[+1)] by Remark 8.2.1. Thus, the conclusion of Theorem 8.2.1 extends to any MCV- _P_[exch(] _[n]_[+1)] estimator, on any _P[⊗]_[(] _[n]_[+1)] with _P ∈P_ .[3] 

**Proof sketch.** For any given distribution _P ∈P_ , and a given mask _m ∈M_ such that _PM_ ( _m_ ) _>_ 0, the idea of the proof is the following. Build another distribution _Q ∈P_ , which equals _P_ whenever _M_ = _m_ , and that “admits” an arbitrary spread on _Y_ when _M_ = _m_ (in short, _Q_ is meant to be pathological yet close to _P_ ). By doing so, two statements can be made. First, _Q[⊗]_[(] _[n]_[+1)] belongs to _P[⊗]_[(] _[n]_[+1)] , therefore, as _C_[�] _n,α_ is MCV- _P[⊗]_[(] _[n]_[+1)] , under _Q[⊗]_[(] _[n]_[+1)] the probability of _C_[�] _n,α_ being uninformative is 1 _− α_ since _Y_ can typically be anywhere. Second, as _P_ and _Q_ are the same everywhere except on _{M_ = _m}_ , the total variation distance between them is smaller than _PM_ ( _m_ ). This leads to the total variation distance between _P[⊗]_[(] _[n]_[+1)] and _Q[⊗]_[(] _[n]_[+1)] being smaller than ∆ _m,n_ . Combining these two observations, it finally leads to the probability of _C_[�] _n,α_ being uninformative under _P[⊗]_[(] _[n]_[+1)] which is greater than 1 _− α −_ ∆ _m,n_ . The complete proof is given in Section 8.A. 

A familiar reader will note the similarity with the proofs given by Lei and Wasserman (2014); Vovk (2012). The difference is that, on the one hand, Vovk (2012) proof leverages 

3 The same is true for the subsequent Proposition 8.2.1 and Proposition 8.2.2. 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

186 

an “reductio ad absurdum” that does not allow to explicitly build the set on which _P_ = _Q_ . On the other hand, Lei and Wasserman (2014) is constructive. Nonetheless, it relies on a crucial step that implicitly assumes that conditional-validity holds conditionally on the _n_ data points, leading to an inexact statement: the lower bound obtained becomes 1. As we discussed, as well as Vovk (2012), the lower bound can not be bigger than 1 _− α_ . We provide an alternate proof to this well-known _X_ -conditional impossibility result that is constructive. Another improvement is that our expression of ∆ _m,n_ comes from a tighter inequality than the ones used in Lei and Wasserman (2014) and Vovk (2012). Indeed, for the original impossibility result, the lower bound does not really matter as we then take its limit when the ball around _x_ 0 shrinks, which is 0. But in our case, this ball is fixed to the event _{M_ = _m}_ . 

## **8.2.2 Restricting the class of admissible missingness distributions** 

Interestingly, the proof of Theorem 8.2.1 adapts to MCV- _P_ MAR _[⊗]_[(] _[n]_[+1)] or MCV- _P_ MCAR _[⊗]_[(] _[n]_[+1)][.] 

**Proposition 8.2.1** (Trade-off set size and mask probability on _P_ MAR or _P_ MCAR) **.** _Let Q be either P_ MAR _or P_ MCAR _. Suppose than an estimator C_[�] _n,α is MCV-Q[⊗]_[(] _[n]_[+1)] _at the level α. Then_ for any _Q ∈Q and any m ∈M such that QM_ ( _m_ ) _>_ 0 _, it holds:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0204-06.png)


_with_ ∆ _m,n given in Theorem 8.2.1._ 

_Remark_ 8.2.4 (no direct implication between results) _._ Proposition 8.2.1 for _Q_ = _P_ MAR does not imply Proposition 8.2.1 for _Q_ = _P_ MCAR, nor the contrary. Indeed, on the one hand, as _P_ MCAR _[⊗]_[(] _[n]_[+1)] _[⊆P]_ MAR _[⊗]_[(] _[n]_[+1)] , any method that is MCV- _P_ MAR _[⊗]_[(] _[n]_[+1)] is MCV- _P_ MCAR _[⊗]_[(] _[n]_[+1)][(Remark][8.2.1][).] However, on the other hand, Proposition 8.2.1 (or Theorem 8.2.1) provides a uniform statement over _Q ∈Q_ (Remark 8.2.2): as _P_ MCAR _[⊗]_[(] _[n]_[+1)] _[⊆P]_ MAR _[⊗]_[(] _[n]_[+1)] , the final statement holds on more distributions for _Q_ = _P_ MAR than for _Q_ = _P_ MCAR. Thereofore, Proposition 8.2.1 for _Q_ = _P_ MAR provides a _stronger statement_ over _fewer methods_ than Proposition 8.2.1 for _Q_ = _P_ MCAR. 

For the same reason, Proposition 8.2.1 is not deduced directly from Theorem 8.2.1, but from a careful consideration of the construction in its proof: the adversarial distribution built therein does not make any assumption on the relationship between _X_ and _M_ , which can be as simple as desired. 

In fact, the key point for the proof of Theorem 8.2.1 is that the algorithm achieves MCV also on distributions under which _Y_ and _M_ can be dependent even conditionally on _X_ : thus, it allows us to construct an adversarial distribution under which _Y_ is equally likely to be anywhere on the label space for a given _m ∈M_ . 

In view of this, one could think that in order to break Theorem 8.2.1, and therefore to ensure that MCV is achievable in an informative way even on low probability masks, we 

_8.3. Links between missing covariates and predictive uncertainty_ 

187 

have to _at least_ assume _Y ⊥⊥M |X_ (A1). However, in Proposition 8.2.2, we show that even estimators that are only MCV- _P_ Y _[⊗] ⊥⊥_[(] M _[n]_[+1)] _|_ X[suffer][from][the][same][trade-off][on][efficiency.] 

**Proposition 8.2.2** (Trade-off set size and mask probability on _P_ Y _⊥⊥_ M _|_ X) **.** _Suppose that an estimator C_[�] _n,α is MCV-P_ Y _[⊗] ⊥⊥_[(] M _[n]_[+1)] _|_ X _[at][the][level][α][.][Then][for][any][P][∈P]_[Y] _[⊥⊥]_[M] _[ |]_[X] _[and][for][any] m ∈M such that_ 1 _[it][holds:]_ ~~_√_~~ 2 _[≥][P][M]_[(] _[m]_[)] _[ >]_[ 0] _[,]_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0205-04.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0205-05.png)


All in all, Proposition 8.2.2 demonstrates that even the simplest relationship between _Y_ and _M_ does not allow informative predictive sets. This reveals that to ensure that it is possible to obtain informative sets even on low probability masks (or events), one has to design a method that will be conditionally valid _only_ on distributions with a constrained structure of dependence between _Y_ and _M_ given _X_ , but also between _M_ and _X_ . In particular, trying to ensure MCV- _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[(where] _[ P]_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[:=] _[ P]_ MCAR _[⊗]_[(] _[n]_[+1)] _[∩P]_ Y _[⊗] ⊥⊥_[(] M _[n]_[+1)] _|_ X[)] as done in Zaffran et al. (2023) appears as a natural way to approach the minimal set of assumptions. 

_Remark_ 8.2.5 _._ In Figure 8.4, we illustrate that, on a distribution _P ∈P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[,][a] provably MCV- _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[method][(introduced][in][Section][8.4][)][consistently][outputs][finite] length predictive intervals (regression case). Therefore, we can conclude that obtaining a hardness result on _P[⊗]_[(] _[n]_[+1)][impossible,][as][such][it][would][induce][Remark][8.2.3] MCAR _,_ Y _⊥⊥_ M _|_ X[appears] (with _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[instead][of] _[P][⊗]_[(] _[n]_[+1)][).] 

## **8.3 Links between missing covariates and predictive uncertainty** 

In light of the previous section, MCV appears hard to achieve. Thus, the problem that we aim to address now is to **find ways to model properly the missing covariates’ influence on predictive uncertainty** . To understand the relationship between missing — values and predictive uncertainty, this section explores simplified distributions on ( _X, M, Y_ ) such as MCAR and _Y ⊥⊥M |X_ —and/or on ( _X, Y_ )—such as linearity, Gaussianity. We consider the regression case with _Y_ = R. This exploration aims to facilitate the development of suitable frameworks for probabilistic inference when covariates are missing—i.e., models that are as close as possible to achieving MCV. 

## **8.3.1 Increasing uncertainty with nested masks** 

The hardness results of Section 8.2 induce that MCV cannot be (efficiently) achieved without structural assumptions on the links between the predictive distributions conditional 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

188 

on each missing pattern. In this subsection, we gain insights into the underlying reasons for this phenomenon: the predictive uncertainty depends on the missing pattern, a form of _heteroskedasticity_ . In summary, we explore the following idea, which is a natural modelization attempt in that direction: 

## **Idea:** _The predictive uncertainty increases when less covariates are observed._ 

In technical words, the aforementioned heteroskedasticity takes the form of an _isotonicity_ (monotony) with respect to the mask, with the inclusion order given by Definition 8.3.1 below. In short: the more missing values, the more uncertainty there is. 

**Definition 8.3.1** (Included masks) **.** Let ( _m, m[′]_ ) _∈M_[2] , _m ⊂ m[′]_ if for any _j ∈_ �1 _, d_ � such that _mj_ = 1 then _m[′] j_[= 1][,][i.e.,] _[m][′]_[includes][at][least][the][same][missing][values][than] _[m]_[.] 

Hereafter, we formally quantify such a statement, in particular in terms of conditional variance, inter-quantile distance, and predictive interval length. We demonstrate that some of those statements are valid, to different extent, under distributional assumptions, either generic or on specific model or examples. To that end, we introduce several properties, that can be considered as non-parametric assumptions on the underlying distributions. We put together some results of this section in the following Table 8.3, that can be used as a reading guide throughout the section. 

## 8.3.1.1 Conditional Variance Isotony w.r.t. the missing data patterns 

We start by focusing on the link between _M_ and the _conditional variance_ of _Y |X_ obs( _M_ ), that constitutes a natural proxy on the predictive uncertainty. Denote _V_ ( _X_ obs( _M_ ) _, M_ ) := Var � _Y |X_ obs( _M_ ) _, M_ � the conditional variance of _Y_ given � _X_ obs( _M_ ) _, M_ �. We introduce two properties regarding its ordering with respect to _M_ : (Var-1) and (Var-2). 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0206-09.png)


Property Var-1 is stronger than Property Var-2 as it is an almost sure result w.r.t. the covariates _X_ . The following proposition ensures that (Var-2) is satisfied under _P_ MCAR _,_ Y _⊥⊥_ M _|_ X (that is, assumptions for which no hardness result can exist). 

**Proposition 8.3.1.** _Under P_ MCAR _,_ Y _⊥⊥_ M _|_ X _,_ (Var-2) _is valid._ 

|Property<br>Setup|Model 8.3.2|Model 8.3.1|_P_MCAR_,_Y_⊥⊥_M_|_X|
|---|---|---|---|
|Variance|Var-1|<br>Var-1<br>Var-2|Var-2|
|Inter-quantile|IQ-1|IQ-2||
|Length of Oracle PI|Len-1|Len-2|Len-2|



Table 8.3: Summary of the results from Section 8.3.1. 

_8.3. Links between missing covariates and predictive uncertainty_ 

189 

The proof of this result is given in Section 8.B.1. This is a first significant result: under general assumptions—i.e., strong assumption on the relation between the mask and both the response and the features, but no assumptions on their distribution—, the averaged variance is always smaller on smaller masks. This establishes the existence of a link between the uncertainties _on patterns that can be compared_ , that is patterns that are nested in one another. Note that the order given by Definition 8.3.1 is only a partial order: the average variance ordering is only enforced w.r.t. that partial order. 

It is possible that the predictive uncertainty increases on average with the mask (Equation (Var-2)) but not almost surely on _X_ (Equation (Var-1)), as illustrated by Model 8.3.1 below: 

**Model 8.3.1** (Unidimensional heteroskedasticity) **.** Consider the following one-dimensional model: 

- _X ∼N_ (0 _, σ_[2] ), _σ ∈_ R+; 

- _ξ ∼N_ (0 _, τ_[2] ), _τ ∈_ R+, such that _ξ ⊥⊥ X_ ; 

- _Y_ = _βX_ + _Xξ_ , with _β ∈_ R; 

- _M ∼B_ ( _ρ_ ), with _ρ ∈_ [0 _,_ 1], and _M ⊥⊥_ ( _X, Y_ ). 

Under this model, we obtain that _M ⊥⊥ X_ (MCAR) and _Y ⊥⊥M |X_ , and 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0207-10.png)


Thus Equation (Var-2) is verified but Equation (Var-1) is only satisfied for _X_ such that _X_[2] _≤_ 1 + _[β] τ_[2][2] _σ_[2] . This is illustrated in Figure 8.1. The first subplot represents _Y_ depending on _X_ , while the third subplot displays _Y − βX_ depending on _X_ , that is an illustration of the uncertainty of the distribution of _Y |X_ . For any _X_ outside the vertical dashed lines (corresponding to _±_ (1 + _β_[2] _/τ_[2] ) _σ_[2] ), the conditional variance of _Y_ given _X_ is larger than the overall variance when _X_ is missing. Yet, the average variance of _Y_ when _X_ is missing is indeed higher than the average variance of _Y_ when _X_ is observed: this can be seen on the two histograms on subplots 2 and 4. 

Figure 8.1: Visualisation of a random draw from the data distribution of Model 8.3.1, with 100000 i.i.d. samples, _ρ_ = 0 _._ 2, _σ_[2] = 1 _._ 5, _τ_[2] = 1 and _β_ = 2. The colors indicate whether _X_ is observed or missing. The first subplot represents _Y_ depending on _X_ , while the third subplot displays _Y − βX_ depending on _X_ only for observed _X_ , that is an illustration of the uncertainty of _Y |X_ . The second subplot is an histogram of _Y_ when _X_ is missing, while the forth subplot is an histogram of _Y − βX_ when _X_ is observed, i.e., they represent the predictive distribution of _Y_ depending on whether _X_ is observed or missing. 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

190 

Finally, while Model 8.3.1 shows that (Var-1) is not always true, even under the assumptions of Proposition 8.3.1, we now show that it can be achieved in the following Gaussian linear model, a particular case of Gaussian pattern mixture model. 

**Model 8.3.2** (Gaussian linear model (GLM)) **.** The data is generated according to a linear model and the covariates are Gaussian conditionally to the pattern: 

• _Y_ = _β[T] X_ + _ε_ , _ε ∼N_ (0 _, σε_[2][)] _[ ⊥⊥]_[(] _[X, M]_[)][,] _[β][∈]_[R] _[d]_[.] 

- for all _m ∈M_ , there exist _µ[m] ∈_ R _[d]_ and Σ _[m] ∈_ R _[d][×][d]_ such that _X|_ ( _M_ = _m_ ) _∼N_ ( _µ[m] ,_ Σ _[m]_ ) _._ 

Such a model results in a MCAR distribution when Σ _[m] ≡_ Σ. Indeed under Model 8.3.2 the resulting predictive distribution is given by _Y |_ ( _X_ obs( _m_ ) _, M_ = _m_ ) _∼N_ (˜ _µ[m] ,_ � _σ[m]_ ) for any _m ∈M_ , with: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0208-07.png)


with _µ[m]_ mis _|_ obs[and][Σ] _[m]_ mis _|_ obs[defined][in][Section][8.B.1.2][(][Le][Morvan][et][al.][,][2020b][;][Ayme][et][al.][,] 2022; Zaffran et al., 2023). Crucially, _σ_ � _[m]_ depends on _m_ in a non-linear fashion, even in MCAR. That is, even in MCAR and a homoskedastic model for _Y |X_ , the predictive distribution of _Y |X_ obs( _M_ ) is heteroskedastic: basically, the distribution of _Y_ is a mixture of various distributions with the mask being the latent variable. This simple example already illustrates that missing values generate strong heteroskedasticity: in Proposition 8.3.2, we show that under this Model 8.3.2 and _P_ MCAR, the variance of the conditional distribution of _Y_ increases when the missing pattern increases (in the sense of Definition 8.3.1). 

**Proposition 8.3.2** (Conditional variance increases with the mask under MCAR GLM) **.** _Under Model 8.3.2 and P_ MCAR _, if the covariance matrix_ Σ _is positive definite, Equation_ (Var1) _is satisfied._ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0208-10.png)


Next, in order to go beyond variances, we focus on inter-quantile distances as a measure of uncertainty, and establish a general result on the expected length of oracle predictive intervals. 

8.3.1.2 Conditional Inter-quantile Isotony w.r.t. the missing data patterns 

Ideally, we would like to access the oracle predictive interval (the interval satisfying Equation (MCV) with minimal expected length). Thus, in this section we are interested in characterizing its behavior with respect to _M_ , in order to be able to mimic it. We denote this interval _Cα[∗][,P]_ , that is formally defined for any _m ∈M_ as: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0208-14.png)


_8.3. Links between missing covariates and predictive uncertainty_ 

191 

In fact, under Model 8.3.2, the oracle predictive interval is uniquely defined by the quantiles _α/_ 2 and 1 _− α/_ 2 of the _N_ (˜ _µ[m] ,_ � _σ[m]_ ). More importantly, this oracle interval even achieves _X_ -conditional coverage. Proposition 8.3.2 shows that under _P_ MCAR and Model 8.3.2, increasing the number of missing values (in a nested way) induces an increase in the predictive uncertainty of _Y_ : the oracle intervals, that are given by inter-quantiles intervals, are nested. Notably, this is true almost surely on _X_ obs and not only marginally. 

To generalize this property beyond the Gaussian case, we introduce the inter-quantile distance, that encodes the uncertainty for conditional predictive distribution. For all _β ≤_[1] 2 _[≤][γ]_[,][we][define][the][inter-quantile][space][for][quantile][distributions:] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0209-04.png)


And the following two assumptions, that are similar in spirit to (Var-1) and (Var-2) 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0209-06.png)


The assumptions on the quantiles and the variance are equivalent for Gaussian (conditional) distributions. As a consequence, (IQ-2) is satisfied under Model 8.3.2 and _P_ MCAR as well as under Model 8.3.1, while (IQ-1) is satisfied only under Model 8.3.2 and _P_ MCAR. Interquantile assumptions are related to predictive intervals: for any distribution _P_ such that _PY |X_ obs( _M_ ) _,M_ is a.s. unimodal, the oracle predictive interval _Cα[∗][,P]_ writes as an inter-quantile interval almost surely, that is there exist functions _β, γ_ : _X × M →_ [0 _,_ 1] such that 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0209-08.png)


Indeed, to minimize the average length, the best oracle solution consists in minimizing the length conditionally to ( _X_ obs( _M_ ) _, M_ ), which is achieved by an inter-quantile interval, under the unimodality assumption. The quantity _γ_ ( _X_ obs( _M_ ) _, M_ ) _− β_ ( _X_ obs( _M_ ) _, M_ ) corresponds to the ( _X_ obs( _M_ ) _, M_ )–conditional coverage, that is on average, conditionally to _M_ = _m_ , the targeted 1 _− α_ . 

Yet, in practice, the constructed intervals are not the oracle ones. Therefore, a natural question is whether (IQ-2) extends to a non-oracle _Cα_ . As generally _Cα_ is not based on the underlying true conditional quantiles, we focus on _Cα_ length instead, a quantity similar in spirit to the inter-quantile. We consider the two following assumptions: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0209-11.png)


We have the following Theorem 8.3.1 on isotonicity (Len-2) under _P_ MCAR _,_ Y _⊥⊥_ M _|_ X. 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

192 

**Theorem 8.3.1.** _Let Cα be an MCV-P_ MCAR _,_ Y _⊥⊥_ M _|_ X _predictive interval. There exists a predictive interval C_[�] _α which_ 

_i) is MCV-P_ MCAR _,_ Y _⊥⊥_ M _|_ X _,_ 

_ii) has conditional length smaller or equal to that of Cα on each pattern,_ 

_iii) is averaged-length-isotonic w.r.t. the patterns, i.e., satisfies_ (Len-2) _._ 

The proof of Theorem 8.3.1 exploits the fact that under _P_ MCAR _,_ Y _⊥⊥_ M _|_ X, a strategy to ensure conditional coverage w.r.t. a pattern _m_ , is to transform ( _X_ obs( _m_ ) _, m_ ) into ( _X_ obs( _m[′]_ ) _, m[′]_ ) by additionally masking some entries, and using the predictive interval given on pattern _m[′]_ . For _m ⊂ m[′]_ , we denote _X_ obs(max( _m,m′_ )) the point in which we additionally mask elements of _m[′]_ in _X_ . We have that under _P_ MCAR _,_ Y _⊥⊥_ M _|_ X, the distribution of the data _post-masking_ is equal to that of the data with more missing entries: P _Y |X_ obs(max( _M,m′_ )) _,_ max( _M,m′_ ) = _PY |X_ obs( _m′_ ) _,M_ = _m′_ . We can leverage this observation to build intervals: if the averaged length of the predictive interval conditionally to a pattern _m ⊂ m[′]_ is larger than that conditionally to a pattern _m ⊂ m[′]_ , we can replace _Cα_ ( _X_ obs( _m_ ) _, m_ ) by _Cα_ ( _X_ obs( _m′_ ) _, m[′]_ ), ensuring both that new interval length is smaller and that we satisfy (Len-2). Formally, we proceed by induction: starting from the pattern _m[′]_ = (1 _, . . . ,_ 1) (no data observed), we first consider all patterns _m_ = (1 _, . . . ,_ 1 _,_ 0 _,_ 1 _, . . ._ ) with a single observed value, and define _C_[�] _α_ ( _X_ obs( _M_ ) _, M_ ), conditionally to _M_ = _m_ , as either _Cα_ ( _X_ obs( _M_ ) _, M_ ) or _Cα_ ( _X_ obs(max( _M,m′_ )) _,_ max( _M, m[′]_ )) (depending on which expected length is smaller). We then repeat the same reasoning inductively. For a pattern _m_ , we pick for _C_[�] _α_ either _Cα_ ( _·, m_ ) or the minimal-length interval among all _Cα_ ( _·, m[′]_ ) for all patterns _m[′]_ that have one more missing data than _m_ , and artificially mask on of the components of _X_ obs( _m_ ) when predicting. **Interpretation:** we leverage towards predictive interval construction the fact that we can transform an observed point, by removing some covariates, and recover the same distribution as the one with more missing entries. This idea will be one of the key techniques leveraged in Section 8.4. 

As consequence of Theorem 8.3.1 is the following corollary, that is obtained by a minimality argument for the oracle interval (i.e., knowing that applying the aforedmentioned transformation to the oracle does not change it, as it already has minimal-expected length on each pattern): 

**Corollary 8.3.1.** _Let P ∈P_ MCAR _,_ Y _⊥⊥_ M _|_ X _. Then the oracle interval Cα[∗][,P] is averaged-lengthisotonic w.r.t. the patterns, i.e., satisfies_ (Len-2) _._ 

Overall, (Len-2) is thus satisfied by our target sets under _P_ MCAR _,_ Y _⊥⊥_ M _|_ X, and thus appears as a reasonable constraint to impose on our predictive sets. Indeed, it seems to be close to the minimal set of assumptions required in order to ensure that no hardness result exists (Section 8.2) while inducing a leverageable structure between patterns that can be compared (Theorem 8.3.1). 

_8.3. Links between missing covariates and predictive uncertainty_ 

193 

## **8.3.2 Guidelines for practitioners: which information through imputation for quantile regression?** 

In this section, we highlight specifities of predictive uncertainty quantification under missing covariates with respect to mean regression, and provide generic guidelines usable in practice. 

**Impute-then-predict.** Most predictive algorithms can not cope directly with missing covariates. To bypass this, the most common approach is to impute the incomplete data via an imputation function Φ, that maps observed values to themselves and missing values to a function of the observed values. Using notations from Le Morvan et al. (2021) we note _ϕ[m]_ : R _[|]_[obs(] _[m]_[)] _[|] →_ R _[|]_[mis(] _[m]_[)] _[|]_ the imputation function which, given a mask _m ∈M_ , takes as input observed values and outputs imputed values, i.e., plausible values. Then, the overall imputation function Φ belongs to _F[I]_ := Φ : _X × M →X_ : _∀j ∈_ �1 _, d_ � _,_ � (Φ ( _X, M_ )) _j_ = _Xj_ 1 _Mj_ =0 + � _ϕ[M]_[ �] _X_ obs( _M_ )�� _j_[1] _[M][j]_[=1] �. The imputed data set becomes the _n_ random variables (Φ ( _X, M_ ) _, M, Y_ ). In practice, Φ is the result of an algorithm _I_ trained on �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)][��] _[n] k_ =1[+1][.][The][impact][of][imputation][has][been][studied][for][mean][regression] tasks (in particular in Le Morvan et al., 2021; Ayme et al., 2023, 2024). 

**How to account for the missingness when imputing?** Given the impact of missing covariates on the shape of prediction uncertainty discussed in Section 8.3.1, impute-thenpredict raises a specific concern: is there a way to impute which incorporates the necessary information on the missing values? 

Hereafter, we show that the answer is significantly different if we restrict ourselve to mean regression. Specifically, we show that incorporating the mask (e.g., by concatenating the mask to the features) is more critical for quantile regression. To that end, we provide in Proposition 8.3.3 simple models showcasing that unbiased imputation choices are sufficient to obtain an optimal model for regression but fail for quantile regression. For mean regression, the efficiency of such imputation methods have been established in practice (see e.g., Josse et al., 2019; Le Morvan et al., 2021) and Proposition 8.3.3 support those findings. 

**Proposition 8.3.3.** _Assume P_ MCAR _,_ Y _⊥⊥_ M _|_ X _and Y_ = _β[∗][T] X_ + _ε with ε s.t._ E � _ε|X_ obs( _M_ ) _, M_ � = 0 _._ 

- _i) Mean regression_ 

   - _if the covariates_ ( _Xj_ ) _[d] j_ =1 _[are][independent,][then][the][optimal][linear][model][taking]_ Φmean( _X, M_ ) _as input is Bayes optimal, with_ Φmean _the imputation by the mean;_ 

   - _the optimal linear model taking_ Φconditional mean( _X, M_ ) _as input is Bayes optimal, with_ Φconditional mean _the imputation by the conditional mean;_ 

- _ii) Any quantile linear model taking unbiased imputed data as input (i.e.,_ E [Φ( _X, M_ ) _|M_ ] _[a.s.]_ = E [ _X_ ] _) leads to intervals of constant expected length across patterns, thus is not Bayes optimal when Y ̸⊥⊥ X._ 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

194 

Point i) of Proposition 8.3.3 illustrates that if the learner was able to retrieve the true underlying regression coefficients and the data were imputed by their mean or conditional mean, then the learned model would be the best possible at the task of predicting the conditional expectation, i.e., all necessary information is preserved by using only the imputed data set and not leveraging the associated mask. Although the non-necessity of using the mask in the conditional expectation estimation and MCAR framework does not systematically extend when the data is more complex than linear, it is insightful as even in the linear setting, the same does not hold for quantile regression. 

Indeed, point ii) of the same Proposition 8.3.3 highlights that on the contrary a learner accessing the true underlying regression coefficients with the very same unbiased imputed data would not lead to an optimal model, as a method whose resulting predictive interval have constant lengths across the missing patterns does not retrieve the underlying heteroskedasticity induced by the missing values (Section 8.3.1), and thereby cannot be MCV. Precisely, the assumption on the imputation for this result corresponds for example to imputing by the feature’s expectation (i.e., Φmean), the feature’s conditional expectation (i.e., Φconditional mean), or a random draw from a distribution whose expectation is the feature’s expectation, under _P_ MCAR. This includes MICE (van Buuren and Groothuis-Oudshoorn, 2011), which consists in imputing by random draws from the conditional distribution hence the imputed data have the same expectation than the features themselves. 

Overall, Proposition 8.3.3 tells that _i_ ) the state-of-the-art imputation method MICE is not the best choice for predictive uncertainty quantification, _ii_ ) by contrast to mean regression, in the linear case imputing by the expectation or the conditional expectation is detrimental. In fact, data-independent constant imputation would result in more adaptive intervals. This is because quantile regression needs to retrieve the information on the patterns to adapt its structure to it. Therefore, when using such imputations, **a natural idea is to give the information of the mask to the model by concatenating the mask to the features** . 

## **8.4 Principled unified Missing Data Augmentation (MDA) framework:** `CP-MDA-Nested` _[⋆]_ 

In this section, we go beyond generic guidelines and we introduce a general framework, coined `CP-MDA-Nested` _[⋆]_ , to generate predictive sets that achieve MCV under _P_ MCAR _,_ Y _⊥⊥_ M _|_ X. Our approach is applicable to both classification and regression tasks, by building upon any conformal score function (Vovk et al., 2005). It combines over-masking ideas introduced in Section 8.3, with subsampling techniques, and similar machinery than leave-one-out conformal prediction methods (Barber et al., 2021b; Gupta et al., 2022). 

## **8.4.1 Presentation of** `CP-MDA-Nested` _[⋆]_ 

We start by reminding the necessary concepts of split Conformal Prediction (CP) in the complete case, without missing values, before diving into the details of our unified framework `CP-MDA-Nested` _[⋆]_ . 

_8.4. Principled unified Missing Data Augmentation (MDA) framework:_ _`CP-MDA-Nested`[⋆]_ 

195 

## 8.4.1.1 Background on split CP 

Introduced in Papadopoulos et al. (2002); Vovk et al. (2005); Lei et al. (2018), split CP builds predictive regions by first splitting the _n_ points of the training set into two disjoint sets Tr _,_ Cal _⊂_ �1 _,_ n�, to create a _proper training set_ , Tr, and a _calibration set_ , Cal, of sizes #Tr = (1 _− ρ_ ) _n_ and #Cal = _ρn_ with _ρ ∈_ ]0 _,_ 1]. On the proper training set, a model _f_[ˆ] (chosen by the user) is fitted, and then used to predict on the calibration set. _Conformity scores S_ = _s X_[(] _[k]_[)] _, Y_[(] _[k]_[)] ; _f_[ˆ] _∪{_ + _∞}_ are computed to assess how well the fitted �� � �� _k∈_ Cal� model _f_[ˆ] predicts the response values of the calibration points. In regression, usually the ˆ absolute value of the residuals is used, i.e. _s_ ( _x, y_ ; ˆ _µ_ ) = _|µ_ ( _x_ ) _− y|_ . In classification, the simplest score is _s_ ( _x, y_ ; ˆ _p_ ) = 1 _− p_ ˆ( _x_ ) _y_ (where _p_ ˆ : _X �→_ [0 _,_ 1] _[Y]_ outputs a vector of estimated probabilities for each class). Finally, the (1 _− α_ )-th quantile of these scores _q_ 1 _−α_ ( _S_ ) (i.e., their _⌈_ (1 _− α_ ) (#Cal + 1) _⌉_ smallest value) is computed to define the predictive region: � ˆ _Cn,α_ ( _x_ ) := _{y ∈Y_ such that _s_ ( _x, y_ ; _f_ ) _≤ q_ 1 _−α_ ( _S_ ) _}_ . In regression with the absolute values of the residual score, this reduces to _C_[�] _n,α_ ( _x_ ) := [ˆ _µ_ ( _x_ ) _± q_ 1 _−α_ ( _S_ )]. 

This procedure satisfies Equation (8.1) for any _f_[ˆ] , any (finite) sample size _n_ , as long as the data points are exchangeable.[4] For more details on split CP, we refer to Angelopoulos and Bates (2023); Vovk et al. (2005), as well as to Manokhin (2022). 

## 8.4.1.2 `CP-MDA-Nested` _[⋆]_ 

From an high level perspective, the idea is to apply split CP on top of an impute-then-predict pipeline (of imputation function Φ), and to modify the calibration step in order to ensure MCV. This is called CP-MDA, for _conformal prediction with missing data augmentation_ . Generally, for a given test point � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] , CP-MDA works by artificially masking covariates in the calibration set so as to match _at least_ the mask of the test point, by creating a new mask _M_[�][(] _[k]_[)] = max � _M_[(] _[k]_[)] _, M_[(] _[n]_[+1)][�] for each _k ∈_ Cal. In other words, it corresponds to discarding from the calibration set the covariates that are missing in the test point. This leads to _M_[(] _[n]_[+1)] _⊆ M_[�][(] _[k]_[)] , i.e., all over-masked (or _augmented_ ) points _X_[(] _[k]_[)] _, M_[�][(] _[k]_[)] _, Y_[(] _[k]_[)][�] � _k∈_ Cal have at least the missing entries of � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] . The points such that _M_[�][(] _[k]_[)] = _M_[(] _[n]_[+1)] can be used directly as under distributional assumptions ( _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[),][they][now][have] the same mask and distribution as the test point. Yet for many calibration points it remains that _M_[�][(] _[k]_[)] = _M_[(] _[n]_[+1)] (precisely, for all the _k ∈_ Cal such that _M_[(] _[k]_[)] _̸⊆ M_[(] _[n]_[+1)] ). This means that those over-masked points follow another conditional distribution than the one of the test point, and MCV can not be directly ensured. 

An idea is to subsample the calibration set so that the effective calibration set contains only _k ∈_ Cal such that _M_[(] _[k]_[)] _̸⊆ M_[(] _[n]_[+1)] (i.e., _M_[�][(] _[k]_[)] = _M_[(] _[n]_[+1)] ) (this is the approach followed in CP-MDA-Exact, Zaffran et al., 2023). However, this can lead to overly small calibration set size in high dimension, resulting in a large variance (on the coverage level and thus set size). Therefore, two questions naturally arise: 

- How to build the calibration set? 

> 4Only the calibration and test data points need to be exchangeable. 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

196 

   - How to leverage the test point so as to account for the different distributions present in the over-masked calibration set—and with many of them not matching the test mask conditional distribution—when constructing the predictive set? 

- The answers we suggest define our generalized framework `CP-MDA-Nested` _[⋆]_ , whose pseudocode is available in Algorithm 16, and are illustrated in Figure 8.2. 

**Construction of the calibration set.** `CP-MDA-Nested` _[⋆]_ includes a subsampling step: it calibrates on the set of indices Cal[�] _⊆_ Cal provided by the user, where Cal[�] can be obtained with any subsampling strategy, that might even be stochastic, as long as the randomness is independent of the covariates and outputs, � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _∪{n_ +1 _}_[(it][can][still][depend][on] the masks). The following strategies work if the data distribution belongs to _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X (which is an assumption we make anyway when using `CP-MDA-Nested` _[⋆]_ since, as we show precisely in Theorem 8.4.2, `CP-MDA-Nested` _[⋆]_ is typically MCV- _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[):] 

- i) subsampling only the indices � _k ∈_ Cal : _M_[(] _[k]_[)] _⊆ M_[(] _[n]_[+1)][�] := Cal[�] (this is the strategy of CP-MDA-Exact, Zaffran et al., 2023); 

- ii) no subsampling, Cal[�] := Cal (this is the path taken by CP-MDA-Nested, Zaffran et al., 2023); 

- iii) subsampling only the indices � _k ∈_ Cal : _M_[(] _[k]_[)] _⊆ m[′]_[�] := Cal[�] , for some _m[′] ⊇ M_[(] _[n]_[+1)] ; iv) obtain Cal[�] by subsampling from the indices � _k ∈_ Cal : _M_[(] _[k]_[)] _⊆ m[′]_[�] , for some _m[′] ⊇ M_[(] _[n]_[+1)] , using a mixture distribution, whose weights only depend on � _M_[(] _[k]_[)][�] _k∈_ Cal _∪{n_ +1 _}_[.] 

- Then, for any _k ∈_ Cal[�] , the over-mask is constructed, defining _M_[�][(] _[k]_[)] = max � _M_[(] _[k]_[)] _, M_[(] _[n]_[+1)][�] . This is schematized in Figure 8.2. 

**Leveraging temporary test points.** After the subsampling step aforedmentioned, the over-masked calibration points and the test point do not necessarily have the same conditional distribution conditionally to the mask, as _M_[(] _[n]_[+1)] _⊆ M_[�][(] _[k]_[)] without equality in general. In order to match those distributions, an idea is to create temporary test points (one for each calibration point) and to apply _M_[�][(] _[k]_[)] to it. This is illustrated in green in Figure 8.2. `CP-MDA-Nested` _[⋆]_ evaluates the number of over-masked calibration points that have a conformity score smaller than that of the _corresponding over-masked test point_ for a given _y ∈Y_ . Then, the predictive set includes only the _y ∈Y_ such that this number is small enough (a threshold that depends on _α_ and the effective calibration size). This careful treatment of the test point allows to compare scores obtained from identical distributions conditionally on their associated mask. 

## 8.4.1.3 Key comments on `CP-MDA-Nested` _[⋆]_ 

In summary, `CP-MDA-Nested` _[⋆]_ bridges the gap between CP-MDA-Exact and CP-MDANested by proposing a tighter generalized framework. On the one hand, CP-MDA-Exact comes with a potentially small calibration set, thus with increased variability. On the other hand, by leveraging all calibration points, including those with very few observed covariates, the average interval length produced by CP-MDA-Nested is typically larger than 

_8.4. Principled unified Missing Data Augmentation (MDA) framework:_ _`CP-MDA-Nested`[⋆]_ 

197 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0215-02.png)


**----- Start of picture text -----**<br>
Overmasked calibration set Temporary test points<br>-1 1 0 3 1 2<br>4 2 1 3 1 2<br>keep same mask<br>0 1 -2 3 1 2<br>Test point<br>3 1 2<br>-1 1 0 3 1 2<br>Initial calibration set<br>4 2 1 3 1 2<br>-1 -10 6 1 0<br>keep arbitrary selection 5 3 3 2<br>4 -2 2 1<br>0 1 -2 3 1 2<br>5 1 1 3<br>0 1 -2<br>-3 0<br>-1 1 0 3 1 2<br>4 2 1 3 1 2<br>keep all points<br>5 3 3 2<br>0 1 -2 3 1 2<br>**----- End of picture text -----**<br>


Figure 8.2: `CP-MDA-Nested` _[⋆]_ illustration. Different subsampling strategies are shown, with their associated over-masked calibration set and temporary test points according to one test point. 

**Algorithm 16** `CP-MDA-Nested` _[⋆]_ 

**Input:** Training set �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][��] _[n] k_ =1[,][imputation][algorithm] _[I]_[,][learning][algorithm] _A_ taking its values in _F_ := _Y[X×M]_ , calibration proportion _ρ ∈_ ]0 _,_ 1], Tr _,_ Cal _,_ Φ _, A_[ˆ] the � � output of the splitting Algorithm 17 ran on ��� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][��] _[n] k_ =1 _[,][ I][,][ A][, ρ]_ �, conformity score function _s_ ( _·, ·_ ; _f_ ) for _f ∈F_ , significance level _α_ , test point � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] , subsampled set of calibration indices Cal[�] _⊆_ Cal **Output:** Prediction set _C_[�] _n,α_[MDA-Nested] _[⋆]_ � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] // Generate an over-masked calibration set: 1: **for** � _k ∈_ Cal[�] **do** Additional nested masking 2: _M_[(] _[k]_[)] = max( _M_[(] _[k]_[)] _, M_[(] _[n]_[+1)] ) 3: **end for** Over-masked calibration set generated. // 4: _C_[�] _n,α_[MDA-Nested] _[⋆]_ � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] := � _y ∈Y_ : (1 _− α_ )(1 + #Cal)[�] _>_ � 1 � _s_ �� _X_[(] _[k]_[)] _, M_[�][(] _[k]_[)][�] _, Y_[(] _[k]_[)] ; _A_[ˆ] (Φ ( _·, ·_ ) _, ·_ )� _< s_ �� _X_[(] _[n]_[+1)] _, M_[�][(] _[k]_[)][�] _, y_ ; _A_[ˆ] (Φ ( _·, ·_ ) _, ·_ )��� _k∈_ Cal 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

198 

## **Algorithm 17** Split and train 

**Input:** Imputation algorithm _I_ , learning algorithm _A_ taking its values in _F_ := _Y[X×M]_ , training set �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][��] _[n] k_ =1[,][calibration][proportion] _[ρ][ ∈]_[]0] _[,]_[ 1]] **Output:** Splitted sets of indices Tr and Cal, imputation function Φ, fitted predictor _A_[ˆ] 

- 1: Randomly split _{_ 1 _, . . . , n}_ into 2 disjoint sets Tr & Cal of sizes #Tr = (1 _− ρ_ ) _n_ and #Cal = _ρn_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0216-05.png)


that of CP-MDA-Exact (cf. (Len-2)). Furthermore, CP-MDA-Nested is less generic than CP in the sense that it is specific to predictive _intervals_ (unlike CP-MDA-Exact which is as generic as CP and can be plugged with any score function, including classification). Overall, `CP-MDA-Nested` _[⋆]_ unifies this framework for any score function and provides high flexibility in the trade-offs between _efficiency_ and _variability_ : 

- At the extreme of no subsampling at all, we obtain a generalization of `CP-MDA-Nested` which encapsulates the classification setting; 

- This generalization provides tighter sets than that of `CP-MDA-Nested` in the particular case of interval-based scores (see Remark 8.4.1); 

- At the other extreme of the strictest subsampling procedure, we retrieve `CP-MDA-Exact` ; 

- Any other less restrictive subsampling (possibly with a random selection between various augmented mask) belongs to this framework, providing more flexibility in the trade-offs between exact validity and statistical variability. 

This overview is summarized in Table 8.4. 

In the case where the nested predictive sets are intervals and Cal[�] = Cal, then the final predictive sets obtained through `CP-MDA-Nested` _[⋆]_ are included in the ones of CP-MDANested. 

_Remark_ 8.4.1 _._ When Cal[�] = Cal, and using absolute value of the residuals scores or conformalized quantile regression scores (Romano et al., 2019), or any score such that _{y ∈ Y_ such that _s_ ( _x, y_ ; _f_[ˆ] ) _≤ b}_ for some _b_ is an interval, then _C_[�] _n,α_[MDA-Nested] _[⋆]_ ( _·_ ) _⊆ C_[�] _n,α_[MDA-Nested] ( _·_ ) (see Section 8.D). 

This unification allows us to provide theoretical guarantees, stated in Section 8.4.2, leveraging the deep connections between `CP-MDA-Nested` _[⋆]_ and leave-one-out conformal 

|Method|CP-MDA-Exact|`CP-MDA-Nested`_⋆_**(new)**|CP-MDA-Nested||
|---|---|---|---|---|
|Size of actual calibration set|# points in Cal with _M ⊆M_(_n_+1)|Any|#Cal||
|Mask of the points used for calibration|exactly _M_(_n_+1)||all, leading to �<br>_M_ s.t. _M_(_n_+1)|_⊆_�<br>_M_|
|Overall behavior|Too few Cal points _→_high coverage variance|Flexible|Too large intervals (cf. (Len-2))||
|Applies to classifcation||(new)|||
|Outputs non-interval sets||(new)|||
|Marginal guarantee (MV)||(new)|(new)||
|Conditional guarantee (MCV)||(new)|(new)||



Table 8.4: Summary of the high-level characteristics of MDA algorithms, coming from the literature, as well as our novel contributions indicated by “(new)”. Characteristics are given for a test point � _X_[(] _[n]_[+1)] _, Y_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] . Details regarding guarantees are given in Table 8.5. 

199 

## _8.4. Principled unified Missing Data Augmentation (MDA) framework:_ _`CP-MDA-Nested`[⋆]_ 

|Guarantees|MV|MCV|
|---|---|---|
|`CP-MDA-Exact`|_P⊗_(_n_+1)<br>MCAR_,_Y_⊥⊥_M_|_X, level _α_,|_P⊗_(_n_+1)<br>MCAR_,_Y_⊥⊥_M_|_X, level _α_,|
|i.e., `CP-MDA-Nested`_⋆_with subsampling|with upper bound,|with upper bound,|
|only _k ∈_Cal s.t. _M_(_k_) _⊆M_(_n_+1)|from Zafran et al. (2023)|from Zafran et al. (2023)|
|`CP-MDA-Nested`_⋆_|_P⊗_(_n_+1)<br>MCAR_,_Y_⊥⊥_M_|_X, level 2_α_|_P⊗_(_n_+1)<br>MCAR_,_Y_⊥⊥_M_|_X, level 2_α_|
|`CP-MDA-Nested`_⋆_without subsampling|_P_exch(_n_+1), level 2_α_|_P⊗_(_n_+1)<br>MCAR_,_Y_⊥⊥_M_|_X, level 2_α_|



Table 8.5: Theoretical guarantees of `CP-MDA-Nested` _[⋆]_ depending on the subsampling choice. 

methods (such as Barber et al., 2021b; Gupta et al., 2022). Indeed, the rationale for predicting on masked test points, using the augmented calibration masked, is that we want to treat the test and calibration points in a symmetric way. We summarize them in the following Table 8.5. 

## **8.4.2 Theoretical guarantees on CP-MDA-Nested and** `CP-MDA-Nested` _[⋆]_ **leveraging their connection to leave-one-out CP** 

Hereafter, we give our theoretical results on the coverage of our `CP-MDA-Nested` _[⋆]_ algorithm. 

**Theorem 8.4.1** (Marginal validity of `CP-MDA-Nested` _[⋆]_ ) **.** _`CP-MDA-Nested`[⋆] with_ Cal[�] = Cal _and (and thus CP-MDA-Nested) is MV-P_[exch(] _[n]_[+1)] _at the level_ 1 _−_ 2 _α._ 

Theorem 8.4.1 provides a lower bound on `CP-MDA-Nested` _[⋆]_ and CP-MDA-Nested coverage as 1 _−_ 2 _α_ . This result is important as it equips `CP-MDA-Nested` _[⋆]_ with Cal[�] = Cal and CP-MDA-Nested with controlled coverage on any exchangeable distribution: they are marginally valid even on MNAR distributions or when _Y ̸⊥⊥ M |X_ . It means that despite modifying the data set independently from _X_ and _Y_ and breaking the structure of ( _X, M, Y_ ), the obtained estimator makes reliable predictions including when _X, M_ , and _Y_ are strongly dependent. This originates from the fact that the whole data set has been treated equally, including the test point. 

**Theorem 8.4.2** (Conditional validity of `CP-MDA-Nested` _[⋆]_ ) **.** _`CP-MDA-Nested`[⋆] with_ Cal[�] _independent of the data set_ � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _∪{n_ +1 _}[(and][thus][CP-MDA-Nested)][is][MCV-] P[⊗]_[(] _[n]_[+1)] _[the][level]_[1] _[ −]_[2] _[α][.]_ MCAR _,_ Y _⊥⊥_ M _|_ X _[at]_ 

The proofs of Theorems 8.4.1 and 8.4.2 are deferred to Section 8.D.1 and Section 8.D.2 respectively. They are heavily based on the deep connections between `CP-MDA-Nested` _[⋆]_ with Jackknife+ and general leave-one-out or _k_ -fold CP (Barber et al., 2021b; Vovk, 2015; Gupta et al., 2022). Indeed, one can observe that, for each _k ∈_ Cal, we evaluate the conformity score of the test point ( _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)] _, Y_[(] _[n]_[+1)] ) using the _k_ -th augmented mask, as the equivalent of evaluating the conformity score of the test point with the fitted model that has left-out the _k_ -th calibration point. This connection between `CP-MDA-Nested` _[⋆]_ and leave-one-out conformal approaches directly stems from the same core motivations: _i_ ) both enforce a design that use all the observations of the training or calibration sets to handle 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

200 

small sample sizes, _ii_ ) both need to avoid invalid designs that arise naturally when keeping all these points, such as comparing scores obtained with different predictors. 

**On the factor 2 and link with empirical quantile aggregation.** Despite the coverage guarantee being of 1 _−_ 2 _α_ instead of the desired 1 _− α_ , in practice, our experiments in Section 8.5 show that `CP-MDA-Nested` _[⋆]_ without subsampling (i.e., CP-MDA-Nested) tends to over-cover. This aligns with Figure 2 of Barber et al. (2021b), that illustrates the fact that leave-one-out conformal methods achieve empirically exactly 1 _− α_ coverage, while _K_ -fold conformal approaches over-cover. The reason behind this phenomenon is still unclear in the community, and is likely to be the same than the reason for `CP-MDA-Nested` _[⋆]_ over-coverage, as one can see `CP-MDA-Nested` _[⋆]_ as having access to many folds of calibration points, since each augmented calibration mask typically appears many times in the calibration set. In particular, Zaffran et al. (2023) provide MCV- _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[guarantees][at][the][level] 1 _− α_ on a modified version of CP-MDA-Nested which leverages this folding point of view by calibrating only on one (arbitrarily) chosen such fold. Similarly than for _K_ -fold and leave-one-out conformal methods, we can look at `CP-MDA-Nested` _[⋆]_ as a way to aggregate many valid empirical quantiles or _p_ -values, one for each fold, i.e., one for each augmented mask. Due to the strong dependencies between these random variables, such an aggregation does not lead to a valid aggregated quantile or _p_ -value, and induces a loss of coverage. 

**Theorem 8.4.2 proof approach: coupling our algorithm with a leave-one-out conformal method on a virtual complete data set.** We work conditionally to the mask of the test point, _M_[(] _[n]_[+1)] . Then, we introduce a randomized predictor, for which “training” consists in randomly picking one individual predictor among a bag of individual predictors, each of them corresponding to an augmented calibration mask. This bag contains exactly 2 _[|]_[obs(] _[M]_[(] _[n]_[+1)][)] _[|]_ possible individual predictors, where _|_ obs( _M_[(] _[n]_[+1)] ) _|_ is the number of 1s in _M_[(] _[n]_[+1)] , i.e., the number of observed features in the test point. Each individual predictor in the bag is thus parametrized by a _super/over-mask_ of _M_[(] _[n]_[+1)] . We call such a predictor a mixture-predictor, as it basically consists in picking randomly one individual predictor in a mixture of individual predictors. That sampling has to be made independently of the data the mixture predictor is applied to, but non necessarily uniformly. Furthermore, we ensure that the individual predictor indexed by a mask _M_ only relies on the covariates _X_ obs( _M_ ) for the prediction, in order for this algorithm to be applicable in practice (e.g., an invalid design would be individual predictors that require the knowledge of some of the _X_ mis( _M_ ), unobserved in practice, in order to make predictions). 

We then show that our algorithm `CP-MDA-Nested` _[⋆]_ , applied to the data set with missing _n_ +1 entries _X_[(] _[k]_[)][(] _[k]_[)] _[, M]_[(] _[k]_[)] , has the same guarantees in expectation as the leave� obs( _M_[(] _[k]_[)] ) _[, Y]_ � _k_ =1 one-out conformal that uses the mixture predictor, applied onto a virtual complete data set � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k[n]_ =1[+1][,][if][we][make][some][assumptions][on][the][missingness][distribution.][More] specifically, we show that _there exists a coupling between the two algorithms_ , that ensures that the output (and thus coverage) have the same distribution. This ultimately enables us to reuse existing guarantees for leave-one-out conformal estimators. 

_8.5. A practical glimpse on the impacts of breaking the distribution’s assumptions_ 

201 

## **8.5 A practical glimpse on the impacts of breaking the distribution’s assumptions** 

In this concluding section, we investigate the numerical performances of `CP-MDA-Nested` _[⋆]_ mainly outside its theoretical set of assumptions. Experiments under _P_ MCAR _,_ Y _⊥⊥_ M _|_ X are provided in Section 8.5.1, then Section 8.5.2 presents numerical results when the data distribution either belongs to _P_ MAR or _P_ MNAR, and finally Section 8.5.3 reports empirical performances when _Y ̸⊥⊥M |X_ . 

In all experiments, the data are imputed using iterative regression ( `iterative ridge` implemented in Scikit-learn, Pedregosa et al. (2011)). The predictive models are fitted on the imputed data concatenated with the mask. The prediction algorithm is a neural network, fitted to minimize the pinball loss (Sesia and Romano, 2021). For the vanilla QR, we use both the training and calibration sets for training. The training set contains 500 data points, and the calibration set 250 data points. To evaluate the marginal coverage, a test set is generated with missing values following the same distribution as on the training and calibration sets. Then, to estimate mask-conditional coverage (i.e., P( _Y ∈ C_[�] _n,α_ ( _X, m_ ) _|M_ = _m_ ) for each _m ∈M_ ), we generate another test set by imposing that the number of observations per pattern is fixed to 100, in order to ensure that the variability is not impacted by P ( _M_ = _m_ ). Each experiment is repeated 100 times (unless stated otherwise). 

## **8.5.1 Experiments under** _P_ MCAR _,_ Y _⊥⊥_ M _|_ X 

**Data generation.** The data is generated with _d_ = 10 according to Model 8.3.2 (regression), _Y_ = _β[T] X_ + _ε_ with _X ∼N_ ( _µ,_ Σ), _µ_ = (1 _, · · · ,_ 1) _[T]_ and Σ = _ϕ_ (1 _, · · · ,_ 1) _[T]_ (1 _, · · · ,_ 1)+(1 _−ϕ_ ) _Id_ , _ϕ ∈{_ 0 _,_ 0 _._ 8 _}_ depending on the experiment, Gaussian noise _ε ∼N_ (0 _,_ 1) _⊥⊥_ ( _X, M_ ) and the following regression coefficients _β_ = (1 _,_ 2 _, −_ 1 _,_ 3 _, −_ 0 _._ 5 _, −_ 1 _,_ 0 _._ 3 _,_ 1 _._ 7 _,_ 0 _._ 4 _, −_ 0 _._ 3) _[T]_ . Each of these 10 features is missing with probability 0 _._ 2 independently from anything else. 

## 8.5.1.1 `CP-MDA-Nested` _[⋆]_ provides flexibility 

In our first experiments, we compare CQR to CP-MDA-Exact and CP-MDA-Nested, as well as `CP-MDA-Nested` _[⋆]_ where we subsample all the calibration points that have at most two features that are missing among the observed features of the test point. As _d_ = 10, there are 1024 different patterns, avoiding to display the performances of the algorithms on each of the patterns. Therefore, instead, we represent the coverage and the length of the predictive intervals depending on the mask size, a proxy for mask-conditional coverage. For each pattern size, 100 observations are drawn according to the distribution of _M |_ size( _M_ ) in the test set. In this subsection only, the number of repetition is of 50. 

Figure 8.3a displays the results of this experiment. As noticed in Zaffran et al. (2023), CQR is not MCV- _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[as][its][intervals][undercover][or][overcover][depending][on] the number of missing values. The three versions of `CP-MDA-Nested` _[⋆]_ ensure that the coverage is at least 1 _− α_ for any pattern size, as supported by our theory (Section 8.4.2)[5] Comparing CP-MDA-Exact and CP-MDA-Nested, we observe that CP-MDA-Exact is more 

> 5Note that MCV implies validity on any mask size, but not the contrary. 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

202 

efficient as it produces smaller intervals and its coverage is exactly of 1 _− α_ on average, while suffering for more variability than CP-MDA-Nested. The intermediate version of `CP-MDA-Nested` _[⋆]_ allows to reduce CP-MDA-Exact variability while improving the efficiency of the intervals by 5.5% marginally (the comparison consists in computing the difference between `CP-MDA-Nested` _[⋆]_ and CP-MDA-Nested intervals’ median length, and normalize it by CP-MDA-Nested intervals’ median length), reaching nearly 10% of improvement on the test points that have no missing values. For 7 to 9 missing values, this `CP-MDA-Nested` _[⋆]_ is equivalent to CP-MDA-Nested as the subsampling scheme of `CP-MDA-Nested` _[⋆]_ boils down to keeping all the calibration points on these patterns. 

CP-MDA-Nested reveals all its interest over CP-MDA-Exact in settings where the exact subsampled calibration set contains really few points for some masks (e.g., in high dimension or when the probability of missing values is high). In Figure 8.3b, the probability of each features being missing is increased to 0.4. We observe that CP-MDA-Exact outputs infinite intervals more than half of the time on the marginal test, as well as on the test sets 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0220-04.png)


**----- Start of picture text -----**<br>
CQR-MDA-Nested [⋆] subsampling<br>CQR CQR-MDA-Exact points with at most 2 more  NA s CQR-MDA-Nested<br>1 . 0<br>0 . 8<br>tere efbetteetel Eeteeenapial coseeeeepag<br>0 . 6 VOM) V |!<br>15 Oracle length<br>10<br>5<br>gogeaeesbd egg ett?! beg egsteet beseee tert<br>(a) Each features is missing with probability 0.2.<br>CQR-MDA-Nested [⋆] subsampling<br>CQR CQR-MDA-Exact points with at most 2 more  NA s CQR-MDA-Nested<br>1 . 0<br>0 . 8<br>“yt feeea TYYYPUBCASTILITLT aaa LOL!<br>0 . 6<br>15 Oracle length<br>y 4! 9!<br>10<br>5<br>eqgogeg ened! |, aati shveseatts rreperdiKas?<br>(b) Each features is missing with probability 0.4.<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>coverage<br>Average<br>length<br>Average<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 8.3: Validity and efficiency with **MCAR missing values** on dependent Gaussian features, with _ϕ_ = 0 _._ 8, and such that **Y** _⊥⊥_ **M** _|_ **X** . Average coverage (top) and length (bottom) as a function of the missing pattern sizes. The black horizontal line in each violin plot corresponds to the median. The first violin plot shows the marginal coverage. The marginal test set includes 2000 observations. The mask-conditional test set includes 100 individuals for each missing data pattern size. 

_8.5. A practical glimpse on the impacts of breaking the distribution’s assumptions_ 

203 

containing between 0 and 4 missing values. This is particularly unpractical. On the contrary, CP-MDA-Nested produces finite length intervals on any test point, at the cost of being overly conservative. The improvements brought by `CP-MDA-Nested` _[⋆]_ with subsampling only the calibration points with at most 2 additional missing values are more stringent. In particular, the efficiency is improved by nearly 9.5% marginally, and is in between 8.5% and 10% on test points that have between 1 and 6 missing values. 

Note that this is only one example of `CP-MDA-Nested` _[⋆]_ for a given subsampling strategy, and that in practice the choice of strategy is highly dependent on the settings and could lead to even better performances. From now on, we restrict the subsequent experiments with `CP-MDA-Nested` _[⋆]_ to the two extremes—CP-MDA-Exact and CP-MDA-Nested—as their main goal is to investigate the robustness beyond _P_ MCAR _,_ Y _⊥⊥_ M _|_ X. For the same reason, we do not want to restrict ourselves to the mask-size conditional coverage, as it does not imply mask conditional coverage. Therefore, we use another visualization approach that was introduced in Zaffran et al. (2023). As an appetizer, Figure 8.4 presents the results under _P[⊗]_[(] _[n]_[+1)] MCAR _,_ Y _⊥⊥_ M _|_ X[for QR, CQR, CP-MDA-Exact and CP-MDA-Nested, using this visualization.] The _x_ -axis represents the average coverage and the average length is in the _y_ -axis. The marker colors are associated to the different methods. A method is MCV if all the markers of its color are at the right of the vertical dotted line (90%). The design of Figure 8.4, and the following figures, requires a cautious interpretation. For each method we report, for the pattern having the highest (or lowest) coverage, its length and coverage. However, as this pattern may depend on the method, the length for the highest/lowest should not be directly compared between methods. 

This Figure 8.4 illustrates that `CP-MDA-Nested` _[⋆]_ is MCV- _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[.][Our][hardness] results of Section 8.2 provide a new perspective on these results: 

_Remark_ 8.5.1 _._ If `CP-MDA-Nested` _[⋆]_ was MCV on a broader class of distributions than _P[⊗]_[(] _[n]_[+1)][which][a][hardness][result][exists,][then][it][would][produce][uninformative] MCAR _,_ Y _⊥⊥_ M _|_ X[for] intervals on any distribution within this class, including _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[.][Therefore,][the][fact] 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0221-06.png)


**----- Start of picture text -----**<br>
10<br>QR<br>CQR<br>8 CQR-MDA-Exact<br>CQR-MDA-Nested<br>Marginal<br>6 Lowest<br>Highest<br>4<br>0 . 6 0 . 8 1 . 0<br>Average coverage<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 8.4: Validity and efficiency with **MCAR missing values** on dependent Gaussian features, with _ϕ_ = 0 _._ 8, and such that **Y** _⊥⊥_ **M** _|_ **X** . Colors represent the methods. Diamonds (♦) represent marginal coverage while the patterns giving the lowest and highest coverage are represented with triangles (▼ and ▲). Vertical dotted lines represent the target coverage of 90%. Experimental details: #Tr = 500; #Cal = 250; the marginal test set includes 2000 observations; the mask-conditional test set includes 100 individuals for each missing data pattern. 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

204 

that `CP-MDA-Nested` _[⋆]_ obtain finite length intervals in this experiment (Figure 8.4) tends to confirm (with high probability) that the theory on the `CP-MDA-Nested` _[⋆]_ MCV can not be extended to _P_ Y _[⊗] ⊥⊥_[(] M _[n]_[+1)] _|_ X[or] _[P]_ MAR _[⊗]_[(] _[n]_[+1)] nor _P_ MCAR _[⊗]_[(] _[n]_[+1)][.][This][analysis][is][included][in][Table][8.2][,][as][a] numerical confirmation on `CP-MDA-Nested` _[⋆]_ theory. 

## **8.5.2 Beyond MCAR** 

**Beyond MCAR experiments.** To generate missing values under MAR or MNAR distribution, we select 6 variables (denote this set _X_ missing) out of 10 that can be missing (the 4 others form the set _X_ observed). Especially, _X_ missing = _{X_ 1 _, X_ 2 _, X_ 3 _, X_ 5 _, X_ 8 _, X_ 9 _}_ in order to include different range of associated regression coefficients. We used the GitHub repository associated to Muzellec et al. (2020) in order to introduce missing values in _X_ missing according to the following mechanisms, fixing the proportion of missing entries to be 20%. For each of these following settings, we run two sets of experiments: one in which the correlation between the features is high ( _ϕ_ = 0 _._ 8) and therefore imputing through iterative regression allows to recover quite accurately the missing values, and one in which the features are independent ( _ϕ_ = 0) leading to an imputation that can not be better than the marginal expectation of the features. 

▶ MAR experiments (Figure 8.5). Missing values in _X_ missing are introduced under a MAR mechanism. To do so, a logistic model of arguments _X_ observed determines the probability of the variables in _X_ missing to be missing. This setting is declined 5 times, with different weights for the logistic model. Within each one, the experiments are repeated 100 times to assess for the variability. 

▶ MNAR self-masked (Figure 8.6). Missing values in _X_ missing are introduced under a MNAR self masked mechanism. To do so, a logistic model determines the probability of each variable in _X_ missing to be missing by taking as input the exact same variable. This setting is declined 5 times, with different weights for the logistic model. Within each one, the experiments are repeated 100 times to assess for the variability. 

▶ MNAR quantile censorship (Figure 8.7). Missing values in _X_ missing are introduced under a quantile censorship MNAR mechanism. In particular, missing values are introduced at random in each _q_ -quantile of the variables in _X_ missing. _q_ varies between 0.5, 0.75, 0.8, 0.85, 0.9 and 0.95 and this way we obtain 6 different settings. Within each one, the experiments are repeated 100 times to assess for the variability. 

These experiments show that impute-then-CQR is marginally valid even under _P_ MAR and _P_ MNAR. This is expected due to Proposition 3.3 of Zaffran et al. (2023), that demonstrates that vanilla impute-then-SplitCP is marginally valid for any missing mechanism as long as the initial data set is exchangeable. However, it is not MCV, which is also expected for the same reason that the fact that it is not MCV under _P_ MCAR _,_ Y _⊥⊥_ M _|_ X. Most importantly, `CP-MDA-Nested` _[⋆]_ , through CP-MDA-Exact and CP-MDA-Nested, is both marginally valid and MCV, despite the MCAR assumption not being satisfied, even when the imputation can not retrieve more information than the features expectation (i.e., when _ϕ_ = 0). This is a positive empirical result that hints robustness of `CP-MDA-Nested` _[⋆]_ on more complex relationships between _X_ and _M_ than independence. 

_8.5. A practical glimpse on the impacts of breaking the distribution’s assumptions_ 

205 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0223-02.png)


**----- Start of picture text -----**<br>
Setting 1 Setting 2 Setting 3 Setting 4 Setting 5<br>8<br>6<br>4<br>0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9<br>Average coverage Average coverage Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>(a) Dependent Gaussian features, with ϕ  = 0 . 8.<br>Setting 1 Setting 2 Setting 3 Setting 4 Setting 5<br>12<br>10<br>8<br>6<br>4<br>0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0<br>Average coverage Average coverage Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>(b) Independent Gaussian features.<br>length<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 8.5: Same caption than Figure 8.4, for **MAR missing values** , each panel representing a different setting (set of parameters) for the missingness distribution. 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0223-04.png)


**----- Start of picture text -----**<br>
Setting 1 Setting 2 Setting 3 Setting 4 Setting 5<br>10<br>8<br>6<br>4<br>0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0<br>Average coverage Average coverage Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>(a) Dependent Gaussian features, with ϕ  = 0 . 8.<br>Setting 1 Setting 2 Setting 3 Setting 4 Setting 5<br>15 . 0<br>12 . 5<br>10 . 0<br>7 . 5<br>5 . 0<br>0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0 0 . 8 1 . 0<br>Average coverage Average coverage Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>(b) Independent Gaussian features.<br>length<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 8.6: Same caption than Figure 8.5, for **MNAR self masked missing values** . 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

206 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0224-02.png)


**----- Start of picture text -----**<br>
Censorship at quantile level 0.5 Censorship at quantile level 0.75 Censorship at quantile level 0.8<br>7<br>6<br>5<br>4<br>Censorship at quantile level 0.85 Censorship at quantile level 0.9 Censorship at quantile level 0.95<br>7<br>6<br>5<br>4<br>0 . 8 0 . 9 0 . 8 0 . 9 0 . 8 0 . 9<br>Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>(a) Dependent Gaussian features, with ϕ  = 0 . 8.<br>Censorship at quantile level 0.5 Censorship at quantile level 0.75 Censorship at quantile level 0.8<br>12<br>10<br>8<br>6<br>4<br>Censorship at quantile level 0.85 Censorship at quantile level 0.9 Censorship at quantile level 0.95<br>12<br>10<br>8<br>6<br>4<br>0 . 7 0 . 8 0 . 9 1 . 0 0 . 7 0 . 8 0 . 9 1 . 0 0 . 7 0 . 8 0 . 9 1 . 0<br>Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>(b) Independent Gaussian features.<br>length<br>Average<br>length<br>Average<br>length<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 8.7: Same caption than Figure 8.5, for **MNAR quantile censorship missing values** . 

_8.5. A practical glimpse on the impacts of breaking the distribution’s assumptions_ 

207 

## **8.5.3 Breaking** _Y ⊥⊥M |X_ **Assumption** 

Our last set experiments aim at breaking the _Y ⊥⊥ M |X_ assumption. We focus on _d_ = 3 to be able to display all of the patterns and thus better illustrate the phenomenon. We generate data with _ε ∼N_ (0 _,_ 1) _⊥⊥_ ( _X, M_ ), _X ∼N_ ( _µ,_ Σ), _µ_ = (1 _,_ 1 _,_ 1) _[T]_ , Σ = _ϕ_ (1 _,_ 1 _,_ 1) _[T]_ (1 _,_ 1 _,_ 1)+(1 _−ϕ_ ) _Id_ , _ϕ ∈{_ 0 _,_ 0 _._ 8 _}_ depending on the experiment, and _Mi ∼B_ (0 _._ 2) for any _i ∈_ �1 _,_ 3�, independently from _X_ and _ε_ . Finally: _Y_ = _X_ 11 _{M_ 1 = 0 _}_ +2 _X_ 11 _{M_ 1 = 1 _}_ + 3 _X_ 21 _{M_ 2 = 1 _, M_ 3 = 1 _}_ + _ε_ . Note that according to this data generation process, the masks for which at least _X_ 1 is missing, and the mask where _X_ 2 and _X_ 3 are missing, have important predictive power. As there are only 3 features that can be missing in this setting, Figures 8.8a and 8.8b represent the 7 different missing patterns. 

These figures highlight that in the easiest setting where the conditional expectation imputation is able to reconstruct the missing values quite accurately ( _ϕ_ = 0 _._ 8, Figure 8.8a) `CP-MDA-Nested` _[⋆]_ manages to maintain MCV. However, in the hardest case of uncorrelated features ( _ϕ_ = 0, Figure 8.8b), it does not achieve MCV as it undercovers on the masks that have predictive power. Yet, `CP-MDA-Nested` _[⋆]_ still improves upon vanilla impute-thenpredict+CQR, and in particular CP-MDA-Nested is slightly more robust than CP-MDAExact. 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

208 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0226-02.png)


**----- Start of picture text -----**<br>
QR CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 0<br>1  − α<br>0 . 5<br>20<br>10<br>(a) Dependent Gaussian features, with ϕ  = 0 . 8.<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 0<br>1  − α<br>0 . 5<br>20<br>10<br>(b) Independent Gaussian features.<br>X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing<br>X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing X Marginalfullyobserved( XX 11missing , X 2)missing( XX 22missing , X 3)missing( XX 31missing , X 3)missing<br>coverage<br>Average<br>length<br>Average<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 8.8: _Y_ and _M_ are not independent given _X_ , and the features are Gaussian dependent with _ϕ_ = 0 _._ 8. Average coverage (top) and length (bottom) as a function of the missing patterns. The first violin plot shows the marginal coverage. The marginal test set includes 2000 observations. The mask-conditional test set includes 100 individuals for each missing data pattern. 

## **Appendix to Predictive Uncertainty Quantification with Missing Covariates** 

The appendices are organized as follows. 

Section 8.A provides a the proofs for the hardness results presented in Section 8.2. 

Section 8.B contains the proofs of the Section 8.3 results. 

Section 8.C reminds the proof of leave-one-out CP in the case of randomized algorithms. Section 8.D derives `CP-MDA-Nested` _[⋆]_ theoretical validities proofs, marginal and conditional. 

## **8.A Hardness results** 

## **8.A.1 Most general distribution-free result: Theorem 8.2.1** 

- _Proof._ Let _n ∈_ N _[∗]_ the total training size (proper training and calibration). Let _α ∈_ ]0 _,_ 1[. 

   - Let _C_[�] _n,α_ be MCV, as defined in Definition 8.2.1. 

   - Let _P_ a distribution on _X × M × Y_ . 

Let _m_ 0 _∈M_ . 

Denote by _ρ_ := _PM_ ( _{m_ 0 _}_ ). 

- _�→_ Regression case. 

Let _D >_ 0. 

Define _Q_ another distribution on _X × M × Y_ such that for any _A ⊆X_ , for any _L ⊆M_ and for any _B ⊆Y_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0227-15.png)


with _R_ defined on _Y_ , uniform on [ _−D_ ; _D_ ]. 

Recall that the total variation distance between two probability distributions on _Z_ , say _P_ and _Q_ , is defined as: _TV_ ( _P, Q_ ) := sup _Z∈Z |P_ ( _Z_ ) _− Q_ ( _Z_ ) _|_ . 

On the one hand, by construction, _TV_ ( _P, Q_ ) _≤ PM_ ( _{m_ 0 _}_ ) = _ρ_ . Hence, using _n_ +1[�] Lemma 8.A.1: _TV_ ( _P[⊗]_[(] _[n]_[+1)] _, Q[⊗]_[(] _[n]_[+1)] ) _≤_ 2 1 _−_ 1 _−[ρ]_ 2[2] . Therefore, for any � � ~~�~~ � 

209 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

210 

_A ⊆X_ , for any _L ⊆M_ and for any _B ⊆Y_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0228-03.png)


On the other hand, as _C_[�] _n,α_ is MCV, it satisfies: 

Note that Λ _C_ � _n,α X_[(] _[n]_[+1)] _, m_ 0 _∩_ [ _−D_ ; _D_ ] _×_ 21 _D[≤]_[1][almost][surely.][Therefore,][using] (fy) ) Lemma 8.A.2, for any _t >_ 0: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0228-06.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0228-07.png)


Letting _D →_ + _∞_ , the result is proven. Classifcation case. 

Let _y ∈Y_ . 

_8.A. Hardness results_ 

211 

Define _Q_ another distribution on _X × M × Y_ such that for any _A ⊆X_ , for any _L ⊆M_ and for any _B ⊆Y_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0229-03.png)


with _S_ defined on _Y_ , being null everywhere except on _y_ (a dirac in _y_ ). 

On the one hand, exactly as in the regression case, by construction, _TV_ ( _P, Q_ ) _≤ n_ +1[�] _PX_ ( _E_ ) _≤ PM_ ( _m_ 0) = _ρ_ . _TV_ ( _P[⊗]_[(] _[n]_[+1)] _, Q[⊗]_[(] _[n]_[+1)] ) _≤_ 2 1 _−_ 1 _−[ρ]_ 2[2] . Therefore, for � � ~~�~~ � any _A ⊆X_ , for any _L ⊆M_ and for any _B ⊆Y_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0229-06.png)


On the other hand, as _C_[�] _n,α_ is MCV, it satisfies: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0229-08.png)


Combining with Equation (8.3), we finally get: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0229-10.png)


which concludes the proof for the classification case. 

The proof of Theorem 8.2.1 relied on the following Lemmas 8.A.1 and 8.A.2. 

**Lemma 8.A.1.** _For P and Q two probability distributions, and n ∈_ N _[∗] , it holds:_ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0229-14.png)


_Proof._ The proof of this lemma is based on the relationship between the total variation distance and the Hellinger distance between two probability distributions denoted by _H_ ( _·, ·_ ) (see Tsybakov, 2009). 

Let _n ∈_ N _[∗]_ and let _P_ and _Q_ be two probability distributions. 

On the one hand, note that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0229-18.png)


_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

212 

On the other hand, observe that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0230-03.png)


Therefore, by combining Equations (8.4) and (8.5) (that can be found in Tsybakov, 2009), we obtain the desired result. 

**Lemma 8.A.2.** _Let W be a random variable such that_ 0 _≤ W ≤_ 1 _and_ E [ _W_ ] _≥ β with β ∈_ [0 _,_ 1] _._ 

_Then, for any t >_ 0 _, it holds_ P ( _W ≥_ 1 _− t_ ) _≥_ 1 _−_[1] _[−] t[β][.]_ 

_Proof._ Let _t >_ 0. 

As _W ≤_ 1, 1 _− W ≥_ 0. Therefore, using Markov’s inequality: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0230-09.png)


Noting that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0230-11.png)


we finally get P ( _W ≥_ 1 _− t_ ) _≥_ 1 _−_[1] _[−] t[β]_[.] 

## **8.A.2 Restricting to** _P_ Y _⊥⊥_ M _|_ X **: Proposition 8.2.2** 

_Proof._ The skeleton of the proof is the exactly the same than the one of Theorem 8.2.1, with a careful attention required in the construction of the adversarial distribution _Q_ . 

Let _n ∈_ N _[∗]_ the total training size (proper training and calibration). 

Let _α ∈_ ]0 _,_ 1[. 

Let _C_[�] _n,α_ be MCV- _P_ Y _[⊗] ⊥⊥_[(] M _[n]_[+1)] _|_ X[.] 

Let _P ∈P_ Y _⊥⊥_ M _|_ X. 

Let ( _X, M, Y_ ) _∼ P_ . 

Let _m_ 0 _∈M_ such that _ρ_ := _PM_ ( _{m_ 0 _}_ ) _>_ 0. 

- _�→_ Regression case. 

Let _D >_ 0. 

We will now define _Q_ another distribution on _X × M × Y_ which is: 

- (i) close in total variation to _P_ with respect to _ρ_ ; 

- (ii) such that Assumption A1 holds (to ensure that _C_[�] _n,α_ is also MCV under _Q_ ); 

- (iii) such that there exists some subset of _X_ , say _F_ 0, which determines the event of drawing mask _m_ 0 under _Q_ . This allows to remark that 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0230-27.png)


_8.A. Hardness results_ 

213 

Let ( _X,_[˜] _M,_[˜] _Y_[˜] ) _∼ Q_ . _Q_ is built in the following way. Let _F_ 0 _⊆X_ such that _PX_ ( _F_ 0) = _ρ_ . 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0231-03.png)


Using this construction, the proof will follow as in Theorem 8.2.1. The only “tricky points” to check are (i), (ii), and (iii). 

By construction, (iii) is directly satisfied. 

Remark that by construction P ( _X, M, Y_ ) _̸_ = ( _X,_[˜] _M,_[˜] _Y_[˜] ) _≤_ 2 _δ_ (the worst case scenario � � being if _F_ 0 has been chosen such that 1 _{X ∈ F_ 0 _}_ 1 _{M_ = _m_ 0 _}[a.s.]_ = 0, leading to an equality in the previous equation). Therefore, using Lemma 8.A.3, we get that _TV_ ( _P, Q_ ) _≤_ 2 _δ_ , therefore verifying (i). 

The remaining task is to show that (ii) is satisfied. Let _B ∈Y_ . We have: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0231-08.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0231-09.png)


The idea is as previously, except that, as in the other hardness results, we replace the uniform distribution by a Dirac. In particular, let _y ∈Y_ . 

Let ( _X,_[˜] _M,_[˜] _Y_[˜] ) _∼ Q_ . _Q_ is built in the following way. 

Let _F_ 0 _⊆X_ such that _PX_ ( _F_ 0) = _ρ_ . 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0231-13.png)


The conclusion follows as in Theorem 8.2.1, since, as shown in the regression case above, _Q_ is such that: (i) _TV_ ( _P, Q_ ) _≤_ 2 _ρ_ , (ii) Assumption A1 and (iii) holds by construction. 

**Lemma 8.A.3.** _Let_ P _Z and_ P _Z′ be two distributions for the random variables X and X[′] taking their value in Z. TV_ (P _Z,_ P _Z′_ ) _≤_ P( _Z_ = _Z[′]_ ) _._ 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

214 

_Proof._ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0232-03.png)


## **8.B Link between missing covariates and uncertainty** 

## **8.B.1 Proofs for Conditional Variance results** 

## 8.B.1.1 Results under _P_ MCAR _,_ Y _⊥⊥_ M _|_ X (Proposition 8.3.1) 

_Proof._ Under the assumptions, _M ⊥⊥_ ( _Y, X_ ), and thus for any _m_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0232-08.png)


Moreover, for any _m ⊂ m[′]_ , 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0232-10.png)


8.B.1.2 Results under Gaussian Linear Model and _P_ MCAR 

Previous works (Le Morvan et al., 2020b; Ayme et al., 2022; Zaffran et al., 2023) have shown that under Model 8.3.2, _Y |_ ( _X_ obs( _m_ ) _, M_ = _m_ ) _∼N_ (˜ _µ[m] ,_ � _σ[m]_ ) for any _m ∈M_ , with: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0232-13.png)


We now provide the proof of Proposition 8.3.2. 

_8.B. Link between missing covariates and uncertainty_ 

215 

_Proof._ Consider Model 8.3.2 and assume additionally that the missing mechanism is MCAR. Therefore, for any _m ∈M_ , Σ _[m]_ = Σ. Hence, for any _m ∈M_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0233-03.png)


with Σ _[m]_ mis _|_ obs[= Σ][mis(] _[m]_[)] _[,]_[mis(] _[m]_[)] _[ −]_[Σ][mis(] _[m]_[)] _[,]_[obs(] _[m]_[)][(Σ][obs(] _[m]_[)] _[,]_[obs(] _[m]_[)][)] _[−]_[1][Σ][obs(] _[m]_[)] _[,]_[mis(] _[m]_[)][.] Let ( _m, m[′]_ ) _∈M_[2] such that _m ⊆ m[′]_ . Our goal is to show that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0233-05.png)


The marginal covariance matrix Σ can be rewritten by blocks in the following way: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0233-07.png)


where: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0233-09.png)


Additionally, assume that Σ _>_ 0 (that is, Σ is definite positive) 

Therefore, _D >_ 0 _, F >_ 0. Thus _F_ is invertible, of inverse _F[−]_[1] _>_ 0. Furthermore, _G_ := _D − EF[−]_[1] _E[T]_ is also positive definite, as it is the sum of _D >_ 0 and _EF[−]_[1] _E[T] ≥_ 0, and thus _G_ is invertible. 

Σ _[m]_ mis _|_ obs[and][Σ] _[m]_ mis _[′] |_ obs[can][be][rewritten][using][the][previous][decomposition.] On the one hand, for _m_ it gives: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0233-13.png)


_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

216 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0234-02.png)


and by denoting _H_ := _B − CF[−]_[1] _E[T]_ , we finally obtain (as _F_ is symmetric): 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0234-04.png)


On the other hand, for _m[′]_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0234-06.png)


Therefore, combining the two terms and rewriting together, we obtain: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0234-08.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0234-09.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0234-10.png)


_8.B. Link between missing covariates and uncertainty_ 

217 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0235-02.png)


## **8.B.2 Impact of the imputation under a linear quantile regression model (Proposition 8.3.3)** 

To prove Item i) of Proposition 8.3.3, we prove the following Lemma 8.B.1. 

**Lemma 8.B.1.** _Assume P_ MCAR _, and Y_ = _β[∗][T] X_ + _ε with ε s.t._ E � _ε|X_ obs( _M_ ) _, M_ � = 0 _._ 

_Then_ E � _Y |X_ obs( _M_ ) _, M_ � = _β[∗][T]_ Φconditional mean( _X, M_ ) _, with_ Φconditional mean _the imputation by the conditional mean. Furthermore, if the covariates are independent, then_ E � _Y |X_ obs( _M_ ) _, M_ � = _β[∗][T]_ Φmean( _X, M_ ) _, with_ Φmean _the imputation by the mean. Proof._ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0235-07.png)


To prove Item ii) of Proposition 8.3.3, we prove the following Proposition 8.B.1. Indeed, the oracle predictive intervals vary at least once in length we respect to the patterns, as, on the one hand, under _P_ MCAR _,_ Y _⊥⊥_ M _|_ X Equation (Len-2) holds and, on the other hand, when _Y ̸⊥⊥ X_ the variance of _Y_ given _X_ is different than the overall variance of _Y_ . 

**Proposition 8.B.1** (Non-adaptivity of the linear quantile regression) **.** _Assume that:_ 

_i) the quantile regression is learned within the class of linear models;_ 

- _ii) the (random) values used to impute have the same expectation than the feature itself, i.e.,_ E [Φ( _X, m_ ) _|M_ = _m_ ] = E [ _X_ ] _for any m ∈M such that_ P( _M_ = _m_ ) _>_ 0 _._ 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

218 

_Then the expectation of the predictive intervals length is independent of the missing pattern._ 

_Proof._ Since the quantile regression is learned within the class of linear models, the fitted � quantile functions (upper and lower) can be written as _qδ_ ( _z_ ) = _βδ[T][z]_[ +] _[ β] δ_[0][,][with] _[β][∈]_[R] _[d]_ and _β_[0] _∈_ R. Therefore, the length of the resulting interval _Lα_ at some—imputed—point Φ( _X_ obs( _M_ ) _, M_ ) will be: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0236-04.png)


with _δ_ ( _l_ ) and _δ_ ( _u_ ) chosen by the user or fixed by the algorithm such that _δ_ ( _u_ ) _− δ_ ( _l_ ) = 1 _− α_ . Thus: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0236-06.png)


Let _m ∈M_ such that P( _M_ = _m_ ) _>_ 0. Conditioning by _m_ : 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0236-08.png)


Given the assumption that E �Φ( _X_ obs( _M_ ) _, M_ ) _|M_ = _m_ � = E [ _X_ ], one can conclude that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0236-10.png)


## **8.C Leave-one-out predictive sets for randomized algorithms** 

We provide in this section a more detailed proof of leave-one-out or _k_ -fold cross-conformal (Vovk, 2015) and jackknife+ (Barber et al., 2021b) methods which allows us to highlight where exactly the arguments of data exchangeability and symmetrical algorithm play a role. In particular, by emphasizing these precise influences, we can understand how to include a non-deterministic symmetrical algorithm (such as Random Forest or Stochastic Gradient Descent). 

## **8.C.1 On the definition of randomized symmetric algorithms** 

**Definition 8.C.1** (Randomized learning algorithm) **.** A randomized learning algorithm is defined as: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0236-15.png)


where _ξ_ encodes the randomness of _A_ . 

_8.C. Leave-one-out predictive sets for randomized algorithms_ 

219 

**Definition 8.C.2** (Randomized symmetric algorithm (Kim and Barber, 2023)) **.** A randomized learning algorithm _A_ is symmetric if for any data set � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[,][for][any] permutation _σ_ on �1 _, n_ �, there exists a coupling that maps _ξ ∼U_ ([0 _,_ 1]) to _ξ[′] ∼U_ ([0 _,_ 1]), which depends only on _σ_ , s.t.: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0237-03.png)


## **8.C.2 Detailing leave-one-out conformal predictors validity proof** 

Let � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1][be][exchangeable,][and] _[A]_[a][(possible][randomized)][symmetric][algorithm.] Let _s_ be a conformity score function. For _i ∈_ �1 _, n_ �, denote _A_[ˆ] _−i_ ( _·_ ) := _A X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1 , �� _k_ = _i_ � that is the fitted left-one-out algorithm, removing data point _i_ . 

Consider the leave-one-out conformal estimator as: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0237-07.png)


Previous works (Barber et al., 2021b; Gupta et al., 2022) have proven that under exchangeability of � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1][and][symmetry][of] _[A]_[,][P] � _Y_[(] _[n]_[+1)] _∈ C_[�] _n,α_[LOO] � _X_[(] _[n]_[+1)][��] _≥_ 1 _−_ 2 _α_ . We recall below the key proof’s steps, detailing the last one which uses the exchangeability and symmetry arguments. 

**Step 1.** Remark that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0237-10.png)


with _S_[(] _[i]_[)] _[,j]_ := _s_ � _X_[(] _[i]_[)] _, Y_[(] _[i]_[)] ; _A_[ˆ] _−_ ( _i,j_ )� the score on data point _i_ of the predictor that has been fitted without seeing nor data point _i_ nor data point _j_ , for ( _i, j_ ) _∈_ �1 _, n_ + 1�[2] and extending ˆ ˆ _A−i_ to _A−_ ( _i,j_ ) := _A X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n]_[+1] _k_ =1 , where the _n_ + 1 data point is added. �� _k/∈{i,j}_ � Denote by C _A_ the function building the comparison matrix _C ∈{_ 0 _,_ 1 _}_[(] _[n]_[+1)] _[×]_[(] _[n]_[+1)] : C _A_ �� _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1] � _i,j_[=][ 1] � _S_[(] _[i]_[)] _[,j] > S_[(] _[j]_[)] _[,i]_[�] = _Ci,j_ . 

_n_ +1 **Step 2.** Deterministically, Barber et al. (2021b) shows that # _{i ∈_ �1 _, n_ + 1� : � _Ci,j ≥ j_ =1 (1 _− α_ )( _n_ + 1) _} ≤_ 2 _α_ ( _n_ + 1). This is shown for _any_ comparison matrix. 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

220 

**Step 3.** The last (and crucial) step of leave-one-out conformal predictors is to show that _d_ for any permutation _σ_ on �1 _, n_ + 1� it holds: � _Cσ_ ( _i_ ) _,σ_ ( _j_ )� _i,j_ = ( _Ci,j_ ) _i,j_ . 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0238-03.png)


Thus, leveraging the fact that _ξσ[′][⊥⊥]_ � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1][and][that] � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1][are][exchange-] able, we obtain that: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0238-05.png)


_d_ Hence, for any permutation _σ_ on �1 _, n_ + 1� it holds that Π _[T] σ[C]_[Π] _[σ]_ = _C_ , concluding the proof as then each element of �1 _, n_ + 1� is equally likely to belong to _{i ∈_ �1 _, n_ + 1� : _n_ +1 � _Ci,j ≥_ (1 _− α_ )( _n_ + 1) _}_ . _j_ =1 

## **8.D Theory on** `CP-MDA-Nested` _[⋆]_ **and CP-MDA-Nested** 

Let us first remark that _C_[�] _n,α_[MDA-Nested] _[⋆]_ ( _·_ ) _⊆ C_[�] _n,α_[MDA-Nested] ( _·_ ) when the conformity score function outputs intervals and Cal = Cal[�] (Remark 8.4.1). 

_Proof._ 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0238-10.png)


_8.D. Theory on_ _`CP-MDA-Nested`[⋆] and CP-MDA-Nested_ 

221 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0239-02.png)


Therefore, any upper bound on the miscoverage of `CP-MDA-Nested` _[⋆]_ extends to CPMDA-Nested. 

## **8.D.1 Marginal validity of** `CP-MDA-Nested` _[⋆]_ **.** 

The proof of Theorem 8.4.1 is highly inspired by the leave-one-out conformal predictors proof, from Barber et al. (2021b) and detailed previously in Section 8.C. 

_Proof._ One can see this proof as analogous of the one of leave-one-out conformal predictors, where “predicting on point _i_ with point _j_ left out” corresponds to “predicting on point _i_ when additionally masking it with the mask of point _j_ ”. 

## **Step 1.** 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0239-08.png)


where we defined _S_[(] _[i]_[)] _[,j]_ := _s X_[(] _[i]_[)] _,_ max � _M_[(] _[i]_[)] _, M_[(] _[j]_[)][��] _, Y_[(] _[i]_[)] ; _A_[ˆ] (Φ ( _·, ·_ ) _, ·_ ) , that is the score �� � of the point _i_ when the mask of the point _j_ is applied to it, on top of its own mask _M_[(] _[i]_[)] . 

**Step 2.** Define the comparison matrix _C ∈{_ 0 _,_ 1 _}_[(#Cal+1)] _[×]_[(#Cal+1)] , s.t. for ( _i, j_ ) _∈_ (Cal _∪{n_ + 1 _}_ )[2] : _Ci,j_ = 1 � _S_[(] _[i]_[)] _[,j] > S_[(] _[j]_[)] _[,i]_[�] . Hence, we now have (since by definition _Cn_ +1 _,n_ +1 = 0): 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0239-11.png)


_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

222 

Denote _W_ ( _C_ ) = _{i ∈_ Cal _∪{n_ +1 _}_ : � _Ci,k ≥_ (1 _− α_ )(#Cal +1) _}_ . We can re-write: _k∈_ Cal _∪{n_ +1 _}_ 

� _Y_[(] _[n]_[+1)] _∈/ C_[�] _n,α_[MDA-Nested] _[⋆]_ � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][��] = _{n_ + 1 _∈ W_ ( _C_ ) _} ._ Therefore P � _Y_[(] _[n]_[+1)] _∈/ C_[�] _n,α_[MDA-Nested] _[⋆]_ � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][��] = P _{n_ + 1 _∈ W_ ( _C_ ) _}_ . Thus, we will now bound P _{n_ + 1 _∈ W_ ( _C_ ) _}_ . 

Again, # _W_ ( _C_ ) _≤_ 2 _α_ (#Cal + 1) deterministically (Barber et al., 2021b). 

**Step 3.** To conclude the proof, observe that the matrix _C_ can be viewed as the output of a deterministic function C of the exchangeable (by A2) sequence � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1][:] _C_ = C �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1] �. Thus, for any permutation _σ_ on Cal _∪{n_ + 1 _}_ , it holds: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0240-06.png)



![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0240-07.png)


## **8.D.2 MCV of** `CP-MDA-Nested` _[⋆]_ 

To prove that `CP-MDA-Nested` _[⋆]_ and CP-MDA-Nested are MCV- _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[,][we][leverage] again the parallel with leave-one-out conformal predictors, but this time seeing the missing pattern as exogenous randomness, which is possible when working with distributions in _P_ MCAR _,_ Y _⊥⊥_ M _|_ X. 

_Proof._ Under _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[, it holds that] _[ M]_[(] _[n]_[+1)] _[⊥⊥]_ �� _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[,]_ � _X_[(] _[n]_[+1)] _, Y_[(] _[n]_[+1)][��] . Thus the sequence �� _X_[(] _[k]_[)] _, M_[(] _[n]_[+1)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[,]_ � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)] _, Y_[(] _[n]_[+1)][��] is exchangeable conditionally to _M_[(] _[n]_[+1)] . 

Remark now that for any ( _X, M, Y_ ) _∈X × M × Y_ , we can rewrite the score on this point with augmented mask _M_[�] := max � _M, M_[(] _[n]_[+1)][�] as: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0240-12.png)


where, for an additional mask _M[′] ∈M_ , Φ ([�] _X, M_ ; _M[′]_ ) := Φ ( _X,_ max ( _M, M[′]_ )) and similarly � ˆ _A_ ( _X, M_ ; _M[′]_ ) := _A_ ( _X,_ max ( _M, M[′]_ )). 

_8.D. Theory on_ _`CP-MDA-Nested`[⋆] and CP-MDA-Nested_ 

223 

Thus, we can re-write `CP-MDA-Nested` _[⋆]_ as: 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0241-03.png)


Therefore, an equivalent rewriting of `CP-MDA-Nested` _[⋆]_ is a specific instance of what is presented in Algorithm 18, where the differences with `CP-MDA-Nested` _[⋆]_ (Algorithm 16) are highlighted through green text. 

**Algorithm 18** MDA based on random masks 


![](markdown_output/Zaffran_PhD_Manuscript_images/Zaffran_PhD_Manuscript.pdf-0241-06.png)


Indeed, conditionally on _M_[(] _[n]_[+1)] , we can apply Algorithm 18 to the modified data set � _X_[(] _[k]_[)] _, M_[(] _[n]_[+1)] _, Y_[(] _[k]_[)][�] _k∈_ Cal[�][,][by][using][the] � _M_[(] _[k]_[)][�] _k∈_ Cal[�][as][random][draw][for][(] _[ν][k]_[)] _k∈_ Cal[�][in][line] 3. This is legit only when the distribution of � _X_[(] _[k]_[)] _, M_[(] _[n]_[+1)] _, Y_[(] _[k]_[)][�] _k∈_ Cal[�] _∪{n_ +1 _}_[belongs][to] Cal+1) _P_ MCAR _[⊗]_[(#][�] _,_ Y _⊥⊥_ M _|_ X[,][as][then][for][any] _[k][∈]_ Cal[�] , it holds that _M_[(] _[k]_[)] _⊥⊥_ � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)] _, X_[(] _[n]_[+1)] _, Y_[(] _[n]_[+1)][�] . This Algorithm 18 is a special case of leave-one-out CP presented in Section 8.C, with a randomized algorithm that only returns a pre-determined function associated with a parameter value, without fitting anything on the _n −_ 1 data points. Therefore, the validity result of leave-one-out CP extends to Algorithm 18. 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

224 

In particular, under _P_ MCAR _[⊗]_[(] _[n]_[+1)] _,_ Y _⊥⊥_ M _|_ X[,] `[CP-MDA-Nested]` _[⋆]_[corresponds][to][applying][Algo-] rithm 18 to the data set � _X_[(] _[k]_[)] _, M_[(] _[n]_[+1)] _, Y_[(] _[k]_[)][�] _k∈_ Cal[which][is][exchangeable][conditionally][on] _M_[(] _[n]_[+1)] , and by using in line 3 the � _M_[(] _[k]_[)][�] _k∈_ Cal[as][random][draw][for][(] _[ν][k]_[)] _[k][∈]_[Cal][.][Therefore,] `CP-MDA-Nested` _[⋆]_ is MCV- _P[⊗]_[(] _[n]_[+1)][the][level][1] _[ −]_[2] _[α]_[.] MCAR _,_ Y _⊥⊥_ M _|_ X[at] 

The idea in this re-writing is to see that, conditionally on _M_[(] _[n]_[+1)] , `CP-MDA-Nested` _[⋆]_ predicting on the test point � _X_[(] _[n]_[+1)] _, M_[(] _[n]_[+1)][�] given the data set � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[,][is] in fact another run of `CP-MDA-Nested` _[⋆]_ which predicts on a complete test point _X_[˘][(] _[n]_[+1)] _∈ X_[˘] , where _X_[˘] is the set of dimension _|_ obs � _M_[(] _[n]_[+1)][�] _|_ containing only the observed dimensions of _X_ according to _M_[(] _[n]_[+1)] , given the cropped data set _X_ ˘[(] _[k]_[)] _, M_ ˘[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n]_[with] _M_[˘][(] _[k]_[)] _∈ M_[˘] � _k_ =1[,] that, similarly to _X_[˘] , is the set of dimension _|_ obs � _M_[(] _[n]_[+1)][�] _|_ containing only the observed dimensions of _M_ according to _M_[(] _[n]_[+1)] . 

## **Part IV** 

## **Conclusion and perspectives** 

225 

_8.D. Theory on_ _`CP-MDA-Nested`[⋆] and CP-MDA-Nested_ 

227 

## **Conclusion** 

In this thesis, we have studied several aspects of post-hoc predictive uncertainty quantification approaches, and in particular conformal methods, motivated by the goal of forecasting electricity prices. However, the methods that we developed are generic enough to be applied in any sensitive field. 

Our first contribution provides an extension of Conformal Prediction (CP) to time series forecasting, a challenging context as time series are not exchangeable, the only assumption of conformal prediction. Namely, we start by studying theoretically the efficiency of Adaptive Conformal Inference (ACI, Gibbs and Candès, 2021) depending on its learning rate _γ_ using Markov Chain theory. The results emphasize that _i_ ) on exchangeable residuals, ACI’s efficiency worsens linearly in _γ_ with respect to standard CP, and _ii_ ) when the residuals are auto-regressive, there exists an optimal _γ[∗] >_ 0 that depends on the auto-regressive coefficient in a non-monotonic fashion. Therefore, we propose an adaptive algorithm, coined `AgACI` , that wraps around ACI using online aggregation under expert advice to avoid having to choose _γ_ . Finally, we perform extensive synthetic experiments with benchmarks methods that underline the benefits brought by ACI with a well-chosen _γ_ and by our proposed algorithm. We conclude with an application to French electricity prices forecasting in 2019, leading to the same conclusion. 

We deepen this application in our second contribution, which focuses on probabilistic forecasting of French electricity prices in the demanding years 2020 and 2021. Our goal is to understand to which extent it is possible to adaptively post-process existing probabilitistic forecasts so as to be more robust to sudden important non-stationarity. First, we construct a novel explanatory variable that demonstrates great interest empirically: the nuclear availability. Then, we conduct extensive numerical experiments that emphasizes _i_ ) the need for more adaptivity as none of them achieves nominal coverage, and _ii_ ) the difficulty of choosing one given model. By adding either a layer of conformalization—in an appropriate way that respect the temporal structure, such as our new proposal `OSSCP-horizon` or `AgACI` —or a layer of online aggregation, the coverage is improved, even in late 2021, while preserving informativeness. We highlight that aggregating various `AgACI` , each one of them being based on different individual forecasters, provides enhanced performances, and simultaneously reveals key aspects of the markets. 

Our third contribution moves away from time series to focus on predictive uncertainty quantification with missing values. We consider impute-then-predict strategies, topped with CP. We first show that this plugged-in approach ensures marginal validity for any missingness distribution and almost all imputation function. However, by examining a Gaussian linear model, we find out that missing values induce heteroskedasticity, that is not taken into account by CP. This leads to uneven coverage depending on the missing pattern. Therefore, we suggest two algorithms, relying on the core idea of Missing Data Augmentation (MDA), and prove that they are valid conditionally to the patterns of missing values, despite their exponential number, under independence assumptions. We then show that a universally consistent quantile regression algorithm trained on the imputed data is Bayes optimal for the pinball risk, thus achieving valid coverage conditionally to any given 

_Chapter 8. Predictive Uncertainty Quantification with Missing Covariates_ 

228 

data point. Finally, synthetic experiments along with real critical care data application support our theory and reflect improved performance of our MDA methods. 

Our last contribution constitutes a deep delve into when and how it is possible to build predictive sets that are valid conditionally on the missing pattern. We start by proving hardness results that justify the independence assumptions made by MDA’s algorithms: without these assumptions, any method that is valid conditionally on the missing pattern outputs predictive sets that includes almost all the label space. Then, we characterize the interplay between missing values and predictive uncertainty quantification in (Gaussian) linear models or under non-parametric assumptions on the data distribution. Precisely, we illustrate in some cases that the predictive uncertainty increases with more missing values by providing various formal quantifications of this statement, and that even when the features are independent from the missing pattern it is crucial to allow the predictive model to know the missing pattern. In a third part, we bridge the gap between the two algorithms of MDA, providing a wide range of MDA methods in `CP-MDA-Nested` _[⋆]_ , and extending them to classification. Leveraging the unified framework, we are able to obtain stronger theoretical guarantees on its validity. Lastly, we test the robustness of MDA on synthetic experiments breaking the independence assumptions. This emphasizes that an important dependence between the missing patterns and the covariates does not undermine MDA’s mask-conditional-validity, yet this is not true for the link between the response and the missing pattern. 

## **Open directions** 

Following these works, several exciting perspectives are raised, beyond the ones mentioned in conclusion of each individual chapter. 

**Multidimensional predictive uncertainty quantification (** _**ongoing work**_ **).** All of the methods discussed in this manuscript produce a one dimensional predictive set. A natural question is: do they extend to a multidimensional response? For instance, we could wish to forecast the electricity prices of different market and in different countries simultaenously. As long as we design a score function that maps any point that belongs to the multidimensional _Y_ onto a unidimensional quantity (Feldman et al., 2023; Cauchois et al., 2021), the theory presented will follow. However, such an approach does not take into account correlation and dependences between the uncertainty themselves, as it models the predictive uncertainty as a scalar quantity. 

Therefore, an informative design’ choice would be to define a score function that takes its value in a multidimensional space too. But then, to leverage CP framework, we would need to compute the empirical quantile of these multidimensional scores. However, defining multivariate quantiles is demanding as there is no canonical ordering on multivariate spaces. One historical solution could be to resort to Tukey’s depth (Tukey, 1975) but it requires making distributional assumptions. To overcome this limitation, leveraging tools from the optimal transport literature, specifically Monge-Kantorovich ranks (Chernozhukov et al., 2017; Hallin et al., 2021), seems promising. 

_8.D. Theory on_ _`CP-MDA-Nested`[⋆] and CP-MDA-Nested_ 

229 

**Missing values.** Our MDA approach achieves Mask-Conditional-Validity (MCV) by assuming independence between the mask _M_ and the covariates _X_ , as well as between the mask and the response _Y_ given the covariates. In Chapter 8, we showed that we can not hope to achieve MCV without constraining the link between _M_ and _X and_ the link between _M_ and _Y_ . Relaxing the assumption of _Y ⊥⊥M |X_ seems to be particularly tricky as even the task of point-prediction (without uncertainty quantification) can be very challenging in this situation (Ayme et al., 2022). However, aiming at MCV on MAR and _Y ⊥⊥M |X_ distribution appears more within our reach. Indeed, an idea would be to build on causal inference tools (J. M. Robins, 1994; Hirano et al., 2003), such as inverse propensity weights. The underpinning idea is that while the conformity scores are still exchangeable with missing values, they are not exchangeable conditional on the mask, and under MAR mechanism we could learn the weights allowing to obtain weighted exchangeability conditional on the mask. 

Another attractive path is to leverage isotonic regression (Barlow et al., 1972) to design an uncertainty quantification model conveying the core idea that more `NA` s induce more uncertainty, relying on the key observation that we do not need an ordering on the whole _M_ but only between nested patterns. 

**Broader point of view on Part III – Missing Values.** The fundamental idea in both Chapters 7 and 8 is that even though the predictive distributions vary with the missing pattern, we are able to improve our predictive uncertainty quantification on one of these distributions thanks to the other ones. In fact, this idea echoes with domain adaptation questions, and it would be interesting to see how to broaden our analysis. Especially, as discussed in Chapter 8, our theoretical results – on the hardness part as well as on the MCV of our methodology – do not take any advantage of the specificity of missingness and they extend directly to any features’ group. However, our algorithms’ design relies on the core idea that we can modify the historical data to match the test domain. This is easy with missing values, but appears trickier beyond. Finding concrete other applications that would be compatible with our framework is appealing. 

**On leave-one-out CP approaches.** To prove the MCV of our generalized MDA framework, we relied on the deep similarities with leave-one-out CP approaches based on some randomized algorithm _A_ . This uncloaked an interesting basics question on such approaches. As we do not require anymore the assumption of stochastic domination of the quantiles, it remains unclear as to why `MDA-Nested` overcovers. Our preliminary investigations highlight that leave-one-out CP approaches also suffer from over-cover when plugged in with an algorithm that is a mixture of deterministic predictors. Especially, assume that fitting _A_ corresponds to randomly choosing (by drawing from a Bernoulli of parameter _ρ_ ) between two pre-determined estimated regressors. Then, when _ρ_ equals either 0 or 1, we retrieve Split CP, achieving (nearly) exactly 1 _− α_ coverage. When _ρ ∈_ ]0 _,_ 1[, experimentally we observe over-coverage. The question now is: what drives the coverage behavior in between these two extremes? The answer seems unclear for now, and is in fact related to the more general question of why _K_ -fold CP over-covers but not leave-one-out 

CP? (see the experiments and especially Figure 2 in Barber et al., 2021b) This is coherent with our finding as _i_ ) `MDA-Nested` is in fact close to _K_ -fold CP since several occurence of the same augmented mask are present in the calibration set, and _ii_ ) our experiments on mixture of deterministic predictors also corresponds to multiple repetition of the same predictor which is what happend in _K_ -fold CP. Therefore, this over-covering phenomenon appears to impact randomized algorithms beyond MDA, and it is thus crucial to understand. 

**On the implications of the theoretical properties.** A broader and more fundamental perspective of post-hoc finite sample distribution-free uncertainty quantification is how the different theoretical properties (marginal and different notion of conditional validity, efficiency) intertwin. While all of these properties appear to be rooted into practice, the link between them is not well understood. For example: 

- i) We can show that optimizing one can be detrimental to another: for some distributions the smallest prediction set is only marginal, as achieving conditional coverage would then increase the predictive set size. How efficiency and features-conditionality interact? 

- ii) In Chapter 8, our hardness results (but seen with the lens of general groups instead of missing pattern) make one step in the direction of understanding how the efficiency depends on the calibration size. However, they only characterize the probability of uninformative sets, and the rest of the distribution remain uncharacterized. Can we derive theoretical results on the expected length depending on the calibration size? This would shed light on the practicality of binning the calibration set in order to achieve approximate conditional coverage. 

- iii) Efficiency is substantially used to assess the performances of predictive sets. In Chapter 5, we have discussed extensively on the impact of infinite intervals and their impact on how to qualify a method as informative, and we ended up relying on the empirical median length instead of the empirical average length. Why should we assess efficiency through the mean and not the median? 

Characterizing theoretically the interplays between all metrics is necessary to guide practice and design informed decision-making pipelines based on predictive uncertainty quantification. Indeed, identifying what can be deduced from a property and then used by external agents, depends on how this property connects to other practical requirements, i.e., other metrics. 

## **Bibliography** 

- L. Amabile, D. Bresch-Pietri, G. El Hajje, S. Labbé, and N. Petit. Optimizing the self-consumption of residential photovoltaic energy and quantification of the impact of production forecast uncertainties. _Advances in Applied Energy_ , 2:100020, 2021. (p. 113.) 

- Y. Amara-Ouali, M. Fasiolo, Y. Goude, and H. Yan. Daily peak electrical load forecasting with a multi-resolution approach. _International Journal of Forecasting_ , 39(3):1272–1286, 2023. (p. 119.) 

- A. N. Angelopoulos and S. Bates. Conformal prediction: A gentle introduction. _Foundations and Trends® in Machine Learning_ , 16(4), 2023. (pp. 34, 67, 140, 157, 161, and 195.) 

- A. N. Angelopoulos, E. J. Candes, and R. J. Tibshirani. Conformal PID Control for Time Series Prediction. In _Advances in Neural Information Processing Systems_ , 2023. (pp. 55 and 125.) 

- A. N. Angelopoulos, R. F. Barber, and S. Bates. Online conformal prediction with decaying step sizes, 2024. (pp. 55 and 125.) 

- A. Ayme, C. Boyer, A. Dieuleveut, and E. Scornet. Near-optimal rate of consistency for linear models with missing values. In K. Chaudhuri, S. Jegelka, L. Song, C. Szepesvari, G. Niu, and S. Sabato, editors, _Proceedings of the 39th International Conference on Machine Learning_ , 162, 1211–1243. PMLR, 2022. (pp. 137, 141, 153, 159, 178, 190, 214, and 229.) 

- A. Ayme, C. Boyer, A. Dieuleveut, and E. Scornet. Naive imputation implicitly regularizes high-dimensional linear models. In A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and J. Scarlett, editors, _Proceedings of the 40th International Conference on Machine Learning_ , 202 of _Proceedings of Machine Learning Research_ , 1320–1340. PMLR, 23–29 Jul 2023. (pp. 178 and 193.) 

- A. Ayme, C. Boyer, A. Dieuleveut, and E. Scornet. Random features models: a way to study the success of naive imputation, 2024. (pp. 178 and 193.) 

- M. S. Bakare, A. Abdulkarim, M. Zeeshan, and A. N. Shuaibu. A comprehensive overview on demand side energy management towards smart grids: challenges, solutions, and future direction. _Energy Informatics_ , 6(1), Mar. 2023. (p. 6.) 

231 

- R. F. Barber, E. J. Candès, A. Ramdas, and R. J. Tibshirani. The limits of distribution-free conditional predictive inference. _Information and Inference: A Journal of the IMA_ , 10 (2), 2021a. (pp. 25, 41, 146, 154, 177, and 183.) 

- R. F. Barber, E. J. Candès, A. Ramdas, and R. J. Tibshirani. Predictive inference with the jackknife+. _The Annals of Statistics_ , 49(1), 2021b. (pp. 46, 48, 49, 141, 145, 157, 182, 194, 199, 200, 218, 219, 221, 222, and 230.) 

- R. F. Barber, E. J. Candès, A. Ramdas, and R. J. Tibshirani. Conformal prediction beyond exchangeability. _The Annals of Statistics_ , 51(2), Apr. 2023. (pp. 53 and 157.) 

- R. E. Barlow, D. J. Bartholomew, J. M. Bremner, and H. D. Brunk. _Statistical inference under order restrictions: Theory and application of isotonic regression_ . John Wiley & Sons, 1972. (p. 229.) 

- O. Bastani, V. Gupta, C. Jung, G. Noarov, R. Ramalingam, and A. Roth. Practical adversarial multivalid conformal prediction. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc., 2022. (pp. 55 and 125.) 

- J. Berrisch and F. Ziel. Crps learning. _Journal of Econometrics_ , 237(2):105221, 2023. (pp. 74 and 122.) 

- J. Berrisch and F. Ziel. Multivariate probabilistic crps learning with an application to day-ahead electricity prices. _International Journal of Forecasting_ , 2024a. (p. 114.) 

- J. Berrisch and F. Ziel. _The profoc Package: An R package for probabilistic forecast combination using CRPS Learning_ , 2024b. R package version 1.3.1. (p. 122.) 

- A. Bhatnagar, H. Wang, C. Xiong, and Y. Bai. Improved online conformal prediction via strongly adaptive online learning. In A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and J. Scarlett, editors, _Proceedings of the 40th International Conference on Machine Learning_ , 202 of _Proceedings of Machine Learning Research_ , 2337–2363. PMLR, 23–29 Jul 2023. (pp. 55 and 125.) 

- M. Bian and R. F. Barber. Training-conditional coverage for distribution-free predictive inference. _Electronic Journal of Statistics_ , 17(2):2044–2066, 2023. (p. 51.) 

- R. Bjorgan, C.-C. Liu, and J. Lawarree. Financial risk management in a competitive electricity market. _IEEE Transactions on power systems_ , 14(4):1285–1291, 1999. (p. 114.) 

- D. Bunn, A. Andresen, D. Chen, and S. Westgaard. Analysis and forecasting of electricty price risks with quantile factor models. _The Energy Journal_ , 37(1), 2016. (p. 113.) 

- E. Burnaev and V. Vovk. Efficiency of conformalized ridge regression. In M. F. Balcan, V. Feldman, and C. Szepesvári, editors, _Proceedings of The 27th Conference on Learning Theory_ , 35 of _Proceedings of Machine Learning Research_ , 605–622, Barcelona, Spain, 13–15 Jun 2014. PMLR. (p. 45.) 

- Y. Cai and N. Davies. A simple bootstrap method for time series. _Communications in Statistics-Simulation and Computation_ , 41(5):621–631, 2012. (p. 101.) 

- E. Candès, L. Lei, and Z. Ren. Conformalized survival analysis. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 85(1):24–45, Jan. 2023. (p. 52.) 

- M. Cauchois, S. Gupta, and J. C. Duchi. Knowing what you know: valid and validated confidence sets in multiclass and multilabel prediction. _Journal of Machine Learning Research_ , 22(81):1–42, 2021. (pp. 26 and 228.) 

- M. Cauchois, S. Gupta, A. Ali, and J. C. Duchi. Robust validation: Confident predictions even when distributions shift. _Journal of the American Statistical Association_ , page 1–66, Feb. 2024. (pp. 53 and 68.) 

- N. Cesa-Bianchi and G. Lugosi. _Prediction, learning, and games_ . Cambridge University Press, 2006. (pp. 58, 73, 74, 114, 122, and 125.) 

- W. Chen, Z. Wang, W. Ha, and R. F. Barber. Trimmed conformal prediction for highdimensional models, 2016. (p. 45.) 

- W. Chen, K. Chun, and R. F. Barber. Discretized conformal prediction for efficient distribution-free inference. _Stat_ , 7(1), Jan. 2018. (p. 45.) 

- V. Chernozhukov, A. Galichon, M. Hallin, and M. Henry. Monge–Kantorovich depth, quantiles, ranks and signs. _The Annals of Statistics_ , 45(1):223 – 256, 2017. (p. 228.) 

- V. Chernozhukov, K. Wüthrich, and Z. Yinchu. Exact and Robust Conformal Inference Methods for Predictive Machine Learning with Dependent Data. In _Conference On Learning Theory_ . PMLR, 2018. (pp. 51, 68, and 123.) 

- V. Chernozhukov, K. Wüthrich, and Y. Zhu. Distributional conformal prediction. _Proceedings of the National Academy of Sciences_ , 118(48), 2021. (p. 26.) 

- G. Cherubin, K. Chatzikokolakis, and M. Jaggi. Exact optimization of conformal predictors via incremental and decremental learning. In _Proceedings of the 38th International Conference on Machine Learning_ . PMLR, 2021. (p. 45.) 

- C. Cornell, N. T. Dinh, and S. A. Pourmousavi. A probabilistic forecast methodology for volatile electricity prices in the australian national electricity market. _International Journal of Forecasting_ , 2024. (p. 114.) 

- M. Dashevskiy and Z. Luo. Network traffic demand prediction with confidence. In _IEEE Global Telecommunications Conference_ . IEEE, 2008. (p. 68.) 

- M. Dashevskiy and Z. Luo. Time series prediction with performance guarantee. _IET communications_ , 5(8):1044–1051, 2011. (p. 68.) 

- T. Deschatre, O. Féron, and P. Gruet. A survey of electricity spot and futures price models for risk management applications. _Energy Economics_ , 102:105504, 2021. (p. 114.) 

- T. Ding, A. Angelopoulos, S. Bates, M. Jordan, and R. J. Tibshirani. Class-conditional conformal prediction with many classes. In A. Oh, T. Neumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, _Advances in Neural Information Processing Systems_ , 36, 64555–64576. Curran Associates, Inc., 2023. (p. 42.) 

- D. Dua and C. Graff. UCI machine learning repository, 2017. (p. 149.) 

- M. L. Eaton. _Multivariate statistics_ . John Wiley & Sons, Nashville, TN, 1983. (p. 158.) 

- EU-2017/2195. Commission Regulation (EU) 2017/2195 of 23 November 2017 establishing a guideline on electricity balancing (text with EEA relevance.). `https://eur-lex.europa. eu/eli/reg/2017/2195/oj` . Published: 2017-11-23. (p. 6.) 

- EUPHEMIA. Euphemia public description, single price coupling algorithm, April 2019. (p. 79.) 

- C. Fannjiang, S. Bates, A. N. Angelopoulos, J. Listgarten, and M. I. Jordan. Conformal prediction under feedback covariate shift for biomolecular design. _Proceedings of the National Academy of Sciences_ , 119(43):e2204569119, 2022. (p. 52.) 

- M. Fasiolo, S. N. Wood, M. Zaffran, R. Nedellec, and Y. Goude. Fast calibrated additive quantile regression. _Journal of the American Statistical Association_ , 116(535):1402–1412, mar 2020. (p. 119.) 

- M. Fasiolo, S. N. Wood, M. Zaffran, R. Nedellec, and Y. Goude. qgam: Bayesian nonparametric quantile regression modeling in R. _Journal of Statistical Software_ , 100(9):1–31, 2021. (p. 119.) 

- S. Feldman, S. Bates, and Y. Romano. Calibrated multiple-output quantile regression with representation learning. _Journal of Machine Learning Research_ , 24(24):1–48, 2023. (p. 228.) 

- France-2023-491. Loi n° 2023-491 du 22 juin 2023 relative à l’accélération des procédures liées à la construction de nouvelles installations nucléaires à proximité de sites nucléaires existants et au fonctionnement des installations existantes. `https://www.legifrance. gouv.fr/loda/id/JORFTEXT000047715784/` . Published: 2023-06-22. (p. 5.) 

- J. H. Friedman. Greedy function approximation: a gradient boosting machine. _Annals of statistics_ , 1189–1232, 2001. (p. 119.) 

- J. H. Friedman, E. Grosse, and W. Stuetzle. Multidimensional additive spline approximation. _SIAM J. Sci. Stat. Comput._ , 1983. (p. 75.) 

- P. Gaillard and Y. Goude. _OPERA_ , 2021. R package version 1.2.0. (pp. 74 and 122.) 

- P. Gaillard, G. Stoltz, and T. Van Erven. A second-order bound with excess losses. In _Conference on Learning Theory_ , 176–196. PMLR, 2014. (p. 74.) 

- P. Gaillard, Y. Goude, and R. Nedellec. Additive models and robust aggregation for GEFCom2014 probabilistic electric load and electricity price forecasting. _International Journal of Forecasting_ , 32(3):1038–1050, 2016. (p. 67.) 

- I. Gibbs and E. Candès. Adaptive conformal inference under distribution shift. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc., 2021. (pp. v, vii, 9, 54, 65, 68, 69, 70, 114, 124, and 227.) 

- I. Gibbs and E. Candès. Conformal inference for online prediction with arbitrary distribution shifts, 2023. (pp. 55, 125, and 183.) 

- I. Gibbs, J. J. Cherian, and E. J. Candès. Conformal prediction with conditional guarantees, 2023. arXiv: 2305.12616. (p. 26.) 

- B. Goehry. Random forests for time-dependent processes. _ESAIM: Probability and Statistics_ , 24:801–826, 2020. (p. 101.) 

- B. Goehry, H. Yan, Y. Goude, P. Massart, and J.-M. Poggi. Random forests for time series. _HAL hal-03129751_ , 2021. (p. 101.) 

- L. Grinsztajn, E. Oyallon, and G. Varoquaux. Why do tree-based models still outperform deep learning on typical tabular data? _Advances in Neural Information Processing Systems_ , 35:507–520, 2022. (p. 119.) 

- L. Guan. Localized conformal prediction: a generalized inference framework for conformal prediction. _Biometrika_ , 110(1), 2022. (pp. 26 and 183.) 

- Y. Gui, R. F. Barber, and C. Ma. Conformalized matrix completion, 2023a. (p. 180.) 

- Y. Gui, R. Hore, Z. Ren, and R. F. Barber. Conformalized survival analysis with adaptive cut-offs. _Biometrika_ , Dec. 2023b. (p. 52.) 

- C. Gupta, A. K. Kuchibhotla, and A. Ramdas. Nested conformal prediction and quantile out-of-bag ensemble methods. _Pattern Recognition_ , 127:108496, 2022. (pp. 36, 47, 49, 145, 182, 194, 199, and 219.) 

- M. Hallin, E. del Barrio, J. Cuesta-Albertos, and C. Matrán. Distribution and quantile functions, ranks and signs in dimension _d_ : A measure transportation approach. _The Annals of Statistics_ , 49(2):1139 – 1165, 2021. (p. 228.) 

- W. Härdle, J. Horowitz, and J.-P. Kreiss. Bootstrap methods for time series. _International Statistical Review_ , 71(2):435–459, 2003. (p. 101.) 

- T. Hastie and R. Tibshirani. Generalized additive models. _Statistical Science_ , 1(3):297–310, 1986. (p. 118.) 

- E. Hazan. Introduction to online convex optimization. _arXiv preprint arXiv:1909.05207_ , 2019. (p. 74.) 

- HCC-2021. Rapport annuel 2021 “renforcer l’atténuation, engager l’adaptation”, haut conseil pour le climat. `https://www.hautconseilclimat.fr/wp-content/uploads/2021/06/ HCC-rappport-annuel-2021.pdf` . Published: 2021-06-30. (p. 5.) 

- O. Himych, A. Durand, and Y. Goude. Adaptive Forecasting of Extreme Electricity Load. working paper or preprint, Feb. 2024. (p. 130.) 

- K. Hirano, G. W. Imbens, and G. Ridder. Efficient estimation of average treatment effects using the estimated propensity score. _Econometrica_ , 71(4):1161–1189, 2003. (p. 229.) 

- T. Hong, P. Pinson, S. Fan, H. Zareipour, A. Troccoli, and R. J. Hyndman. Probabilistic energy forecasting: Global energy forecasting competition 2014 and beyond, 2016. (p. 114.) 

- P. IEA. Covid-19 impact on electricity. Technical report, Technical report, 2021. (pp. 7 and 113.) 

- P. IEA. Renewable electricity. Technical report, Technical report, 2022a. (pp. 5 and 113.) 

- P. IEA. World energy outlook 2022. Technical report, Technical report, 2022b. (pp. 7 and 113.) 

- R. Izbicki, G. Shimizu, and R. Stern. Flexible distribution-free conditional predictive bands using density estimators. In S. Chiappa and R. Calandra, editors, _Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics_ , 108, 3068–3077. PMLR, 2020. (pp. 151 and 154.) 

- R. Izbicki, G. Shimizu, and R. B. Stern. Cd-split and hpd-split: Efficient conformal regions in high dimensions. _Journal of Machine Learning Research_ , 23(87):1–32, 2022. (pp. 26, 151, and 154.) 

- L. P. Z. J. M. Robins, A. Rotnitzky. Estimation of regression coefficients when some regressors are not always observed. _Journal of the American Statistical Association_ , 89 (427):846–866, 1994. (p. 229.) 

- A. Jędrzejewski, J. Lago, G. Marcjasz, and R. Weron. Electricity price forecasting: The dawn of machine learning. _IEEE Power and Energy Magazine_ , 20(3):24–31, 2022. (p. 113.) 

- W. Jiang, M. Bogdan, J. Josse, S. Majewski, B. Miasojedow, V. Ročková, and TraumaBase® Group. Adaptive bayesian slope: Model selection with incomplete data. _Journal of Computational and Graphical Statistics_ , 31(1):113–137, 2022. (p. 150.) 

- Y. Jin and E. J. Candès. Model-free selective inference under covariate shift via weighted conformal p-values, 2023. (p. 52.) 

- J. Josse and J. P. Reiter. Introduction to the Special Section on Missing Data. _Statistical Science_ , 33(2):139 – 141, 2018. (pp. 137 and 178.) 

- J. Josse, N. Prost, E. Scornet, and G. Varoquaux. On the consistency of supervised learning with missing values, 2019. (pp. 137, 178, and 193.) 

- C. Jung, G. Noarov, R. Ramalingam, and A. Roth. Batch multivalid conformal prediction. In _International Conference on Learning Representations_ , 2023. (pp. 26 and 183.) 

- C. Kath and F. Ziel. Conformal prediction interval estimation and applications to day-ahead and intraday power markets. _International Journal of Forecasting_ , 37(2):777–799, 2021. (pp. 68 and 69.) 

- B. Kim and R. F. Barber. Black-box tests for algorithmic stability. _Information and Inference: A Journal of the IMA_ , 12(4):2690–2719, Sept. 2023. (pp. 44 and 219.) 

- D. P. Kingma and J. Ba. Adam: A method for stochastic optimization, 2014. (p. 168.) 

- D. Kivaranovic, K. D. Johnson, and H. Leeb. Adaptive, Distribution-Free Prediction Intervals for Deep Networks. In _International Conference on Artificial Intelligence and Statistics_ . PMLR, 2020. (p. 26.) 

- R. Koenker. _Quantile Regression_ . Econometric Society Monographs. Cambridge University Press, 2005. (p. 118.) 

- J.-P. Kreiss and E. Paparoditis. The hybrid wild bootstrap for time series. _Journal of the American Statistical Association_ , 107(499):1073–1084, 2012. (p. 101.) 

- H. R. Kunsch. The jackknife and the bootstrap for general stationary observations. _The annals of Statistics_ , 1217–1241, 1989. (p. 127.) 

- J. Lago, F. De Ridder, and B. De Schutter. Forecasting spot electricity prices: Deep learning approaches and empirical comparison of traditional algorithms. _Applied Energy_ , 221:386–405, 2018. (p. 67.) 

- J. Lago, G. Marcjasz, B. De Schutter, and R. Weron. Forecasting day-ahead electricity prices: A review of state-of-the-art algorithms, best practices and an open-access benchmark. _Applied Energy_ , 293:116983, 2021. (pp. 7, 67, and 113.) 

- M. Le Morvan, J. Josse, T. Moreau, E. Scornet, and G. Varoquaux. Neumiss networks: differentiable programming for supervised learning with missing values. In H. Larochelle, M. Ranzato, R. Hadsell, M. Balcan, and H. Lin, editors, _Advances in Neural Information Processing Systems_ , 33, 5980–5990. Curran Associates, Inc., 2020a. (pp. 137, 159, and 178.) 

- M. Le Morvan, N. Prost, J. Josse, E. Scornet, and G. Varoquaux. Linear predictor on linearly-generated data with missing values: non consistency and solutions. In S. Chiappa and R. Calandra, editors, _Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics_ , 108, 3165–3174. PMLR, 2020b. (pp. 137, 157, 159, 178, 190, and 214.) 

- M. Le Morvan, J. Josse, E. Scornet, and G. Varoquaux. What’s a good imputation to predict with missing values? In M. Ranzato, A. Beygelzimer, Y. Dauphin, P. Liang, and J. W. Vaughan, editors, _Advances in Neural Information Processing Systems_ , 34, 

11530–11540. Curran Associates, Inc., 2021. (pp. 59, 137, 139, 146, 147, 165, 166, 178, and 193.) 

- Y. Lee, E. Dobriban, and E. T. Tchetgen. Simultaneous conformal prediction of missing outcomes with propensity score _ε_ -discretization, 2024. (p. 180.) 

- J. Lei. Fast exact conformalization of the lasso using piecewise linear homotopy. _Biometrika_ , 106(4), 2019. (p. 45.) 

- J. Lei and L. Wasserman. Distribution-free prediction bands for non-parametric regression. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 76(1), 2014. (pp. 25, 37, 38, 146, 153, 177, 185, and 186.) 

- J. Lei, M. G’Sell, A. Rinaldo, R. J. Tibshirani, and L. Wasserman. Distribution-Free Predictive Inference for Regression. _Journal of the American Statistical Association_ , 2018. (pp. v, vii, 19, 23, 36, 67, 85, 121, 137, 140, 157, 161, 162, and 195.) 

- L. Lei and E. J. Candès. Conformal inference of counterfactuals and individual treatment effects. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 83(5): 911–938, Oct. 2021. (p. 52.) 

- R. Liang and R. F. Barber. Algorithmic stability implies training-conditional coverage for distribution-free prediction methods. _arXiv preprint arXiv:2311.04295_ , 2023. (p. 51.) 

- Z. Lin, S. Trivedi, and J. Sun. Locally valid and discriminative prediction intervals for deep learning models. In M. Ranzato, A. Beygelzimer, Y. Dauphin, P. Liang, and J. W. Vaughan, editors, _Advances in Neural Information Processing Systems_ , 34, 8378–8391. Curran Associates, Inc., 2021. (pp. 151 and 154.) 

- R. J. A. Little. _Statistical analysis with missing data, third edition_ . John Wiley & Sons, Nashville, TN, 3 edition, 2019. (pp. 137 and 178.) 

- S. Loizidis, A. Kyprianou, and G. E. Georghiou. Electricity market price forecasting using elm and bootstrap analysis: A case study of the german and finnish day-ahead markets. _Applied Energy_ , 363:123058, 2024. (p. 114.) 

- K. Maciejowska, J. Nowotarski, and R. Weron. Probabilistic forecasting of electricity spot prices using Factor Quantile Regression Averaging. _International Journal of Forecasting_ , 32(3):957–965, 2016. (p. 67.) 

- K. Maciejowska, B. Uniejewski, and R. Weron. Forecasting electricity prices, 2022. (p. 116.) 

- S. Makridakis, E. Spiliotis, and V. Assimakopoulos. M5 accuracy competition: Results, findings, and conclusions. _International Journal of Forecasting_ , 38(4):1346–1364, 2022. (p. 119.) 

- V. Manokhin. Awesome conformal prediction, Apr. 2022. https://github.com/valeman/awesome-conformal-prediction. (pp. 140 and 195.) 

- G. Marcjasz, T. Serafin, and R. Weron. Selection of calibration windows for day-ahead electricity price forecasting. _Energies_ , 11(9), 2018. (pp. 113 and 128.) 

- G. Marcjasz, M. Narajewski, R. Weron, and F. Ziel. Distributional neural networks for electricity price forecasting. _Energy Economics_ , 125:106843, 2023. (p. 114.) 

- I. Mayer, A. Sportisse, J. Josse, N. Tierney, and N. Vialaneix. R-miss-tastic: a unified platform for missing values methods and workflows, 2019. (pp. 137 and 178.) 

- N. Meinshausen. Quantile regression forests. _Journal of Machine Learning Research_ , 7(35): 983–999, 2006. (p. 119.) 

- MEPS. Medical expenditure panel survey. `https://meps.ahrq.gov/mepsweb/data_stats/ data_overview.jsp` . (p. 149.) 

- S. P. Meyn and R. L. Tweedie. _Markov chains and stochastic stability_ . Springer Science & Business Media, 2012. (pp. 89, 98, and 99.) 

- B. M. Moreno, M. Brégère, P. Gaillard, and N. Oudjane. A mirror descent approach for mean field control applied to demande-side management. 2023. (p. 113.) 

- B. Muzellec, J. Josse, C. Boyer, and M. Cuturi. Missing data imputation using optimal transport. In H. D. III and A. Singh, editors, _Proceedings of the 37th International Conference on Machine Learning_ , 119, 7130–7140. PMLR, 2020. (p. 204.) 

- N. Nassar, D. Silva, and H. Morais. Hierarchical energy management solution for smart charging. In _CIRED Porto Workshop 2022: E-mobility and power distribution systems_ , 2022, 721–725, 2022. (p. 113.) 

- E. Ndiaye. Stable conformal prediction sets. In _Proceedings of the 39th International Conference on Machine Learning_ . PMLR, 2022. (p. 45.) 

- E. Ndiaye and I. Takeuchi. Computing full conformal prediction set with approximate homotopy. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc., 2019. (p. 45.) 

- E. Ndiaye and I. Takeuchi. Root-finding approaches for computing conformal prediction set. _Machine Learning_ , 112(1), 2022. (p. 45.) 

- D. Nickelsen and G. Müller. Bayesian hierarchical probabilistic forecasting of intraday electricity prices. _arXiv preprint arXiv:2403.05441_ , 2024. (p. 114.) 

- W. Nitka, T. Serafin, and D. Sotiros. Forecasting electricity prices: Autoregressive hybrid nearest neighbors (arhnn) method. In M. Paszynski, D. Kranzlmüller, V. V. Krzhizhanovskaya, J. J. Dongarra, and P. M. Sloot, editors, _Computational Science_ 

- _– ICCS 2021_ , 312–325, Cham, 2021. Springer International Publishing. (p. 113.) 

- I. Nouretdinov, T. Melluish, and V. Vovk. Ridge regression confidence machine. In _Proceedings of the 18th International Conference on Machine Learning_ , 2001. (p. 45.) 

- J. Nowotarski and R. Weron. Computing electricity spot price prediction intervals using quantile regression and forecast averaging. _Computational Statistics_ , 30(3):791–803, Aug. 2014. (p. 122.) 

- J. Nowotarski and R. Weron. Recent advances in electricity price forecasting: A review of probabilistic forecasting. _Renewable and Sustainable Energy Reviews_ , 81:1548–1568, 2018. (pp. 8 and 67.) 

- H. Papadopoulos, K. Proedrou, V. Vovk, and A. Gammerman. Inductive confidence machines for regression. In _Machine learning: ECML 2002: 13th European conference on machine learning Helsinki, Finland, August 19–23, 2002 proceedings 13_ , 345–356. Springer, 2002. (pp. v, vii, 19, 22, 67, 68, 114, 120, 121, 137, 140, 157, 161, and 195.) 

- F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay. Scikit-learn: Machine learning in Python. _Journal of Machine Learning Research_ , 12:2825–2830, 2011. (pp. 119, 147, and 201.) 

- A. Podkopaev and A. Ramdas. Distribution-free uncertainty quantification for classification under label shift. In _Proceedings of the Thirty-Seventh Conference on Uncertainty in Artificial Intelligence_ . PMLR, 2021. (pp. 52 and 53.) 

- D. N. Politis and J. P. Romano. The stationary bootstrap. _Journal of the American Statistical association_ , 89(428):1303–1313, 1994. (p. 127.) 

- C. Remlinger, C. Alasseur, M. Brière, and J. Mikael. Expert aggregation for financial forecasting. _The Journal of Finance and Data Science_ , 9:100108, 2023. (pp. 74 and 114.) 

- Y. Romano, E. Patterson, and E. Candès. Conformalized Quantile Regression. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc., 2019. (pp. viii, 26, 27, 29, 36, 59, 67, 121, 136, 137, 140, 142, 154, 155, 162, and 198.) 

- Y. Romano, R. F. Barber, C. Sabatti, and E. Candès. With Malice Toward None: Assessing Uncertainty via Equalized Coverage. _Harvard Data Science Review_ , 2(2), 2020a. (pp. 26, 159, 161, and 183.) 

- Y. Romano, M. Sesia, and E. Candes. Classification with valid and adaptive coverage. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc., 2020b. (pp. 33 and 34.) 

- J. RTE. Bilan électrique 2022, 2022. (pp. 5 and 113.) 

- D. B. Rubin. Inference and missing data. _Biometrika_ , 63(3):581–592, 1976. (pp. 139 and 178.) 

- M. Sadinle, J. Lei, and L. Wasserman. Least ambiguous set-valued classifiers with bounded error levels. _Journal of the American Statistical Association_ , 114(525):223–234, June 2018. (p. 32.) 

- A. Saha, S. Basu, and A. Datta. Random forests for spatially dependent data. _Journal of the American Statistical Association_ , 0(0):1–19, 2021. (p. 101.) 

- N. Seedat, A. Jeffares, F. Imrie, and M. van der Schaar. Improving adaptive conformal prediction using self-supervised learning. In F. Ruiz, J. Dy, and J.-W. van de Meent, editors, _Proceedings of The 26th International Conference on Artificial Intelligence and Statistics_ , 206 of _Proceedings of Machine Learning Research_ , 10160–10177. PMLR, 25–27 Apr 2023. (p. 180.) 

- M. Sesia and E. J. Candès. A comparison of some conformal quantile regression methods. _Stat_ , 9(1):e261, 2020. (pp. 29, 43, 126, 146, 151, and 154.) 

- M. Sesia and Y. Romano. Conformal prediction using conditional histograms. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc., 2021. (pp. 26, 147, 168, and 201.) 

- G. Shafer and V. Vovk. A Tutorial on Conformal Prediction. _JMLR_ , 9:51, 2008. (p. 67.) 

- S. Shalev-Shwartz and Y. Singer. A primal-dual perspective of online learning algorithms. _Machine Learning_ , 69(2-3):115–142, 2007. (p. 74.) 

- M. Shao and Y. Zhang. Distribution-free matrix prediction under arbitrary missing pattern, 2023. (p. 180.) 

- A. Sportisse, C. Boyer, A. Dieuleveut, and J. Josse. Debiasing averaged stochastic gradient descent to handle missing values. In H. Larochelle, M. Ranzato, R. Hadsell, M. Balcan, and H. Lin, editors, _Advances in Neural Information Processing Systems_ , 33, 12957–12967. Curran Associates, Inc., 2020. (pp. 151 and 171.) 

- H. Susmann, A. Chambaz, J. Josse, M. Wargon, P. Aegerter, and E. Bacry. Probabilistic Prediction of Arrivals and Hospitalizations in Emergency Departments in Île-de-France. working paper or preprint, Apr. 2024. (p. 130.) 

- R. Tibshirani. Regression shrinkage and selection via the lasso. _Journal of the Royal Statistical Society. Series B (Methodological)_ , 58(1):267–288, 1996. (p. 118.) 

- R. J. Tibshirani, R. F. Barber, E. Candes, and A. Ramdas. Conformal Prediction Under Covariate Shift. In _Advances in Neural Information Processing Systems_ . Curran Associates, Inc., 2019. (pp. 23, 52, 53, and 68.) 

- L. Tschora, E. Pierre, M. Plantevit, and C. Robardet. Electricity price forecasting on the day-ahead market using machine learning. _Applied Energy_ , 313:118752, 2022. (p. 113.) 

- A. B. Tsybakov. _Introduction to Nonparametric Estimation_ . Springer New York, 2009. (pp. 211 and 212.) 

- J. W. Tukey. Mathematics and the picturing of data. In _Proceedings of the International Congress of Mathematicians_ , 1975. (p. 228.) 

- B. Uniejewski and R. Weron. Regularized quantile regression averaging for probabilistic electricity price forecasting. _Energy Economics_ , 95:105121, 2021. (pp. 67 and 114.) 

- B. Uniejewski, J. Nowotarski, and R. Weron. Automated variable selection and shrinkage for day-ahead electricity price forecasting. _Energies_ , 9(8), 2016. (p. 113.) 

- B. Uniejewski, R. Weron, and F. Ziel. Variance stabilizing transformations for electricity spot price forecasting. _IEEE Transactions on Power Systems_ , 33(2):2219–2229, 2018. (p. 113.) 

- S. van Buuren and K. Groothuis-Oudshoorn. mice: Multivariate imputation by chained equations in r. _Journal of Statistical Software_ , 45(3):1–67, 2011. (p. 194.) 

- M. Van Ness, T. M. Bosschieter, R. Halpin-Gregorio, and M. Udell. The missing indicator method: From low to high dimensions, 2022. (pp. 137 and 178.) 

- V. Vovk. Conditional Validity of Inductive Conformal Predictors. In _Asian Conference on Machine Learning_ . PMLR, 2012. (pp. 25, 37, 38, 42, 51, 146, 154, 177, 181, 185, and 186.) 

- V. Vovk. Cross-conformal predictors. _Annals of Mathematics and Artificial Intelligence_ , 74: 9–28, 2015. (pp. 49, 182, 199, and 218.) 

- V. Vovk, A. Gammerman, and C. Saunders. Machine-Learning Applications of Algorithmic Randomness. In _Proceedings of the Sixteenth International Conference on Machine Learning_ , 444–453. Morgan Kaufmann Publishers Inc., 1999. (pp. 67, 114, and 120.) 

- V. Vovk, A. Gammerman, and G. Shafer. _Algorithmic Learning in a Random World_ . Springer US, 2005. (pp. v, vii, 19, 22, 26, 36, 44, 67, 114, 120, 123, 137, 140, 141, 157, 181, 183, 194, and 195.) 

- V. G. Vovk. Aggregating strategies. _Proc. of Computational Learning Theory_ , 1990. (pp. 74 and 100.) 

- R. Weron. Electricity price forecasting: A review of the state-of-the-art with a look into the future. _International Journal of Forecasting_ , 30(4):1030–1081, 2014. (pp. 7, 67, and 113.) 

- O. Wintenberger. Optimal learning with bernstein online aggregation. _Machine Learning_ , 106(1):119–141, 2017. (pp. 74, 100, and 122.) 

- W. Wisniewski, D. Lindsay, and S. Lindsay. Application of conformal prediction interval estimations to market makers’ net positions. In _Proceedings of the Ninth Symposium on Conformal and Probabilistic Prediction and Applications_ , 128 of _Proceedings of Machine Learning Research_ , 285–301. PMLR, 2020. (pp. 68, 69, 77, 121, and 123.) 

- S. N. Wood, Y. Goude, and M. Fasiolo. _Interpretability in Generalized Additive Models_ , page 85–123. Springer International Publishing, 2022. (p. 130.) 

- C. Xu and Y. Xie. Conformal prediction interval for dynamic time-series. In _Proceedings of the 38th International Conference on Machine Learning_ , 139 of _Proceedings of Machine Learning Research_ , 11559–11569. PMLR, 2021. (pp. 68, 77, 78, 80, and 101.) 

- M. Yang. _Features Handling by Conformal Predictors_ . PhD thesis, Royal Holloway, University of London, 2015. (p. 141.) 

- Y. Yang, J. Guo, Y. Li, and J. Zhou. Forecasting day-ahead electricity prices with spatial dependence. _International Journal of Forecasting_ , 2023. (p. 113.) 

- Z. Yang, E. Candès, and L. Lei. Bellman conformal inference: Calibrating prediction intervals for time series, 2024. (p. 55.) 

- M. Zaffran, O. Féron, Y. Goude, J. Josse, and A. Dieuleveut. Adaptive conformal predictions for time series. In K. Chaudhuri, S. Jegelka, L. Song, C. Szepesvari, G. Niu, and S. Sabato, editors, _Proceedings of the 39th International Conference on Machine Learning_ , 162, 25834–25866. PMLR, 2022. (pp. 55, 114, 121, 123, 124, 125, and 149.) 

- M. Zaffran, A. Dieuleveut, J. Josse, and Y. Romano. Conformal prediction with missing values. In A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and J. Scarlett, editors, _Proceedings of the 40th International Conference on Machine Learning_ , 202 of _Proceedings of Machine Learning Research_ , 40578–40604. PMLR, 23–29 Jul 2023. (pp. 178, 179, 180, 181, 182, 187, 190, 195, 196, 199, 200, 201, 203, 204, and 214.) 

- F. Ziel and R. Weron. Day-ahead electricity price forecasting with high-dimensional structures: Univariate vs. multivariate modeling frameworks. _Energy Economics_ , 70: 396–420, feb 2018. (p. 116.) 

- Çağatay Berke Bozlak and C. F. Yaşar. An optimized deep learning approach for forecasting day-ahead electricity prices. _Electric Power Systems Research_ , 229:110129, 2024. (p. 113.) 

**Titre :** Quantification post-hoc de l’incertitude pr´edictive : m´ethodes avec applications `a la pr´evision des prix de l’´electricit´e 

**Mots cl´es :** Quantification d’incertitude pr´edictive, apprentissage statistique, pr´evision de s´eries temporelles, donn´ees manquantes, march´es de l’´energie 

**R´esum´e :** L’essor d’algorithmes d’apprentissage statistique offre des perspectives prometteuses pour pr´evoir les prix de l’´electricit´e. Cependant, ces m´ethodes fournissent des pr´evisions ponctuelles, sans indication du degr´e de confiance `a leur accorder. Pour garantir un d´eploiement sˆur de ces mod`eles pr´edictifs, il est crucial de quantifier leur incertitude pr´edictive. Cette th`ese porte sur le d´eveloppement d’intervalles pr´edictifs pour tout algorithme de pr´ediction. Bien que motiv´ees par le secteur ´electrique, les m´ethodes d´evelopp´ees, bas´ees sur la pr´ediction conforme par partition (SCP), sont g´en´eriques : elles peuvent ˆetre appliqu´ees dans de nombreux autres domaines sensibles. 

Dans un premier temps,cette th`ese ´etudie la quantification post-hoc de l’incertitude pr´edictive pour les s´eries temporelles. Le premier obstacle `a l’application de SCP pour obtenir des pr´evisions probabilistes th´eoriquement valides des prix de l’´electricit´e de mani`ere post-hoc est l’aspect temporel hautement non-stationnaire des prix de l’´electricit´e, brisant l’hypoth`ese d’´echangeabilit´e. La premi`ere contribution propose un algorithme qui ne d´epend pas d’un param`etre et adapt´e aux s´eries temporelles, reposant 

sur l’analyse th´eorique de l’efficacit´e d’une m´ethode pr´e-existante, l’Inf´erence Conforme Adaptative. La deuxi`eme contribution m`ene une ´etude d’application d´etaill´ee sur un nouveau jeu de donn´ees de prix spot franc¸ais r´ecents et turbulents en 2020 et 2021. 

Un autre d´efi sont les valeurs manquantes ( `NA` s). Dans un deuxi`emte temps, cette th`ese analyse l’interaction entre les `NA` s et la quantification de l’incertitude pr´edictive. La troisi`eme contribution montre que les `NA` s induisent de l’h´et´erosc´edasticit´e, ce qui conduit `a une couverture in´egale en fonction de quelles valeurs sont manquantes. Deux algorithmes sont conc¸us afin d’assurer une couverture constante quelque soit le sch´ema de `NA` s, ceci ´etant assur´e sous des hypoth`eses distributionnelles sur les `NA` s. La quatri`eme contribution approfondit l’analyse th´eorique afin de comprendre pr´ecis´ement quelles hypoth`eses de distribution sont in´evitables pour construite des r´egions pr´edictives informatives. Elle unifie ´egalement les algorithmes propos´es pr´ec´edemment dans un cadre g´en´eral qui d´emontre empiriquement ˆetre robuste aux violations des hypoth`eses distributionnelles sur les `NA` s. 

**Title :** Post-hoc predictive uncertainty quantification: methods with applications to electricity price forecasting **Keywords :** Predictive uncertainty quantification, statistical learning, time series forecasting, missing values, energy markets 

**Abstract :** The surge of more and more powerful statistical learning algorithms offers promising prospects for electricity prices forecasting. However, these methods provide ad hoc forecasts, with no indication of the degree of confidence to be placed in them. To ensure the safe deployment of these predictive models, it is crucial to quantify their predictive uncertainty. This PhD thesis focuses on developing predictive intervals for any underlying algorithm. While motivated by the electrical sector, the methods developed, based on Split Conformal Prediction (SCP), are generic : they can be applied in many sensitive fields. 

First, this thesis studies post-hoc predictive uncertainty quantification for time series. The first bottleneck to apply SCP in order to obtain guaranteed probabilistic electricity price forecasting in a post-hoc fashion is the highly non-stationary temporal aspect of electricity prices, breaking the exchangeability assumption. The first contribution proposes a parameter-free algorithm tailored for time series, 

which is based on theoretically analysing the efficiency of the existing Adaptive Conformal Inference method. The second contribution conducts an extensive application study on novel data set of recent turbulent French spot prices in 2020 and 2021. Another challenge are missing values ( `NA` s). In a second part, this thesis analyzes the interplay between `NA` s and predictive uncertainty quantification. The third contribution highlights that `NA` s induce heteroskedasticity, leading to uneven coverage depending on which features are observed. Two algorithms recovering equalized coverage for any `NA` s under distributional assumptions on the missigness mechanism are designed. The forth contribution pushes forwards the theoretical analysis to understand precisely which distributional assumptions are unavoidable for theoretical informativeness. It also unifies the previously proposed algorithms into a general framework that demontrastes empirical robustness to violations of the supposed missingness distribution. 

**Institut Polytechnique de Paris** 91120 Palaiseau, France 

