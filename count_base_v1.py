import pandas as pd
import numpy as np
from io import StringIO
from Bio.SeqUtils import GC
import os

filter_file='final_energy_data.txt'
os.system("grep -v \"((\" "+filter_file+" > input.txt")

def generateData(cont_1_list,cont_2_list):
    cont_1_str="".join(cont_1_list)
    cont_2_str="".join(cont_2_list)
    
    str_pd=pd.read_csv(StringIO(cont_2_str))
    str_pd['two_struct']=str_pd.structure.str.split('III')
    str_pd['seq1_len']=str_pd.two_struct.str[0].apply(lambda x:len(x))
    str_pd['seq2_len']=str_pd.two_struct.str[1].apply(lambda x:len(x))
    for i in range(0,str_pd.shape[0]):
        str_pd.loc[i,'seq1_gc']=GC(str_pd.two_struct[i][0])/100
        str_pd.loc[i,'seq2_gc']=GC(str_pd.two_struct[i][1])/100
    str_pd_1=pd.read_csv(StringIO(cont_1_str))
    str_pd_1['segment_count']=str_pd.shape[0]
    str_pd_1['lncrna_rel_GC_ratio']=str_pd.seq1_gc.sum()/str_pd.shape[0]
    str_pd_1['mrna_rel_GC_ratio']=str_pd.seq2_gc.sum()/str_pd.shape[0]
    return str_pd_1



fo = open("input.txt", "r")
line_no=list()
cont_1_list=list()
first_list=list()
cont_2_list=list()
second_list=list()
count=1

for x in fo:
    if str.startswith(x,','):
        if(len(cont_2_list)!=0):
            second_list.append(cont_2_list)
            cont_2_list=list()
        flag=-1
    elif (str.startswith(x,'lncrna')):
        if(len(cont_1_list)!=0):
            first_list.append(cont_1_list)
            cont_1_list=list()
        flag=1
    if flag>0:
        cont_1_list.append(x)
    elif flag<0:
        cont_2_list.append(x)
    count+=1
first_list.append(cont_1_list)
second_list.append(cont_2_list)




final_df=pd.DataFrame(columns=['lncrna', 'mrna', 'acc_energy_lncrna(kcal/mol)',
       'acc_energy_mrna(kcal/mol)', 'hybrid_energy(kcal/mol)',
       'int_energy(kcal/mol)', 'segment_count', 'lncrna_rel_GC_ratio',
       'mrna_rel_GC_ratio'])
for i in range(0,len(first_list)):
    interaction_out=generateData(first_list[i],second_list[i])
    final_df=final_df.append(interaction_out)


final_df.to_csv('out2.csv',sep='\t',index=False)




