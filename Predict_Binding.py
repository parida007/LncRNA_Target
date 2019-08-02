import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pickle


def predict_binding_score(feature_set,model_name):
    filename = 'Standard_Scaler_Data.sav'
    scaler = pickle.load(open(filename, 'rb'))
    filename = model_name
    feature_set=scaler.transform(feature_set)
    loaded_model = pickle.load(open(filename, 'rb'))
    binding_proba=loaded_model.predict_proba(feature_set)
    binding_perc=binding_proba[:,1]*100
    return binding_perc

   




