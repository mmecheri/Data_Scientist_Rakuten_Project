import streamlit as st
import pandas as pd
import numpy as np
import data_exp_Viz, data_preprocessing
from multiapp import MultiApp
# from submultiapp import SubMultiAppMultiApp
from PIL import Image

def app():

    st.subheader('Description des données')
  
    read_page_text(text_page ='./page_descriptions/data_description_txt.md')     
  
    load_samples()
#

def read_page_text(text_page):
        '''The text page. Read from .md file '''
        with open(text_page, 'r', encoding='utf-8') as txtpage: 
            txtpage = txtpage.read().split('------')
            st.markdown(txtpage[0], unsafe_allow_html=True)


def load_samples():
    
   # image = Image.open(path + im_name)
  
    #col1, col2 = st.columns([2,1])
    col1, col2, col3 = st.columns([2.5,1,0.75])
    with col1:
        #st.header("Exemple d\'entrées -  donnée d\'entrainement")
        #☺st.image(image,output_format="auto")
        st.markdown('Extract du dataset d\'entrainement(X_train):',  unsafe_allow_html=True) 
        df = pd.read_pickle('./demo_Inputs/data/Extact_Xtain.pkl')
        df.index.name = 'Id'     
        st.dataframe(df) 
        agree1 = st.checkbox('Afficher la description des colonnes')
        if agree1:
              with open('./page_descriptions/data_col_description.md', 'r', encoding='utf-8') as subpage1: 
               subpage1 = subpage1.read().split('------')
               st.markdown(subpage1[0], unsafe_allow_html=True)
    
    with col2:
           st.markdown('Les classes associées «**prdtypecode**»(y_train)',  unsafe_allow_html=True) 
           df = pd.read_pickle('./demo_Inputs/data/Extact_Ytain.pkl')
          # df.index.name = 'Id'     
           st.dataframe(df)
    
    
    with col3:
        with open('./page_descriptions/data_img_description.md', 'r', encoding='utf-8') as subpage2: 
            subpage2 = subpage2.read().split('------')
            st.markdown(subpage2[0], unsafe_allow_html=True) 
         

    
    
    
    image = Image.open('./doc/exmpl_data_with_image.png')
    st.image(image,output_format="auto")  
       
        
        
        
        
        
        
    # st.markdown('----------' )   
    
    # col3, col4 = st.columns([2,1])

    # with col3:
    #      image = Image.open('./doc/images_sample.png')
    #      st.image(image,output_format="auto") 
        
    # with col4:
    #     with open('./page_descriptions/data_img_description.md', 'r', encoding='utf-8') as subpage2: 
    #         subpage2 = subpage2.read().split('------')
    #         st.markdown(subpage2[0], unsafe_allow_html=True)
            
    # st.markdown('----------' ) 
    # col5, col6 = st.columns([2,1])

    # with col5:
    #     df = pd.read_csv('./demo_Inputs/data/Extact_Ytain.csv',sep=',' , index_col=0)
    #    # df.index.name = 'Id'     
    #     st.dataframe(df) 
        
    # with col6:
    #     with open('./page_descriptions/data_ytrain_description.md', 'r', encoding='utf-8') as subpage2: 
    #         subpage2 = subpage2.read().split('------')
    #         st.markdown(subpage2[0], unsafe_allow_html=True)