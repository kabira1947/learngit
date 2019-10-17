number = int(input("enter a number for table = \n"))
'''print("_____________________________________________")
for i in range(1,10):
    print("{}*{}={}".format(number,i,number*i))
    print("____________________________________________")
print()'''

import math
for u in range(number):
    print("{}*{}={}".format(u,u,u*u))
    print("{}^3={}".format(u,u*u*u))
    print("{}sq.root={}".format(u,math.sqrt(u)))
print()

n=int(input("number please = "))
print("{}*{}={}".format(n,n,n*n))