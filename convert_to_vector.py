from encoder import Model
import time


model = Model()

import sys

filename = "test_text"

f = open(filename)

fh = open(filename+".vectors","w")

line = f.readline()
my_dict = {}
while line:
    x = line.strip()
    if x in my_dict:
    	print("duplicate")
    	print(x)
    	vectorOutput = my_dict[x]
    	fh.write(vectorOutput.strip())
    	fh.write("\n")
    	line = f.readline()
    	continue
    mylist = []
    mylist.append(x)
    teXt = model.transform(mylist).reshape(-1)
    vectorOutput = " ".join(str(x) for x in teXt)

    #for x in teXt:
    #	fh.write(str(x))
    #	fh.write(" ")
    fh.write(vectorOutput.strip())
    fh.write("\n")
    my_dict[x] = vectorOutput

    line = f.readline()
f.close()
fh.close()