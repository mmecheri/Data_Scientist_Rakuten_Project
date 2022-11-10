
import streamlit as st
import text_models, img_models,images_models, bimodal
from multiapp import MultiApp


def app():
    
    apps = MultiApp(None, 'Modélisation')
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