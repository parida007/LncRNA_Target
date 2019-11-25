import os
from numpy import *
import numpy as np
import pandas as pd
from Bio import SeqIO
import sys

str1='query.fa'
str2='RNA_Composition_LNC.csv'
str3='target.fa'
str4='RNA_Composition_MRNA.csv'
str5='LNCRNA_Rel_Composition.csv'
str6='MRNA_Rel_Composition.csv'



os.system("python cal_modified_hybrid_energy1.py")

os.system("awk 'NF > 0' final_energy_data.txt >final_energy_data1.txt")
os.system("mv  final_energy_data1.txt final_energy_data.txt")
os.system("rm  final_energy_data1.txt")
os.system("python count_base_v1.py")
os.system("python features_predict.py "+str1+" "+str2+" "+str5)
os.system("python features_predict.py "+str3+' '+str4+" "+str6)
os.system("python Dataset_Generator.py")

#os.system("/home/sibun/anaconda3/bin/python features_predict.py "+str1+" "+str2+" "+str5)
#os.system("/home/sibun/anaconda3/bin/python features_predict.py "+str3+' '+str4+" "+str6)
#os.system("/home/sibun/anaconda3/bin/python Dataset_Generator.py")

