import streamlit as st
import dataset_description, data_exp_Viz, data_preprocessing
from multiapp import MultiApp
from submultiapp import SubMultiApp

def app():

    st.title("Jeu de données")
    #data_description_txt.md contains the page text
    # read_text(homepage_path='data_description_txt.md')
    
    apps = SubMultiApp(None, 'Donnée')
  
    apps.add_app("Description", dataset_description.app)  
    apps.add_app("Exploration et DataViz", data_exp_Viz.app)
    apps.add_app("Preprocessing", data_preprocessing.app)
    
    apps.run()
    
    
def read_text(homepage_path):
        '''The home page. '''
        with open(homepage_path, 'r', encoding='utf-8') as homepage: 
            homepage = homepage.read().split('------')
            st.markdown(homepage[0], unsafe_allow_html=True)
   