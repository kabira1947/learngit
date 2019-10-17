
def read1():
    f=open("likun.txt", "r")
    str=f.readlines()
    count=0
    for i in str:
        count+=1
        print(count,i[::-1], end=" ")

read1()


