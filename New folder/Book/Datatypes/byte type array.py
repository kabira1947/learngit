nums=[10,23,43,56,51]

A=bytearray(nums)

print(A)

for i in A:
    print(i)

# modify array


A[0]= 88
A[1]= 90

print(A)
for i in A:
    print(i)