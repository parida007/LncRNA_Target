import psutil
import sys

f = open('IS_RUNNING.txt', "w")
flag=0
for process in psutil.process_iter():
    if process.cmdline() == ['python', 'Main.py']:
        flag=1
        break
if flag==1:
    f.write('YES')
else:
    f.write('NO')

f.close()