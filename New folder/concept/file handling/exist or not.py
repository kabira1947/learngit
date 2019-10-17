import os,sys

f=input("enter the file name: ")

if os.path.exists(f):
    p=open(f,"r")
else:
    print("The file {} doesn't exists".format(f))
    sys.exit()

str = p.read()

print(str)

p.close()
