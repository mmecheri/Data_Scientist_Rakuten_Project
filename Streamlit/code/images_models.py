
import streamlit as st
from PIL import Image


#   
def app():

    st.subheader("Modélisation partie Images")
    page_content(text_page ='./page_descriptions/models_image_txt.md')     
                
       
def page_content(text_page):
        
        '''The text page. Read from .md file '''
        with open(text_page, 'r', encoding='utf-8') as txtpage: 
            txtpage = txtpage.read().split('---Insersetion---')
            st.markdown(txtpage[0], unsafe_allow_html=True)
            
            
            # with col1:
            #  st.markdown(txtpage[1], unsafe_allow_html=True)
            # # Modèles --------------------------------------------------------------------------------- 
            #  image1 = Image.open('./doc/imgs_selected_models.png')
            #  st.image(image1, use_column_width='auto')
           # Paramères ---------------------------------------------------------------------------------
            st.markdown(txtpage[1], unsafe_allow_html=True)
            col1, col2 = st.columns([0.3,1])
            with col2:           
               # Modèles --------------------------------------------------------------------------------- 
                #image1 = Image.open('./doc/imgs_selected_models.png')
                image1 = load_image('imgs_selected_models.png')
                st.image(image1, use_column_width='auto')
                      
            
            agree1 = st.checkbox('Afficher les paramètres utilisés')
            if agree1:       
             st.markdown(txtpage[2], unsafe_allow_html=True)

            agree2 = st.checkbox('Couches de classification')
            if agree2:       
              # image12 = load_image('classification_layers.png')
               image12 = load_image('classification_layers.png')
               st.image(image12, use_column_width='auto')

       # STEP1 Démarche--------------------------------------------------------------------------------
            st.markdown(txtpage[3], unsafe_allow_html=True)
       # STEP1 Résultats--------------------------------------------------------------------------------
    
            st.markdown(txtpage[4], unsafe_allow_html=True)
            #image3 = Image.open('./doc/result_img_step1.png') 
            image3 = load_image('result_img_step1.png')
            st.image(image3, use_column_width='auto')
            
            st.markdown(txtpage[5], unsafe_allow_html=True)
            #image4 = Image.open('./doc/result_img_step1_top_5.png')
            image4 = load_image('result_img_step1_top_5.png')
            st.image(image4, use_column_width='auto')
            
            agree3 = st.checkbox('Afficher les F1-score par classe, par catégorie et par modèle')
            if agree3:
              #image5 = Image.open('./doc/result_img_step1_top_5_details.png')
              image5 = load_image('result_img_step1_top_5_details.png')
              st.image(image5, use_column_width='auto')
            st.markdown('----------' )      
      # STEP2 Démarche--------------------------------------------------------------------------------
            #st.markdown(txtpage[6], unsafe_allow_html=True)           
       # STEP2 Résultats---------------------------------------------------------------------------------       
            #image6 = Image.open('./doc/result_img_step2.png')
            col3, col4 = st.columns([0.75,0.25])
            with col3:
              st.markdown(txtpage[6], unsafe_allow_html=True) 
              image6 =  load_image('result_img_step2.png')
              st.image(image6, use_column_width='auto')
              st.info('''L’augmentation des données ne semble pas apporter une amélioration au niveau des performances,voire les dégrade un peu ! 
                      Cependant, ils pourraient mieux se généraliser sur des nouveaux jeux de données''')
            with col4:
              st.markdown(txtpage[15], unsafe_allow_html=True) 
              # st.markdown('Rappel - Meilleurs scores jusqu\'ici(Etape 1) (Sans agmentation des données)' ) 
              # image12 =  load_image('rappel_step1.png')
              # st.image(image12, use_column_width='auto')
            
            st.markdown('----------' ) 
            
            col4, col5 = st.columns([0.75,0.25])
           
            with col4:
       # STEP3 Démarche--------------------------------------------------------------------------------
             st.markdown(txtpage[7], unsafe_allow_html=True)                 
       # STEP3 Résultats--------------------------------------------------------------------------------- 
            #image7 = Image.open('./doc/result_img_step3.png')
             image7 =  load_image('result_img_step3.png')
             st.image(image7, use_column_width='auto')
             st.info( '''  
            	Nous observons une amélioration au niveau de tous les modèles, sauf pour le DenseNet121 qui n'a pas bougé.
             Xception passe en tête avec 0.65 en F1-score Weighted avec une amélioration de 4% par rapport à son score obtenu à l’étape 1''')
             st.markdown('----------' ) 
            with col5:
             st.markdown(txtpage[16], unsafe_allow_html=True)
        # STEP4 Démarche--------------------------------------------------------------------------------
        
        
            st.markdown(txtpage[8], unsafe_allow_html=True)
   # # # STEP4 Résultats---------------------------------------------------------------------------------
            #image8 = Image.open('./doc/result_LR_step4.png')
            image8 =  load_image('result_LR_step4.png')
            st.image(image8,use_column_width='auto')           
            agree4 = st.checkbox('Afficher un exemple de la méthode suivie pour obetenir ces Learning Rate optimisés(Xception)')
            if agree4:
                col1, col2 = st.columns([2,1])        
                with col1:
                    #image9 = Image.open('./doc/exemple_LR_Xception.png')
                    image9 =  load_image('exemple_LR_Xception.png')
                    st.image(image9, use_column_width='auto')
                with col2:
                      st.markdown(txtpage[9], unsafe_allow_html=True)
                    
                col3, col4 = st.columns([2,1]) 
                with col3:
                    #image10= Image.open('./doc/exemple_LR_Xception_Vs_Loss.png')
                    image10 =  load_image('exemple_LR_Xception_Vs_Loss.png')
                    st.image(image10, use_column_width='auto')
                with col4:
                    st.markdown(txtpage[10], unsafe_allow_html=True)
                    # st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
            st.markdown('----------' ) 
        # STEP5 Démarche--------------------------------------------------------------------------------
            col6, col7 = st.columns([0.75,0.25])
            with col6:
             st.markdown(txtpage[11], unsafe_allow_html=True)
    #     # STEP5 Résultats---------------------------------------------------------------------------------
             st.markdown(txtpage[12], unsafe_allow_html=True)
            #image11 = Image.open('./doc/result_img_step5.png')
             image11 =  load_image('result_img_step5.png')
             st.image(image11, use_column_width='auto')
            with col7:
             st.markdown(txtpage[17], unsafe_allow_html=True)
    
    
    # Conclusion--------------------------------------------------------------------------------
            #st.markdown(txtpage[13], unsafe_allow_html=True)
            st.info(txtpage[13])
    
            
            st.markdown('----------' ) 
            st.info(txtpage[14])
            #st.info('''Ces résultats dépassent largement ceux annoncés dans le modèle de référence Rakuten pour la classification basée sur les données Images(0.55)''')


@st.cache(allow_output_mutation=True)
def load_image(imageName):
    #data = dict()
    image = Image.open('./doc/'+imageName)
    return image