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


if __name__ == "__main__":
	Train_Data = pd.read_csv("Input_ML.csv", sep=",", engine="python")
	Train_np=Train_Data.values
	X_Train=Train_np[:,2:]

	
	Train_Data['Logistic_Regression']=0
	Train_Data['Decision_Tree']=0
	Train_Data['SVM_Linear']=0
	Train_Data['SVM_Poly']=0
	Train_Data['SVM_Rbf']=0
	Train_Data['Random_Forest']=0
	Train_Data['Lightgbm']=0
	Train_Data['PU_Bagging_Logistic_Regression']=0
	Train_Data['PU_Bagging_Decision_Tree']=0
	Train_Data['PU_Bagging_SVM_Linear']=0
	Train_Data['PU_Bagging_SVM_Poly']=0
	Train_Data['PU_Bagging_SVM_Rbf']=0
	Train_Data['PU_Bagging_Random_Forest']=0
	Train_Data['PU_Bagging_Lightgbm']=0
	Train_Data['Interaction_Confidence']='0'

	model_list=['Logistic_Regression','Decision_Tree','SVM_Linear','SVM_Poly','SVM_Rbf','Random_Forest','Lightgbm',
			'PU_Bagging_Logistic_Regression','PU_Bagging_Decision_Tree','PU_Bagging_SVM_Linear','PU_Bagging_SVM_Poly',
			'PU_Bagging_SVM_Rbf','PU_Bagging_Random_Forest','PU_Bagging_Lightgbm']
			
	for model in model_list:
		model_file=model+'.sav'
		Train_Data[model]=predict_binding_score(X_Train,model_name=model_file)
	
	for i in range(0,Train_Data.shape[0]):
		model_list=list()
		for j in Train_Data.columns[10:-1]:
			if (Train_Data.loc[i,j]>=70):
				model_list.append(j)
		Train_Data.loc[i,'Interaction_Confidence']=len(model_list)/14
		
	Train_Data.to_csv('LncRNA_MRNA_Binding_Prediction.csv',index=False)

