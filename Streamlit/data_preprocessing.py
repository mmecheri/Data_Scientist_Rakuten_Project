
import streamlit as st
from PIL import Image



#   
def app():

    st.subheader("Préprocessing des données")
    read_page_text(text_page ='./page_descriptions/data_preprocessing_txt.md')     
                
  
     
def read_page_text(text_page):
        '''The text page. Read from .md file '''
        with open(text_page, 'r', encoding='utf-8') as txtpage: 
            txtpage = txtpage.read().split('---Insersetion---')
            st.markdown(txtpage[0], unsafe_allow_html=True)
            
            # image = Image.open('./doc/Nas_values.png')
            # st.image(image, use_column_width='auto')
            
            # st.markdown(txtpage[1], unsafe_allow_html=True)
            # image = Image.open('./doc/repartition_classes_2.png')
            # st.image(image, use_column_width='auto')
            
            # st.markdown(txtpage[2], unsafe_allow_html=True)
            # image = Image.open('./doc/tableau_proportions.png')
            # st.image(image, use_column_width='auto')
            
        
           