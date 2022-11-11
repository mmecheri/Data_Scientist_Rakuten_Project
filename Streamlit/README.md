
## L'application Streamlit est hebergée sur Hugging Face et accessible via ce lien : https://huggingface.co/spaces/mmecheri/streamlit_Rakuten


# Streamlit Demo : Rakuten France Multimodal Product Data Classification
Dans la partie Démo, nous vous présentons une interface permettant de faire des prédictions. Celles-ci peuvent être réalisées avec un modèle basé sur les données Texte ou Images ou les deux combinés

- Une **classification basée** sur le **Texte**: Conv1D et Simple DNN
- Une **classification basée sur les Images**: Xception et InceptionV3
- Une **classification Bimodal - Texte et Images**:
  - Conv1D, Simple DNN et Xception
  - Conv1D, Simple DNN et InceptionV3
  
Les ***données** peuvent être **selectionnée**s à partir de notre jeu de données(**de manière aléatoire**) ou **entrées manuellement** par l'utilisateur

Voici quelques exemples de prédictions:

#### - A partir de données Texte saisie manuellement en utlisant Conv1D: 
![Example_1](https://user-images.githubusercontent.com/88212289/201320562-bab4503a-88c2-4c62-baf6-8f2b2a23c64e.PNG)


#### - A partir d'une données Image entrée manuellement en utilisant InceptionV3:
![Example_2](https://user-images.githubusercontent.com/88212289/201320580-2c7fb54e-6609-494b-9868-96bec8f1fa12.PNG)


#### - A partir de données Texte et d'Images(Bimodal) avec Conv1D&Simple DNN&InceptionV3
![Example_3](https://user-images.githubusercontent.com/88212289/201320598-b1103685-7f16-44be-8b39-13446d2eb88a.PNG)

## Comment exécuter cette Démo

*git clone https://github.com/mmecheri/Data_Scientist_Rakuten_Project.git* 

*cd Streamlit*

*pip install -r requirements.txt*

*cd code*

*streamlit run rakupy_home.py*
