#n=int(input("please enter a number to check prime = "))
for n in range(100,1099):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                #print(n,"number is not prime")
                break
        else:
            #print(n," is prime number")
            print(n)
    else:
       # print(n,"not a prime number")
        print(n)

