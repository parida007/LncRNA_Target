#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import pandas as pd
import numpy as np


# In[17]:


cpc_query = pd.read_csv('cpc2_query.txt', sep="\t", engine="python")
cpc_query.loc[cpc_query.label=='coding','label']='Coding'
cpc_query.loc[cpc_query.label=='noncoding','label']='Non-coding'
cpc_query=cpc_query[['#ID','label']]
cpc_query.columns=['#ID','CPC_label']

cpc_target = pd.read_csv('cpc2_target.txt', sep="\t", engine="python")
cpc_target.loc[cpc_target.label=='coding','label']='Coding'
cpc_target.loc[cpc_target.label=='noncoding','label']='Non-coding'
cpc_target=cpc_target[['#ID','label']]
cpc_target.columns=['#ID','CPC_label']


# In[19]:


plek_query = pd.read_csv('plek_query.txt', sep="\t", engine="python",names=["label", "Scoring", "#ID"])
plek_query['#ID']=plek_query['#ID'].str[1:]
plek_query=plek_query[['#ID','label']]
plek_query.columns=['#ID','PLEK_label']

plek_target = pd.read_csv('plek_target.txt', sep="\t", engine="python",names=["label", "Scoring", "#ID"])
plek_target['#ID']=plek_target['#ID'].str[1:]
plek_target=plek_target[['#ID','label']]
plek_target.columns=['#ID','PLEK_label']


# In[20]:


cpat_query = pd.read_csv('cpat_query.txt', sep="\t", engine="python")
cpat_query.reset_index(inplace=True)
cpat_query.loc[cpat_query.coding_prob<0.364,'label']='Non-coding'
cpat_query.loc[cpat_query.coding_prob>=0.364,'label']='Coding'
cpat_query=cpat_query[['index','label']]
cpat_query.columns=['#ID','CPAT_label']


cpat_target = pd.read_csv('cpat_target.txt', sep="\t", engine="python")
cpat_target.reset_index(inplace=True)
cpat_target.loc[cpat_target.coding_prob<0.364,'label']='Non-coding'
cpat_target.loc[cpat_target.coding_prob>=0.364,'label']='Coding'
cpat_target=cpat_target[['index','label']]
cpat_target.columns=['#ID','CPAT_label']


# In[26]:


cpc_plek=pd.merge(cpc_query,plek_query,on='#ID',how='left')
final_query=pd.merge(cpc_plek,cpat_query,on='#ID')
final_query['Output']='Coding'
final_query.loc[(final_query.CPC_label=='Non-coding')|(final_query.PLEK_label=='Non-coding')|(final_query.CPAT_label=='Non-coding'),'Output']='Non-coding'


# In[28]:


cpc_plek=pd.merge(cpc_target,plek_target,on='#ID',how='left')
final_target=pd.merge(cpc_plek,cpat_target,on='#ID')
final_target['Output']='Non-coding'
final_target.loc[(final_target.CPC_label=='Coding')|(final_target.PLEK_label=='Coding')|(final_target.CPAT_label=='Coding'),'Output']='Coding'


# In[29]:


final_query[['Output']].to_csv('result_query.txt',index=False,header=False)
final_target[['Output']].to_csv('result_target.txt',index=False,header=False)

