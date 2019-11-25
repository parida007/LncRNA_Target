import os
from numpy import *
import numpy as np
import pandas as pd
from itertools import groupby
from operator import itemgetter
from Bio import SeqIO
import timeit
import sys

start = timeit.default_timer()
os.system("rm acc_stem_query1.txt");
os.system("rm acc_stem_target1.txt");


str1=sys.argv[1]

os.system("cp "+str1+" copy1.fa")
num_lines = sum(1 for line in open(str1))

#str2='copy3_t.fa'
str3='query_stem_t.txt'
#str4='target_stem_t.txt'
str5='query_acc1.txt'
str6='target_acc1.txt'
os.system("rm "+str6+"");

def parsorr(str,str_output,maximal_span):
 import os
 os.system("../src/ParasoR --pre --constraint "+maximal_span+" --input "+str+" --stem > "+str_output+"")
 os.system("tail -n +10 "+str_output+" > jj_t.txt")
 os.system(''' awk '{print $2"\t"$4}' jj_t.txt >input21_t.txt''')
 os.system("mv input21_t.txt "+str_output+"");
 
 return [];

 
 
def acc_regions(str):
    data = pd.read_csv(str, header = None,sep='\t')
    data=np.array(data)
    acc_cond=data[:,1]<0.5
    indx=[i for i, x in enumerate(acc_cond) if x]
    today=map(lambda x:x+1,indx)
    final_range=[]
    
    
    for k, g in groupby(enumerate(today), lambda x:x[1]-x[0]):
        ranges = []
        group = list(map(itemgetter(1), g))
        ranges.append(group[0])
        ranges.append(group[-1])
        final_range.append(ranges)
    return final_range
 
 
 
def remove_same_nucl_reg(array):
 x=np.diff(array)
 idx=np.where(x==0)
 idx=idx[0]
 array=np.delete(array,idx,0);
 return array


def cal_acc_energy(array,maximal_span,str_output1,strr):
 acc_seq=[]
 records = list(SeqIO.parse(strr, "fasta"))
 rna_name=records[0].id
 Sequence = records[0].seq
 for i in range(0,len(array)):
 
  s=Sequence[array[i,0]-1:array[i,1]]

  s=str(s)
  acc_seq.append(s)
  w=(len(s)-1);
  w=np.str(w);
  os.system("../src/ParasoR --pre  -w "+w+" -f "+s+" --acc>acc_stem1_t.txt");
  os.system("tail -n +10 acc_stem1_t.txt> jj_t.txt")
  os.system(''' awk '{print $2"\t"$4}' jj_t.txt >acc_stem1_t.txt''')
  os.system("cat acc_stem1_t.txt >> "+str_output1+"")
 return acc_seq,rna_name
  
def acc_inf_lesszero(strs,array):
 df_energy = pd.read_csv(strs,delimiter='\t',header=None)
 df_energy=df_energy.drop(df_energy.columns[0],axis=1)
 df_region=pd.DataFrame(array,columns=['Start','end'])
 indx=np.where(df_energy>1000000)
 indx=indx[0]
 df_energy=df_energy.drop(df_energy.index[indx])
 df_region=df_region.drop(df_region.index[indx])
 indx=np.where(df_energy==0)
 indx=indx[0]
 df_energy=df_energy.drop(df_energy.index[indx])
 df_region=df_region.drop(df_region.index[indx])
 frames=[df_energy,df_region]
 result=pd.concat(frames,axis=1)
 return result,df_energy

 
 
num_lines=int(num_lines/2)
total_acc_energy_query=[];
maximal_span2='5';

RNA_sequence=[];
len_RNA_sequence=[]
records = list(SeqIO.parse(str1, "fasta"))
type_lncrna=[]

for i in range(0,len(records)):
   len_RNA_sequence.append(len(records[i].seq))
   RNA_sequence.append(records[i].id)
    

RNA_sequence=np.array(RNA_sequence)
len_RNA_sequence=np.array(len_RNA_sequence)
#type_lncrna=pd.read_csv("Biotype_lncrintr.txt")
#type_lncrna.columns=['type_lncrna']
#type_lncrna=np.array(type_lncrna)
#type_lncrna=pd.DataFrame(type_lncrna,columns=['type_lncrna'])
 
 
RNA_sequence=pd.DataFrame(RNA_sequence,columns=['RNA_sequence']);      

maximal_span='95'   
os.system("cp "+str1+" copy1.fa")

rel_acc_len_ratio=[]
for i in range(1,num_lines+1):
   os.system("head -2 copy1.fa > copy21.fa && sed -i '1,+1d' copy1.fa")
   parsorr('copy21.fa',str3,maximal_span);
   range_query = acc_regions(str3);
   range_query = np.array(range_query);
   range_query = remove_same_nucl_reg(range_query);
   cal_acc_energy(range_query,maximal_span2,'acc_stem_query1.txt','copy21.fa');
   acc_query_region_energy,query_acc_energy =acc_inf_lesszero('acc_stem_query1.txt',range_query);
   acc_len=np.array((acc_query_region_energy['end']-acc_query_region_energy['Start'])+1)
   j=i-1
   acc_len=acc_len/float(len_RNA_sequence[j])
   rel_acc_len_ratio.append(sum(acc_len))
   os.system("rm acc_stem_query1.txt");
  
rel_acc_len_ratio=pd.DataFrame(rel_acc_len_ratio,columns=['rel_acc_len_ratio']);
str_out=sys.argv[2]

os.system("python basecount.py "+str1+" "+str_out)
composition_data=pd.read_csv(str_out)
frames1=[composition_data['ID'],composition_data['Length'],composition_data['GC%'],rel_acc_len_ratio];
predict_features=pd.concat(frames1,axis=1)

str_rel_out=sys.argv[3]
predict_features.to_csv(str_rel_out,index=False)


#stop = timeit.default_timer()






