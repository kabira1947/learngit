
#1
'''n= int(input("enter the number: "))
a= list(range(1,n+1))

print(" The number:- ",n)

print("Array :- ",str(a))

print("Reverse array:- ",a[::-1])
print("print the number in order:- ")

for i in a:
    print(i, end=" ")

print()
print("print the numbers in reversed order:- ")
for i in reversed(a):
    print(i, end=" ")
'''
n=int(input())
a=[int(x) for x in input().split()]
for i in reversed(a):
     print(i, end=" ")


print("")