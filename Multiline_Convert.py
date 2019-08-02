import sys

file_name=sys.argv[1]
fileHandler = open (file_name, "r")
listOfLines = fileHandler.readlines()
fileHandler.close()

final=''
indiv=''
for line in listOfLines:
    if(line.startswith('>')):
        final+=indiv
        indiv='\n'
        indiv+=line
        continue
    else:
        indiv+=line.strip()
final+=indiv
final=final[1:]

f = open(file_name, "w")
f.write(final)
f.close()