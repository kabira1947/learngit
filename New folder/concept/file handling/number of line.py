def numline():
    f = open("likun.txt", "r")
    str=f.readlines()
    print(len(str))
    count=0
    for line in str:
        count+=1
        print(count,line,end="")
    print(count,end=" ")
numline()

