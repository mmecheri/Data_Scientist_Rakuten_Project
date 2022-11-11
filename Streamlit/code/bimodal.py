import streamlit as st
from PIL import Image

def app():

    st.subheader("Modélisation basée sur les données Texte et Images")
    read_page_text(text_page ='./page_descriptions/bimodal_txt.md')
                

    
def read_page_text(text_page):
            '''The text page. Read from .md file '''
            with open(text_page, 'r', encoding='utf-8') as txtpage: 
                txtpage = txtpage.read().split('---Insersetion---')
                st.markdown(txtpage[0], unsafe_allow_html=True)
                
                st.markdown(txtpage[1], unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(txtpage[2], unsafe_allow_html=True)
                with col2:
                     st.markdown(txtpage[3], unsafe_allow_html=True)
                     
                st.markdown(txtpage[4], unsafe_allow_html=True)    
                # col2, col3 = st.columns(2)
                # with col2:
                st.markdown(txtpage[5], unsafe_allow_html=True)
                # with col3:
                # st.markdown(txtpage[6], unsafe_allow_html=True)
                
                agree1 = st.checkbox('Afficher Les poids utilisés pour le Weighted Average voting')                
                if agree1:
                  st.markdown(txtpage[6], unsafe_allow_html=True)
                  
              # Résultats --------------------------Simple DNN conv1E Xception-----------------------------------------------

                st.markdown(txtpage[7], unsafe_allow_html=True)
                #msg1 = '<span style="color:red">La classe de produit prédite: A REVOIR le numéros des classes </span>'
                #st.markdown(msg1, unsafe_allow_html=True)
                #image1 = Image.open('./doc/bimodal_result_1.png')
                image1 = load_image('bimodal_result_1.png')               
                st.image(image1, use_column_width='auto')
                #st.info(txtpage[8]) # A revoir
                
                agree2 = st.checkbox('Afficher les F1-score par classe, par catégorie avec la 1ère combinaison de Vote')                
                if agree2:
                  # image1 = Image.open('./doc/tab_voting_DNN_Con1D_Xception.png')     
                  #image2 = Image.open('./doc/bimodal_avec_xception.png') 
                  image2 = load_image('bimodal_avec_xception.png') 
                  st.image(image2, use_column_width='auto')
                  
                  
               # Résultats --------------------------Simple DNN conv1E Inception-----------------------------------------------
                st.markdown(txtpage[8], unsafe_allow_html=True)
                #image3 = Image.open('./doc/bimodal_result_2.png') 
                image3 = load_image('bimodal_result_2.png')               
                st.image(image3, use_column_width='auto')
                
                # msg2 = '<span style="color:red">La classe de produit prédite: A REVOIR le numéros des classes</span>'
                # st.markdown(msg2, unsafe_allow_html=True)
                #st.info(txtpage[10]) # Revoir
                
                agree3 = st.checkbox('Afficher les F1-score par classe, par catégorie avec la 2ème combinaison de Vote')   
                if agree3:
                   #image4 = Image.open('./doc/bimodal_avec_inceptionV3.png')
                   image4 = load_image('bimodal_avec_inceptionV3.png') 
                   st.image(image4, use_column_width='auto')

                #tableau_comparison
                #msg3 = '<span style="color:red">Ajouter Tableau tous les modèles + Vote inception et Xception </span>'
                #st.markdown(msg3, unsafe_allow_html=True)
                st.markdown(txtpage[9], unsafe_allow_html=True)
                agree4 = st.checkbox('Analyse et comparaison des résultats des deux combinaisons')   
                if agree4:
                    #image5 = Image.open('./doc/tableau_comparison.png')
                  # image5 = Image.open('./doc/tableau_comparison.png')
                    image5 = load_image('tableau_comparison_last.png') 
                    st.image(image5, use_column_width='auto')

                
                st.markdown('----------')
                st.info(txtpage[10])




@st.cache(allow_output_mutation=True)
def load_image(imageName):
    #data = dict()
    image = Image.open('./doc/'+imageName)
    return image