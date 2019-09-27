#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report
import pickle
from Predict_Binding import predict_binding_score
import sys
import warnings
warnings.filterwarnings('ignore')


# In[2]:


if __name__ == "__main__":
    Train_Data = pd.read_csv("Input_ML.csv", sep=",", engine="python")
    Train_np=Train_Data.values
    X_Train=Train_np[:,2:]


    Train_Data['Binary_Classifier_Logistic_Regression']=0
    Train_Data['Binary_Classifier_Decision_Tree']=0
    Train_Data['Binary_Classifier_SVM_Linear']=0
    Train_Data['Binary_Classifier_SVM_Poly']=0
    Train_Data['Binary_Classifier_SVM_RBF']=0
    Train_Data['Binary_Classifier_Random_Forest']=0
    Train_Data['Binary_Classifier_LightGBM']=0
    Train_Data['PU_BAGGING_Logistic_Regression']=0
    Train_Data['PU_BAGGING_Decision_Tree']=0
    Train_Data['PU_BAGGING_SVM_Linear']=0
    Train_Data['PU_BAGGING_SVM_Poly']=0
    Train_Data['PU_BAGGING_SVM_RBF']=0
    Train_Data['PU_BAGGING_Random_Forest']=0
    Train_Data['PU_BAGGING_LightGBM']=0
    Train_Data['Interaction_Confidence']='0'

    model_list=['Binary_Classifier_Logistic_Regression','Binary_Classifier_Decision_Tree','Binary_Classifier_SVM_Linear',
                'Binary_Classifier_SVM_Poly','Binary_Classifier_SVM_RBF','Binary_Classifier_Random_Forest','Binary_Classifier_LightGBM',
            'PU_BAGGING_Logistic_Regression','PU_BAGGING_Decision_Tree','PU_BAGGING_SVM_Linear','PU_BAGGING_SVM_Poly',
            'PU_BAGGING_SVM_RBF','PU_BAGGING_Random_Forest','PU_BAGGING_LightGBM']

    for model in model_list:
        model_file=model+'.sav'
        Train_Data[model]=predict_binding_score(X_Train,model_name=model_file)

    for i in range(0,Train_Data.shape[0]):
        model_list=list()
        for j in Train_Data.columns[10:-1]:
            if (Train_Data.loc[i,j]>=64.5):
                model_list.append(j)
        Train_Data.loc[i,'Interaction_Confidence']=str(len(model_list)/14)

    Train_Data.to_csv('LncRNA_MRNA_Binding_Prediction.csv',index=False)


# In[ ]:




