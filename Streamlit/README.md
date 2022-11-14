
# L'application Streamlit est accessible via ce lien: https://huggingface.co/spaces/mmecheri/Rakuten_Streamlit
Dans la partie Démo de l'application, vous pouvez réaliser vos propres prédictions via des données Texte ou Image ou les deux combinés.  


# Streamlit Demo : Rakuten France Multimodal Product Data Classification
Dans la partie Démo, nous vous présentons une interface permettant de faire des prédictions. Celles-ci peuvent être réalisées avec un modèle basé sur les données Texte ou Images ou les deux combinés.

- Une **classification basée** sur le **Texte**: Conv1D et Simple DNN
- Une **classification basée sur les Images**: Xception et InceptionV3
- Une **classification Bimodal - Texte et Images**:
  - Conv1D, Simple DNN et Xception
  - Conv1D, Simple DNN et InceptionV3
  
Les **données** peuvent être **selectionnée**s à partir de notre jeu de données(**de manière aléatoire**) ou **entrées manuellement** par l'utilisateur.

Voici quelques exemples de prédictions:

#### - A partir de données Texte en utlisant un modèle RNN Conv1D: 
![Exemple_1](https://user-images.githubusercontent.com/88212289/201482989-6387b7a0-7e10-4be0-b141-671657c8eeb5.PNG)


#### - A partir d'une données Image en utilisant CNN Xception:
![Exemple_2](https://user-images.githubusercontent.com/88212289/201482993-a912f1f9-dcde-4b7f-9114-634e24f5050f.PNG)


#### - A partir de données Texte et d'Images(Bimodal) avec Conv1D&Simple DNN&InceptionV3
![Exemple_3](https://user-images.githubusercontent.com/88212289/201483002-23c24943-e9e0-4412-841d-5d88b2546bb6.PNG)


