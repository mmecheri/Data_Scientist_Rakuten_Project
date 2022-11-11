
import streamlit as st
from PIL import Image



#   
def app():

    st.subheader("Modélisation partie Texte")
    read_page_text(text_page ='./page_descriptions/models_text_txt.md')     
                
  
     
def read_page_text(text_page):
        '''The text page. Read from .md file '''
        with open(text_page, 'r', encoding='utf-8') as txtpage: 
            txtpage = txtpage.read().split('---Insersetion---')
            st.markdown(txtpage[0], unsafe_allow_html=True)
            
            #image1 = Image.open('./doc/tab_ml_text.png')
            image1 = load_image('tab_ml_text.png')
            st.image(image1, use_column_width='auto')
            
            agree1 = st.checkbox('Afficher les paramètres ML utilisés')
            if agree1:                          
                #image2 = Image.open('./doc/tab_ml_text_parem.png')
                image2 = load_image('tab_ml_text_parem.png')
                st.image(image2, use_column_width='auto')
                
                
            st.markdown(txtpage[1], unsafe_allow_html=True)
            #image3 = Image.open('./doc/tab_dl_text.png')
            image3 = load_image('tab_dl_text.png')
            st.image(image3, use_column_width='auto')
            
            agree2 = st.checkbox('Afficher les paramètres DL utilisés')
            if agree2:
              st.markdown(txtpage[2], unsafe_allow_html=True)  
            
            agree3 = st.checkbox('Afficher les résulats détaillés par classes de Conv1D et Simple DNN (F1-score Weighted)')
            if agree3: 
              #image4 = Image.open('./doc/tab_dl_details_conv1d_simpleDNN.png')
              image4 =  load_image('tab_dl_details_conv1d_simpleDNN.png')
              st.image(image4, use_column_width='auto')
              
            agree4 = st.checkbox('Afficher les classes les moins bien prédites (le F1-score est inférieur à celui du modèle de référence(0.80) ')            
            if agree4: 
               col1, col2 = st.columns([2,1])        
               with col1:
                   #image5 = Image.open('./doc/conv1_simpleDNN_less_ref.png')
                   image5 = load_image('conv1_simpleDNN_less_ref.png')
                   st.image(image5, use_column_width='auto')
               with col2:
                    st.markdown(txtpage[3], unsafe_allow_html=True)
                    
            st.info(txtpage[4])
           

@st.cache(allow_output_mutation=True)
def load_image(imageName):
      #data = dict()
      image = Image.open('./doc/'+imageName)
      return image  
    