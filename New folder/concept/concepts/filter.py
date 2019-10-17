
a=[2,34,3,28,4,21]

#1

print(list(filter(lambda x:x>3,a)))
print([x>3 for x in a])
print([x for x in a if x>3])

#2

print(list(filter(lambda x:x%2==0,a)))
print([x for x in a if x%2==0])
