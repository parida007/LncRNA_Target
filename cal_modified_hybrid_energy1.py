import os
from numpy import *
import numpy as np
import pandas as pd
from itertools import groupby
from operator import itemgetter
from Bio import SeqIO
import timeit

#str1=raw_input('Query File\n')
str1='query.fa'
os.system("cp "+str1+" copy_t.fa")
num_lines = sum(1 for line in open(str1))
num_lines = int(num_lines/2)
#str2=raw_input('Target File\n')
str2='target.fa'
os.system("cp "+str2+" copy1_t.fa")
str_r='temp_t1.txt'
os.system("rm RNAstructure/"+str_r+"");
num_lines1 = sum(1 for line in open(str2))
num_lines1 = int(num_lines1/2)
os.system("rm RNAstructure/final_energy_data.txt")
os.system("rm RNAstructure/final_energy_data.html")
os.system("rm final_energy_data.html")


start = timeit.default_timer() 
for i in range(1,num_lines+1):
 os.system("head -2 copy_t.fa > copy2_t.fa && sed -i '1,+1d' copy_t.fa")
 os.system("cp "+str2+" copy1_t.fa")
 for i in range(1,num_lines1+1):
  os.system("head -2 copy1_t.fa > copy3_t.fa && sed -i '1,+1d' copy1_t.fa")
  #os.system(" (head -1  copy2_t.fa; head -1 copy3_t.fa )>temp1_t.txt")
  #os.system('''awk 'NR%2{printf "%s ",$0;next;}1' temp1_t.txt>temp2_t.txt''')
  #os.system('''paste temp2_t.txt total_acc_energy.txt | column -s $'\t' -t>temp3_t.txt''')
  os.system("python cal_stem.py")
  os.system("mv query_acc1.txt RNAstructure/query_acc1.txt")
  os.system("mv target_acc1.txt RNAstructure/target_acc1.txt")
  os.chdir('RNAstructure/')
  #os.chdir('/home/sibun/ParasoR/script/RNAstructure/')
  os.system("python cal_hybrid.py")
  os.system("cat final_prediction.txt >> final_energy_data.txt")
  os.system("rm final_prediction.txt")
  #os.system('''paste ../temp3_t.txt temp4_t.txt | column -s $'\t'>temp5_t.txt''');
  #os.system("cat temp5_t.txt>>"+str_r+"")
  #os.system("rm ../temp3_t.txt temp4_t.txt temp5_t.txt")
  os.chdir('../')
  #os.chdir('/home/sibun/ParasoR/script/')

stop = timeit.default_timer()
#print "Time complexity ",stop-start

os.system("csv2html -o RNAstructure/final_energy_data.html RNAstructure/final_energy_data.txt")
os.system("sed -i 's/&lt;br&gt;/<br>/g' RNAstructure/final_energy_data.html")
os.system("sed -i 's/<br>/\\n/g' RNAstructure/final_energy_data.txt")
os.system("cp RNAstructure/final_energy_data.txt final_energy_data.txt")




os.system("mv RNAstructure/final_energy_data.html final_energy_data.html")


with open('final_energy_data.html', 'a') as f:
 f.write("<a download href="+"'final_energy_data.txt'"+"> Download results as txt file</a>")
 f.write("<br/><br/>")
 f.write("<a href='Cleaning_Ops_1.php'>Go to Home Page</a>")




#os.chdir('/home/bose/Downloads/ParasoR/script/RNAstructure/')
#os.system("sed 's/[>]//g' "+str_r+"");
#os.system('''sed '1i lncRNA mRNA\tAcc_Energy(lncRNA)\tAcc_Energy(mRNA)\tHybridization_Energy\tInteraction_energy' query_seq_target.txt''')
