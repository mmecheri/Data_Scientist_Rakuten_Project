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
---Insersetion---
L’objectif du projet étant de faire mieux que les résultats du modèle de référence