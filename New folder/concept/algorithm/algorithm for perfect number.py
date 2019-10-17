for n in range(1,1000):
    result=0
    for i in range(1,n):
        if (n%i)==0:
            result=result+i
    if n==result:
        print(n,"this is a perfect number")
    else:
        pass
        #print(n,"this is not a perfect number")