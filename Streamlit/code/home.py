import streamlit as st

     
# homme.py



def app():
    
    st.title("Rakuten France Multimodal Product Data Classification")
    
    st.header("Le projet")  
      
    # text_contexte ="""
    #               Ce projet a été réalisé dans le cadre d'un challenge 
    #               proposé par [Rakuten](https://challengedata.ens.fr/participants/challenges/35/) et de notre formation de DataScientist au sein de l'organisme [DataSientest](https://datascientest.com/).              
                
    #               Le challenge porte sur le thème de la classification des produits "e-commerce". 
                  
    #               L'objectif est de prédire le code type (prdtypecode) de chaque produit en utilisant des données textuelles (désignation et description du produit) ainsi que des données images (image du produit)
    #               tel qu'il est défini dans le catalogue de Rakuten France.                  
                  
    #               Un modèle de référence est indiqué dans le site du challenge 
    #               avec deux modèles distincts pour le Texte et les Images:
    #                 -	RNN utilisant les données texte : 0.8113 weighted F1-score
    #                 -	ResNet sur les données image : 0.5534 weighted F1-score
                    
    #               Il est demandé d’utiliser la métrique weighted-F1-score pour évaluer les performances de la classification. 
                  
    #               L’objectif du projet étant de faire mieux que les résultats du modèle de référence.

    #               """
    # st.markdown(text_contexte,  unsafe_allow_html=True)
    
    #st.header("Objectifs")
    # text_objectif =  """
    #        ---
    #        Ce streamlit présente les étapes que nous avons suivies, depuis le Preprocessing des données jusqu'à l'implémentation de modèles de Deep Learning 
    #        & Machine Learning et l’optimisation des résultats obtenus.
    #          """
    # st.markdown(text_objectif,  unsafe_allow_html=True)   
    
    page_content(text_page ='./page_descriptions/description_projet.md')  
    
    
def page_content(text_page):
        
        '''The text page. Read from .md file '''
        with open(text_page, 'r', encoding='utf-8') as txtpage: 
            txtpage = txtpage.read().split('---Insersetion---')
            st.markdown(txtpage[0], unsafe_allow_html=True)
        st.markdown('----------' ) 
        st.markdown(txtpage[1], unsafe_allow_html=True)
    # page_bg_img = '''
    
    #    <style>
    #    # /*background de la page  et couleur du texte*/ 
    #    #  section{
    #    #      background: #f08080;        
    #    #      color: 	#000000;
    #    #  }
        
    #    #  /*Titre   Rakuten France M ....*/                   
    #    # h1 {
       	
    #    #    color:black ;
       	
    #    # }
    
    
    
    #    # .css-hi6a2p {
    #    #     max-width: 830px;
    #    #     }
    #    # /*Titre   Le projet ....*/ 
    #    # h2 {
       
    #    #     color: #blacl;
           
    
               
    #    # /*Titre   info*/   
    #    .stAlert{
    #        background: 	#0000ff;
    #        border: solid 1px black;
    #        border-radius: 15px;
    
    #    }
    
       
    
    #    </style>
    #    '''
    # #st.markdown(page_bg_img, unsafe_allow_html=True)
    
       
       