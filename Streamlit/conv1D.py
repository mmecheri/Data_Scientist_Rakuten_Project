# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 10:45:05 2022

@author: MME
"""
# import numpy as np
# from demo_inputs import tokenize_text, get_class_code, get_label
# #from demo_inputs import load_conv1D

#model = load_conv1D()

# def predict_text(input_text, model):
    
#     #print('[predict_text] - input_text:', input_text)
#     text_tokenized = tokenize_text(input_text)
#     #print('[predict_text] - text_tokenized:', text_tokenized)
#     #model = load_conv1D()
#     #model.summary()
#     y_pred_proba = model.predict(text_tokenized)
#     y_pred_class = np.argmax(y_pred_proba,axis = 1).astype(int)
    
    
#     # Prediction
#     y_pred = y_pred_class[0]
#     pred_class = get_class_code(y_pred)
#     pred_label = get_label(pred_class)
    
#     #Real
#     #y_pred_real_target = row_cleaned['prdtypecode'].values[0]
#     # real_class = row_cleaned['prdtypecode_org'].values[0]
#     # real_label = row_cleaned['labels'].values[0]
          
 
#     #print('[predict_text] - Predicted -  Class:', pred_class)
#     #print('-----------------------------------------------------------------------------------')
#     #print('[predict_text] - Predicted -  Label:', pred_label)
#     #print('-----------------------------------------------------------------------------------')
#     return pred_class , pred_label
