for n in range(2,100):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print(n)
                break
        else:
            pass
    else:
        print( "special")