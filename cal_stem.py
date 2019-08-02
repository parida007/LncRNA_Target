import os
from numpy import *
import numpy as np
import pandas as pd
from itertools import groupby
from operator import itemgetter
from Bio import SeqIO

os.system("rm acc_stem_query1.txt");
os.system("rm acc_stem_target1.txt");

#str1=raw_input('Query File\n')
str1='copy2_t.fa'

#str2=raw_input('Target File\n')
str2='copy3_t.fa'
#str3=raw_input('Output for query stem probability\n')
str3='query_stem_t.txt'
#str4=raw_input('Output for target stem probability\n')
str4='target_stem_t.txt'
#str5=raw_input('Output for acc_energy of query\n')
str5='query_acc1.txt'
#str6=raw_input('Output for acc_energy of target\n')
str6='target_acc1.txt'
#maximal_span=raw_input('maximal bair span constraint for query\n')
maximal_span=loadtxt('max_base_span.txt')
maximal_span=np.int(maximal_span)
maximal_span=np.str(maximal_span)
#maximal_span='95'
#maximal_span1=raw_input('maximal bair span constraint for target\n')
maximal_span1=maximal_span

#maximal_span2=raw_input('maximal bair span constraint for segment\n')
maximal_span2='5'

import timeit


def parsorr(str,str_output,maximal_span):
 import os
 os.system("../src/ParasoR --pre --constraint "+maximal_span+" --input "+str+" --stem > "+str_output+"")
 os.system("tail -n +10 "+str_output+" > jj_t.txt")
 os.system(''' awk '{print $2"\t"$4}' jj_t.txt >input21_t.txt''')
 os.system("mv input21_t.txt "+str_output+"");
 
 #os.system("tail -n +9 input.txt > jj.txt")
 #os.system(''' awk '{print $2"\t"$4}' jj.txt >input21.txt''')
 return [];

def acc_regions(str):
 data = pd.read_csv(str, header = None,sep='\t')
 data=np.array(data)
 acc_cond=data[:,1]<0.5
 indx=[i for i, x in enumerate(acc_cond) if x]
 today=map(lambda x:x+1,indx)
 #print(today)
 ranges = []
 #for k, g in groupby(enumerate(indx), lambda (i,x):i-x):
 for k, g in groupby(enumerate(today), lambda (i,x):i-x):
     group = map(itemgetter(1), g)
     ranges.append((group[0], group[-1]))	
 return ranges
 
 
 
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

def acc_inf_lesszero(strs,array,array1):
 df_energy = pd.read_csv(strs,delimiter='\t',header=None)
 df_energy=df_energy.drop(df_energy.columns[0],axis=1)
 df_energy.columns=['Accessible_energy']
 df_region=pd.DataFrame(array,columns=['Start','end'])
 df_sequence=pd.DataFrame(array1,columns=['RNA_segment'])
 indx=np.where(df_energy>1000000)
 indx=indx[0]
 df_energy=df_energy.drop(df_energy.index[indx])
 df_region=df_region.drop(df_region.index[indx])
 df_sequence=df_sequence.drop(df_sequence.index[indx])
 #print(df_energy)
 #print(df_sequence)
 indx=np.where(df_energy==0)
 indx=indx[0]
 df_energy=df_energy.drop(df_energy.index[indx])
 df_region=df_region.drop(df_region.index[indx])
 df_sequence=df_sequence.drop(df_sequence.index[indx])
 frames=[df_energy,df_region,df_sequence]
 result=pd.concat(frames,axis=1)
 return result,df_energy


start = timeit.default_timer() 
parsorr(str1,str3,maximal_span);
parsorr(str2,str4,maximal_span1);

range_query = acc_regions(str3);
#print(range_query)
range_target= acc_regions(str4);
range_query = np.array(range_query);
range_target = np.array(range_target);
range_query = remove_same_nucl_reg(range_query);
range_target = remove_same_nucl_reg(range_target);

acc_seq_query,lncrna=cal_acc_energy(range_query,maximal_span2,'acc_stem_query1.txt',str1);
acc_seq_query=np.array(acc_seq_query);
#print(acc_seq_query)
acc_seq_target,mrna=cal_acc_energy(range_target,maximal_span2,'acc_stem_target1.txt',str2);
acc_seq_target=np.array(acc_seq_target);
acc_query_region_energy,query_acc_energy =acc_inf_lesszero('acc_stem_query1.txt',range_query,acc_seq_query);
#print(acc_query_region_energy)
#print(query_acc_energy)
acc_target_region_energy,target_acc_energy =acc_inf_lesszero('acc_stem_target1.txt',range_target,acc_seq_target);
acc_query_region_energy.to_csv(str5, encoding='utf-8',sep='\t')
acc_target_region_energy.to_csv(str6, encoding='utf-8',sep='\t')

total_acc_energy_query=query_acc_energy.values.sum()
#print(total_acc_energy_query)
total_acc_energy_target=target_acc_energy.values.sum()

total_acc_energy_query=np.array(total_acc_energy_query)
total_acc_energy_target=np.array(total_acc_energy_target)
lncrna=np.array(lncrna)
mrna=np.array(mrna)
g=np.vstack([lncrna,mrna,total_acc_energy_query,total_acc_energy_target])
g=np.transpose(g)
np.savetxt('total_acc_energy.txt',g,delimiter='\t',fmt='%s')

stop = timeit.default_timer()
print "Time complexity ",stop-start



#range_query_output=pd.DataFrame(range_query,columns=['Start','end'])
#range_target_output=pd.DataFrame(range_target,columns=['Start','end'])

#df = pd.read_csv('acc_stem_query.txt',delimiter='\t',header=None)
#rangee=acc_threshold('acc_stem_query.txt',range_query);
#print len(rangee);
#print len(range_query)
#print len(df)

#rangee=pd.DataFrame(rangee);
#rangee.to_csv('jj.txt',sep='\t')
#result=acc_threshold('acc_stem_target.txt',range_target);

#result1.to_csv('query_acc_regions.txt', encoding='utf-8',sep='\t')
#result2.to_csv('target_acc_regions.txt', encoding='utf-8',sep='\t')


#range_query_output.to_csv('query_acc_regions.txt', encoding='utf-8',sep='\t')
#range_target_output.to_csv('target_acc_regions.txt', encoding='utf-8',sep='\t')

