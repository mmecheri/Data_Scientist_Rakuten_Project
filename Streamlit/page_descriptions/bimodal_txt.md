Dans cette partie, nous abordons le **défi principal** du challenge Rakuten , à savoir,  une **classification multimodal**, en se basant sur les
données **Texte** et **Images**

L’idée consiste à combiner de multiples modèles en un seul, et d’obtenir des performances prédictives supérieures à celles de ces modèle pris individuellement. La combinaison de deux modèles d'apprentissage, autrement connu sous le nom d'apprentissage d'ensemble, comporte de nombreuses techniques. Parmi les plus citées dans la littérature, le Voting, le Stacking.
#### Démarche

Dans le cadre de notre problème de classification, nous avons opté pour l’approche de Voting (Max Voting et Weighted Average Voting) comme suit :
-	**Max Voting** : choisir la prédiction avec la probabilité la plus élevée parmi les modèles combinés
-	**Weighted Average** : associer un poids à chaque modèle selon son F1-score 
---Insersetion---
#### Choix des meilleurs modèles

Parmi l’ensemble des modèles Texte et Images testés, les meilleures performances ont été obtenues avec les modèles suivants:
---Insersetion---
**Partie Texte**: 
>- Embedding + Conv1D: F1-score Weighted et une accuracy de 0.80
>- Simple DNN : F1-score Weighted et une accuracy de 0.81 
---Insersetion---
**Partie Images**:
>- Xception: F1-score Weighted et une accuracy à  0.66
>- InceptionV3: F1-score Weighted et une accuracy à  0.64
---Insersetion---
#### Combinaisons utilisées - Texte et Images
Nous avons utilisé deux combinaisons pour le système de vote : 
---Insersetion---
>>- **Simple DNN** , **Conv1D**  et **Xception**
>>- **Simple DNN**, **Conv1D** et **InceptionV3**
---Insersetion---
Les poids associés pour le vote pondéré(Weighted Average) aux différents modèles sont :
>>- Simple DNN: **0.81**, Conv1D:   **0.80**
>>- Xception: **0.66**, InceptionV3: **0.65**
---Insersetion---

#### Résultats

##### Simple DNN, Conv1D et Xception
---Insersetion---

##### Simple DNN, Conv1D et InceptionV3
---Insersetion---
##### Analyse des résulats des deux combinaisons
---Insersetion---
Par ailleurs, nous avons soumis nos prédictions sur le site du challenge(sur plus de 13000 observations) avec nos deux combinaisons pour le Vote et nous avons atteint:

>>- Conv1D, Simple DNN et Xception: le 21 février 2022 avec un score de **0.8333**, ce qui nous a placé en 27ème position sur 83.
>>- Conv1D, Simple DNN et InceptionV3: le 19 mars 2022 avec un score de **0.8349**, ce qui nous a placé en **25ème** position sur **83**.
