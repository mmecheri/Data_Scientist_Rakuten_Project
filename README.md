# Rakuten France Multimodal Product Data Classification

## Le Projet 
Ce projet a été réalisé dans le cadre d'un challenge proposé par [Rakuten](https://challengedata.ens.fr/participants/challenges/35/) et de notre formation de DataScientist au sein de l'organisme [DataSientest](https://datascientest.com/).              

Le challenge porte sur le thème de la **classification des produits "e-commerce"**.

L'objectif est de prédire le code type (**prdtypecode**) de chaque produit en utilisant des **données textuelles** (désignation et description du produit) ainsi que des **données images** (image du produit) tel qu'il est défini dans le catalogue de Rakuten France.                  

**Un modèle de référence** est indiqué dans le site du challenge 
avec deux modèles distincts pour le Texte et les Images:
-	RNN utilisant les données **texte: 0.8113 weighted F1-score**
-	ResNet sur les données  **images: 0.5534 weighted F1-score**

Il est demandé d’utiliser la **métrique weighted-F1-score** pour **évaluer** les performances de la classification. 


L’objectif du projet étant de faire mieux que les résultats du modèle de référence.

----------

## Jeu de données
Pour ce challenge, Rakuten France met à disposition environ 99 000 listes de produits au format CSV, y compris l'ensemble d'entraînement (84 916) et l'ensemble de test (13 812).</br>
		
Les données sont réparties suivant des critères , formant 4 datasets distincts :	

- « X_train_update.csv »:  échantillons d'**entraînement**, avec la description textuelle ainsi que le référencement du fichier image associé
- « y_train_CVw08PX.csv »: contient les variable cible (**prdtypecode**)
- « X_test_update.csv »:  échantillons de test(pour la sommission des résulats)
- « images.zip »: ce fichier contient toutes les images:
	- « image_train » contenant 84 916 images pour l'**entraînement**
	- « image_test » contenant 13 812 images (pour la sommission des résulats)
	
**Exemples de données :** </br>
![data_example](https://user-images.githubusercontent.com/88212289/201135993-81d5834d-c4ab-44ca-8d2e-ad61ccce3e4b.png)

----------

## Modélisation

### Modélisation partie Texte
#### Machine learning
Ci-dessous un récapitulatif comparatif des résultats d’entrainement en choisissant dans un premier temps seulement la colonne « designation » et dans un second temps en utilisant les deux colonnes « designation » et « description », combinées en une colonne « text »:

![Ml_text](https://user-images.githubusercontent.com/88212289/201136744-3cf17787-f827-4b5e-b116-a4b09e4614f3.png)
#### Deelp learning
Voici les modèles utilisés et les résulats obetenus:

![DL_text](https://user-images.githubusercontent.com/88212289/201137059-3586e8f2-c90d-4e4d-a125-b62241fbca8b.png)
#### Résultats:
Les modèles Conv1D et DNN (Deep Neural Network) donnent les meilleurs scores. Le modèle LinearSVC a également donné des résultats de scoring intéressants. En fait, nous avons constaté que le modèle Conv1D présente la particularité d’être beaucoup plus rapide à l’entraînement.

### Modélisation partie Images
Sachant la complixité de notre jeu de données Images et les ressemblances qui existent entre les différentes classes, nous avons rapidement opté pour l’utilisation des méthodes d’apprentissage par transfert(transfert learning) avec des modèles reposant sur les réseaux de neurones artificiels, capables d’apprentissage profond (Deep Learning). Nous avons ainsi utilisé les modèles les plus adaptés aux images : les réseau de neurones convolutifs (CNN).

#### Choix des modèles pré-entrainés
Parmis la listes des modèles présentés [ici](https://keras.io/api/applications/),
nous avons retenu les modèles qui ont le moins de paramètres afin de réduire les durées d’entrainement et limiter ainsi les contraintes liées au manque de ressources de calcul.

![selected_models](https://user-images.githubusercontent.com/88212289/201138152-db60d1d2-0c5e-4416-a526-2455cf73b09d.png)
#### Etape 1 - Sélection des meilleurs modèles
- Entrainer les modèles selectionnés avec des images d’entrées de diffrérentes tailles
- Varier le batch size  de 32 à 64</br>
- Varier le nombre d’Epoch de 10, 20 à 40</br>
- Noter les 5 meilleurs modèles selon la mesure F1-score weighted

Les résultats de l'ensemble des modèles testés:
![Tested_Models](https://user-images.githubusercontent.com/88212289/201144494-fdbbba04-bceb-42a3-b15c-0c6e3f0d425b.png)

Les 5 meilleurs modèles selon F1-score Weighted sont: 
![Top_5_models](https://user-images.githubusercontent.com/88212289/201144809-d0c4b7bd-73c0-4fe1-a9ac-754c16da6518.png)


#### Etape 2 - Augmentation des données avec les meilleurs modèles obtenus à l’Etape 1
#### Etape 3 - Augmentation des données + fine tuning des modèles
#### Etape 4 - Optimisation LR (Sans augmentation des données ni fine-tuning)
#### Etape 5 - Augmentation des données, fine-tuning avec les LRs optimisés

#### Résultats finaux modélisation partie Images:
Les 2 meilleurs résultats ont été obtenus avec :

- **Xception**: **LR** à **0,0004** , **F1-score Weighted** à **0.66**
- **InceptionV3**: **LR** à **0,0003**, **F1-score weighted** à **0.65**
(Avec augmentation des données et fine-tuning)

Ces résultats dépassent largement ceux annoncés dans le modèle de référence Rakuten pour la classification basée sur les données Images(0.55).

###  Modélisation basée sur les données Texte et Images - Bimodal
Dans cette partie, nous abordons le défi principal du challenge Rakuten , à savoir, une classification multimodal, en se basant sur les données Texte et Images.

#### Démarche
Dans le cadre de notre problème de classification, nous avons opté pour l’approche de Voting (Max Voting et Weighted Average Voting) comme suit:

- Max Voting : choisir la prédiction avec la probabilité la plus élevée parmi les modèles combinés
- Weighted Average : associer un poids à chaque modèle selon son F1-score

#### Combinaisons utilisées - Texte et Images
- Simple DNN , Conv1D et Xception
- Simple DNN, Conv1D et InceptionV3

#### Résultats
- Simple DNN, Conv1D et Xception
 ![voting_Simple_DNN_Conv1D_Xception](https://user-images.githubusercontent.com/88212289/201141605-e4898203-3f30-434a-b2e7-8c97f87f7a6e.png)

-  Simple DNN, Conv1D et InceptionV3
![voting_Simple_DNN_Conv1D_Inception](https://user-images.githubusercontent.com/88212289/201141940-796c7003-9a3b-41ec-8471-d2a3babc80a6.png)

Les résultats sont quasiment identiques avec une accuracy très légèrement supérieure avec le Max Voting pour la combinaison Simple DNN, Conv1D et InceptionV3

----------
Par ailleurs, nous avons soumis nos prédictions sur le site du challenge(sur plus de 13000 observations) avec nos deux combinaisons pour le Vote et nous avons atteint:

- Conv1D, Simple DNN et Xception: le 21 février 2022 avec un score de 0.8333, ce qui nous a placé en 27ème position sur 83.
- Conv1D, Simple DNN et InceptionV3: le 19 mars 2022 avec un score de 0.8349, ce qui nous a placé en 25ème position sur 83.


----------
**Data Scientist Promotion Juin 2021**:

Participants:
- Tooba SHAUKAT
- Brahim CHLAGHME
- Mourad MECHERI

Mentor: 
- Gaspard GRIMM

