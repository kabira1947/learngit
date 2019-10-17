import os
import sys
f=input("enter file name: ")

if os.path.exists(f):
    p=open(f,"r")
else:
    print("file {} does not exists".format(f))
    sys.exit()
def word():
    cl=0
    cw=0
    cc=0

    for line in p:
        words=line.split()
        cl+=1
        cw+= len(words)
        cc+= len(line)
    print("characters:- ",cc," Words:- ",cw," lines:-",cl)


word()
p.close()