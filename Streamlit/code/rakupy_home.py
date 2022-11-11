import streamlit as st
from multiapp import MultiApp
#import home, dataset, models,bimodal,text_models, img_models, demo,conclusion
import home,  demo, dataset ,models, conclusion
# Start page


#@st.cache()
def main():
    
    
    st.set_page_config('rakupy', layout="wide")  
  
    apps = MultiApp('Navigation','Menu')
 
    # Add all your application here    
    apps.add_app("Description du projet", home.app)
    apps.add_app("Jeu de données", dataset.app)
    #apps.add_app("Visualisation des données", dataViz.app)
    apps.add_app("Modélisation", models.app)
    apps.add_app("Démo", demo.app)
    apps.add_app("Conclusion", conclusion.app)

                
    
    # The main app
    apps.run()


if __name__ == '__main__': 
    #import os
    # with streamlit_analytics.track(unsafe_password=os.environ['analytics_pwd']): 
    #st.set_page_config(page_title='Rakuten France Multimodal Product Data Classification', page_icon='./docs/datascientest.png', layout='centered', initial_sidebar_state='auto')
    #try: 
     main()
    #except: 
      # st.error('Oops! Something went wrong...! ')
      # raise
