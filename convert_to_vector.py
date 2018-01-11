from encoder import Model
import time
model = Model()
import sys
filename = "def"
f = open(filename)
fh = open(filename+".vectors","w")
line = f.readline()
my_dict = {}
mylist = []
while line:
    x = line.strip()
    mylist.append(x)
    line = f.readline()
f.close()

teXt = model.transform(mylist).reshape(-1)
print(len(teXt))
count = 0
for x in teXt:
    fh.write(str(x))
    fh.write(" ")
    count = count+1
    if count==4096:
        count = 0
        fh.write("\n")
fh.close()
