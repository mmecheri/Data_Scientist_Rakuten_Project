#### Données Texte

>**Variables**
>>- La colonne «**designation**»: ne contient pas de valeurs manquantes
>>- Le colonne «**description**» donne plus d’informations sur les produits, mais comporte un nombre important de valeurs manquantes(35%)

Pour les données textuelles, nous avons:
>>>-  utiliser la colonne «**designation**» uniquement
>>>- ensuite **regroupé** les deux variables «description» et «designation» en une variable unique appelée «**text** »

>**Nettoyage du Texte**
>>>-	Mettre tous les mots en lettres minuscules
>>>-	Suppression des accents et des balises HTML
>>>-	Instanciation et suppression des stopwords(Français, Anglais et Allemand)
>>>-	Suppression des mots ayant moins de deux lettres  </br>

>**Représentation vectorielle**
>>- **Machine Learning**: chaque observation du text est vectorisé à l'aide de la classe ***TfidfVectorizer*** fixant le ***max_features*** à 5000.</br>
>>- **Deep Learning**: nous avons séparé le texte en mots grâce à la classe ***Tokenizer*** de « tf.keras.preprocessing.text» avec un nombre maximum de mots(***num_words***) de 20 000. Nous avons ensuite défini la longueur maximum d’une séquence à 200.


#### Données Images

> Nous avons utilisé un génerateur de données (**ImageDataGenerator**, du module tensorflow.keras.preprocessing.image). 
Le générateur de données permet les avantages suivants :
>>-	D’enrichir notre jeu de données
>>- Réduire le surapprentissage (overfitting)
>>-	Permet de reduire les containtes liées aux manques de ressources de calcul

---Insersetion---







