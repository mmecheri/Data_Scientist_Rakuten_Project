# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:30:24 2022

@author: MME
"""
import streamlit as st
#import conv1D
import  demo_inputs
import  cleaning_text  
from PIL import Image
import numpy as np
import cv2
#from  init_demo_input import input_config
# homme.py
# from  demo_inputs import get_inputs
# from  load_data import get_data
# from  load_best_models import get_models


def app():
   
    
    st.title("Prédictions (Démo)")
    contenent_page(text_page ='./page_descriptions/demo_txt.md')


def contenent_page(text_page):
    
    '''The text page. Read from .md file '''
    with open(text_page, 'r', encoding='utf-8') as txtpage: 
        txtpage = txtpage.read().split('---Insersetion---')
        
        st.markdown(txtpage[0], unsafe_allow_html=True) 

     
        classif_options = st.selectbox(
        'Veuillez sélectionner le type de classification',
          (['', 'A partir du Texte', 'A partir d\'Images', 'A partir du Texte et d\'Images(Bimodal)']))
    
        
        if classif_options != '':
                
            if classif_options == 'A partir du Texte':
                st.markdown(txtpage[1], unsafe_allow_html=True)                           
                models_txt_options = st.selectbox(
                  'Veuillez sélectionner un modèle',
                  (['','Conv1D', 'Simple DNN']))
            
                
            elif classif_options == 'A partir d\'Images':
                st.markdown(txtpage[1], unsafe_allow_html=True) 
                models_img_options = st.selectbox(
                  'Veuillez sélectionner un modèle',
                  (['', 'Xception', 'InceptionV3']))
              
                
            elif classif_options == 'A partir du Texte et d\'Images(Bimodal)':
                    st.markdown(txtpage[1], unsafe_allow_html=True) 
                    models_bimod_options = st.selectbox(
                      'Veuillez sélectionner une combinaison',
                      (['', 'Conv1D & Simple DNN & Xception', 'Conv1D & Simple DNN & InceptionV3']))
                                    
               
            st.markdown(txtpage[2], unsafe_allow_html=True)                    

            source_options = st.selectbox(
                      'Veuillez sélectionner une source de données',
                      #(['', 'Echantillon du jeu de données(Choix Aléatoire)', 'Manuel', 'Avec une URL le site de Rakuten' ]))
                      (['', 'Echantillon du jeu de données(Choix Aléatoire)', 'Manuel' ]))

     
#***************************************************************************************************************************** 
#------------------------------------------ Depuis le jeu de données d\'entrainement(Choix Aléatoire)--------------------------
#*****************************************************************************************************************************          
            if  classif_options == 'A partir du Texte' and models_txt_options == 'Conv1D' :
              if  source_options == 'Echantillon du jeu de données(Choix Aléatoire)':
           
           
                  if st.button('Obtenir un exemple et Classifier'): 
                      design, descrip, im_name, text_cleaned, row_index = demo_inputs.get_random_row()
                     
                                         
                      st.text_input('Designation', design, disabled = True)
                      st.text_input('Description', descrip, disabled = True)
                                    
                      pred_class , pred_label ,y_pred_proba =  demo_inputs.predict_with_conv1D(text_cleaned)                    
                      prodcode, label = demo_inputs.get_real_class_info(row_index)
                      
                      col1, col2 = st.columns(2)
                      with col1: 
                          msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                          msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_label + '</span>'
                    
                          precision = np.amax(y_pred_proba)
                          precision = precision * 100
                          precision = np.round(precision,2)
                        
                          msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                          st.markdown(msg1, unsafe_allow_html=True)
                          st.markdown(msg2, unsafe_allow_html=True) 
                          st.markdown(msg3, unsafe_allow_html=True) 
                                      
                      with col2:                       
                              msg4 = '<span style="color:green">Classe rèelle du produit: '  + str(prodcode) + '</span>'
                              msg5 = '<span style="color:green">Catégorie rèelle du produit : ' + str(label) + '</span>'
                              st.markdown(msg4, unsafe_allow_html=True) 
                              st.markdown(msg5, unsafe_allow_html=True) 
                              
# #****************************************************************************************************************                  
            if  classif_options == 'A partir du Texte' and models_txt_options == 'Simple DNN' :
                      if  source_options == 'Echantillon du jeu de données(Choix Aléatoire)':
                   
                   
                          if st.button('Obtenir un exemple et Classifier'): 
                              design, descrip, im_name, text_cleaned,row_index = demo_inputs.get_random_row()
                                                         
                            
                              st.text_input('Designation', design, disabled = True)
                              st.text_input('Description', descrip, disabled = True)
                                     
                              pred_class , pred_label ,y_pred_proba =  demo_inputs.predict_with_simpDNN(text_cleaned) 
                              prodcode, label = demo_inputs.get_real_class_info(row_index)
                     
                              col1, col2 = st.columns(2)
                              with col1: 
                               msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                               msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_label + '</span>'
                            
                               precision = np.amax(y_pred_proba)
                               precision = precision * 100
                               precision = np.round(precision,2)
                            
                               msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                               st.markdown(msg1, unsafe_allow_html=True)
                               st.markdown(msg2, unsafe_allow_html=True) 
                               st.markdown(msg3, unsafe_allow_html=True) 
                            			  
                              with col2:                       
                            	  msg4 = '<span style="color:green">Classe rèelle du produit: '  + str(prodcode) + '</span>'
                            	  msg5 = '<span style="color:green">Catégorie rèelle du produit : ' + str(label) + '</span>'
                            	  st.markdown(msg4, unsafe_allow_html=True) 
                            	  st.markdown(msg5, unsafe_allow_html=True)
                                  
# #****************************************************************************************************************            
            if  classif_options == 'A partir d\'Images' and models_img_options == 'Xception' :
              if  source_options == 'Echantillon du jeu de données(Choix Aléatoire)':
             
           
                  if st.button('Obtenir un exemple et Classifier'): 

                   
                    design, descrip, im_name, text_cleaned, row_index = demo_inputs.get_random_row()
                
                     
                    image = Image.open(demo_inputs.images_dir + im_name)
                    st.image(image, caption= im_name)
                    
                    pred_class ,pred_label,y_pred_proba = demo_inputs.predict_with_xception(im_name)
                    prodcode, label = demo_inputs.get_real_class_info(row_index)
                    
                    col1, col2 = st.columns(2)
                    with col1: 
                      msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                      msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_label + '</span>'
                    
                      precision = np.amax(y_pred_proba)
                      precision = precision * 100
                      precision = np.round(precision,2)
                    
                      msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                      st.markdown(msg1, unsafe_allow_html=True)
                      st.markdown(msg2, unsafe_allow_html=True) 
                      st.markdown(msg3, unsafe_allow_html=True) 
                                  
                    with col2:                       
                          msg4 = '<span style="color:green">Classe rèelle du produit: '  + str(prodcode) + '</span>'
                          msg5 = '<span style="color:green">Catégorie rèelle du produit : ' + str(label) + '</span>'
                          st.markdown(msg4, unsafe_allow_html=True) 
                          st.markdown(msg5, unsafe_allow_html=True)
   
# #****************************************************************************************************************
            if  classif_options == 'A partir d\'Images' and models_img_options == 'InceptionV3' :
              if  source_options == 'Echantillon du jeu de données(Choix Aléatoire)':
                         
                  if st.button('Obtenir un exemple et Classifier'): 
                   
                    design, descrip, im_name, text_cleaned,row_index= demo_inputs.get_random_row()
                 
                     
                    image = Image.open(demo_inputs.images_dir + im_name)
                    st.image(image, caption= im_name)
                    
                    pred_class ,pred_label,y_pred_proba = demo_inputs.predict_with_inception(im_name)
                    prodcode, label = demo_inputs.get_real_class_info(row_index)
 
                    col1, col2 = st.columns(2)
                    with col1: 
                      msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                      msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_label + '</span>'
                    
                      precision = np.amax(y_pred_proba)
                      precision = precision * 100
                      precision = np.round(precision,2)
                    
                      msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                      st.markdown(msg1, unsafe_allow_html=True)
                      st.markdown(msg2, unsafe_allow_html=True) 
                      st.markdown(msg3, unsafe_allow_html=True) 
                                  
                    with col2:                       
                          msg4 = '<span style="color:green">Classe rèelle du produit: '  + str(prodcode) + '</span>'
                          msg5 = '<span style="color:green">Catégorie rèelle du produit : ' + str(label) + '</span>'
                          st.markdown(msg4, unsafe_allow_html=True) 
                          st.markdown(msg5, unsafe_allow_html=True)
                          
##************************************************************************************************************************  
#                                                 Bimodal
##************************************************************************************************************************            
            if  classif_options == 'A partir du Texte et d\'Images(Bimodal)' and models_bimod_options == 'Conv1D & Simple DNN & Xception' :
              if  source_options == 'Echantillon du jeu de données(Choix Aléatoire)':
            
           
                  if st.button('Obtenir un exemple et Classifier'): 
                   
                    design, descrip, im_name, text_cleaned,row_index= demo_inputs.get_random_row()
           
                    st.text_input('Designation', design, disabled = True)
                    st.text_input('Description', descrip, disabled = True)
                    
                    image = Image.open(demo_inputs.images_dir + im_name)
                    st.image(image, caption= im_name)  
                    
                    pred_class ,pred_label, y_pred_proba = demo_inputs.predict_conv1D_simp_DNN_xception(text_cleaned, im_name)
                    prodcode, label = demo_inputs.get_real_class_info(row_index)
                    
                    #Pred by text only
                    #Pred by image only
                    pred_class_conv1 , pred_label_conv1 ,y_pred_proba_conv1 =  demo_inputs.predict_with_conv1D(text_cleaned) 
                    pred_class_sDNN , pred_label_sDNN ,y_pred_proba_sDNN =  demo_inputs.predict_with_simpDNN(text_cleaned) 
                    pred_class_Xcep ,pred_label_Xcep,y_pred_proba_Xcep = demo_inputs.predict_with_xception(im_name) 
                  
                    
                    
                    
                    col1, col2, col3 = st.columns(3)
                    with col1: 
                     msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                     msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_label + '</span>'
                  
                     precision = np.amax(y_pred_proba)
                     precision = precision * 100
                     precision = np.round(precision,2)
                  
                     msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                     st.markdown(msg1, unsafe_allow_html=True)
                     st.markdown(msg2, unsafe_allow_html=True) 
                     st.markdown(msg3, unsafe_allow_html=True) 
                     
                     with col2:                       
                       msg4 = '<span style="color:black">La classe de produit et la catégorie prédites à partir du Texte avec le modèle Conv1D: '  + str(pred_class_conv1) +', ' +pred_label_conv1 + '</span>'
                       #msg5 = '<span style="color:black">La catégorie prédite à partir du Texte avec le modèle Conv1D : ' + pred_label_conv1 + '</span>'
                       st.markdown(msg4, unsafe_allow_html=True) 
                      # st.markdown(msg5, unsafe_allow_html=True)
                      
                       msg6 = '<span style="color:black">La classe de produit et la catégorie prédites  à partir du Texte avec le modèle Simple DNN: '  + str(pred_class_sDNN)  +', ' +pred_label_sDNN +  '</span>'
                       #msg7 = '<span style="color:black">La catégorie prédite à partir du Texte avec le modèle  Simple DNN : ' + pred_label_sDNN + '</span>'
                       st.markdown(msg6, unsafe_allow_html=True) 
                      # st.markdown(msg7, unsafe_allow_html=True) 
                      
                       msg8 = '<span style="color:black">La classe de produit et la catégorie prédites  à partir de l\'Image avec le modèle Xception(CNN): '  + str(pred_class_Xcep) +', ' +pred_label_Xcep +  '</span>'
                      # msg9 = '<span style="color:black">La catégorie prédite à partir de l\'Image avec le modèle  Xception(CNN) : ' + pred_label_Xcep + '</span>'
                       st.markdown(msg8, unsafe_allow_html=True) 
                       #st.markdown(msg9, unsafe_allow_html=True) 
                      
                    with col3:                       
                       msg10 = '<span style="color:green">Classe rèelle du produit: '  + str(prodcode) + '</span>'
                       msg11 = '<span style="color:green">Catégorie rèelle du produit : ' + str(label) + '</span>'
                       st.markdown(msg10, unsafe_allow_html=True) 
                       st.markdown(msg11, unsafe_allow_html=True)
                          
##**********************************************************************************************************************            
            if  classif_options == 'A partir du Texte et d\'Images(Bimodal)' and models_bimod_options == 'Conv1D & Simple DNN & InceptionV3' :
              if  source_options == 'Echantillon du jeu de données(Choix Aléatoire)':
                   
                  if st.button('Obtenir un exemple et Classifier'): 
                   
                    design, descrip, im_name, text_cleaned,row_index= demo_inputs.get_random_row()
                  
                    st.text_input('Designation', design, disabled = True)
                    st.text_input('Description', descrip, disabled = True)
                    
                    image = Image.open(demo_inputs.images_dir + im_name)
                    st.image(image, caption= im_name)
                    
                    pred_class ,pred_label, y_pred_proba = demo_inputs.predict_conv1D_simp_DNN_inception(text_cleaned, im_name)
                    prodcode, label = demo_inputs.get_real_class_info(row_index)
                    
                    #Pred by text only
                    #Pred by image only
                    pred_class_conv1 , pred_label_conv1 ,y_pred_proba_conv1 =  demo_inputs.predict_with_conv1D(text_cleaned) 
                    pred_class_sDNN , pred_label_sDNN ,y_pred_proba_sDNN =  demo_inputs.predict_with_simpDNN(text_cleaned) 
                    pred_class_incep ,pred_label_incep,y_pred_proba_incep = demo_inputs.predict_with_inception(im_name)
                    
                                      
                    
                    col1, col2, col3 = st.columns(3)
                    with col1: 
                     msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                     msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_label + '</span>'
                  
                     precision = np.amax(y_pred_proba)
                     precision = precision * 100
                     precision = np.round(precision,2)
                  
                     msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                     st.markdown(msg1, unsafe_allow_html=True)
                     st.markdown(msg2, unsafe_allow_html=True) 
                     st.markdown(msg3, unsafe_allow_html=True) 
                     
                     with col2:                       
                       msg4 = '<span style="color:black">La classe de produit et la catégorie prédites à partir du Texte avec le modèle Conv1D: '  + str(pred_class_conv1) +', ' +pred_label_conv1 + '</span>'
                       #msg5 = '<span style="color:black">La catégorie prédite à partir du Texte avec le modèle Conv1D : ' + pred_label_conv1 + '</span>'
                       st.markdown(msg4, unsafe_allow_html=True) 
                      # st.markdown(msg5, unsafe_allow_html=True)
                      
                       msg6 = '<span style="color:black">La classe de produit et la catégorie prédites  à partir du Texte avec le modèle Simple DNN: '  + str(pred_class_sDNN)  +', ' +pred_label_sDNN +  '</span>'
                       #msg7 = '<span style="color:black">La catégorie prédite à partir du Texte avec le modèle  Simple DNN : ' + pred_label_sDNN + '</span>'
                       st.markdown(msg6, unsafe_allow_html=True) 
                      # st.markdown(msg7, unsafe_allow_html=True) 
                      
                       msg8 = '<span style="color:black">La classe de produit et la catégorie prédites  à partir de l\'Image avec le modèle InceptionV3(CNN): '  + str(pred_class_incep) +', ' +pred_label_incep +  '</span>'
                      # msg9 = '<span style="color:black">La catégorie prédite à partir de l\'Image avec le modèle  Xception(CNN) : ' + pred_label_Xcep + '</span>'
                       st.markdown(msg8, unsafe_allow_html=True) 
                       #st.markdown(msg9, unsafe_allow_html=True) 
                      
                    with col3:                       
                       msg10 = '<span style="color:green">Classe rèelle du produit: '  + str(prodcode) + '</span>'
                       msg11 = '<span style="color:green">Catégorie rèelle du produit : ' + str(label) + '</span>'
                       st.markdown(msg10, unsafe_allow_html=True) 
                       st.markdown(msg11, unsafe_allow_html=True)
                  
##**************************************************************************************************************************** 
##----------------------------------------------Manuel------------------------------------------------------------------------
##****************************************************************************************************************************            
            if  classif_options == 'A partir du Texte' and models_txt_options == 'Conv1D' :
              if  source_options == 'Manuel':
                  
                      
                  user_Desig_input = st.text_area('Designation(obligatoire)', )
                  user_Descrip_input = st.text_area('Description', )

                
                  if st.button('Classifier'): 
                     
                      if user_Desig_input == "":
                          st.write('Veuillez saisir un le champ "Designation"' ) 
                        
                      else : 

                        df = cleaning_text.createdfManuel(user_Desig_input, user_Descrip_input)  
                        df_cleaned = cleaning_text.CreateTextANDcleaning(df)                        
        
                        
                        pred_class , pred_label ,y_pred_proba =  demo_inputs.predict_with_conv1D(df_cleaned)                    
                
                        precision = np.amax(y_pred_proba)
                        precision = precision * 100
                        precision = np.round(precision,2)
                      
                        msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                        msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_label + '</span>'
                        msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                        
                        st.markdown(msg1, unsafe_allow_html=True)
                        st.markdown(msg2, unsafe_allow_html=True)
                        st.markdown(msg3, unsafe_allow_html=True) 
        
                         
##**************************************************************************************************************** 
##****************************************************************************************************************           
            if  classif_options == 'A partir du Texte' and models_txt_options == 'Simple DNN' :
              if  source_options == 'Manuel':
                  
                             
                  user_Desig_input = st.text_area('Designation(obligatoire)', )
                  user_Descrip_input = st.text_area('Description', )

                
                  if st.button('Classifier'): 
                     
                      if user_Desig_input == "":
                          st.write('Veuillez saisir un le champ "Designation"' ) 
                        
                      else :  
                                               
                        
                        df = cleaning_text.createdfManuel(user_Desig_input, user_Descrip_input)  

                        df_cleaned = cleaning_text.CreateTextANDcleaning(df)                        
 
                        
                        pred_class , pred_label ,y_pred_proba =  demo_inputs.predict_with_simpDNN(df_cleaned)
                        
                        precision = np.amax(y_pred_proba)
                        precision = precision * 100
                        precision = np.round(precision,2)
                        
                        msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                        msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_label + '</span>'
                        msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                        st.markdown(msg1, unsafe_allow_html=True)
                        st.markdown(msg2, unsafe_allow_html=True)
                        st.markdown(msg3, unsafe_allow_html=True)
                

##**************************************************************************************************************** 
##****************************************************************************************************************            
            if  classif_options == 'A partir d\'Images' and models_img_options == 'Xception' :
              if  source_options == 'Manuel':
                       
                  #uploaded_file = st.file_uploader("Sélectionner un fichier image", type="jpg")
                  uploaded_file = st.file_uploader("Sélectionner un fichier image")
                  #img="" 
                  if uploaded_file is not None: 
                     
                      file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                      opencv_image = cv2.imdecode(file_bytes, 1)                    
   
                      st.image(opencv_image, channels="BGR",width=299) 
         
                      if st.button('Classifier'): 
                       pred_class ,pred_label,y_pred_proba = demo_inputs.predict_with_xception_manu(opencv_image)
                       
                       precision = np.amax(y_pred_proba)
                       precision = precision * 100
                       precision = np.round(precision,2)
                       
                       msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                       msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_label + '</span>'
                       msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                       st.markdown(msg1, unsafe_allow_html=True)
                       st.markdown(msg2, unsafe_allow_html=True)
                       st.markdown(msg3, unsafe_allow_html=True)

##****************************************************************************************************************
##****************************************************************************************************************            
            if  classif_options == 'A partir d\'Images' and models_img_options == 'InceptionV3' :
              if  source_options == 'Manuel':
                       
                  #uploaded_file = st.file_uploader("Sélectionner un fichier image", type="jpg")
                  uploaded_file = st.file_uploader("Sélectionner un fichier image")
                  #img="" 
                  if uploaded_file is not None: 
                     
                      file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                      opencv_image = cv2.imdecode(file_bytes, 1)                   
                      st.image(opencv_image, channels="BGR",width=299) 

                      if st.button('Classifier'):
                       pred_class ,pred_label,y_pred_proba =demo_inputs.predict_with_inception_manu(opencv_image)
                      
                       precision = np.amax(y_pred_proba)
                       precision = precision * 100
                       precision = np.round(precision,2)

                       msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                       msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_label + '</span>'
                       msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                       
                       st.markdown(msg1, unsafe_allow_html=True)
                       st.markdown(msg2, unsafe_allow_html=True)
                       st.markdown(msg3, unsafe_allow_html=True)

##****************************************************************************************************************
##****************************************************************************************************************            
            if  classif_options == 'A partir du Texte et d\'Images(Bimodal)' and models_bimod_options == 'Conv1D & Simple DNN & Xception' :
              if  source_options == 'Manuel':
                       
                  # Add Descignation and descption text input 
                       user_Desig_input = st.text_area('Designation(obligatoire)', )
                       user_Descrip_input = st.text_area('Description', )                       
                       #uploaded_file = st.file_uploader("Sélectionner un fichier image", type="jpg") 
                       uploaded_file = st.file_uploader("Sélectionner un fichier image")  
    
                       
                       if uploaded_file is not None:
                           # To read file as bytes:
                          file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                          opencv_image = cv2.imdecode(file_bytes, 1)                  
                          st.image(opencv_image, channels="BGR",width=299) 
                        
                                                   
                       if st.button('Classifier'): 
                       
                         if user_Desig_input == "" and uploaded_file is  None:
                            st.write('Veuillez renseigner le champ "Designation" est charger une image' ) 
                          
                         elif uploaded_file is  None:
                             st.write('Veuillez charger une image')
                          
                                      
                         elif user_Desig_input == "":                          
                                 st.write('Veuillez renseigner le champ "Designation"')
                             
                         else : 
                             df = cleaning_text.createdfManuel(user_Desig_input, user_Descrip_input) 
                             df_cleaned = cleaning_text.CreateTextANDcleaning(df)                       

                             # file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                             # opencv_image = cv2.imdecode(file_bytes, 1)                  
                             # st.image(opencv_image, channels="BGR",width=299) 
                 
                    
                             
                             pred_class ,pred_label, proba = demo_inputs.predict_conv1D_simp_DNN_xception_manu(df_cleaned, opencv_image) 
                             
                             
                             #Pred by text only
                            #Pred by image only
                             pred_class_conv1 , pred_label_conv1 ,y_pred_proba_conv1 =  demo_inputs.predict_with_conv1D(df_cleaned) 
                             pred_class_sDNN , pred_label_sDNN ,y_pred_proba_sDNN =  demo_inputs.predict_with_simpDNN(df_cleaned) 
                             pred_class_Xcep ,pred_label_Xcep,y_pred_proba_Xcep = demo_inputs.predict_with_xception_manu(opencv_image) 
                             
                             col1, col2= st.columns(2)
                             with col1: 
                              msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                              msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_label + '</span>'  
                              
                              precision = np.amax(proba)
                              precision = precision * 100
                              precision = np.round(precision,2)
                              
                              msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                              st.markdown(msg1, unsafe_allow_html=True)
                              st.markdown(msg2, unsafe_allow_html=True)
                              st.markdown(msg3, unsafe_allow_html=True)
                              
                              
                             with col2: 
                                msg4 = '<span style="color:black">La classe de produit et la catégorie prédites à partir du Texte avec le modèle Conv1D: '  + str(pred_class_conv1) +', ' +pred_label_conv1 + '</span>'
                                st.markdown(msg4, unsafe_allow_html=True) 

                                msg6 = '<span style="color:black">La classe de produit et la catégorie prédites  à partir du Texte avec le modèle Simple DNN: '  + str(pred_class_sDNN)  +', ' +pred_label_sDNN +  '</span>'
                                st.markdown(msg6, unsafe_allow_html=True) 
                                
                                
                                msg7 = '<span style="color:black">La classe de produit et la catégorie prédites  à partir de l\'Image avec le modèle Xception(CNN): '  + str(pred_class_Xcep) +', ' +pred_label_Xcep +  '</span>'
                                st.markdown(msg7, unsafe_allow_html=True) 

                       
##****************************************************************************************************************            
            if  classif_options == 'A partir du Texte et d\'Images(Bimodal)' and models_bimod_options == 'Conv1D & Simple DNN & InceptionV3' :
              if  source_options == 'Manuel':
                       
                  # Add Descignation and descption text input 
                       user_Desig_input = st.text_area('Designation(obligatoire)', )
                       user_Descrip_input = st.text_area('Description', )                       
                       #uploaded_file = st.file_uploader("Sélectionner un fichier image", type="jpg") 
                       uploaded_file = st.file_uploader("Sélectionner un fichier image")   
                       
                       if uploaded_file is not None:
                            # To read file as bytes:
                           file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                           opencv_image = cv2.imdecode(file_bytes, 1)                  
                           st.image(opencv_image, channels="BGR",width=299) 
                                                
                       if st.button('Classifier'): 
                       
                         if user_Desig_input == "" and uploaded_file is  None:
                            st.write('Veuillez renseigner le champ "Designation" est charger une image' ) 
                          
                         elif uploaded_file is  None:
                             st.write('Veuillez charger une image')
                          
                                      
                         elif user_Desig_input == "":                          
                                 st.write('Veuillez renseigner le champ "Designation"')
                             
                         else : 
                             df = cleaning_text.createdfManuel(user_Desig_input, user_Descrip_input) 
                             df_cleaned = cleaning_text.CreateTextANDcleaning(df)                       

                             # file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                             # opencv_image = cv2.imdecode(file_bytes, 1)                   
                             # st.image(opencv_image, channels="BGR",width=299) 
                 
                                                
                             pred_class ,pred_class, proba = demo_inputs.predict_conv1D_simp_DNN_xception_manu(df_cleaned, opencv_image) 
                             
                             pred_class_conv1 , pred_label_conv1 ,y_pred_proba_conv1 =  demo_inputs.predict_with_conv1D(df_cleaned) 
                             pred_class_sDNN , pred_label_sDNN ,y_pred_proba_sDNN =  demo_inputs.predict_with_simpDNN(df_cleaned) 
                             pred_class_incep ,pred_label_incep ,y_pred_proba_incep  = demo_inputs.predict_with_inception_manu(opencv_image) 

                             col1, col2= st.columns(2)
                             with col1: 
                               msg1 = '<span style="color:blue">La classe de produit prédite: '  + str(pred_class) + '</span>'
                               msg2 = '<span style="color:blue">La catégorie prédite : ' + pred_class + '</span>'
                               
                               precision = np.amax(proba)
                               precision = precision * 100
                               precision = np.round(precision,2)
                              
                               msg3 = '<span style="color:blue">Certitude : ' + str(precision) +'%'+ '</span>'
                               st.markdown(msg1, unsafe_allow_html=True)
                               st.markdown(msg2, unsafe_allow_html=True)
                               st.markdown(msg3, unsafe_allow_html=True)

                             with col2: 
                                msg4 = '<span style="color:black">La classe de produit et la catégorie prédites à partir du Texte avec le modèle Conv1D: '  + str(pred_class_conv1) +', ' +pred_label_conv1 + '</span>'
                                st.markdown(msg4, unsafe_allow_html=True) 
                                msg6 = '<span style="color:black">La classe de produit et la catégorie prédites  à partir du Texte avec le modèle Simple DNN: '  + str(pred_class_sDNN)  +', ' +pred_label_sDNN +  '</span>'
                                st.markdown(msg6, unsafe_allow_html=True)                                 
                                
                                msg7 = '<span style="color:black">La classe de produit et la catégorie prédites  à partir de l\'Image avec le modèle Inception(CNN): '  + str(pred_class_incep) +', ' +pred_label_incep +  '</span>'
                                st.markdown(msg7, unsafe_allow_html=True) 





# @st.cache(allow_output_mutation=True)
# def load_image(imageName):
#     #data = dict()
#     image = Image.open('./doc/'+imageName)
#     return image