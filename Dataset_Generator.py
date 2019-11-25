import pandas as pd
import numpy as np

out2=pd.read_csv('out2.csv',sep='\t')
lncrna=pd.read_csv('LNCRNA_Rel_Composition.csv')
mrna=pd.read_csv('MRNA_Rel_Composition.csv')

drop_cols=['acc_energy_lncrna(kcal/mol)','acc_energy_mrna(kcal/mol)',
       'int_energy(kcal/mol)', 'segment_count',
       'mrna_rel_GC_ratio']

out2.drop(drop_cols,axis=1,inplace=True)


out2.columns=['lncrna', 'mrna', 'hybrid_energy(kcal/mol)','lncrna_rel_GC_ratio']

lncrna.columns=['lncrna','lncrna-length','lncrna-GC%','lncrna-rel_acc_len_ratio']

mrna.columns=['mrna','mrna-length','mrna-GC%','mrna-rel_acc_len_ratio']

lnc_m_props=lncrna.assign(key=1).merge(mrna.assign(key=1),on='key').drop('key', 1)

final_dataset=pd.merge(lnc_m_props,out2,on=['lncrna','mrna'])


new_col=['lncrna','mrna', 'lncrna-length','mrna-length', 'lncrna-GC%','mrna-GC%', 
                    'lncrna-rel_acc_len_ratio','mrna-rel_acc_len_ratio','hybrid_energy(kcal/mol)', 'lncrna_rel_GC_ratio']
final_dataset=final_dataset.reindex(columns=new_col)

final_dataset.columns=['lncrna','mrna', 'lncrna-length','mrna-length', 'lncrna-GC%','mrna-GC%', 
                    'lncrna_relative_accessible_length_ratio','mrna_relative_accessible_length_ratio','hybrid_energy(kcal/mol)', 'lncrna_relative_GC_ratio']


final_dataset.to_csv('Input_ML.csv',index=False)
