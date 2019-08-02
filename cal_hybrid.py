import os
from numpy import *
import numpy as np
import pandas as pd
from itertools import groupby
from operator import itemgetter
from Bio import SeqIO
import operator
import itertools
from operator import itemgetter, attrgetter
os.environ['DATAPATH']='/home/bose/Downloads/ParasoR/script/RNAstructure/data_tables'
os.environ['PATH']='/home/bose/perl5/bin:/bin:/usr/bin:/usr/X11R6/bin:/usr/local/bin:/home/bose/Downloads/ParasoR/script/RNAstructure/exe/'

#str_r=raw_input("hybridization_file\t")
str_r='hybrid_query_target.ct'
str6='final_prediction.txt'
os.system("rm "+str_r+"")
os.system("rm "+str6+"")


os.system("rm hybrid1.dot")
query_data=pd.read_csv('query_acc1.txt',delimiter='\t',header=None)
target_data=pd.read_csv('target_acc1.txt',delimiter='\t',header=None)
query_rna_segment=query_data.ix[:,4]
target_rna_segment=target_data.ix[:,4]
query_rna_segment=np.array(query_rna_segment)
target_rna_segment=np.array(target_rna_segment)

def hybrid_bifold(array,array1):
 for i in range(1,len(array)):
  h=np.str(i)
  f = open( 'query_seq_acc.txt', 'w' )
  f.write('>header-'+h+'\n'+array[i])
  f.close()
  for j in range(1,len(array1)):
   h=np.str(j)
   k = open( 'target_seq_acc.txt', 'w' )
   k.write('>target-'+h+'\n'+array1[j])
   k.close()
   os.system("bifold query_seq_acc.txt target_seq_acc.txt --intramolecular target_query.ct")
   os.system("ct2dot target_query.ct 1 hybrid.dot")
   os.system("cat target_query.ct >> "+str_r+"")
   os.system("cat hybrid.dot >> hybrid1.dot")
 os.system("grep ENERGY "+str_r+" >hybrid_energy.txt")
 os.system("grep -A2 -P '>ENERGY' hybrid1.dot >hybrid2.dot")
 hybrid_data=pd.read_csv('hybrid_energy.txt',delimiter='_| |-',header=None, engine='python')
 #hybrid_data=pd.read_csv('hybrid_energy.txt',delimiter='_| |-',header=None)
 hybrid_data=np.array(hybrid_data);
 hybrid_data1=np.delete(hybrid_data, [0,1,2,3,4,6,7,9], axis=1)
 return hybrid_data1;
#os.system("export DATAPATH='/media/bose/Ghoshlab_2015/Backup_4TB/ParasoR/script/RNAstructure/data_tables'")


hybrid_data2=hybrid_bifold(query_rna_segment,target_rna_segment);
hybrid_data2=pd.DataFrame(hybrid_data2,columns=['energy','query_seg','tar_seg'])
hybrid_data2=hybrid_data2.sort_values(['energy'],ascending=[0])
#hybrid_data2=hybrid_data2.sort(['energy'],ascending=[0])
query_seg_grp=hybrid_data2.groupby(['query_seg']).head(1)
hybrid_data2=query_seg_grp.groupby(['tar_seg']).head(1)
hybrid_data2['energy']=-(hybrid_data2['energy'])
hybrid_energy=(hybrid_data2['energy'].sum())

access_data=pd.read_csv('../total_acc_energy.txt',delimiter='\t',header=None,names=['lncrna','mrna','acc_energy_lncrna(kcal/mol)','acc_energy_mrna(kcal/mol)'])
int_energy=sum(access_data,axis=1)+hybrid_energy
hybrid_energy=pd.DataFrame([hybrid_energy],columns=['hybrid_energy(kcal/mol)'])
int_energy=pd.DataFrame(int_energy,columns=['int_energy(kcal/mol)'])
energy_data=pd.concat([access_data,hybrid_energy,int_energy],axis=1)

acc_seg=hybrid_data2.ix[:,'query_seg':'tar_seg']
query_seg=np.array(acc_seg.ix[:,'query_seg'])
tar_seg=np.array(acc_seg.ix[:,'tar_seg'])
query_seg=[str(i) for i in query_seg]
tar_seg=[str(i) for i in tar_seg]

dot_bracket=[]
hyb_seq=[]
str_seq=[]
for i in range(len(query_seg)):
 y='header-'+query_seg[i]+'_target-'+tar_seg[i]
 u=os.popen("grep "+y+" -A2 hybrid2.dot").read()
 u=u.split('\n')
 dot_bracket.append(u[2])
 hyb_seq.append(u[1])
 str_seq.append(u[1])
 str_seq.append(u[2])
 
p=[ '<br>'.join(x) for x in zip(str_seq[0::2], str_seq[1::2]) ]

str_seq=p

start_end_query=query_data.ix[acc_seg.ix[:,'query_seg'],2:3]
start_end_target=target_data.ix[acc_seg.ix[:,'tar_seg'],2:3]

del hybrid_data2['query_seg']
del hybrid_data2['tar_seg']

hybrid_data2=np.array(hybrid_data2)
start_end_query=np.array(start_end_query)
start_end_target=np.array(start_end_target)
#dot_bracket=np.array(dot_bracket)

hybrid_data2=np.concatenate([start_end_query,start_end_target,hybrid_data2],axis=1)
hybrid_data2=pd.DataFrame(hybrid_data2,columns=['start_query','end_query','start_target','end_target','hybrid_energy(kcal/mol)'])



dot_bracket=pd.DataFrame(str_seq,columns=['structure']) 

hybrid_data2=pd.concat([hybrid_data2,dot_bracket],axis=1)


energy_data.to_csv(str6, encoding='utf-8',sep=',',index=None)
with open(str6,'a') as f:
    f.write('\n')

hybrid_data2.to_csv(str6,encoding='utf-8',sep=',',mode='a')

with open(str6,'a') as f:
    f.write('\n')


#os.system("csv2html -o final_energy_data.html final_prediction.txt")
#os.system("sed -i 's/&lt;br&gt;/<br>/g' final_energy_data.html")
#os.system("sed -i 's/<br>/\\n/g' final_prediction.txt")

#with open('final_energy_data.html', 'a') as f:
# f.write(energy_data.to_html(classes='energy_data',index=False))
# f.write("<br />")
# f.write(hybrid_data2.to_html(classes='hybrid_data2',index=False))
# f.write("<br />")



#o=np.array(hybrid_data2)
#o=pd.DataFrame(o)
#second_struct=np.where(o.duplicated([1,2]))


#print "hybrid_energy = ",hybrid_energy,"\ninteraction_energy = ",int_energy
#def int_energy1(array2):
 #query_segment=[];
 #for key, group in itertools.groupby(array2, key=lambda x:x[1]):
  #query_segment.append(list(group))
 #high_energy=[]
 #high_energy1=[]
 #query_segment=np.array(query_segment) 
 #for i in range(0,len(query_segment)):
  #r=np.array(query_segment[i])
  #r=sorted(r, key=operator.itemgetter(0), reverse=True)
  #high_energy.append(r[:2])
 #high_energy1=sum(high_energy,axis=1)
 #high_energy1=np.array(high_energy1)
 #..r,t,c=high_energy1.shape
 #..high_energy1=high_energy1.reshape(r,c)
 #high_energy1=high_energy1.astype(float)
 #target_segment=pd.DataFrame(high_energy1)
 #uniq_tar_seg=np.unique(high_energy1[:,2])
 #group_tar_seg=target_segment.groupby(2)
 #hybrid_energy=[]
 #for i in range(len(uniq_tar_seg)):
  #o=group_tar_seg.get_group(uniq_tar_seg[i])
  #hybrid_energy.append(o[0].max())
 #hybrid_energy=sum(hybrid_energy)
 #hybrid_energy=-(hybrid_energy)
 #print "hybrid_energy = ",hybrid_energy
 #accessible_data=np.loadtxt('../total_acc_energy.txt')
 #int_energy=sum(accessible_data)+hybrid_energy
 #print "interaction_energy = ",int_energy
 #g=np.vstack([hybrid_energy,int_energy])
 #g=np.transpose(g)
 #np.savetxt('temp4.txt',g,delimiter='\t',fmt='%f')
 #return int_energy;

#interaction_energy=int_energy1(hybrid_data2);

#target_segment=[];
#for key, group in itertools.groupby(high_energy1, key=lambda x:x[2]):
# target_segment.append(list(group))
 
#len_tar_seg=[]
#for i in range(len(target_segment)):
# len_tar_seg.append(len(target_segment[i]))

#target_segment=np.array(target_segment);
#len_tar_seg=np.array(len_tar_seg);
#indx=len_tar_seg>1
#indx=[i for i, x in enumerate(indx) if x]
#indx=np.array(indx)
#target_segment1=target_segment[indx] 

#target_segment2=np.delete(target_segment,indx,axis=0)
 
 
#high_energy2=[]
#for i in range(len(target_segment1)):
# r=np.array(target_segment1[i])
# r=sorted(r, key=operator.itemgetter(0), reverse=True)
# high_energy2.append(r[:1])
 
#high_energy2=np.array(high_energy2)
#high_energy2=high_energy2.reshape(229,3)
#high_energy2=high_energy2.astype(float)
#unique_high_energy2=np.unique(high_energy2,axis=0)
#high_energy3=sum(unique_high_energy2[:,0])
