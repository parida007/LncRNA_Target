import os
from numpy import *
import numpy as np
import pandas as pd
from Bio import SeqIO
import sys

str1=sys.argv[1]
str2=sys.argv[2]

input_file = open(str1, 'r') 
output_file=pd.DataFrame(columns=['ID','Length','GC%'])
i=0

for cur_record in SeqIO.parse(input_file, "fasta") :
    gene_name = cur_record.name
    A_count = cur_record.seq.count('A') 
    C_count = cur_record.seq.count('C') 
    G_count = cur_record.seq.count('G') 
    T_count = cur_record.seq.count('T') 
    length = len(cur_record.seq) 
    #print(length)
    cg_percentage = (C_count + G_count) / length
    at_percentage=1-cg_percentage
    output_file.loc[i,'ID']=gene_name
    output_file.loc[i,'Length']=length
    output_file.loc[i,'GC%']=cg_percentage
    i=i+1

output_file.to_csv(str2,index=False)