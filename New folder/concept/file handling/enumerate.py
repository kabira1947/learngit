f=open("likun.txt","r")
str=f.readlines()

for i in enumerate((str),1):
    print(i,end=" ")

for i in reversed(str):
    print(i,end="")
