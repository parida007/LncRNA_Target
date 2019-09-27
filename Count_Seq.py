fo = open("query.fa", "r")
count_q_seq=0
for x in fo:
    if str.startswith(x,'>'):
        count_q_seq+=1
        
fw=open('count_q_seq.txt','w')
fw.write(str(count_q_seq))
fw.close()
fo.close()




fo = open("target.fa", "r")
count_t_seq=0
for x in fo:
    if str.startswith(x,'>'):
        count_t_seq+=1
        
fw=open('count_t_seq.txt','w')
fw.write(str(count_t_seq))
fw.close()
fo.close()






