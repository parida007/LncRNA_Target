#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pickle


# In[ ]:


def predict_binding_score(feature_set,model_name):
    filename = 'Model_Files/Standard_Scaler_Data.sav'
    scaler = pickle.load(open(filename, 'rb'))
    feature_set=scaler.transform(feature_set)
    
    filename_1 = 'Model_Files/'+'1_'+model_name
    filename_2 = 'Model_Files/'+'2_'+model_name
    filename_3 = 'Model_Files/'+'3_'+model_name
    
    
    model_1 = pickle.load(open(filename_1, 'rb'))
    model_2 = pickle.load(open(filename_2, 'rb'))
    model_3 = pickle.load(open(filename_3, 'rb'))
    
    Y_Pred_1=model_1.predict_proba(feature_set)
    Y_Pred_2=model_2.predict_proba(feature_set)
    Y_Pred_3=model_3.predict_proba(feature_set)
    binding_proba=(Y_Pred_1+Y_Pred_2+Y_Pred_3)/3
    
    binding_perc=binding_proba[:,1]*100
    return binding_perc

   

