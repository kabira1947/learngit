n=int(input("print the number = "))
for i in range(n):
    for j in range(n):
        if i==j or i==(j-1) or j==0:
            print("*",end="")
        else:
            print(end=" ")
    print()

num= int(input("print the number = "))

for i in range(num):
    for j in range(num):
        if i == j or i== j-1 or j == 0:
            print("#", end="")
    print()