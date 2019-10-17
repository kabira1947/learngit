my_list = [1, 3, 6, 10]

a= [x**2 for x in my_list] # array
print(a)
b= (x**2 for x in my_list) # cul
print(b)

print(next(b))
print(next(b))

print(sum(my_list))
print(max(my_list))

print(max(x**2 for x in my_list))
print(min(x**-1 for x in my_list))