#### Machine learning 
Ci-dessous un récapitulatif comparatif des résultats d’entrainement en choisissant dans un premier temps seulement 
la colonne « designation » et dans un second temps en utilisant les deux colonnes « designation » et « description », combinées en une colonne « text »:
---Insersetion---
Les modèles de Machine Learning ont montré leurs limites pour atteindre des performances satisfaisantes. Nous nous sommes donc orientés vers des modèles de Deep Learning.
#### Deep learning 

Voici les modèles utilisés et les résulats obetenus:
---Insersetion---
Choix des paramètres:
>-&nbsp;Batch size: 200</br>
>-&nbsp;Epochs: 5 epochs</br>
>-&nbsp;Learning Rate: 0.001</br>
>-&nbsp;Optimizer: “adam”</br>

---Insersetion---
Les classes de produits les moins bien prédites sont globalement les mêmes pour les deux modèles Conv1D et Simple DNN, sauf pour les  classes de produits: 1302, 50, 2220 et 2462 
qui sont mieux prédites par le modèle Simple DNN

---Insersetion---
#### Conclusion
Les modèles Conv1D et DNN (Deep Neural Network) donnent les meilleurs scores. Le modèle LinearSVC a également donné des résultats de scoring intéressants. En fait, nous avons constaté que le modèle Conv1D présente la particularité d’être beaucoup plus rapide à l’entraînement
---Insersetion---
#### Démo - Prédictions
Pour les prédictions , nous intéresserons uniquement aux deux meilleurs modèles: **Conv1D** et **DNN**
---Insersetion---






