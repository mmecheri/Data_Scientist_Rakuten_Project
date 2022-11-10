# Rakuten France Multimodal Product Data Classification

## Le Projet 
Ce projet a été réalisé dans le cadre d'un challenge 
proposé par [Rakuten](https://challengedata.ens.fr/participants/challenges/35/) et de notre formation de DataScientist au sein de l'organisme [DataSientest](https://datascientest.com/).              

Le challenge porte sur le thème de la **classification des produits "e-commerce"**. 

L'objectif est de prédire le code type (**prdtypecode**) de chaque produit en utilisant des **données textuelles** (désignation et description du produit) ainsi que des **données images** (image du produit)
tel qu'il est défini dans le catalogue de Rakuten France.                  

**Un modèle de référence** est indiqué dans le site du challenge 
avec deux modèles distincts pour le Texte et les Images:
-	RNN utilisant les données **texte: 0.8113 weighted F1-score**
-	ResNet sur les données  **images: 0.5534 weighted F1-score**

Il est demandé d’utiliser la **métrique weighted-F1-score** pour **évaluer** les performances de la classification. 


L’objectif du projet étant de faire mieux que les résultats du modèle de référence

## Jeu de données
Pour ce challenge, Rakuten France met à disposition environ 99 000 listes de produits au format CSV, 
                y compris l'ensemble d'entraînement (84 916) 
                et l'ensemble de test (13 812).</br>
		
Les données sont réparties suivant des critères , formant 4 datasets distincts :	

- « X_train_update.csv »:  échantillons d'**entraînement**, avec la description textuelle ainsi que le référencement du fichier image associé
- « y_train_CVw08PX.csv »: contient les variable cible (**prdtypecode**)
- « X_test_update.csv »:  échantillons de test(pour la sommission des résulats)
- « images.zip »: ce fichier contient toutes les images:
	- « image_train » contenant 84 916 images pour l'**entraînement**
	- « image_test » contenant 13 812 images (pour la sommission des résulats)
	
**Exemples de données :** </br>

<!-- ### Les données Texte-->
<!-- ### Les données Images-->