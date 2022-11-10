
import streamlit as st
import text_models, img_models,images_models, bimodal
#from multiapp import MultiApp
from submultiapp import SubMultiApp


def app():
    
    st.title("Modélisation")
    #data_description_txt.md contains the page text
    # read_text(homepage_path='data_description_txt.md')
    
    #apps = SubMultiApp(None, 'Donnée')
    
    
    apps = SubMultiApp(None, 'Modélisation')
    #st.title("Modélisation")
    
    apps.add_app("Texte", text_models.app)
    #apps.add_app("Images", img_models.app) 
    apps.add_app("Images", images_models.app) 
    apps.add_app("Bimodal", bimodal.app)
    
    # text_data = """Modélisation texte
    #             """
                
    # st.markdown(text_data,  unsafe_allow_html=True) 
    #st.image(path+"sorties.jpg")
    # add_checkbox_2 = st.sidebar.radio('Modélisation:' , ('Texte',
    #                                   'Images', 'Bimodal'))
    
    apps.run()